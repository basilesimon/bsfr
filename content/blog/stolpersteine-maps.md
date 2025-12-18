---
date: "2020-11-13T00:00:00Z"
updated: "2025-12-18T00:00:00Z"
description: "Comparing Stolpersteine memorial datasets: Wikidata vs stolpersteine-berlin.de. Updated 2025 analysis with 10,000+ Berlin records and interactive maps."
image: "assets/stolpersteine-maps.png"
tags: [observable, viz, berlin, stolpersteine, open-data, holocaust-memorial]
title: "Berlin Stolpersteine Data: Comparing Memorial Databases"
---

> **December 2025 Update:** I've refreshed the data for this analysis. The landscape has changed dramatically—Wikidata's coverage has improved so much that it now *exceeds* the Berlin-specific database. See updated numbers below.

---

Here are two datasets documenting Berlin's Stolpersteine memorial plaques. In 2020, their coverage differed dramatically. Four years later, Wikidata has caught up—and surpassed—the Berlin-specific database.

   🔸 Wikidata reference 🔹 Stolpersteine-berlin dataset
[![maps of Stolpersteine](assets/stolpersteine-maps.png)](https://observablehq.com/@basilesimon/berlin-stolpersteine)
<svg role="img" viewBox="0 0 25 28" width="25" height="28" aria-label="Observable" fill="currentColor" style="width: 22px; transform: translateY(5px);" class="near-black"><path d="M12.5 22.6667C11.3458 22.6667 10.3458 22.4153 9.5 21.9127C8.65721 21.412 7.98339 20.7027 7.55521 19.8654C7.09997 18.9942 6.76672 18.0729 6.56354 17.1239C6.34796 16.0947 6.24294 15.0483 6.25 14C6.25 13.1699 6.30417 12.3764 6.41354 11.6176C6.52188 10.8598 6.72292 10.0894 7.01563 9.30748C7.30833 8.52555 7.68542 7.84763 8.14479 7.27274C8.62304 6.68378 9.24141 6.20438 9.95208 5.87163C10.6979 5.51244 11.5458 5.33333 12.5 5.33333C13.6542 5.33333 14.6542 5.58467 15.5 6.08733C16.3428 6.588 17.0166 7.29733 17.4448 8.13459C17.8969 8.99644 18.2271 9.9103 18.4365 10.8761C18.6448 11.841 18.75 12.883 18.75 14C18.75 14.8301 18.6958 15.6236 18.5865 16.3824C18.4699 17.1702 18.2639 17.9446 17.9719 18.6925C17.6698 19.4744 17.2948 20.1524 16.8427 20.7273C16.3906 21.3021 15.7927 21.7692 15.0479 22.1284C14.3031 22.4876 13.4542 22.6667 12.5 22.6667ZM14.7063 16.2945C15.304 15.6944 15.6365 14.864 15.625 14C15.625 13.1073 15.326 12.3425 14.7292 11.7055C14.1313 11.0685 13.3885 10.75 12.5 10.75C11.6115 10.75 10.8688 11.0685 10.2708 11.7055C9.68532 12.3123 9.36198 13.1405 9.375 14C9.375 14.8927 9.67396 15.6575 10.2708 16.2945C10.8688 16.9315 11.6115 17.25 12.5 17.25C13.3885 17.25 14.124 16.9315 14.7063 16.2945ZM12.5 27C19.4031 27 25 21.1792 25 14C25 6.82075 19.4031 1 12.5 1C5.59687 1 0 6.82075 0 14C0 21.1792 5.59687 27 12.5 27Z" fill="currentColor"></path></svg>
<a href="https://observablehq.com/@basilesimon/berlin-stolpersteine">View on Observable</a>

---

## Background
In the night of Nov 9 to 10, 1938, Nazi Germany's SA forces carried out a devastating pogrom. The event came to be called [_Kristallnacht_, "The Night of Broken Glass."](https://en.wikipedia.org/wiki/Kristallnacht)

Last week, as I walked in the street in the evening I noticed that some of the brass plaques had candles and roses next to them, a silent and unattended vigil in the street. It was in remembrance of Kristallnacht. The picture below is mine:

![A Stolperstein memorial plaque in a Berlin street, with candles placed beside it](assets/stolpersteine.jpg)

These plaques are Stolpersteine—the world's largest decentralized memorial, with over 100,000 brass-topped concrete cubes installed across Europe by artist Gunter Demnig:

> "A Stolperstein (pronounced [ˈʃtɔlpɐˌʃtaɪn]; literally "stumbling stone", metaphorically a "stumbling block") is a sett-size, ten-centimetre (3.9 in) concrete cube bearing a brass plate inscribed with the name and life dates of victims of Nazi extermination or persecution."

> "Today, Stolpersteine are being realized for Jews, Sinti and Roma, people from the political or religious resistance, victims of the "euthanasia" murders, homosexuals, Jehovahs Witnesses and for people who were persecuted for being declared to be "asocial"."

[(Wikipedia)](https://en.wikipedia.org/wiki/Stolperstein)

---

## The Data: 2020 vs 2025

These are two public records of the location and number of Berlin's Stolpersteine:

* the [Wikidata database](https://www.wikidata.org/wiki/Q26703203),
* and the dataset produced by [stolpersteine-berlin.de](https://www.stolpersteine-berlin.de/en), referenced in the [daten.berlin.de](https://daten.berlin.de/datensaetze/liste-der-stolpersteine-berlin) catalogue. It describes itself as "a liaison office between the artist Gunter Demnig together with his team and the local Stolperstein-groups."

| Source | 2020 Records | 2025 Records | Change |
|--------|--------------|--------------|--------|
| [stolpersteine-berlin.de](https://www.stolpersteine-berlin.de/en) | 3,307 | **10,341** | +213% |
| [Wikidata](https://www.wikidata.org/wiki/Q26703203) (Berlin) | ~1,780 | **11,992** | +574% |
| Wikidata (all Europe) | ~14,000 | **47,320** | +238% |

In 2020, there were only about **1,780 Wikidata records** in Berlin, overwhelmingly in the west of the city. Stolpersteine-berlin had **3,307 records**, many including several family members at the same address.

By 2025, the situation has reversed. Wikidata now has **more Berlin records** than the Berlin-specific database, thanks to community contributors adding nearly 35,000 geocoded entries across Europe.

The Wikidata dataset spans not only all of Germany, but all of Europe:
<iframe width="100%" height="584" frameborder="0"
  src="https://observablehq.com/embed/@basilesimon/berlin-stolpersteine?cell=viz"></iframe>

## Technical Notes

The stolpersteine-berlin.de site now provides a [JSON API](https://www.stolpersteine-berlin.de/en/api/json/stolpersteine.json) with pre-geocoded coordinates. The old XML endpoint I used in 2020 no longer exists.

For Wikidata, a SPARQL query retrieves all Stolpersteine with coordinates:

```sparql
SELECT ?item ?itemLabel ?coords WHERE {
  ?item wdt:P31 wd:Q26703203 .
  OPTIONAL { ?item wdt:P625 ?coords }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
```

---

*Originally published November 2020. Updated December 2025 with fresh data.*
