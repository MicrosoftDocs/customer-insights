---
title: "(Preview) - Export Customer Insights data to Azure Synapse Analytics"
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

# Overview

You can now use your Customer Insights data within [Azure Synapse Analytics](https://docs.microsoft.com/en-us/azure/synapse-analytics/overview-what-is).

# Prerequisites

To configure the connection from Customer Insights to Azure Synapse Analytics and to use your Customer Insights data within Azure Synapse Analytics, the following prerequisites must be met:

  > [!NOTE]
  > Using Customer Insights data in Azure Synapse Analytics is only working if the following prerequisites, in particular the role assignments, are respected.  

## Prerequisites in Customer Insights

* You have an **Administrator** role in Audience Insights. Learn more about [setting user permissions in audience insights](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/permissions#assign-roles-and-permissions)

## Prerequisites in Azure

* You have an active Azure Subscription

* If using a new Azure Data Lake Storage Gen2 account, the service principal for Audience Insights and the user needs to be assigned **Storage Blob Contributor** permissions. Learn more on [how to connect to an Azure Data Lake Storage Gen2 account with an Azure service principal for audience insights](https://docs.microsoft.com/en-us/dynamics365/customer-insights/audience-insights/connect-service-principal). The Data Lake Storage Gen2 **must have** [hierarchical namespace](https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-namespace) enabled.

* On the Resource Group the Synapse workspace is located, the service principal for Audience Insights needs to be assigned at least **Reader** permissions. Learn more on [Assign Azure roles using the Azure portal](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).

* On the Resource Group the Synapse workspace is located, user needs to be assigned at least **Reader** permissions. Learn more on [Assign Azure roles using the Azure portal](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).

* On Azure Data Lake Storage Gen2 account where the data is located and linked to the Synapse workspace, the user needs to be assigned **Storage Blob Data Contributor** permissions. Learn more on [Use the Azure portal to assign an Azure role for access to blob and queue data](https://docs.microsoft.com/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

* On Azure Data Lake Storage Gen2 account where the data is located and linked to the Synapse workspace, the [Azure Synapse workspace managed identity](https://docs.microsoft.com/azure/synapse-analytics/security/synapse-workspace-managed-identity) needs to be assigned **Storage Blob Data Contributor** permissions. Learn more on [Use the Azure portal to assign an Azure role for access to blob and queue data](https://docs.microsoft.com/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

* On Synapse workspace, the service principal for Audience Insight needs **Synapse Administrator** role assigned. Learn more on [How to set up access control for your Synapse workspace](https://docs.microsoft.com/en-us/azure/synapse-analytics/security/how-to-set-up-access-control).

# Set up the connection to Azure Synapse Analytics from within Customer Insights

## Configure a connection
1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Azure Synapse Analytics** or click the **Set up** on the **Azure Synapse Analytics** tile to configure the connection.

1. Give your connection a recognizable name in the Display name field. The name and the type of the connection describes this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Select or search for the subscription you want the Customer Insights data use in. As soon as a subscription is selected, you can also select Workspace, Storage account and Container.

1. Select **Save** to save the connection.

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add export**.

1. In the **Connection for export** field, choose a connection from the **Azure Synapse Analytics** section. If you don't see this section name, there are no connections of this type available to you.

1. Provide a recognizable **Display name** for your export and a **Database name**.

1. Select which entities you want to export to Azure Synapse Analytics.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab).
You can also [export data on demand](export-destinations.md#run-exports-on-demand).

## Update an Export

1. Go to **Data** > **Exports**.

1. Click  **Edit** on the export which should be updated.

* **Add** or **Remove** entities from the selection. If entities are removed from the selection they won't get deleted on the Azure Synapse database. But on the subsequent data refreshes the entities won't get updated on Synapse.

* **Changing** the **Database Name** will create a new Database on Synapse. The Database withthe previous name in the configuration won't receive any updates in subsequent refreshes.

## FAQ

### Working with Audience Insights data in Synapse

* **Question**: The setup is working fine but when other users are granted access to the workspace they can't query the database containing the Audience Insights data.
* **Answer**: The user needs **Storage Blob Contributor** role assigned on the storage the data is exported to in addition to the Synapse workspace permissions.
