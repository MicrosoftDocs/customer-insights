---
title: "Export data to Azure Data Lake Storage Gen2 (preview)"
description: "Learn how to configure the connection to Azure Data Lake Storage Gen2."
ms.date: 10/06/2021
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: stefanie-msft
ms.author: sthe
manager: shellyha
---

# Export data to Azure Data Lake Storage Gen2 (preview)

Store your Customer Insights data in a Data Lake Storage Gen2 account or use it to transfer your data to other applications.

## Prerequisites

- A [storage account to use with Azure Data Lake Gen2](/azure/storage/blobs/create-data-lake-storage-account). To find the storage account name and key, see [Manage storage account settings in the Azure portal](/azure/storage/common/storage-account-manage).
- An [Azure Blob Storage container](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container).

## Known limitations

- For Azure Data Lake Storage Gen2, choose between [Standard performance and Premium performance tier](/azure/storage/blobs/create-data-lake-storage-account). If you choose the Premium performance tier, select the [premium block blobs as account type](/azure/storage/common/storage-account-overview#types-of-storage-accounts).

## Set up connection to Azure Data Lake Storage Gen2

You must be an [administrator](permissions.md) in Customer Insights to add a connection.

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Azure Data Lake Gen 2**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter **Account name**, **Account key**, and **Container** for your Azure Data Lake Storage Gen2.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

## Configure an export

To configure this export, you must have [permission](export-destinations.md#set-up-a-new-export) for this connection type.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Azure Data Lake section. Contact an administrator if one is not available.

1. Enter a name for the export.

1. Enter the folder name for the Azure Data Lake Storage Gen2 storage.

1. Select the box next to each of the entities you want to export to this destination.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand).

Exported data is stored in the Azure Data Lake Gen 2 storage container you configured.

> [!TIP]
> Export of entities that contain a large amount of data can lead to multiple CSV files in the same folder for each export. Splitting exports happens for performance reasons to minimize the time it takes for an export to complete.

[!INCLUDE [footer-include](includes/footer-banner.md)]
