---
title: "Why I'm back to building the Digital Evidence Toolkit"
description: "Archive.today's tampering scandal cost Wikipedia 700K citations. Here's why newsrooms need independent, cryptographically signed web archives instead."
author: Basile Simon
date: 2026-03-25
---


Last month, [Wikipedia banned Archive.today and began removing close to 700,000 citation links](https://www.webpronews.com/wikipedia-blacklists-archive-today-after-alleged-ddos-attack-and-evidence-of-tampered-web-captures/). The reason was forensic evidence that the service had been quietly altering its own archived captures. As hard as it is to believe...

Archive.today was the _if-you-know-you-know_ resource for journalists and fact-checkers. [Its operators were always anonymous](https://www.heise.de/en/news/Hundreds-of-thousands-of-links-Wikipedia-bans-Archive-today-after-cyberattack-11185344.html), which felt like... a quirk, not a flaw? Turns out the opacity was the whole problem: the same people who ran the infrastructure could rewrite what it stored. An archive that rewrites history is not an archive. It's a liability.

[It's a story of loss and of misplaced trust in the commons](https://www.digitalevidencetoolkit.org/news/archive-dot-today-removed-from-wikipedia). And in the use cases which are deliberate research and investigations, it's not acceptable. That's what I set out to address when I started the Digital Evidence Toolkit back in 2021, then funded by the Prototype Fund. The premise hasn't changed: you cannot outsource your archive to the commons and hope for the best. The provenance has to be yours — cryptographically, legally, operationally.

Today, what's changed is the scope of what we're building.

I'm now working with Niko Para and Tilman Miraß who work together at [DOT•STUDIO](https://www.dot.studio/en/), supported by the [MIZ Babelsberg](https://www.miz-babelsberg.de/startseite.html), on a second, substantially more complete version of DEPT. It captures web content on your own machine, inside your own browser session — including paywalled and authenticated pages. It signs captures cryptographically, produces WACZ archives with full chain of custody, and lets you search through your own material. When you're ready, you can publish an authenticated, replayable embed of a source directly in your story.

When I say you: I mean your newsroom. It runs on machines / a virtual private cloud you manage, or on premises directly.

As for you, the investigator and your sources: nothing leaves your machine unless you decide it does. No third party holds your archive. No one can tamper with it.

If you're working on an investigation that depends on online sources, or you're thinking about how your newsroom handles this — I'd like to talk. It's election time in Europe, and there are plenty of use cases to collaborate on.
