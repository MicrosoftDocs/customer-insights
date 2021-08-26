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

Unified profile demographic dimensions allow engagement insights users to access audience insights profile properties. You can then use these properties in interactive analyses of behavioral data, including data captured by engagement insights on a customer’s website or mobile app.

>[!NOTE]
> Engagement insights includes out-of-the-box dimensions for event properties. For more information, see [View and create dimensions](dimensions.md).

## Prerequisites

Engagement insights environment in which you have customer profile data linked to the audience insights environment where the customer profiles are created. For more information, see [Create a link between audience insights and engagement insights](integrate-audience-insights-engagement-insights.md).

> [!NOTE]
> Once you create a link between the audience insights and engagement insights environment, refer to [Enable audience insights unified profiles attributes and segments](integrate-audience-insights-engagement-insights.md#enable-audience-insights-unified-profiles-attributes-and-segments) if you only want data specific to customer profile properties, which can be useful as dimensions in engagement insights.

## Create a new custom report

To create a new custom report in engagement insights:

1. Select a desired metric. (For this example, we chose Custom > New report.)

    :::image type="content" source="media/curated-dimensions1.png" alt-text="Select a metric":::

2. In the Visualization editor, select **Dimensions**, then **demographic** in the Dimension type dropdown box.

    :::image type="content" source="media/curated-dimensions2.png" alt-text="Select demographic":::

3. Select a **signal.customer.xxx** dimension. (This example shows *signal.customer.country*.)

    :::image type="content" source="media/curated-dimensions3.png" alt-text="Select a dimension":::
  
## Limitations

Currently you can only use demographic dimensions for splitting behavioral data.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
