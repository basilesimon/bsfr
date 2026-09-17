d3.csv("http://blog.basilesimon.fr/assets/scripts/isr.csv", function(data) {
  var isrChart= dc.barChart("#isr-sorties");

  var ndx = crossfilter(data);
  var all = ndx.groupAll();

  var monthsDimension = ndx.dimension(function(d) {
    return d.Date;
  });

  var afghanistan = monthsDimension.group().reduceSum(function(d) {
    return d.Afghanistan;
  });

  var iraqSyria = monthsDimension.group().reduceSum(function(d) {
    return d.IraqSyria;
  });

  isrChart
    .width(700).height(300)
    .dimension(monthsDimension)
    .group(afghanistan, "Enduring Freedom (Afghanistan)")
    .stack(iraqSyria, "Inherent Resolve (Iraq and Syria)")
    .x(d3.scale.ordinal())
    .xUnits(dc.units.ordinal)
    .brushOn(false)
    //.legend(dc.legend().x(60).y(10).itemHeight(13).gap(5))
    .yAxisLabel("ISR sorties");

  dc.renderAll();
});

