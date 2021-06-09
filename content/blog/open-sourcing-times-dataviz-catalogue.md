---
date: "2017-12-18T00:00:00Z"
description: 'We are happy to share the first version of our data visualisation catalogue: a collection of data visualisations created for the Times and Sunday Times, collected together in one place in the hope that what we have learned can be useful to others.'
image: https://basilesimon.fr/assets/catalogue.png
title: Opening The Times Dataviz Catalogue
---

![](assets/catalogue.png)

Today, we are happy to share the first version of our data visualisation catalogue: a collection of data visualisations created for the Times and Sunday Times, collected together in one place in the hope that what we have learned can be useful to others.

Our goal is to compile and showcase the best of our burgeoning data visualisation work, rather than to offer a taxonomy of visual journalism (the FT’s Visual Vocabulary is a fantastic resource for that).

This collection will also be used internally as a training resource to upskill members of our digital team. From reporters to editors, developers and designers, understanding the correct way to visualise a data set is crucial to enhancing our stories and bringing them to life online.

The catalogue is both a publicly accessible website showing the breadth of our work, and a [Github repository](https://github.com/times/dataviz-catalogue) allowing developers to understand how they are built.

---

## Two audiences?

[The website is a great starting place](https://times.github.io/dataviz-catalogue/) for showcasing our work and a resource we intend to grow over time. The website can also be used to [crowbar](http://nytimes.github.io/svg-crowbar/) SVGs out for additional Illustrator massage — think of it as a hiring tool and a style guide.

We display only one chart per page to keep things clean, and we’re publishing everything on Github so you can clone the code and see a data visualisation’s evolution there too.

![](assets/catalogue.gif)

README files for each type of chart provide handy details about the data format we have implemented. As a growing number of journalists become proficient with basic data manipulation, we wanted to fulfill this requirement directly.

---

Frequent practitioners will notice that the code is kept very simple. This is a purposeful decision, and following conventions and habits (particularly around d3.js). In doing so, we aim to make our code more familiar, and hopefully easier to experiment with.

The only notable exception to what remains common in d3 world is the use of ES6. The elegance of arrow functions, the relatively wide cross-browser support, and the broad adoption of tools like Babel to cater for those browsers that don’t fully support ES6 should convince everyone to make the switch.

```js
/*
 * d3.extent returns a [min,max] array
 * /

var xExtent = d3.extent(dataset, function(d) {
  return d.Age;
});

// in ES6:
const xExtent = d3.extent(dataset, d => d.Age);
```

As mentioned previously, the whole project is [on Github ](https://github.com/times/dataviz-catalogue/)and we intend to continue improving it. You can also check out our [list of issues](https://github.com/times/dataviz-catalogue/) and see where we’re headed.
