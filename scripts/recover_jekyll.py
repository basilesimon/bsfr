#!/usr/bin/env python3
"""Convert posts from the archived Jekyll blog into Hugo content files.

The original source of blog.basilesimon.fr survives at
github.com/basilesimon/archive-blog. This reads posts from a checkout of that
repo and writes content/<section>/<slug>.md, copying referenced assets into
static/assets/ — falling back to `git show` against the archive's history for
files that are no longer in its worktree.

Which posts to convert comes from the checklists in IMPLEMENTATION_PLAN.md,
which also supply each post's historical URL (used as the Hugo alias).

See IMPLEMENTATION_PLAN.md, stages 2-3.
"""

import argparse
import html
import os
import posixpath
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(REPO, "IMPLEMENTATION_PLAN.md")

# Images live in these directories of the archive, in priority order.
ASSET_DIRS = ("_assets", "_attachments")

# Any site-hosted file a post points at: images, but also the iframe bundles,
# scripts and video that several posts embed. Quoted attributes are matched to
# their closing quote because a few WordPress filenames contain spaces.
ASSET_RE = re.compile(
    r"""(?:src|href)=["'](/assets/[^"']+)["']"""  # quoted: may contain spaces
    r"""|(?:src|href)=(/assets/[^\s>"']+)"""  # unquoted, as WordPress wrote it
    r"""|(?:\]\(|url\()\s*(/assets/[^)\s]+)"""  # Markdown and CSS references
    r"""|^\s*\[[^\]]+\]:\s*(/assets/\S+)""",  # reference-style link definitions
    re.M,
)
# pandoc escapes Markdown punctuation even inside the raw HTML it emits, where
# a backslash is literal rather than an escape. Undo that inside asset paths.
MD_ESCAPE_RE = re.compile(r"\\([_*\[\]()~`>#+=|.!-])")
# Relative references inside a copied iframe bundle's HTML.
BUNDLE_RE = re.compile(r"""(?:src=|href=)["']([^"'#/][^"':]*?)["']""")
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
    """Strip YAML quoting from a scalar.

    WordPress's exporter emitted titles containing a colon as `! 'Some: title'`
    — a non-specific tag followed by a single-quoted scalar, in which an
    apostrophe is escaped by doubling it.
    """
    value = re.sub(r"^!+\S*\s+", "", value.strip())
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        quote = value[0]
        return value[1:-1].replace(quote * 2, quote)
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


def strip_wordpress_cruft(body):
    """Remove WordPress widgets that cannot survive the move off WordPress."""
    # The Google+ button it stamped onto every exported post.
    body = re.sub(
        r'\s*<div class="wp_plus_one_button".*?</div>\s*', "\n\n", body, flags=re.S
    )

    # Emoticons were served as images from wp-includes, which is gone. Each one
    # carries the emoticon it replaced in its alt text, so put that back.
    def smiley(m):
        alt = re.search(r'alt="([^"]*)"', m.group(0))
        return alt.group(1) if alt else ""

    return re.sub(r"<img[^>]*\bwp-smiley\b[^>]*>", smiley, body)


