---
date: "2020-10-21T00:00:00Z"
image: https://blog.basilesimon.fr/assets/gw-full.png
tags: [portfolio, viz]
title: 'Portfolio case study: Global Witness'' Pipedown interactive map'
---

![Pipedown screenshot](assets/gw-full.png)

**An interactive map of natural gas infrastructure in the EU, built with Svelte and d3, for Global Witness.**

---

### Some context

The EU has a rule in place to regulate which electricity and fossil fuel projects it will financially support. These projects include the terminals and pipelines used to import and transport fossil gas – sometimes referred to as natural gas. Under this regulation, selected gas projects get fast-track approval and access to billions in public subsidies.

That's a law called TEN-E Regulation.

And it has a problem: it gifts remarkable power over EU policy to an obscure cadre of gas companies called the _European Network of Transmission System Operators for Gas_, or ENTSOG. Under the law, ENTSOG companies help the EU predict how much gas Europe needs and helps the Commission decide what gas infrastructure projects to support.

**Conflict of interest? Legal but non-virtuous circle?**

---

**For their campaign, Global Witness wanted to visualise all the gas projects the EU has subsidised, and how much projects backed by these ENTSOG companies have received.**

### Project course
From a rough interactive map prototype, I pitched a stack proposal and a five-day contract, which I worked over three or four weeks.

I focused on the complex interactivity first, bringing in styles from GW's guidelines as we went along. We kept the show on track with frequent reviews, which were helpful but greatly helped by the fact that we were all on the same page and that my proposals and initiative seemed to be appreciated.

We kept some on-call hours for publication day, but it all went smoothly.

---

### Visual density and jargon
The campaign is aimed at European lawmakers or persons of influence. Folks who know about a particular country, or particular infrastructure projects, and who _will_ want to know the precise names and amounts.

So we're getting away with this kind of rather busy display, which has the merit of displaying _a lot_ of information, though it's rather wordy:

![](assets/gw-bulgaria.png)

### Link in place
Readers can link to a specific country, as well as tweet some pre-defined patterns of copy which are also country-specific. Here again, we're helping the MEP tweet out their outrage about projects in their country.

### Explorable, clickable, hoverable
This is where reactive programming patterns really help:

We use [Svelte](https://svelte.dev/) to set up a central, app-wide source of truth, which the different components and views can access, and sometimes edit.

This allows us to have different behaviours at different moments. For example:
+ When looking at the European level, we don't highlight and can't click the individual projects ; but we can do so at the country level.
+ We display different data depending on the country highlighted. For the Trans Adriatic Pipeline, a Belgian MEP will see the funding of Belgian ENTSOG companies ; an Italian will see their side of the projects, and so on.
