---
uid: developers/tutorials/metrics-apply-transforms
title: Apply transforms 
author: ruthaisabokhae
description: Apply transforms 
ms.author: ruthai
ms.date: 05/09/2019
ms.service: product-insights
ms.topic: conceptual
---

# Apply transforms 

When exploring data, you can apply various transforms to your data for further insight. These are found above the data visualization pane. 

![Applying a transform](media/ApplyTransforms.png)

TK: -- Add as the transforms become available 

Working out rolling averages, deltas, and other such common operations are extremely easy to add to your chart using the transform feature. Currently we support the following operations:

## Absolute value

Calculates absolute value of each data point in each series.

## Anomalies
Finds and marks anomalies in the time series (values that deviate from expected values based on historical patterns).

**Note** Health alerts based on anomaly detection coming soon. 

Parameters:
- Sensitivity - Represents how much evaluated data point has to deviate from expected value to be considered anomalous. High sensitivity means even small deviations are marked as anomalies. Low sensitivity marks only largest deviations.
- Direction - Specifies whether to mark only anomalies where value is higher than expected (Up), only lower than expected (Down) or both.

## Clipping

The clipping transform "clips" the time series at configurable, optional, maximum and minimum limits. If both limits are present then top limit must be greater than the bottom limit. At least one limit must be specified.

Parameters:
-Top limit - this is an optional maximum limit to clip the value at (this means all values exceeding this limit are replaced with this limit)
-Bottom limit - this is an optional minimum limit to clip the value at (this means all values less than this limit are replaced with this limit)

## Comparison

Returns original series and specified number of series shifted by specified period for comparison (e.g. current week and last 2 weeks).

Parameters:
Period - Period of time to shift back for comparison transform.
Possible values:
	- Hour over hour
	- Day over day
	- Week over week
	- Month over month
- Number of periods - Number of shift periods to move back. Each shift produces a series with data shifted by a period. Possible values: 1-6, default: 1.

Example: day over day comparison with last 2 days.

## Cumulative Sum

Calculates cumulative sum resetting to 0 at specified interval. Weeks reset on Monday 12am.

Parameters:
- Reset period - Specifies how often to reset the summation for cumulative sum.

Example: Cumulative sum of metrics with weekly reset.

## Delta

For each data point, calculates difference with another data point shifted back by specified period (e.g. previous data point, yesterday, last week).

Parameters:
- From -  Represents how far back to calculate the delta with.
Possible values:
	- Previous data point
	- 1 hour ago
	- 1 day ago
	- 1 week ago
	- 2 weeks ago
	- 3 weeks ago
	- 4 weeks ago
	- 8 weeks ago
	- 12 weeks ago
	- 1 quarter ago (13 weeks)
	- 2 quarters ago (26 weeks)
	- 1 year ago (52 weeks)

Example: change in metric from last week.

## Dimension aggregation

Aggregates series for all combinations of specified dimensions using specified aggregation operator.

Parameters:
- Operation -  Operation to perform to aggregate selected dimensions.
Possible values:
	- Average
	- Max
	- Min
	- P01
	- P05
	- P50
	- P95
	- P99
	- StDev
	- Sum
	- Variance
- Dimensions - dimensions to aggregate for.

Example: Dimension aggregation calculated for each metric aggregating 2 dimensions, Version and Network, using Max as aggregation operator.

## Exponent

The series becomes the exponent which the base is raised to.

Parameters:
-Base - this is the base that is raised to an exponent, for example: if the base were 2, a value of 3 would be transformed to 8

## Exponential Rolling Average

Smooths the time series by way of exponential moving average. This smoothing technique weights previous values in an exponentially decaying manner.

Parameters:
-Alpha - the degree of weighting decrease, a constant smoothing factor between 0 and 1, a higher alpha discounts older observations faster

## Gating

The time series is converted to a binary series whereby a value of 1 indicates that all gate conditions are satisfied, a value of 0 indicates that a gate has been crossed. At least one gate must be specified.

Parameters:
-Top gate - this is an optional maximum value to limit the time series to, if this value is exceeded then a value of 0 is returned (otherwise 1 is returned)
-Bottom gate - this is an optional minimum value to limit the time series to, if a value is less than this value then a 0 is returned (otherwise 1 is returned)

## Interpolate NaNs

Interpolates / replaces NaN values in a time series

Parameters:
- Method -
Represents how to interpolate / replace NaN values in the series.
Possible values:
	- Linearly interpolate - interpolates values as a straight line that connects to values that are present at the ends of the interval comprised of NaNs
	- Replace with 0 - replaces all NaN values with 0

## Logarithm

Every point in the series is evaluated as a logarithm.

Parameters:
- Base
This is the base of the logarithm that is taken for every point in the series, for example: if the base were 2, a value of 8 would be transformed to 3

## Movers

Identify segments which moved (changed its Count) significantly between the first half of the time window and the second half of the time window. Only segments which have a  minimum support threshold (fraction  of the overall population represented by the segment) of 0.5% of the query are shown. 

