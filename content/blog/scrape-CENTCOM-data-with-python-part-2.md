---
aliases: ["/2015/01/22/scrape-CENTCOM-data-with-python-part-2/"]
date: "2015-01-22T00:00:00Z"
description: "All right, now for part two of our quick tutorial on scraping CENCTOM. Important note: I asked my pal Balto for advices in his field of expertise: Python.…"
tags: []
title: "Scrape CENTCOM's data - part 2"
---
All right, now for part two of our quick tutorial on scraping CENCTOM. 

**Important note:** I asked my pal [Balto](https://www.twitter.com/brouberol) for advices in his field of expertise: Python. Long story short, he corrected a bunch of things in my script, from variables not capitalised to indentation, and also more important things.

Anyway, moving on.

### Preparing the variables
```python
BASE_NEWS_URL = "http://www.centcom.mil/en/news"
NEWS_PAGE_URL = BASE_NEWS_URL + "/P"
```

As we did before with `BASE_URL`, we're going to define the basic URLs that we'll use later.

### Getting the content
We don't need to change anything in our `get_links()` function, which grabs all the links from the index page. 

However, we'll need a new function to scrape the press releases. 

```python
def get_content(link):
    print('Scraping press release from %s...' % (link))
    soup = make_soup(link)
    table = soup.findAll("table", "contentpaneopen")[1]
    paras = table.findAll("p")
    for text in paras:
        press_releases.append(text)
```

So, we call another `soup()` on our links, and then, as we did before for `get_link()`, we throw in some parameters in, i.e. the DOM elements containing the body of the press releases.

### Calling all our stuff
Balto made some adjustments to the boilerplate used to call the functions, so let's just re-use it as is: 

```python
if __name__ == '__main__':
    links, releases = [], []
    urls = [BASE_NEWS_URL] + [NEWS_PAGE_URL + str(i) for i in range(0, 165, 11)]
```

Then I propose we simplify: instead of storing the URLs in a JSON file, let's just use the variable containing these URLs to scrape the press releases directly. Like this:

```python
    # Scrape following pages
    for url in urls:
        links.extend(get_links(url))

    # Scrape press releases
    for link in links:
        releases.append(get_content(link))

    with open('press-releases.json', 'w') as f:
        json.dump(releases, f, indent=4)
    print "Output result in press-releases.json"
```

Voila. Everything will be inputed in a (messy) JSON: 

```javascript
"[<p>January 9, 2015<br/>Release # 2015009<br/>FOR IMMEDIATE RELEASE</p>, <p><strong>SOUTHWEST ASIA -</strong> U.S. and partner nation military forces continued to attack ISIL terrorists in Syria, Jan. 8, using fighter and bomber aircraft(...)
```

Now, you noted that there are some HTML tags in there. That's quite good, because we can directly generate an HTML output by replacing `.json` by `.html`. then, some styling. Because it's 2015, people. 

**And, as promised, [the Github Gist](https://gist.github.com/basilesimon/9eb2f7e7449268a39ca0).**
