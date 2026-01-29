---
title: Sync data tables into the segment builder
description: Learn how to sync data tables into the segment builder in the Customer Insights - Journeys.
ms.date: 04/03/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Sync data tables into the segment builder

The Customer Insights - Journeys segment builder allows you to sync data tables without relying on the help of administrators. This saves you time when setting up segments, letting you directly add data tables to Dynamics 365 Customer Insights - Journeys without using the Dynamics 365 admin center.

> [!NOTE]
> 1. Real-time marketing doesn't support adding virtual tables. Trying to add these tables using the "+Add table" button won't reveal the tables in the table list. This is because virtual tables aren't synced on the backend.
> 2. Adding tables to the segment builder increases Dataverse database storage consumption because additional data must be stored and maintained in your environment. Only add tables when required, and remove any tables that are not in use. After enabling new tables, monitor your Dataverse storage consumption.

**Example**: You want to create a segment using attributes from the Fax table in Dataverse, but you notice that Fax isn’t available in your related data tables.

To add the Fax table directly from the Customer Insights - Journeys app, go to the Customer Insights - Journeys segment builder and create or select a segment. Then, in the **Elements** side pane, select **+Add table** next to **Related tables**. Search for the Fax table, select the check box next to it, then select **Next** to add the table to the segment builder. 

> [!div class="mx-imgBorder"]
> ![Add table to segment builder](media/real-time-marketing-add-table-to-segment-builder.png "Add table to segment builder")

After you add the new table, you can use the attributes from Fax immediately in your segment creation.

> [!div class="mx-imgBorder"]
> ![use attributes right away](media/real-time-marketing-use-attributes-right-away.png "use attributes right away")

> [!NOTE]
> It can take up to 24 hours for a data table to be synchronized into the system. At this time, the segment member size estimate and preview features are not available. You cannot view the segment membership until the table is synchronized into the system.  

[!INCLUDE [footer-include](./includes/footer-banner.md)]
