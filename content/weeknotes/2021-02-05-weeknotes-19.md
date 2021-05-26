---
date: "2021-02-05T00:00:00Z"
published: false
title: 'Odd sketches - weeknotes #19'
---

The week started with [CVE 2021-3156](https://security-tracker.debian.org/tracker/CVE-2021-3156), which I patched across Global Witness' boxes with Ansible. Nice little tool, this! As the playbook grows, I wonder how folks keep track of what's in the toolkit?

Some progress on my portable, dockerised and backed-up install of Neo4J, but I've hit a wall while trying to integrate it with Linkurious. I've got a hunch that in fact I shouldn't have based this image on v4.2.0.  
Oh, and since we're using the free, "community" release of Neo4J, it's actually not full Docker: the database/container needs to be stopped anyway in order to safely take a backup 😔

And I belatedly met [Ben](https://twitter.com/BenAyre), Global Witness' new (and only) interactive developer. As such, he's going to work on building their stack -- and I am hearing he's quite the Observable fan... 😉

---

Sketching and storyboarding continues for Tactical Tech. Observable is such a good tool for this.

<iframe width="100%" height="1509" frameborder="0"
  src="https://observablehq.com/embed/@basilesimon/experiments-in-circle-packing?cells=ind_packed_bubbles%2Ctime"></iframe>

I'm still dealing with this very wide, sparse matrix of tags associated with companies (~1,000 deep and 250 across). Each company has several tags associated with it, and I'm looking for a general-purpose, explainable way of attributing each one with _one_ qualifier.

This week, I asked the researcher to reduce the size of our vocabulary of tags by going through them and applying Human Reasoning ™.

Meanwhile, I've been looking at different k-means clustering. Here are two sketches illustrating one cluster defined by the algorithm:

- The dendrogram represents the hierarchy and the distance between each tags, and is useful to spot lone branches or several clusters within the cluster.
- The heatmap focuses on distance between items and can be used to spot odd spots. This blue banding around item #30, after looking more in detail, is caused by these four companies being very closely related to image signal processing.

![]({{ site.baseurl }}/assets/dendrogram-cluster.png)
![]({{ site.baseurl }}/assets/heatmap-cluster.png)

---

Our demo of RadarTech got cancelled very last minute, which will only make the technical feedback I'm waiting for more overdue.

---

Had a good phone call with [Niko](https://niko.io/), who's joining Deutsche Welle's [Research and Cooperations](https://innovation.dw.com/) projects.

[Friedrich](https://twitter.com/pudo) and I braved the arrival of the snowstorm on Friday afternoon for a drinkie and a work catchup. Wherever you find yourself in Berlin, there's plenty of history to take in, and Friedrich is a nice guide. I did, however, catch a cold.

### Read and seen
- [Ramda patterns in React](https://tommmyy.github.io/ramda-react-redux-patterns/pages/react-ramda.html), by [@tommmyy](https://github.com/tommmyy)...
- Following [Easily integrate Ramda with into your React workflow](https://hint.io/blog/react-and-ramda), by Nate Shoemaker with nice real-world examples...
- Following the [Thinking in Ramda](https://randycoulman.com/blog/2016/05/31/thinking-in-ramda-combining-functions/) series by Randy Coulman.