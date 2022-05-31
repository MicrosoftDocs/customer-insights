---
title: "Connect Common Data Model data to an Azure Data Lake account"
description: "Work with Common Data Model data using Azure Data Lake Storage."
ms.date: 05/30/2022

ms.subservice: audience-insights
ms.topic: how-to
author: matgos
ms.author: mukeshpo
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-data-sources
  - ci-create-data-source
  - ci-attach-cdm
  - customerInsights
---

# Connect to data in Azure Data Lake storage

This article provides information on how to ingest data into Dynamics 365 Customer Insights using your Azure Data Lake Storage Gen2 account. Data ingestion can be full or incremental.

## Prerequisites

- Data ingestion supports Azure Data Lake *Gen2* storage accounts exclusively. You can't use Azure Data Lake Gen1 storage accounts to ingest data.

- The Azure Data Lake storage account must have [hierarchical namespace enabled](/azure/storage/blobs/data-lake-storage-namespace). The data must be stored in a hierarchical folder format that defines the root folder and has subfolders for each entity. The subfolders can have full data or incremental data folders.

- To authenticate with an Azure service principal, make sure it's configured in your tenant. For more information, see [Connect to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md).

- The Azure Data Lake you want to connect and ingest data from have to be in the same Azure region as the Dynamics 365 Customer Insights environment. Connections to a Common Data Model folder from a data lake in a different Azure region is not supported. To know the Azure region of the environment, go to **Admin** > **System** > **About** in Customer Insights.

- Data stored in online services may be stored in a different location than where data is processed or stored in Dynamics 365 Customer Insights. By importing or connecting to data stored in online services, you agree that data can be transferred to and stored with Dynamics 365 Customer Insights. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

