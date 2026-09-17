---
aliases: ["/2016/09/10/mailchimp/"]
date: "2016-09-10T00:00:00Z"
description: "A couple of weeks back, I discovered that MailChimp, the newsletter provider, has quite weird default options that make your lists vulnerable to forced…"
tags: []
title: "MailChimp known subscriber attack"
---
A couple of weeks back, I discovered that MailChimp, the newsletter provider, has quite weird default options that make your lists vulnerable to forced, unwanted, and silent subscription cancellations.

---

One of the mailing lists I managed lost a subscriber, you see. Of course, these things happen - but this subscriber was special to us:

*It was one of the editors of the mailing list itself!*

The incident was reported to me, and much cluelessness ensued. This person did *definitely not* unsubscribe. Somebody managed to unsubscribe them... and my colleagues were nervous, as you might imagine.

So I set out to see if I could replicate what happened.

---

By default, our list had a public unsubscribe form available at

```
http://$LIST.usX.list-manage.com/unsubscribe?u=$U&id=$ID
```

From this form, anybody with the knowledge of any email address can unsubscribe this person from the list. No confirmation needed by default.

A spokesperson for MailChimp confirmed this are the default settings for mailing lists.

---

Asked about whether these settings make MailChimp lists vulnerable to unwanted unsubscriptions, they acknowledged that the process of unsubscribing is a complex problem to solve. "MailChimp makes it easy to unsubscribe, by design. A "one-click unsubscribe" ensures there is very little friction around the process of taking yourself off an email list," they said.

"MailChimp has opted for an easy unsubscribe process, as the type of unwanted unsubscribes that you’ve described is narrow and unlikely."

Their recommendation? Turning on the post-unsubscribe email acknowledging the unsubscription both to the list owner and the person who unsubscribed.

---

In the meantime, anybody who gets an email from a MailChimp list can grab the URL at the bottom, keep only the `u=` and `id=` parameters, and screw around with your list.

All you can do is tick this box in your settings:

![](/assets/mailchimp.png)

Not cool.
