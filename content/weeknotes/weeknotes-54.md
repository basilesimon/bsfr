---
date: "2021-10-09T00:00:00Z"
published: false
title: 'Speccing = cool - weeknotes #54'
---

I've been working about 50% this week as I'm chaperoning the little one in her introduction to the new daycare centre. Which means that I spent my mornings with a group of about a dozen 2-6 year olds – a relatively different bunch than my regular colleagues, believe me.

I won't bore you with parental softness, but it's a really sweet thing seeing her navigating this new world and having so much to take on, from the new everyday language (🇫🇷) to the many rules of this new, strange place.

---

I've gladly welcomed (tautology?) the opportunity to work on some UI bits through tools nudging towards the isolation and "statelessness" of components.

On the JS, React side I'm leaning on [Storybook](https://storybook.js.org/) once again and... still loving it so far.

It's a bit more involved in ClojureScript, as I didn't find the courage to set up the plumbing for [devcards](https://github.com/bhauman/devcards). Instead, Niko and I scaffolded a one-page view where I can toss my components and rather manually recreate their state.

---

For obscure large-company-German-IT reasons, the question of knowledge bases for a small team has come up. It's something I'd like to get my thoughts in order about, as I've been using a few systems in the last few years, including as a now-floating agent.

TL;DR: where I used to favour dev-integrated tools (reference a PR/issue seamlessly), I've come to favour autosaved, WYSIWYG, great UI-X ones.

---

I've discovered [Clojure Spec](https://clojure.org/guides/spec), part of the standard library, which assists the spec-ing and confirmity checking of data structures.

In a simplified form, it works this way:

Let's define a `post`, which is a map/object containing, at least, `type`, `author`, and `copy` and at most the aforementioned plus `media` and `location`:

```clj
(s/def ::post (s/keys :req-un [::type
                               ::author
                               ::copy]
                      :opt-un [::media
                               ::location]))
```

Is this map valid? Nope...

```clj
(s/valid? ::post
          {:type "text"
           :author "basile"})
=> false
```

Why? `explain-data` points at the missing keyword:

```clj
(s/explain-data ::post {:type "text"
                        :author "basile"})
=> #:spec{:problems
          ({:path [],
            :pred (clojure.core/fn [%] (clojure.core/contains? % :copy)),
            :val {:type "text", :author "basile"},
            :via [:spec-demo.core/post],
            :in []}), :spec :spec-demo.core/post,
          :value {:type "text", :author "basile"}}
```
