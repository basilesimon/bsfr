---
aliases: ["/2014/06/19/responsive-videos-made-easy/"]
date: "2014-06-19T00:00:00Z"
description: "Github is definitely a nice place to be around. Following people leads to lucky discoveries.\\ This morning, Paul Adenot, software engineer at Mozilla, and…"
tags: []
title: "Responsive videos made easy"
---
Github is definitely a nice place to be around. Following people leads to lucky discoveries.\
This morning, [Paul Adenot](http://twitter.com/padenot), software engineer at Mozilla, and specialised in audio and video, [published a new repo](https://github.com/padenot/talk-rich-media) with the content of his talk about rich audio and video on the web.

The talk can be accessed at [this address](http://padenot.github.io/talk-rich-media/), and it's a short delight.

While I was quickly going through it, I stumbled upon the slide about responsive videos without Javascript - and, of course, it rang a bell.

**Basically, CSS media queries now work on the `<video>` element.**

Without going through the codecs question (addressed earlier in the talk), you can add a media property to your HTML5 videos, like that:

\`\`\`html

<video controls>

<source src="retina.webm" media="(min-resolution: 300dpi)">

</source>

<source src="desktop.webm" media="(min-device-width: 769px)">

</source>

<source src="mobile.webm" media="(max-device-width: 769px)">

</source>

</video>

\`\`\`

Easy, right?\
[Jump to the slide](http://padenot.github.io/talk-rich-media/?full#source-media) to see a demo, that is quite impressive.

That is *not* a revolution - and it's already a 2-year-old solution, but it is progress in terms of usability, simplicity, and weight.\
No need for that fancy Javascript looking at your browser properties and running tests: **it's all in your browser, right away**.\
*(Provided you use Firefox, for Chrome doesn't integrate this functionality yet.)*
