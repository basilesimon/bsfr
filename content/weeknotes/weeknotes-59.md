---
date: "2021-11-12T00:00:00Z"
published: true
title: 'The Toolkit returns? - weeknotes #59'
---

First week with an M1 laptop. It's kind of insane, and it's the little things. The instant wake and opening of apps. The whole-workday battery life. The total silence. 

---

I followed up on a few leads for the [Digital Evidence Toolkit](https://digitalevidencetoolkit.org/), and it's quite pleasant to see that some of them are still ongoing.

The plans remain the same, though: I'm still fleshing out options for either future work (collaboration on an org-wide instance, for example) or pivots (provide chain-of-custody as a service kind of a thing).

---

It appears that I did a couple of Clojure/ClojureScript things this week. [Bastien](https://bzg.fr) had his big moment as the minister announced ambitious plans for the Digital Commons, and I ended up submitting a couple of CLJS patches to [code.gouv.fr](https://code.gouv.fr/), which aggregates open source code and projects from the French administration. 

There's a chart that's been bugging me in this release, and so I'm looking into either re-doing it in a nice, pure HTML form (which I'm yet to draft) or just bash it with Observable's latest baby: [Plot](https://observablehq.com/@observablehq/plot).

CLJS interops with Javascript, but it's kind of a funny one. See for example the need to move data structures between Clojure and JS with `clj->js` and the relatively gross rendering of Plot's return, which is a built `SVGElement`:

```clj
(defn make-plot [data]
  (plot/plot
   (-> {:marks
        [(plot/barY
          (clj->js data)
          (clj->js {:x "letter" :y "frequency"}))]
        :x {:label ""}
        :caption "test caption"}
       clj->js)))

(defn <header> []
  [:header.mb-5
   [:h3.title.is-3 "Frequency of letters in the English language"]])

(defn render-dom-el
  "Renders a js DOM element as a reagent component, and updates 
   when the DOM element updates, too"
  [dom-el] [:div {:dangerouslySetInnerHTML {:__html (.-outerHTML dom-el)}}])
```

---

And I had a lovely chat with Chris (who [also writes weeknotes](https://blog.chrislowis.co.uk/)), a mix of a friendly catchup and sussing out "collabs."

---

- [“Arcane, hereditary, all-male — and at the heart of British democracy”](https://www.ft.com/content/d5aebb99-0316-41a9-b19a-505713e4fb41) by George Parker from the Financial Times. Comes for the artistocratic tosh, stay for the plot twist explaning why they're still around.
- [“Suppose I Wanted to Kill a Lot of Pilots”](https://newsletter.butwhatfor.com/p/invert-always-invert-avoid-failure) by But What For? on Substack. I've just discovered this way of finding answers through coachings, and found the writing to be a real eye-opener.
