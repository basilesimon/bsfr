---
date: "2020-11-13T00:00:00Z"
description: ""
image: ""
title: Comparing Berlin memorial street plaques datasets
---

Here are two quite different datasets, which supposedly represent the same thing. Hard to miss how different is the extent of their geographical coverage.

   🔸 Wikidata reference 🔹 Stolpersteine-berlin dataset
[![maps of Stolpersteine](assets/stolpersteine-maps.png)](https://observablehq.com/@basilesimon/berlin-stolpersteine)
<svg role="img" viewBox="0 0 25 28" width="25" height="28" aria-label="Observable" fill="currentColor" style="width: 22px; transform: translateY(5px);" class="near-black"><path d="M12.5 22.6667C11.3458 22.6667 10.3458 22.4153 9.5 21.9127C8.65721 21.412 7.98339 20.7027 7.55521 19.8654C7.09997 18.9942 6.76672 18.0729 6.56354 17.1239C6.34796 16.0947 6.24294 15.0483 6.25 14C6.25 13.1699 6.30417 12.3764 6.41354 11.6176C6.52188 10.8598 6.72292 10.0894 7.01563 9.30748C7.30833 8.52555 7.68542 7.84763 8.14479 7.27274C8.62304 6.68378 9.24141 6.20438 9.95208 5.87163C10.6979 5.51244 11.5458 5.33333 12.5 5.33333C13.6542 5.33333 14.6542 5.58467 15.5 6.08733C16.3428 6.588 17.0166 7.29733 17.4448 8.13459C17.8969 8.99644 18.2271 9.9103 18.4365 10.8761C18.6448 11.841 18.75 12.883 18.75 14C18.75 14.8301 18.6958 15.6236 18.5865 16.3824C18.4699 17.1702 18.2639 17.9446 17.9719 18.6925C17.6698 19.4744 17.2948 20.1524 16.8427 20.7273C16.3906 21.3021 15.7927 21.7692 15.0479 22.1284C14.3031 22.4876 13.4542 22.6667 12.5 22.6667ZM14.7063 16.2945C15.304 15.6944 15.6365 14.864 15.625 14C15.625 13.1073 15.326 12.3425 14.7292 11.7055C14.1313 11.0685 13.3885 10.75 12.5 10.75C11.6115 10.75 10.8688 11.0685 10.2708 11.7055C9.68532 12.3123 9.36198 13.1405 9.375 14C9.375 14.8927 9.67396 15.6575 10.2708 16.2945C10.8688 16.9315 11.6115 17.25 12.5 17.25C13.3885 17.25 14.124 16.9315 14.7063 16.2945ZM12.5 27C19.4031 27 25 21.1792 25 14C25 6.82075 19.4031 1 12.5 1C5.59687 1 0 6.82075 0 14C0 21.1792 5.59687 27 12.5 27Z" fill="currentColor"></path></svg>
<a href="https://observablehq.com/@basilesimon/berlin-stolpersteine">View on Observable</a>

---

## Background
In the night of Nov 9 to 10, 1938, Nazi Germany's SA forces carried out a devastating pogrom. The event came to be called [_Kristallnacht_, "The Night of Broken Glass."](https://en.wikipedia.org/wiki/Kristallnacht)

Last week, as I walked in the street in the evening I noticed that some of the brass plques had candles and roses next to them, a silent and unattended vigil in the street. It was in remeberance of Kristallnacht. The picture below is mine:

![picture of a Stolperstein in the street](assets/stolpersteine.jpg)

These plaques are Stolpersteine:

> "A Stolperstein (pronounced [ˈʃtɔlpɐˌʃtaɪn]; literally "stumbling stone", metaphorically a "stumbling block") is a sett-size, ten-centimetre (3.9 in) concrete cube bearing a brass plate inscribed with the name and life dates of victims of Nazi extermination or persecution." 

> "Today, Stolpersteine are being realized for Jews, Sinti and Roma, people from the political or religious resistance, victims of the "euthanasia" murders, homosexuals, Jehovahs Witnesses and for people who were persecuted for being declared to be "asocial"."   

> "(It is a) project created by Gunter Demnig for honoring victims of National Socialism"
[(Wikipedia)](https://en.wikipedia.org/wiki/Stolperstein)

---

## So why is the data so different?
These are two public records of the location and number of Berlin's Stolpersteine:

* the [Wikidata database](https://www.wikidata.org/wiki/Q314003),
* and another database referenced in the [daten.berlin.de](daten.berlin.de) catalogue, is the dataset produced by [stolpersteine-berlin.de](https://stolpersteine-berlin.de) – which describes itself as "(a) liaison office between the artist Gunter Demnig together with his team and the local Stolperstein-groups."

There are only about **1,780 Wikidata records** in Berlin, and they're overwhelmingly in the west of the city. Stolpersteine-berlin, on the other hand, has **3,307 records**, many of them including several family members.

The Wikidata dataset has however the merit of spanning not only all of Germany, but also all of Europe:
<iframe width="100%" height="584" frameborder="0"
  src="https://observablehq.com/embed/@basilesimon/berlin-stolpersteine?cell=viz"></iframe>

Could the second dataset, good enough to be referenced by the Berlin open data initiative, be added to the Wikidata records, I wonder?
