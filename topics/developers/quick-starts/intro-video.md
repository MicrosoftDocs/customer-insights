---
layout: page
title: Introduction to Aria
sub_title: Set up your data pipeline and dashboards straight away

---

Aria enables you to instrument your app or service, send telemetry data, process it, and then visualize it in real-time. You can create a dashboard, drill into metrics using multi-dimensional cubes, and inspect your raw telemetry events.

**This topic covers the following tasks**

1. [Navigating and finding your project](#1-navigating-and-finding-your-project)
1. [Visualizing your data in charts](#2-visualizing-your-data-in-charts)
1. [Inspecting raw telemetry events](#3-inspecting-raw-telemetry-events)
1. [Creating a real-time aggregate cube](#4-creating-a-real-time-aggregate-cube)

---

**The contents of this topic is also available in the following video**

{% include video.html src="AriaWalkthrough.mp4" %}

## 1. Navigating and finding your project

If you want try it out yourself, visit the Explorer section of [the Portal]({{ site.portal_url }}/welcome-screen). If you have already sent data for a project, you can select that project. Here, you can select the **Aria calling app sample**.

{% img "tutorial/choose-project.png" alt:"Find your project" class:"img-responsive" %}

In the Explorer menu, you can see all of the resources that belong to this project. Resources can be dashboards, or any other operation that you are performing on your data.

{% img "tutorial/Applications.png" alt:"See all resources" class:"img-responsive" %}

## 2. Visualizing your data in charts

A dashboard is a collection of visualizations (charts). You can customize each visualization (which we will cover later). To see how visualizations are powered, you can look into the actual streaming events.

{% img "tutorial/Dashboard.png" alt:"Dashboard" class:"img-responsive" %}

## 3. Inspecting raw telemetry events

You have downloaded the SDK and sent data. To verify this, you can use Event Explorer to view incoming events. You can select the event at the top, wait for sample events, and click on an event to see what type of data it contains.

{% img "tutorial/event-inspector.png" alt:"Event Explorer" class:"img-responsive" %}

## 4. Creating a real-time aggregate cube

Based on the telemetry you send, you can now create a *cube*. In Aria, a cube is a data processing configuration for processing (aggregating) your streaming data in real-time. For example, you can measure the average latency of all of the latency values, and this value can be broken-down (split) into dimensions. For example, this could give you the average latency *per platform* (a dimension). Therefore, you can get the average latency of Android devices that are connected using Wi-Fi.

{% img "tutorial/cube-editing.png" alt:"Edit cube" class:"img-responsive" %}

The arithmetic operations, counts, and other such aggregations that you define are calculated, then separately stored. This means that you must define a measure for a cube (such as a count), before you can use it in a visualization.

Each cube has *measures*, which produce numeric values. Dimensions (also known as splits) that you create, are categories into which your measures are assigned. In the example, you use a property called *DurationInMinutes*, that is split by *Platform*. You can then create a visualisation with this cube. Create a new dashboard if you want, choose a layout, and then create a graph. Click on **New Layer** > **Cube Query**, then select the measure you created - *latency*, and then choose dimensions - *platform*.

{% img "tutorial/new-visualisation.png" alt:"Create Viz" class:"img-responsive" %}

You can choose from charting options such as pie charts, bar charts, stacked charts etc.

{% img "tutorial/chart-types.png" alt:"Chart types" class:"img-responsive" %}

You can either get separate values per dimension with 'split', or you can use *merged*, which will produce a one-time series for all data that matches the values here. So not merged, separate values for each dimensions, and only one if merged.

{% img "tutorial/merged-values.png" alt:"Merged values" class:"img-responsive" %}

If you use this grouping often - platforms and manufacturers for specific values, then you can create a *segment*. You can resuse this later to select the same data subset. Segments are useful if you reuse your dimension selection often, so for example, you could select 10 different countries for "Western Europe" values - then you perform the merge option, and then save it as a segment.

{% img "tutorial/Segment.png" alt:"Segment" class:"img-responsive" %}

You can customize other parts of the graph as well - tick label format for example. You can also set the minimum and maximum to adjust the display. Of course you can also change properties such as name and description.

{% img "tutorial/axis-options.png" alt:"Axis Options" class:"img-responsive" %}

So let's revise. You download our SDK, and begin sending telemetry data. You can check the incoming events in Event Explorer. You can then create a cube that defines aggregation operations to be performed on the incoming data. Then, using the aggregated data, you can create visualisations, and add them to dashboards.
