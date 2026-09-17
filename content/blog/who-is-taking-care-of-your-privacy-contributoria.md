---
aliases: ["/2014/10/01/who-is-taking-care-of-your-privacy-contributoria/"]
date: "2014-10-01T00:00:00Z"
description: "Maybe you've read it already, but I wanted to re-publish my Contributoria article here. It feels really great to be supported by this crowd-funding…"
tags: []
title: "Long read - Who is taking care of protecting your privacy?"
---
Maybe you've read it already, but I wanted to re-publish my Contributoria article here. It feels really great to be supported by this crowd-funding scheme, and I am very grateful to all the persons who backed my story.

Meeting with Frederic was a very pleasant and rich experience. This led me to reconsider the format of the piece, to finally choose a profile with a small narrative in it instead of a rather boring Q&A.

But more importantly, I liked what we talked about. I enjoyed our interaction. And I loved writing this piece, partly at the airport, then in the plane, and finally in London, at home.

Fortunately, Contributoria offered me a platform to do that - i.e. to get some future money in to pay for my trip to Switzerland, through the system of crowd-funding.

It is pretty good, if you think about it. When was the last time you sat down with a good idea, proposed it to the world or to a community, and got a little bit of money to realise it?

That's just amazing. I tried to explain the system to my family, but the only asked about what would happen if I didn't do anything, or if it wasn't good at all. The fact is that, once the proposal is funded, I feel responsible in front of all the backers. I'm not the only one: my good friend Michael, who published this fantastic piece on child labour in Bolivia after a long stay there, turned down work to have time to properly write his article.

I hope that I will be given the same amount of trust in the future through this platform, because I will definitely propose more. This interview gave me tons of ideas, and, with your support, I will be able to pursue them and write about some of them.

**Thank you. Really.**

***

![venn](/assets/venn.jpg)

**Several times this year, I found myself in a room with other guys, discussing our latest ideas to “save the world”, to “make it a better place.” As you might imagine, the revelations of former NSA contractor Edward Snowden about mass-surveillance, eavesdropping, and interception led us to reconsider the secrecy of our communications, and of privacy in general.**

**I personally never considered my communications safe from interception, but:**

*   **I imagined that these things were targeting individuals in particular,**
*   **I thought I wasn't worth the trouble,**
*   **And I was preaching the “I've got nothing to hide” theory.**

**Snowden, Greenwald, the Guardian, and all the others proved all this wrong.**

**Despite all our worthless chit-chats, not-so-worthless pro-privacy campaigns, and prestigious prizes awarded to outstanding journalistic reportings on the matter, nothing much has changed since last summer, when the world discovered with more of less interest and indignation what the US's NSA and the UK's GCHQ, among others, were doing with their citizens' data.**

**Still, for many people around the world, your privacy is worth fighting for. Some are even smart enough to think of ways and to design software to help you protect yourself a little better.**

---------

*"Basile?"* I hear behind my back. I am standing outside Lausanne station, in Switzerland, after a 40 minutes train ride from Geneva. A beautiful train ride, I might even say, although I reckon that not everybody loves trains as much as I do; on the right-hand side, the massive Lake Léman, and on the left-hand side, gigantic modern design houses.

