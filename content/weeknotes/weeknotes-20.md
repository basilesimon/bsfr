---
date: "2021-02-12T00:00:00Z"
draft: true
title: "Bubbles bubbles - weeknotes #20"
---

There's been perma-snow in Berlin for the last two weeks now. This weekend, hundreds of people were having a wander on the frozen canals. Two digits negative temperatures. Proper winter!

However, lockdown is going to last a while longer here in Germany. While the infection numbers are falling, the concern is the still-invisible surge of infections from the other variants, which would (according to some models) rocket up in the next three weeks and bring us the omniously-named Third Wave.

[Zeit have all the details](https://www.zeit.de/wissen/gesundheit/2021-02/corona-varianten-verbreitung-deutschland-mutationen-virus-datenlage/komplettansicht), but the chart below summarises it:

![Screenshot of Zeit Covid model](assets/zeit-infection-rate.png)

So there we have it. We're adapting our daycare plans.

---

I've sketched out an intro for the Tactical Tech project, in Observable. Big hit with the team. It feels that we're now on the same page and all looking in the same direction content-wise.

<video autoplay="" loop="" muted="" playsinline="" class="video-background" style="width:100%">
  <source src="assets/tactech-intro.mp4" type="video/mp4">
</video>

I've also produced another notebook to allow us to play with some parameters and to collectively agree on a definition.

In this example, what do we mean by "companies X and Y are in quasi-monopolies in this and that field"? With the tool, we can not only pick out which fields see such monopolies, but also influence our definition of a monopoly. Is it one company owning more than 70% of the field? Or more?

<video autoplay="" loop="" muted="" playsinline="" class="video-background" style="width:100%">
  <source src="assets/tactech-notebook.mp4" type="video/mp4">
</video>

---

Since we're at capacity work-wise anyway, a little more can't hurt. [Charles](https://twitter.com/cboutaud) asked me to review some of the material they collected and scraped, as well as the code he wrote. Very keen to oblige the Bureau, I said yes.

---

Good news from my previously-mentioned Neo4J problem: a new v.3.5 instance is up a running, and the data from the dead server was replicated... and picked up by Linkurious as if nothing happened.

My fancy Docker plans were then shelved for now.

To console myself I put in a bit of time in a nice [Geoserver](http://geoserver.org/) for Louis, who last I checked was delighted by it.

And to be honest, it's the first week I managed to keep it to our agreed four hours, so that was it for Global Witness.

---

I spoke with a few people on the phone -- most notably Thomas, who [also publishes weeknotes](https://détour.studio/) _(wink wink)_. We're both in a good place, how nice to hear 😊

### Thing of the week

<iframe width="100%" height="584" frameborder="0"
  src="https://observablehq.com/embed/@basilesimon/hello-d3-render-a-declarative-wrapper-around-d3s-update-pat?cells=chart"></iframe>

As I was looking into idiomatic ways of updating a chart, I came across [Kaho Cheung](https://github.com/unkleho)'s [d3-render](https://github.com/unkleho/d3-render) -- and boy did I get excited.

For my own understanding, [I made a useless viz](https://blog.basilesimon.fr/2021/02/11/hello-d3-render/).
