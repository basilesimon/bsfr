d3.csv("http://blog.basilesimon.fr/assets/scripts/airpower-statistics.csv", function(data) {
  var airpowerStatisticsChart = dc.barChart("#weapons-release");

  var ndx = crossfilter(data);
  var all = ndx.groupAll();

  var monthsDimension = ndx.dimension(function(d) {
    return d.Date;
  });

  var enduringFreedom = monthsDimension.group().reduceSum(function(d) {
    return d.EF;
  });

  var inherentResolve = monthsDimension.group().reduceSum(function(d) {
    return d.IR;
  });

 airpowerStatisticsChart
    .width(700).height(300)
    .dimension(monthsDimension)
    .group(enduringFreedom, "Enduring Freedom (Afghanistan)")
    .stack(inherentResolve, "Inherent Resolve (Iraq and Syria)")
    .x(d3.scale.ordinal())
    .xUnits(dc.units.ordinal)
    .brushOn(false)
    .legend(dc.legend().x(60).y(10).itemHeight(13).gap(5))
    .yAxisLabel("Weapons releases");

  dc.renderAll();
});
