---
aliases: ["/2014/06/11/the-datajournalists-toolbox/"]
date: "2014-06-11T00:00:00Z"
description: "Iain and I are at it again. As good computer-assisted people, we both see a lot of stuff coming up every day on the internets. New libraries, new…"
tags: []
title: "The datajournalists' toolbox"
---
![](/assets/Screenshot-from-2014-06-11-133800.png)

[Iain](http://twitter.com/iaincollins) and I are at it again. As good computer-assisted people, we both see a lot of stuff coming up every day on the internets. New libraries, new *how-did-I-do-my-job-without-this-before* tools...

And it's hard to know which one to pick up when we start a new project.

Well, in fact, choosing a tool is actually part of the fun, like the special-ops do in [*Black Hawk Down*](http://www.imdb.com/title/tt0265086/), before rocking up to Mogadishu, attaching with velcro to their uniforms a bunch of ammo and weird things.

The comparison is a bit far-fetched, but it is accurate to a certain extent.

For our projects, it is exciting to see which tools we are going to use, and how their use and limitations actually constrain us in the job. Time for an example:\
When we were working on the 2014 UK EU elections, we went at first for doughnut charts and hemicycles built by Google Spreadsheets graphic tools. A problem surfaced quite quickly: however nice and flexible they are, they need to be embedded in iframes, and thus lack responsiveness (despite the fact that colleagues actually came up with [a fix](http://responsivenews.co.uk/post/71845174511/responsive-iframes)).\
So we looked for another way around this, and we ended up working with [Chart.js](http://www.chartjs.org/). And to satisfy this easy-to-use library, we re-formatted a big part of our data to arrays instead of CSVs and spreadsheets. That would have been nice to actually remove this useless iteration from the work-flow from the beginning.

**So**, I would like to get to the point without being that much interrupted by myself.

Head to [the Datajournalists' toolbox](https://github.com/basilesimon/datajournalists-toolbox) Github repo. Here, you will find a list of tools we are using every day. The list will detail case uses, Gists, examples, and links to documentations and installation procedures.

If you are on Github, do contribute. Make a pull request.\
If you are not, send us an email, a tweet, or a pigeon, with your idea.

*Note: this project is a work in progress. There's not much at the moment, but there will be more in the days and weeks to come. Hopefully, thanks to you too.*
