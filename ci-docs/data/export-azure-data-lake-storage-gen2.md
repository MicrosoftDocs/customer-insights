---
title: "Export data to Azure Data Lake Storage Gen2 (preview)"
description: "Learn how to configure the connection to Azure Data Lake Storage Gen2."
ms.date: 02/01/2024
ms.reviewer: mhart
ms.topic: how-to
author: pkieffer
ms.author: nikeller
---

# Export data to Azure Data Lake Storage Gen2 (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Store your data from Dynamics 365 Customer Insights - Data in a Data Lake Storage Gen2 account or use it to transfer your data to other applications.

[!INCLUDE [data-out-azure-synapse-link](includes/data-out-azure-synapse-link.md)]

## Prerequisites

- An [Azure Blob Storage account with a container](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container).
- User who sets up the connection must have the permission to access the content of the container. For example, a [Blob Storage Contributor](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) role.
- The [Customer Insights Service Principal](connect-service-principal.md) has write permissions on the container. For example, a [Blob Storage Contributor](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) role.

## Known limitations

- For Azure Data Lake Storage Gen2, choose between [Standard performance and Premium performance tier](/azure/storage/blobs/create-data-lake-storage-account). If you choose the Premium performance tier, select the [premium block blobs as account type](/azure/storage/common/storage-account-overview#types-of-storage-accounts).
- Enabling public access to your own storage account after [setting up managed identities for Azure resources](private-link.md) won't work. Managed identities is only supported if you disable public access to the storage account. Remove the managed identities setup to re-enable public access.
- This export works only for CSV formatted files.

## Set up connection to Azure Data Lake Storage Gen2

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Azure Data Lake Gen 2**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter **Subscription**, **Resource group**, **Storage account**, and **Container** for your Azure Data Lake Storage Gen2.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Azure Data Lake section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Enter the folder name for the Azure Data Lake Storage Gen2 storage.

1. Select the box next to each of the tables you want to export to this destination.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

Exported data is stored in the Azure Data Lake Gen 2 storage container you configured.

> [!TIP]
> Export of tables that contain a large amount of data can lead to multiple CSV files in the same folder for each export. Splitting exports happens for performance reasons to minimize the time it takes for an export to complete.

[!INCLUDE [footer-include](includes/footer-banner.md)]
