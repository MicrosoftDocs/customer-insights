---
title: "Connect to data in Azure Data Lake Storage"
description: "Work with Common Data Model data using Azure Data Lake Storage."
ms.date: 03/02/2023
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
ms.custom: bap-template
searchScope: 
  - ci-data-sources
  - ci-create-data-source
  - ci-attach-cdm
  - customerInsights
---

# Connect to data in Azure Data Lake Storage

Ingest data into Dynamics 365 Customer Insights using your Azure Data Lake Storage Gen2 account. Data ingestion can be full or incremental.

## Prerequisites

- Data ingestion supports Azure Data Lake Storage *Gen2* accounts exclusively. You can't use Data Lake Storage Gen1 accounts to ingest data.

- The Azure Data Lake Storage account must have [hierarchical namespace enabled](/azure/storage/blobs/data-lake-storage-namespace). The data must be stored in a hierarchical folder format that defines the root folder and has subfolders for each entity. The subfolders can have full data or incremental data folders.

- To authenticate with an Azure service principal, make sure it's configured in your tenant. For more information, see [Connect to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md).

- The Azure Data Lake Storage you want to connect and ingest data from has to be in the same Azure region as the Customer Insights environment and the subscriptions must be in the same tenant. Connections to a Common Data Model folder from a data lake in a different Azure region is not supported. To know the Azure region of the environment, go to **Admin** > **System** > **About** in Customer Insights.

- Data stored in online services may be stored in a different location than where data is processed or stored in Customer Insights. By importing or connecting to data stored in online services, you agree that data can be transferred to and stored with Customer Insights. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

- The Customer Insights service principal must be in one of the following roles to access the storage account. For more information, see [Grant permissions to the service principal to access the storage account](connect-service-principal.md#grant-permissions-to-the-service-principal-to-access-the-storage-account).
  - Storage Blob Data Reader
  - Storage Blob Data Owner
  - Storage Blob Data Contributor

- The user that sets up the data source connection needs at least Storage Blob Data Contributor permissions on the storage account.

- Data in your Data Lake Storage should follow the Common Data Model standard for storage of your data and have the common data model manifest to represent the schema of the data files (*.csv or *.parquet). The manifest must provide the details of the entities such as entity columns and data types, and the data file location and file type. For more information, see [The Common Data Model manifest](/common-data-model/sdk/manifest). If the manifest is not present, Admin users with Storage Blob Data Owner or Storage Blob Data Contributor access can define the schema when ingesting the data.

  > [!NOTE]
  > If any of the fields in the .parquet files have data type Int96, the data may not display on the **Entities** page. Customer Insights recommends using standard data types, such as the Unix timestamp format (which represents time as the number of seconds since January 1, 1970, at midnight UTC).

## Recommendations

For optimal performance, Customer Insights recommends the size of a partition be 1 GB or less and the number of partition files in a folder must not exceed 1000.

## Connect to Azure Data Lake Storage

1. Go to **Data** > **Data sources** and select **Add data source**. Then, select **Azure data lake storage**.

   :::image type="content" source="media/data_sources_ADLS.png" alt-text="Dialog box to enter connection details for Azure Data Lake." lightbox="media/data_sources_ADLS.png":::

1. Enter a **Name** for the data source and an optional **Description**. The name uniquely identifies the data source and is referenced in downstream processes and can't be changed.

1. Choose one of the following options for **Connect your storage using**. For more information, see [Connect Customer Insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md).

   - **Azure resource**: Enter the **Resource Id**. Optionally, if you want to ingest data from a storage account through an Azure Private Link, select **Enable Private Link**. For more information, see [Private Links](private-link.md).
   - **Azure subscription**: Select the **Subscription** and then the **Resource group** and **Storage account**. Optionally, if you want to ingest data from a storage account through an Azure Private Link, select **Enable Private Link**. For more information, see [Private Links](private-link.md).
  
   > [!NOTE]
   > You need one of the following roles either to the container or the storage account to create the data source:
   >
   >  - Storage Blob Data Reader is sufficient to read from a storage account and ingest the data to Customer Insights.
   >  - Storage Blob Data Contributor or Owner is required if you want to edit the manifest files directly in Customer Insights.  
  
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
   > To edit an entity in a JSON editing interface, select the entity and then **Edit schema file**. Make changes and select **Save**.

1. For selected entities that require incremental ingestion, **Required** displays under **Incremental refresh**. For each of these entities, see [Configure an incremental refresh for Azure Data Lake data sources](incremental-refresh-data-sources.md).

1. For selected entities where a primary key has not been defined, **Required** displays under **Primary key**. For each of these entities:
   1. Select **Required**. The **Edit entity** panel displays.
   1. Choose the **Primary key**. The primary key is an attribute unique to the entity. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.
   1. Optionally, change the partition pattern.
   1. Select **Close** to save and close the panel.

1. Select the number of **Attributes** for each included entity. The **Manage attributes** page displays.

   :::image type="content" source="media/dataprofiling-entities.png" alt-text="Dialog box to select data profiling.":::

   1. Create new attributes, edit, or delete existing attributes. You can change the name, the data format, or add a semantic type.
   1. To enable analytics and other capabilities, select **Data profiling** for the whole entity or for specific attributes. By default, no entity is enabled for data profiling.
   1. Select **Done**.

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Entities**](entities.md) page.

