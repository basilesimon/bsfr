---
date: "2019-01-02T00:00:00Z"
description: Scraping Strava to map 10,000km of cycling with Python, R and ggplot
image: https://blog.basilesimon.fr/assets/strava-map-final.jpeg
tags: [r, viz]
title: Strava rides map in R
---

![](assets/strava-map-final.jpeg)

This is a Christmas present to myself to celebrate 10,000km of commuting on my bicycle: a lovely frame print of all my GPS traces on a home-made map of London. Here's how I made it.

_This blog was contributed to [R Bloggers](https://www.r-bloggers.com/)_

---

## Step one: getting Strava data

The process has become slightly convoluted in May 2018. In the past, it was possible to download a Strava archive which contained all activities as GPX; however, GDPR regulations [led to a change in bulk export format](https://support.strava.com/hc/en-us/community/posts/360014914631-Activities-in-the-new-bulk-export-feature-have-meaningless-names-and-multiple-formats-).

Anyway: [request your Strava archive](https://www.strava.com/athlete/delete_your_account), wait for the email, download it.

`activities.csv` gives us a list of activities... which we can then scrape from Strava.

```
$ cat activities/activities.csv | head -5
id,date,name,type,description,elapsed_time,distance,commute,gear,filename
1988225457,2018-11-27 19:11:32,Evening Ride,Ride,"",1468,6075.0,true,1x1x8,activities/2125648250.fit.gz
1992478096,2018-11-29 10:02:58,Morning Ride,Ride,"",1449,5869.0,true,1x1x8,activities/2130096306.fit.gz
1992478209,2018-11-29 23:04:16,Night Ride,Ride,"",1166,5930.0,true,1x1x8,activities/2130096453.fit.gz
1992479540,2018-11-30 08:51:29,Morning Ride,Ride,"",1427,6563.0,true,Michel le fixie,activities/2130097780.fit.gz
```

Clone [hugovk/strava-tools](https://github.com/hugovk/strava-tools), a set of Python tools to do automate interactions with Strava. There are some instructions at the top of `download_fit_as_gpx.py`.

Follow these before running `$ python download_fit_as_gpx.py`

Some time later... here we are!

```
$ ls activities/activities | head -5
20160908-170525-Ride.gpx
20160909-080222-Ride.gpx
20160909-180740-Ride.gpx
20160912-081014-Ride.gpx
20160912-172611-Ride.gpx
```

---

## Step two: Ingesting activities in R

Install [ marcusvolz/strava](https://github.com/marcusvolz/strava), an excellent suite of R functions that help us load activities in a (big, big) dataframe.

```r
library(devtools)
devtools::install_github("marcusvolz/strava")
library(strava)
library(tidyverse)

# main ingestion method
# ACHTUNG: slow!
data  <-  process_data("./activities/activities/")
data %>% head()

  id      lat      lon   ele                time dist_to_prev    cumdist time_diff_to_prev  cumtime
1  1 45.78514 4.717282 295.7 2015-12-26 11:21:48  0.000000000 0.00000000                 0        0
2  1 45.78512 4.717559 295.3 2015-12-26 11:22:12  0.021643479 0.02164348                24       24
3  1 45.78512 4.717573 295.2 2015-12-26 11:22:13  0.001111138 0.02275462                 1       25
4  1 45.78512 4.717583 295.2 2015-12-26 11:22:17  0.000785528 0.02354015                 4       29
5  1 45.78509 4.717684 295.1 2015-12-26 11:22:38  0.008715879 0.03225602                21       50
6  1 45.78508 4.717694 295.1 2015-12-26 11:22:39  0.001181249 0.03343727                 1        5
```

---

## Step three: Visualising our activities

We can piece together a simple plot (besides throwing a caveman-like `plot(data)`) limited to London:

```r
library(ggplot2)
theme_opts<-list(theme(panel.grid.minor = element_blank(),
  panel.background = element_blank(),
  plot.background = element_blank(),
  axis.line = element_blank(),
  axis.text.x = element_blank(),
  axis.text.y = element_blank(),
  axis.ticks = element_blank(),
  axis.title.x = element_blank(),
  axis.title.y = element_blank(),
  plot.title = element_blank(),
  panel.grid.major = element_line(colour = 'transparent'),
  legend.position = "none"))

ggplot(data,
  aes(lon, lat, group = id)) +
  geom_path(colour="steelblue",alpha = 0.2) + 
  coord_map(projection = "mercator", 
    xlim = c(-0.41, 0.08), 
    ylim = c(51.42, 51.73), clip = "on") +
  theme_opts
```

![](assets/strava-map-1.png)

Obviously we are going to need some geographical landmarks to get our bearings. [geotheory/londonShapefiles](https://github.com/geotheory/londonShapefiles/) is one of the simplest and quickest ways to get London boundaries loaded in - and that includes the river Thames.


```r
library(devtools)
install_github("geotheory/londonShapefiles")
library("londonShapefiles")
thames <- load_thames()
thames.proj <- spTransform(thames, CRS("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"))
thames.df <- fortify(thames.proj)

ggplot() +
  geom_polygon(thames.df,
   mapping=aes(long, lat, group = group,
    fill = I("skyblue")), alpha = 0.4) +
  geom_path(data,
    mapping=aes(lon, lat, group = id,
    alpha = 0.9, color = I("tomato")),
    size=1/3) +
  coord_map(projection = "mercator",
    xlim = c(-0.41, 0.08),
    ylim = c(51.42, 51.73)) +
  theme_opts
```

![](assets/strava-map-2.png)

But behold, we can also get data straight from Open Street Map thanks to [osmdata](https://cran.r-project.org/web/packages/osmdata/vignettes/osmdata.html). The syntax is relatively concise and OSM's web interface allows you to query features directly from there:

![](https://i.gyazo.com/4f3440eea455f9f94ce42e46444cb838.gif)

In our example, we grab all the parks in London and them use `geom_sf()` to represent both the `polygons` and `multipolygons` (the `osmdata`object [has plenty inside it](https://cran.r-project.org/web/packages/osmdata/vignettes/osmdata.html#3_the_osmdata_object)). We need both polygons and multipolygons because, according to the OSM wiki:

> Any area that is more complex than that (e.g., because its outline consists of several ways joined together, or because the area consists of multiple disjunct parts, or has holes) requires a _multipolygon_ relation. 

```r
library(osmdata)
parks2 <- opq(bbox = c(-0.41, 51.42,
  0.08, 51.73)) %>%
  add_osm_feature(key = 'leisure',
    value = "park") %>%
  osmdata_sf()

ggplot() +
  geom_polygon(thames.df,
   mapping=aes(long, lat, group = group,
    fill = I("skyblue")), alpha = 0.4) +
  geom_sf(parks2$osm_polygons,
   mapping=aes(fill = I("springgreen4"),
    color = I("transparent")),
    alpha = 0.4) +
  geom_sf(parks2$osm_multipolygons,
   mapping=aes(fill = I("springgreen4"),
   color = I("transparent")), alpha = 0.4) +
  geom_path(data,
  mapping=aes(lon, lat, group = id,
   alpha = 0.9, color = I("tomato")),
   size=1/3) +
  coord_sf(xlim = c(-0.41, 0.08),
           ylim = c(51.42, 51.73)) +
  theme_opts
```

![](assets/strava-map-3.png)

---

Well, we're almost there. For this first draft I stopped at the map above, exported an SVG and sent that to the lab for printing.

There is no limit to how much you can play with this data. One thing that really struck me was how imprecise my GPS tracking devices were in the City of London (despite being prosumer equipment). Below is a representation of one year of data, on which I've overlaid the OSM paths corresponding to the streets around Bishopsgate, Cheapside, Monument, Cannon Street, Aldgate, Smithfields, London Bridge and Blackfriars.

```r
streets <- opq(bbox = c(-0.21, 51.47,
  0.05, 51.61)) %>%
  add_osm_feature(key = 'highway',
  value = "primary") %>%
  osmdata_sf()
streets2 <- opq(bbox = c(-0.21, 51.47,
  0.05, 51.61)) %>%
  add_osm_feature(key = 'highway',
  value = "secondary") %>%
  osmdata_sf()
streets3 <- opq(bbox = c(-0.21, 51.47,
  0.05, 51.61)) %>%
  add_osm_feature(key = 'highway',
  value = "tertiary") %>%
  osmdata_sf()

+ geom_sf(streets$osm_lines,
   mapping=aes(fill = I("transparent"),
   color = I("darkgray")), size = 0.5) +
geom_sf(streets2$osm_lines,
   mapping=aes(fill = I("transparent"),
   color = I("darkgray")), size = 0.3) +
geom_sf(streets3$osm_lines,
   mapping=aes(fill = I("transparent"),
   color = I("darkgray")), size = 0.1) 
```

![](assets/strava-map-4.png)
