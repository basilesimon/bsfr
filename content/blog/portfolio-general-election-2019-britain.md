---
date: "2020-11-08T00:00:00Z"
description: null
image: https://blog.basilesimon.fr/assets/ge2019-header.png
title: "Portfolio case study: Reuters' 2019 general election results page"
---

![Intro to GE2019 page screenshot](assets/ge2019-header.png)

**A node backend and a modular, reactive front page visualising the UK general election results, as they happened. For Reuters Graphics.**

Unfortunately, this page was deleted from the internet.

---

## Front end: the results page

The page was built to be modular, i.e. to work this way:

- clients must be able to pick and choose which graphics they want, from one of them to all of them,
- there is only one repository of code I update and push out to clients.

So the main app itself is broken down into sections which are totally independent from one another.

The root of the main app, which all clients will run, is then quite minimal in terms of data processing, as it does not need to worry about what kind of data wrangling the modular sections downstream require.

---

### Selected graphics
**A blue wave... if you don't know where to look**   
For the results map, we weren't quite ready to commit to cartogram only, for fear that our very international audience wouldn't quite recognise the country.

I felt it was an important thing to include, though, since urban/rural voting patterns are quite different in the UK, and Labour's importance is visually underwhelming otherwise.

So I built both, and I'm particularly proud of I managed to run 650 [tween interpolators](https://github.com/d3/d3-transition#transition_attrTween) at the same time to transition between the two states. [Noah, thanks for Flubber](https://github.com/veltman/flubber) once again!

<video autoplay loop muted playsinline class="video-background" style="width:100%">
  <source src="assets/ge2019-maps.mp4" type="video/mp4">
</video>

<div style="margin-top: 70px"></div>

**Visualising change and who won from whom**  
I'm no stranger to ternary plots, which allow to plot three dimensions in an Euclidean space, in 2D. I think The Economist did a chart like this just before the election (if it was you, please email me a link :)).

I wanted to show the swing and who picked up seats from whom, but we weren't sure how the night was going to play out, and it would have looked very empty for a while. So this was done live and added as a hot commit overnight. And I'm quite pleased (in a non-political way) about how well it shows Labour losing seats to quite literally everyone.

![Screenshot of the GE2019 ternary charts](assets/ge2019-ternaries.png)

<div style="margin-top: 70px"></div>

And finally, the classic barcode references, which I think do a decent job of conveying the general sense of distribution (and outliers) as well as the general picture.

![Screenshot of miscellaneous bits of the GE2019 page](assets/ge2019-misc.png)


---

## Backend
The backend I put together was two-fold:

* A `bash` scraper polled the PA's FTP server for data they'd put out (yes you read this right: FTP) and would mirror and version this data to our `S3` buckets,
* A `node` app would then poll these buckets and take it from there.

In this instance, the role of the backend is to build up, from all the XML files dropped by the PA, a JSON-like representation of the election results as they currently stand.

There are quite a few hoops to jump through and hurdles to clear, such as recounts and corrections, and unfortunately this process can be quite manual (e.g. file names) or edge cases (e.g. the Speaker's constituency is handled differently by different news organisations).

---

## Inception and duties
I designed, built and maintained this project, under the careful editing of Simon Scarr.

We had code reviews and handovers with colleagues in other offices (Bangalore, Singapore, New York City) in case I'd be incapacitated, or if I needed a rest overnight.
