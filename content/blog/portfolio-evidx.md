---
date: "2026-04-13T00:00:00Z"
tags: [portfolio, viz]
title: "Portfolio: evidx – web evidence preservation for journalists"
---

<video src="https://www.evidx.de/demo2.mp4" autoplay loop muted playsinline style="width: 100%;"></video>

**A cryptographic web archiving tool for investigative journalists and newsrooms — co-founded and built with investment from MIZ Babelsberg.**

---

### The problem

Web content disappears. Pages are edited, deleted, taken down — often precisely when they matter most to a story. For investigative journalists, that creates a chain-of-custody problem: how do you prove that what you saw on the web is what you're reporting on?

Existing archiving tools weren't built with journalists in mind. They're public-by-default, don't support paywalled or authenticated pages, and offer no cryptographic proof of integrity.

---

### What evidx does

evidx lets journalists capture any web page directly from their browser — including authenticated, paywalled, or ephemeral content — and produces a tamper-evident archive with a cryptographic signature and a server-witnessed timestamp.

Archives are stored on the newsroom's own infrastructure. Nothing goes to a third-party server. The chain of custody stays in-house.

Key features:
- **One-click browser capture** into the open [WACZ](https://specs.webrecorder.net/wacz/latest/) archive format, with interactive replay
- **C2PA cryptographic signing** — the standard used by major international newsrooms and news agencies
- **Server-witnessed timestamps** for legally meaningful chain-of-custody documentation
- **Private by default** — on-premises deployment, GDPR-compliant, built in Germany with eIDAS in mind
- **No vendor lock-in** — built entirely on open standards

---

### Building it

evidx is co-founded with Niko Para (co-founder of Syrian Archive) and Tilman Miraß (formerly at Deutsche Welle), bringing together expertise in digital forensics, open-source archiving infrastructure, and newsroom tooling.

The project is backed by [MIZ Babelsberg](https://www.miz-babelsberg.de/) and Germany's [Prototype Fund](https://prototypefund.de/).

I lead product and engineering, drawing on prior work in digital evidence at Stanford's Starling Lab and the [Digital Evidence Toolkit](https://digitalevidencetoolkit.org/).

---

[evidx.de →](https://www.evidx.de)
