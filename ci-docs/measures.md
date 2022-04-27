---
title: "Understand and manage measures"
description: "Learn how measures help analyze and reflect the performance of your business."
ms.date: 03/24/2022

ms.subservice: audience-insights
ms.topic: conceptual
author: v-wendysmith
ms.author: wameng
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-measures
  - ci-measure-builder
  - ci-measure-template
  - ci-enrichment-details
  - customerInsights
---

# Measures overview

Measures help you to better understand customer behaviors and business performance. They look at relevant values from [unified profiles](data-unification.md). For example, a business wants to see the *total spend per customer* to understand an individual customer’s purchase history or measure *total sales of the company* to understand the aggregate-level revenue in the whole business.  

Measures are created [using the measure builder](measure-builder.md), a data query platform with various operators and simple mapping options. It lets you filter the data, group results, detect [entity relationship paths](relationships.md), and preview the output. You can [use predefined templates](measure-templates.md) to efficiently configure commonly used measures.

Use the measure builder to plan business activities by querying customer data and extract insights. For example, creating a measure of *total spend per customer* and *total return per customer* helps identify a group of customers with high spend yet high return. You can [create a segment](segments.md) based on these measures to drive next best actions.

## Manage your measures

You can find the list of measures on the **Measures** page.

You'll find information about the measure type, the creator, creation date, status, and state. When you select a measure from the list, you can preview the output and download a CSV file.

:::image type="content" source="media/measures-actions.png" alt-text="Actions to manage single measures."lightbox="media/measures-actions.png":::

The following actions are available when you select a measure:

- **Edit** the configuration of the measure.
- **Duplicate** a measure. You can choose to edit its properties right away or simply save the duplicate.
- **Refresh** the measure based on the latest data. To refresh all of your measures at the same time, select all measures and then **Refresh**.
- **Rename** the measure.
- **Activate** or **Deactivate**. Inactive measures won't get refreshed during a [scheduled refresh](system.md#schedule-tab).
- **Tag** to [manage tags](work-with-tags-columns.md#manage-tags) for the segment.
- **Delete** the measure.

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

## Next step

You can use existing measures to create [a customer segment](segments.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
