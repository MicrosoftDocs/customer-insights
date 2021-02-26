---
title: "Export destinations"
description: "Export data and manage export destinations."
ms.date: 07/21/2020
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Export destinations (preview) overview

The **Export destinations** page shows you all locations you've set up to export data to. You can also add new destinations for export. Additionally, it shows export currently available options. Get a quick overview, description, and find out what you can do with each extensibility option. Export unified profiles, measures, and segments to supported apps relevant for your business.

Go to **Admin** > **Export destinations** to find the following extensibility options:

- [Dynamics 365 Customer Card Add-in](customer-card-add-in.md)
- [Facebook Ads Manager connector](export-facebook.md)
- [Power Automate connector](export-power-automate.md)
- [Power Apps connector](export-power-apps.md)
- [Power BI connector](export-power-bi.md)
- [Adobe Campaign Standard](export-adobe-campaign-standard.md)
- [Adobe Experience Platform](export-adobe-experience-platform.md)
- [Autopilot](export-autopilot.md)
- [AdRoll](export-adroll.md)
- [DotDigital](export-dotdigital.md)
- [Dynamics 365 Sales](export-dynamics365-sales.md)
- [Dynamics 365 Marketing](export-dynamics365-marketing.md)
- [Azure Blob Storage](export-azure-blob-storage.md)
- [Azure Data Lake Storage Gen2](export-azure-data-lake-storage-gen2.md)
- [SendGrid](export-sendgrid.md)
- [LiveRamp&reg; connector](export-liveramp.md)
- [Bot for Microsoft Teams](export-teams-bot.md)
- [Mailchimp](export-mailchimp.md)
- [Customer Insights API](apis.md)

## Add a new export destination

To add export destinations, you have [administrator permissions](permissions.md). If you export to Microsoft services, we assume both services are in the same organization.

1. Go to **Admin** > **Export destinations**.

1. Switch to the **My export destinations** tab.

1. Select **Add destination** to create a new export destination.

1. In the **Add destination** pane, select the **Type** of export destination in the drop-down.

1. Provide the required details and select **Next** to create the export destination.

You can also select **Set up** on a tile on the **Discover** tab.

## View Export destinations

After creating export destinations, you'll find them in a table on the **My export destinations** tab. This table has three columns:

- **Display name**: The name you entered when creating the destination.
- **Type**: The export destination type you set when creating the destination.
- **Created**: The date you created the destination.

## Edit an export destination

1. Select the vertical ellipsis for the Export destination you want to edit.

   > [!div class="mx-imgBorder"]
   > ![Vertical ellipsis](media/export-destinations-page-ellipsis.png "Vertical ellipsis")

1. Select **Edit** from the dropdown menu.

1. Change the values that require update and select **Save**.

## Export data on demand

After configuring a connector for an export destination, exports will run with every [scheduled refresh](system.md#schedule-tab).

To export data without waiting for a scheduled refresh, go the **My export destinations** tab on **Admin** > **Export destinations**.

> [!div class="mx-imgBorder"]
> ![Vertical ellipsis](media/export-destinations-page-ellipsis.png "Vertical ellipsis")

- Select **Export** above the list to run the export to all export destinations simultaneously.
- Select the ellipsis (...) after a list item and then choose the **Export** option to run the export for a single export destination.

## Remove an Export destination

To remove an Export destination, start from the main **Export destinations** page.

1. Select the vertical ellipsis for the Export destination you want to remove.

   > [!div class="mx-imgBorder"]
   > ![Vertical ellipsis](media/export-destinations-page-ellipsis.png "Vertical ellipsis")

2. Select **Remove** from the dropdown menu.

3. Confirm the removal by selecting **Remove** on the confirmation screen.


[!INCLUDE[footer-include](../includes/footer-banner.md)]