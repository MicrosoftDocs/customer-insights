---
title: "Segments overview"
description: "Overview on segments and how to create and manage them."
ms.date: 07/27/2022
ms.subservice: audience-insights
ms.topic: overview
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-customers-page
  - ci-enrichment-details
  - ci-segments
  - ci-segment-details
  - customerInsights
---

# Segments overview

Segments let you group your customers based on demographic, transactional, or behavioral attributes. You can use segments to target promotional campaigns, sales activities, and customer support actions to achieve your business goals.

Customer or contact profiles that match the filters of a segment definition are referred to as *members* of a segment. Some [service limits](/dynamics365/customer-insights/service-limits) apply.

In business accounts (B-to-B), segments can be based on audience type: accounts from the *Customer* entity or contacts from the *ContactProfile* entity. Choose the audience type when creating the segment.

## Create a segment

Choose how to create a segment based on your target audience.

# [Individual consumers (B-to-C)](#tab/b2c)

- Complex segments with segment builder: [Build your own](segment-builder.md)
- Simple segments with one operator: [Quick segment](segment-quick.md)
- AI-powered way to find similar customers: [Similar customers](find-similar-customer-segments.md)
- AI-powered suggestions based on measures or attributes: [Suggested segments based on measures](suggested-segments.md)
- Suggestions based on activities: [Suggested segments based on customer activity](suggested-segments-activity.md)

# [Business accounts (B-to-B)](#tab/b2b)

- Simple or complex segments with segment builder: [Build your own](segment-builder.md)

---

## Manage existing segments

Go to the **Segments** page to view the segments you created, their status and state, and the last time the data was refreshed. You can sort the list of segments by any column or use the search box to find the segment you want to manage.

In B-to-C environments, the **Segments** page also displays the number of members. In B-to-B environments, the **Segments** page also displays **Audience Type** which indicates whether the segment is based on accounts or contacts.

Select a segment to view available actions.

:::image type="content" source="media/segments-selected-segment.png" alt-text="Selected segment with options dropdown list and available options." lightbox="media/segments-selected-segment.png":::

- [**View**](#view-segment-details) the segment details, including member count trend and a preview of segment members.
- **Download** the list of members as a .CSV file.
- **Edit** the segment to change its properties.
- **Create duplicate** of a segment. You can choose to edit its properties right away or save the duplicate.
- [**Refresh**](#refresh-segments) the segment to include the latest data.
- **Activate** or **Deactivate** the segment. Inactive segments won't get refreshed during a [scheduled refresh](system.md#schedule-tab) and have the **Status** listed as **Skipped**, indicating that a refresh wasn't even attempted. Active segments are refreshed based on their type: static or dynamic.
- **Make static** or **Make dynamic** the segment type. Static segments must be refreshed manually. Dynamic segments are automatically refreshed during system refreshes.
- [**Find similar customers**](find-similar-customer-segments.md) from the segment.
- **Rename** the segment.
- **Tag** to [manage tags](work-with-tags-columns.md#manage-tags) for the segment.
- [**Manage exports**](#export-segments) to see export-related segments and manage them. [Learn more about exports.](export-destinations.md)
- **Delete** the segment.
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
>The list is a preview of the matching segment members and shows the first 100 records of your segment so that you can quickly evaluate it and review its definitions if needed. To see all matching records, select **See more** which opens the [**Entities**](entities.md) page or [export the segment](export-destinations.md).

## Refresh segments

Segments can be refreshed on an automatic schedule or refreshed manually on demand. To manually refresh one or more segments, select them and choose **Refresh**.

To [schedule an automatic refresh](system.md#schedule-tab), go to **Admin** > **System** > **Schedule**. The following rules apply:

- All segments with the type **Dynamic** or **Expansion** will be automatically refreshed at the set cadence. Once the refresh is complete, the **Status** indicates if there were any issues in refreshing the segment. The **Last refreshed** shows a timestamp of the last successful refresh. If an error occurs, select the error to see details about what happened.
- Segments with the type **Static** *won't* be refreshed automatically. The **Last refreshed** shows a timestamp of the last time the static segment was run or refreshed manually.

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

## Export segments

Export segments to other apps to further use the data. Export a segment from the segments page or the [exports page](export-destinations.md).

1. Go to the **Segments** page and select the segment you want to export.

1. Select **Manage exports**. The page **Exports (preview) for segment** opens. View all configured exports grouped by whether they contain the current segment or not.

   1. To add the selected segment to an export, **Edit** the respective export to select the corresponding segment, then save. In environments for individual customers, select the export in the list and select **Add segment** to achieve the same outcome.

   1. To create a new export with the selected segment, select **Add export**. For more information about creating exports, see [Set up a new export](export-destinations.md#set-up-a-new-export).

1. Select **Back** to return to the main page for segments.

## Track usage of a segment

If you use segments in apps which are based on the same Microsoft Dataverse organization that is connected with Customer Insights, you can track the usage of a segment. For [Customer Insights segments used in customer journeys of Dynamics 365 Marketing](/dynamics365/marketing/real-time-marketing-ci-profile), the system informs you about the usage of that segment.

When editing a segment that is being used within the Customer Insights environment, or in a customer journey in Marketing, a banner in the [segment builder](segment-builder.md) informs you about the dependencies. Inspect the dependency details directly from the banner or by selecting **Usage** in the segment builder.

The **Segment usage** pane shows the details about the usage of this segment in Dataverse-based apps. For segments used in customer journeys, you’ll find a link to inspect the journey in Marketing where this segment is used. If you have permissions to access the Marketing app, view more details there.

:::image type="content" source="media/segment-usage-pane.png" alt-text="Side pane with details of the segment usage in the segment builder.":::

The system informs you about the usage of a tracked segment when you try to delete it. If the segment you're about to delete is used in a customer journey in Marketing, that journey will stop for all users in the segment. If the journey is part of a marketing campaign, the deletion will affect that campaign itself. However, you can still delete the segment despite the warnings.

:::image type="content" source="media/segment-usage-delete.png" alt-text="Dialog box to confirm segment deletion when a segment is used in a Dataverse application.":::

### Supported apps

Usage is currently tracked in the following Dataverse-based apps:

- [Customer journeys in Dynamics 365 Marketing](/dynamics365/marketing/real-time-marketing-ci-profile)

[!INCLUDE [footer-include](includes/footer-banner.md)]
