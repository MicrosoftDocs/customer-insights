---
title: View and create segments
description: How to create, edit, and delete segments and where to use them.
ms.reviewer: mhart
ms.author: jusali
author: jusali
ms.date: 05/20/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# View and create segments

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Value prop and intro to segments (create a custom set of filters based on dimensions to quickly apply on reports, introduce filtering methods on reports in addition to drill-down, )

## View dimensions

1. Go to **Data** in the left navigation pane. 
1. Select the **Segments** tab to see a list of all segments in the workspace. 

## Create a segment

- Environment and workspace admins can create segments.
- Segment is a set of rules. At least one, can be multiple rules.
- Rules are filters applied on dimensions.
- Multiple rules are connected via AND or OR, no combination of logical connectors.

Describe an example - Segment where Browser name = Edge OR Edge mobile -> Filter reports for all events that come from either Edge or Edge mobile.

1. Go to **Data** > **Segments**.
1. Select **New segment**.

   :::image type="content" source="media/new-metric.png" alt-text="Add a metric to an event":::

1. Click path for rule definition in simple steps.
1. Select **Save**. 
1. Enter a name for the metric and select **Save**.

It can take up to a minute for the metric before you can use it apply filters on reports.

## Edit a segment

1. Go to **Data** > **Segments**.
1. ... 

## Delete a segment

1. Go to **Data** > **Metrics**.
1. ...

[!INCLUDE[footer-include](../includes/footer-banner.md)]