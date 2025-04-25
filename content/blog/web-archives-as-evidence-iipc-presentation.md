---
date: "2025-04-25T00:00:00Z"
description: How Starling Lab’s “Web Archives as Evidence” presentation at IIPC 2025 in Oslo leverages Hypercore and Hyperbee to deliver independently verifiable metadata for web archives.
image: https://netpreserve.org/resources/GAWAC2025-banner.png
tags: []
title: Web Archives as Evidence presentation at IIPC 2025 
---

I am pleased to have been selected to present at the [International Internet Preservation Consortium (IIPC) annual conference](https://netpreserve.org/ga2025/), which took place in April 2025 in Oslo. My talk provides a high-level overview of the work conducted over the past year by the whole team at the [Starling Lab for Data Integrity](https://www.starlinglab.org/) (co-founded and established at Stanford University and the University of Southern California). 

In this talk called “Web Archives as Evidence”, I presented our Authenticated Attributes (AA) prototypes to an audience of archivists and web archiving professionals, many of them from national libraries. 

The central proposition of AA is to be a database of authenticated key-value metadata pairs – much like a spreadsheet, but with independent and verifiable provenance for every cell. Also, it’s peer-to-peer replicated, and folks can subscribe to this feed of strong metadata. 

AA is built on [Hypercore](https://github.com/holepunchto/hypercore) and [Hyperbee](https://github.com/holepunchto/hyperbee), which work together to make sharing and finding information easy, fast, and secure:

- Hypercore is a distributed append-only log that forms the foundation of a peer-to-peer network. It enables the creation of efficient and cryptographically-secure data structures that can be shared and synchronized across multiple devices. This technology enables advanced features like hole-punching, enhancing connectivity even in difficult or firewalled network environments.

- Hyperbee is a distributed B-tree database layered on top of Hypercore, designed to store and retrieve key-value pairs with high efficiency. Think of it as an advanced filing system where information is systematically organised, making it easy to locate specific data quickly.

I am honored to be part of a session chaired by [Meghan Lyon](https://www.linkedin.com/in/meghanlyon) from the [Library of Congress](https://www.loc.gov/). Meghan has been actively involved in the IIPC community, chairing sessions at previous conferences, including the Web Archiving Conference in Paris in 2024, which I also attended.  

[The IIPC, established in 2003](https://netpreserve.org/), is a global organization dedicated to acquiring, preserving, and making accessible knowledge and information from the Internet for future generations. Its membership includes national libraries, archives, and other cultural heritage institutions committed to web archiving initiatives.