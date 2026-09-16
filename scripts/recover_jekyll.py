#!/usr/bin/env python3
"""Convert posts from the archived Jekyll blog into Hugo content files.

The original source of blog.basilesimon.fr survives at
github.com/basilesimon/archive-blog. This reads posts from a checkout of that
repo and writes content/<section>/<slug>.md, copying referenced images into
static/assets/ — falling back to `git show` against the archive's history for
images that are no longer in its worktree.

Which posts to convert comes from the checklists in IMPLEMENTATION_PLAN.md,
which also supply each post's historical URL (used as the Hugo alias).

See IMPLEMENTATION_PLAN.md, stages 2-3.
"""

import argparse
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(REPO, "IMPLEMENTATION_PLAN.md")

# Images live in these directories of the archive, in priority order.
ASSET_DIRS = ("_assets", "_attachments")

IMG_RE = re.compile(
    r"""(?:src=["']|\]\(|url\()\s*([^"')]+?\.(?:png|jpe?g|gif|svg|webp))""",
    re.I,
)
PLAN_ENTRY_RE = re.compile(
    r"- \[[ x]\] `(\d{4}-\d{2}-\d{2})` \*\*(.+?)\*\*.*?— `(/\S+?)`"
)


# --------------------------------------------------------------------------
# archive source
# --------------------------------------------------------------------------


def git(archive, *args):
    """Run git in the archive checkout, returning stdout (text)."""
    return subprocess.run(
        ["git", "-C", archive, *args], capture_output=True, text=True
    ).stdout


def history_paths(archive):
    """Map basename -> paths that ever existed in the archive's history."""
    out = {}
    for line in git(archive, "log", "--all", "--pretty=format:", "--name-only").split("\n"):
        line = line.strip()
        if line:
            out.setdefault(os.path.basename(line), set()).add(line)
    return out


def read_from_history(archive, path):
    """Recover a file's last known contents from git history, or None."""
    rev = git(archive, "rev-list", "--all", "-1", "--", path).strip()
    if not rev:
        return None
    for spec in (f"{rev}:{path}", f"{rev}^:{path}"):
        blob = subprocess.run(
            ["git", "-C", archive, "show", spec], capture_output=True
        )
        if blob.returncode == 0 and blob.stdout:
            return blob.stdout
    return None


def source_posts(archive):
    """Map slug -> (directory, filename, date) for every post in the archive."""
    out = {}
    for d in ("_posts", "_archive"):
        for f in sorted(os.listdir(os.path.join(archive, d))):
            m = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.(md|html)$", f)
            if m:
                out.setdefault(m.group(2), (d, f, m.group(1)))
    return out


# --------------------------------------------------------------------------
# frontmatter
# --------------------------------------------------------------------------


def split_frontmatter(text):
    """Split a Jekyll file into (frontmatter text, body)."""
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    return parts[1], parts[2]


def parse_frontmatter(fm):
    """Parse the small subset of YAML Jekyll actually uses here.

    Handles `key: scalar` and `key:` followed by an indented `- item` list.
    That covers every key present across the 276 archived posts.
    """
    data = {}
    key = None
    for raw in fm.split("\n"):
        if not raw.strip():
            continue
        item = re.match(r"^\s+-\s*(.*)$", raw)
        if item and key:
            value = unquote(item.group(1).strip())
            if value:
                data.setdefault(key, [])
                if isinstance(data[key], list):
                    data[key].append(value)
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if m:
            key, value = m.group(1), m.group(2).strip()
            data[key] = unquote(value) if value else None
    return data


def unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def yaml_quote(value):
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


# --------------------------------------------------------------------------
# body rewriting
# --------------------------------------------------------------------------


def rewrite_liquid(body):
    """Drop Jekyll's site-root Liquid so paths become site-absolute.

    Must run before pandoc, which would otherwise URL-encode the braces.
    """
    return re.sub(r"\{\{\s*site\.(?:url|baseurl)\s*\}\}", "", body)


def rewrite_highlight(body):
    """Turn Jekyll's {% highlight lang %} blocks into fenced code blocks."""
    body = re.sub(r"\{%\s*highlight\s+(\w+)[^%]*%\}", r"```\1", body)
    body = re.sub(r"\{%\s*highlight\s*%\}", "```", body)
    return re.sub(r"\{%\s*endhighlight\s*%\}", "```", body)


