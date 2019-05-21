---
uid: developers/tutorials/metrics-apply-transforms
title: Apply transforms 
author: hakrou
description: Apply transforms 
ms.author: hakrou
ms.date: 05/09/2019
ms.service: product-insights
ms.topic: conceptual
---

# Apply transforms 

When exploring data, you can apply various transforms to your data for further insight. These are found above the data visualization pane. 

TK: -- Add as the transforms become available 

Working out rolling averages, deltas, and other such common operations are extremely easy to add to your chart using the transform feature. Currently we support the following operations:

* **Delta**: display delta or delta of deltas
* **Comparison**: compare with previous time windows (for example, week over week)
* **Rolling Average**: smooth a line by computing its rolling average
* **Absolute Value**: show absolute values, instead of actual values
* **Cumulative Sum**: cumulative sum for every series
* **Dimension Aggregation**: aggregate by dimension
* **Time Aggregation**: aggregate by time
* **Rate Normalization**: divide to get a number per second, minute, or hour
* **Scale**: multiply a number
* **Series Ordering**: order a series
* **Clipping**: remove outliers by setting upper and lower bounds
* **Gating**: convert values to binary. Linear values can be converted to `1` and `0`.
* **Power/root**: square a value, cube a value, or get a root of the value
* **Log/exponent**: get a log of the value or use the value as an exponent for base x
* **NaN interpolation**: let Aria interpolate missing values
* **Shift**: move values up and down the Y axis
* **Rolling median**: addition to an existing rolling average
* **Exponential rolling average**: give more weight to the latest data and react faster to recent changes; this is the preferred smoothing transform

## Detailed explanations of the transforms

### Comparison

Comparing the number of items such as calls to a previous period is often the first transform to try. Select a comparison, then choose which period you will compare it to. You can select the number of days or weeks. The graph will update with another series from the time period of your choice.

### Delta

With two graphs overlaid, it may not be clear what the difference in volume is. You can choose to chart the delta (difference) between two series with the delta transform. You will only see the difference between the original two series. For example, if calls are 30 today but were 40 last week, you'll see -10.

### Absolute value

If you're looking at the magnitude or variability of call volume, you can apply the absolute value transform on top of the delta transform. This removes the negative signs. If calls were 30 today but 40 last week, 10 will be plotted. If it was 40 today but 30 last week, it will also be 10.

### Cumulative sum

Calculating total calls for the week or for the whole month is easy with cumulative sum transform. You can choose to aggregate daily values for a weekly reset for a weekly (or monthly) call volume. You can also add a comparison transform, to see if you have a higher number of total calls compared to last week.

### Rolling average

Some signals are noisy. To reduce fluctuations and noise, you can use rolling averages to smooth out variability and outliers. It also makes trends much easier to spot. Choose automatic time grain to let the system find the optimal window size.

### Scale

If your units are large and cause the axis to look cluttered, you can use the scale option to reduce the numbers. Values in the millions can be reduced to single digits by multiplying the x axis values by 0.00001.

### Series ordering

If you have selected multiple series, perhaps with multiple dimensions, you can order the series. For example, you can select the top five regions where call volume varies the most, and then toggle the top or bottom N with the toggle switch.

### Rate normalization

You know what the total calls are per hour, or per five minute bucket, which is usually the default time grain. So if you get 5000 calls per day, how many calls is that per minute? You can have a chart that tracks the minute rate with rate normalization. This is useful for scenarios such as failures per second for each hour, requests per second made for the day, and so on.

### Dimension aggregation

Say you have selected all data from all regions in Europe and all manufacturers. Now you want to aggregate further. Choose `manufacturer`, and you can get maximum call volume per region. You used the `manufacturer` dimension to aggregate, or "squash" together, so that now you only see regions.

Another example. You select exam score data for students from all countries and universities. Choose countries to aggregate to get an average, and you will get the average score per university. The average has been calculated per country. If you choose to aggregate by both dimensions, you will get the average score for all selected students.

### Time aggregation

By default, we store measures per five minute bucket. In an hour, you'd have 12 such values. If you choose to time-aggregate by 1 hour, you will select minimum, maximum, average, and so on from these values. So with an average, you'd get the average of the 12 values. With mininum, you'd get the number of calls recorded during the slowest time of that hour. Using the same example, you could pick the slowest, or the busiest number recorded per hour for that day. In a call center, that could help you decide the minimum number of people to handle calls to minimize the waiting period.

Please refer to [the transforms reference](/developers/deep-dives/series-transforms) for a complete list.
Additional transforms are discussed [on the Aria blog](/2018/02/28/maths-transforms/).

