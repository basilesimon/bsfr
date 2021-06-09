---
date: "2017-02-02T00:00:00Z"
title: January Transfer Window graphics in The Times
---

![](assets/TransferWindow2.png)

I never thought I'd talk about football this much, but here you go.

I spent the last weeks working on a rather massive piece looking at the January Transfer Window, this time of year where extraordinary sums are spent to convince men to come kick in a ball somewhere else.

[Read the whole piece and the club-by-club analysis](www.thetimes.co.uk/article/january-transfer-window-s9br65rj6) on The Times. Note: you can now register for free and benefit from two free articles.

---

### Scatterplots

![](assets/TransferWindow3.png)

We elected to set the y-axis domain manually, so it would be identical for both charts. Fixing the y-axis (instead of running it from minimum to maximum) shows how the Oscar transfer to a Chinese club skews the analysis.

French midfielder Morgan Schneiderlin's £24m fee seem little in comparison to Oscar's £60m.

---

### Snakey chart

![](assets/TransferWindow1.png)

Inspired by [this WSJ piece about swing in US states](http://www.wsj.com/graphics/elections/2016/how-is-your-state-swinging/), we decided to try to flip the coordinates of a rather standard line chart, so to display it vertically.

We decided to call them _Snakey charts_. And here's [an implementation of them in D3.js](https://bl.ocks.org/basilesimon/e72a435920fffaf2f88a74790e076320).

Oh, and that was also the first time the Times played with [annotations](http://1wheel.github.io/swoopy-drag/). Unconvinced by the traditional bendy arrows, the designers asked us to go for straight lines, with a bubble at the top. Which apprently looks more Times-y.

_(Apologies for the Times fonts being lost in the bl.ock...)_

---

### Treemaps

<div style="display: flex">
  <img src="assets/TransferWindow4.png" height=400></img>
  <img src="assets/TransferWindow5.png" height=400><img/>
</div>

To illustrate where players were coming from as well as the positiong they occupy on the pitch, we produced a set of treemaps, complete with hover-click states, and a mobile view. I must say the Times colour palette produced decent looking results.

<style>
img {
  border: 1px solid #ddd;
  margin: 0 auto;
}
</style>
