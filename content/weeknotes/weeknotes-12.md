---
date: "2020-12-11T00:00:00Z"
draft: true
title: "Belated winter travels - weeknotes #12"
---

These notes are coming out a few days later than usual, as I spent the tail end of last week off the computer.

We've travelled to France via Switzerland to spend a month around the winter holidays. The trip was long and we have to stay a little bit a distance before meeting my family, so we've got to stay a while to make it worth it.

---

God I hate Slack. I'm in several Slack instances to talk to quite literally one or two people. At times, we send each other long messages. To refer to anything, I need to open Slack and look for it. I can't do it from my phone.

If only there was a better way. Oh wait.

---

### Thing of the week

Less "a thing" and more a "look at my `bash`", I admit.

I've removed a bunch (read: a lot) of old blogs on `[blog.basilesimon.fr]({{ site.baseurl }})` and I wanted to delete the corresponding media assets, which are no longer used.

My solution:

```sh
$ comm -23 <(ls ../_assets) <(ls . |
      xargs grep -o 'assets/[^"]*' |
      awk -F"assets/" '{gsub(/\)$/,""); print $2}' |
      sort) |
  xargs -I {} echo "/Users/b/blog/_assets/"{} |
  xargs -I {} mv {} ~/Desktop/bin
```

- lists all posts in `/_posts`
- `awk`-fu the path of each of the media referenced in them
- diff this list with the list of files in `_assets`
- move away files that aren't needed anymore
