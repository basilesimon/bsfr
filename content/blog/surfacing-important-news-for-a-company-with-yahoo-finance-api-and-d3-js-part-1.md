---
aliases: ["/2014/05/08/surfacing-important-news-for-a-company-with-yahoo-finance-api-and-d3-js-part-1/"]
date: "2014-05-08T00:00:00Z"
description: "There are quite a few things I'm working on at the moment, but they all come down to a set of goals or questions I have: - Can I surface information…"
tags: []
title: "Surfacing important news for a company with Yahoo Finance API and d3.js (part"
---
There are quite a few things I'm working on at the moment, but they all come down to a set of *goals* or *questions* I have:

- **Can I surface information better?**
- **Can I give a more accurate and simple picture of a story's background?**

Hence my interest for data stringers and computer-assisted reporting.

Coming down to this blog post, about a simple combination of APIs and d3.js enabling the user (a journalist or a reader) to understand better a situation, in a glance.

**I'm going to go through a simple way to display a chart of a company, and to add some visual indicators of important changes in this company's market value.** All that, step by step.

For doing that efficiently, we need a couple of things:

- The company's value, stored somewhere or queried dynamically (part 1)
- A d3 chart representing this value (part 2)
- A couple of inputs for the user to customize the results (part 3)
- And a way to detect *important* changes. (part 4)

Prerequisites:\
It is my ambition to make technological solutions more accessible, hence these tutorial-ish articles. You don't need much to complete them, but I strongly advise against copy-pasting like an idiot. For obvious reasons, take the time to read the code, to understand it, and, more important, to understand why you are using this and that.\
Basics in HTML and Javascript are required, just to understand the difference between a `variable` and a `function`, for example.\
I voluntarily will not post full gists of the page we are creating, at least until the end of this tutorial. It's up to you to re-write the code and to put things in the right place. Again, use the comment section if you have questions.

------------------------------------------------------------------------

#### Part 1: Getting a company's value history with Yahoo Finance

We are looking at a way to get historical for stock quotes, and we are lucky, because Yahoo! Finance allows us to do that - for free.\
Yahoo! has its own language to communicate with its APIs, the [Yahoo! Query Language](https://developer.yahoo.com/yql/), which is fairly straightforward to understand.

For this example, we want to get data out of Yahoo! stored in a JSON, about, let's say, Apple, between January 1st, 2013, and January 1st, 2014.\
You can head to the [Yahoo! Console to try things out](http://developer.yahoo.com/yql/console), and then continue when you're ready.\
The query we want will look like that:

http://query.yahooapis.com/v1/public/yql?q=select \* from yahoo.finance.historicaldata where symbol in ("AAPL") and startDate = "2013-01-01" and endDate = "2014-01-01"&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json\

Because you read carfully this query, you noted that we used *AAPL*, and not *Apple* for our query. That is because this API requires the symbol of the company. You can use [Yahoo! Symbol Finder](http://finance.yahoo.com/lookup) if you are not sure. As an example, Apple is *AAPL*, Facebook is *FB*, Yahoo is *YHOO*, Microsoft is *MSFT*.\
Paste this URL in your browser, and, *voilà*, you've got a nice JSON file of this form:

\`\`\`javascript { query: { count: 252, created: "2014-05-08T11:17:28Z", lang: "en-US", results: { quote: \[ { Symbol: "AAPL", Date: "2013-12-31", Open: "554.17", High: "561.28", Low: "554.00", Close: "561.02", Volume: "7967300", Adj_Close: "557.68" }, { Symbol: "AAPL", Date: "2013-12-30", Open: "557.46", High: "560.09", Low: "552.32", Close: "554.52", Volume: "9058200", Adj_Close: "551.22" }, (...) \`\`\`

*Remark: This is only a pre-set query. We will want later to be able to customise the results according to user inputs. We will go through that in part 3. Spoiler alert: it is really easy to do.*

Now we want **to query it in the browser directly**. For that, I will beg for your forgiveness, but I will recommend jQuery, because the `$.getJSON()` method is incredibly simple to use.\
Stop checking Reddit every ten seconds, open up your favourite text editor, create a new HTML file, and between two `<script>` tags, use something similar to that:

\`\`\`javascript var myQuery = "http://query.yahooapis.com/v1/public/yql?q=select \* from yahoo.finance.historicaldata where symbol in ("AAPL") and startDate = "2013-01-01" and endDate = "2014-01-01"&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json"; var data = \$.getJSON(myQuery, foo); function foo(data) { console.log(data); } \`\`\`

Now, what the heck did you just write?

- The `myQuery` variable contains the query we wrote previously (and that we are eventually going to customize).
- The `data` variable is the querying itself to Yahoo! services, with the help of `getJSON` jQuery method. It takes two arguments:
  - the query
  - and a function where to send the collected data (a fallback)
- The `foo` thing is our fallback, a function in which we are going to do stuff with the data. In that case, we just log in the console the result of our query.

------------------------------------------------------------------------

That was easy, right? You now have a Javascript Object ready to be used and tweaked. Have fun with different values for this query until part 2 comes up - where we will look for a way to represent graphically the results we just got.
