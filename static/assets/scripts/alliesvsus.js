d3.csv("/assets/scripts/Airwars-dataset.csv", function(data) {
  var AlliesVUS = dc.barChart("#allies-versus-us");
  var AlliesAloneVUS = dc.barChart("#allies-versus-us-alone");

  var ndx = crossfilter(data);
  var all = ndx.groupAll();

  var targetCountriesDim = ndx.dimension(function(d) {
    if (d["Target country"] === "Iraq" || d["Target country"] === "Syria") {
      return d["Target country"];
    }
  });

  /* US v. allies */
  var USStrikesPerMonth = targetCountriesDim.group().reduceSum(function(d) {
    if (d["Country 1"] === "USA") {
      return d["Strikes in Iraq"] + d["Strikes in Syria"];
    } else {
      return 0;
    }
  });
  var alliesStrikesPerMonth = targetCountriesDim.group().reduceSum(function(d) {
    if (d["Country 1"] != "USA" || d["Country 2"]) {
      return d["Strikes in Iraq"] + d["Strikes in Syria"];
    } else {
      return 0;
    }
  });

  AlliesVUS
    .width(700).height(200)
    .dimension(targetCountriesDim)
    .group(USStrikesPerMonth, "USA")
    .stack(alliesStrikesPerMonth, "Allies")
    .x(d3.scale.ordinal())
    .xUnits(dc.units.ordinal)
    .elasticX(true)
    .brushOn(false)
    .legend(dc.legend().x(400).y(0).itemHeight(13).gap(5))
    .yAxisLabel("Total number of strikes");

  /* Allies alone v. US */
  var USStrikesPerMonth = targetCountriesDim.group().reduceSum(function(d) {
    if (d["Country 1"] === "USA") {
      return d["Strikes in Iraq"] + d["Strikes in Syria"];
    } else {
      return 0;
    }
  });
  var alliesStrikesPerMonth = targetCountriesDim.group().reduceSum(function(d) {
    if (d["Country 1"] != "USA") {
      return d["Strikes in Iraq"] + d["Strikes in Syria"];
    } else {
      return 0;
    }
  });

  AlliesAloneVUS
    .width(700).height(200)
    .dimension(targetCountriesDim)
    .group(USStrikesPerMonth, "USA")
    .stack(alliesStrikesPerMonth, "Allies alone")
    .x(d3.scale.ordinal())
    .xUnits(dc.units.ordinal)
    .elasticX(true)
    .brushOn(false)
    .legend(dc.legend().x(400).y(0).itemHeight(13).gap(5))
    .yAxisLabel("Total number of strikes");

  dc.renderAll();
});


