---
title: Recurring activity bulk deletion
description: "For administrators: Recurring bulk deletion system jobs for Dynamics 365 Customer Insights - Journeys."
ms.date: 08/23/2023
ms.topic: concept-article
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
---

# Recurring activity bulk deletion

## What is msdyncrm_mktactivity?

The **Marketing Activity** entity (msdyncrm_mktactivity) is used by Customer Insights - Journeys Services to send system updates. Each activity is processed by the Customer Insights - Journeys data plugin (Microsoft.Dynamics.Crm.MarketingPlugins.Plugins.Data), which then executes the designated action.

Activities are used across the entire Customer Insights - Journeys app. The number and frequency of activities depend on the scale and patterns of usage of your Dynamics 365 Customer Insights - Journeys implementation. After an activity is successfully executed, it is stored in Microsoft Dataverse, which, over time, can increase the database size.

## How are marketing activities automatically cleared?

To prevent the database size from increasing indefinitely, we have created recurring bulk deletion system jobs that delete old marketing activity entities. The bulk deletion jobs are automatically deployed and are executed once per day, clearing activities that are older than seven days. The bulk deletion jobs include:

- *Microsoft.Dynamics.Crm.Marketing.ActivityBulkDeleteJob* to clear marketing activities.
- *Microsoft.Dynamics.EventManagement.ActivityBulkDeleteJob* to clear event management-specific activities.

> [!div class="mx-imgBorder"]
> ![Deployed bulk activity deletion job on a customer instance.](media/bulk-activity-deletion.png)

## Options to manually clear the table

The marketing activity table varies in size, depending on your Customer Insights - Journeys usage. If you are creating a large number of marketing activities, you may want to clear the table more frequently than every seven days.

To clear the table more frequently, you can create additional recurring bulk deletion jobs. The table is safe to be truncated at any time. All data can be cleared, regardless of the age of the data. Data processing is synchronous; only successfully executed activities are stored.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
