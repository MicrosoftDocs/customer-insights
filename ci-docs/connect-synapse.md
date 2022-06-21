---
title: "Ingest data from Azure Synapse Analytics"
description: "Use a database in Azure Synapse as a data source in Dynamics 365 Customer Insights."
ms.date: 03/25/2022
ms.reviewer: v-wendysmith
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
manager: shellyha
---

# Connect an Azure Synapse Analytics data source (preview)

Azure Synapse Analytics is an enterprise analytics service that accelerates time to insights across data warehouses and big data systems. Azure Synapse Analytics brings together the best of SQL technologies used in enterprise data warehousing, Spark technologies used for big data, Data Explorer for log and time series analytics, Pipelines for data integration and ETL/ELT, and deep integration with other Azure services such as Power BI, Cosmos DB, and AzureML.

For more information, see [Azure Synapse overview](/azure/synapse-analytics/overview-what-is).

## Prerequisites

> [!IMPORTANT]
> Make sure to set all **role assignments** as described.  

**In Customer Insights**:

* You have an **Administrator** role in Customer Insights. Learn more about [user permissions in Customer Insights](permissions.md#assign-roles-and-permissions).

**In Azure**:

- An active Azure subscription.

- If using a new Azure Data Lake Storage Gen2 account, the *service principal for Customer Insights* needs **Storage Blob Data Contributor** permissions. Learn more about [connecting to an Azure Data Lake Storage with a service principal for Customer Insights](connect-service-principal.md). The Data Lake Storage Gen2 **must have** [hierarchical namespace](/azure/storage/blobs/data-lake-storage-namespace) enabled.

- On the resource group the Azure Synapse workspace is located, the *service principal* and the *user for Customer Insights* needs to be assigned at least **Reader** permissions. For more information, see [Assign Azure roles using the Azure portal](/azure/role-based-access-control/role-assignments-portal).

- The *user* needs **Storage Blob Data Contributor** permissions on the Azure Data Lake Storage Gen2 account where the data is located and linked to the Azure Synapse workspace. Learn more about [using the Azure portal to assign an Azure role for access to blob and queue data](/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

- The *[Azure Synapse workspace managed identity](/azure/synapse-analytics/security/synapse-workspace-managed-identity)* needs **Storage Blob Data Contributor** permissions on the Azure Data Lake Storage Gen2 account where the data is located and linked to the Azure Synapse workspace. Learn more on [using the Azure portal to assign an Azure role for access to blob and queue data](/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

- On the Azure Synapse workspace, the *service principal for Customer Insights* needs **Synapse Administrator** role assigned. For more information, see [How to set up access control for your Synapse workspace](/azure/synapse-analytics/security/how-to-set-up-access-control).

## Connect to the data lake database in Azure Synapse Analytics

1. Go to **Data** > **Data sources**.

1. Select **Add data source**.

1. Choose the **Azure Synapse Analytics (Preview)** method.

   :::image type="content" source="media/data_sources_synapse.png" alt-text="Dialog box to connect to Synapse Analytics data":::
  
1. Enter a **Name** for the data source and an optional **Description**.

1. Choose an [available connection](connections.md) to Azure Synapse Analytics or create a new one.

1. Choose a **Database** from the workspace connected in the selected Azure Synapse Analytics connection and select **Next**.
> [Note]
> Only databases type ```Lake database``` are currently supported. 

1. Select the entities to ingest from the connected database and select **Next**.

1. Optionally, choose the data entities to allow data profiling on.

1. Select **Save** to apply your selection and start the ingestion of the data from your newly created data source linked to the Lake database tables in Azure Synapse Analytics. The **Data sources** page opens showing the new data source in **Refreshing** status.
