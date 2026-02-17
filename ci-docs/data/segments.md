---
title: "Create and manage segments"
description: "How to create and manage a group of customers called segments."
author: JimsonChalissery
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.topic: how-to
ms.date: 02/17/2026
ms.custom: bap-template
---

# Create and manage segments

Segments let you group your customers based on demographic, transactional, or behavioral attributes. Use segments to target promotional campaigns, sales activities, and customer support actions to achieve your business goals.

Customer or contact profiles that match the filters of a segment definition are referred to as *members* of a segment. Some [service limits](/dynamics365/customer-insights/service-limits) apply.

## Create segments

Choose how to create a segment based on your target audience.

- Complex segments with segment builder: [Build your own](segment-builder.md)
- Simple segments with one operator: [Quick segment](segment-quick.md)
- AI-powered way to find similar customers: [Similar customers](find-similar-customer-segments.md)
- AI-powered suggestions based on measures or attributes: [Suggested segments based on measures](suggested-segments.md#suggested-segments-based-on-measures-preview)
- Suggestions based on activities: [Suggested segments based on customer activity](suggested-segments.md#suggested-segments-based-on-activity-preview)

## Manage existing segments

Go to the **Insights** > **Segments** page to view the segments you created, their status and state, the last time the data was refreshed, and their refresh schedule. You can sort the list of segments by any column or use the search box to find the segment you want to manage.

Select next to a segment to view available actions.

:::image type="content" source="media/segments-selected-segment.png" alt-text="Selected segment with options dropdown list and available options." lightbox="media/segments-selected-segment.png":::

> [!TIP]
> Supported bulk operations include: refresh, download, delete, change state (activate/deactivate), change type (static/dynamic), and tags.

- [**View**](#view-segment-details) the segment details, including member count trend and a preview of segment members.
- **Download** the list of members as a CSV file for one or more segments.
- **Edit** the segment to change its properties or [view segment member counts](#view-segment-member-counts-preview) for each rule.
- **Create duplicate** of a segment. You can choose to edit its properties right away or save the duplicate.
- **Refresh** one or more segments manually to include the latest data. The **Last refreshed** column shows a timestamp of the last successful refresh. If an error occurs, select the error to see details about what happened.
- **Activate** or **Deactivate** one or more segments. For multiple segments, select **Change state**. Inactive segments don't get refreshed during a [scheduled refresh](segments-schedule.md) and have the **Status** listed as **Skipped**, indicating that a refresh wasn't even attempted. Active segments are refreshed based on their type: static or dynamic and their [schedule](segments-schedule.md).
- **Make static** or **Make dynamic** the segment type. Static segments must be refreshed manually. Dynamic segments are automatically refreshed according to their [schedule](segments-schedule.md).
- [**Find similar customers**](find-similar-customer-segments.md) from the segment.
- **Rename** the segment.
- **Tag** to [manage tags](work-with-tags-columns.md#manage-tags) for one or more segments.
- [**Manage exports**](#export-segments) to see export-related segments and manage them. [Learn more about exports.](export-destinations.md)
- **Delete** one or more segments.
- [**Schedule**](segments-schedule.md) to customize schedules for segments.
- [**Disable auto cleanup**](#automated-deactivation-of-unused-segments).
- **Columns** to [customize the columns](work-with-tags-columns.md#customize-columns) that display.
- **Filter** to [filter on tags](work-with-tags-columns.md#filter-on-tags).
- **Search name** to search by segment name.

### Segment management tips

The smaller the number of segments and measures that need to be refreshed daily, the quicker the overall system refresh takes. To lower the number of segments refreshed daily, consider the following tips:

- When a campaign is over and you no longer need a segment, **Delete** it. If a campaign runs more than once, you can deactivate the segment. Deactivating it saves the segment configuration, but stops the automatic refresh.

- [Schedule](segments-schedule.md) segments on a slower cadence so they aren't refreshed daily.

- We recommend setting up a recurring audit process to review segments and measures and delete the ones that aren't needed anymore. To help you with this process, [use tags](work-with-tags-columns.md) with campaign and end date information. During the audit process you can search for tags and delete segments and measures in bulk.

## View segment details

On the **Segments** page, select a segment to view the processing history and segment members.

The upper part of the page includes a trend graph that visualizes changes in member count. Hover over data points to see the member count on a specific date. Change the time frame of the visualization.

:::image type="content" source="media/segment-time-range.png" alt-text="Segment time range.":::

The lower part contains a list of the segment members.

> [!NOTE]
> Fields that appear in this list are based on the attributes of your segment's tables.
>
> The list is a preview of the matching segment members and shows the first 100 records of your segment so that you can quickly evaluate it and review its definitions if needed. To see all matching records, select **See more** which opens the [**Tables**](tables.md) page or [export the segment](export-destinations.md).

## View segment member counts (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

View the number of members based on each rule or combination of rules in a segment. The number of members can help you determine if the rules are meeting your expectations.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

1. On the **Segments** page, find the segment you want to view and select **Edit**.

1. Turn on **Inspection mode**.

1. Save the segment.

1. Run or refresh the segment. After the refresh completes, segment member counts display.

> [!TIP]
> While you edit a segment, the rules show the old value for the member count until you save the updated segment. Once save, the values are reset to zero. After you refresh it, the updated values show on the rules.

The following image shows the different member counts.

:::image type="content" source="media/segment-count.svg" alt-text="Example of segment member count.":::

1. The number of members at the top of the page shows the number of customers for the segment after all rules are calculated.

1. Each rule shows the number of customers based on that rule, its subrules, and its conditions.

1. If you hover over the member count for each rule, a tooltip displays. The tooltip shows the number of customers based on that rule and all previous rules. For example, the Rule 2 tooltip shows the union or combined count of Rule 1 and Rule 2. The Rule 3 tooltip shows the combined count of Rule 1 and Rule 2 and the intersection of Rule 3.

## Export segments

Export segments to other apps to further use the data. Export a segment from the segments page or the [exports page](export-manage.md).

1. Go to the **Insights** > **Segments** page and select the segment you want to export.

1. Select **Manage exports**. The page **Exports (preview) for segment** opens. View all configured exports grouped by whether they contain the current segment or not.

   - To add the selected segment to an export, **Edit** the respective export to select the corresponding segment, then save. In environments for individual customers, select the export in the list and select **Add segment** to achieve the same outcome.

   - To create a new export with the selected segment, select **Add export**. For more information about creating exports, see [Set up a new export](export-manage.md#set-up-a-new-export).

1. Select **Back** to return to the main page for segments.

## Automated deactivation of unused segments

To optimize refresh performance, the system automatically deactivates unused segments every day. Unused segments are segments that aren't used in exports, measures, other segments, or in Customer Insights - Journeys and created or updated more than 45 days ago.

Contributors can delete these deactivated segments if they're no longer needed or reactivate them if they intend to use them again. Alternatively, admins can [specify segments that are excluded from the automated deactivation](#specify-segments-that-never-expire).

Deactivated segments don't refresh automatically when the system refreshes. They're tagged with **AutoDeactivated** when updated by automated cleanup.

### Specify segments that never expire

> [!IMPORTANT]
> This feature is only available to users with an Administrator user role.

To avoid automated deactivation if a segment is no longer in use, admins can mark these segments.

1. Go to the **Insights** > **Segments** page and select a segment.

1. In the command bar, select **Disable auto cleanup**.

1. Confirm the selection.

## Manage the number of active segments

When you approach or exceed the number of active segments based on the [service limits](service-limits.md), you might experience the following:

- Typical system refresh time is slower.
- Running or refreshing individual segments is slower.
- Refresh failures indicating out of memory.

The complexity of your segments can also impact performance. To help you prevent performance issues, Dynamics 365 Customer Insights - Data provides messages or warnings when you approach, reach, or exceed the total number of active segments. These messages display on the **Segments** list page. If you encounter these messages or symptoms, see the following recommendations.

1. Delete old or no longer relevant segments even if they're static or inactive. When a campaign ends, deactivate associated segments for recurring campaigns.
1. [Schedule individual segments](segments-schedule.md) to run weekly or monthly during slow business days (such as the weekend) instead of daily.

## Use segments in Customer Insights - Journeys

To use Customer Insights - Data segments in Customer Insights - Journeys, [connect the two applications](marketing-get-started.md#connect-customer-insights---data-to-customer-insights---journeys).

1. Create your segment in Customer Insights - Data.
1. Verify the segment appears in Dataverse. Go to **Power Apps** > **Tables** > **msdynci_segmentmembership** and confirm data exists.
1. In Customer Insights - Journeys, create a new journey and select the segment under "Customer Insights segments."

### Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Segment not visible in Journeys | Dataverse sync not enabled | Enable in **Settings** > **Data sharing** |
| Segment shows 0 members in Journeys | Segment hasn't synced to Dataverse yet | Wait for the next scheduled refresh |
| "Individual segment evaluation failed" | Segment query references unavailable data | Edit segment, verify all referenced tables exist and have data |

## Known limitations

- Filter value dropdowns in the segment builder do not currently support sorting. Use the search box within the dropdown to find specific values.

## See also

- [FastTrack blog: Understanding Job Execution Flow in Customer Insights - Data Batch Runs](https://community.dynamics.com/blogs/post/?postid=84fbbaaf-262b-f011-8c4e-7c1e5218b899)

[!INCLUDE [footer-include](includes/footer-banner.md)]