def fix_tight_headings(body):
    """kramdown accepted `##Heading`; Goldmark needs a space after the hashes.

    Skips fenced code, where a leading `#` is a comment rather than a heading.
    """
    parts = re.split(r"(```.*?```)", body, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"^(#{1,6})(?=[^\s#])", r"\1 ", parts[i], flags=re.M)
    return "".join(parts)


def rewrite_urls(body, linkmap):
    """Point old-domain asset and post URLs at their current location."""
    body = re.sub(
        r"https?://blog\.basilesimon\.fr/wp-content/uploads/(?:\d{4}/\d{2}/)?",
        "/assets/",
        body,
    )
    body = re.sub(r"https?://(?:blog\.)?basilesimon\.fr/assets/", "/assets/", body)

    def post_link(m):
        path = "/" + m.group("path").strip("/") + "/"
        return linkmap.get(path, path)

    # Links to posts on the dead subdomain, and bare old-style paths.
    body = re.sub(
        r"https?://blog\.basilesimon\.fr/(?P<path>\d{4}/\d{2}(?:/\d{2})?/[^\s)\"'<>]+?)/?(?=[\s)\"'<>]|$)",
        post_link,
        body,
    )
    body = re.sub(
        r"(?<=\()(?P<path>/\d{4}/\d{2}(?:/\d{2})?/[^\s)\"'<>]+?)/?(?=\))",
        post_link,
        body,
    )
    return body


def html_to_markdown(body):
    """Convert WordPress-era HTML bodies to Markdown.

    `gfm` alone silently drops <iframe> embeds, so raw_html is required on both
    sides to keep the Twitter/infogr.am/YouTube embeds intact.
    """
    out = subprocess.run(
        ["pandoc", "-f", "html+raw_html", "-t", "gfm+raw_html", "--wrap=none"],
        input=body,
        capture_output=True,
        text=True,
    )
    if out.returncode != 0:
        raise RuntimeError(f"pandoc failed: {out.stderr.strip()}")
    return out.stdout


