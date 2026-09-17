---
aliases: ["/2014/08/01/data-stringers/"]
date: "2014-08-01T00:00:00Z"
description: "WTF data-stringer? Who knows what a data-stringer is? A quick Google search reveals that only a couple of people actually use this word. I was introduced…"
tags: []
title: "Building a datastringer"
---
## WTF data-stringer?
Who knows what a *data-stringer* is? A quick Google search reveals that only a couple of people actually use this word.

I was introduced to this esoteric thing in November, during a Hacks/Hackers(1) meetup. OpenNews fellow [Annabel Church](https://twitter.com/annabelchurch) was running a workshop about... well, here's her definition of a data-stringer:

>Stringer journalists are freelance reporters that create news stories from remote countries or crisis zones. Data stringers, in a similar way, are small computer programmes that live in a remote data feed and ask routine journalistic questions of that data. Keeping track of what is happening in government or business, they can trigger notifications whenever events of journalistic significance occur.

Computer-assisted journalism level [> 9000](http://blog.sheasilverman.com/wp-content/uploads/2014/05/tumblr_lwhv2roIab1qd47jqo1_500.gif).

## Getting the idea
Anyway, [Iain](https://twitter.com/iaincollins), [Michael](https://twitter.com/miertl), [Massimo](https://twitter.com/ma_paradiso), and I pitched an idea for a stringer which would gather housing data, cost of living indexes, and energy prices, to notify a journalist about a certain raise - the topic is very popular in London, where prices are going bananas these days.

The idea stayed in my mind for some time, but I'm at it again, joined by [Clément](https://twitter.com/5c2v), a software engineer friend.

Annabel actually published a tool to create data-stringers, called [Datawi.re](https://github.com/pudo/datawi.re/blob/master/README.md). However, I find the requirements too high for the layman journo, who is no sysadmin. Keeping that in mind, Clément and I will try to design something easier to grasp and use.

## Proof of concept
I won't have much time, as I would like to showcase the project to OpenNews mid-August. Hopefully, it will be enough to produce something at least decent.

So, we are going to take three different data sources:

* Three ways to query them
* And three types of results

And... try to build a proof of concept prototype which would be rather simple to scale and adapt to other types of sources. So far, we went for [Police.uk](http://www.police.uk/) Rest API, which sends us nice and simple JSON files with street-level crimes and news in your neighbourhood, and also a set of [Gov.uk](https://www.gov.uk/) PR releases, powered by an Atom RSS feed. The third source is likely to be a numbers-only CSV dataset.

## Wanna help?
The project is open-source, so if you want to get your hands dirty or simply have a look at how we're doing, head to the [Datastringer repo on Github](https://github.com/basilesimon/datastringer).

It will be much appreciated!

---

*(1) If you don't know Hacks/Hackers, head to the website to find a [local chapter](http://hackshackers.com/chapters/) in your city. The goal of these meetups is to put together in a room journalists and hackers, to "reboot journalism", and "rethink the future of news and information."*
*It's a vibrant initiative, and the London chapter is taking us to incredible offices for talks and drinks. Do join!*
