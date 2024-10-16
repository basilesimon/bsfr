---
date: "2021-01-22T00:00:00Z"
draft: true
title: "More work helps - weeknotes #17"
---

Big work week in response to the workload (which I'm very happy about!). I worked four afternoons and probably will work Saturday's, as well as a couple of evenings.

---

Audrey and I are putting the finishing touches on the first draft of RadarTech, this survey for the French administration. Big deal for me: I've relied on [SurveyJS](https://surveyjs.io/) to render the survey and do the accessibility work -- if we end up not happy at all with the way it works, I might have to fall back to writing the whole thing manually 😱

---

Second half-day work for Global Witness. I spent some time auditing the AWS infrastructure to get a sense of where we are weird policies and roles-wise.

I'm managing some parts through Ansible already, and I'll be looking to beef that up and to expand the scope of the automated maintenance and reporting tools.

They've got an interactive dev starting shortly (the first on the Data Investigations team) and I look forward to supporting their work as well as the team's tooling.

---

The exploratory work for Tactical Tech continues. The more I look at this data, the more I think we'll be looking at a fancy scrolly thing.

In the meantime, I've put together a tool for the project's researcher. They can toss the dataset in there and play with common machine learning algorithms, hopefully echoing their domain knowledge.

![tsne output]({{ site.baseurl }}/assets/a-tsne.png)

It's a bit useless without the data (which I can't share yet) but [here is the Observable notebook](https://observablehq.com/@basilesimon/explorations-in-d3-and-druid-js), which makes good use of [DruidJS](https://github.com/saehm/DruidJS/), a new JS lib for dimensionality reduction.

### O'Reilly books I wish existed

- _Docker to deploy things - for those who missed the boat_
- _Ansible without breaking everything_

### Read

["Have you ever noticed that feedback is implicitly considered to be right, when it’s purely opinion?"](https://twitter.com/jasonfried/status/1344364060679184384) - @jasonfried, from David Bauer's Weekly Filet (https://weeklyfilet.substack.com/)
