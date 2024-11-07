---
title: "Export data to Azure Synapse Analytics (preview)"
description: "Learn how to configure the connection to Azure Synapse Analytics."
ms.date: 11/07/2024
ms.reviewer: mhart
ms.topic: how-to
author: pkieffer
ms.author: philk
---

# Export data to Azure Synapse Analytics (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

[!INCLUDE [azure-ad-to-microsoft-entra-id](../journeys/includes/azure-ad-to-microsoft-entra-id.md)]

Azure Synapse is an analytics service that accelerates time to insight across data warehouses and big data systems. You can ingest and use data from Dynamics 365 Customer Insights - Data in [Azure Synapse](/azure/synapse-analytics/overview-what-is).

[!INCLUDE [data-out-azure-synapse-link](includes/data-out-azure-synapse-link.md)]

## Prerequisites

> [!NOTE]
> Make sure to set all **role assignments** as described.

- In Customer Insights - Data, your Microsoft Entra ID account must have an [Administrator role](user-roles.md#admin).

In Azure:

- An active Azure subscription.

- A user with an **Administrator** role in Customer Insights - Data needs the **User Access Administrator** role in the Azure subscription to grant the *service principal* access to Azure resources in the Customer Insights - Data UI. Otherwise, a user in Azure who has the **User Access Administrator** role must set following permissions. Learn more about the [User Access Administrator](/azure/role-based-access-control/built-in-roles#user-access-administrator) role and how to choose between [Owner vs User Access Administrator](/azure/role-based-access-control/role-assignments-steps#step-2-select-the-appropriate-role). The **Owner** implicitly has the **User Access Administrator** role.

- If using a new Azure Data Lake Storage Gen2 account, the [service principal for Customer Insights - Data](connect-service-principal.md) has **Storage Blob Data Contributor** permissions. The Data Lake Storage Gen2 **must have** [hierarchical namespace](/azure/storage/blobs/data-lake-storage-namespace) enabled.

- On the resource group with the Azure Synapse workspace, the *service principal* and the *user with admin permissions in Customer Insights - Data* needs at least **Reader** [permissions](/azure/role-based-access-control/role-assignments-portal).

- The *user with admin permissions in Customer Insights - Data* has **Storage Blob Data Contributor** permissions on the Azure Data Lake Storage Gen2 account where the data is located and linked to the Azure Synapse workspace. Learn more about [using the Azure portal to assign an Azure role for access to blob and queue data](/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

- The *[Azure Synapse workspace managed identity](/azure/synapse-analytics/security/synapse-workspace-managed-identity)* has **Storage Blob Data Contributor** permissions on the Azure Data Lake Storage Gen2 account where the data is located and linked to the Azure Synapse workspace. Learn more on [using the Azure portal to assign an Azure role for access to blob and queue data](/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

- On the Azure Synapse workspace, the *service principal for Customer Insights - Data* has **Synapse Administrator** [role assigned](/azure/synapse-analytics/security/how-to-set-up-access-control).

- If your Customer Insights - Data environment stores data in your [own Azure Data Lake Storage](own-data-lake-storage.md), the user who sets up the connection to Azure Synapse Analytics needs at least the built-in **Reader** role on the Data Lake Storage account. For more information, see [Assign Azure roles using the Azure portal](/azure/role-based-access-control/role-assignments-portal).

## Known limitation

- Azure Synapse export doesn't support incremental refresh for data sources if an environment uses a custom Azure Data Lake for data storage.
- [Power Query data sources](connect-power-query.md) as input tables are only supported if your environment stores data in your [own Azure Data Lake Storage](own-data-lake-storage.md).
- Enabling public access to your own storage account after [setting up an Azure Private Link](private-link.md) won't work. Private Link is only supported if you disable public access to the storage account. Remove the Private Link setup to re-enable public access.
- This export works only for CSV formatted files.

## Set up connection to Azure Synapse

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Azure Synapse Analytics**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describes this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Select or search for the subscription you want to use the Customer Insights data in. As soon as you select a subscription, you can also select **Workspace**, **Storage account**, and **Container**.

1. Optionally, if your storage account is behind a firewall, select **Enable Private Link**. For more information, go to [Private Links](private-link.md).

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)] To configure the export with a shared connection, you need at least **Contributor** permissions in Customer Insights - Data.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Azure Synapse Analytics section. Contact an administrator if no connection is available.

1. Provide a recognizable **Display name** for your export and a **Database name**. The export will create a new [Azure Synapse lake database](/azure/synapse-analytics/database-designer/concepts-lake-database) in the workspace defined in the connection.

1. Select which tables you want to export to Azure Synapse Analytics.
   > [!NOTE]
   > Data sources based on a [Common Data Model folder](connect-common-data-model.md) aren't supported.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

To query data in Synapse Analytics, you need **Storage Blob Data Reader** access to the destination storage on the workspace of exports.

## Update an export

1. Go to **Data** > **Exports**.

1. Select **Edit** on the export you want to update.

   - **Add** or **Remove** tables from the selection. If you remove tables from the selection, they stay in the Synapse Analytics database. However, future data refreshes won't update the removed tables in that database.

   - **Changing the Database Name** creates a new Synapse Analytics database. The old database won't receive any updates in future refreshes.

[!INCLUDE [footer-include](includes/footer-banner.md)]