- The Customer Insights service principal must be in one of the following roles to access the storage account. For more information, see [Grant permissions to the service principal to access the storage account](connect-service-principal.md#grant-permissions-to-the-service-principal-to-access-the-storage-account).
  - Storage Blob Data Reader
  - Storage Blob Data Owner
  - Storage Blob Data Contributor

- Data in your Azure Data Lake must follow the Common Data Model standard for storage of your data and have the common data model manifest to represent the schema of the data files (*.csv or *.parquet). The manifest must provide the details of the entities such as entity columns and data types, and the data file location and file type. For more information, see [The Common Data Model manifest](/common-data-model/sdk/manifest). If the manifest is not present, Admin users with Storage Blob Data Owner or Storage Blob Data Contributor access can define the schema when ingesting the data.

## Connect to Azure Data Lake storage

1. Go to **Data** > **Data sources**.

1. Select **Add data source**.

1. Select **Azure data lake storage**.

   :::image type="content" source="media/data_sources_ADLS.png" alt-text="Dialog box to enter connection details for Azure Data Lake." lightbox="media/data_sources_ADLS.png":::

1. Enter a **Name** for the data source and an optional **Description**. The name uniquely identifies the data source and is referenced in downstream processes. The name can't be changed.

1. Choose one of the following options for **Connect your storage using**. For more information, see [Connect Customer Insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md).

   - **Azure resource**: Enter the **Resource Id**. Optionally, if you want to ingest data from a storage account through an Azure Private link, select **Enable Private link**. For more information, see [What is Azure Private Link?](/azure/private-link/private-link-overview).
   - **Azure subscription**: Select the **Subscription** and then the **Resource group** and **Storage account**. Optionally, if you want to ingest data from a storage account through an Azure Private link, select **Enable Private link**. For more information, see [What is Azure Private Link?](/azure/private-link/private-link-overview).
  
1. Choose the name of the **Container** that contains the data and schema (model.json or manifest.json file) to import data from, and select **Next**.
   > [!NOTE]
   > Any model.json or manifest.json file associated with another data source in the environment won't show in the list. However, the same model.json or manifest.json file can be used for data sources in multiple environments.

1. To create a new schema, go to [Create a new schema file](#create-a-new-schema-file).

1. To use an existing schema, navigate to the folder containing the model.json or manifest.cdm.json file. You can search within a directory to find the file.

1. Select the json file and select **Next**. A list of available entities displays.

   :::image type="content" source="media/review-entities.png" alt-text="Dialog box of a list of entities to select":::

1. Select the entities you want to include.

   :::image type="content" source="media/ADLS_required.png" alt-text="Dialog box showing Required for Primary key":::

   > [!TIP]
   > To edit the entities in a JSON editing interface, select **Show more** > **Edit schema file**. Make changes and select **Save**.

1. For selected entities that require incremental ingestion, **Required** displays under **Incremental refresh**. For each of these entities, see [Configure an incremental refresh for Azure Data Lake data sources](incremental-refresh-data-sources.md).

1. For selected entities where a primary key has not been defined, **Required** displays under **Primary key**. For each of these entities:
   1. Select **Required**. The **Edit entity** panel displays.
   1. Choose the **Primary key**. The primary key is an attribute unique to the entity. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.
   1. Optionally, change the partition pattern.
   1. Select **Close** to save and close the panel.

1. Select **Attributes** for each included entity. The Manage attributes page displays.

   :::image type="content" source="media/dataprofiling-entities.png" alt-text="Dialog box to select data profiling.":::

   1. Create new attributes, edit, or delete existing attributes. You can change the name, the data format, or add a semantic type.
   1. To enable analytics and other capabilities, select **Data profiling** for the whole entity or for specific attributes. By default, no entity is enabled for data profiling.
   1. Select **Done**.

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

### Create a new schema file

1. Select **New schema file**.

1. Enter a name for the file and select **Save**.

1. Select **New entity**. The New Entity panel displays.

1. Enter the entity name and choose the **Data files location**.
   - **Multiple .csv or .parquet files**: Browse to the root folder, select the pattern type, and enter the expression.
   - **Single .csv or .parquet files***: Browse to the .csv or .parquet file and select it.

   :::image type="content" source="media/ADLS_new_entity_location.png" alt-text="Dialog box to create a new entity with Data files location highlighted.":::

1. Select **Save**.

   :::image type="content" source="media/ADLS_new_entity_define_attributes.png" alt-text="Dialog box to define or auto generate attributes.":::

1. Select **define the attributes** to add the attributes, or select **auto generate them**. To manually define the attributes, enter a name, select the data format and optional semantic type. For auto-generated attributes:

   1. After the attributes are auto-generated, select **Review attributes**. The Manage attributes page displays.

   1. Ensure the data format is correct for each attribute.

   1. To enable analytics and other capabilities, select **Data profiling** for the whole entity or for specific attributes. By default, no entity is enabled for data profiling.

      :::image type="content" source="media/dataprofiling-entities.png" alt-text="Dialog box to select data profiling.":::

   1. Select **Done**. The **Select entities** page displays.

1. Continue to add entities and attributes, if applicable.

1. After all entities have been added, select **Include** to include the entities in the data source ingestion.

   :::image type="content" source="media/ADLS_required.png" alt-text="Dialog box showing Required for Primary key":::

1. For selected entities that require incremental ingestion, **Required** displays under **Incremental ingestion**. For each of these entities, see [Configure an incremental refresh for Azure Data Lake data sources](incremental-refresh-data-sources.md).

1. For selected entities where a primary key has not been defined, **Required** displays under **Primary key**. For each of these entities:
   1. Select **Required**. The **Edit entity** panel displays.
   1. Choose the **Primary key**. The primary key is an attribute unique to the entity. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.
   1. Optionally, change the partition pattern.
   1. Select **Close** to save and close the panel.

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.


## Edit an Azure Data Lake storage data source

You can update the *Connect to storage account using* option. For more information, see [Connect Customer Insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md). To connect to a different container from your storage account, or change the account name, [create a new data source connection](#connect-to-azure-data-lake-storage).

1. Go to **Data** > **Data sources**.

1. Next to the data source you'd like to update, select  **Edit**.

   :::image type="content" source="media/data_sources_edit_ADLS.png" alt-text="Dialog box to edit Azure Data Lake data source.":::

1. Change any of the following information:

   - **Description**
   - **Connect your storage using** and connection information. You can't change **Container** information when updating the connection.
      > [!NOTE]
      > One of the following roles must be assigned to the storage account or container:
        > - Storage Blob Data Reader
        > - Storage Blob Data Owner
        > - Storage Blob Data Contributor

   - **Enable private link** (for Azure resource or subscription connections) if you want to ingest data from a storage account through an Azure Private link. For more information, see [What is Azure Private Link?](/azure/private-link/private-link-overview).

1. Select **Next**.
1. Change any of the following:
   - Navigate to a different model.json or manifest.json file with a different set of entities from the container.
   - To add additional entities to ingest, select **New entity**.
   - To remove any already selected entities if there are no dependencies, select the entity and **Delete**.
      > [!IMPORTANT]
      > If there are dependencies on the existing model.json or manifest.json file and the set of entities, you'll see an error message and can't select a different model.json or manifest.json file. Remove those dependencies before changing the model.json or manifest.json file or create a new data source with the model.json or manifest.json file that you want to use to avoid removing the dependencies.
   - To change data file location or the primary key, select **Edit**.
   - To change the incremental ingestion data, see [Configure an incremental refresh for Azure Data Lake data sources](incremental-refresh-data-sources.md)

1. Select **Attributes** to add or change attributes, or to enable data profiling. Then select **Done**.

1. Click **Save** to apply your changes and return to the **Data sources** page.
