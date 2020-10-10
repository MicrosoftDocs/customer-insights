---
title: export refined events
description: How to export refined and base events
ms.reviewer: ruthaisabokhae
author: pickwick129
ms.author: v-salash
manager: shellyha
ms.date: 10/09/2020
ms.service: product-insights
ms.topic: how-to
ROBOTS: NOINDEX 
---

# Export refined events

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

You can export both events and refined events to an external storage. An export is a forward data stream. You can't refill the stream. Additionally, exports have fixed schemas. If you add custom properties <to an event?>, they won’t be included and you will need to create a new export.

## Export a refined event

From the **Events** page, select **...** next to the event you want to export and select **Export** from the drop-down menu. You are guided through the five steps of export creation:

1. Choose a **Name** for the export.
2. Select an event for export and an export cadence. The cadence informs how often an immutable folder with your event's information is created in Azure Data Lake Storage.
3. Select the format for your export.
4. Specify the Azure Data Lake Storage location and your credentials.
5. Review and confirm your selections.

Once you've set up an export, you can view it by navigating to **Admin** > **Data** > **Exports**. Use the **...** selections on the page to edit or delete an existing export.
