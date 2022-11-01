---
title: "Incremental refresh for Power Query and Azure Data Lake data sources"
description: "Refresh new and updated data for large data sources based on Power Query or Azure data lake data sources."
ms.date: 11/15/2022
ms.reviewer: v-wendysmith

ms.subservice: audience-insights
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
manager: shellyha
searchScope: 
  - ci-system-schedule
  - customerInsights
---

# Incremental refresh for Power Query and Azure Data Lake data sources

Incremental refresh for data sources based on Power Query or Azure Data Lake provides the following advantages:

- **Faster refreshes** - Only data that has changed gets refreshed. For example, you might refresh only the past five days of a historical dataset.
- **Increased reliability** - With smaller refreshes, you don't need to maintain connections to volatile source systems for as long, reducing the risk of connection issues.
- **Reduced resource consumption** - Refreshing only a subset of your total data leads to more efficient use of computing resources and decreases the environmental footprint.

## Configure incremental refresh for data sources based on Power Query

Customer Insights allows incremental refresh for data sources imported through Power Query that support incremental ingestion. For example, Azure SQL databases with date and time fields, which indicate when data records were last updated.

1. [Create a new data source based on Power Query](connect-power-query.md).

1. Select a data source that supports incremental refresh, such as [Azure SQL database](/power-query/connectors/azuresqldatabase).

1. Select the tables to ingest.

1. Complete the transformation steps and select **Next**.

1. In the **Set up incremental refresh** dialog box, select **Set up** to open the **Incremental refresh settings**. If you select **Skip**, the data source will refresh the entire data set.
   > [!TIP]
   > You can also apply incremental refresh later by editing an existing data source.

1. On **Incremental refresh settings**, you'll configure the incremental refresh for all tables that you selected when creating the data source.

   :::image type="content" source="media/incremental-refresh-settings.png" alt-text="Configure incremental refresh settings.":::

1. Select a table, and provide the following details:

   - **Define the primary key**: Select a primary key for the table.
   - **Define the "last updated" field**: This field will only display attributes of type date or time. Select an attribute that indicates when the records were last updated. It will be used to identify the records that fall within the incremental refresh time frame.
   - **Check for updates every**: Specify how long you want the incremental refresh time frame to be.

1. Select **Save** to complete the creation of the data source. The initial data refresh will be a full refresh. Afterwards, the incremental data refresh happens as configured in the previous step.

## Configure incremental refresh for Azure Data Lake data sources

Customer Insights allows incremental refresh for data sources connected to Azure Data Lake Storage. To use incremental ingestion and refresh for a table, configure that table when adding the Azure Data Lake data source or later when editing the data source. The table data folder must contain the following folders:

- **FullData**: Folder with data files containing initial records
- **IncrementalData**: Folder with date/time hierarchy folders in **yyyy/mm/dd/hh** format containing the incremental updates. **hh** represents the UTC hour of the updates and contains the **Upserts** and **Deletes** folders. **Upserts** contains data files with updates to existing records or new records. **Deletes** contains data files with records to be removed.

1. When adding or editing a data source, navigate to the **Attributes** pane for the table.

1. Review the attributes. Make sure a created or last updated date attribute is set up with a *dateTime* **Data format** and a *Calendar.Date* **Semantic type**. Edit the attribute if necessary and select **Done**.

1. From the **Select Tables** pane, edit the table. The **Incremental ingestion** checkbox is selected.

   :::image type="content" source="media/ADLS_inc_refresh.png" alt-text="Configure tables in a data source for incremental refresh.":::

   1. Browse to the root folder that contains the .csv or .parquet files for full data, incremental data upserts, and incremental data deletes.
   1. Enter the extension for the full data and both incremental files (\.csv or \.parquet).
   1. For .csv files, select the column delimiter and if you want the first row of the file as a column header.
   1. Select **Save**.

1. For **Last updated**, select the date timestamp attribute.

1. If the **Primary key** is not selected, select the primary key. The primary key is an attribute unique to the table. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.

1. Select **Close** to save and close the pane.

1. Continue with adding or editing the data source.

[!INCLUDE [footer-include](includes/footer-banner.md)]
