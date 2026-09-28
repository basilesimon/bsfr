---
aliases: ["/2016/10/26/learning-react-in-2-weeks/"]
date: "2016-10-26T00:00:00Z"
description: "I was apparently bullied into opening an account on Medium (for the second time). This content is mine, not theirs, so I reproduced it below. For those…"
tags: []
title: "From Medium: Learning React in 2 weeks"
---
*I was apparently bullied into opening an account on Medium (for the second time). This content is mine, not theirs, so I reproduced it below.*

![](https://d262ilb51hltx0.cloudfront.net/max/1600/1*uEs18QFmWRaLh0mA3bZZ2g.gif)

For those who know as little as I do: the Ryder Cup apparently is a golf competition between teams from Europe and the USA. Despite some jargon in this article, this piece is not about golf at all. If you’re disappointed and want to hear about Team Europe’s prowesses*, I’ll refer you to The Times’ coverage of the competition.

Indeed, we’ll rather discuss passing data through state and props up and down the components ladder than foursomes, singles and fourballs.

Because, you see, a week or so into my new position at *The Times* and *Sunday Times*, this larger-than-usual project about the Ryder Cup came up, and as some of my colleagues were on leave or booked out, I had to give a hand.

Maybe I could learn React in the process ; maybe I’ll just have to, an unnamed colleague — Chris Hutchinson — proposed without really leaving me a choice.

Heck, I figured ; React will go well with my beard, my fixie, and my home-grown sourdough culture.

*note: they lost. 17–11.*

---

A bit of context: React.js is an open-source Javascript framework, maintained by Facebook. React is pretty much used everywhere these days, and it embodies the hype in web-dev communities.

I had a few things to get started on this interactive newsgame project:

* The (brilliant) React docs
* And a template app implementing a basic ticker component.

I found the docs to be actually very good and useful. ["Thinking in React"](https://facebook.github.io/react/docs/thinking-in-react.html), in particular, was an excellent read that really allowed me to understand what I’d have to do and how I’d go about doing it.

---

Designing a (provisional) components structure was super valuable in order to get to grips with the way to build an app with React.

I ended up tweaking it a little bit later on in the week, but it remained (surprisingly) stable for a quick day one draft.

The objective here is to structure your app into smaller chunks with clear and separate purposes. Most of them don’t need to know about each other, and the parents pass on properties and data to their children.

A navbar at the top, for example, doesn’t need to know anything about what’s happening below it, really. Your main container in charge of rendering and piloting your interactive doesn’t need to know everything that happens inside it at any given moment: you just need to tell it when and how to render which component. See below:

![](https://d262ilb51hltx0.cloudfront.net/max/1600/1*Q64Gq1jTV-IoibtI25YdMw.jpeg)

---

As usual, the best way to learn is to try your hand at building something. For me, this was the landing page of [our game](http://thetimes.co.uk/rydercup2016). I started with the bare minimum: a navbar (already built) and a title, just to get the hang of the syntax.

![](https://d262ilb51hltx0.cloudfront.net/max/1600/1*1sPV25KVY-mQlDg42qGvmQ.png)

And so, after building the landing page, it soon became necessary to implement a team-picker functionality, so our users could choose whether they’d captain Europe or the US in the game. It probably took me two days before I got this working and passing the resulting data up to the app — a signal that the game itself had to be launched.

Don’t just copy and paste or jump to the line you want to edit: re-write everything, from `const React = require(‘react’);` to creating your component’s `Class()` and its mandatory `render()` method. The rationale behind this is that it will make you memorise these and understand how similarly your components are built.

Surely enough, as you do so you will gain confidence in seeing your data and variables flow down the fold and the methods you wrote two components up being triggered when you click a tiny button further down your app.

---

But do not get over-confident just yet, for your colleagues are looking over your shoulder and reading your commits; elegance and DRY still count.

I found helpful to refer to the hierarchy I drew on day one and to think about ownership of the different chunks of my project, and about which of these should know what.

> Does the main game view need to know the result at any given moment, or isn’t it better just to let it know the final result, as an instruction for rendering the last result page?

Knowing where your data must live is helpful when it comes to building the separate parts. In the example above, I decided that the main game view needs not to know the result of every round at any given moment. This decision allowed me to build this game view as a container: it would start the game and let it run its course up to the point where the game would send back a full results list. The reception of this list is the signal that the game is over, and that the results page must be rendered.

Oh, and it must be rendered with — guess what? — the results data we just received!

---

Next stop on this two-week journey was confusion. React bundles Javascript and HTML into an unfamiliar XML-like soup — that compiles (transpiles?) to Javascript: [JSX](https://facebook.github.io/react/docs/jsx-in-depth.html). If you feel strongly about writing vanilla Javascript, you don’t have to write your code in JSX, but again… why miss out?

Well, for one, you may be utterly confused for a while about what you’re actually writing. I mean, check this bit out of the official docs:

> Since JSX is JavaScript, identifiers such as class and for are discouraged as XML attribute names. Instead, React DOM components expect DOM property names like className and htmlFor, respectively.

Learn not to worry. You’re rendering components by writing them as HTML tags — or is it XML? — in your code, and if the Facebook folks think it’s good for you, then so it must be.

```
<GameContainer
    userTeam   = {this.state.userTeam}
    cpuTeam    = {this.state.cpuTeam}
    onFinished = {this.finished}
    finished   = {this.state.finished} />
```

I know. Missing Python yet?

---

In the end, your ability to write in React will be a function of your ability to think logically and to slice a problem into smaller chunks. Coming from a non-technical background myself and having picked up a little bit of coding at some point, learning how to think in a functional way and with inheritance over scope in mind was kind of a game-changer. This is to me the single great take-away of these two weeks.

The whole surrounding ecosystem I did not touch too much. At the Times, Chris has put together a generator that sorts you out with React and Webpack, as well as scaffolding a full project from scratch. Everything was there and ready, and it only took a bit* of pestering Chris to be up and running.

*note: a lot*

---

In short: React’s nice. Get hype. Try it. [Give it five minutes](https://signalvnoise.com/posts/3124-give-it-five-minutes).

*P.S. I still ignore much of what golfing is about.*
