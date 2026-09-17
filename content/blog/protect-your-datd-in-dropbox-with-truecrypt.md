---
aliases: ["/2013/10/21/protect-your-datd-in-dropbox-with-truecrypt/"]
date: "2013-10-21T00:00:00Z"
description: "Let's say I know somebody who needs privacy. Let's say he's far from his country, doing a PhD on something in between political sciences and media…"
tags: []
title: "How to protect your data in Dropbox with TrueCrypt"
draft: true
---
<img src="/assets/Untitled.png" class="aligncenter size-full wp-image-2534" alt="Untitled" />

Let's say I know somebody who needs privacy. Let's say he's far from his country, doing a PhD on something in between political sciences and media studies. Let's say that his research topic seems quite interesting to us Westerners... but could take him to jail in his country. And he wants to use Dropbox.

My friend is right to be worried. Dropbox already showed weakness in the protection of our cloud-stored data. In 2011, for example, [all the passwords were disabled for 4 hours](http://lifehacker.com/5813861/dropbox-accidentally-unlocked-all-accounts-for-4-hours) - meaning that a single email address was enough to log in to your account. Oops. And in September 2013, Mathew J. Schwartz, a security journalist for InformationWeek, raised doubts after he proved that each and every document stored on Dropbox was [opened by an Amazon instance](http://www.informationweek.com/security/client/dropbox-responds-to-security-flap/240161362) with Libre Office, for preview-generating puroposes, Dropbox told him.

Honestly, the list of vulnerabilities of your data in the cloud could go on for a long time. But that is not the point.\
Storing something is taking a risk for somebody to find it. You can be tortured to be forced to reveal an information you stored in your memory. One can break into your flat to steal the passwords you wrote on a post-it. One can break into your computer's hard drive in order to steal your data. And of course, one can break into the cloud which contains your data. The cloud is just another risk, get over it. Just protect your data and enjoy its convenience.

\_\_\_\_\_\_\_\_\_\_

The solution I use and recommend is TrueCrypt, one of the most popular encryption tools available - and it's open source! And the advice I have for you is to abuse of its power. It can be [downloaded for free](http://www.truecrypt.org/downloads) and works on Windows, Mac OS and Linux.\
TrueCrypt is used to create encrypted volumes and containers, meaning that a key is necessary to decrypt and read the documents stored in the container. This protection is AES-256, which is a hash algorithm - way better than a password-protected zip file of pdf.

How secure is it? Well, the NSA considers the AES-256 encryption "sufficient to protect classified information up to the Top Secret level", says [TrueCrypt's website](http://www.truecrypt.org/docs/aes#Y0).

Here's how you proceed:

1.  Download TrueCrypt
2.  Create an encrypted container in your Dropbox folder\
    /home/basile/Dropbox for me for example. NB: this volume"s size needs to be inferior to your Dropbox capacity, e.g. 2Gb out of the box.
3.  No step 3.

And here you are: done!\
A few things to know and remember:

1.  If you lose your password, you will never see your files again.
2.  You will need to mount the encrypted folder in order to access your files. Hence, TrueCrypt must be installed on the computer you are using to access them.
3.  You shall never open the encrypted volume at two different places. Don't leave it mounted on your computer at thome if you want to access it in the library.
4.  Don't forget your password.

Now your files are securely stored in Dropbox's cloud. Nobody will be able to access them without your password.\
Note that this solution does not protect the data stored on your computer.
