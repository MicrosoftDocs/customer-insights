---
layout: page
title: Health monitoring metrics
---

For a quick introduction, you can watch the video below.

{% include video.html src="HealthMonitoringV2.mp4" %}

## Creating a health metric

1. Open the Health Monitoring App
2. Click The **+** button in the **Health Model** view.

### Data pane

Define your dimensions and measures as you would for your time series chart, but note that only one measure can be selected for a health metric. Aria does not support alerting on multiple measures yet.

{% img "how-to/healthmonitoring/metricDataPane.png" alt:"Data pane of a health metric" class:"img-responsive" %}

### Health pane

Define your health configurations such as ranges and criterias for alerting.

{% img "how-to/healthmonitoring/metricHealthPane.png" alt:"Health pane of a health metric" class:"img-responsive" %}

### Ranges

Define the ranges of values that are relevant and assign a color to each range. Commonly, users select **Green** to indicate that the metric is behaving as expected, **Yellow** to indicate slight degradation and **Red** to indicate severe degradation. Nonetheless, the color semantics are left to the user as the colors do not have an inherent meaning. The colors are then used to set up the alert criteria and severity.

### Alert Criteria

Define the number of times a particular threshold color must be observed within a window by the health monitor to raise an alert with the specified severity.

### Options

Define custom behaviors for this specific health metric.

### Subscriptions

Lists all the subscriptions made to this specific metric and has a link to the User Role Manager app to allow the user to create new user roles and subscribe with them.

> **Note**: In order for users to receive the alerts raised by a given metric or model they need to actively [subscribe][Set up Subscriptions] to the metric or model using a user role that contains the contacts where they want their alert to be sent.

{% img "how-to/healthmonitoring/healthPaneSubscriptions.png" alt:"Subscription section in the health pane of a health metric" class:"img-responsive" %}

### Still not clear?

Please refer to the health mon faq page: [/help/faqs/health-monitoring/](/help/faqs/health-monitoring/)


[Set up Subscriptions]: /developers/how-to/user-role

