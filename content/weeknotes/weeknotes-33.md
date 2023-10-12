---
date: "2021-05-14T00:00:00Z"
published: false
title: 'Good busy and Toolkit progress - weeknotes #33'
---

It was a really fun week, I think. Don't get me wrong, it was busy – but maybe the _right kind of busy_ ™️.

I even managed to squeeze in an afternoon in the park on baby duties, taking in the sun (which did not last) and chatting with Fellow Young Parents about our common experience.

---

I spent a bit more time designing the Digital Evidence Toolkit – as in, from the problem-definition and breaking up perspective:

- What problems are we trying to solve here?
- What does _this_ problem actually consist of? What about _that one_?
- Can I break these into smaller problems?

I'm also adding constraints in there. Having but little time to do something is one ; another is that I'm not a software engineer or legal expert by trade but that these two domains are principal components of my problem.

The progress made delights me, however. I hope to share some news soon.

---

Speaking of sharing news (and I alluded to it last week), I'm the final stages of bringing in a researcher to do some ground work for me – including back-tracking and taking the time to explain what it is I'm doing here.

I think I'm realising that once I've worked something out (for myself) I happily move one without ever spending the time to explain it. That may be why I'm not great at The Twitters and The Social Media.

---

The Data & Investigations team I support at Global Witness launched a new piece from the [Forests campaign](https://www.globalwitness.org/en/campaigns/forests/), which aims to raise awareness of the destruction of climate-critical tropical forests.

You can punch in a (British) postcode [in the interactive](https://www.globalwitness.org/en/campaigns/forests/how-long-would-your-local-park-survive-deforestation/) and let Ben show how quickly your local park would disappear... in real time. Mind-bogglingly scary stuff.

I did some load-testing with [Artillery](https://artillery.io/), a tool I had wanted to try for a while. Initial thoughts:

- It lived up to my expectations of simplicity... and customisation
- I may have over-tested a bit. I don't think we were quite looking at these 3,000 signups in 10 minutes 😇

And an oddity cropped up in our CloudFront CDN distribution: readers in Belgium, Denmark and Germany were reporting missing Origin headers and thus pages failing to load. The whole distribution wasn't including these headers, right. I only tested for half an hour but I did quite a few other countries, and only in these three did I find systematic failures.

Curious.

### Read
- [“What I learned roasting 200 landing pages in 12 months”](https://blog.roastmylandingpage.com/landing-page-roasts/) - a small business success story with boat-loads of valuable lessons for anybody who's got a shopwindow website
- [The Berlin Flat Quest](https://www.settle-in-berlin.com/berlinflatquest/) - a newsgame with lovely aesthetics about [“collective frustration”](https://www.settle-in-berlin.com/berlin-flat-quest-the-game/)
