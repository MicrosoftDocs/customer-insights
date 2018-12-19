---
layout: page
title: Analyze metrics using real-time cubes

---

You can transform your events into metrics using Aria real-time cubes.
Suppose you develop a calling app that logs the following event upon the completion of a call.

Timestamp     | Event                         | Platform         | Locale          | Duration
--------------|-------------------------------|------------------|-----------------|----------------
5:06:12       | aria_sample_call_completion   | Android          | en-US           | 20
5:06:54       | aria_sample_call_completion   | Android          | en-US           | 80
5:07:10       | aria_sample_call_completion   | Windows          | en-UK           | 100
5:07:48       | aria_sample_call_completion   | Windows          | en-UK           | 200
5:08:01       | aria_sample_call_completion   | Android          | es-MX           | 35
5:09:25       | aria_sample_call_completion   | Android          | zh-CN           | 75
{: .table .table-striped}

You can create a cube where Count(Event), Avg(Duration), and Max(Duration) are measures and Platform and Locale are dimensions. The real-time cube would produce such metrics for each 5-minute grain (default):

Grain               | Platform         | Locale          | Count(Event)   | Avg(Duration)  | Max(Duration)
--------------------|------------------|-----------------|----------------|----------------|----------------
5:05:00 - 5:09:59   | Android          | en-US           | 2              | 50             | 80
5:05:00 - 5:09:59   | Android          | es-MX           | 1              | 35             | 35
5:05:00 - 5:09:59   | Android          | zh-CN           | 1              | 75             | 75
5:05:00 - 5:09:59   | Windows          | en-UK           | 2              | 150            | 200
5:05:00 - 5:09:59   | iOS              | en-US           | 0              | –              | –
{: .table .table-striped}

The grains can be further aggregated into 1-hour, 1-day, and 1-week granularity.

The Real-Time Aggregation (RTA) engine computes these cubes in near real-time at tremendous scale as events arrive. You can create multiple cubes so you can analyze different metrics and dimensions.

This tutorial will use the [Aria Calling App sample][21]. This sample sends an app\_sample\_call\_completion event with these properties:

{% highlight shell %}
2015-07-11 05:53:28Z: [aria_sample_call_completion] - DurationInMinutes: 34, UserRating: 2, Platform: Android, Manufacturer: Samsung, Locale: hi-IN, Version: 1.3
{% endhighlight %}

## 1. Create a cube

Check [here](../create-a-cube) on how to create a cube.

Event Names: app\_sample\_call_completion

Measures

Measure          | Units          | Property             | Description                     | Distinct Count
-----------------|----------------|----------------------|---------------------------------|---------------------
Calls            | Calls          | [Event count]        | Number of calls                 | No
Duration         | Minutes        | DurationInMinutes    | Duration of calls in minutes    | No
{: .table .table-striped}

Dimensions

Dimension        | Property
-----------------|---------------------------------
Platform         | Platform
Locale           | Locale
{: .table .table-striped}

The configured cube can be seen [here]({{ site.portal_url }}/cube/7a206f3f78074c078df75cbafe09caf4/settings)

{% img "getting-started/analyze-metrics/CubeConfig.png" alt:"Cube Config 1" class:"img-responsive" %}

## 2. Send events

Run the [Aria Calling App sample simulator][20] with this command to back-populate 24 hours of data and continue to send events in real time once it finishes back-population:

{% highlight shell %}
CallingAppSimulator.exe /token:<your-token> /backpop:24
{% endhighlight %}

[20]: /developers/downloads/calling-app-simulator

Aria computes the aggregates in the real-time cube as events arrive. A newly created cube starts processing the selected events in the pipeline immediately upon creation. It does not process previously sent events.

## 3. Do multi-dimensional analysis

Launch the Time Series Analytics app from the taskbar. Select your cube and select at least one measure. Select values in one or more dimensions to split the measures by those combinations, a tuple of the selected dimensions. It takes a few minutes for your events to become visible in the Time Series app.

This screenshot illustrates counting the number of calls split by the tuple (platform, locale):

{% img "take-a-tour_active-users-by-platform.png" alt:"Time-series screenshot" class:"img-responsive" %}

## Note about service limits

The RTA engine limits the dimensional cardinality of each cube to 100,000 combinations in a five-minute window to prevent a user with an errant cube from impacting others. It will throttle cubes with high cardinality (e.g., a cube with a dimension with millions of unique GUIDs) and notify their tenant owner of the throttling.

If you need to pivot by many dimensions, we encourage to split them across separate cubes, grouping the dimensions that you will typically need to pivot together in one cube.

The RTA architecture supports a cardinality in the low millions so we expect to raise this service limit in the future.

## Congratulations!

You have created charts and metrics from a multi-dimensional cube. Next, learn to create your own dashboards.

[Learn to create dashboards](../create-dashboards)
