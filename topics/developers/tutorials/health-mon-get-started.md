---
layout: page
title: Get started with health monitoring
sub_title: Use health monitoring to get alerts
---

## Getting Started

Health Monitoring allows users to define models that group multiple metrics and the range of values where a user expects that metric to be in. The user can then get alerted in case the value of a metric moves in or out of a defined range.

1. Creating a Health Model

	A health model is a way to group metrics that are related to a particular health monitoring scenario. For example, your team may want to create a health model called 'Dev Ops' that contain metrics and alerts for live site issues. In order to setup a Model, navigate to the [Health Monitoring App]({{ site.portal_url }}/health){: target="_blank"} which will allow you to create a new health model or navigate through your existing Health Models. After the model is created, health metrics can be created within the context of that Model.

2. Creating a Health Metric

	After defining a health model, you will be taken to the health home page that is similar to a dashboard. From there you can add health metrics to your dashboard. A health metric is a time series chart configuration that includes information such as ranges of values, severity, criteria for raising an alert, and the subscriptions that are interested in those alerts. Read more about creating a [health metric][Define a Health Metric].

3. Configuring where health alerts are sent

	Once the intended health metrics are defined, users can [subscribe][Set up Subscriptions] either to the entire model or to a specific metric so that they are notified when a health metric reaches the range defined in its alert criteria.
	In order to be able to subscribe to metrics or models, users must create user roles - This can be done in the User Role Manager App. A user role defines a set of contacts and owns a set of subscriptions that define which health models and metrics that specific role is interested in, as well as, which set of the defined contacts should notifications be sent to for a specific subscription.

4. Legacy Health Metrics and Health Models

	For now the legacy metrics, models, and subscriptions are rendered as read-only to show users how they would look and be defined in the new portal. In the near future we will be releasing a migration feature, that will allow users to migrate their legacy metrics and models into full-fledged aria.ms models and metrics.

[Set up Subscriptions]: /developers/how-to/user-role
[Define a Health Metric]: /developers/how-to/health-mon-metrics
