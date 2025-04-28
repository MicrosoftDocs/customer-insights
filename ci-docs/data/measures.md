---
title: "Create and manage measures"
description: "Create and manage measures to help analyze and reflect the performance of your business."
author: JimsonChalissery
ms.author: jimsonc
ms.topic: how-to
ms.date: 04/28/2025
ms.custom: bap-template
---

# Create and manage measures

Measures help you to better understand customer behaviors and business performance. They look at relevant values from [unified profiles](data-unification.md). For example, a business wants to see the *total spend per customer* to understand an individual customer’s purchase history or measure *total sales of the company* to understand the aggregate-level revenue in the whole business. Some [service limits](/dynamics365/customer-insights/service-limits) apply.

## Create measures

Create measures to plan business activities by querying customer data and extract insights. For example, create a measure of *total spend per customer* and *total return per customer* to help identify a group of customers with high spend yet high return. Then, [create a segment](segments.md) based on these measures to drive next best actions.

Choose how to create a measure.

- From scratch with measure builder: [Build your own](measure-builder.md).
- From commonly used measures: [Use predefined templates](measure-templates.md).

## Manage existing measures

Go to the **Insights** > **Measures** page to view the measures you created, their status, measure type, and the last time the data was refreshed. You can sort the list of measures by any column or use the search box to find the measure you want to manage.

Select next to a measure to view available actions. Select the measure name to preview the output and download a CSV file.

:::image type="content" source="media/measures-actions.png" alt-text="Actions to manage single measures."lightbox="media/measures-actions.png":::

> [!TIP]
> Supported bulk operations include: refresh, delete, change state (activate/deactivate), and tags.

- **Edit** the measure to change its properties.
- **Refresh** one or more measures manually to include the latest data.
- **Rename** the measure.
- **Activate** or **Deactivate** one or more measures. For multiple measures, select **Change state**. Inactive measures don't get refreshed during a [scheduled refresh](schedule-refresh.md) and have the **Status** listed as **Skipped**, indicating that a refresh wasn't even attempted.
- **Tag** to [manage tags](work-with-tags-columns.md#manage-tags) for one or more measures.
- **Delete** one or more measures.
- [**Schedule**](measures-schedule.md) to customize schedules for measures.
- **Columns** to [customize the columns](work-with-tags-columns.md#customize-columns) that display.
- **Filter** to [filter on tags](work-with-tags-columns.md#filter-on-tags).
- **Search name** to search by measure name.
- [**Disable auto cleanup**](#automated-deactivation-of-unused-measures).

## Automated deactivation of unused measures

To optimize refresh performance, the system automatically deactivates unused measures every day. Unused measures are measures that aren't used in exports, other measures, or segments and created more than 45 days ago.

> [!NOTE]
> Exclude measures used in Customer Insights - Journey from the deactivation process. Go to [Specify measures that never expire](#specify-measures-that-never-expire).

Admins can delete these deactivated measures if they're no longer needed or reactivate them if they intend to use them again. Alternatively, admins can [specify measures that are excluded from the automated deactivation](#specify-measures-that-never-expire).

Deactivated measures don't refresh automatically when the system refreshes. They're tagged with **SystemDeactivated** when updated by automated cleanup.

### Specify measures that never expire

To avoid automated deactivation if a measure is no longer in use, admins can mark these segments.

1. Go to the **Insights** > **Measures** page and select a measure.

1. In the command bar, select **Never expires**.

1. Confirm the selection.

## Manage the number of active measures

When you approach or exceed the number of active measures based on the [service limits](service-limits.md), you might experience the following:

- Typical system refresh time is slower
- Running or refreshing individual measures is slower
- Refresh failures indicating out of memory

The complexity of your measures can also impact performance. To help you prevent performance issues, you get notifications or warnings when you approach, reach, or exceed the total number of active measures. These messages display on the **Measures** list page. If you encounter these messages or symptoms, see the following recommendations.

1. Delete old or no longer relevant measures even if they're static or inactive.
1. [Schedule individual measures](measures-schedule.md) to run weekly or monthly during slow business days (such as the weekend) instead of daily.

[!INCLUDE [footer-include](includes/footer-banner.md)]
