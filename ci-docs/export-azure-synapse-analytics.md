---
title: "Export data to Azure Synapse Analytics (preview)"
description: "Learn how to configure the connection to Azure Synapse Analytics."
ms.date: 04/11/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: stefanie-msft
ms.author: sthe
manager: shellyha
---

# Export data to Azure Synapse Analytics (preview)

Azure Synapse is an analytics service that accelerates time to insight across data warehouses and big data systems. You can ingest and use your Customer Insights data in [Azure Synapse](/azure/synapse-analytics/overview-what-is).

## Prerequisites

> [!NOTE]
> Make sure to set all **role assignments** as described.

- In Customer Insights, your Azure Active Directory (AD) user account must have an [Administrator role](permissions.md#assign-roles-and-permissions).

In Azure:

- An active Azure subscription.

- If using a new Azure Data Lake Storage Gen2 account, the [service principal for Customer Insights](connect-service-principal.md) has **Storage Blob Data Contributor** permissions. The Data Lake Storage Gen2 **must have** [hierarchical namespace](/azure/storage/blobs/data-lake-storage-namespace) enabled.

- On the resource group where the Azure Synapse workspace is located, the *service principal* and the *Azure AD user with admin permissions in Customer Insights* must be assigned at least **Reader** [permissions](/azure/role-based-access-control/role-assignments-portal).

- The *Azure AD user with admin permissions in Customer Insights* has **Storage Blob Data Contributor** permissions on the Azure Data Lake Storage Gen2 account where the data is located and linked to the Azure Synapse workspace. Learn more about [using the Azure portal to assign an Azure role for access to blob and queue data](/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

- The *[Azure Synapse workspace managed identity](/azure/synapse-analytics/security/synapse-workspace-managed-identity)* has **Storage Blob Data Contributor** permissions on the Azure Data Lake Storage Gen2 account where the data is located and linked to the Azure Synapse workspace. Learn more on [using the Azure portal to assign an Azure role for access to blob and queue data](/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

- On the Azure Synapse workspace, the *service principal for Customer Insights* has **Synapse Administrator** [role assigned](/azure/synapse-analytics/security/how-to-set-up-access-control).

## Set up connection to Azure Synapse

You must be an [administrator](permissions.md) in Customer Insights to add a connection.

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Azure Synapse Analytics**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describes this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Select or search for the subscription you want to use the Customer Insights data in. As soon as a subscription is selected, you can also select **Workspace**, **Storage account**, and **Container**.

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Save** to complete the connection.

## Configure an export

To configure this export, you must have [permission](export-destinations.md#set-up-a-new-export) for this connection type. To configure the export with a shared connection, you need at least **Contributor** permissions in Customer Insights.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Azure Synapse Analytics section. Contact an administrator if one is not available.

1. Provide a recognizable **Display name** for your export and a **Database name**.

1. Select which entities you want to export to Azure Synapse Analytics.
   > [!NOTE]
   > Data sources based on a [Common Data Model folder](connect-common-data-model.md) aren't supported.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand).

To query data that was exported to Synapse Analytics, you need **Storage Blob Data Reader** access to the destination storage on the workspace of exports.

## Update an export

1. Go to **Data** > **Exports**.

1. Select **Edit** on the export you want to update.

   - **Add** or **Remove** entities from the selection. If entities are removed from the selection, they aren't deleted from the Synapse Analytics database. However, future data refreshes won't update the removed entities in that database.

   - **Changing the Database Name** creates a new Synapse Analytics database. The database with the name that was configured before won't receive any updates in future refreshes.
