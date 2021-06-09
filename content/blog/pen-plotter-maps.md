---
date: "2018-12-19T00:00:00Z"
description: Drawing Strava data on pen-plotter maps in R
image: https://basilesimon.fr/assets/blog-map-final-group.JPG
tags: [r]
title: Pen plotter maps in R
---

![](assets/blog-map-final-group.JPG)

I made a sweet Christmas present for my friend Clément, who cycles far too much. Last year he got himself a nice custom bicycle made and started [documenting his travels](https://github.com/Cgg/stayer-super-audax-prototype-road-log).

So I grabbed the lot and started playing, and I pen-plotted his journeys on postcards.

_This blog was contributed to [R Bloggers](https://www.r-bloggers.com/)_

---

## Base map

First order of business is getting and representing borders of the countries travelled. Arcane base R beware.

```r
###################
# Get the world map
worldMap <- rworldmap::getMap(resolution = "high")

# Europe
europe <- c('France', 'United Kingdom')
# Select only the index of states member of the E.U.
country_filtered <- which(worldMap$NAME%in%europe)

# Extract longitude and latitude border's coordinates of countries
# Rebuild a dataframe with just the stuff we want
europeCoords <- lapply(country_filtered, function(i){
  df <- data.frame(worldMap@polygons[[i]]@Polygons[[1]]@coords)
  df$region = as.character(worldMap$NAME[i])
  colnames(df) <- list("long", "lat", "region")
  return(df)
})

europeCoords <- do.call("rbind", europeCoords)
```

![](assets/blog-map-1.png)

## Parsing GPX files and tracks

Since Clément has done some good work compiling this dataset, we only need to loop over all GPX files we can find in the directories. We've kept `data@time` to have a look at when the journeys happened.

Oh, and we need to assign a `group` variable to each unique path in order to be able to separate them when visualising. Otherwise, we'll end up with one single uninterrupted line.

```r
########################
# build riders' paths in df
paths <- data.frame()
for (file in list.files("data/", pattern = "gpx", recursive = TRUE)) {
  print(file)
  track_points <- rgdal::readOGR(paste("data/", file, sep = ""),
                           layer = "track_points")
  track_points@data$time_clean <- ymd_hms(track_points@data$time)
  
  df1 <- data.frame(track_points@data)
  df2 <- data.frame(track_points@coords)
  df <- bind_cols(df1, df2)
  
  df.filter <- df %>%
    select(time, coords.x1, coords.x2) %>%
    mutate(group = file)
  colnames(df.filter) <- c('time', 'lon', 'lat', 'group')
  
  paths <- rbind(paths, df.filter)
}

> paths %>% head()
                    time       lon      lat                                  group
1 2017/04/08 01:00:45+00 -1.983406 50.71916 17-04-08-hard-boiled-300/gpx/trace.gpx
2 2017/04/08 01:00:57+00 -1.983241 50.71897 17-04-08-hard-boiled-300/gpx/trace.gpx
3 2017/04/08 01:01:03+00 -1.982949 50.71899 17-04-08-hard-boiled-300/gpx/trace.gpx
4 2017/04/08 01:01:15+00 -1.982324 50.71934 17-04-08-hard-boiled-300/gpx/trace.gpx
5 2017/04/08 01:01:27+00 -1.981452 50.71970 17-04-08-hard-boiled-300/gpx/trace.gpx
6 2017/04/08 01:01:32+00 -1.981107 50.71955 17-04-08-hard-boiled-300/gpx/trace.gpx
```

## Visualising and plotting

Easy as pie: our country boundaries are `polygons`, while the GPS tracks are `paths`, in `ggplot` world.

Once happy with a general layout, exporting an SVG is trivial.

```r
ggplot() +
  geom_polygon(data = europeCoords,
    aes(x = long, y = lat, group = region),
      colour = "#DDDDDD",
      fill = "#FFFFFF") +
  geom_path(data = paths,
    aes(lon, lat, group = group),
      colour="steelblue",
      alpha = 0.5) +
  theme_opts  + 
  coord_map(projection = "mercator")
```

![](assets/blog-map-2.png)

## Pen plotting

In the output SVG file, the country boundaries and the tracks are in separate `<g>` groups, and very easy to isolate. This makes plotting the result one group after the other, with two different pens, very easy. There's a video of the plotting below.

![](assets/blog-map-final.jpg)

<video width="500" autoplay nocontrols loop muted src="https://giant.gfycat.com/ClearcutGrotesqueGoat.webm">
<source src="https://giant.gfycat.com/ClearcutGrotesqueGoat.webm">
</video>