The man I am not waiting for anymore is [Frédéric Jacobs](https://twitter.com/FredericJacobs), from [Open Whisper Systems](https://whispersystems.org/), who is a student at the prestigious Ecole Polytechnique Fédérale de Lausanne (EPFL). I had no reception on my phone, and the sole clue he had was that I was wearing a blue polo shirt. We exchange salutations in French, despite our previous communications in English. *"Shall we speak French?"*, he asks, without any kind of Belgian accent.

It's a marvellous sunny day, and we settle on the terrace of a restaurant. The conversation starts right away about SS7, the protocol used by all mobile providers to handle texts. According to Frédéric, it is simply completely broken, and offers no security whatsoever to its users, i.e. every mobile phone user in the world. Companies even establish themselves in Eastern Europe to register as (fake) phone providers to obtain a license to connect to this network, monitor its usage, the users' geo-localisations, and the content of these texts... to sell it - to whoever is ready to buy, explains Frédéric. Talk about a proper start.

We both order the cheeseburger. While I resolve to give a shot to the local beer, the *Lausannoise*, he gets an apple juice. I finally get to have a closer look at this young 22 year old, with already a great reputation in the cryptography and infosec communities. He is proudly displaying a black crow on his t-shirt - the Open Whisper Sytems logo. We are wearing the same Pebble smartwatch, and his half-long golden hair remind me of my brother who studied in the same school.

Frédéric is in practice still a student at EPFL's Computer Science department, currently in his Bachelor's last year. He earns roughly half of his university credits by taking regular classes, and the other half by doing research at EPFL's Cryptography Lab.

He is also co-leading the iOS development of Open Whisper products, which include TextSecure, an app encrypting texts, and Signal, an app encrypting phone calls. He made no mention of a packed schedule, though, which I take as a sign that he can handle several occupations as well as he manages to eat his burger while providing long and detailed answers to my questions.

He enjoys doing research. *"Plus, cryptography may be one of the rare spots where academia is more advanced than the industry."* How advanced? To the point of designing algorithms capable of resisting attacks by quantum computers, a project he is taking part in.

*"My background in Computer Science is actually pretty useful: it makes me think about implementation and usability rather than in terms of pure maths."* Frédéric, and Whisper Systems in general, insist on delivering a *"usable cryptography"*, one that can be used by everybody. Without even talking about the old PGP protocol (which stands for Pretty Good Privacy), which he considers outdated and even insecure to a certain extent, the key to a more massive adoption of advanced cryptography solutions is usability.

But even considering that there would be an *"ideal"* solution on the market, the idea of protecting one's privacy online must also make his way. I told Frédéric the now classical argument given by those who dismiss privacy concerns: *"I've got nothing to hide."* He reaches over the table, palm facing the sky: *"Then, can you give me your phone?"*

> *"You use your phone for everything, from talking to your friends, your girlfriend, to very often do your job. Are you sure you never sent credit card or bank information by email? Would you mind if your private conversations appeared online?"*

Having the NSA scandal in mind, I provoke him by replying that I trust my State and civil servants not to steal from my bank account should they gain access to it. There are no mentions of such cases in the Snowden leaks (as far as I know).

But Frédéric warns that it is important to be very well aware that there are multiple threats, and that the NSA might not be the biggest. *"If an intelligence agency can steal your data, gain access to your devices or account, so can some other people."* No, the NSA would probably not leak your private pictures online. But evil or irresponsible hackers might (I insist on the adjectives here). That is precisely what happened a couple of weeks ago to a dozen of celebrities.

The fact that these threats are real is a given. As he told last year to [Apache](http://www.apache.be/fr/2013/11/26/frederic-jacobs-le-hacker-belge-qui-rend-la-cryptographie-accessible-au-grand-public/)], there are several ways to react and to handle these: the first one is passing legislation that prohibits practices as such revealed by Edward Snowden. However, the citizen is protected neither against abuses made by the administration, nor against those willing to break the law.

The second one, cryptography, is the only way to protect yourself against these threats by making sure that whatever data you possess or send cannot be read and used by somebody who intercepts it.

Frédéric came to computers quite young, and started his journey to becoming an influential figure in the community by being active in the iPhone jailbreaks space. *"Not for piracy, just because the phone was not usable in my country, and I wanted it."*

Then came the Arab Spring, and these episodes would greatly influence the very knowledgable man walking with me down the hill to the shores of the majestic Léman. He became active in Telecomix, a decentralised structure that he describes as *"Anonymous who grew up."* He followed closely the uprisings in Libya and Syria, and deployed structures on the ground to anti-regime protesters.

> *"My objective is to provide cryptography for those who need it the most."*

He speaks without any arrogance of helping protesters under authoritarian regimes and journalists around the world do their job. As it was normal.

He also travels a lot, to train activists to secure communications. For their security and his, he chose not to tell me much about it. Still, he explained how he starts his training sessions: he tells the audience that it is okay to use their phones and laptops while he is talking, and sniffs the whole network for five minutes. *"It is incredibly easy to do,"* he promises to my amused eyes. Then, he shows his audience everything he collected: *"See, I read all your emails, and oh, I can log in to your Instagram account because you used it - should I delete all your photos?"*

*"Trust me,"* he adds to convince me when it wasn't necessary at all, *"there's one thing you ask: how can I protect myself, now?"*

Open Whisper Systems aims for a somehow different goal: *"When you have a look at all the money Google and Facebook invest in UX (user experience), it's not possible for us to compete. We're doing the best we can, but what we want is to promote our cryptography, or a strong cryptography, as the industry-standard."* It's not a start-up reaching for the stars and dreaming of jousting with the huge players, it is about demonstrating a credible, viable alternative.

It is also responding to this new post-Snowden demand for privacy, and these new concerns arising from the sudden realisation that nothing we do is private. *"I know tons of persons who started working in September last year, a month or so after the Guardian started publishing the leaks. Give them two or three years of hard work and there will be very serious alternatives on the market."*

Although these new talents are today in the spotlights (Edward Snowden recently announced his official endorsement and support to Whisper System), cryptography remains a playground for the elite. *"There are maybe 300 cryptographers who read and understood the implementation of the OTR protocol (for Off The Record)."* So it is sometimes a matter of trust, says the very man who explained in details how little could be trusted nowadays.

As we contemplate the French side of the lake, and the green slopes of Evian, which seems at the same time very close and so far away because of the height of the surrounding mountains, I take a moment to snap a few pictures of the landscape.

Frédéric just explained to me how the [Broadcasting Board of Governors](http://en.wikipedia.org/wiki/Broadcasting_Board_of_Governors), an independent federal agency of the United States government, indirectly supports Whisper Systems through Radio Free Asia, which itself supports the Open Technology Fund.

The Snowden leaks were not a surprise for Frédéric: *"It just brought proof and evidence to what everybody already knew. No, the only real surprise was the depth of these practices, the point they're ready to go to. Look, they're boycotting cryptography themselves, for their internal comms and documents, not to encourage its use and spread... so they can continue to break it!"*

We talk for a while about intelligence and government. His activism and his job oblige him to be cautious when travelling. That means having several laptops, or ignoring the password required to unlock the data he's carrying. Although the system itself can be a bit ridiculous sometimes: *"I once traveled with radioactive material sent to me by the Catholic University of Louvain (in Belgium). They thought my Geiger counter was a decibel-meter... So they let me go."*

He keeps on smiling when we talk about what he is going to do in the future. There does not seem to be much pressure on this front, as he receives many offers. If working in the intelligence isn't a possibility he entertains, he would like to maintain a relationship with them, as it offers a possibility to bring change from within:

> *"I could explain to them why one might want to use Tor, and that not all Tor users are criminals. That you shouldn't have your home raided by the police because you are hosting a Tor exit node."*

*This article is the first of several profiles I intend to write about people like Frédéric. Hopefully, I will have the opportunity to publish some more with the support of the Contribiutoria community.*
