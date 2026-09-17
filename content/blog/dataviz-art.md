---
aliases: ["/2014/07/08/dataviz-art/"]
date: "2014-07-08T00:00:00Z"
description: "As I was working on a project for the News Labs, I fired up - as usual - the beloved d3.js library. Without saying to much, because guessing is actually…"
tags: []
title: "Dataviz art - or WTF"
---
As I was working on a project for the [News Labs](http://twitter.com/BBC_News_Labs), I fired up - *as usual* - the beloved d3.js library.

Without saying to much, because guessing is actually the whole point of this post, I wanted to chart *relationships between people.* Without too much hesitation, I went for a force-directed layout, using d3's ``d3.layout.force()``.

![10 people](/assets/10persons.png)
**10 people:**
Above, this is the very first result I obtained once the d3 template working fine. Observe how the chart's core revolves around UK's PM David Cameron and the other main parties' leaders. Cameron connects two worlds:

* International affairs, with US' Barack Obama, Germany's Angela Merkel, and Ukraine's Petro Poroshenko ;
* And national politics, with former PM Tony Blair, Mayor of London Boris Johnson, and George Galloway.

![50 people](/assets/50persons.png)
**50 people:**
Ah, this is getting more interesting. Here, you can see 50 people plotted in the graph as bubbles, as well as 250 links towards other people. Note how *separate* parts of the chart begin to take shape, even though the core is pretty dense.

![100 people](/assets/100persons.png)
**100 people:**
Same graph with 100 persons plotted and 500 links. The very high number of links, coloured in grey, express the relationships between the bubble entities and the external ones. D3's capacities to generate gravity and force field are truly magestic to see when the graph is drawing, each time the page is reloaded.

![100 people names](/assets/100personsnolinks.png)
What if I add all the names and delete the links? Disco ball.

![500](/assets/500refined.png)
**500 people:**
This is the latest version I have. I refined several parameters, following Mike Bostock's advices, in order to better exploit d3's legwork in representing the relationships. See the left-hand side clearly separated and all connected to a single, large bubble. See also the strong links (the only one drawn) to several distant entities. And once again, see this very dense core.

### Now, up to you: what is it?
