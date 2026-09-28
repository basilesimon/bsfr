---
aliases: ["/2017/01/16/cycling-ii/"]
date: "2017-01-16T00:00:00Z"
description: "Red light. Slow down. Pedal less. On a fixed gear, pushing back feels like pedalling backwards. Odd. The junction is turning orange. I don’t want to…"
tags: []
title: "Cycling II"
---
Red light. Slow down. Pedal less. On a fixed gear, pushing back feels like pedalling backwards. Odd. The junction is turning orange. I don’t want to unclip. Or to stop. Stand up on the pedals. Long strokes, moving backwards and forwards. I could track-stand if need be. But I don’t want to stop.

Don’t know if the pedestrian crossing will have it, or if I will. I should remember this junction. I’ll head to the advanced stop line super slowly and hope. That car is so turning left. They’re not indicating yet, but I don’t know, there’s something about it. I’ll stop in front of it. Eyes staring at the lights.

<style type="text/css">
  #line{
    width: 100%;
    margin: 20px 0;
    height: 100px;
  }
  .old {
    stroke: lightgrey;
  }
</style>

<div id="line">

</div>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.4.1/d3.min.js"></script>

<script type="text/javascript">
    var w = document.getElementsByClassName("content")[0].clientWidth;
    //var w = 600;
    var h = 100;
    var svg = d3.select("#line")
      .append("svg")
      .attr("width", w)
      .attr("height", h)
      .attr("id", "visualization");
    var x = d3.scaleLinear().domain([0, 10]).range([0, w]);
    var y = d3.scaleLinear().domain([0, 10]).range([10, h - 10]);
    var line = d3.line()
      .x(function(d,i) {return x(i);})
      .y(function(d) {return y(d);})
      .curve(d3.curveNatural)
    // data is created inside the function so it is always unique
    let i=0;
    let repeat = () => {
      var data = d3.range(11).map(function(){return Math.random()*10})
      // Uncomment following line to clear the previously drawn line
      //svg.selectAll("path").remove();
      // Set a light grey class on old paths
      svg.selectAll("path").attr("class", "old");
      var path = svg.append("path")
        .attr("d", line(data))
        .attr("stroke", "darkgrey")
        .attr("stroke-width", "2")
        .attr("fill", "none");
      var totalLength = path.node().getTotalLength();
      path
        .attr("stroke-dasharray", totalLength + " " + totalLength)
        .attr("stroke-dashoffset", totalLength)
        .transition()
          .duration(4000)
          .ease(d3.easeLinear)
          .attr("stroke-dashoffset", 0)
          .on("end", function() {
            if (i<6) {repeat();}
          });
      i++;
      console.log(i);
    };
    repeat();
  </script>

Green in a couple of seconds. Go.

I throw my weight into my handlebars, and push hard on the pedals. It's safer quickly off the line. It's safer ahead. I’m not rushing or racing, I just have to work with that gear ratio to gain momentum. MAMIL\* who joined me is far behind but will catch me once he picks up speed. Only if there’s no traffic, that is. Otherwise, the road is mine...

------------------------------------------------------------------------

\*MAMIL: Middle-aged man in lycra
