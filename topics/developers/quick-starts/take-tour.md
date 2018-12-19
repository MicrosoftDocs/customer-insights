---
layout: page
title: Take a tour of Aria
sub_title: Discover what Aria can do

---

Aria enables you to instrument you app or service, process the telemetry data, monitor it, and visualize it in real-time. You can create dashboards, drill into metrics using multi-dimensional cubes, and inspect your raw telemetry events.

**Aria's key features**

* [Dashboards](#dashboards)
* [Time-series analytics](#time-series-analytics)
* [Real-time cubes](#real-time-cubes)
* [Event inspection](#event-inspection)
* [Compliance and privacy](#compliance-and-privacy)
* [Ease of use](#ease-of-use)
* [Scale and reliability](#scale-and-reliability)

## Dashboards

Create dashboards that bring your metrics together on a single screen. Double-click on a chart to drill into its real-time cube, and pivot the data further. You can adjust the columns, change the time range, and add new tabs and charts.

*Dashboards refresh automatically since Aria is a real-time data platform.*

{% img "take-a-tour_dashboard.png" alt:"Dashboard screenshot" class:"img-responsive" %}

You can see sample dashboards by visiting our [Sample gallery]({{ site.portal_url }}/sample-gallery).

{% img "take-a-tour-sample-gallery.png" alt:"Sample Gallery" class:"img-responsive" %}

## Time-series analytics

Visualize and analyze your telemetry events as metrics over time. Graph the count of events, or graph the average of the values in a specific event property. Split the metrics across one or more dimensions (which map to event properties). The screenshot below shows a pivot of the number of calls by platform type.

See for yourself. Select **Visualize a metric** from the [Sample gallery]({{ site.portal_url }}/sample-gallery).

{% img "take-a-tour_active-users-by-platform.png" alt:"Time-series screenshot" class:"img-responsive" %}

## Real-time cubes

The Real-Time Aggregation (RTA) engine in Aria powers the time-series analytics. The RTA computes a multi-dimensional cube on the telemetry streams in near real-time&mdash;at tremendous scale (10 million+ events per second). RTA enables you to analyze your metrics, split across multiple dimensions (as shown below).

{% img "take-a-tour_new-visualisation.png" alt:"Time-series second screenshot" class:"img-responsive" %}

You create and configure real-time cubes in the Aria Management Portal. You select the events to process, and then choose the event properties to use as measures and dimensions. As soon as you create your cube, Aria will begin computing the cube as the selected events arrive from your app or service.

{% img "take-a-tour-cube-editing.png" alt:"Cube configuration screenshot" class:"img-responsive" %}

Take a look at the real-time cubes in the Aria Calling App sample:

[Calling Metrics][20]{: target="_blank" }
: Computes call volume and duration, split by platform, network type, and device.

[Client statistics][21]{: target="_blank" }
: Computes the distinct count on User ID, split by platform, locale, and app version.

[20]: {{ site.portal_url }}/cube/7a206f3f78074c078df75cbafe09caf4/settings
[21]: {{ site.portal_url }}/cube/c3e7d54d1e3245fc8350f4a51e8ab8e8/settings

## Event inspection

Inspect samples of your raw telemetry in real-time as they flow through the Aria data pipeline. Debug your instrumentation and your real-time cubes using this tool.

Browse the events of the Aria Calling App sample using the [Event Explorer][22].

{% img "take-a-tour_event-inspector.png" alt:"Event Explorer screenshot" class:"img-responsive" %}

[22]: {{ site.portal_url }}/event-inspector?projectId=bac7b6a05f514c49a71e4f4f84364572&event=aria_funnel_step

## Compliance and privacy

Tag your event properties for automatic Personal Identifiable Information (PII) scrubbing by the Aria Collector, ensuring that sensitive data is safe as it flows through the pipeline.

The following screenshot shows **NetworkId** and **UserId** with scrubbed values.

{% img "take-a-tour_pii.png" alt:"PII Scrub" class:"img-responsive" %}

## Ease of use

Our mission is to empower you to build great products using data-driven insight in real-time. We believe in delivering self-service with ease of use. We built Aria as a self-serve, multi-project platform so you can independently manage your projects and data.

Please [send us your feedback][40] to help us improve Aria.

[40]: /help/community/

## Scale and reliability

Aria is Microsoft's next-generation real-time data platform. It has been in production since March 2013, and it has been handling a scale of 10 M+ events per second from 800 M+ devices since June 2014. We are committed to delivering enterprise-class quality to our users.

## Do you want to get started with using Aria?

It takes just five minutes to [get started with Aria]({{ site.portal_url }}/welcome-screen). Please don't hesitate to reach out to us and the Aria community at [Aria Discussion](mailto:ariadisc) if you have any questions.

*Thanks for taking the time to learn about Aria!*
