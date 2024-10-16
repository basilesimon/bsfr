---
date: "2021-02-19T00:00:00Z"
draft: true
title: "Jaccard and dendrograms - weeknotes #21"
---

The little one is spending more and more time at daycare, and I'm loving it.  
It feels like it's such a nice place for her, she's got her own buddies and comes home hyper-stimulated. Meanwhile, I get to hang out with my internet buddies and be stimulated 😇

---

Despite having more time however, I had to kick the Tactical Tech deadline -- first time of my new freelance life I have to do that.

We've made some good progress, though. Right now, the companies I'm looking at still fall in several buckets. And it feels natural, right? My startup X builds a _machine learning_ model for tractors (e.g. _hardware_) to improve their plowing and the farm's yield (so, _agriculture_).

Going from these three fields to one (without manually looking at each and every company) is an issue.

Right now, I've reduced the vocabulary to around 50 fields, and a dissimilarity matrix based on the Jaccard distance allows us to surface 17 "buckets" -- each company falling into one at the most:

![Dendrogram of company categories](assets/ward-dendro.png)

But labelling and explaining is difficult too. Particularly when one such bucket brings together "Food", "Gamification", "IoT", etc.

---

The Bureau published the story I audited last week:
[Amazon’s empty pledge leaves agency workers without shifts and pay](https://www.thebureauinvestigates.com/stories/2021-02-18/amazons-empty-pledge-leaves-agency-workers-without-shifts-and-pay). I'm credited as _Tech auditor_, which is a first for me!

It made me think that I rather enjoy this support role to investigative journalism teams, so I added this section to my website:

> **I support investigative journalism work**  
> Part of my time is spent working as a technologist and advisor to investigative journalism organisations, such as Global Witness and The Bureau of Investigative Journalism.  
> Some of that work consists of code reviews, data audits, and system administration. Out of the trenches, I advise on infrastructure and systems architecture to support the work of these teams.

---

Aside from looking after backing up Neo4J instances, I quickly stood up an uptime monitor thanks to the [Koj team's](https://twitter.com/kojengineering) excellent work:

![Screenshot of my uptime monitor](assets/upptime-monitor.png)

[https://basilesimon.github.io/upptime-monitor](https://basilesimon.github.io/upptime-monitor)

It's all GitHub Actions-based, and totally not how I would have gone about building it, but works brilliantly so far!

---

We celebrated D3.js' 10th anniversary and welcomed a new space: [d3js.community](https://d3js.community/) 🎉

I owe a lot to the D3 team, to the contributors, and to the community in general. News online and the NGO space, among others, would be visually quite different were it not for their work.

So thank you.
