---
title: "Connect Common Data Model data to an Azure Data Lake account"
description: "Work with Common Data Model data using Azure Data Lake Storage."
ms.date: 02/22/2022

ms.subservice: audience-insights
ms.topic: how-to
author: matgos
ms.author: adkuppa
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-data-sources
  - ci-create-data-source
  - ci-attach-cdm
  - customerInsights
---

# Connect to data in Azure data lake storage

This article provides information on how to ingest data from Azure Data Lake including data from a Common Data Model folder using your Azure Data Lake Storage Gen2 account.

## Important considerations

- Data in your Azure Data Lake must follow the Common Data Model standard. For more information, see [The Common Data Model manifest](https://docs.microsoft.com/common-data-model/sdk/manifest).

- Data ingestion supports Azure Data Lake *Gen2* storage accounts exclusively. You can't use Azure Data Lake Gen1 storage accounts to ingest data.

- The Azure Data Lake storage account must have [hierarchical namespace enabled](/azure/storage/blobs/data-lake-storage-namespace).

- To authenticate with an Azure service principal, make sure it's configured in your tenant. For more information, see [Connect audience insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md).

- The Azure Data Lake you want to connect and ingest data from must be in the same Azure region as the Dynamics 365 Customer Insights environment. Connections to a Common Data Model folder from a data lake in a different Azure region is not supported. To know the Azure region of the environment, go to **Admin** > **System** > **About** in audience insights.

- Data stored in online services may be stored in a different location than where data is processed or stored in Dynamics 365 Customer Insights. By importing or connecting to data stored in online services, you agree that data can be transferred to and stored with Dynamics 365 Customer Insights. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

- One of the following roles must be assigned to the storage account or container. For more information, see [Grant permissions to the service principal to access the storage account](connect-service-principal.md#grant-permissions-to-the-service-principal-to-access-the-storage-account).
  - Storage Blob Data Reader
  - Storage Blob Data Owner
  - Storage Blob Data Contributor

## Prerequisites
- Obtain the container name and folder path for where the model.json or manifest.json file resides.

## Connect to Azure data lake storage
  
1. Go to **Data** > **Data sources**.

1. Select **Add data source**.

1. Select **Azure data lake storage**.

   :::image type="content" source="media/data_sources_ADLS.png" alt-text="Dialog box to enter connection details for Azure Data Lake.":::

1. Enter a **Name** for the data source and an optional **Description**.

1. Choose your preferred option for **Connect your storage using**. For a resource or a subscription-based option for authentication, see [Connect audience insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md).

   - **Azure resource**: Enter the **Resource Id**.
   - **Azure subscription**: Select the **Subscription** and then the **Resource group** and **Storage account**.
   - **Account key**: Enter the **Account name** and **Account key**.

1. To enable an Azure private link, select **Enable Private link**. For more information, see  [What is Azure Private Link?](/azure/private-link/private-link-overview).

<!--- Need more information --->

1. Enter the name of the **Container** that contains the model.json or manifest.json file to import data from, and select **Next**.
   > [!NOTE]
   > Any model.json or manifest.json file associated with another data source in the environment won't show in the list. However, the same model.json or manifest.json file can be used for data sources in multiple environments.

1. Navigate to the folder containing the model.json or manifes.cdm.json file.

1. If you want to edit the entities in a JSON editing interface, select to the left of the json file name and then select **Edit schema**. Make changes and select **Save**.

1. Select the json file and select **Next**. A list of available entities displays.

   :::image type="content" source="media/review-entities.png" alt-text="Dialog box to select entities":::

1. Select the entities you want to include.

   :::image type="content" source="media/deltalake_required.png" alt-text="Dialog box showing Required for Primary key":::

1. For selected entities where a primary key has not been defined, **Required** displays under **Primary key**. For each of these entities:
   1. Select **Required**. The **Edit entity** panel displays.
   1. Choose the **Primary key**.
   1. Optionally, change the partition pattern.
   1. Select **X** to save and close the panel.

1. To enable analytics and other capabilities, select **Attributes**. Select **Data profiling** for the whole entity or for specific attributes and then select **Done**. By default, no entity is enabled for data profiling.

   :::image type="content" source="media/dataprofiling-entities.png" alt-text="Dialog box to select data profiling.":::

1. To enable an incremental refresh, see [Incremental refresh for Azure data lake and Databricks data sources](data-sources-incremental-refresh.md).

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

## Edit an Azure data lake storage data source

You can update the *Connect to storage account using* option from an account key connection to a resource-based or a subscription-based connection. For more information, see [Connect audience insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md). To connect to a different container from your storage account, or change the account name, [create a new data source connection](#connect-to-azure-data-lake-storage).

1. Go to **Data** > **Data sources**.

1. Next to the data source you'd like to update, select the ellipsis.

1. Select the **Edit** option from the list.

   :::image type="content" source="media/data_sources_edit_ADLS.png" alt-text="Dialog box to edit Azure data lake data source.":::

1. Optionally, you can update from an account key connection to a resource-based or a subscription-based connection. For more information, see [Connect audience insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md). You can't change **Container** information when updating the connection.

   > [!NOTE]
   > One of the following roles must be assigned to the storage account or container:

   > - Storage Blob Data Reader
   > - Storage Blob Data Owner
   > - Storage Blob Data Contributor

1. Optionally, choose a different model.json or manifest.json file with a different set of entities from the container.

1. Optionally, you can select additional entities to ingest. You can also remove any already selected entities if there are no dependencies.

   > [!IMPORTANT]
   > If there are dependencies on the existing model.json or manifest.json file and the set of entities, you'll see an error message and can't select a different model.json or manifest.json file. Remove those dependencies before changing the model.json or manifest.json file or create a new data source with the model.json or manifest.json file that you want to use to avoid removing the dependencies.

1. Optionally, you can select additional attributes or entities to enable data profiling on or disable already selected ones.

1. Click **Save** to apply your changes and return to the **Data sources** page.
