---
date: "2020-10-21T00:00:00Z"
description: A step-by-step walkthrough of a beeswarm layout I produced as an alternative a bar chart
image: https://basilesimon.fr/assets/beeswarm-obs.png
tags: [observable, d3, viz]
title: A beeswarm layout in Observable -- on deadline
---

![](assets/beeswarm-obs.png)

I recently had to complete a technical test for a role I'm interested in.

The task: from [a story out of the Global Witness website](https://www.globalwitness.org/en/campaigns/oil-gas-and-mining/chevron-stop-funding-racism/), can you come up with an alternative visualisation? **You've got two hours.**

As there were no embed constraints, I figured there was no point in faffing with boilerplate code and scaffolds, so I went down the Observable route to put a chart together.

Here's what we need scales-wise:
* On the y axis, the amount of the individual donations range from 0 to $10,000 -- we'll use a linear scale which domain is mapped to this extent;
* On the x axis, we've got two categories: the donations that pass the NAACP criteria, and those that don't. We cue an ordinal scale which domain are these values;
* A simple colour scale;

---

But as donation amounts overlap each other, so do our circles. Here they are, with a small increasing offset to show this banding effect:

![](assets/beeswarm-overlap.png)

Comes the force layout to the rescue, adding some simulated entropy to the x/y coordinates of our circles and allowing us to appreciate the difference in scale between the two columns.

```js
const simulation = d3
  .forceSimulation(data)
  .force('x', d3.forceX(d => x(d.category)).strength(0.2))
  .force('y', d3.forceY(d => y(+d.donationUSD)).strength(1))
  .force('collide', d3.forceCollide(d => size(Math.sqrt(+d.donationUSD))))
  .alphaDecay(0)
  .alpha(0.3)
  .stop();
```

We apply three forces to our simulation:
* One **on the x axis**, so our circles bucket into our two categories. We specify a weak `.strength()` so they spread out horizontally rather than vertically (and thus are more truthful to the precise donation amounts);
* One **on the y axis**, where in this case the `.strength()` is far greater to squeeze them further, as seen above;
* A **collision force** which repels the circles from each other, so as to spread them apart.

Here they are, showing the influence of x and y's `.strength()`:

<video autoplay loop muted playsinline>
       <source src="assets/beeswarm.mp4" type="video/mp4">
</video>

Did I say I had two hours to do this? I had to skimp on the annotations, which I've positioned manually and quite roughly as <text> elements.

---

Read more:

* [@rospearce's layout greatly helped](https://observablehq.com/@rospearce/beeswarm)
* There appears to be an actual npm module to produce such layouts: [d3-beeswarm](https://github.com/Kcnarf/d3-beeswarm)
* [A rather complete tutorial from @chartfleau](https://www.chartfleau.com/tutorials/d3swarm/)
