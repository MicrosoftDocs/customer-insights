---
title: Manage existing segments
description: Learn how to manage existing segments in Customer Insights 
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

# Manage existing segments

Go to the **Segments** page to view the segments you created, their status and state, the last time the data was refreshed, and their refresh schedule. You can sort the list of segments by any column or use the search box to find the segment you want to manage. In B-to-B environments, the **Audience Type** column identifies whether a segment is based on accounts or contacts.

Select next to a segment to view available actions.

:::image type="content" source="media/segments-selected-segment.png" alt-text="Selected segment with options dropdown list and available options." lightbox="media/segments-selected-segment.png":::

> [!TIP]
> Supported bulk operations include: refresh, download, delete, change state (activate/deactivate), change type (static/dynamic), and tags.

- [**View**](#view-segment-details) the segment details, including member count trend and a preview of segment members.
- **Download** the list of members as a .CSV file for one or more segments.
- **Edit** the segment to change its properties.
- **Create duplicate** of a segment. You can choose to edit its properties right away or save the duplicate.
- **Refresh** one or more segments manually to include the latest data. The **Last refreshed** column shows a timestamp of the last successful refresh. If an error occurs, select the error to see details about what happened.
- **Activate** or **Deactivate** one or more segments. For multiple segments, select **Change state**. Inactive segments won't get refreshed during a [scheduled refresh](segments-schedule.md) and have the **Status** listed as **Skipped**, indicating that a refresh wasn't even attempted. Active segments are refreshed based on their type: static or dynamic and their [schedule](segments-schedule.md).
- **Make static** or **Make dynamic** the segment type. Static segments must be refreshed manually. Dynamic segments are automatically refreshed according to their [schedule](segments-schedule.md).
- [**Find similar customers**](find-similar-customer-segments.md) from the segment.
- **Rename** the segment.
- **Tag** to [manage tags](work-with-tags-columns.md#manage-tags) for one or more segments.
- [**Manage exports**](#export-segments) to see export-related segments and manage them. [Learn more about exports.](export-destinations.md)
- **Delete** one or more segments.
- [**Schedule**](segments-schedule.md) to customize schedules for segments.
- **Columns** to [customize the columns](work-with-tags-columns.md#customize-columns) that display.
- **Filter** to [filter on tags](work-with-tags-columns.md#filter-on-tags).
- **Search name** to search by segment name.

## View segment details

On the **Segments** page, select a segment to view the processing history and segment members.

The upper part of the page includes a trend graph that visualizes changes in member count. Hover over data points to see the member count on a specific date. Change the time frame of the visualization.

:::image type="content" source="media/segment-time-range.png" alt-text="Segment time range.":::

The lower part contains a list of the segment members.

> [!NOTE]
> Fields that appear in this list are based on the attributes of your segment's entities.
>
> The list is a preview of the matching segment members and shows the first 100 records of your segment so that you can quickly evaluate it and review its definitions if needed. To see all matching records, select **See more** which opens the [**Entities**](entities.md) page or [export the segment](export-destinations.md).

## Export segments

Export segments to other apps to further use the data. Export a segment from the segments page or the [exports page](export-destinations.md).

1. Go to the **Segments** page and select the segment you want to export.

1. Select **Manage exports**. The page **Exports (preview) for segment** opens. View all configured exports grouped by whether they contain the current segment or not.

   - To add the selected segment to an export, **Edit** the respective export to select the corresponding segment, then save. In environments for individual customers, select the export in the list and select **Add segment** to achieve the same outcome.

   - To create a new export with the selected segment, select **Add export**. For more information about creating exports, see [Set up a new export](export-destinations.md#set-up-a-new-export).

1. Select **Back** to return to the main page for segments.

## Manage the number of active segments

When you approach or exceed the number of active segments based on the [service limits](service-limits.md), you might experience the following:

- Typical system refresh time is slower
- Running or refreshing individual segments is slower
- Refresh failures indicating out of memory

The complexity of your segments can also impact performance. To help you prevent performance issues, Customer Insights provides messages or warnings when you approach, reach, or exceed the total number of active segments. These messages display on the **Segments** list page. If you encounter these messages or symptoms, see the following recommendations.

1. Delete old or no longer relevant segments even if they are static or inactive.
1. [Schedule individual segments](segments-schedule.md) to run weekly or monthly during slow business days (such as the weekend) instead of daily.

[!INCLUDE [footer-include](includes/footer-banner.md)]
