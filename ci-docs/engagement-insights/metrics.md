---
title: View and create metrics
description: How to create, edit, and delete metrics.
ms.reviewer: mhart
ms.author: jusali
author: jusali
ms.date: 10/01/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# View and create metrics

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Metrics help understand behavior of your visitors. They aggregate event properties and measure statistics and performance of your web properties.  

Suppose you’re running a marketing promotion on your website. You can use metrics to track the number of unique visitors or users who came to your website during the promotion. Analyzing metrics helps you better understand your website audience. Combining metrics with [dimensions](dimensions.md) on a [custom report](custom-reports.md) lets you measure behavior to understand your users. For example,you can separate visitors into new and returning categories to identify the differences in interest and intent between the groups.

## View metrics

Engagement insights includes commonly used aggregations of event properties as system metrics: 

- Visitors
- Visits
- Page views
- Clicks

These system metrics are based on existing event properties in base events.

1. Go to **Data** in the left navigation pane. 
1. Select the **Metrics** tab to see a list of all metrics in the workspace. 
   > [!NOTE]
   > System-generated metrics are read-only. You can’t edit or delete them. You can only create and edit custom metrics.

## Create a metric

Environment and workspace admins can create metrics. Event properties must be sent to the workspace before you create a metric. You can create metrics based on event properties that are sent by base events or use the web SDK to [send custom event properties](advanced-SDK-implementation.md).

1. Go to **Data** > **Metrics**.
1. Select **New metric** to open the **Resource Library** and **New untitled metric** dialog.

   :::image type="content" source="media/new-metric.png" alt-text="Add a metric to an event.":::

1. In the **New untitled metric** dialog, select the **Format** dropdown list, and choose the **Integer** or **Double** datatype. Integer is a whole number. For Double, you can choose one and three decimal places.

   :::image type="content" source="media/create-new-metric.png" alt-text="Create a new metric.":::
   
5. In the **Resource Library** pane, find the event property to base the metric on.
6. Select the **plus sign (+)** next to the property to use it in the formula. You can only create a formula based on one property. 
7. Choose one of the following aggregate functions. 

   - Sum: the arithmetic total of all values 
   - Average: the mean average of all values
   - Count: the total number of values
   - Distinct count: the total number of distinct values

   After defining the metric, you see an activity preview of the metric for the last hour.

1. Select **Save**. 
1. Enter a name for the metric and select **Save**.

It can take up to a minute for the metric before you can use it to [create custom reports](custom-reports.md).

## Edit a metric

You can only edit custom metrics.

1. Go to **Data** > **Metrics**.
1. Select the metric in the list.
1. Change the definition of the metric
1. Select **Save**.

## Change the name of a metric

You can only change the name of custom metrics.

1. Go to **Data** > **Metrics**.
1. Select **More [...]** for a metric and choose **Edit name**.
1. Change the name. 
1. Select **Rename**.

## Delete a metric

You can only delete custom metrics.

1. Go to **Data** > **Metrics**.
1. Select **More [...]** for a metric and choose **Delete**.

   :::image type="content" source="media/delete-metric.png" alt-text="Delete a metric to an event.":::

1. Select **Delete** to confirm the deletion.



[!INCLUDE[footer-include](../includes/footer-banner.md)]
