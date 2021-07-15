---
title: Export refined events
description: How to export refined events and base events.
ms.reviewer: mhart
ms.author: jusali
author: jusali
ms.date: 04/30/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# Export events

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

An event represents user behavior. It records when a user views a page (view event) or interacts with content(action event). When you can decide which properties of the data that you want to display in a report, this virtual view of the data is called a *refined event*. 

- You can export events and refined events to external storage. 
- The exports are a forward data stream. You can't refill the stream. 
- Exports have fixed schemas. If you add custom properties to an event, they won't be included. You'll need to create a new export.

## Prerequisites

Before setting up an export, you need to have access and an active subscription to the Azure portal. You'll need the storage account information during the export process. 

### Create an Azure Data Lake Storage Gen 2 accounts

1. Sign in to the Azure portal and [create a new storage account](/azure/storage/common/storage-account-create). 

1. Make sure that you enable **Hierarchical namespace** on the **Advanced** tab. 

   :::image type="content" source="media/enable-hierarchical-namespace.png" alt-text="Enable hierarchical namespace on the advanced tab.":::

1. Once it has been deployed, go to the newly created storage account. In the navigation pane, select **Settings** > **Access keys**. 

1. Copy the **Account name** and **Key** to use them when creating a new export.
   :::image type="content" source="media/storage-account-access-keys.png" alt-text="Access keys in a storage account.":::

## Export events

There are two ways to export events: 
- Go to **Data** > **Exports** and select **New export**.
- Go to **Data** > **Events**, select **More [...]** next to the event you want to export and select **Export** from the dropdown menu. 

You're guided through the steps to create an export:

1. Provide an **Export name**.

1. In the **Events selection** dropdown list, choose the base events and refined events to include in the export. 

1. Under **File structure**, select the cadence to create new files in the destination storage. Events are exported continuously as they arrive.

1. Select the format for your export. You can choose between **Common Data Model**, **CSV**, and **JSON** format. To use the export with other Dynamics 365 applications, we recommend using the Common Data Model format.

1. In the **Choose destination** step, specify the Azure Data Lake Storage Gen 2 location.
    1. **ADLS Gen 2 account name** is the name of the storage account you want to save the export to. 
    1. **Folder path** defines where the export should be stored in the file system and directory structure of the storage account.
    1. **Shared key** is available from the Azure portal for the storage account.

1. Review and confirm your selections.

## View and manage exports

Once you've set up an export, go to **Data** > **Exports** to view it. Select **More [...]** for any existing export to edit or delete it.


[!INCLUDE[footer-include](../includes/footer-banner.md)]