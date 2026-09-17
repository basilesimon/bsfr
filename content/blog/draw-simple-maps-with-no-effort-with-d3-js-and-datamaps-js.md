---
aliases: ["/2014/04/24/draw-simple-maps-with-no-effort-with-d3-js-and-datamaps-js/"]
date: "2014-04-24T00:00:00Z"
description: "I started working on a new project for BBC News Labs this morning, and that project heavily relies on a map. After spending these last months working…"
tags: []
title: "Draw simple maps with no effort with d3.js and datamaps.js"
---
I started working on a new project for BBC News Labs this morning, and that project heavily relies on a map. After spending these last months working around Javascript and the famous datavisualisation library [d3.js](http://d3js.org), my first reflex was to jump on d3.

However, the one first I find the hardest with d3 is to find tutorials to **learn how to d3.**

So this morning, when coming across *topoJSON*, *geoson* and other formats, phew, it was hard. The plan was to create a simple world map template that I could reuse later with many different datasets. Then, I discovered [DataMaps](http://datamaps.github.io/), a light JS library to create "*customizable SVG map visualisations for the web in a single Javascript file using D3.js*". Sounded cool.

DataMaps is in fact really easy to set up, with a classic constructor to fill with options. At the moment, and without too much exploration, I find some limitations to it (for example, loading data from an external file, or the format of the data required), but hey, that's a quick and simple solution.

<p>

In a handful of minutes, just throw in your

</p>
