---
date: "2019-03-02T00:00:00Z"
description: Using phylogenetics visualisations to represent the Tractatus Logico-Philosophicus
image: https://blog.basilesimon.fr/assets/tractatus_tree.png
tags: [r]
title: Tractatus Logico (Phylo)sophicus
---

<div id="viz" width="100%"></div>

Over the Christmas holidays, I read ["Maths Meets Myths: Quantitative Approaches to Ancient Narratives,"](https://www.amazon.co.uk/Maths-Meets-Myths-Quantitative-Understanding-ebook/dp/B01LXAHGCK?SubscriptionId=AKIAILSHYYTFIVPWUY6Q&tag=duckduckgo-ffab-uk-21&linkCode=xm2&camp=2025&creative=165953&creativeASIN=B01LXAHGCK) from the Springer _Understanding Complex Systems_ collection.

The authors present their application of "hard" science techniques to datasets coming from the humanities -- mostly large corpus of texts, legends and myths.

One paper in particular uses bioinformatics and phylogenetics to [study the spread of a popular folk tale: Little Red Riding Hood](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0078871). The story that I knew from Perrult and Grimm has patterns that are also found in African and East Asian tales.

---

### The Tractatus Logico-Philosophicus viewed as a phylogenetic tree

Inspired by this, I've had a look at Wittgenstein's [Tractatus Logico Philosophicus](https://en.wikipedia.org/wiki/Tractatus_Logico-Philosophicus) (available on [Project Gutenberg](http://www.gutenberg.org/ebooks/5740)), which is presented as hierachically numbered statements and sub-statements.

We start by scraping the book into a dataframe with one row per statement:

```r
library(rvest)
page <- read_html("http://www.tractatuslogico-philosophicus.com/")
root <- page %>% html_node("#root")

df <- data.frame()
for (item in root %>% html_nodes('li')) {
  label <- item %>% html_attr("data-name")
  content <- item %>% html_text(trim = TRUE)

  temp <- data.frame(label, content)
  df <- rbind(df, temp)
}
```

We then generate our cluster analysis based on the distance between the columns of `df`, hoping that the hierachical numbering of statements will yield something interesting.

We adopt the `single` method, described like so:

> The _single linkage_ method (which is closely related to the minimal spanning tree) adopts a ‘friends of friends’ clustering strategy

```r
clusters <- hclust(dist(df), method = "single")
```

---

### Dendograms galore

From these clusters, we can represent the book as dendograms, which are used in phylogenetics to represent evolutionary splits and genetic relationships in a tree.

```r
plot(clusters, labels = clusters$labels)
```
![](assets/Rplot01.png)

```r
d <- as.dendrogram(clusters)
plot(d, horiz = TRUE, type = "triangle")
```
![](assets/Rplot02.png)

```r
library(ape)
plot(as.phylo(clusters), type = "fan")
```
![](assets/Rplot03.png)

The diagrams above show how our clusters have correctly grouped together the hierachical statements of the _Tractatus_.

From Mike Bostock's [Tree of Life](https://observablehq.com/@mbostock/tree-of-life) helped by Jason Davies' work [parsing a Newick text file format](https://github.com/jasondavies/newick.js) (standard in tree representations) in Javascript, I re-implemented the above with `d3-jetpack` and ES6: [https://bl.ocks.org/basilesimon/66db4338c15099f6e8d62f236db2ef2d](https://bl.ocks.org/basilesimon/66db4338c15099f6e8d62f236db2ef2d).

The resulting chart is at the top of this page.

I love how simple the result looks and how little we end up knowing about the book itself. The only thinkg I'll let you in the final, chapter seven put-down of this book about language, facts and truths of the world:

> What we cannot speak about we must pass over in silence.

Precisely what I didn't do in this blog about phylogenetics and a book I never finished.

<!-- Copyright 2011 Jason Davies https://github.com/jasondavies/newick.js -->
<script>function parseNewick(a){for(var e=[],r={},s=a.split(/\s*(;|\(|\)|,|:)\s*/),t=0;t<s.length;t++){var n=s[t];switch(n){case"(":var c={};r.branchset=[c],e.push(r),r=c;break;case",":var c={};e[e.length-1].branchset.push(c),r=c;break;case")":r=e.pop();break;case":":break;default:var h=s[t-1];")"==h||"("==h||","==h?r.name=n:":"==h&&(r.length=parseFloat(n))}}return r}</script>

<!-- Copyright 2016 Mike Bostock https://d3js.org -->
<script src="https://d3js.org/d3.v4.min.js"></script>
<script src="https://unpkg.com/d3-jetpack@2.0.20/build/d3-jetpack.js"></script>

<script>
const outerRadius = 900/2,
  innerRadius = outerRadius - 150;

const color = d3
  .scaleOrdinal()
  .domain(["1.", "2.", "3.", "4.", "5.", "6.", "7."])
  .range(d3.schemeCategory10);

const cluster = d3
  .cluster()
  .size([360, innerRadius])
  .separation(function(a, b) {
    return 1;
  });

const svg = d3
  .select('#viz')
  .append('svg')
  .at({
    width: outerRadius * 2,
    height: outerRadius * 2,
  });

const chart = svg.append('g').translate([outerRadius-100, outerRadius]);

d3.text(
  'https://gist.githubusercontent.com/basilesimon/fa37a436836e3556b1cc36a5067e5e33/raw/a4dddacc9e4332219ac5b94568818e7272977cdd/tlp.txt',
  function(error, life) {
    if (error) throw error;

    const root = d3
      .hierarchy(parseNewick(life), d => d.branchset)
      .sum(d => (d.branchset ? 0 : 1))
      .sort(
        (a, b) =>
          a.value - b.value || d3.ascending(a.data.length, b.data.length)
      );

    cluster(root);

    setRadius(root, (root.data.length = 0), innerRadius / maxLength(root));
    setColor(root);

    const linkExtension = chart
      .append('g')
      .attr('class', 'link-extensions')
      .selectAll('path')
      .data(root.links().filter(d => !d.target.children))
      .enter()
      .append('path')
      .each(function(d) {
        d.target.linkExtensionNode = this;
      })
      .attr('d', linkExtensionConstiable);

    const link = chart
      .append('g')
      .attr('class', 'links')
      .selectAll('path')
      .data(root.links())
      .enter()
      .append('path')
      .each(function(d) {
        d.target.linkNode = this;
      })
      .attr('d', linkConstant)
      .attr('stroke', d => d.target.color);

    chart
      .append('g')
      .attr('class', 'labels')
      .selectAll('text')
      .data(root.leaves())
      .enter()
      .append('text')
      .attr('dy', '.31em')
      .attr(
        'transform',
        d =>
          'rotate(' +
          (d.x - 90) +
          ')translate(' +
          (innerRadius + 4) +
          ',0)' +
          (d.x < 180 ? '' : 'rotate(180)')
      )
      .attr('text-anchor', d => (d.x < 180 ? 'start' : 'end'))
      .text(d => (d.data.name.length < 3 ? d.data.name : ''));


  }
);

// Compute the maximum cumulative length of any node in the tree.
const maxLength = d =>
  d.data.length + (d.children ? d3.max(d.children, maxLength) : 0);

// Set the radius of each node by recursively summing and scaling the distance from the root.
const setRadius = (d, y0, k) => {
  d.radius = (y0 += d.data.length) * k;
  if (d.children)
    d.children.forEach(function(d) {
      setRadius(d, y0, k);
    });
};

// Set the color of each node by recursively inheriting.
const setColor = d => {
  const name = d.data.name.substring(0,2);
  d.color =
    color.domain().indexOf(name) >= 0
      ? color(name)
      : d.parent ? d.parent.color : null;
  if (d.children) d.children.forEach(setColor);
};

const linkConstiable = d =>
  linkStep(d.source.x, d.source.radius, d.target.x, d.target.radius);

const linkConstant = d =>
  linkStep(d.source.x, d.source.y, d.target.x, d.target.y);

const linkExtensionConstiable = d =>
  linkStep(d.target.x, d.target.radius, d.target.x, innerRadius);

const linkExtensionConstant = d =>
  linkStep(d.target.x, d.target.y, d.target.x, innerRadius);

// Like d3.svg.diagonal.radial, but with square corners.
function linkStep(startAngle, startRadius, endAngle, endRadius) {
  const c0 = Math.cos((startAngle = (startAngle - 90) / 180 * Math.PI)),
    s0 = Math.sin(startAngle),
    c1 = Math.cos((endAngle = (endAngle - 90) / 180 * Math.PI)),
    s1 = Math.sin(endAngle);
  return (
    'M' +
    startRadius * c0 +
    ',' +
    startRadius * s0 +
    (endAngle === startAngle
      ? ''
      : 'A' +
        startRadius +
        ',' +
        startRadius +
        ' 0 0 ' +
        (endAngle > startAngle ? 1 : 0) +
        ' ' +
        startRadius * c1 +
        ',' +
        startRadius * s1) +
    'L' +
    endRadius * c1 +
    ',' +
    endRadius * s1
  );
}


</script>

<style>
.links {
  fill: none;
  stroke: #000;
}

.link-extensions {
  fill: none;
  stroke: #000;
  stroke-opacity: .25;
}

.labels {
  font: 10px sans-serif;
  font-weight: bold;
}

</style>
