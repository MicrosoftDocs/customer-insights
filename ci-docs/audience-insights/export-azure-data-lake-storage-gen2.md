---
title: "Export Customer Insights data to Azure Data Lake Storage Gen2"
description: "Learn how to configure the connection to Azure Data Lake Storage Gen2."
ms.date: 02/04/2021
ms.reviewer: sthe
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for Azure Data Lake Storage Gen2 (preview)

Store your Customer Insights data in Azure Data Lake Storage Gen2 or use it to transfer your data to other applications.

## Configure the connector for Azure Data Lake Storage Gen2

1. In audience insights, go to **Admin** > **Export destinations**.

1. Under **Azure Data Lake Storage Gen2**, select **Set up**.

1. Give your destination a recognizable name in the **Display name** field.

1. Enter **Account name**, **Account key**, and **Container** for your Azure Data Lake Storage Gen2.
    - To learn how to create a storage account to use with Azure Data Lake Storage Gen2, see [Create storage account](/azure/storage/blobs/create-data-lake-storage-account). 
    - To learn more about how to find the Azure Data Lake Gen2 storage account name and account key, see [Manage storage account settings in the Azure portal](/azure/storage/common/storage-account-manage).

1. Select **Next**.

1. Select the box next to each of the entities you want to export to this destination.

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md#export-data-on-demand). The export will also run with every [scheduled refresh](system.md#schedule-tab).