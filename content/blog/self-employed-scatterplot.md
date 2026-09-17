---
aliases: ["/2017/03/11/self-employed-scatterplot/"]
date: "2017-03-11T00:00:00Z"
description: "Build a weighted scatterplot about self-employment in the UK in no time with R and charting package ggplot2"
tags: []
title: "A super quick weighted scatterplot about self-employment in R and ggplot2"
---
# The two self-employed worlds

### The 'privileged' and the 'precarious'


<svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 720.00 576.00'>
<defs>
  <style type='text/css'>
    line, polyline, path, rect, circle {
      fill: none;
      stroke: #000000;
      stroke-linecap: round;
      stroke-linejoin: round;
      stroke-miterlimit: 10.00;
    }
  </style>
</defs>
<rect width='100%' height='100%' style='stroke: none; fill: #FFFFFF;'/>
<defs>
  <clipPath id='cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA=='>
    <rect x='58.55' y='5.98' width='559.29' height='524.33' />
  </clipPath>
</defs>
<polyline points='58.55,473.75 617.84,473.75 ' style='stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='58.55,342.83 617.84,342.83 ' style='stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='58.55,211.92 617.84,211.92 ' style='stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='58.55,81.00 617.84,81.00 ' style='stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='58.96,530.31 58.96,5.98 ' style='stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='151.60,530.31 151.60,5.98 ' style='stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='244.25,530.31 244.25,5.98 ' style='stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='336.90,530.31 336.90,5.98 ' style='stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='429.55,530.31 429.55,5.98 ' style='stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='522.19,530.31 522.19,5.98 ' style='stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='614.84,530.31 614.84,5.98 ' style='stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='58.55,408.29 617.84,408.29 ' style='stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='58.55,277.37 617.84,277.37 ' style='stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='58.55,146.46 617.84,146.46 ' style='stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='58.55,15.55 617.84,15.55 ' style='stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='105.28,530.31 105.28,5.98 ' style='stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='197.93,530.31 197.93,5.98 ' style='stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='290.58,530.31 290.58,5.98 ' style='stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='383.22,530.31 383.22,5.98 ' style='stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='475.87,530.31 475.87,5.98 ' style='stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<polyline points='568.52,530.31 568.52,5.98 ' style='stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='194.54' cy='465.48' r='9.06pt' style='stroke-width: 0.71; fill: #7F7F7F;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='223.54' cy='460.95' r='12.75pt' style='stroke-width: 0.71; fill: #7F7F7F;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='219.29' cy='502.55' r='16.36pt' style='stroke-width: 0.71; fill: #7F7F7F;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='145.92' cy='477.99' r='6.51pt' style='stroke-width: 0.71; fill: #7F7F7F;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='263.99' cy='387.01' r='6.30pt' style='stroke-width: 0.71; fill: #7F7F7F;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='154.90' cy='355.59' r='11.07pt' style='stroke-width: 0.71; fill: #7F7F7F;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='154.19' cy='471.24' r='10.58pt' style='stroke-width: 0.71; fill: #7F7F7F;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='181.32' cy='450.73' r='7.32pt' style='stroke-width: 0.71; fill: #7F7F7F;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='323.19' cy='129.66' r='7.73pt' style='stroke-width: 0.71; fill: #F8766D;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='292.02' cy='208.09' r='6.08pt' style='stroke-width: 0.71; fill: #F8766D;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='344.92' cy='292.44' r='5.99pt' style='stroke-width: 0.71; fill: #F8766D;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='592.41' cy='58.41' r='8.43pt' style='stroke-width: 0.71; fill: #F8766D;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='430.38' cy='118.09' r='7.75pt' style='stroke-width: 0.71; fill: #F8766D;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='275.99' cy='154.99' r='7.45pt' style='stroke-width: 0.71; fill: #F8766D;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='204.67' cy='210.63' r='8.95pt' style='stroke-width: 0.71; fill: #F8766D;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='124.88' cy='465.83' r='10.92pt' style='stroke-width: 0.71; fill: #7F7F7F;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='466.82' cy='85.04' r='5.28pt' style='stroke-width: 0.71; fill: #F8766D;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='134.33' cy='150.59' r='11.58pt' style='stroke-width: 0.71; fill: #F8766D;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='462.70' cy='29.81' r='9.38pt' style='stroke-width: 0.71; fill: #F8766D;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='124.25' cy='319.59' r='7.45pt' style='stroke-width: 0.71; fill: #7F7F7F;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='181.47' cy='105.13' r='8.01pt' style='stroke-width: 0.71; fill: #F8766D;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='83.97' cy='305.38' r='6.30pt' style='stroke-width: 0.71; fill: #7F7F7F;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<circle cx='116.59' cy='459.66' r='10.36pt' style='stroke-width: 0.71; fill: #7F7F7F;' clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)' />
<g clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)'><text x='219.24' y='510.41' style='font-size: 11.04px; font-family: Arial;' textLength='124.14px' lengthAdjust='spacingAndGlyphs'>Construction and building</text></g>
<g clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)'><text x='99.35' y='176.58' style='font-size: 11.04px; font-family: Arial;' textLength='48.93px' lengthAdjust='spacingAndGlyphs'>Education</text></g>
<g clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)'><text x='406.41' y='52.21' style='font-size: 11.04px; font-family: Arial;' textLength='64.81px' lengthAdjust='spacingAndGlyphs'>Health sector</text></g>
<g clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)'><text x='74.11' y='438.41' style='font-size: 11.04px; font-family: Arial;' textLength='62.35px' lengthAdjust='spacingAndGlyphs'>Hairdressers</text></g>
<g clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)'><text x='71.22' y='287.86' style='font-size: 11.04px; font-family: Arial;' textLength='105.17px' lengthAdjust='spacingAndGlyphs'>Sports and recreation</text></g>
<g clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)'><text x='188.15' y='84.94' style='font-size: 11.04px; font-family: Arial;' textLength='19.56px' lengthAdjust='spacingAndGlyphs'>Arts</text></g>
<g clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)'><text x='355.40' y='314.04' style='font-size: 11.04px; font-family: Arial;' textLength='55.64px' lengthAdjust='spacingAndGlyphs'>Real estate</text></g>
<g clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)'><text x='129.20' y='497.32' style='font-size: 11.04px; font-family: Arial;' textLength='26.28px' lengthAdjust='spacingAndGlyphs'>Taxis</text></g>
<g clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)'><text x='287.38' y='111.12' style='font-size: 11.04px; font-family: Arial;' textLength='99.04px' lengthAdjust='spacingAndGlyphs'>IT and programming</text></g>
<g clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)'><text x='441.32' y='137.31' style='font-size: 11.04px; font-family: Arial;' textLength='69.09px' lengthAdjust='spacingAndGlyphs'>Consultancies</text></g>
<g clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)'><text x='165.34' y='386.04' style='font-size: 11.04px; font-family: Arial;' textLength='28.12px' lengthAdjust='spacingAndGlyphs'>Retail</text></g>
<g clip-path='url(#cpNTguNTUwMXw2MTcuODM3fDUzMC4zMDh8NS45Nzc1OA==)'><text x='497.69' y='39.12' style='font-size: 11.04px; font-family: Arial;' textLength='104.59px' lengthAdjust='spacingAndGlyphs'>Legal and accounting</text></g>
<defs>
  <clipPath id='cpMHw3MjB8NTc2fDA='>
    <rect x='0.00' y='0.00' width='720.00' height='576.00' />
  </clipPath>
