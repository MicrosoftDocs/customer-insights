---
title: Use demographic dimensions for splitting behavioral data (curated dimensions)
description: Use unified profile curated dimensions to enable audience insights customer profile properties.
ms.date: 07/27/2021
ms.service: customer-insights
ms.topic: conceptual
author: mkisel
ms.author: mkisel
ms.reviewer: mhart
manager: shellyha
---

# Use demographic dimensions for splitting behavioral data

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

By using unified profile demographic dimensions, engagement insights users can access audience insights profile properties. You can then use these properties in interactive analyses of behavioral data, including data captured by engagement insights on your website or mobile app.

>[!NOTE]
> Engagement insights includes out-of-the-box dimensions for event properties. More information: [View and create dimensions](dimensions.md)

## Prerequisite

- An engagement insights environment in which you have customer profile data linked to the audience insights environment where the customer profiles are created. More information: [Create a link between audience insights and engagement insights](integrate-audience-insights-engagement-insights.md)

> [!NOTE]
> After you create a link between the audience insights and engagement insights environments, you might only want data specific to customer profile properties, which can be useful as dimensions in engagement insights. For more information, go to [Enable audience insights unified profiles attributes and segments](integrate-audience-insights-engagement-insights.md#enable-audience-insights-unified-profiles-attributes-and-segments).

## Create a new custom report

1. On the left pane, select **Custom** > **New report**, and then select the metric you want. (For this example, we chose **Page views by Hour**.)

    :::image type="content" source="media/curated-dimensions1.png" alt-text="Select a metric.":::

2. In the Visualization editor, select **Dimensions**, and then select **Demographic** in the **Dimension Type** dropdown menu.

    :::image type="content" source="media/curated-dimensions2.png" alt-text="Select demographic.":::

3. Select a **Signal.Customer.*xxx*** dimension. (This example shows Signal.Customer.Country.)

    :::image type="content" source="media/curated-dimensions3.png" alt-text="Select a dimension.":::
  
## Limitations

Currently you can only use demographic dimensions for splitting behavioral data.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
