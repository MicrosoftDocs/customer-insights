---
title: Manage existing measures
description: Learn how to manage existing measures in Customer Insights  
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: v-wendysmith
manager: shellyha 
ms.service: customer-insights
ms.subservice: audience-insights

ms.topic: how-to
ms.date: 01/05/2023
ms.custom: bap-template
---

# Manage existing measures

Go to the **Measures** page to view the measures you created, their status, measure type, the last time the data was refreshed, and their refresh schedule. You can sort the list of measures by any column or use the search box to find the measure you want to manage.

Select next to a measure to view available actions. Select the measure name to preview the output and download a CSV file.

:::image type="content" source="media/measures-actions.png" alt-text="Actions to manage single measures."lightbox="media/measures-actions.png":::

> [!TIP]
> Supported bulk operations include: refresh, delete, change state (activate/deactivate), and tags.

- **Edit** the measure to change its properties.
- **Refresh** one or more measures manually to include the latest data.
- **Rename** the measure.
- **Activate** or **Deactivate** one or more measures. For multiple measures, select **Change state**. Inactive measures won't get refreshed during a [scheduled refresh](schedule-refresh.md) and have the **Status** listed as **Skipped**, indicating that a refresh wasn't even attempted.
- **Tag** to [manage tags](work-with-tags-columns.md#manage-tags) for one or more measures.
- **Delete** one or more measures.
- [**Schedule**](measures-schedule.md) to customize schedules for measures.
- **Columns** to [customize the columns](work-with-tags-columns.md#customize-columns) that display.
- **Filter** to [filter on tags](work-with-tags-columns.md#filter-on-tags).
- **Search name** to search by measure name.

## Manage the number of active measures

When you approach or exceed the number of active measures based on the [service limits](service-limits.md), you might experience the following:

- Typical system refresh time is slower
- Running or refreshing individual measures is slower
- Refresh failures indicating out of memory

The complexity of your measures can also impact performance. To help you prevent performance issues, Customer Insights provides messages or warnings when you approach, reach, or exceed the total number of active measures. These messages display on the **Measures** list page. If you encounter these messages or symptoms, see the following recommendations.

1. Delete old or no longer relevant measures even if they are static or inactive.
1. [Schedule individual measures](measures-schedule.md) to run weekly or monthly during slow business days (such as the weekend) instead of daily.


[!INCLUDE [footer-include](includes/footer-banner.md)]
