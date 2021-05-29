---
date: "2020-11-25T00:00:00Z"
description: null
image: null
title: "Portfolio case study: Machine learning's take on Brexit"
---

**An original data-driven experiment looking at how Brexit splits the Tories. Modelling of a dataset to test a hypothesis.**

---

### Project course
The project came to be as a backburner piece for my contribution to the Europe, Middle East and Africa Reuters file: a kind of backgrounder, explainer story we could mention and push out again every once in a while.

The central question was whether we could back up the feeling Lobby reporters had that there were several groups of Tories, so-called "tribes," with different attitudes to Brexit — while Labour parliamentarians were relatively united in pushing back against Theresa May's deal.

**[The main Reuters Graphics story](https://graphics.reuters.com/BRITAIN-EU-LEADER/010092Q33KW/index.html)** studied 12 key votes on amendments to the deal, which were fascinating as they reprensented new ideas from parliamentarians about what to do about Brexit.

**[I also published a follow-up looking at 238 votes](https://blog.basilesimon.fr/2019/10/06/brexit-machine-learning/)** and feeding the records to a machine learning algorithm, which as it was a lot more speculative was not Reuters' cup of tea.

---

![](assets/tsne.svg)

## t-SNE for machine mapping of Brexit personalities
Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.  Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam, dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.  Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.  Vestibulum convallis, lorem a tempus semper, dui dui euismod elit, vitae placerat urna tortor vitae lacus.  Nullam libero mauris, consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo sit amet elit.

tktktk


---

![](assets/brexit-split.png)
![](assets/brexit-decision-tree.png)
![](assets/brexit-rift-reuters.png)

## A decision tree through original solutions to Brexit
tktktk
Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.  Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam, dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.  Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.  Vestibulum convallis, lorem a tempus semper, dui dui euismod elit, vitae placerat urna tortor vitae lacus.  Nullam libero mauris, consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo sit amet elit.


---

### Data work and modelling
To make out groups of MPs, we looked at their voting record. I'm forever grateful to [Evan Odell](https://evanodell.com/), who maintains R packages I've used through my time in news.

[@evanhodell/hansard](https://github.com/evanodell/hansard)'s was used to fetch a bunch of data from an original [Institute for Government](https://www.instituteforgovernment.org.uk/) research, which highlighted recent Brexit-related votes.
