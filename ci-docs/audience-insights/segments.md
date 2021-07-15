---
title: "Segments in audience insights"
description: "Overview on segments and how to create and manage them."
ms.date: 05/03/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: mhart
manager: shellyha
---

# Segments overview

Segments let you group your customers based on demographic, transactional, or behavioral attributes. You can use segments to target promotional campaigns, sales activities, and customer support actions to achieve your business goals.

Customer profiles that match the filters of a segment definition are referred as *members* of a segment. Some [service limits](service-limits.md) apply.

## Create a new segment

There are multiple ways to create a new segment: 

- Complex segment with segment builder: [Blank segment](segment-builder.md#create-a-new-segment)
- Simple segments with one operator: [Quick segment](segment-builder.md#quick-segments)
- AI-powered way to find similar customers: [Similar Customers](find-similar-customer-segments.md)
- AI-powered suggestions based on measures or attributes: [Suggested segments to improve measures](suggested-segments.md)
- Suggestions based on activities: [Suggested segments based on customer activity](suggested-segments-activity.md)

## Manage existing segments

Go to the **Segments** page, to view all your saved segments and manage them.

Each segment is represented by a row that includes additional information about the segment.

:::image type="content" source="media/segments-selected-segment.png" alt-text="Selected segment with options dropdown list and available options.":::

The following action are available when you select a segment:

- **View** the segment details, including member count trend a preview of segment members.
- **Edit** the segment to change its properties.
- **Create duplicate** of a segment. You can choose to edit its properties right away or simply save the duplicate.
- **Refresh** the segment to include the latest data.
- **Activate** or **Deactivate** the segment. Segments have two possible states - active or inactive. These states come in handy when editing a segment. For inactive segments, the segment definition exists but it doesn't contain any customers yet. When you activate a segment, its state changes from 'inactive' to 'active" and it starts looking for customers that match the segment definition. If a [scheduled refresh](system.md#schedule-tab) is configured, inactive segments have the **Status** listed as **Skipped**, indicating that a refresh wasn't even attempted. When an inactive segment is activated, it will refresh and will be included in scheduled refreshes.
  Alternatively, you can use the **Schedule later** functionality in the **Activate/Deactivate** dropdown to specify a future date and time for activation and deactivation of a particular segment.
- **Rename** the segment.
- **Download** the list of members as a .CSV file.
- **Manage exports** to see exports related segment and manage them. [Learn more about exports.](export-destinations.md)
- **Delete** the segment.

## Refresh segments

You can refresh all segments at once by selecting **Refresh all** on the **Segments** page or you can refresh one or multiple segments when you select them and choose **Refresh** in from the options. Alternatively, you can configure a recurring refresh on **Admin** > **System** > **Schedule**.

> [!TIP]
> There are [six types of status](system.md#status-types) for tasks/processes. Additionally, most processes [depend on other downstream processes](system.md#refresh-policies). You can select the status of a process to see details on the progress of the entire job. After selecting **See details** for one of the job's tasks, you find additional information: processing time, the last processing date, and all errors and warnings associated with the task.

## Export segments

You can export a segment from the segments page or the [exports page](export-destinations.md). 

1. Go to the **Segments** page.

1. Select **Show more [...]** for the segment you want to export.

1. Select **Manage exports** from the actions dropdown list.

1. The page **Exports (preview) for segment** opens. You can see all configured exports grouped by by exports that contain the current segment or don't contain it.

   1. To add the selected segment to an export, select the export in the list and select **Add segment**.

   1. To create a new export with the selected segment, select **Add export**. For more information about creating exports, see [Set up a new export](export-destinations.md#set-up-a-new-export).

1. Select **Back** to return to the main page for segments.

## View processing history and segment members

You can see consolidated data about a segment by reviewing its details.

On the **Segments** page, select the segment you want to review.

The upper part of the page includes a trend graph that visualizes changes in member count. Hover over data points to see the member count on a specific date.

You can update the time frame of the visualization.

> [!div class="mx-imgBorder"]
> ![Segment time range.](media/segment-time-range.png "Segment time range")

The lower part contains a list of the segment members.

> [!NOTE]
> Fields that appear in this list are based on the attributes of your segment's entities.
>
>The list is a preview of the matching segment members and shows the first 100 records of your segment so that you can quickly evaluate it and review its definitions if needed. To see all matching records, you need to [export the segment](export-destinations.md).

[!INCLUDE[footer-include](../includes/footer-banner.md)] 
