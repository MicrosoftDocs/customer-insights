---
title: View and create metrics
description: How to create, edit, and delete metrics.
ms.reviewer: jusali
ms.author: v-salash
author: pickwick129
ms.date: 05/18/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# View and create metrics

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Metrics help understand behavior of your visitors. They aggregate [event](refined-events.md) properties and measure how often an action was taken or a behavior occurred.  

Suppose you’re running a marketing promotion on your website. You can use metrics to track the number of unique visitors or users who came to your website during the promotion. Analyzing metrics helps you better understand your website audience. You can separate visitors into new and returning categories to identify the differences in interest and intent between the groups.

Engagement insights include common metrics for out-of-the-box web and mobile events, such as: 

- Visitors
- Visits
- Page views
- Clicks

## View metrics

By using the [web SDK,](advanced-SDK-implementation.md) 
your events will automatically be sent with these metrics. Combining metrics with  [dimensions](view-create-dimensions.md) on a chart lets you measure behavior to understand your users. 

1. Go to **Data** in the left navigation pane. 
1. Select **Metrics** to see a list of all dimensions in the workspace. 
   > [!NOTE]
   > System-generated metrics are read-only. You can’t edit them. You can only create and edit custom metrics.

## Create a custom metric

Event and Workspace admins can create custom metrics. These *base* metrics are based on existing event properties. The property must be sent to an [event](advanced-SDK-implementation.md) in the workspace before you create the metric.

1. Go to **Data** and then select **Metrics**.
1. If the property is being sent, select **New metric**.

 :::image type="content" source="media/new-metric.png" alt-text="Add a metric to an event":::

3. In the pane, select a property to base the metric on.
1. To create a formula, select the **plus sign (+)** next to the property you want to add. Engagement insights currently only supports creating a formula based on one property. Then select one of the following aggregate functions. 

- Sum: the arithmetic total of all values 
- Average: the mean average of all values
- Count: the total number of values
- Distinct count: the total number of distinct values

5. For format, select the **Integer** or **Double** datatype. Integer is a whole number. For Double, you can pick between one and three decimal places.
1. Enter a display name for the metric and optionally a description.
1. Select **Save**. 

Once the formula is created, a preview of the chart shows the metric activity for the last hour. It can take up to a minute for the metric to show up in the list of metrics. Then it can be used in any report.

## Delete a custom metric

1. Go to **Data** and then select **Metrics**.
1. Select **More [...]** for a metric and then select **Delete**.

 :::image type="content" source="media/delete-metric.png" alt-text="Delete a metric to an event":::

3. Enter **CONFIRM DELETE** to confirm the deletion. 
1. Enter **Delete**.

 



[!INCLUDE[footer-include](../includes/footer-banner.md)]