The results indicate relative increases between the two halves of the time window, so it might pick a *decreasing combination* as an *increaser* or vice versa, if the overall population decreased a lot more than the decreasing combination. 

Each segment result includes *percentage increase or decrease* between the half windows. New or disappearing segments are marked as well. 

In cases where the time window is not an even multiple of the granularity of the chart, we extend it into the past by one time window so the time windows are of equal size.

Parameters:
- Direction
This is either Increasers for increasing combinations or Decreasers for decreasing combinations.

## Outliers

Identify segments within the query which are more likely to have high or low outliers compared to the overall population in the current query. The analysis ignores segments which do not meet a minimum support threshold (fraction of the overall population in the query) of 0.5% of the data in the query. The results are presented with two metrics -- 
 *support*, which indicates what percentage of the population the segment represents
  *risk ratio*, which indicates how much more likely the segment was to be an outlier.  

Parameters:
- High outliers

High outliers picks an outlier threshold of 99th percentile of the measure and finds segments which are much more likely to be high outliers compared to the overall population in the current query. 

- Low outliers

Low outliers picks an outlier threshold of the 1st percentile of the measure and finds segments which are  more likely to be low outliers compared to the overall population in the current query.

## PopulationComparison

Given a dimension name and a value (target) which are included in the current query, find segments which are relatively more likely in the target population compared to the overall population in current query. The target dimension must be selected in the filters section of the query as a 'Separate' dimension with at least one additional value beside the target dimension value. The values selected for the dimension in the filter identify the overall population for comparison.


Example - For a cube with Country and AppVersion, comparing Country = UK vs Country = USA might tell you what application versions are more likely in UK over (UK, USA).

The analysis ignores segments which do not meet a minimum support threshold (fraction of the overall population in the query) of 0.5% of the data in the query. The results are presented with two metrics -- 
 *support*, which indicates what percentage of the population the segment represents
  *[risk ratio](https://en.wikipedia.org/wiki/Relative_risk)*, which indicates how much more likely the segment was in the target.  

Parameters:
- Target - A predicate identifying a target population in the query
	- fieldName - Dimension name
	- operator - Operator for comparison
	- value - Value of dimension name

## Power

Every point in the series is raised to a power.

Parameters:
-Power - this is the power that every point in the series is raised to, for example: a power of 2 would transform 10 to 100 (it would square it)

## Rate normalization

Converts each data point into a value per specified rate.

Parameters:
- Rate -  Represents time grain to normalize into.
Possible values:
	- One millisecond
	- One second
	- One minute
	- Five minutes
	- One hour
	- One day
	- One week

Example: Rate normalization of metrics to "per 1 hour" rate.

## RollingAverage

Calculates rolling average on specified window size (in grains) or finds optimal window size for rolling average automatically (to reduce local outliers) and calculates rolling average on this window.

Parameters:
- Is automatic - Indicates whether to find optimal window size automatically.
- Number of points - Specifies size of window in points to use for the rolling average (if not using automatic window size).

Example: rolling average with automatically computed window size of 42.

## Rolling Median

Calculates rolling median on specified window size (in grains).

Parameters:
- Number of points - Specifies size of window in points to use for the rolling median.

## Root

The root of every point in the series (this can also be understood as raising every point to the 1/root power).

Parameters:
-Root - this is the root that is take, for example: a value of 2 would indicate a square root, this means 4 would be transformed to 2 on the y-axis

## Scale

Multiplies value of each data point in each series by a constant.

Parameters:
- Scalar - Constant to multiply value of each data point in each series.

Example: scaling metrics by 1/1000000.

## Series ordering

Calculates top series aggregated using specified operation on specified interval and ordered either ascending or descending, up to specified limit.

Parameters:
- Operation -  Operation by which to aggregate and sort.
Possible values:
	- Average
	- Max
	- Min
	- P01
	- P05
	- P50
	- P95
	- P99
	- StDev
	- Sum
	- Variance
- Sort - Sorting order of the series.
Possible values:
	- Ascending
	- Descending
- Limit - Limit of series to return. 1-50, default limit is 50.

Example: Series sorted by max metric value.

## Shift

Shifts the series vertically on the y-axis by a constant value.

Parameters:
-Value - this is the amount that the series is shifted, for example: a value of -100 would shift a value in the series of 120 to 20 on the y-axis

## Time aggregation

Aggregates data points from a specified source grain (no greater than chart grain) using specified aggregation operator.

Parameters:
- Operation -  Operation to perform to aggregate data points into selected query grain.
Possible values:
	- Average
	- Max
	- Min
	- P01
	- P05
	- P50
	- P95
	- P99
	- StDev
	- Sum
	- Variance
- Source grain - Grain to aggregate data points from by using selected aggregation operation.

Example: Time aggregation calculating Min 5 minute window in each 1h grain.

