---
aliases: ["/2014/02/10/ddj-project-migrations-in-europe/"]
date: "2014-02-10T00:00:00Z"
description: "I'm glad to be back, and with some good news. Michael and I published a data-journalism project about the flows of migration in Europe. The idea came from…"
tags: []
title: "! 'DDJ project: migrations in Europe'"
---
![](/assets/Screen-Shot-2014-02-10-at-12.59.57.png)</a>

</p>

I'm glad to be back, and with some good news.

Michael and I published a data-journalism project about the [flows of migration in Europe](http://basilesimon.fr/projects/immigration/index.html). The idea came from Michael, one night in our favourite pub. We drew the first sketches on the back of a bill, analogue-style.

The project is basically a compilation of public data from the national offices of statistics of ten European countries, and aims to paint a more precise picture of migrations on our continent.

It was the occasion for me stick my toes into Javascript for the first time, through the Canvas.js library, as I was just completing the Codecademy's JS course at the moment.

Still, many problems we had were caused by the library and by my limited skills in Javascript.\
For example, the arrows appearing when hovering the countries are PNG images, and not dynamically drawn SVGs. Nope, they're just stupid images refreshed with this small function

\`\`\`javascript var dataPoints = chart.options.data\[0\].dataPoints;   for(var i = 0; i \< dataPoints.length; i++){      dataPoints\[i\].mouseover = updateBackgroundImage;   } function updateBackgroundImage(e){ document.getElementById('chartContainer').style.backgroundImage = "url('" + e.dataPoint.imageUrl + "')";          } \`\`\`

Aligning them was quite a pain in the neck - as one can see when looking at the CSS. And let's not talk about the home-made responsiveness.

But in the end, the project may look like more hacking than proper development, but it works. And it works quite well, indeed!\
Showing it around allowed me to join the BBC News Lab, as well as the Centre for Investigative Journalism to work with Paul Bradshaw, and will maybe get Michael and I an internship in a well known and respected paper - that I'll not name here to avoid jinxing us.

The only regret we have is neglecting the journalism side of the story. We focused a lot of our efforts into the look and feel of the page, as well as the gathering of the data, and did not take the time to write a good story with an appealing angle.
