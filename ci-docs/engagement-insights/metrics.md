---
title: View and create metrics
description: How to create, edit, and delete metrics.
ms.reviewer: jusali
ms.author: v-salash
author: pickwick129
ms.date: 05/20/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# View and create metrics

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Metrics help understand behavior of your visitors. They aggregate event properties and measure how often an action was taken or a behavior occurred.  

Suppose you’re running a marketing promotion on your website. You can use metrics to track the number of unique visitors or users who came to your website during the promotion. Analyzing metrics helps you better understand your website audience. You can separate visitors into new and returning categories to identify the differences in interest and intent between the groups.

## View metrics

Engagement insights includes commonly used metrics for events, such as: 

- Visitors
- Visits
- Page views
- Clicks

By using the [web SDK](advanced-SDK-implementation.md), your events will automatically be sent with these metrics. These default metrics are based on existing event properties in base events. Combining metrics with [dimensions](dimensions.md) on a [custom report](custom-reports.md) lets you measure behavior to understand your users. 

1. Go to **Data** in the left navigation pane. 
1. Select **Metrics** to see a list of all metrics in the workspace. 
   > [!NOTE]
   > System-generated metrics are read-only. You can’t edit them. You can only create and edit custom metrics.

## Create a custom metric

Environment and workspace admins can create custom metrics. Event properties must be sent to the workspace before you create a metric. You can create metrics based on event properties that are sent by base events or use the web SDK to [send custom event properties](advanced-SDK-implementation.md).

1. Go to **Data** > **Metrics**.
1. Select **New metric**.

   :::image type="content" source="media/new-metric.png" alt-text="Add a metric to an event":::

1. For format, select the **Integer** or **Double** datatype. Integer is a whole number. For Double, you can pick between one and three decimal places.
1. In the **Resource library** pane, find the event property to base the metric on.
1. Select the **plus sign (+)** next to the property to use it in the formula. You can only create a formula based on one property. 
1. Choose one of the following aggregate functions. 

   - Sum: the arithmetic total of all values 
   - Average: the mean average of all values
   - Count: the total number of values
   - Distinct count: the total number of distinct values

   After defining the metric, you see an activity preview of the metric for the last hour.

1. Select **Save**. 
1. Enter a name for the metric and select **Save**.

It can take up to a minute for the metric before you can use it to [create custom reports](../audience-insights/segments.md).

## Edit a custom metric

1. Go to **Data** > **Metrics**.
1. Select the metric in the list.
1. Change the definition of the metric
1. Select **Save**.

## Change the name of a custom metric

1. Go to **Data** > **Metrics**.
1. Select **More [...]** for a metric and choose **Edit name**.
1. Change the name. 
1. Select **Rename**.

## Delete a custom metric

1. Go to **Data** > **Metrics**.
1. Select **More [...]** for a metric and choose **Delete**.

   :::image type="content" source="media/delete-metric.png" alt-text="Delete a metric to an event":::

1. Select **Delete** to confirm the deletion.

[!INCLUDE[footer-include](../includes/footer-banner.md)]