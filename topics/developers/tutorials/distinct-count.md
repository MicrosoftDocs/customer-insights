---
layout: page
title: Distinct count operations

---

{% assign howtoLink="/developers/how-to" %}
{% assign articlesLink="/developers/articles" %}

* [Options]({{howtoLink}}/distinct-count#options)
* [Limitations]({{howtoLink}}/distinct-count#limitations)
* [Algorithm]({{howtoLink}}/distinct-count#algorithm)
* [Accuracy]({{howtoLink}}/distinct-count#accuracy)
* [Further reading]({{howtoLink}}/distinct-count#further-reading)
* [Help]({{howtoLink}}/distinct-count#help)

## Options

Aria exposes two ways of computing distinct count:

- Fast, but imprecise ([HyperLogLog with 512B sketch]({{howtoLink}}/distinct-count#algorithm))
- Accurate, but slower ([HyperLogLog with 16KB sketch]({{howtoLink}}/distinct-count#algorithm))

## Limitations

Calculating `FastDistinctCount` is an order of magnitude more expensive than `Count` or arithmetic operations. Currently, Aria doesn't enforce cardinality limits for this operation, but it’s likely to be enabled in the near future.

`AccurateDistinctCount` is four times slower than the percentiles operation. For this reason, it has guards in place to ensure that cubes created with it can be served without performance degradation.

### Cardinality limits

Cubes with `AccurateDistinctCount` enabled are allowed a maximum cardinality of __250__ per day. If at any time the cube breaches this threshold, it will be stopped and further data will be disregarded. Existing data collected by the cube up to that point will still be available for querying. Once the cube reaches such a state, it is not recoverable and a new cube has to be created, so please design cubes carefully.

To help spot such cases in time, email alerts will be sent once a cube is close to the allowed cardinality. Should the cube stop due to cardinality limits, another email alert will be sent to the tenant's notification alias.

We don’t enforce limits for `FastDistinctCount`, but we suggest to keep cubes below a cardinality of 10,000 per day. Here are a number of useful links that will be of help:

- [How cubes work]({{articlesLink}}/real-time-cubes)
- [Cube design tips]({{articlesLink}}/cube-design-tips)
- [Cube performance tips]({{articlesLink}}/cube-performance-tips)

### Cube eligibilty

`AccurateDistinctCount` can _only_ be added when cloning existing cubes. This provides a safety net in case the cloned cube goes above the allowed daily threshold and as a result stops processing data.

The original cube must belong to the tenant and listen only to events belonging to the tenant in question.

### Cubes with AccurateDistinctCount enabled

A cube that has `AccurateDistinctCount` enabled following the above procedure can be edited like any other normal cube, with the exception that it's not possible to remove `AccurateDistinctCount` from a measure, or to add it. If another measure needs to be added to the cube, a new clone needs to be created.

### Cube cardinality information

While carefully designing a cube is always important, for `AccurateDistinctCount` containing the cardinality of a cube it is of paramount importance. To help getting a sense of the cardinality of a cube, we display the maximum cardinality seen in the last two days in the settings/edit page, together with a cardinality trend indicator.

## Algorithm

Aria uses the `HyperLogLog` algorithm for estimating the number of distinct values of a property.
The following video explains how Aria uses `HyperLogLog`:

{% include video.html src="HyperLogLog.mp4" %}

In short:

1.	Given a good hashing function, we change input data sets into evenly distributed, pseudorandom values.

2.	Next, we split the hash into two parts. The split point decides about accuracy, the prefix decides about the bucket and number of leading zeros, and the suffix decides about the value.

3.	For all input data, we keep track of the maximum value per bucket.

4.	For a single bucket, we hit a sequence with `k` zero bits once in every 2<sup>k</sup> elements. It is possible to provide a formula for a specified state of buckets, which estimates the most probable number of input elements that evaluates to that state. This is our result estimate.

If you are not familiar with the `HyperLogLog` algorithm, we recommend [Nick’s blog entry](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation) for a more detailed explanation. As well as [the paper](http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf) that contains all details and mathematics behind the algorithm. We also suggest further readings from [Google Research](https://research.google.com/pubs/pub40671.html) that show how to use HLL with 64-bit hash functions.

## Accuracy

The number of buckets or registers (also called "sketch size") used for collecting `HyperLogLog` decides about its accuracy. In Aria Real-Time Cubes, we use the following sketch sizes.

1. For `FastDistinctCount`: A 512 byte sketch size with an average estimation error of around 5%. It was chosen as a tradeoff between accuracy and performance. Such a relatively small sketch size allows us to offer real-time `DistinctCount` aggregations in cubes with up to 10,000 dimensional cardinalities. Keep in mind that, before compression, such cubes will occupy 5MB space per 5-minute window and 1.5GB for a day.

2. For `AccurateDistinctCount`: A 16KB sketch size (same as in Kusto) with an average estimation error of around 0.8%. It provides high accuracy at the cost of performance. It requires us to introduce a 250 cardinality limit per cube to perform comparably to fast cubes. Limits for this operation type are enforced.

{% if site.internal %}
As a comparison, Kusto also uses `HyperLogLog` and provides three levels of accuracy (specified as a parameter for the `dcount` operator): 0, with a 4KB sketch and 1.6% error; 1, with a 16KB sketch and 0.8% error; and 2, with a 64KB sketch and 0.4% error. Please be aware that results you can get from Kusto are much more accurate than results from RTA at this moment. We therefore suggest using the [Kusto cron feature](/developer/how-to/kusto-cubes) if the current error level of RTA is too high for your use case.
{% endif %}

Last but not least, the declared accuracy is the average error rate you can expect. As is the case with most probabilistic algorithms, `HyperLogLog` is known to have high variances in results. The following charts show the typical behavior of HLL for datasets of 400, 6,000 and 100,000 elements in RTA cubes. Our input data is a set of n-GUIDs in every 5 minute time bucket.

{% img "distinctcount/distinctcount1.png" alt:"Distinct Count #1" class:"img-responsive" %}

---

{% img "distinctcount/distinctcount2.png" alt:"Distinct Count #2" class:"img-responsive" %}

---

{% img "distinctcount/distinctcount3.png" alt:"Distinct Count #3" class:"img-responsive" %}

---

{% img "distinctcount/distinctcount4.png" alt:"Distinct Count #4" class:"img-responsive" %}

## Further Reading

* [How Real-Time Cubes work]({{articlesLink}}/real-time-cubes)
* [Cube design tips]({{articlesLink}}/cube-design-tips)

## Help

For any feedback or queries about percentiles, or what to do when a cube has been stopped due to cardinality limits, please contact our alias [ariaconnect](mailto:ariaconnect@microsoft.com)