### Create a new schema file

1. Select **New schema file**. Enter a name for the file and select **Save**.

1. Select **New entity**. The **New Entity** panel displays.

1. Enter the entity name and choose the **Data files location**.
   - **Multiple .csv or .parquet files**: Browse to the root folder, select the pattern type, and enter the expression.
   - **Single .csv or .parquet files**: Browse to the .csv or .parquet file and select it.

   :::image type="content" source="media/ADLS_new_entity_location.png" alt-text="Dialog box to create a new entity with Data files location highlighted.":::

1. Select **Save**.

   :::image type="content" source="media/ADLS_new_entity_define_attributes.png" alt-text="Dialog box to define or auto generate attributes.":::

1. Select **define the attributes** to manually add the attributes, or select **auto generate them**. To define the attributes, enter a name, select the data format and optional semantic type. For auto-generated attributes:

   1. After the attributes are auto-generated, select **Review attributes**. The **Manage attributes** page displays.

   1. Ensure the data format is correct for each attribute.

   1. To enable analytics and other capabilities, select **Data profiling** for the whole entity or for specific attributes. By default, no entity is enabled for data profiling.

      :::image type="content" source="media/dataprofiling-entities.png" alt-text="Dialog box to select data profiling.":::

   1. Select **Done**. The **Select entities** page displays.

1. Continue to add entities and attributes, if applicable.

1. After all entities have been added, select **Include** to include the entities in the data source ingestion.

   :::image type="content" source="media/ADLS_required.png" alt-text="Dialog box showing Required for Primary key":::

1. For selected entities that require incremental ingestion, **Required** displays under **Incremental refresh**. For each of these entities, see [Configure an incremental refresh for Azure Data Lake data sources](incremental-refresh-data-sources.md).

1. For selected entities where a primary key has not been defined, **Required** displays under **Primary key**. For each of these entities:
   1. Select **Required**. The **Edit entity** panel displays.
   1. Choose the **Primary key**. The primary key is an attribute unique to the entity. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.
   1. Optionally, change the partition pattern.
   1. Select **Close** to save and close the panel.

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Entities**](entities.md) page.

## Edit an Azure Data Lake Storage data source

