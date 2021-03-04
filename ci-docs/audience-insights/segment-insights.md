---
title: "Segment insights for existing segments"
description: "Get insights on existing segments to see differences and commonalities."
ms.date: 06/10/2020
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: mhart
ms.reviewer: jimsonc
manager: shellyha
---

# Segment insights (preview)

Discover additional information and insights around your existing segments. Find out what differentiates two segments or what they have in common.

## Segment overlap

Segment overlap analysis shows how many and which customers are common to two or more segments. For example, how a segment of frequent customers overlaps with a segment that contains customers that are satisfied with your service or product.
You can also analyze how the overlap changes for specific attributes.

### Run an overlap analysis

1. Go to **Segments** and select the **Insights (preview)** tab.

1. Select **New** and choose the **Overlap** option in the **Choose Insight Type** pane.

1. Choose the segments of interest and select **Next**.

1. Optionally, choose one or more fields of interest to analyze overlaps for every possible field value and select **Next**.

1. Provide a name for you overlap analysis, an optional display name, and a description.

1. Select **Save** to start the analysis. The overlap analysis is ready when the status changes from Refreshing to Successful.

### View and optimize an overlap analysis

After completing the analysis, find details on this insight on **Segments** > **Insights (preview)**.

> [!div class="mx-imgBorder"]
> :::image type="content" source="media/segment-overlap.png" alt-text="Segment overlap insight details":::

Select an insight to see the analysis results:

- The number of members overlapping the segments selected for analysis.
- The number of members included in one of the segments but not in the rest of the segments.
- If you selected fields while configuring the overlap analysis, you'll find them in the corresponding tabs. You can use the filter drop-down to select any attribute level of interest and the table at the bottom will show the corresponding data.

## Segment differentiators

Segment differentiators help you find out what differentiates a segment from the rest of your customers or from another segment. You just have to select a segment and the system will identify profile attributes and measures that distinguish the selected segment.

### Run a differentiator analysis

1. Go to **Segments** and select the **Insights (preview)** tab.

1. Select **New** and choose the **Overlap** option in the **Choose Insight Type** pane.

1. Choose the segment you want to analyze as **Primary segment** and select **Next**.

1. Choose **All customers** or a **Secondary segment** to compare your primary segment with and select **Next**.

1. Optionally, choose one or more fields of interest to focus the analysis on specific attributes and select **Next**.

1. Provide a name for you overlap analysis, an optional display name, and a description.

1. Select **Save** to start the analysis. The overlap analysis is ready when the status changes from Refreshing to Successful.

### View and optimize a differentiators analysis

After completing the analysis, find details on this insight on **Segments** > **Insights (preview)**.

> [!div class="mx-imgBorder"]
> :::image type="content" source="media/segment-differentiators.png" alt-text="Segment differentiator insight details":::

Select an insight to see the analysis results. A differentiator analysis includes two tabs. The **Attributes** tab lists profile attributes considered as differentiators. The **Measures** tab lists differentiators. Each tab includes the following details:

- Ranked list of differentiators, sorted by difference score.
- The **Difference score** for each differentiator. The difference score represents the degree of difference of an attribute between two segments. The higher the difference score, the more the attributes differ between the two segments. Select a score to open the **Difference score** pane with the distributions of values for that attribute.

## Manage segment insights

You can use the following options on your insights from the command bar:

- **Back** to return the list of insights
- **Refresh** to run the analysis again
- **Delete** to remove this insight


[!INCLUDE[footer-include](../includes/footer-banner.md)]