---
aliases: ["/2017/03/22/quick-r-uk-foreign-trade-balance/"]
date: "2017-03-22T00:00:00Z"
description: "No trick for this example: we're plotting imports and exports on different axes, thus isolating the most important trade partners of the United Kingdom.…"
tags: []
title: "Quick R: the UK foreign trade balance in ggplot2"
---
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   viewBox="0 0 720.00 576.00"
   id="svg3838"
   version="1.1"
   inkscape:version="0.91 r13725"
   sodipodi:docname="file2.svg">
  <metadata
     id="metadata4300">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <sodipodi:namedview
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1"
     objecttolerance="10"
     gridtolerance="10"
     guidetolerance="10"
     inkscape:pageopacity="0"
     inkscape:pageshadow="2"
     inkscape:window-width="1032"
     inkscape:window-height="764"
     id="namedview4298"
     showgrid="false"
     inkscape:zoom="0.953125"
     inkscape:cx="338.0284"
     inkscape:cy="263.43203"
     inkscape:window-x="0"
     inkscape:window-y="0"
     inkscape:window-maximized="0"
     inkscape:current-layer="svg3838" />
  <defs
     id="defs3840">
    <style
       type="text/css"
       id="style3842"><![CDATA[
    line, polyline, path, rect, circle {
      fill: none;
      stroke: #000000;
      stroke-linecap: round;
      stroke-linejoin: round;
      stroke-miterlimit: 10.00;
    }
  ]]></style>
  </defs>
  <rect
     width="720"
     height="576"
     style="fill:#ffffff;stroke:none;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:10"
     id="rect3844"
     x="-96"
     y="29.90164" />
  <defs
     id="defs3846">
    <clipPath
       id="cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==">
      <rect
         x="74.68"
         y="5.98"
         width="639.34"
         height="524.33"
         id="rect3849" />
    </clipPath>
  </defs>
  <polyline
     points="74.68,456.82 714.02,456.82 "
     style="stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3851" />
  <polyline
     points="74.68,357.52 714.02,357.52 "
     style="stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3853" />
  <polyline
     points="74.68,258.21 714.02,258.21 "
     style="stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3855" />
  <polyline
     points="74.68,158.91 714.02,158.91 "
     style="stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3857" />
  <polyline
     points="74.68,59.60 714.02,59.60 "
     style="stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3859" />
  <polyline
     points="176.40,530.31 176.40,5.98 "
     style="stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3861" />
  <polyline
     points="321.70,530.31 321.70,5.98 "
     style="stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3863" />
  <polyline
     points="467.00,530.31 467.00,5.98 "
     style="stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3865" />
  <polyline
     points="612.31,530.31 612.31,5.98 "
     style="stroke-width: 1.07; stroke: #FAFAFA; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3867" />
  <polyline
     points="74.68,506.48 714.02,506.48 "
     style="stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3869" />
  <polyline
     points="74.68,407.17 714.02,407.17 "
     style="stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3871" />
  <polyline
     points="74.68,307.86 714.02,307.86 "
     style="stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3873" />
  <polyline
     points="74.68,208.56 714.02,208.56 "
     style="stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3875" />
  <polyline
     points="74.68,109.25 714.02,109.25 "
     style="stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3877" />
  <polyline
     points="74.68,9.95 714.02,9.95 "
     style="stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3879" />
  <polyline
     points="103.74,530.31 103.74,5.98 "
     style="stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3881" />
  <polyline
     points="249.05,530.31 249.05,5.98 "
     style="stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3883" />
  <polyline
     points="394.35,530.31 394.35,5.98 "
     style="stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3885" />
  <polyline
     points="539.66,530.31 539.66,5.98 "
     style="stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3887" />
  <polyline
     points="684.96,530.31 684.96,5.98 "
     style="stroke-width: 0.43; stroke: #E5E5E5; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline3889" />
  <circle
     cx="104.61"
     cy="505.76"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3891" />
  <circle
     cx="103.77"
     cy="506.38"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3893" />
  <circle
     cx="117.82"
     cy="504.80"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3895" />
  <circle
     cx="104.10"
     cy="506.29"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3897" />
  <circle
     cx="109.63"
     cy="502.53"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3899" />
  <circle
     cx="103.93"
     cy="506.32"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3901" />
  <circle
     cx="108.81"
     cy="504.16"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3903" />
  <circle
     cx="103.86"
     cy="506.37"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3905" />
  <circle
     cx="138.99"
     cy="472.49"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3907" />
  <circle
     cx="133.84"
     cy="496.09"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3909" />
  <circle
     cx="104.70"
     cy="502.70"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3911" />
  <circle
     cx="104.67"
     cy="505.98"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3913" />
  <circle
     cx="105.68"
     cy="504.47"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3915" />
  <circle
     cx="120.40"
     cy="503.42"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3917" />
  <circle
     cx="104.63"
     cy="506.03"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3919" />
  <circle
     cx="103.93"
     cy="506.20"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3921" />
  <circle
     cx="273.79"
     cy="446.19"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3923" />
  <circle
     cx="104.46"
     cy="506.40"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3925" />
  <circle
     cx="106.48"
     cy="503.83"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3927" />
  <circle
     cx="103.83"
     cy="506.34"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3929" />
  <circle
     cx="104.16"
     cy="506.25"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #336A98;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3931" />
  <circle
     cx="103.95"
     cy="505.58"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3933" />
  <circle
     cx="122.02"
     cy="491.28"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3935" />
  <circle
     cx="105.81"
     cy="503.62"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3937" />
  <circle
     cx="104.27"
     cy="505.15"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3939" />
  <circle
     cx="109.11"
     cy="503.45"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3941" />
  <circle
     cx="103.82"
     cy="506.38"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3943" />
  <circle
     cx="104.52"
     cy="506.07"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3945" />
  <circle
     cx="109.85"
     cy="506.36"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3947" />
  <circle
     cx="104.72"
     cy="506.01"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3949" />
  <circle
     cx="159.10"
     cy="477.68"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3951" />
  <circle
     cx="105.94"
     cy="501.96"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3953" />
  <circle
     cx="103.80"
     cy="506.40"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3955" />
  <circle
     cx="108.79"
     cy="503.62"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3957" />
  <circle
     cx="382.63"
     cy="440.03"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3959" />
  <circle
     cx="108.80"
     cy="503.98"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3961" />
  <circle
     cx="104.12"
     cy="504.60"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3963" />
  <circle
     cx="105.41"
     cy="506.09"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3965" />
  <circle
     cx="104.99"
     cy="505.70"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3967" />
  <circle
     cx="107.18"
     cy="505.04"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3969" />
  <circle
     cx="104.96"
     cy="506.32"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3971" />
  <circle
     cx="112.08"
     cy="502.55"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3973" />
  <circle
     cx="144.18"
     cy="495.41"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3975" />
  <circle
     cx="103.87"
     cy="506.26"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3977" />
  <circle
     cx="137.45"
     cy="484.31"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3979" />
  <circle
     cx="103.79"
     cy="506.45"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #336A98;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3981" />
  <circle
     cx="105.10"
     cy="505.90"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3983" />
  <circle
     cx="104.58"
     cy="505.90"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3985" />
  <circle
     cx="112.08"
     cy="499.77"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3987" />
  <circle
     cx="103.79"
     cy="506.40"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3989" />
  <circle
     cx="105.89"
     cy="505.95"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3991" />
  <circle
     cx="105.76"
     cy="505.47"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3993" />
  <circle
     cx="105.25"
     cy="505.56"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3995" />
  <circle
     cx="104.12"
     cy="505.88"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3997" />
  <circle
     cx="104.01"
     cy="506.38"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle3999" />
  <circle
     cx="122.44"
     cy="495.75"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4001" />
  <circle
     cx="367.90"
     cy="375.68"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4003" />
  <circle
     cx="104.19"
     cy="506.00"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4005" />
  <circle
     cx="104.25"
     cy="506.34"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4007" />
  <circle
     cx="104.17"
     cy="506.11"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4009" />
  <circle
     cx="614.95"
     cy="313.82"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4011" />
  <circle
     cx="106.21"
     cy="503.27"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4013" />
  <circle
     cx="109.16"
     cy="494.99"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4015" />
  <circle
     cx="126.00"
     cy="497.70"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4017" />
  <circle
     cx="104.59"
     cy="506.31"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4019" />
  <circle
     cx="103.77"
     cy="506.29"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4021" />
  <circle
     cx="104.22"
     cy="506.22"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4023" />
  <circle
     cx="104.67"
     cy="506.42"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4025" />
  <circle
     cx="164.96"
     cy="473.74"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4027" />
  <circle
     cx="125.60"
     cy="499.29"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4029" />
  <circle
     cx="108.05"
     cy="504.88"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4031" />
  <circle
     cx="172.65"
     cy="480.22"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4033" />
  <circle
     cx="113.54"
     cy="502.93"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4035" />
  <circle
     cx="104.35"
     cy="505.72"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4037" />
  <circle
     cx="105.10"
     cy="504.06"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4039" />
  <circle
     cx="239.42"
     cy="404.47"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4041" />
  <circle
     cx="116.27"
     cy="498.47"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4043" />
  <circle
     cx="252.54"
     cy="436.24"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4045" />
  <circle
     cx="105.44"
     cy="506.00"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4047" />
  <circle
     cx="173.25"
     cy="464.74"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4049" />
  <circle
     cx="104.29"
     cy="503.44"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4051" />
  <circle
     cx="108.74"
     cy="503.45"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4053" />
  <circle
     cx="107.22"
     cy="504.15"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4055" />
  <circle
     cx="109.46"
     cy="500.80"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4057" />
  <circle
     cx="103.98"
     cy="506.46"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4059" />
  <circle
     cx="108.31"
     cy="505.09"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4061" />
  <circle
     cx="104.72"
     cy="504.41"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4063" />
  <circle
     cx="104.59"
     cy="505.00"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4065" />
  <circle
     cx="103.95"
     cy="506.24"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4067" />
  <circle
     cx="110.57"
     cy="504.63"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4069" />
  <circle
     cx="121.33"
     cy="496.98"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4071" />
  <circle
     cx="103.87"
     cy="506.17"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4073" />
  <circle
     cx="104.11"
     cy="503.42"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4075" />
  <circle
     cx="104.06"
     cy="506.40"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4077" />
  <circle
     cx="104.06"
     cy="506.40"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4079" />
  <circle
     cx="120.53"
     cy="497.18"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4081" />
  <circle
     cx="104.46"
     cy="506.37"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4083" />
  <circle
     cx="108.50"
     cy="502.80"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4085" />
  <circle
     cx="103.85"
     cy="506.38"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4087" />
  <circle
     cx="103.79"
     cy="506.36"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4089" />
  <circle
     cx="107.82"
     cy="505.61"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4091" />
  <circle
     cx="115.46"
     cy="498.72"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4093" />
  <circle
     cx="105.18"
     cy="506.04"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4095" />
  <circle
     cx="103.91"
     cy="506.34"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4097" />
  <circle
     cx="111.14"
     cy="502.96"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4099" />
  <circle
     cx="104.61"
     cy="505.82"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4101" />
  <circle
     cx="104.02"
     cy="506.07"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4103" />
  <circle
     cx="105.39"
     cy="506.07"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4105" />
  <circle
     cx="372.04"
     cy="380.17"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4107" />
  <circle
     cx="113.04"
     cy="502.38"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4109" />
  <circle
     cx="103.92"
     cy="506.38"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4111" />
  <circle
     cx="103.84"
     cy="506.42"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4113" />
  <circle
     cx="116.76"
     cy="497.23"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4115" />
  <circle
     cx="206.95"
     cy="482.50"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4117" />
  <circle
     cx="105.36"
     cy="503.58"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4119" />
  <circle
     cx="115.09"
     cy="502.83"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4121" />
  <circle
     cx="104.14"
     cy="505.54"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4123" />
  <circle
     cx="104.62"
     cy="505.68"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4125" />
  <circle
     cx="103.84"
     cy="506.35"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4127" />
  <circle
     cx="106.34"
     cy="505.53"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4129" />
  <circle
     cx="110.95"
     cy="504.31"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4131" />
  <circle
     cx="177.51"
     cy="485.11"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4133" />
  <circle
     cx="136.44"
     cy="496.68"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4135" />
  <circle
     cx="123.65"
     cy="496.08"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4137" />
  <circle
     cx="117.57"
     cy="500.21"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4139" />
  <circle
     cx="141.97"
     cy="484.16"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4141" />
  <circle
     cx="103.77"
     cy="506.39"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4143" />
  <circle
     cx="120.11"
     cy="481.62"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4145" />
  <circle
     cx="104.09"
     cy="506.00"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4147" />
  <circle
     cx="105.23"
     cy="505.80"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4149" />
  <circle
     cx="104.25"
     cy="506.36"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4151" />
  <circle
     cx="103.80"
     cy="506.24"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4153" />
  <circle
     cx="131.78"
     cy="478.46"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4155" />
  <circle
     cx="119.74"
     cy="503.64"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4157" />
  <circle
     cx="106.69"
     cy="505.15"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4159" />
  <circle
     cx="132.75"
     cy="490.08"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4161" />
  <circle
     cx="138.70"
     cy="481.41"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4163" />
  <circle
     cx="285.35"
     cy="447.82"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4165" />
  <circle
     cx="114.19"
     cy="505.04"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4167" />
  <circle
     cx="104.20"
     cy="506.37"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4169" />
  <circle
     cx="103.76"
     cy="506.42"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4171" />
  <circle
     cx="103.87"
     cy="505.92"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4173" />
  <circle
     cx="176.16"
     cy="471.38"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4175" />
  <circle
     cx="194.86"
     cy="423.20"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4177" />
  <circle
     cx="103.77"
     cy="506.45"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4179" />
  <circle
     cx="129.72"
     cy="499.26"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4181" />
  <circle
     cx="103.77"
     cy="506.45"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4183" />
  <circle
     cx="104.58"
     cy="505.59"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4185" />
  <circle
     cx="129.43"
     cy="498.88"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4187" />
  <circle
     cx="103.82"
     cy="506.07"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4189" />
  <circle
     cx="104.96"
     cy="505.62"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4191" />
  <circle
     cx="106.12"
     cy="505.55"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4193" />
  <circle
     cx="166.10"
     cy="487.54"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4195" />
  <circle
     cx="103.99"
     cy="506.27"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4197" />
  <circle
     cx="104.35"
     cy="506.14"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4199" />
  <circle
     cx="106.31"
     cy="504.82"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4201" />
  <circle
     cx="131.03"
     cy="472.21"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4203" />
  <circle
     cx="534.27"
     cy="123.46"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4205" />
  <circle
     cx="104.46"
     cy="505.50"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4207" />
  <circle
     cx="103.81"
     cy="506.32"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4209" />
  <circle
     cx="105.67"
     cy="505.14"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4211" />
  <circle
     cx="128.82"
     cy="504.39"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #132B43;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4213" />
  <circle
     cx="103.76"
     cy="506.46"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4215" />
  <circle
     cx="103.76"
     cy="506.28"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4217" />
  <circle
     cx="104.18"
     cy="505.95"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4219" />
  <circle
     cx="104.22"
     cy="506.12"
     r="5.69pt"
     style="stroke-width: 0.71; fill: #56B1F7;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="circle4221" />
  <polyline
     points="110.23,503.16 116.70,499.84 123.17,496.52 129.64,493.20 136.11,489.88 142.58,486.56 149.05,483.24 155.52,479.91 161.99,476.59 168.47,473.27 174.94,469.95 181.41,466.63 187.88,463.31 194.35,459.99 200.82,456.67 207.29,453.35 213.76,450.03 220.23,446.71 226.70,443.39 233.17,440.07 239.64,436.75 246.11,433.43 252.59,430.11 259.06,426.79 265.53,423.47 272.00,420.15 278.47,416.83 284.94,413.51 291.41,410.19 297.88,406.87 304.35,403.55 310.82,400.23 317.29,396.91 323.76,393.59 330.23,390.27 336.70,386.95 343.18,383.63 349.65,380.31 356.12,376.99 362.59,373.67 369.06,370.35 375.53,367.03 382.00,363.70 388.47,360.38 394.94,357.06 401.41,353.74 407.88,350.42 414.35,347.10 420.82,343.78 427.30,340.46 433.77,337.14 440.24,333.82 446.71,330.50 453.18,327.18 459.65,323.86 466.12,320.54 472.59,317.22 479.06,313.90 485.53,310.58 492.00,307.26 498.47,303.94 504.94,300.62 511.41,297.30 517.89,293.98 524.36,290.66 530.83,287.34 537.30,284.02 543.77,280.70 550.24,277.38 556.71,274.06 563.18,270.74 569.65,267.42 576.12,264.10 582.59,260.78 589.06,257.46 595.53,254.14 602.01,250.82 608.48,247.49 614.95,244.17 "
     style="stroke-width: 2.13; stroke: #3366FF; stroke-linecap: butt;"
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="polyline4223" />
  <g
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="g4225"
     transform="translate(-9.442623,-10.491803)">
    <text
       x="215.42"
       y="311.79999"
       style="font-size:11.03999996px;font-family:Arial"
       textLength="67.25px"
       lengthAdjust="spacingAndGlyphs"
       id="text4227">
      <tspan
         style="font-size:25px;fill:#808080"
         id="tspan4320">Trade surplus</tspan>
    </text>
  </g>
  <g
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="g4229">
    <text
       x="436.74"
       y="502.47"
       style="font-size: 11.04px; font-family: Arial;"
       textLength="60.53px"
       lengthAdjust="spacingAndGlyphs"
       id="text4231">
      <tspan
         style="font-size:25px;fill:#808080"
         id="tspan4318">Trade deficit</tspan>
    </text>
  </g>
  <g
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="g4233"
     transform="translate(0,30)">
    <text
       x="414.70105"
       y="141.21071"
       style="font-size:11.03999996px;font-family:Arial"
       textLength="66.04px"
       lengthAdjust="spacingAndGlyphs"
       id="text4235">
      <tspan
         style="font-size:12.5px"
         id="tspan4302">United States</tspan>
    </text>
  </g>
  <g
     clip-path="url(#cpNzQuNjgyOXw3MTQuMDIyfDUzMC4zMDh8NS45Nzc1OA==)"
     id="g4237"
     transform="translate(-17.836066,19.409836)">
    <text
       x="560.63"
       y="331.66"
       style="font-size:11.03999996px;font-family:Arial"
       textLength="45.24px"
       lengthAdjust="spacingAndGlyphs"
       id="text4239">Germany</text>
  </g>
  <defs
     id="defs4241">
    <clipPath
       id="cpMHw3MjB8NTc2fDA=">
      <rect
         x="0.00"
         y="0.00"
         width="720.00"
         height="576.00"
         id="rect4244" />
    </clipPath>
  </defs>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4246">
    <text
       x="52.33"
       y="510.05"
       style="font-size: 9.60px; font-family: Arial;"
       textLength="5.56px"
       lengthAdjust="spacingAndGlyphs"
       id="text4248">0</text>
  </g>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4250">
    <text
       x="27.31"
       y="410.75"
       style="font-size: 9.60px; font-family: Arial;"
       textLength="30.59px"
       lengthAdjust="spacingAndGlyphs"
       id="text4252">25,000</text>
  </g>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4254">
    <text
       x="27.31"
       y="311.44"
       style="font-size: 9.60px; font-family: Arial;"
       textLength="30.59px"
       lengthAdjust="spacingAndGlyphs"
       id="text4256">50,000</text>
  </g>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4258">
    <text
       x="27.31"
       y="212.14"
       style="font-size: 9.60px; font-family: Arial;"
       textLength="30.59px"
       lengthAdjust="spacingAndGlyphs"
       id="text4260">75,000</text>
  </g>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4262">
    <text
       x="21.74"
       y="112.83"
       style="font-size: 9.60px; font-family: Arial;"
       textLength="36.15px"
       lengthAdjust="spacingAndGlyphs"
       id="text4264">100,000</text>
  </g>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4266">
    <text
       x="21.74"
       y="13.53"
       style="font-size: 9.60px; font-family: Arial;"
       textLength="36.15px"
       lengthAdjust="spacingAndGlyphs"
       id="text4268">125,000</text>
  </g>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4270">
    <text
       x="100.96"
       y="554.26"
       style="font-size: 9.60px; font-family: Arial;"
       textLength="5.56px"
       lengthAdjust="spacingAndGlyphs"
       id="text4272">0</text>
  </g>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4274">
    <text
       x="233.76"
       y="554.26"
       style="font-size: 9.60px; font-family: Arial;"
       textLength="30.59px"
       lengthAdjust="spacingAndGlyphs"
       id="text4276">20,000</text>
  </g>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4278">
    <text
       x="379.06"
       y="554.26"
       style="font-size: 9.60px; font-family: Arial;"
       textLength="30.59px"
       lengthAdjust="spacingAndGlyphs"
       id="text4280">40,000</text>
  </g>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4282">
    <text
       x="524.36"
       y="554.26"
       style="font-size: 9.60px; font-family: Arial;"
       textLength="30.59px"
       lengthAdjust="spacingAndGlyphs"
       id="text4284">60,000</text>
  </g>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4286">
    <text
       x="669.67"
       y="554.26"
       style="font-size: 9.60px; font-family: Arial;"
       textLength="30.59px"
       lengthAdjust="spacingAndGlyphs"
       id="text4288">80,000</text>
  </g>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4290"
     transform="translate(-72,0)">
    <text
       x="374.35001"
       y="567.63"
       style="font-size:12px;font-family:Arial"
       textLength="40.01px"
       lengthAdjust="spacingAndGlyphs"
       id="text4292">Imports (in £m)</text>
  </g>
  <g
     clip-path="url(#cpMHw3MjB8NTc2fDA=)"
     id="g4294"
     transform="translate(0,-1.2500001e-6)">
    <text
       transform="matrix(0,-1,1,0,16.96,288.48)"
       style="font-size:12px;font-family:Arial"
       textLength="40.68px"
       lengthAdjust="spacingAndGlyphs"
       id="text4296">Exports (in £m)</text>
  </g>
  <flowRoot
     xml:space="preserve"
     id="flowRoot4304"
     style="font-style:normal;font-weight:normal;font-size:40px;line-height:125%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
     transform="translate(0,26)"><flowRegion
       id="flowRegion4306"><rect
         id="rect4308"
         width="162.8432"
         height="49.33519"
         x="415.45422"
         y="146.45001"
         style="fill:none;stroke:#000000;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:10" /></flowRegion><flowPara
       id="flowPara4310"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:12.5px;font-family:Arial;-inkscape-font-specification:Arial">first export destination</flowPara></flowRoot>  <text
     xml:space="preserve"
     style="font-style:normal;font-weight:normal;font-size:40px;line-height:125%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
     x="336.81467"
     y="344.90359"
     id="text4341"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan4343"
       x="336.81467"
       y="344.90359" /></text>
  <path
     style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:10;stroke-opacity:1"
     d="m 451.14754,156.85246 c 0,-28.32787 69.77049,-34.62295 69.77049,-34.62295"
     id="path4349"
     inkscape:connector-curvature="0" />
  <path
     style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:10;stroke-opacity:1"
     d="m 592.2623,348.32787 c 23.08196,0 22.55737,-22.55738 22.55737,-22.55738"
     id="path4353"
     inkscape:connector-curvature="0" />
  <text
     xml:space="preserve"
     style="font-style:normal;font-weight:normal;font-size:40px;line-height:125%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
     x="423.86884"
     y="402.36066"
     id="text4355"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan4357"
       x="423.86884"
       y="402.36066"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:12.5px;font-family:Arial;-inkscape-font-specification:Arial">France and</tspan><tspan
       sodipodi:role="line"
       x="423.86884"
       y="417.98566"
       id="tspan4359"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:12.5px;font-family:Arial;-inkscape-font-specification:Arial">the Netherlands</tspan></text>
  <text
     xml:space="preserve"
     style="font-style:normal;font-weight:normal;font-size:40px;line-height:125%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
     x="315.27869"
     y="480.5246"
     id="text4361"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan4363"
       x="315.27869"
       y="480.5246"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:12.5px;font-family:Arial;-inkscape-font-specification:Arial">China</tspan></text>
  <path
     style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:10;stroke-opacity:1"
     d="m 352,476.32787 c 32.52459,0 30.42623,-25.18033 30.42623,-25.18033"
     id="path4365"
     inkscape:connector-curvature="0" />
  <path
     style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:10;stroke-opacity:1"
     d="m 417.04918,407.60656 c -43.01639,0 -44.59016,-17.31148 -44.59016,-17.31148"
     id="path4367"
     inkscape:connector-curvature="0" />
