---
aliases: ["/2015/01/14/scrape-CENTCOM-data-with-python-and-beautifulsoup/"]
date: "2015-01-14T00:00:00Z"
description: "Yesterday, I attended a new meetup, led by Elliot Bentley, Graphics Editor at Wall Street Journal, called Journocoders. The theme was \"Scraping with…"
tags: []
title: "Scrape CENTCOM's data with Python and BeautifulSoup"
---
Yesterday, I attended a new meetup, led by [Elliot Bentley](https://twitter.com/elliot_bentley/), Graphics Editor at Wall Street Journal, called [Journocoders](https://twitter.com/journocoders/). 

The theme was "Scraping with Python." And so we did - or at least tried to do. For some obscure Python versions reasons, I had lots of trouble going through Greg Reda's famous tutorial: [Web Scraping 101 with Python](http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/). So I figured I'd have another go today. 

## Getting data from CENTCOM
For those who do not read this blog or are not interested in the war against the group calling itself Islamic State, CENTCOM (which stands for Central Command) is the branch of the US military managing the Middle East. They have been, since August 8 and the beginning of the airstrikes, the authority publishing the most comprehensive (daily or so) reports of the strikes. 

For our project Airwars, [Chris Woods](https://twitter.com/chrisjwoods) and I rely on this data heavily. 

But here's the catch: **Chris is tired of copy-pasting the press releases into our datasets daily.** So let's automate this bit, shall we?

Before you read further, have a look at the tutorial above. It will introduce you to the basics of Python and BeautifulSoup, the scraping library we'll use. As for before, I'll go through the example bit by bit - don't proceed further if you don't understand. There will be a Github Gist at the end. 

**This tutorial will be in two parts:**

* The first one will grab all the URLs containing relevant press releases,
* The second will fetch the PRs themselves and wrap it all up.

### Importing all the things

```python
from bs4 import BeautifulSoup
from urllib2 import urlopen
import json 

base_url = "http://www.centcom.mil"
links_collection = []
```

So, here, we're importing a bunch of things at the top of our document. 

We've got to start with `beautifulsoup`, our scraping library. You might want to install it first with `pip install beautifulsoup4`, or have a look at Greg's tutorial. Then we proceed with `urlopen`, so we can actually use URLs in our code. And finally, `json`, because we will export to this format. 

We define the base URL we will work from. You might have noticed that we did not declare [centcom.mil/news](http://www.centcom.mil/news) for this - more later. 

And finally, hello `links_collection`, the list we will store our results in.

### Souping the page

```python
def make_soup(url):
  html = urlopen(url).read()
  return BeautifulSoup(html, "lxml")

def get_links(section_url):
  soup = make_soup(section_url)
```

Nothing extremely fancy is happening here: we're just making a "soup", i.e. a scraper, from the URL we want. 

Note that we are still referring to `section_url` for the moment, we will pass the correct argument in the end. 

### The good bit

```python
  # Define where the data is in the page 
  table = soup.find("table", "blog")
  tds = table.findAll("td", "contentheading")

  # Grab all the links
  for td in tds:
    links_collection.append(base_url + td.a["href"])

  # Output the whole think in JSON file
  with open("links_collections.json", 'w') as outfile:
    json.dump(links_collection, outfile)

```

As explained by the comments in the code, this is where you have to get your hands dirty and fire up your web-developer tools in your browser. This step is well documented in Greg's tutorial - with screenshots -, so I won't come back to that. 

The `/news` index of CENTCOM is basically a table of links sending you to the full press releases. Before scraping the press releases themselves, we need to know where they live, and thus, to know their URL. As the page only contains 6 links, we will have to scrape this page quite a few times...

Anyway, the `table` containing the links has a class: `blog`, and is filled with `td`, which all have a `contentheading` class. In each of these, we will find the links in `a` elements. 

Note that we `append` to our list, `links_collection`, and that we add `base_url` before the link, as they are relative. This will be easier to go through later. The links we're getting here already include the `/news` prefix, and that's what we left it out when we defined `base_url` at the top. 

Moving on to the last paragraph, in which, quite simply, outputs the data into a JSON file. Kid's stuff. 

### Solving the pagination issue
I told you earlier: we only have six articles per page, and we want to go back all the way to the beginning of August! Two solutions here: **we could grab the link to the next page each time we scrape one, or we're lucky and we can find a pattern in the URLs.** 

In this case, there is a pattern: `centcom.mil/en/news` is the first page, then jumps to `centcom.mil/en/news/P11`, then `P22`... all the way to `P365`, which is a multiple of 11. 

So be it:

```python
if __name__ == '__main__':

  # Scrape home-page
  url_to_scrape = ("http://www.centcom.mil/en/news")
  pages = get_links(url_to_scrape)
  
  # Scrape following pages
  for i in range(0, 165, 11):
    url_to_scrape = ("http://www.centcom.mil/en/news/P" + str(i))
    pages = get_links(url_to_scrape)
```

The first line is just Python boilerplate. 

Then we divided the program into two parts: the home page first, and then all the following pages. 

So, we pass the home page URL to the `get_links` function, and voila. First page A-OK.

And then, we use a `for` loop with increments of 11 to go to page 165, where the first report of the war lives. The syntax being `for i in range(start, end, increment)`.

Execute the whole script... And voilà!

```javascript
[
    "http://www.centcom.mil/en/news/articles/jan.-9-military-airstrikes-continue-against-isil-in-syria-and-iraq",
    "http://www.centcom.mil/en/news/articles/jan.-8-military-airstrikes-continue-against-isil-in-syria-and-iraq",
    "http://www.centcom.mil/en/news/articles/u.s.-military-begins-training-iraqi-forces-to-take-on-isil"
    (...)
]
```
Easy, right? That's pretty much it, in the end. **Next time, we're going to use all these URLs we've got in this JSON file to grab the press releases.**

Oh, and by the way, [the Github Gist with the code is here!](https://gist.github.com/basilesimon/7e970e4b4e1dafeadb8d)
