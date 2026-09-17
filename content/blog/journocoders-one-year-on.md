---
aliases: ["/2016/02/15/journocoders-one-year-on/"]
date: "2016-02-15T00:00:00Z"
description: "It's been a little over a year since we started running the Journocoders meetup. We've organised 14 events in total, actually. Every month, we go through…"
tags: []
title: "Thoughts on the Journocoders meetup, one year on"
---
<img src="http://www.journocoders.com/img/logo.png" style="margin: auto">

It's been a little over a year since we started running the [Journocoders](http://www.journocoders.com) meetup. We've organised 14 events in total, actually.

Every month, we go through a tutorial explaining practically a different bit of tech deemed useful for modern journalists - *"people who like journalism and code,"* as we say.

The [list of topics we covered](http://www.journocoders.com) during this year goes from command line basics, cleaning data with Open Refine, d3 and charts things, API wrangling, mapping, Twitter bots, and scraping.

Our format is very much hands-on: aside from introducing what we're going to do and a little show-and-tell at the beginning, the session mostly runs itself as the attendees go through the tutorial on their own. We encourage people to try to find the solution to their problem by asking their neighbour (or us) for help.

Here are some thoughts on this experience.

---

### Dev environment == pain

We spend loads of time each month dealing with just getting people started with the tutorial, and we often have to mitigate the harder bits (eg providing the final topoJSON file if some were not able to go through its creation). That's because it's often a pain to have a working development environment set up when you're not too technical - or doing this for the first time.

Classic problems: getting to grips with the command line takes time. UNIX-style command line on Windows is horrible. You don't have a decent text editor installed. Nor do you have `node` and `npm`. Installing `node` and `npm` on Windows is horrible. You're missing `python` and `pip`. Installing `python` and `pip` on Windows is horrible. And you need `ruby` and `gem`. Installing `ruby` and `gem` is horrible.

So, yes, there are [great intros to setting up a working laptop for code things](http://blog.apps.npr.org/2013/06/06/how-to-setup-a-developers-environment.html). But many people show up with Windows laptops, and unfortunately our sessions don't allow for a solid hour of setup before getting diving into an interesting tutorial.

(Personally, I can only help with Mac OS X if it's command line-related, and I'm useless with Windows problems. Not in IT, sorry.)

---

### Not using the dev tools == not understanding a web page and the DOM

This is a literacy challenge I encounter very often when a participant is stuck with an error. Basic web inspection and `console.log()` will take you so far away in terms of debugging that they should be reflexes.

We never taught these basics, as we've never taught the programming basics of either language (I include HTML) in this one. That means that some people come with these skills while some don't. That means that some people are more autonomous than others.

And that there might be yet another set of things to figure out at an event, in addition to the tutorial topic and the dev environment shenanigans.

---

### A different language and tech every month

Since the very beginning, we've ran the meetup this way: every month, a new tutorial and a new skill under your belt.

After a year, we got the opportunity to come back to some of these and dive a bit deeper: our first event was about "Scraping with Python," and we proposed an episode two last month ; after an intro to d3 in September last year, we just came back to this vast topic to have a look at how to create maps.

This diversity is awesome for those who come regularly and thus get the full spectrum of the topics we choose. But let's face it, not all of our members come regularly. Some cherry-pick topics, some join us along the way. I'd say that only very few attended all of them.

And this is quite a big issue for us in terms of learning impact.

---

# How to fix?

* Encourage people to come more often, rather than cherry-picking subjects
* Encourage members to re-use what they've learned every month for at least one small project
* Find or create a large tutorial explaining how to set up a laptop running Windows, Mac OS, or Linux
* Keep going :)