</defs>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='21.74' y='411.87' style='font-size: 9.60px; font-family: Arial;' textLength='20.01px' lengthAdjust='spacingAndGlyphs'>20%</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='21.74' y='280.95' style='font-size: 9.60px; font-family: Arial;' textLength='20.01px' lengthAdjust='spacingAndGlyphs'>40%</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='21.74' y='150.04' style='font-size: 9.60px; font-family: Arial;' textLength='20.01px' lengthAdjust='spacingAndGlyphs'>60%</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='21.74' y='19.12' style='font-size: 9.60px; font-family: Arial;' textLength='20.01px' lengthAdjust='spacingAndGlyphs'>80%</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='91.38' y='554.26' style='font-size: 9.60px; font-family: Arial;' textLength='27.81px' lengthAdjust='spacingAndGlyphs'>10000</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='184.02' y='554.26' style='font-size: 9.60px; font-family: Arial;' textLength='27.81px' lengthAdjust='spacingAndGlyphs'>20000</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='276.67' y='554.26' style='font-size: 9.60px; font-family: Arial;' textLength='27.81px' lengthAdjust='spacingAndGlyphs'>30000</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='369.32' y='554.26' style='font-size: 9.60px; font-family: Arial;' textLength='27.81px' lengthAdjust='spacingAndGlyphs'>40000</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='461.97' y='554.26' style='font-size: 9.60px; font-family: Arial;' textLength='27.81px' lengthAdjust='spacingAndGlyphs'>50000</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='554.61' y='554.26' style='font-size: 9.60px; font-family: Arial;' textLength='27.81px' lengthAdjust='spacingAndGlyphs'>60000</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='293.18' y='567.63' style='font-size: 12.00px; font-family: Arial;' textLength='90.04px' lengthAdjust='spacingAndGlyphs'>Mean income (£)</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text transform='translate(16.96,328.85) rotate(-90)' style='font-size: 12.00px; font-family: Arial;' textLength='121.42px' lengthAdjust='spacingAndGlyphs'>Percentage of degrees</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='630.59' y='172.32' style='font-size: 12.00px; font-family: Arial;' textLength='48.69px' lengthAdjust='spacingAndGlyphs'>Category</text></g>
<circle cx='639.23' cy='185.28' r='1.95pt' style='stroke-width: 0.71; fill: #F8766D;' clip-path='url(#cpMHw3MjB8NTc2fDA=)' />
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='650.03' y='188.86' style='font-size: 9.60px; font-family: Arial;' textLength='43.91px' lengthAdjust='spacingAndGlyphs'>Privileged</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='630.59' y='216.69' style='font-size: 12.00px; font-family: Arial;' textLength='42.68px' lengthAdjust='spacingAndGlyphs'>Number</text></g>
<circle cx='650.81' cy='230.05' r='7.16pt' style='stroke-width: 0.71;' clip-path='url(#cpMHw3MjB8NTc2fDA=)' />
<circle cx='650.81' cy='251.87' r='9.98pt' style='stroke-width: 0.71;' clip-path='url(#cpMHw3MjB8NTc2fDA=)' />
<circle cx='650.81' cy='280.31' r='12.14pt' style='stroke-width: 0.71;' clip-path='url(#cpMHw3MjB8NTc2fDA=)' />
<circle cx='650.81' cy='314.05' r='13.97pt' style='stroke-width: 0.71;' clip-path='url(#cpMHw3MjB8NTc2fDA=)' />
<circle cx='650.81' cy='352.35' r='15.57pt' style='stroke-width: 0.71;' clip-path='url(#cpMHw3MjB8NTc2fDA=)' />
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='673.18' y='233.63' style='font-size: 9.60px; font-family: Arial;' textLength='28.09px' lengthAdjust='spacingAndGlyphs'>1e+05</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='673.18' y='255.45' style='font-size: 9.60px; font-family: Arial;' textLength='28.09px' lengthAdjust='spacingAndGlyphs'>2e+05</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='673.18' y='283.89' style='font-size: 9.60px; font-family: Arial;' textLength='28.09px' lengthAdjust='spacingAndGlyphs'>3e+05</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='673.18' y='317.63' style='font-size: 9.60px; font-family: Arial;' textLength='28.09px' lengthAdjust='spacingAndGlyphs'>4e+05</text></g>
<g clip-path='url(#cpMHw3MjB8NTc2fDA=)'><text x='673.18' y='355.92' style='font-size: 9.60px; font-family: Arial;' textLength='28.09px' lengthAdjust='spacingAndGlyphs'>5e+05</text></g>
</svg>

