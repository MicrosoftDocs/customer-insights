---
title: "Connect to Common Data Model tables in Azure Data Lake Storage"
description: "Work with data from Azure Data Lake Storage."
ms.date: 10/29/2024
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Connect to Common Data Model tables in Azure Data Lake Storage

[!INCLUDE [azure-ad-to-microsoft-entra-id](../journeys/includes/azure-ad-to-microsoft-entra-id.md)]

Ingest data into Dynamics 365 Customer Insights - Data using your Azure Data Lake Storage account with Common Data Model tables. Data ingestion can be full or incremental.

## Prerequisites

- The Azure Data Lake Storage account must have [hierarchical namespace enabled](/azure/storage/blobs/data-lake-storage-namespace). The data must be stored in a hierarchical folder format that defines the root folder and has subfolders for each table. The subfolders can have full data or incremental data folders.
- To authenticate with a Microsoft Entra service principal, make sure it's configured in your tenant. For more information, see [Connect to an Azure Data Lake Storage account with a Microsoft Entra service principal](connect-service-principal.md).
- To connect to storage protected by firewalls, [Set up managed identities](private-link.md).
- The Azure Data Lake Storage you want to connect and ingest data from has to be in the same Azure region as the Dynamics 365 Customer Insights environment and the subscriptions must be in the same tenant. Connections to a Common Data Model folder from a data lake in a different Azure region is not supported. To know the Azure region of the environment, go to **Settings** > **System** > **About** in Customer Insights - Data.
- Data stored in online services may be stored in a different location than where data is processed or stored. By importing or connecting to data stored in online services, you agree that data can be transferred. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).
- The Customer Insights - Data service principal must be in one of the following roles to access the storage account. For more information, see [Grant permissions to the service principal to access the storage account](connect-service-principal.md#grant-permissions-to-the-service-principal-to-access-the-storage-account).
  - Storage Blob Data Reader
  - Storage Blob Data Owner
  - Storage Blob Data Contributor

- When connecting to your Azure storage using the *Azure subscription* option, the user that sets up the data source connection needs at least the Storage Blob Data Contributor permissions on the storage account.
- When connecting to your Azure storage using the *Azure resource* option, the user that sets up the data source connection needs at least the permission for the **Microsoft.Storage/storageAccounts/read** action on the storage account. An [Azure built-in role](/azure/role-based-access-control/built-in-roles) that includes this action is the **Reader** role. To limit access to just the necessary action, [create an Azure custom role](/azure/role-based-access-control/custom-roles) that includes only this action.
- For optimal performance, the size of a partition should be 1 GB or less and the number of partition files in a folder must not exceed 1000.
- Data in your Data Lake Storage should follow the Common Data Model standard for storage of your data and have the Common Data Model manifest to represent the schema of the data files (*.csv or *.parquet). The manifest must provide the details of the tables such as table columns and data types, and the data file location and file type. For more information, see [The Common Data Model manifest](/common-data-model/sdk/manifest). If the manifest is not present, Admin users with Storage Blob Data Owner or Storage Blob Data Contributor access can define the schema when ingesting the data.

  > [!NOTE]
  > If any of the fields in the .parquet files have data type Int96, the data may not display on the **Tables** page. We recommend using standard data types, such as the Unix timestamp format (which represents time as the number of seconds since January 1, 1970, at midnight UTC).

## Limitations

- Customer Insights - Data doesn't support columns of decimal type with precision greater than 16.

## Connect to Azure Data Lake Storage

1. Go to **Data** > **Data sources**.
1. Select **Add a data source**.
1. Select **Azure Data Lake Common Data Model tables**.
   :::image type="content" source="media/data_sources_ADLS.svg" alt-text="Dialog box to enter connection details for Azure Data Lake with Common Data Model tables." lightbox="media/data_sources_ADLS.svg":::

1. Enter a **Data source name** and an optional **Description**. The name is referenced in downstream processes and it's not possible to change it after creating the data source.
1. Choose one of the following options for **Connect your storage using**. For more information, see [Connect to an Azure Data Lake Storage account with a Microsoft Entra service principal](connect-service-principal.md).
   - **Azure resource**: Enter the **Resource Id**.
   - **Azure subscription**: Select the **Subscription** and then the **Resource group** and **Storage account**. 
  
   > [!NOTE]
   > You need one of the following roles to the container to create the data source:
   >
   > - Storage Blob Data Reader is sufficient to read from a storage account and ingest the data to Customer Insights - Data.
   > - Storage Blob Data Contributor or Owner is required if you want to edit the manifest files directly in Customer Insights - Data.  
   >
   > Having the role on the storage account will provide the same role on all of its containers.

1. Choose the name of the **Container** that contains the data and schema (model.json or manifest.json file) to import data from.
   > [!NOTE]
   > Any model.json or manifest.json file associated with another data source in the environment won't show in the list. However, the same model.json or manifest.json file can be used for data sources in multiple environments.

1. If your storage account is behind a firewall, determine your next step:
   - If **Enable private link** appears, connect to the account using [Azure private links](private-link.md)
     :::image type="content" source="media/enable-private-link.png" alt-text="Portion of dialog box showing enable private link.":::
   - If **This storage account is behind a firewall** appears, connect to the account using [managed identities for Azure resources (preview)](managed-identities.md).
     :::image type="content" source="media/enable-msi.png" alt-text="Portion of dialog box showing storage account is behind a firewall.":::
1. Select **Next**.

1. To create a new schema, go to [Create a new schema file](#create-a-new-schema-file).
1. To use an existing schema, navigate to the folder containing the model.json or manifest.cdm.json file. You can search within a directory to find the file.
1. Select the json file and select **Next**. A list of available tables displays.
   :::image type="content" source="media/review-tables.png" alt-text="Dialog box of a list of tables to select":::

1. Select the tables you want to include.
   :::image type="content" source="media/ADLS_required.png" alt-text="Dialog box showing Required for Primary key":::

   > [!TIP]
   > To edit a table in a JSON editing interface, select the table and then **Edit schema file**. Make changes and select **Save**.

1. For selected tables where a primary key has not been defined, **Required** displays under **Primary key**. For each of these tables:
   1. Select **Required**. The **Edit table** panel displays.
   1. Choose the **Primary key**. The primary key is an attribute unique to the table. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.
   1. Optionally, change the partition pattern.
   1. Select **Close** to save and close the panel.

1. Select the number of **Columns** for each included table. The **Manage attributes** page displays.
   :::image type="content" source="media/dataprofiling-tables.png" alt-text="Dialog box to select data profiling.":::

   1. Create new columns, edit, or delete existing columns. You can change the name, the data format, or add a semantic type.
   1. To enable analytics and other capabilities, select [**Data profiling**](data-sources.md#data-profiling) for the whole table or for specific columns. By default, no table is enabled for data profiling.
   1. Select **Done**.

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Tables**](tables.md) page.

### Create a new schema file

1. Select **Create schema file**.

1. Enter a name for the file and select **Save**.

1. Select **New table**. The **New Table** panel displays.

1. Enter the table name and choose the **Data files location**.
   - **Multiple .csv or .parquet files**: Browse to the root folder, select the pattern type, and enter the expression.
   - **Single .csv or .parquet files**: Browse to the .csv or .parquet file and select it.

   :::image type="content" source="media/ADLS_new_table_location.png" alt-text="Dialog box to create a new table with Data files location highlighted.":::

1. Select **Save**.

   :::image type="content" source="media/ADLS_new_table_define_attributes.png" alt-text="Dialog box to define or auto generate attributes.":::

1. Select **define the attributes** to manually add the attributes, or select **auto generate them**. To define the attributes, enter a name, select the data format and optional semantic type. For auto-generated attributes:

   1. After the attributes are auto-generated, select **Review attributes**. The **Manage attributes** page displays.

   1. Ensure the data format is correct for each attribute.

   1. To enable analytics and other capabilities, select **Data profiling** for the whole table or for specific columns. By default, no table is enabled for data profiling.

      :::image type="content" source="media/dataprofiling-tables.png" alt-text="Dialog box to select data profiling.":::

   1. Select **Done**. The **Select tables** page displays.

1. Continue to add tables and columns, if applicable.

1. After all tables have been added, select **Include** to include the tables in the data source ingestion.

   :::image type="content" source="media/ADLS_required.png" alt-text="Dialog box showing Required for Primary key":::

1. For selected tables where a primary key has not been defined, **Required** displays under **Primary key**. For each of these tables:
   1. Select **Required**. The **Edit table** panel displays.
   1. Choose the **Primary key**. The primary key is an attribute unique to the table. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.
   1. Optionally, change the partition pattern.
   1. Select **Close** to save and close the panel.

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Data** > **Tables**](tables.md) page.

## Edit an Azure Data Lake Storage data source

You can update the *Connect to storage account using* option. For more information, see [Connect to an Azure Data Lake Storage account with a Microsoft Entra service principal](connect-service-principal.md). To connect to a different container from your storage account, or change the account name, [create a new data source connection](#connect-to-azure-data-lake-storage).

1. Go to **Data** > **Data sources**. Next to the data source you'd like to update, select  **Edit**.

1. Change any of the following information:

   - **Description**
   - **Connect your storage using** and connection information. You can't change **Container** information when updating the connection.
      > [!NOTE]
      > One of the following roles must be assigned to the storage account or container:
      > - Storage Blob Data Reader
      > - Storage Blob Data Owner
      > - Storage Blob Data Contributor

   - **This storage account is behind a firewall** if you want to ingest data from a storage account behind a firewall. Learn more: [Set up managed identities for storage accounts behind firewalls](private-link.md).

1. Select **Next**.
1. Change any of the following:
   - Navigate to a different model.json or manifest.json file with a different set of tables from the container.
   - To add additional tables to ingest, select **New table**.
   - To remove any already selected tables if there are no dependencies, select the table and **Delete**.
      > [!IMPORTANT]
      > If there are dependencies on the existing model.json or manifest.json file and the set of tables, you'll see an error message and can't select a different model.json or manifest.json file. Remove those dependencies before changing the model.json or manifest.json file or create a new data source with the model.json or manifest.json file that you want to use to avoid removing the dependencies.
   - To change data file location or the primary key, select **Edit**.
   - Only change the table name to match the table name in the .json file.

     > [!NOTE]
     > Always keep the table name in the same as the table name in the model.json or manifest.json file after ingestion. Customer Insights - Data validates all table names with the model.json or manifest.json during every system refresh. If a table name changes, an error occurs because Customer Insights - Data cannot find the new table name in the .json file. If an ingested table name was accidentally changed, edit the table name to match the name in the .json file.

1. Select **Columns** to add or change them, or to enable data profiling. Then select **Done**.

1. Select**Save** to apply your changes and return to the **Data sources** page.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
