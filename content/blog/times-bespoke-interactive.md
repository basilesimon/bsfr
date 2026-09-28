---
aliases: ["/2017/01/12/times-bespoke-interactive/"]
date: "2017-01-12T00:00:00Z"
description: "I was apparently bullied into opening an account on Medium (for the second time). This content is mine, not theirs, so I reproduced it below. For the…"
tags: []
title: "Patiently waiting or hastily prototyping: how we built our latest bespoke interactive in React and D3"
---
*I was apparently bullied into opening an account on Medium (for the second time). This content is mine, not theirs, so I reproduced it below. [For the second time.](/blog/learning-react-in-2-weeks/)*

---

![](https://cdn-images-1.medium.com/max/1600/1*-2nVNDXlFP-B-PYmFanXqA.png)

Saturday 7th January’s edition of The Times revealed that [ten out of 11 NHS trusts had been accused of routinely manipulating 999 response times](http://www.thetimes.co.uk/past-six-days/2017-01-07/news/ambulance-trusts-use-loophole-to-claim-faster-response-times-9mt7hgbp5) by using a loophole to claim that they reached life-threatening emergencies in less than ten seconds.

In addition to this, results from a Freedom of Information request [showed that only one of the 13 trusts](http://www.thetimes.co.uk/article/patiently-waiting-ambulance-response-times-in-your-area-gdrw9vwzc) met the target of eight minutes to respond to life or death calls.

For us in the dev team, this project was the occasion to try out a few things.

---

# A dev-led project

In November, I allocated time to start building a prototype of what I thought we could do with the sort of dataset Louis was working on. I wanted the basic functionalities sorted before handing it over to Design.

![](https://cdn-images-1.medium.com/max/1600/1*fPvIPnSSdV-pLk-L43xbVQ.png)

Framing the project right from the start, from a data and developer perspective, eventually made our life easier. The first iteration, seen above, led the project through its life.

It is a fine line, however, as we didn’t want to allow this to restrict the story. The goal of my first prototype was to make the rest of the dev work much more efficient.

And it sort of did. I will spare you the details of the constant back and forth between us, the news desk, and design, and just tell you that while the colours were being decided, the designs were being designed, and the feed back being fed back, I was doing the plumbing and behind-the-scenes work. Parallelising feels great for everyone, since nobody is really waiting any more.

Having a working prototype early put me in a position where I could also have a pretty good idea of what I wanted on the data side. I worked closely with the data team on tweaking and massaging the data structure to be handy and avoid client-side computations.

But crucially, I wanted technical feasibility to drive the project, in collaboration with the data and design teams. Bonus points if this could be done in a short amount of time.

---

# React and D3 together

Upon starting this project, I focused solely on the bar chart. All the code lived in a `prototype` branch, which was dirty simple HTML and JS files. Once satisfied, I would immediately reimplement everything in React.

Making it work, by increments.

Architecturally speaking, a [container](https://medium.com/@learnreact/container-components-c0e67432e005#.glulmmq89) was in charge of fetching the data and handling a basic `d3.csv()` operation, passing a nested data structure down to the chart component:

```javascript
fetchData() {    
  const _this = this;    
  d3.csv("data/data_new2.csv", function(error, data) {       
    // takes our data and groups it by postcode      
    // we end up with one row per year      
    const data_nest = d3.nest()        
      .key(function(d) { return d.postcode})        
      .entries(data);       
    _this.setState ({        
       dataset: data_nest      
    })    
  });  
}
```

The chart component would render an SVG chart, and on `componentDidMount()` / `componentDidUpdate()` call a standard `draw()` function, in which we wrote our standard D3 code.

```javascript
// Component lifecycle handling  
componentDidMount() {    
  const dataset = this.props.dataset();  
}   
componentDidUpdate() {    
  const postcode = this.props.postcode;    
  const _this = this;    
  for (let i=0; i<this.props.data.length; i++) {      
    if(this.props.data[i].key === postcode) {        
      _this.draw(this.props.data[i].values, "year", "median");      
    }    
  }
```

Yes, I know. `const _this = this;` is particularly inelegant. Both React and D3 make quite a big use of `this`, and an under-rated underscore allows us to jump the scope and hopefully get away with it if there’s no code review.

---

# Results: a staggering engagement rate

![](https://cdn-images-1.medium.com/max/1600/1*_pVI8zwE-fLXqKF-XtsDpw.png)

This React app was embedded as an in-article component into the articles on both desktop and tablet. Out of 16,000 views, we had more than 14,000 postcode searches. Which amounts to an 87% engagement rate!

The two suggested postcodes (SE1 and N16) were respectively first and fifth most searched overall. Stratford-upon-Avon (CV37) was curiously the second most searched.

More to the point, 87% engagement is massive, and it means that our time was well invested in this project.

A similar “explore our data” React app we put up earlier in December had a single-digit engagement rate:

![](https://cdn-images-1.medium.com/max/1600/1*9ty6hlR9fHdGZ8Qbc3CVXw.png)

It seems like the wording could have played an important role. From very open choices in the foreign aid app, we then went for the rather direct “enter your postcode”. We did suggest searches for both projects.

---

You can read the two stories here through registering and access up to two articles a week for free:

* [Ambulance trusts use loophole to claim faster response times](http://www.thetimes.co.uk/past-six-days/2017-01-07/news/ambulance-trusts-use-loophole-to-claim-faster-response-times-9mt7hgbp5)
* [Patiently waiting: ambulance response times in your area](http://www.thetimes.co.uk/article/patiently-waiting-ambulance-response-times-in-your-area-gdrw9vwzc)
