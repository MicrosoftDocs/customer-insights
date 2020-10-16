---
title: Export refined events
description: How to export refined and base events
ms.reviewer: ruthai
ms.author: v-salash
author: pickwick129
ms.date: 10/12/2020
ms.service: customer-insights
ms.subservice: 
ms.topic: conceptual
ms.manager: shellyha 
---

# Export refined events

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

An event records when a user views a page (view event) or interacts with content (action event). A refined event is virtual view of an event that you can use to adjust its properties. You can export both events and refined events to an external storage. An export is a forward data stream. You can't refill the stream. Additionally, exports have fixed schemas. If you add custom properties to an event, they won’t be included and you will need to create a new export.

## Prerequisite

Before export, be sure that you have access and an active subscription to the Azure portal. You'll need the storage account information during the export process. 

To get Azure Data Lake Storage (ADLS) settings
1. [Create a new storage account](https://docs.microsoft.com/azure/storage/common/storage-account-create). 
2. From the **Advanced** tab, enable **Hierachical namespace**. 
:::image type="content" source="media/ADLS.png" alt-text="Azure Data Lake Storage account setup":::
3. Once it has been deployed, go to the newly created storage account and from the navigation pane, go to **Settings** > **Access keys**. 
4. Copy the **Account name** and **Key** to use them in **Export** settings in engagement insights capability.

## Export a refined event

From the **Events** page, select **...** next to the event you want to export and select **Export** from the drop-down menu. You are guided through the five steps of export creation:

1. Choose a **Name** for the export.
2. Select an event for export and an export cadence. The cadence informs how often an immutable folder with your event's information is created in Azure Data Lake Storage.
3. Select the format for your export.
4. Specify the Azure Data Lake Storage location and your credentials.
5. Review and confirm your selections.

Once you've set up an export, you can view it by navigating to **Admin** > **Data** > **Exports**. Use the **...** selections on the page to edit or delete an existing export.