---

## Import your dataset

This example uses data from a Resolution Foundation report about self-employment in the UK. It surfaces so-called _privileged_ and _precarious_ professions (based on unclear factors, judging from the report). We'll plot the mean income against the percentage of degrees per SIC (Standard Industrial Classification).

```
df <- read_csv("https://raw.githubusercontent.com/basilesimon/interactive-journalism-module/master/week5/exercise/data_annotated.csv")
```

## Basic plot

We'll use ggplot2's `geom_point` to create our scatterplot. Some precisions:

- To fill the circles with a colour, you've got to change their shape to an empty circle with a stroke. [This is a handy guide to shapes](http://sape.inf.usi.ch/quick-reference/ggplot2/shape) in ggplot2.
- `seq(0, 70000, 10000)` is essentially a shorthand to output an array like so: `[0, 10000, 20000, ..., 70000]`
- If you're surprised by the magic `scales::percent`, [read the docs about continuous scales](http://docs.ggplot2.org/current/scale_continuous.html)

```
colors <- ggplot(df, aes(x = Mean, y = Degrees, size = Number, fill = Category)) +
  geom_point(shape = 21) +
  scale_size_area(max_size = 15) +
  scale_x_continuous(breaks = seq(0, 70000, 10000), name = "Mean income (£)") +
  scale_y_continuous(labels = scales::percent, name = "Percentage of degrees")
```

