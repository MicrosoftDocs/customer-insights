---
title: Connect an Azure Synapse Analytics data source (preview)
description: Use a database in Azure Synapse as a data source in Dynamics 365 Customer Insights.
ms.date: 11/21/2023
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Connect an Azure Synapse Analytics data source (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Azure Synapse Analytics is an enterprise analytics service that accelerates time to insights across data warehouses and big data systems. Azure Synapse Analytics brings together the best of SQL technologies used in enterprise data warehousing, Spark technologies used for big data, Data Explorer for log and time series analytics, Pipelines for data integration and ETL/ELT, and deep integration with other Azure services such as Power BI, Cosmos DB, and AzureML.

For more information, see [Azure Synapse overview](/azure/synapse-analytics/overview-what-is).

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Prerequisites

> [!NOTE]
> - Azure Synapse workspaces which have [firewall enabled](/azure/synapse-analytics/security/synapse-workspace-ip-firewall) are currently not supported.
> - The Azure Synapse workspace used as data source must be in the same tenant as the Customer Insights environment. Cross-tenant scenarios are not supported by Customer Insights.

> [!IMPORTANT]
> Make sure to set all **role assignments** as described.  

**In Customer Insights - Data**:

- You have an **Administrator** role. Learn more about [user permissions in Customer Insights](user-roles.md).

**In Azure**:

- An active Azure subscription.
  
- A user with an **Administrator** role in Customer Insights - Data needs the **User Access Administrator** role in the Azure subscription to grant the *service principal* access to Azure resources in the Customer Insights - Data UI. Otherwise, a user in Azure who has the **User Access Administrator** role must set following permissions. Learn more about the [User Access Administrator](/azure/role-based-access-control/built-in-roles#user-access-administrator) role and how to choose between [Owner vs User Access Administrator](/azure/role-based-access-control/role-assignments-steps#step-2-select-the-appropriate-role). The **Owner** implicitly has the **User Access Administrator** role.

- If using a new Azure Data Lake Storage Gen2 account, the *service principal* for Customer Insights - Data that is "Dynamics 365 AI for Customer Insights" needs **Storage Blob Data Contributor** permissions. Learn more about [connecting to an Azure Data Lake Storage with a service principal](connect-service-principal.md). The Data Lake Storage Gen2 **must have** [hierarchical namespace](/azure/storage/blobs/data-lake-storage-namespace) enabled.

- On the resource group the Azure Synapse workspace is located, the *service principal that is "Dynamics 365 AI for Customer Insights"* and the *user for Customer Insights* needs at least **Reader** permissions. For more information, see [Assign Azure roles using the Azure portal](/azure/role-based-access-control/role-assignments-portal).

- The *user* needs **Storage Blob Data Contributor** permissions on the Azure Data Lake Storage Gen2 account where the data is located and linked to the Azure Synapse workspace. Learn more about [using the Azure portal to assign an Azure role for access to blob and queue data](/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

- The *[Azure Synapse workspace managed identity](/azure/synapse-analytics/security/synapse-workspace-managed-identity)* needs **Storage Blob Data Contributor** permissions on the Azure Data Lake Storage Gen2 account where the data is located and linked to the Azure Synapse workspace. Learn more on [using the Azure portal to assign an Azure role for access to blob and queue data](/azure/storage/common/storage-auth-aad-rbac-portal) and [Storage Blob Data Contributor permissions](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

- On the Azure Synapse workspace, the *service principal for Customer Insights - Data that is "Dynamics 365 AI for Customer Insights" needs **Synapse Administrator** role assigned. The **user** needs at least a **Synapse Contributor** role assigned for the workspace. For more information, see [How to set up access control for your Synapse workspace](/azure/synapse-analytics/security/how-to-set-up-access-control).

- If your Customer Insights environment stores data in your [own Azure Data Lake Storage](own-data-lake-storage.md), the user who sets up the connection to Azure Synapse Analytics needs at least the built-in **Reader** role on the Data Lake Storage account. For more information, see [Assign Azure roles using the Azure portal](/azure/role-based-access-control/role-assignments-portal).

## Connect to the data lake database in Azure Synapse Analytics

1. Go to **Data** > **Data sources**.

1. Select **Add a data source**.

1. Choose the **Azure Synapse Analytics (Preview)** method.

   :::image type="content" source="media/data_sources_synapse.svg" alt-text="Dialog box to connect to Synapse Analytics data":::
  
1. Enter a **Name** for the data source and an optional **Description**.

1. Choose an [available connection](connections.md) to Azure Synapse Analytics or [create a new one](export-azure-synapse-analytics.md#set-up-connection-to-azure-synapse).

1. Choose a **Database** from the workspace connected in the selected Azure Synapse Analytics connection and select **Next**. Currently, we only support the database type *Lake database*.

1. Select the tables to ingest from the connected database and select **Next**.

1. Optionally, choose the data tables to allow [data profiling](data-sources.md#data-profiling) on.

1. Select **Save** to apply your selection and start the ingestion of the data from your newly created data source linked to the Lake database tables in Azure Synapse Analytics. The **Data sources** page opens showing the new data source in **Refreshing** status.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, review the ingested data from the [**Data** > **Tables**](tables.md) page.

## Next steps

- [Data unification overview](data-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
