---
aliases: ["/2014/10/10/monitor-mps-deleted-tweets/"]
date: "2014-10-10T00:00:00Z"
description: "Thanks to Github, who recently released its Education Pack for students, including among other offers a $100 coupon for Digital Ocean VPS services, I got…"
tags: []
title: "Monitor UK MPs deleted tweets"
---
Thanks to Github, who recently released its [Education Pack](https://education.github.com/pack/) for students, including among other offers a $100 coupon for [Digital Ocean VPS services](https://www.digitalocean.com/), I got to mess around with servers today. 

That is, thanks also to the assistance of [Karl](https://twitter.com/karlsutt), who works with me at the BBC News Labs, and who kindly explained to me a bunch - the very basics: how to set the server up, the [essential security measures](http://plusbryan.com/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers), and how to `nginx`.

***

So, today, I took on an idea I had in mind since colleagues at French newspaper Le Monde published a very nice little [list of tweets freshly deleted from Manuel Valls' account](http://www.lemonde.fr/pixels/article/2014/08/27/les-tweets-que-manuel-valls-aimerait-voir-disparaitre_4477776_4408996.html) after the latest cabinet reshuffle - *[English version here](https://translate.google.fr/translate?hl=fr&sl=fr&tl=en&u=http%3A%2F%2Fwww.lemonde.fr%2Fpixels%2Farticle%2F2014%2F08%2F27%2Fles-tweets-que-manuel-valls-aimerait-voir-disparaitre_4477776_4408996.html).*

I found most of what I needed on Github, and [forked the project to make it fit my needs better.](https://github.com/basilesimon/DeleteThatTweet)

### Store it, baby
The approach is the following: the program runs 24/7, and fetches each and every tweet posted by the accounts you follow. It stores them in a database for reference, and takes a screenshot of all of them. Every once in a while, it checks again if the tweets are still available or... if they've been deleted. If that is the case, the screenshot is moved to a different folder and the tweet is stored in another database. 

Pretty neat, eh?

The only downside of it is that, depending on how many accounts you are following, it can end up consuming quite a lot of storage space. My fork aims to fix that by reducing drastically the size of the saved images, but still, it will prove being quite heavy in the long run. 

### Get started!
The program is relatively straightforward to execute. You will need a Twitter account and to [create an app](https://apps.twitter.com/) in order to obtain the credentials required. You will also need either a server to run the whole shebang, or to run it on your machine directly, if you do not power it off too often. 

Besides that, just follow the Readme. 
Oh, and I almost forgot: thanks to [Iain](https://twitter.com/iaincollins) for providing a [big nice CSV listing all UK MPs and their Twitter accounts](https://gist.github.com/iaincollins/8c8e78e8a930c7ea4dce)!
