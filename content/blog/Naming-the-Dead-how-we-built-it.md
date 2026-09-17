---
aliases: ["/2014/11/03/Naming-the-Dead-how-we-built-it/"]
date: "2014-11-03T00:00:00Z"
description: "This is a real pleasure to announce that my first work for the Bureau of Investigative Journalism is now live (click on the image). The Naming the Dead…"
tags: []
title: "Naming the Dead - how we built the viz"
---
This is a real pleasure to announce that my first work for the [Bureau of Investigative Journalism](http://www.thebureauinvestigates.com/) is now live *(click on the image).*

<a href="http://www.thebureauinvestigates.com/2014/10/26/naming-the-dead-visualised/"><img src="/assets/ntd.png"></a>

The Naming the Dead project is part of the large investigation originally led by [Alice Ross](https://twitter.com/aliceross_), and now by Abigail Fielding-Smith, and [Jack Serle](https://twitter.com/jackserle). Naming the Dead is a sub-project which aims to identify the victims killed by US drones strikes in the Middle-East.

This interactive has several goals:

- Provide a graphical representation of the mass of people killed,
- Show how little we in fact know, after years of investigation, about the victims of these strikes,
- And to put as many names and stories as possible on these persons.

## What's in the data?

The Bureau has assembled this quite large (and growing) 700-something entries dataset, which includes many personal informations about the reported victims. These informations are published on the interactive when you click on a person:

![sidebar](/assets/sidebar-ntd.png)

The study and monitoring are very thorough, and hopefully such clarity and precision will inspire other journalists to get in touch to collaborate on stories, or offer background on the whole drones campaign. 

## Behind the scenes

The visualisation is built with the excellent and almighty [d3.js](http://d3js.org/) library. It relies on the Naming the Dead dataset, converted to JSON for use with d3. 

It looks something like this:

```javascript
  [
    {
      "Person ID":"ND1",
      "Strike ID":"B1",
      "Date":"17/06/2004",
      "Location (Agency)":"South Waziristan",
      "Name":"Nek Mohammed",
      "Alternate spelling":"",
      "Aliases":"",
      "Gender":"M",
      "Tribe":"",
      "Age":"27-29",
      "Child Y/N":"N",
      "Type of ID":"Name",
      "Count (min)":"1",
      "Count (max)":"1",
      "ID type and number":"",
      "Country of origin":"Pakistan",
      "Place of origin":"",
      "Place of origin in Pakistan":"Unknown",
      "Reported status":"Militant",
      "Civilian occupation":"",
      "Militant affilliation":"Taliban",
      "Rank":"Senior",
      "Militant affiliation details":"Local Commander",
      "Reward Y/N":"N",
    (...)
    }
  ]
```
One tiny SVG icon is appended to the HTML document for every person present in the dataset. With some d3 magic, the person's data is bound to each individual SVG icon - allowing us to query it a bit later, when the user clicks on it for example.

The colours depend on the person's reported status, and you sure have noticed the big lot of grey ones at the bottom: they represent the total of persons allegedly killed by the United States during the drones campaign for who we do not have a name or information - yet. Because we do not have information about them, they are not in the Naming the Dead dataset, but their presence in the graphics is essential! So, I appended them manually, with some information extracted from the largest Drones investigation dataset.

The next interesting bit is the comparison of Presidents G. W. Bush and B. Obama involvement in this campaign: 

![presidents ntd](/assets/presidents-ntd.png)

I will leave you to your conclusions regarding the meaning to give to this graphical representation.

## More about Naming the Dead

The dataset will be expanded with Jack and the Bureau reporters' researches. Make sure you follow the [Naming the Dead website](http://www.thebureauinvestigates.com/namingthedead/?lang=en) and [Twitter account @NamingTheDead](https://twitter.com/NamingTheDead).
