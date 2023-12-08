---
title: "Connect to Delta tables in Azure Data Lake Storage (preview)"
description: "Work with data stored in Delta Lake format from Azure Data Lake Storage."
ms.date: 12/08/2023
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Connect to Delta tables in Azure Data Lake Storage (preview)

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

[!INCLUDE [public-preview-banner](./includes/public-preview-banner.md)]

Connect to data in Delta format and bring it into Dynamics 365 Customer Insights - Data. [Delta](https://go.microsoft.com/fwlink/?linkid=2248260) is a term introduced with Delta Lake, the foundation for storing data and tables in the Databricks Lakehouse Platform. Delta Lake is an open-source storage layer that brings ACID (atomicity, consistency, isolation, and durability) transactions to big data workloads. For more information, see the [Delta Lake Documentation Page.](https://docs.delta.io/latest/delta-intro.html)

Key reasons to connect to data stored in Delta format:

- Directly import Delta formatted data saving time and effort.
- Eliminate the compute and storage costs associated with transforming and storing a copy of your lakehouse data.
- Automatically improve the reliability of data ingestion to Customer Insights - Data provided by Delta versioning.

For example, Contoso Coffee has millions of records coming in on a daily basis. Currently, they do full refreshes of their data every 6 hours. This full refresh takes lots of time to reprocess everything when most data has already been processed. By using the Delta format, Contoso is able to greatly reduce their processing time by only processing the new records, leading to even faster insights from Customer Insights – Data.

[!INCLUDE [public-preview-banner](./includes/public-preview-note.md)]

## Prerequisites

- The Azure Data Lake Storage must be in the same tenant and Azure region as Customer Insights - Data.

- The Customer Insights - Data service principal must have Storage Blob Data Contributor permissions to access the storage account. For more information, see [Grant permissions to the service principal to access the storage account](connect-service-principal.md#grant-permissions-to-the-service-principal-to-access-the-storage-account).

- The user that sets up the data source connection needs at least Storage Blob Data Reader permissions on the Azure Data Lake Storage account.

- Data stored in online services may be stored in a different location than where data is processed or stored. By importing or connecting to data stored in online services, you agree that data can be transferred. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

- Data in your Azure Data Lake Storage must be in Delta format. Customer Insights - Data relies on the version property in the table's history to identify the latest changes for incremental processing.

- The Delta tables must be in a folder in the storage container and can't be in the container root directory. For example:

  ```
   storage_container_root/
      DeltaLakeDataRoot/
         ADeltaLakeTable/
             _delta_log/
                 0000.json
                 0001.json
             part-0001-snappy.parquet
             part-0002-snappy.parquet 
  ```  

## Connect to Delta data from Azure Data Lake Storage

1. Go to **Data** > **Data sources**.

1. Select **Add a data source**.

1. Select **Azure Data Lake - Delta tables (Preview)**.

   :::image type="content" source="media/delta-lake-new.png" alt-text="Dialog box to enter connection details for Delta Lake.":::

1. Enter a **Data source name** and an optional **Description**. The name is referenced in downstream processes and it's not possible to change it after creating the data source.

1. Choose one of the following options for **Connect your storage using**.

   - **Azure subscription**: Select the **Subscription** and then the **Resource group** and **Storage account**. Optionally, if you want to ingest data from a storage account through an Azure Private Link, select **Enable Private Link**. For more information, see [Private Links](private-link.md).
   - **Azure resource**: Enter the **Resource Id**. Optionally, if you want to ingest data from a storage account through an Azure Private Link, select **Enable Private Link**. For more information, see [Private Links](private-link.md).

1. Choose the name of the **Container** that contains the folder of your data, and select **Next**.

1. Navigate to the folder that contains the data in Delta format and select it. Then, select **Next**. A list of available tables displays.

1. Select the tables you want to include.

   :::image type="content" source="media/delta-edit-table.png" alt-text="Dialog box showing Required for Primary key":::

1. For selected tables where a primary key has not been defined, **Required** displays under **Primary key**. For each of these tables:
   1. Select **Required**. The **Edit table** panel displays.
   1. Choose the **Primary key**. The primary key is an attribute unique to the table. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.
   1. Select **Close** to save and close the panel.

1. To enable data profiling on any of the columns, select the number of **Columns** for the table. The **Manage attributes** page displays.

   :::image type="content" source="media/delta-dataprofiling-columns.png" alt-text="Dialog box to select data profiling.":::

   1. Select **Data profiling** for the whole table or for specific columns. By default, no table is enabled for data profiling.
   1. Select **Done**.

1. Select **Save**. The **Data sources** page opens showing the new data source in **Refreshing** status.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Tables**](tables.md) page.

## Manage schema changes

When a column is added or removed from the schema of a Delta folders data source, the system runs a complete refresh of the data. Full refreshes take longer to process all the data than incremental refreshes.

### Add a column

When a column is added to the data source, the information automatically appends to the data in Customer Insights - Data once a refresh occurs. If you have already configured unification for the table, the new column must be added to the unification process. From the [**Customer data**](data-unification-update.md#edit-customer-data) step, select **Select tables and columns** and select the new column. In the [**Unified data view**](data-unification-update.md#manage-unified-fields) step, make sure the column isn't excluded from the customer profile. Select **Excluded** and readd the column.

### Change or remove a column

When a column is removed from a data source, the system checks for dependencies in other processes. If there's a dependency on the columns, the system stops the refresh and provides an error indicating the dependencies must be removed. These dependencies display in a notification to help you locate and remove them.

### Validate a schema change

After the data source has refreshed, go to **Data** > **Tables** page. Select the table for the data source and verify the schema.

## Delta lake time travel and data refreshes

Delta lake time travel is the ability to query through table versions based on a timestamp or version number. Changes to Delta folders are versioned, and Customer Insights - Data uses the Delta folder versions to keep track of what data to process. In a regular delta table refresh, data is pulled from all the data table versions since the last refresh. As long as all versions are present, Customer Insights - Data can process just the changed elements and deliver faster results. [Learn more about time travel](https://www.databricks.com/blog/2019/02/04/introducing-delta-time-travel-for-large-scale-data-lakes.html).

Data synchronization can fail if your Delta folder data was deleted and then recreated. Or if Customer Insights - Data couldn't connect to your Delta folders for an extended period while the versions advanced. In the case where a version of the data is missing, you must perform a full data refresh on the table.

To avoid the need for a full data refresh, we recommend you maintain a reasonable history backlog, such as 15 days.

### Manually run a full data refresh on a Delta table folder

A full refresh takes all the data from a table in Delta format and reloads it from the Delta table version zero (0). If Customer Insights – Data last synchronized with version 23 of your Delta folder data, it expects to find version 23 and possibly subsequent versions available. If the expected data versions aren't available, data synchronization fails and requires a manual full data refresh.

Changes to the Delta folder schema trigger an automatic full refresh. To manually trigger a full refresh, perform the following steps.

1. Go to **Data** > **Data sources**.

1. Select the **Azure Data Lake - Delta tables (Preview)** data source.

1. Select the table you want to refresh. The **Edit table** pane displays.

   :::image type="content" source="media/delta-refresh-table.png" alt-text="Edit table pane to select one-time full refresh.":::

1. Select **Run one-time full refresh**.

1. Select **Save** to run the refresh. The **Data sources** page opens showing the data source in **Refreshing** status, but only the selected table is refreshing.

1. Repeat the process for other tables, if applicable.

## Next steps

- [Data unification overview](data-unification.md)
- [Common reasons for ingestion errors or corrupt data with Azure Data Lake Storage](common-data-ingestion-errors.md#common-reasons-for-ingestion-errors-or-corrupt-data-with-azure-data-lake-storage)

[!INCLUDE [footer-include](includes/footer-banner.md)]
