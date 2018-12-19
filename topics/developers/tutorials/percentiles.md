---
layout: page
title: Percentiles

---

{% assign howtoLink="/developers/how-to" %}
{% assign articlesLink="/developers/articles" %}

* [Limitations]({{ howtoLink }}/percentiles#limitations)
* [Algorithm]({{ howtoLink }}/percentiles#algorithm)
* [Help]({{ howtoLink }}/percentiles#help)

## How it works

The following video explains how Aria uses percentiles. 

{% include video.html src="Percentiles.mp4" %}
Screenshots in this video are from the old portal. 

We now have custom percentiles which support _all_ percentiles. Simply enter the percentile you want (in whole numbers). 

{% include video.html src="CustomPercentiles.mp4" %}

## Limitations

Calculating and merging percentiles is two orders of magnitude more expensive than the next heavier operation (distinct count). For this reason, specific guards are in place to ensure cubes created with percentiles can be served without any degradation in performance.

### Cardinality limits

Cubes with percentiles enabled are allowed a maximum cardinality of **1,000 per day**. If at any time the cube breaches this threshold, it will be stopped and further data will be disregarded. Existing data collected by the cube up to that point will still be available for querying. _Once the cube reaches such a state, it is not recoverable and a new cube must be created, so please design cubes carefully._ To help spot such cases on time, email alerts will be sent once a cube is close to the allowed cardinality. Should the cube stop due to cardinality limits, another email alert will be sent to the project's notification alias.

Here are a number of useful links:

* [How cubes work]({{ articlesLink }}/real-time-cubes)
* [Cube design tips]({{ articlesLink }}/cube-design-tips)
* [Cube performance tips]({{ articlesLink }}/cube-performance-tips)

### Cube eligibilty

Percentiles can only be added when cloning existing cubes. This is to provide a safety net in case the percentile cube goes above the allowed daily threshold and as a result stops processing data.

The original cube must belong to the project and listen only to events belonging to the project in question.

### Cubes with percentiles enabled

A cube that has had percentiles enabled following the above procedure can be edited like any other normal cube, with the exception that it's not possible to remove (or add) percentiles from a measure. If another measure needs to be added to the cube, a new clone needs to be created.

### Query performance

At the moment, Aria's worst case, querying a cube at full 1K cardinality every 5 minutes on a high volume event, would take around 200 ms per time bucket requested, so the longer the time range requested, the longer the querying time.

In order to get the best experience, it's suggested you take the following steps.

1. Reduce the time range queried to the minimum required. 4 days @ 5 minutes might for the time being result in a query timeout in the worst case.
2. Set your tenant's time zone setting to UTC in order to enjoy the benefits of daily preaggregation.
3. Be as specific as possible in your queries. Queries where constraints for most of the dimensions are specified will perform best as they will require the minimum number of aggregations at querying time.

### Cube cardinality information

While carefully designing a cube is important in any case, for percentiles containing the cardinality of a cube it's of paramount importance. To help get a sense of the cardinality of a cube, we display the maximum cardinality seen in the last two days in the **Settings/Edit** page, together with a cardinality trend indicator.

## Backing Algorithm

In order to calculate an exact percentile on a data set, all samples for the interval in question should be retrieved and sorted. This is not a practical solution for large and streaming data sets. For this reason, Aria is using a data structure called T-Digest that enables space-bounding the problem at the price of accuracy. Extreme percentiles (for example, p95 onwards) are the least error-prone. The median, p50, is the percentile most commonly affected by errors. The error rate also depends on the input data set, but it is usually <2% at p50. More information can be found in the [T-Digest Paper](https://github.com/tdunning/t-digest/blob/master/docs/t-digest-paper/histo.pdf).

## Help

For any feedback or queries about percentiles, or what to do when a cube has been stopped due cardinality limits, please contact our alias [ariaconnect](mailto:ariaconnect@microsoft.com)