</svg>

No trick for this example: we're plotting imports and exports on different axes, thus isolating the most important trade partners of the United Kingdom.

To obtain different colours depending on wether the balance of trade with this country is a surplus or an excedent, we run some quick `dplyr` transformations:

1. We calculate the trade balance (exports minus imports) and store this in a new column, thanks to `mutate()`:

```r
d.2015.balance <- d.2015 %>% mutate(balance = Exports - Imports)
```

2. If the  balance is a surplus, it will be positive (more exports than imports). If it is a deficit, it will be negative. We check the sign with R's built-in `sign()` method, and send the result to a new column, aptly named `balance`, again with `mutate()`:

```r
d.2015.balance <- d.2015.balance %>% mutate(surplus = sign(balance))
```

---

The plotting is very straightforward. We save the file as SVG and open it up in Inkscape to make it come to life a little bit.

We add some smooth curved lines for annotations and liven up the key. Here is the result, as a GIF:

![](/assets/output_wHQk2f.gif)

```r
library(dplyr)
library(readr)
library(scales)
library(ggplot2)
library(ggthemes)

# read csv file from Github
d <- read_csv("https://raw.githubusercontent.com/times/trade-component/master/app/static/data/join_simple.csv?token=AFb-IG5fP6yINxBFEfRkwqATsjFRXihXks5Y2_pPwA%3D%3D")

# only select 2015 data
d.2015 <- d %>% filter(Date == 2015)

# add a 'balance' column
d.2015.balance <- d.2015 %>% mutate(balance = Exports - Imports)

# add a 'surplus' column (-1, 0, or 1) so we have
# categorical colours on the plot
# -1 is deficit (more imports than exports),
# 0 is even balance,
# and 1 is trade surplus (more exports than imports)
d.2015.balance <- d.2015.balance %>% mutate(surplus = sign(balance))

p <- ggplot(data = d.2015.balance,
  aes( x = Imports, y = Exports, fill = surplus)) +
  geom_point(shape = 21, size = 5) +
  stat_smooth(method = "lm", se = FALSE) +
  scale_x_continuous(limits = c(0,80000), labels = comma) +
  scale_y_continuous(limits = c(0,120000), labels = comma) +
  theme_solarized() +
  theme(legend.position = "none")

# annotation layer
p + annotate("text", x = 20000, y = 50000, label = "Trade surplus") +
    annotate("text", x = 50000, y = 2000, label = "Trade deficit") +
    annotate("text", x = 50000, y = 95000, label = "United States") +
    annotate("text", x = 66000, y = 45000, label = "Germany")


```

Data from the Office for National Statistics - [click to download (XLSX)](http://visual.ons.gov.uk/wp-content/uploads/2017/02/Imports-exports-1999-2015.xlsx).
