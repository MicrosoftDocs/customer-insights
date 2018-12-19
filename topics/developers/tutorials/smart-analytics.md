---
layout: page
title: Smart analytics
---

Aria's Smart Analytics feature sifts through large amounts of data, and finds trends, outliers, and possible causes for deviations. 
It will give you ideas on how to get started understanding your data,
including combinations that increased or decreased the most, and [automatically marked anomalies](/developers/deep-dives/series-transforms/#anomalies).

{% img "references/smartanalytics/lightbulb-sa.jpg" alt:"Smart analytics Lightbulb" class:"img-responsive" %} 
The Insights button (above) appears for charts on supported cubes in dashboards. It presents an auto-generated overlay of insights which are created by running [Series Transforms](/developers/deep-dives/series-transforms) on the cube measure underlying the chart. Smart analytics will highlight the insights you need to pay attention to in a section called 'Top Insights'. An animation of an example insights scenario is below.

{% img "references/smartanalytics/smartanalytics.gif" alt:"Smart analytics scenario" class:"img-responsive" %}

Each insight has controls below the description to allow you to quickly experiment with important parameters.

The visualization pane for the insight also has controls to switch between various visualization types and change the time period of the query. These controls do not currently update the description or title of the insight. The 'Show Original' toggle shows the original chart in context.

{% img "references/smartanalytics/viztoolbar-sa.jpg" alt:"Chart controls" class:"img-responsive" %}

Two actions are available in the title bar (image below) --  the save button allows you to save these insights to a dashboard, and the feedback button next to it allows you to send us feedback to improve the relevance of a particular insight.

{% img "references/smartanalytics/actions-sa.jpg" alt:"Actions" class:"img-responsive" %}

Upon saving an insight as a chart, the description of the insight is saved as the description of the chart. The description is not updated when the chart is refreshed.

The list of candidate insights presented by the smart analytics feature are outlined here, together with *when* they are presented and *how* they are computed. Insights which are candidates for top insights section are marked with a (#) and the description describes the evaluation metric.

Insights can take up to a minute to evaluate. The time it takes to evaluate insights is longer for percentile measures, queries which cover a long time interval, especially ones not aligned to day or hour boundaries.

## Outliers ##

*  #### Top high outlier  (#)
*  #### All high outliers
*  #### Top low outlier  (#)
*  #### All low outliers

The [Outliers transform](/developers/deep-dives/series-transforms/#outliers) is used to present this insight for percentile measures -- it highlights segments which are likelier to be a high or low outlier compared to the overall population in the query.

An outlier  threshold of 99th percentile (for high outliers) or 1st percentile (for low outliers) for the measure is used for this analysis; values above or below this threshold are considered outliers. The analysis ignores segments which do not meet a minimum support threshold (fraction of the overall population in the query) of 0.5% of the data in the query.

 Each result has two metrics --

  * support, which indicates what percentage of the population the segment represents
  * [risk ratio](https://en.wikipedia.org/wiki/Relative_risk), (example: 5X likelier) which indicates how much more likely the segment was to be an outlier.

Results are presented as top insights if they have a risk ratio of at least 1.5, which means they are at least 50% more likely to be an outlier.

Top outlier results can be ignored using the 'Ignore this outlier' button {% img "references/smartanalytics/ignore-sa.jpg" alt:"Ignore icon" class:"img-responsive" %} at the bottom of the insight pane. This changes the query to ignore the segment that was previously reported as the top outlier. The insight then shows the top outlier on this updated query.

## Comparison: dimension values ##

* #### Comparison: Value A vs Value B  (#)
* #### Comparison: Value A vs All   (#)

The [PopulationComparison transform](/developers/deep-dives/series-transforms/#populationcomparison) is used to present this insight for measures which have 'Count' or 'DistinctCount' operation.  The results highlight segments of the query which are relatively more likely compared to the selected dimension/value combination (target).

This insight appears when at least one dimension value is selected in the visualization as a 'Separate' filter. The selected dimension value is compared with all other values of that dimension.

If two dimension values are selected, we compare the two dimension values. When more than one dimension value is selected for a dimension, the insight control allows you to change the dimension/value selected as the comparison target.

The analysis ignores segments which do not meet a minimum support threshold (fraction of the overall population in the query) of 0.5% of the data in the query. The results are presented with two metrics --
  * support, which indicates what percentage of the population the segment represents
  * [risk ratio](https://en.wikipedia.org/wiki/Relative_risk), which indicates how much more likely the segment was in the target.

Results are presented as top insights if they have a minimum risk ratio of 1.5, which means that the target segments are at least 50% more common in the target.

## Anomalies ##

* #### Anomalies found (#)

The [Anomalies transform](/developers/deep-dives/series-transforms/#anomalies) is used to present this insight, for all types of measures. The insight is featured in the 'Top insights' category if it finds anomalies with a sensitivity threshold of at least 0.5. The sensitivity threshold can be tuned using the slider in the insight.

## Movers ##

* #### Top gainer (#)
* #### All gainers
* #### Top decliner (#)
* #### All decliners

The [Movers transform](/developers/deep-dives/series-transforms/#movers) is used to present this insight, for measures with a 'Count'  operation. The results are segments which either increased/decreased in count by at least 5% from the first part of the time window to the second part of the time window, or only appear in one part of the time window.

Result segments must also meet a minimum support threshold (fraction of the overall population represented by the segment) of 0.5%.

Each result is presented with two metrics --
* support,  which indicates what percentage of the population is represented by the segment
* percentage increase or decrease between the windows. New or disappearing segments are marked as well.

## Percent change from a prior time window ##
* #### Change from 1 week ago (#)
* #### Change from 1 month ago (#)

This insight is shown if we detect a high percentage delta for at least one time window from an appropriately selected prior time window.  It is generated by the [Delta transform](/developers/deep-dives/series-transforms/#delta)

## Distributions ##
* #### Top dimension values by dimension name

Customers often want to see a breakdown of the top dimension values for every measure -- this insight auto-generates a chart for every dimension in the cube that was not specified in the query as a filter. Results are presented in a pie chart for 'Count' or 'DistinctCount' operation or as a bar chart for other operations. The top 10 dimension values are shown for high cardinality dimensions, this can be changed in the insight control.

## Splits ##
* #### Splits for top dimension values over time

Customers often want to see a split over time of the top dimension values for every measure, this insight auto-generates a chart for every dimension in the cube that was not specified in the query as a filter. The chart is limited to the top 10 dimension values for high cardinality dimensions.

## Trend ##
* #### Week over week trend
* #### Month over month trend

The [Comparison transform](/developers/deep-dives/series-transforms/#comparison) is used to present this insight. For all measure types and operations, we overlay data from an appropriate prior window so you can visually see the comparision from a prior week or month.

## Rolling average ##

This insight is shown if we detect at least one series was automatically smoothed by the [Rolling Average](/developers/deep-dives/series-transforms/#rollingaverage) transform.
