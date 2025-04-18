---
date: "2019-08-18T00:00:00Z"
description: New R package to load, parse and chart 20 years of oceanic storms data
image: https://basilesimon.fr/assets/storms_facet.png
tags: [r]
title: noaastorms R package now supports NOAA IBTrACS v4
---

![](assets/storms_facet.png)

Earlier this year, I released a simple R package (available at [basilesimon/noaastorms](https://github.com/basilesimon/noaastorms)) that downloads, cleans and parses NOAA IBtrack data for you.

As the NOAA updated its datasets, `noaastorms` is now using these!

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

#### Official changelog (retrieved Aug 16, 2019)
[https://www.ncdc.noaa.gov/ibtracs/index.php?name=status][https://www.ncdc.noaa.gov/ibtracs/index.php?name=status]

This is the first release of IBTrACS version 04. It is updated weekly.  
Release date: March 2019

New features (improvements from v03): 
* Best track data updated daily and contain provisional tracks of recent storms.
* Reduced formats - Version 4 is available in 3 formats (netCDF, CSV, shapefiles)
* Consistent formats - The data presented in each format is completely interconsistent (identical).
* More parameters - More parameters provided by the agencies are provided in IBTrACS
* Basin assignment - Any system occuring in a basin is included in that basin file (in version 3, the storm was only included in the basin in which it had its genesis)
* New derived parameters - We provide storm translation speed and direction and other variables requested by users.