## Annotations are the core of the job

Annotations in R are super simple, if only not so fancy.

In this instance, we'll annotate a few of the industry codes to give a bit more life to the plot.

Note that unless we add an interaction layer with tooltips and mouseovers with D3 later, this is everything the reader will see and read. It is good practice to assume the reader won't click or move their mouse about upon implementing tooltips and interactive features anyway, so we'll go down the simple and most effective route: by pointing out what's interesting straight away.

```
annotate("text", x = 29000, y = .05, label = "Construction and building") +
```

## Export your plot as SVG...

... and savour the pleasures of CSS and Illustrator — or even of d3 manipulations.

```
ggsave(file="file.svg", plot=plot, width=10, height=10)
```

---

# Full code

```r
library(ggplot2)
library(readr)
library(ggthemes)

# Load new batch of annotated data
df <- read_csv("https://raw.githubusercontent.com/basilesimon/interactive-journalism-module/master/week5/exercise/data_annotated.csv")

# Color now depends on assigned category
colors <- ggplot(df, aes(x = Mean, y = Degrees, size = Number, fill = Category)) +
  geom_point(shape = 21) +
  scale_size_area(max_size = 15) +
  scale_x_continuous(breaks = seq(0, 70000, 10000), name = "Mean income (£)") +
  scale_y_continuous(labels = scales::percent, name = "Percentage of degrees")

# More annotations
labels <- colors +
  annotate("text", x = 29000, y = .05, label = "Construction and building") +
  annotate("text", x = 12000, y = .56, label = "Education") +
  annotate("text", x = 46000, y = .75, label = "Health sector") +
  annotate("text", x = 10000, y = .16, label = "Hairdressers") +
  annotate("text", x = 12000, y = .39, label = "Sports and recreation") +
  annotate("text", x = 20000, y = 0.7, label = "Arts") +
  annotate("text", x = 40000, y = .35, label = "Real estate") +
  annotate("text", x = 14000, y = .07, label = "Taxis") +
  annotate("text", x = 35000, y = .66, label = "IT and programming") +
  annotate("text", x = 50000, y = .62, label = "Consultancies") +
  annotate("text", x = 18000, y = .24, label = "Retail") +
  annotate("text", x = 58000, y = .77, label = "Legal and accounting")

# Playing with some themes
# And display plot
plot <- labels + theme_minimal()
plot
```

Data courtesy of Resolution Foundation, Feb. 2017 - [*A tough gig? The nature of self-employment in 21st Century Britain and policy implications*](http://www.resolutionfoundation.org/app/uploads/2017/02/Self-employment-presentation.pdf), by Dan Tomlinson and Adam Corlett
