---
title: "Measures overview"
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

Create measures to plan business activities by querying customer data and extract insights. For example, create a measure of *total spend per customer* and *total return per customer* to help identify a group of customers with high spend yet high return. Then, [create a segment](segments.md) based on these measures to drive next best actions.

## Create a measure

Choose how to create a measure based on your target audience.

# [Individual consumers (B-to-C)](#tab/b2c)

- From scratch with measure builder: [Build your own](measure-builder.md).
- From commonly used measures: [Use predefined templates](measure-templates.md).

# [Business accounts (B-to-B)](#tab/b2b)

From scratch with measure builder: [Build your own](measure-builder.md).

---

## Manage existing measures

Go to the **Measures** page to view the measures you created, their status, measure type, and the last time the data was refreshed. You can sort the list of measures by any column or use the search box to find the measure you want to manage.

Select next to a measure to view available actions. Select the measure name to preview the output and download a CSV file.

:::image type="content" source="media/measures-actions.png" alt-text="Actions to manage single measures."lightbox="media/measures-actions.png":::

- **Edit** the measure to change its properties.
- **Refresh** the measure to include the latest data.
- **Rename** the measure.
- **Activate** or **Deactivate** the measure. Inactive measures won't get refreshed during a [scheduled refresh](system.md#schedule-tab) and have the **Status** listed as **Skipped**, indicating that a refresh wasn't even attempted.
- **Tag** to [manage tags](work-with-tags-columns.md#manage-tags) for the measure.
- **Delete** the measure.
- **Columns** to [customize the columns](work-with-tags-columns.md#customize-columns) that display.
- **Filter** to [filter on tags](work-with-tags-columns.md#filter-on-tags).
- **Search name** to search by measure name.

## Refresh measures

Measures can be refreshed on an automatic schedule or refreshed manually on demand. To manually refresh one or more measures, select them and choose **Refresh**. To [schedule an automatic refresh](system.md#schedule-tab), go to **Admin** > **System** > **Schedule**.

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
