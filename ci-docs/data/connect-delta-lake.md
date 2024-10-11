---
title: "Connect to Delta tables in Azure Data Lake Storage"
description: "Work with data stored in Delta tables from Azure Data Lake Storage."
ms.date: 10/02/2024
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Connect to Delta tables in Azure Data Lake Storage

Connect to data in Delta tables and bring it into Dynamics 365 Customer Insights - Data.

[!INCLUDE [delta-lake-benefits](./includes/delta-lake-benefits.md)]

## Supported Databricks features and versions

Customer Insights - Data supports Databricks features with a 'minReaderVersion' of 2 or earlier. Databricks features that require Databricks reader version 3 or later aren't supported. The table shows the supported and unsupported Databricks features.

| Supported features  | Unsupported features |
| ------------------- | -------------------- |
| Basic functionality | Deletion vectors     |
| Change data feed    | Liquid clustering    |
| Check constraints   | Table features write |
| Column mapping      | TimestampNTZ         |
| Generate columns    | Type widening        |
| Identity columns    | Variant              |
| Row tracking        |                      |
| Table features read |                      |
| UniForm             |                      |

 Learn more: [How does Databricks manage Delta Lake feature compatibility?](https://docs.databricks.com/en/delta/feature-compatibility.html#features-by-protocol-version).

## Prerequisites

[!INCLUDE [delta-lake-prereqs](./includes/delta-lake-prereqs.md)]

- Data in your Azure Data Lake Storage must be in Delta tables. Customer Insights - Data relies on the version property in the table's history to identify the latest changes for incremental processing.

## Connect to Delta data from Azure Data Lake Storage

1. Go to **Data** > **Data sources**.

1. Select **Add a data source**.

1. Select **Azure Data Lake Delta tables**.

   :::image type="content" source="media/delta-lake-new.svg" alt-text="Dialog box to enter connection details for Delta Lake." lightbox="media/delta-lake-new.svg":::

1. Enter a **Data source name** and an optional **Description**. The name is referenced in downstream processes and it's not possible to change it after creating the data source.

1. Choose one of the following options for **Connect your storage using**.

   - **Azure subscription**: Select the **Subscription** and then the **Resource group** and **Storage account**.
   - **Azure resource**: Enter the **Resource Id**.

1. Choose the name of the **Container** that contains the folder of your data.
1. If your storage account is behind a firewall, select **This storage account is behind a firewall** to connect using [managed identities for Azure resources](private-link.md).
1. Select **Next**.

1. Navigate to the folder that contains the data in Delta tables and select it. Then, select **Next**. A list of available tables displays.

1. Select the tables you want to include.

1. For selected tables where a primary key isn't defined, **Required** displays under **Primary key**. For each of these tables:
   1. Select **Required**. The **Edit table** panel displays.
   1. Choose the **Primary key**. The primary key is an attribute unique to the table. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.
   1. Select **Close** to save and close the panel.

   :::image type="content" source="media/delta-edit-table.png" alt-text="Dialog box showing Required for Primary key":::

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

When a column is added to the data source, the information automatically appends to the data in Customer Insights - Data once a refresh occurs. If unification is already configured for the table, the new column must be added to the unification process.

1. From the [**Customer data**](data-unification-update.md#edit-customer-data) step, select **Select tables and columns** and select the new column.

1. In the [**Unified data view**](data-unification-update.md#manage-unified-fields) step, make sure the column isn't excluded from the customer profile. Select **Excluded** and readd the column.

1. In the [**Run updates to the unified profile**](data-unification-update.md#run-updates-to-the-unified-profile) step, select **Unify customer profiles and dependencies**.

### Change or remove a column

When a column is removed from a data source, the system checks for dependencies in other processes. If there's a dependency on the columns, the system stops the refresh and provides an error indicating the dependencies must be removed. These dependencies display in a notification to help you locate and remove them.

### Validate a schema change

After the data source refreshes, go to the **Data** > **Tables** page. Select the table for the data source and verify the schema.

## Delta lake time travel and data refreshes

Delta lake time travel is the ability to query through table versions based on a timestamp or version number. Changes to Delta folders are versioned, and Customer Insights - Data uses the Delta folder versions to keep track of what data to process. In a regular delta table refresh, data is pulled from all the data table versions since the last refresh. As long as all versions are present, Customer Insights - Data can process just the changed elements and deliver faster results. [Learn more about time travel](https://www.databricks.com/blog/2019/02/04/introducing-delta-time-travel-for-large-scale-data-lakes.html).

For example, if Customer Insights – Data last synchronized with version 23 of your Delta folder data, it expects to find version 23 and possibly subsequent versions available. If the expected data versions aren't available, data synchronization fails and requires a [manual full data refresh](#manually-run-a-full-data-refresh-on-a-delta-table-folder). Data synchronization can fail if your Delta folder data was deleted and then recreated. Or if Customer Insights - Data couldn't connect to your Delta folders for an extended period while the versions advanced.

To avoid the need for a full data refresh, we recommend you maintain a reasonable history backlog, such as 15 days.

### Manually run a full data refresh on a Delta table folder

A full refresh takes all the data from a table in Delta format and reloads it from the Delta table version zero (0). Changes to the Delta folder schema trigger an automatic full refresh. To manually trigger a full refresh, perform the following steps.

1. Go to **Data** > **Data sources**.

1. Select the **Azure Data Lake Delta tables** data source.

1. Select the table you want to refresh. The **Edit table** pane displays.

   :::image type="content" source="media/delta-refresh-table.png" alt-text="Edit table pane to select one-time full refresh.":::

1. Select **Run one-time full refresh**.

1. Select **Save** to run the refresh. The **Data sources** page opens showing the data source in **Refreshing** status, but only the selected table is refreshing.

1. Repeat the process for other tables, if applicable.

### Data synchronization failure

Data synchronization can fail if your Delta folder data was deleted and then recreated. Or if Customer Insights - Data couldn't connect to your Delta folders for an extended period while the versions advanced. To minimize the impact where an intermittent data pipeline failure creates the need for a full refresh, we recommend you maintain a reasonable history backlog, such as 15 days.

## Next steps

- [Data unification overview](data-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
