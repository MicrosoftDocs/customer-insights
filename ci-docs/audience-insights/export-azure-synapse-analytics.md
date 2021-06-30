---
title: "Export Customer Insights data to Azure Synapse Analytics"
description: "Learn how to configure the connection to Azure Synapse Analytics."
ms.date: 04/12/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: stefanie-msft
ms.author: sthe
manager: shellyha
---

# Export data to Azure Synapse Analytics (Preview)

Azure Synapse is an analytics service that accelerates time to insight across data warehouses and big data systems. You can ingest and use your Customer Insights data in [Azure Synapse](/azure/synapse-analytics/overview-what-is).

## Prerequisites

The following prerequisites must be met to configure the connection from Customer Insights to Azure Synapse.

> [!NOTE]
> Make sure to set all **role assignments** as described.  

## Prerequisites in Customer Insights

* You have an **Administrator** role in audience insights. Learn more about [setting user permissions in audience insights](permissions.md#assign-roles-and-permissions)

In Azure: 

- An active Azure subscription.

- If using a new Azure Data Lake Storage Gen2 account, the *service principal for audience insights* needs **Storage Blob Data Contributor** permissions. Learn more on [connecting to an Azure Data Lake Storage Gen2 account with Azure service principal for audience insights](connect-service-principal.md). The Data Lake Storage Gen2 **must have** [hierarchical namespace](/azure/storage/blobs/data-lake-storage-namespace) enabled.

- On the resource group the Azure Synapse workspace is located, the *service principal* and the *user for audience insights* needs to be assigned at least **Reader** permissions. For more information, see [Assign Azure roles using the Azure portal](/azure/role-based-access-control/role-assignments-portal).

- The *user* needs **Storage Blob Data Contributor** permissions on the Azure Data Lake Storage Gen2 account where the data is located and linked to the Azure Synapse workspace. Learn more about [using the Azure portal to assign an Azure role for access to blob and queue data](/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

- The *[Azure Synapse workspace managed identity](/azure/synapse-analytics/security/synapse-workspace-managed-identity)* needs **Storage Blob Data Contributor** permissions on the Azure Data Lake Storage Gen2 account where the data is located and linked to the Azure Synapse workspace. Learn more on [using the Azure portal to assign an Azure role for access to blob and queue data](/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

- On the Azure Synapse workspace, the *service principal for audience insights* needs **Synapse Administrator** role assigned. For more information, see [How to set up access control for your Synapse workspace](/azure/synapse-analytics/security/how-to-set-up-access-control).

## Set up the connection and export to Azure Synapse

### Configure a connection

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Azure Synapse Analytics** or select the **Set up** on the **Azure Synapse Analytics** tile to configure the connection.

1. Give your connection a recognizable name in the Display name field. The name and the type of the connection describes this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Select or search for the subscription you want to use the Customer Insights data in. As soon as a subscription is selected, you can also select **Workspace**, **Storage account**, and **Container**.

1. Select **Save** to save the connection.

### Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add export**.

1. In the **Connection for export** field, choose a connection from the **Azure Synapse Analytics** section. If you don't see this section name, there are no [connections](connections.md) of this type available to you.

1. Provide a recognizable **Display name** for your export and a **Database name**.

1. Select which entities you want to export to Azure Synapse Analytics.
   * **Note**:  Data Sources based on [Common Data Model folder](connect-common-data-model) are not supported.


2. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand).

### Update an export

1. Go to **Data** > **Exports**.

1. Select **Edit** on the export you want to update.

   - **Add** or **Remove** entities from the selection. If entities are removed from the selection, they aren't deleted from the Synapse Analytics database. However, future data refreshes won't update the removed entities in that database.

   - **Changing the Database Name** creates a new Synapse Analytics database. The database with the name that was configured before won't receive any updates in future refreshes.
