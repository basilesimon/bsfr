---
date: "2021-02-11T00:00:00Z"
description: Hello d3-render, a lovely declarative library looking after the heavy lifting of the General Update Pattern
image: https://blog.basilesimon.fr/assets/share-render.png
title: Some declarative, React-like logic for your Observable/d3 toolkit
---

<iframe width="100%" height="584" frameborder="0"
  src="https://observablehq.com/embed/@basilesimon/hello-d3-render-a-declarative-wrapper-around-d3s-update-pat?cells=chart"></iframe>

Earlier this week, as I was looking into idiomatic ways of updating a chart, I came across [Kaho Cheung](https://github.com/unkleho)'s [d3-render](https://github.com/unkleho/d3-render) -- and boy did I get excited.

`d3-render` packages up a bunch of `d3` commands in a declarative shell, inspired by a eather functional and reactive approach. [@unkleho has got a lovely tutorial](https://observablehq.com/@unkleho/introducing-d3-render-truly-declarative-and-reusable-d3) introducing the library, but here's another one from yours truly anyway.

---
## Implementation
It's going to work this way:

- Our chart is just an `<svg>` element with a timer calling...
- A `draw` function, which draws on an DOM element from an array of objects-like variable. More precisely, it `map`s over each and renders...
- A component-like DOM element for each item in the `map`.

Our components obviously need to be defined and crafted, but we do so at a higher, more declarative level, while `d3-render` looks after the update pattern and the details.


### "Our chart is just an SVG with a timer which calls..."
```js
chart = {
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]);

  let i = 0;
  while (true) {
    await Promises.tick(900);
    yield svg.node();
    drawData(
      svg,
      data.map(e => ({ ...e, value: Math.random() * e.value }))
    );
  }

  return svg.node();
}
```

### "A draw function that maps over data to render..."
```js
drawData = (selection, data) => {
  const root = pack(data);

  const arrayOfBubbles = root
    .descendants()
    .filter(d => d.depth > 0)
    .map((e, i) => {
      const { x, y, r } = e;
      return CircleComponent({
        key: e.data.title,
        cx: x,
        cy: y,
        r: r,
        fill: e.data.group
      });
    });
  render(selection, arrayOfBubbles);
}
```

### "A component-like DOM element for each map item"
```js
CircleComponent = ({ key, r, fill, cx, cy }) => ({
  append: 'circle',
  key,
  r,
  fill,
  cx,
  cy,
  fill: color(fill),
  duration: 1000,
  delay: Math.random() * 50
})
```

---

### Background
The [General Update Pattern](https://observablehq.com/@d3/general-update-pattern) is a commonly-referred to implementation of d3's updating and reactive abilities.

In Observable world, it's Michael Freeman's implementation of the new d3 `.join()` that I was referred to. Here's what the same chart would have looked like in this world -- and bear in mind that you'd have to write a lot of this imperative code for each group of elements in a more complex chart.

```js
oldchart = {
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]);

  svg.node().drawData = function(data) {
    const root = pack(data);

    const circles = svg
      .selectAll('circle')
      .data(root.descendants().filter(d => d.depth > 0));

    circles.join(
      enter =>
        enter
          .append('circle')
          .attr('cx', d => d.x)
          .attr('cy', d => d.y)
          .attr('fill', d => color(d.data.group))
          .attr('r', d => d.r),
      update =>
        update
          .transition()
          .duration(1000)
          .delay(Math.random() * 50)
          .attr('cx', d => d.x)
          .attr('cy', d => d.y)
          .attr('fill', d => color(d.data.group))
          .attr('r', d => d.r)
    );
  };

  return svg.node();
}
```
```js
{
  let i = 0;
  while (true) {
    await Promises.tick(900);
    i++;
    oldchart.drawData(
      data.map(e => ({ ...e, value: Math.random() * e.value }))
    );

    yield oldchart.nodeName;
  }
}
```
