---
title: Use audience insights segments for use in engagement insights reports
description: Use audience insights segments in interactive analyses of behavioral data captured by engagement insights on a customer’s website.
ms.date: 07/27/2021
ms.service: customer-insights
ms.topic: conceptual
author: mkisel
ms.author: mkisel
ms.reviewer: mhart
manager: shellyha
---

# Use audience insights segments for use in engagement insights reports

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Audience insights segments enables engagement insights customers to use audience insights segments in interactive analyses of behavioral data captured by engagement insights on a customer’s website. 

## Prerequisites

Engagement insights environment in which you have audience insights segments data linked to the audience insights environment where the segments and customer profiles are created. For more information, see [Create a link between audience insights and engagement insights](integrate-audience-insights-engagement-insights.md). 

## Create audience insights segments 

> [!IMPORTANT]
> For audience insights segments to show up in engagement insights, you must first [run merge and downstream processes](../audience-insights/merge-entities.md). Downstream processes are important because they generate a unique table that prepares audience insights segments to be shared with engagement insights. (If a system refresh is scheduled, this automatically includes downstream processes.)

You can use audience insights segments in engagement insights out-of-the-box or custom reports. For more information, see [Out-of-box profile reports](profile-reports.md) or [Create and edit custom reports](custom-reports.md).

To use audience insights segments in engagement insights reports:

1. From your **Workspace** page, select **Data**, then the **Segments** tab.

    :::image type="content" source="media/integrate-audience-insights-segments1.png" alt-text="Choose segments":::

  >[!NOTE]
  > Selecting an audience insights segment takes you to audience insights, so you can find out how that segment was created, in terms of the rules and logic. For more information about audience insights segments, see [Segments overview](../audience-insights/segments.md).

2. Select an out-of-the-box report or [create a custom report](custom-reports.md), then select **Add condition**. (For this example, we chose the **Page views** report.)

    :::image type="content" source="media/integrate-audience-insights-segments2.png" alt-text="Add condition":::

3. Select **Filter by segment**, then click the dropdown list and select **Demographic**.

    :::image type="content" source="media/integrate-audience-insights-segments3.png" alt-text="Select demographic":::

4. Select **Segment name** in the dropdown list, then choose an audience insights segment.

    :::image type="content" source="media/integrate-audience-insights-segments4.png" alt-text="Choose segment":::

5. You can apply one or more segments, including behavioral (engagement insights) and demographic (audience insights) segments. 

    :::image type="content" source="media/integrate-audience-insights-segments6.png" alt-text="USA customers example":::

In the above example, the *USA customers* and the *Homepage* segments are shown as restricting the **Page views** report to display only those two segments. 


>[!NOTE]
> You can use audience insights segments to filter out-of-the-box reports, custom reports, and funnels in engagement insights. 


[!INCLUDE[footer-include](../includes/footer-banner.md)]