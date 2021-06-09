---
date: "2019-10-06T00:00:00Z"
description: Visualising 200 Brexit-related votes with machine learning
image: https://basilesimon.fr/assets/tsne.png
tags: [observable, d3, viz]
title: Machine learning's take on the Brexit's House of Commons
---

Let's say things are a little confused over here in Brexit Land. To put it lightly, it has become difficult to explain, or simply to fathom what's going to happen next.

A few months ago I looked at [the rift splitting the Conservative Party](https://graphics.reuters.com/BRITAIN-EU-LEADER/010092Q33KW/index.html), but the topic kept nagging me.

<a href="https://graphics.reuters.com/BRITAIN-EU-LEADER/010092Q33KW/index.html"><img src="assets/brexit-split.png" style="width: 50%; margin: auto;"></img></a>

Obviously the "indicative votes" were a great tool to identify the [Brexit "tribes,"](https://ig.ft.com/brexit-tory-tribes/) as they represented such varied opinions, allowing us to build a mental picture of the different kinds of Brexit MPs could support.

But paying close attention to British politics for a while introduces a certain perception bias, whereby we see some MPs as more or less extreme based on our impressions shaped over a few months discusssing the topic — the quite questionable data we gathered by reading the news.

So here are my questions:

_**What about the long-term, more latent allegiances MPs might hold?**_

_**Could we do without our "Brexit goggles" and look at a more impartial, objective picture of our House of Commons?**_

To find out, I fed a number of House of Commons Brexit-related votes to [`t-SNE`, a machine learning discovery algorithm](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding). The result is below:

<img src="assets/tsne.svg"></img>

<svg role="img" viewBox="0 0 25 28" width="25" height="28" aria-label="Observable" fill="currentColor" style="width: 22px; transform: translateY(5px);" class="near-black"><path d="M12.5 22.6667C11.3458 22.6667 10.3458 22.4153 9.5 21.9127C8.65721 21.412 7.98339 20.7027 7.55521 19.8654C7.09997 18.9942 6.76672 18.0729 6.56354 17.1239C6.34796 16.0947 6.24294 15.0483 6.25 14C6.25 13.1699 6.30417 12.3764 6.41354 11.6176C6.52188 10.8598 6.72292 10.0894 7.01563 9.30748C7.30833 8.52555 7.68542 7.84763 8.14479 7.27274C8.62304 6.68378 9.24141 6.20438 9.95208 5.87163C10.6979 5.51244 11.5458 5.33333 12.5 5.33333C13.6542 5.33333 14.6542 5.58467 15.5 6.08733C16.3428 6.588 17.0166 7.29733 17.4448 8.13459C17.8969 8.99644 18.2271 9.9103 18.4365 10.8761C18.6448 11.841 18.75 12.883 18.75 14C18.75 14.8301 18.6958 15.6236 18.5865 16.3824C18.4699 17.1702 18.2639 17.9446 17.9719 18.6925C17.6698 19.4744 17.2948 20.1524 16.8427 20.7273C16.3906 21.3021 15.7927 21.7692 15.0479 22.1284C14.3031 22.4876 13.4542 22.6667 12.5 22.6667ZM14.7063 16.2945C15.304 15.6944 15.6365 14.864 15.625 14C15.625 13.1073 15.326 12.3425 14.7292 11.7055C14.1313 11.0685 13.3885 10.75 12.5 10.75C11.6115 10.75 10.8688 11.0685 10.2708 11.7055C9.68532 12.3123 9.36198 13.1405 9.375 14C9.375 14.8927 9.67396 15.6575 10.2708 16.2945C10.8688 16.9315 11.6115 17.25 12.5 17.25C13.3885 17.25 14.124 16.9315 14.7063 16.2945ZM12.5 27C19.4031 27 25 21.1792 25 14C25 6.82075 19.4031 1 12.5 1C5.59687 1 0 6.82075 0 14C0 21.1792 5.59687 27 12.5 27Z" fill="currentColor"></path></svg>
<a href="https://observablehq.com/d/8c2c588548870f79">View on Observable</a>

Note the clustering of Brexiteers at the top of the plot, including Labour's Kate Hoey, the DUP, and Boris Johnson's cabinet.

At the bottom of the Conservative cloud are the more moderate MPs and Theresa May's cabinet. Former prime minister Ken Clarke is placed close to Sir Oliver Letwin (author of prominent amendments allowing the House to wrestle control from the government) and Dr Philip Lee, who defected to the Lib Dems.

Kit Malthouse, author of the ["Malthouse compromise"](https://www.theguardian.com/politics/2019/jan/29/the-malthouse-compromise-everything-you-need-to-know-brexit-vote) which gathered support from both sides of the Conservative benches, is in the middle.

---

### A word on the data

The dataset is comprised of 238 votes, including amendments and draft bills, "meaningful" and "indicative" votes (on Theresa May's deal and on a range of freely-submitted, blue-sky-thinking options respectivelly), as well as procedural votes and motions (such as Sir Oliver Letwin's two successes at wrestling control of parliamentary agenda away from the executive branch).

These votes took place between September 2017 and September 2019, and I must thank the [Institute for Government](https://www.instituteforgovernment.org.uk/), who have provided the overwhelming majority of this research labelling Brexit-related votes from two years' worth of votes.

As for the previous Reuters piece, I scraped the [Parliament API](http://www.data.parliament.uk/) to obtain each vote cast by each MP in each House of Commons vote.

The `t-SNE` algorithm took into account how MPs voted (in favour or against a bill) and whether they voted at all (MPs are not bound to cast their vote, and some occasionally abstain).

These numerous variables were reduced by the algorithm to two dimensions for visualisations (_x_ and _y_). Contrary to a principal component analysis (see _The Economist_ piece below), it is not possible to say what `t-SNE` has _seen_ (so to speak) in a dataset.

### Acknowledgements

1. _The Economist_'s [MP's Brexit votes reveal myriad divisions among the Tories](https://www.economist.com/graphic-detail/2019/03/29/mps-brexit-votes-reveal-myriad-divisions-among-the-tories), based on 13 votes including the indicative and meaningful votes and on [principal component analysis](https://en.wikipedia.org/wiki/Principal_component_analysis).
2. The [Institute for Government](https://www.instituteforgovernment.org.uk/)'s continued excellent research and timely analysis of British politics.

<style>
.annotation-note-title {
font-family: sans-serif;
font-weight: 100;
font-sie: 6px;
}
</style>