You can update the *Connect to storage account using* option. For more information, see [Connect Customer Insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md). To connect to a different container from your storage account, or change the account name, [create a new data source connection](#connect-to-azure-data-lake-storage).

1. Go to **Data** > **Data sources**. Next to the data source you'd like to update, select  **Edit**.

   :::image type="content" source="media/data_sources_edit_ADLS.png" alt-text="Dialog box to edit Azure Data Lake data source.":::

1. Change any of the following information:

   - **Description**
   - **Connect your storage using** and connection information. You can't change **Container** information when updating the connection.
      > [!NOTE]
      > One of the following roles must be assigned to the storage account or container:
        > - Storage Blob Data Reader
        > - Storage Blob Data Owner
        > - Storage Blob Data Contributor

   - **Enable Private Link** if you want to ingest data from a storage account through an Azure Private Link. For more information, see [Private Links](private-link.md).

1. Select **Next**.
1. Change any of the following:
   - Navigate to a different model.json or manifest.json file with a different set of entities from the container.
   - To add additional entities to ingest, select **New entity**.
   - To remove any already selected entities if there are no dependencies, select the entity and **Delete**.
      > [!IMPORTANT]
      > If there are dependencies on the existing model.json or manifest.json file and the set of entities, you'll see an error message and can't select a different model.json or manifest.json file. Remove those dependencies before changing the model.json or manifest.json file or create a new data source with the model.json or manifest.json file that you want to use to avoid removing the dependencies.
   - To change data file location or the primary key, select **Edit**.
   - To change the incremental ingestion data, see [Configure an incremental refresh for Azure Data Lake data sources](incremental-refresh-data-sources.md).
   - Only change the entity name to match the entity name in the .json file.

     > [!NOTE]
     > Always keep the entity name in Customer Insights the same as the entity name inside the model.json or manifest.json file after ingestion. Customer Insights validates all entity names with the model.json or manifest.json during every system refresh. If an entity name is changed either inside Customer Insights or outside, an error occurs because Customer Insights cannot find the new entity name in the .json file. If an ingested entity name was accidentally changed, edit the entity name in Customer Insights to match the name in the .json file.

1. Select **Attributes** to add or change attributes, or to enable data profiling. Then select **Done**.

1. Click **Save** to apply your changes and return to the **Data sources** page.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

## Common reasons for ingestion errors or corrupt data

During data ingestion, some of the most common reasons a record might be considered corrupt include:

- The data types and field values don't match between the source file and the schema
- Number of columns in the source file don't match the schema
- Fields contain characters that cause the columns to skew compared to the expected schema. For example: incorrectly formatted quotes, unescaped quotes, newline characters, or tabbed characters.
- Partition files are missing
- If there are datetime/date/datetimeoffset columns, their format must be specified in the schema if it doesn't follow the standard format.

### Schema or data type mismatch

If the data does not conform to the schema, the ingestion process completes with errors. Correct either the source data or the schema and re-ingest the data.

### Partition files are missing

- If ingestion was successful without any corrupt records, but you can't see any data, edit your model.json or manifest.json file to make sure partitions are specified. Then, [refresh the data source](data-sources-manage.md#refresh-data-sources).

- If data ingestion occurs at the same time as data sources are being refreshed during an automatic schedule refresh, the partition files may be empty or not available for Customer Insights to process. To align with the upstream refresh schedule, change the [system refresh schedule](schedule-refresh.md) or the refresh schedule for the data source. Align the timing so that refreshes do not all occur at once and provides the latest data to be processed in Customer Insights.

### Datetime fields in the wrong format

The datetime fields in the entity are not in ISO 8601 or en-US formats. The default datetime format in Customer Insights is en-US format. All the datetime fields in an entity should be in the same format. Customer Insights supports other formats provided annotations or traits are made at the source or entity level in the model or manifest.json. For example:

**Model.json**

   ```json
      "annotations": [
        {
          "name": "ci:CustomTimestampFormat",
          "value": "yyyy-MM-dd'T'HH:mm:ss:SSS"
        },
        {
          "name": "ci:CustomDateFormat",
          "value": "yyyy-MM-dd"
        }
      ]   
   ```

  In a manifest.json, the datetime format can be specified at the entity level or at the attribute level. At the entity level, use "exhibitsTraits" in the entity in the *.manifest.cdm.json to define the datetime format. At the attribute level, use "appliedTraits" in the attribute in the entityname.cdm.json.

**Manifest.json at the entity level**

```json
"exhibitsTraits": [
    {
        "traitReference": "is.formatted.dateTime",
        "arguments": [
            {
                "name": "format",
                "value": "yyyy-MM-dd'T'HH:mm:ss"
            }
        ]
    },
    {
        "traitReference": "is.formatted.date",
        "arguments": [
            {
                "name": "format",
                "value": "yyyy-MM-dd"
            }
        ]
    }
]
```

**Entity.json at the attribute level**

```json
   {
      "name": "PurchasedOn",
      "appliedTraits": [
        {
          "traitReference": "is.formatted.date",
          "arguments" : [
            {
              "name": "format",
              "value": "yyyy-MM-dd"
            }
          ]
        },
        {
          "traitReference": "is.formatted.dateTime",
          "arguments" : [
            {
              "name": "format",
              "value": "yyyy-MM-ddTHH:mm:ss"
            }
          ]
        }
      ],
      "attributeContext": "POSPurchases/attributeContext/POSPurchases/PurchasedOn",
      "dataFormat": "DateTime"
    }
```

[!INCLUDE [footer-include](includes/footer-banner.md)]
