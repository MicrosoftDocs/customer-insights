---
title: "Export Customer Insights data to Azure Data Lake Storage Gen2"
description: "Learn how to configure the connection to Azure Data Lake Storage Gen2."
ms.date: 10/06/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: stefanie-msft
ms.author: sthe
manager: shellyha
---

# Export segment list and other data to Azure Data Lake Storage Gen2 (preview)

Store your Customer Insights data in a Data Lake Storage Gen2 account or use it to transfer your data to other applications.

## Known limitations

1. For Azure Data Lake Storage Gen2 you can choose between [Standard performance and Premium performance tier](/azure/storage/blobs/create-data-lake-storage-account) when you are creating a storage account for your data lake. If you choose the Premium performance tier, select the premium block blobs as account type. 


## Set up the connection to Azure Data Lake Storage Gen2 


1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Azure Data Lake Gen 2** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter **Account name**, **Account key**, and **Container** for your Azure Data Lake Storage Gen2.
    - To learn how to create a storage account to use with Azure Data Lake Storage Gen2, see [Create storage account](/azure/storage/blobs/create-data-lake-storage-account). 
    - To learn more about Azure Data Lake Gen2 storage account name and account key, see [Manage storage account settings in the Azure portal](/azure/storage/common/storage-account-manage).

1. Select **Save** to complete the connection. 

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add export**.

1. In the **Connection for export** field, choose a connection from the **Azure Data Lake** section. If you don't see this section name, there are no connections of this type available to you.

1. Select the box next to each of the entities you want to export to this destination.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-exports-on-demand). 

Exported data is stored in the Azure Data Lake Gen 2 storage container you configured. 

[!INCLUDE[footer-include](../includes/footer-banner.md)]
