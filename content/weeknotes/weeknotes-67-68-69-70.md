---
date: "2022-01-31T00:00:00Z"

title: "50% of 50% January - weeknotes #67, #68, #69, #70"
---

I’ve hardly opened emacs this month. Hadn’t hapenned in a while.

We came back from France early in the month and had somehow missed the memo about my daughter needing to quarantine for a week as she hasn’t gotten the vaccine yet (she doesn’t has strong feelings towards it, she’s just got a few years to wait).  
Then, a mere day after the happy return to daycare it’s our nanny who tested positive, so we had to keep cruising on staggered work days for another week. We’re now in the clear and testing the little one three times a week. It’s mandatory. Fingers crossed this works and is worth it.

The other factor in this text-editor-less spell is... I’ve been enjoying note-taking in Notion, [as I mentioned last month](https://basilesimon.fr/weeknotes/weeknotes-63-64-65-66/). It’s not as fast as I’d wish it were but just quite pleasant to use.

---

It’s been a good month for borderline order-obsessed folks like me. I got to do a whole bunch of cleaning up of the AWS accounts I run, deleting and unallocating cloud resources as if it was raining.

I like running a tight ship. It’s easier to maintain and to enforce policies across. Two examples in Global Witness’ Data & Investigations team:

1. As I reduced our many non-overlapping VPCs and subnets to a couple, setting up Tailscale as a mesh Wireguard tool really opened up opportunities, including in the literal sense by granting access to private resources.
2. As I now have fewer things to look after and more of the similar kind, I could turn my attention to adding further consistency to the few micro services we've got going. Now we’re one step away from automated deployment and easier health monitoring. And it’s just so much easier to list what we’re running and how it’s running.

One item of note this month – which [Louis must have forgotten to mention](https://ltrg.co.uk/2022/01/29/observable-vs-r.html):

We’re now trialing running [PostgREST](https://postgrest.org/en/stable/index.html) to interface between databases RDS and Observable notebooks. Now our public Observable notebooks can use our RDS data from REST endpoints created behind-the-scenes and in pure SQL fashion, which PostgREST kindly maps to views.

We had been looking for this missing piece in the puzzle for a while.

---

Working a little over half-time isn’t so bad. One downside I found is that it becomes okay for tasks to “spill over” into un-booked time, at the expense of the latter.  
But with this extra time and since I can’t ride, I managed to get into a much more consistent running rhythm, clocking about 75km this month.

I also had a bit of time for pro-bono work, and I’m super happy to reconnect with Airwars folks. It’s been, wow, maybe four or five years since I stepped down from an active role, and it’s funny to see how some things have changed and some haven’t.

One area of interest with them is their Wordpress-centric workflow, which has the unfortunate consequence to keep away from folks the raw dataset of incidents of concern, since the PHP-MySQL layer co-mingles with the CMS and web output.

And I don’t know about you but I’ve never had a good experience building on top of Wordpress…

---

So there are two questions in here: one is about custodial data practices and enabling self-service querying/analysis for a variety of technical levels ; the second is about content management systems (CMS) and their use for data inputting.

In other words: beyond spreadsheets, what tools for researchers to populate a database?

One strand of experiments Niko and I are running focus on headless CMS: the nice GUI used to manage and write content is de-coupled from how the database is ran and the content is rendered.

The second looks at tools à la AirTable, BaseRow, which aim to empower engineers to empower their non-technical colleagues, and everyone would look at the same database through a different prism.

---

I hope to have an update to share on the [Digital Evidence Toolkit](https://digitalevidencetoolkit.org) next month. Spoiler: it’s got to do with Datalog, open-source v AWS, and fancy temporality management. For now I’m just excited by the new stuff.

---

![Where is the Moon from my window](assets/moon-sketches.png)

Oh, and I finally published [a v1 version of the Moon sketches](https://observablehq.com/@basilesimon/the-moon-from-my-kitchen-window-this-evening) I mentioned last month. It’s only the base chart (in Observable Plot) for now but I aim to include some `<ref`-fu and to get it over the line.

The notebook got in the "most liked" little sidebar for a while, so that's my kid and me happy about it!
