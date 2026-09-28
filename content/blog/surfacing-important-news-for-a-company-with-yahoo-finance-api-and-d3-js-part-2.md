---
aliases: ["/2014/05/21/surfacing-important-news-for-a-company-with-yahoo-finance-api-and-d3-js-part-2/"]
date: "2014-05-21T00:00:00Z"
description: "After a good start last week, we now know how to get a company share value's historical data with Yahoo Finance API. That's as simple as speaking YQL.…"
tags: []
title: "Surfacing important news for a company with Yahoo Finance API and d3.js (part"
---
After a good start last week, we now know how to get a company share value's historical data with Yahoo Finance API. That's *as simple as speaking YQL.*

Today, we're going to have a look at how to graphically represent this data, with our good friend *d3.js*.\
For those who don't know [d3.js](http://d3js.org/), it is a very popular Javascript library developed by New York Times' Mike Bostock. It is widely used for data-visualisaton, largely because of its impressive capacities when it comes to transitions and its wide range of possible visualisations.

Here's a little souvenir from the last article, in which we formulated the query to Yahoo and prepared its use with jQuery:

\`\`\`javascript var myQuery = "http://query.yahooapis.com/v1/public/yql?q=select \* from yahoo.finance.historicaldata where symbol in ("AAPL") and startDate = "2013-01-01" and endDate = "2014-01-01"&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json"; var data = \$.getJSON(myQuery, foo); function foo(data) { console.log(data); } \`\`\`

The `data` variable contains our JSON blob, and the `$.getJSON()` bit calls a function named `foo()` - we will change this name soon.\
Let's dive right into it by setting up the viewport, i.e. the box in which we will place the chart:

\`\`\`javascript var margin = 50, width = 700, height = 600; \`\`\`

Now, our data is still resting quietly in the `data` variable, and we are going to use it right away.\
Shall we? Throw a function in your code that takes our data variable as a parameter. How? Like this:

\`\`\`javascript function draw(data) { //nasty d3 stuff happening here } \`\`\`

Then, let's declare our *extents* (from where to where our array goes), so we can declare our *scales*, which we need for our *axis*.

\`\`\`javascript // Extents var x_extent = d3.extent(data.query.results.quote.map(function(d) { return d.date; })); var y_extent = d3.extent(data.query.results.quote.map(function(d) { return +d.Close; })); // Scales var y_scale = d3.scale.linear() .domain(y_extent) .range(\[height-margin,margin\]); var x_scale = d3.time.scale() .domain(x_extent) .range(\[margin, width-margin\]); // Axis var x_axis = d3.svg.axis() .scale(x_scale); var y_axis = d3.svg.axis() .scale(y_scale).orient('left'); \`\`\`

I know, that is very painful to go through all this, I do agree. What we just did was basically mapping our arrays (so the program is able to iterate through them), and then using d3's capabilities to create a y-axis that is linear (we want to populate it with US dollars values), and an x-axis that follows time.\
We are almost ready. Let's make sure that our visualisation goes somewhere, and let's draw the axis. To do so, append a SVG element to your HTML document, and append to this SVG element your two axis:

\`\`\`javascript var vis = d3.select("body") .append("svg") .attr("width", width) .attr("height", height); d3.select("svg") .append("g") .attr("class", "x axis") .attr("transform", "translate(0," + (height-margin) + ")") .call(x_axis); d3.select("svg") .append("g") .attr("class", "y axis") .attr("transform", "translate(" + margin + ", 0 )") .call(y_axis); \`\`\`

Now. We want to draw a line chart of the price, right? Have a look at this [clear example](http://bl.ocks.org/mbostock/3883245) from the master himself.\
We are going to call `d3.svg.line`, but with a subtlety:

\`\`\`javascript var line = d3.svg.line() .x(function(d){ return x_scale(d.date); }) .y(function(d){ return y_scale(d.Close); }) .interpolate("linear"); \`\`\`

See what I did there?\
On the y-axis, we will have the daily value, by accessing through `d.Close`; and on the x-axis, the date. But wait, the name should be `d.Date`, right?\
Right. I forgot to mention. There is some preparation to do here.

Outside of `draw(data)`, declare a date format so d3 knows we're doing business with dates - and how it has to deal with them. Like that:

\`\`\`javascript var format = d3.time.format("%Y-%m-%d"); \`\`\`

Then, inside `draw(data)`, parse the date accordingly (we are making sure here that d3 understands what to put on the axis).

\`\`\`javascript data.query.results.quote.forEach(function(d) { d.date = format.parse(d.Date); d.Close = +d.Close; }); data.query.results.quote.sort(function(a,b) { return d3.ascending(a.date, b.date); }); \`\`\`

Append the SVG path to the big SVG element...

\`\`\`javascript var path = vis.append("path") .datum(data.query.results.quote) .style("fill", "none") .attr("class", "line") .attr("d", line); \`\`\`

We also need labels under our axis. Luckily, that's easy.

\`\`\`javascript d3.select(".y.axis") .append("text") .text("lol much text") .attr("transform", "rotate (-90, -43, 0) translate(-280)"); d3.select(".x.axis") .append("text") .text("such axis") .attr("x", function(){return (width / 2) - margin;}) .attr("y", margin/1.5); \`\`\`

And *voilà!* You're good to go!\
If you want some sort of transition while the chart draws, here's an esoteric solution:

\`\`\`javascript var totalLength = path.node().getTotalLength(); path .attr("stroke-dasharray", totalLength + " " + totalLength) .attr("stroke-dashoffset", totalLength) .transition() .duration(2000) .ease("linear") .attr("stroke-dashoffset", 0); \`\`\`

------------------------------------------------------------------------

You may now take a breath.

Next week, we will look at how to use HTML inputs to make something more dynamic than what we have at the moment.
