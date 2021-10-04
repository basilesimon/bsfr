---
date: "2021-04-09T00:00:00Z"
published: false
title: 'Friday already? - weeknotes #28'
---


Wait, is it Friday already?

---

Tactical Tech work shaping up. Now talking about publication with the Product and Infrastructure people over there.

Funny feeling when you tell someone your web app fits in 3MB of static files. No database, no container, no companion microservices. You can almost hear them breathe a sigh of relief.

---

As I was telling [Paul](https://paul.cx/) earlier today, I'm looking forward to being done with this project so I can talk about other things...

---

As problems come in pairs, Audrey and I are working towards a deadline next week to re-architecture quite a few things in RadarTech as the requirements have changed. I mean "evolved."

Terminology aside, it's not a web app talking to a database any more, we need to support several tables (one shared, the others exclusive) which models and accompanying frontends are created from a kind of seed JSON-like file.

It's more work for us, not because abstractions are harder, but because we had not planned on supporting this use, and bolting something abstract on to another system means faffing with it.

### Read

[There was a new release of ClojureScript](https://clojurescript.org/news/2021-04-06-release), and there's some love shown [on HN](https://news.ycombinator.com/item?id=26713329). Note how prominent is the past tense in the comments. As @pizzeriafrida puts it:

> _And this was all years ago now. All that excitement and progress and effort seems to have been trapped inside of Typescript, and React hooks, and did everyone forget?_
