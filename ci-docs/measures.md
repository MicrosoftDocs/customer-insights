---
title: "Measures overview"
description: "Learn how measures help analyze and reflect the performance of your business."
ms.date: 09/16/2022

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
- **Activate** or **Deactivate** the measure. Inactive measures won't get refreshed during a [scheduled refresh](#schedule-measures) and have the **Status** listed as **Skipped**, indicating that a refresh wasn't even attempted.
- **Tag** to [manage tags](work-with-tags-columns.md#manage-tags) for the measure.
- **Delete** the measure.
- [**Schedule**](#schedule-measures) the measure.
- **Columns** to [customize the columns](work-with-tags-columns.md#customize-columns) that display.
- **Filter** to [filter on tags](work-with-tags-columns.md#filter-on-tags).
- **Search name** to search by measure name.

## Schedule measures

Measures can be refreshed on the [scheduled system refresh](schedule-refresh.md), weekly, monthly, or refreshed manually on demand. The default is every scheduled system refresh. For example, you might want to schedule measures that don't change often or are for last season on a slower cadence such as monthly to avoid unnecessary processing time.

Define refresh schedules for individual measures or several measures at once. The currently defined schedule is listed in the **Schedule** column of the measure list.

1. Go to **Measures**.

1. Select one or more measures you want to schedule.

1. Select **Schedule**.

1. In the **Schedule** pane, set the **Schedule run** to **On** to run the segment automatically. Set it to **Off** to refresh it manually.

1. For automatically refreshed measures, select the **Recurrence** value and the details for it. On the scheduled day, the refresh occurs during the time of the scheduled system refresh.

1. When defining the schedule for several measures, make a selection under **Keep or override schedules**:
   - **Keep individual schedules**: Keep the previously defined schedule for the selected measures and only disable or enable them.
   - **Define new schedule for all selected Measures**: Override the existing measures of the selected segments.

1. Select **Save**.

1. To view the next refresh scheduled for a measure, on the **Measures** page, select **Columns** and add the **Next refresh** column.

[!INCLUDE [footer-include](includes/footer-banner.md)]
