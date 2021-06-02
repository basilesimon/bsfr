---
date: "2019-01-30T00:00:00Z"
description: New R package to load, parse and chart 20 years of oceanic storms data
image: https://blog.basilesimon.fr/assets/storms_final.png
tags: [r]
title: 'New R package: load and chart oceanic storms'
---

![](assets/storms_final.png)

Mapping historical storms data is now a little bit easier. [Off the back of this blog](https://blog.basilesimon.fr/2018/09/05/storms-map-in-R/), I have authored an R package (available at [basilesimon/noaastorms](https://github.com/basilesimon/noaastorms)) that downloads, cleans and parses NOAA IBtrack data for you.

The National Oceanic and Atmospheric Administration releases datasets known as [International Best Track Archive for Climate Stewardship](<https://www.ncdc.noaa.gov/ibtracs/>).

These datasets are updated regulary and cover all our oceans. The data found in there is fantasticly detailed and goes back as far as 1850 in some case (I wonder how!).

## How to install

```r
library(devtools)
install_github("basilesimon/noaastorms")
```

## Available functions

`getStorms`: Fetch NOAA historical best track storms data

```r
> df <- getStorms(c('EP'))

> head(df[1:5])
     Serial_Num Season Num Basin Sub_basin    Name
2 1902276N14266   1902  01    EP        MM UNNAMED
3 1902276N14266   1902  01    EP        MM UNNAMED
4 1902276N14266   1902  01    EP        MM UNNAMED
5 1902276N14266   1902  01    EP        MM UNNAMED
6 1902276N14266   1902  01    EP        MM UNNAMED
```

The first argument is a vector of basin codes from this list:

* NA: North Atlantic
* SA: South Atlantic
* NI: North Indian
* SI: South Indian
* EP: East Pacific
* SP: South Pacific
* WP: West Pacific

![NOAA basins map](https://www.ssd.noaa.gov/PS/TROP/TCFP/images/TCFP_basins.gif)

To get storms that took place in the Atlantic for example, run `getStorms(c('NA', 'SA'))`.

The second (optional) argument is a date range to filter data with. For example:

```r
dateRange <- c(as.Date('2010-01-01'), as.Date('2012-12-31'))
getStorms(c('NA', 'SA'), dateRange = dateRange)
```

Will query storms that took place in the Atlantic in 2010 and 2012.


## Usage

```r
# load a map of the world and
# use `clipPolys` to avoid issues
# when zooming in with `coord_map`
wm <- map_data("world")
library("PBSmapping")
data.table::setnames(wm, c("X","Y","PID","POS","region","subregion"))
worldmap <- clipPolys(wm,
  xlim=c(20,110),ylim=c(0, 45),
  keepExtra=TRUE)

# load storms for the Atlantic ocean
spStorms <- getStorms(c('NA', 'SA'))

ggplot(spStorms,
  aes(x = Longitude, y = Latitude,
    group = Serial_Num)) + 
  geom_polygon(data = worldmap,
    aes(x = X, y = Y, group = PID), 
    fill = "whitesmoke",
    colour = "gray10",
    size = 0.2) +
  geom_path(alpha = 0.1, size = 0.8,
    color = "red") +
  coord_map(xlim = c(20,110),
    ylim = c(0, 45)) 
```

![Screenshot of storms](https://github.com/basilesimon/noaastorms/raw/master/Rplot.png)

## Your feedback is important

Next on the list are more complex queries. Sadly, supporting date ranges doesn't change how much data we need to download (the NOAA data is bulk export).

I maintain a [list of open issues on Github](https://github.com/basilesimon/noaastorms) and hope to capture some feature requests there.

If you have ideas, bug reports, feature requests, this is the place to go. Thank you!
