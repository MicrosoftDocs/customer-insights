---
title: "Export data to Azure Data Lake Storage Gen2"
description: "Learn how to configure the connection to Azure Data Lake Storage Gen2."
ms.date: 07/17/2025
ms.reviewer: alfergus
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
---

# Export data to Azure Data Lake Storage Gen2

Store your data from Dynamics 365 Customer Insights - Data in a Data Lake Storage Gen2 account or use it to transfer your data to other applications.

[!INCLUDE [data-out-azure-synapse-link](includes/data-out-azure-synapse-link.md)]

## Prerequisites

- An [Azure Blob Storage account with a container](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container).
- The user who sets up the connection needs permission to access the container content. For example, a [Blob Storage Contributor](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) role.
- The [Customer Insights Service Principal](connect-service-principal.md) needs write permission on the container. For example, a [Blob Storage Contributor](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) role.

## Known limitations

- For Azure Data Lake Storage Gen2, choose between [Standard performance and Premium performance tier](/azure/storage/blobs/create-data-lake-storage-account). If you choose the Premium performance tier, select the [premium block blobs as account type](/azure/storage/common/storage-account-overview#types-of-storage-accounts).
- You can't enable public access to your storage account after [setting up an Azure Private Link](private-link.md). Private Link works only if you disable public access to the storage account. Remove the Private Link setup to enable public access again.
- This export works only for CSV files.

## Set up connection to Azure Data Lake Storage Gen2

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Azure Data Lake Gen 2**.

1. Enter a recognizable name in the **Display name** field. The name and type of the connection describe this connection. Choose a name that explains the purpose and target of the connection.

1. Select who can use this connection. By default, only administrators can use it. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter the **Subscription**, **Resource group**, **Storage account**, and **Container** for your Azure Data Lake Storage Gen2.

1. If your storage account is behind a firewall, select **Enable Private Link**. For more information, see [Private Links](private-link.md).

1. Review [data privacy and compliance](connections.md#data-privacy-and-compliance), and select **I agree**.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Azure Data Lake section. Contact your admin if no connection is available.

1. Enter a name for the export.

1. Enter the folder name for the Azure Data Lake Storage Gen2 storage.

1. Select the box next to each of the tables you want to export to this destination.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

Exported data is stored in the Azure Data Lake Gen2 storage container you set up.

> [!TIP]
> Exporting tables with a large amount of data can create multiple CSV files in the same folder for each export. Splitting exports helps improve performance and minimize export time.

[!INCLUDE [footer-include](includes/footer-banner.md)]