def excerpt(body, limit=155):
    """First prose sentence(s) of a post, for the `description` frontmatter."""
    text = re.sub(r"<[^>]+>", " ", body)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[#>*_`]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    cut = text[:limit]
    return cut[: cut.rfind(" ")].rstrip(" ,;:-") + "…"


# --------------------------------------------------------------------------
# conversion
# --------------------------------------------------------------------------


def convert(slug, entry, archive, src, hist, section, linkmap, stats):
    date, _title, old_url = entry
    directory, filename, file_date = src[slug]
    path = os.path.join(archive, directory, filename)
    raw = open(path, encoding="utf-8", errors="replace").read()
    fm_text, body = split_frontmatter(raw)
    fm = parse_frontmatter(fm_text)

    body = rewrite_liquid(body)
    body = rewrite_highlight(body)
    if filename.endswith(".html"):
        body = html_to_markdown(body)
    else:
        body = fix_tight_headings(body)
    body = rewrite_urls(body, linkmap)
    body = body.strip() + "\n"

    images = copy_images(body, archive, hist, stats)

    # The filename date is the real publication day; the plan's date is derived
    # from the URL, which for WordPress-era posts only carries year and month.
    aliases = [old_url if old_url.endswith("/") else old_url + "/"]
    permalink = fm.get("permalink")
    if permalink and permalink.rstrip("/") + "/" not in aliases:
        aliases.append(permalink.rstrip("/") + "/")

    lines = ["---"]
    lines.append(f"aliases: [{', '.join(yaml_quote(a) for a in aliases)}]")
    lines.append(f'date: "{file_date}T00:00:00Z"')
    description = fm.get("description") or excerpt(body)
    if description:
        lines.append(f"description: {yaml_quote(description)}")
    image = fm.get("image")
    if image:
        image = re.sub(
            r"https?://(?:blog\.)?basilesimon\.fr/assets/", "/assets/", image
        )
        lines.append(f"image: {yaml_quote(image)}")
    tags = fm.get("tags")
    if isinstance(tags, str):
        tags = [tags]
    tags = [t.lower() for t in (tags or []) if t.lower() != "non classé"]
    lines.append(f"tags: [{', '.join(tags)}]")
    lines.append(f"title: {yaml_quote(fm.get('title') or slug)}")
    if str(fm.get("published")).lower() == "false":
        lines.append("draft: true")
        stats["drafts"].append(slug)
    lines.append("---")
    lines.append("")

    out_path = os.path.join(REPO, "content", section, slug + ".md")
    return out_path, "\n".join(lines) + body, images


def copy_images(body, archive, hist, stats):
    """Copy every site-hosted image a post references into static/assets/."""
    copied = []
    for ref in IMG_RE.findall(body):
        ref = ref.strip()
        if re.match(r"https?://", ref):
            continue
        name = os.path.basename(ref.split("?")[0])
        dest = os.path.join(REPO, "static", "assets", name)
        if os.path.exists(dest):
            copied.append(name)
            continue
        data = None
        for d in ASSET_DIRS:
            candidate = os.path.join(archive, d, name)
            if os.path.exists(candidate):
                data = open(candidate, "rb").read()
                break
        if data is None:
            for p in sorted(hist.get(name, [])):
                data = read_from_history(archive, p)
                if data:
                    stats["from_history"].append(name)
                    break
        if data is None:
            stats["missing_images"].append(name)
            continue
        with open(dest, "wb") as fh:
            fh.write(data)
        copied.append(name)
    return copied


# --------------------------------------------------------------------------
# plan + link map
# --------------------------------------------------------------------------


def plan_entries(stage):
    """Parse a stage's checklist from IMPLEMENTATION_PLAN.md."""
    text = open(PLAN, encoding="utf-8").read()
    section = text.split(f"## Stage {stage}")[1].split(f"## Stage {stage + 1}")[0]
    return {
        url.strip("/").split("/")[-1]: (date, title, url)
        for date, title, url in PLAN_ENTRY_RE.findall(section)
    }


def build_linkmap(entries, section):
    """Map every historical post URL to where that post lives now."""
    linkmap = {}
    for slug, (_d, _t, url) in entries.items():
        linkmap["/" + url.strip("/") + "/"] = f"/{section}/{slug}/"
    # Posts already migrated carry their old URLs in `aliases:`.
    for sec in ("blog", "weeknotes"):
        d = os.path.join(REPO, "content", sec)
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if not f.endswith(".md"):
                continue
            head = open(os.path.join(d, f), encoding="utf-8", errors="replace").read(600)
            m = re.search(r"^aliases:\s*\[(.+?)\]", head, re.M)
            if m:
                for alias in re.findall(r'"([^"]+)"', m.group(1)):
                    linkmap["/" + alias.strip("/") + "/"] = f"/{sec}/{f[:-3]}/"
    return linkmap


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--archive", required=True, help="path to an archive-blog checkout")
    ap.add_argument("--stage", type=int, default=3, help="plan stage to convert")
    ap.add_argument("--section", default="blog", help="content/<section> to write into")
    ap.add_argument("--only", nargs="*", help="convert just these slugs")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    entries = plan_entries(args.stage)
    src = source_posts(args.archive)
    hist = history_paths(args.archive)
    linkmap = build_linkmap(entries, args.section)
    stats = {"drafts": [], "from_history": [], "missing_images": [], "written": []}

    todo = args.only or sorted(entries)
    for slug in todo:
        if slug not in entries:
            print(f"  !! {slug}: not in the stage {args.stage} checklist", file=sys.stderr)
            continue
        if slug not in src:
            print(f"  !! {slug}: no source file in the archive", file=sys.stderr)
            continue
        out_path, text, images = convert(
            slug, entries[slug], args.archive, src, hist, args.section, linkmap, stats
        )
        if os.path.exists(out_path) and not args.only:
            print(f"  -- {slug}: already exists, skipped", file=sys.stderr)
            continue
        stats["written"].append(slug)
        if args.dry_run:
            print(f"===== {out_path} ({len(images)} images) =====\n{text}")
        else:
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(text)

    print(f"\nwrote {len(stats['written'])} posts into content/{args.section}/")
    print(f"images recovered from git history: {len(set(stats['from_history']))}")
    if stats["drafts"]:
        print(f"marked draft (published: false in Jekyll): {len(stats['drafts'])}")
    if stats["missing_images"]:
        print(f"UNRECOVERABLE images: {sorted(set(stats['missing_images']))}")


if __name__ == "__main__":
    main()