def rewrite_urls(body, linkmap, section):
    """Point old-domain asset and post URLs at their current location."""
    # Where each post ended up, keyed by slug, for lookups that can't match a
    # full path: French posts kept /YYYY/MM/ permalinks while their English
    # editions got /YYYY/MM/DD/ ones.
    slugmap = {url.strip("/").split("/")[-1]: url for url in linkmap.values()}
    body = re.sub(
        r"https?://blog\.basilesimon\.fr/wp-content/uploads/(?:\d{4}/\d{2}/)?",
        "/assets/",
        body,
    )
    body = re.sub(r"https?://(?:blog\.)?basilesimon\.fr/assets/", "/assets/", body)

    def post_link(m):
        path = "/" + m.group("path").strip("/") + "/"
        return linkmap.get(path, path)

    def en_link(m):
        """`/en/<path>` was the English edition of a French post.

        Those translations were published under the same slug with a `-2`
        suffix, so prefer that; fall back to the original when there is none.
        """
        path = "/" + m.group("path").strip("/") + "/"
        slug = path.strip("/").split("/")[-1]
        return slugmap.get(slug + "-2") or linkmap.get(path, path)

    body = re.sub(
        r"https?://blog\.basilesimon\.fr/en/(?P<path>\d{4}/\d{2}(?:/\d{2})?/[^\s)\"'<>]+?)/?(?=[\s)\"'<>]|$)",
        en_link,
        body,
    )
    # Links to posts on the dead subdomain, and bare old-style paths.
    body = re.sub(
        r"https?://blog\.basilesimon\.fr/(?P<path>\d{4}/\d{2}(?:/\d{2})?/[^\s)\"'<>]+?)/?(?=[\s)\"'<>]|$)",
        post_link,
        body,
    )
    # Standalone WordPress pages that came back as posts.
    def page_link(m):
        return slugmap.get(m.group("slug"), m.group(0))

    body = re.sub(
        r"https?://blog\.basilesimon\.fr/(?P<slug>[a-z0-9-]+)/(?=[\s)\"'<>]|$)",
        page_link,
        body,
    )
    # WordPress tag and category archives have no equivalent here; the section
    # index is the closest thing that still lists the same posts.
    body = re.sub(
        r"https?://blog\.basilesimon\.fr/(?:tag|category)/[^\s)\"'<>]*",
        f"/{section}/",
        body,
    )
    # Whatever is left pointing at the dead subdomain's own root.
    body = re.sub(r"https?://blog\.basilesimon\.fr/(?:en/)?(?=[\s)\"'<>]|$)", "/", body)
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
    text = html.unescape(body)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    # Inline charts, scripts and styles carry text nodes that are not prose.
    text = re.sub(r"<(svg|script|style)\b.*?</\1>", " ", text, flags=re.S | re.I)
    # Reference-style link definitions and horizontal rules are not prose.
    text = re.sub(r"^\s*\[[^\]]+\]:\s*\S+.*$", " ", text, flags=re.M)
    text = re.sub(r"^\s*([-*_])(?:\s*\1){2,}\s*$", " ", text, flags=re.M)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]*)\]\((?:[^)]*)\)", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\[[^\]]*\]", r"\1", text)
    text = re.sub(r"[#>*_`]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    cut = text[:limit]
    return cut[: cut.rfind(" ")].rstrip(" ,;:-") + "…"


# --------------------------------------------------------------------------
# conversion
# --------------------------------------------------------------------------


def convert(slug, entry, archive, src, hist, section, linkmap, stats, keep_tags=True):
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
    body = rewrite_urls(body, linkmap, section)
    body = re.sub(
        r"/assets/[^\s\"'<>)]+", lambda m: MD_ESCAPE_RE.sub(r"\1", m.group(0)), body
    )
    body = strip_wordpress_cruft(body)
    body = body.strip() + "\n"

    assets = copy_assets(body, archive, hist, stats)

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
    tags = fm.get("tags") if keep_tags else None
    if isinstance(tags, str):
        tags = [tags]
    tags = [t.lower() for t in (tags or []) if t.lower() != "non classé"]
    lines.append(f"tags: [{', '.join(tags)}]")
    lines.append(f"title: {yaml_quote(html.unescape(fm.get('title') or slug))}")
    if str(fm.get("published")).lower() == "false":
        lines.append("draft: true")
        stats["drafts"].append(slug)
    lines.append("---")
    lines.append("")

    out_path = os.path.join(REPO, "content", section, slug + ".md")
    return out_path, "\n".join(lines) + body, assets


def fetch_asset(archive, hist, rel, stats):
    """Find one `/assets/<rel>` file, in the archive worktree or its history.

    `rel` keeps its subdirectories: two different images are both named
    scotland-1.jpg, so matching on basename alone would serve the wrong one.
    Basename fallbacks therefore only apply to references that had no
    directory of their own.
    """
    names = [rel]
    # Some accented filenames were committed mangled: the UTF-8 bytes of the
    # name were read back as CP866, so `à` sits on disk as `├а`.
    try:
        mojibake = rel.encode("utf-8").decode("cp866")
        if mojibake != rel:
            names.append(mojibake)
    except (UnicodeDecodeError, UnicodeEncodeError):
        pass
    # WordPress served generated thumbnails like `name-300x215.jpg`; only the
    # full-size original was ever committed.
    for n in list(names):
        full = re.sub(r"-\d+x\d+(?=\.\w+$)", "", n)
        if full != n:
            names.append(full)

    candidates = [os.path.join(d, n) for n in names for d in ASSET_DIRS]
    if os.path.dirname(rel) == "":
        candidates += [
            os.path.join(d, os.path.basename(n)) for n in names for d in ASSET_DIRS
        ]

    for c in candidates:
        path = os.path.join(archive, c)
        if os.path.exists(path):
            return open(path, "rb").read()

    for c in candidates:
        data = read_from_history(archive, c)
        if data:
            stats["from_history"].append(rel)
            return data

    if os.path.dirname(rel) == "":
        for p in sorted(hist.get(os.path.basename(rel), [])):
            data = read_from_history(archive, p)
            if data:
                stats["from_history"].append(rel)
                return data
    return None


def copy_assets(body, archive, hist, stats):
    """Copy every `/assets/...` file a post references into static/assets/.

    Iframe bundles pull in their own stylesheets and scripts, so copied HTML
    is rescanned and its relative references followed.
    """
    copied = []
    queue = []
    for match in ASSET_RE.findall(body):
        ref = next(g for g in match if g)
        queue.append(ref.split("?")[0].split("#")[0])
    seen = set()
    while queue:
        ref = queue.pop(0)
        if ref in seen:
            continue
        seen.add(ref)
        rel = ref[len("/assets/") :]
        dest = os.path.join(REPO, "static", "assets", rel)

        if os.path.exists(dest):
            data = open(dest, "rb").read()
        else:
            data = fetch_asset(archive, hist, rel, stats)
            if data is None:
                stats["missing_assets"].append(rel)
                continue
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as fh:
                fh.write(data)
            copied.append(rel)

        if rel.endswith((".html", ".htm")):
            base = posixpath.dirname(rel)
            for sub in BUNDLE_RE.findall(data.decode("utf-8", "replace")):
                queue.append("/assets/" + posixpath.normpath(posixpath.join(base, sub)))
    return copied


# --------------------------------------------------------------------------
# plan + link map
# --------------------------------------------------------------------------


def plan_entries(stage):
    """Parse a stage's checklist from IMPLEMENTATION_PLAN.md."""
    text = open(PLAN, encoding="utf-8").read()
    section = text.split(f"## Stage {stage}")[1]
    section = re.split(r"^## ", section, maxsplit=1, flags=re.M)[0]
    return {
        url.strip("/").split("/")[-1]: (date, title, url)
        for date, title, url in PLAN_ENTRY_RE.findall(section)
    }


def build_linkmap(entries, section):
    """Map every historical post URL to where that post lives now."""
    linkmap = {}
    for slug, (_d, _t, url) in entries.items():
        linkmap["/" + url.strip("/") + "/"] = f"/{section}/{slug}/"
    # Posts already recovered or migrated carry their old URLs in `aliases:`.
    content = os.path.join(REPO, "content")
    for sec in sorted(os.listdir(content)):
        d = os.path.join(content, sec)
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
    ap.add_argument(
        "--drop-tags",
        action="store_true",
        help="omit source tags; the photography archive carries 309 of them, "
        "which would swamp the site-wide tag list shown on /blog",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    entries = plan_entries(args.stage)
    src = source_posts(args.archive)
    hist = history_paths(args.archive)
    linkmap = build_linkmap(entries, args.section)
    stats = {"drafts": [], "from_history": [], "missing_assets": [], "written": []}

    todo = args.only or sorted(entries)
    for slug in todo:
        if slug not in entries:
            print(f"  !! {slug}: not in the stage {args.stage} checklist", file=sys.stderr)
            continue
        if slug not in src:
            print(f"  !! {slug}: no source file in the archive", file=sys.stderr)
            continue
        out_path, text, assets = convert(
            slug, entries[slug], args.archive, src, hist, args.section, linkmap,
            stats, keep_tags=not args.drop_tags,
        )
        if os.path.exists(out_path) and not args.only:
            print(f"  -- {slug}: already exists, skipped", file=sys.stderr)
            continue
        stats["written"].append(slug)
        if args.dry_run:
            print(f"===== {out_path} ({len(assets)} assets) =====\n{text}")
        else:
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(text)

    print(f"\nwrote {len(stats['written'])} posts into content/{args.section}/")
    print(f"assets recovered from git history: {len(set(stats['from_history']))}")
    if stats["drafts"]:
        print(f"marked draft (published: false in Jekyll): {len(stats['drafts'])}")
    if stats["missing_assets"]:
        print(f"UNRECOVERABLE assets: {sorted(set(stats['missing_assets']))}")


if __name__ == "__main__":
    main()
