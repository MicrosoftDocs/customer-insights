---
title: "Data sources overview"
description: "Learn how to import or ingest data from various sources."
ms.date: 06/24/2024
ms.topic: overview
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Data sources overview

To configure Dynamics 365 Customer Insights - Data, first bring in source data for processing. Customer Insights - Data provides several types of data connectors to connect to and ingest data from a broad set of sources.

This article describes options that can affect data ingestion performance.

## Delta format

The Delta data format is the native processing format used by Customer Insights – Data. If you can provide source data in the Delta format, there are many advantages.

- **Better efficiency with Customer Insights - Data**: Delta format is used internally by Customer Insights - Data.
- **Faster data ingestion**: Delta format provides superior compression for faster data transfers.
- **Faster unification**: With the [Delta time travel feature](connect-delta-lake.md#delta-lake-time-travel-and-data-refreshes), Customer Insights – Data unifies just the changed data rather than reprocessing the entire set of data. Incremental unification requires all data inputs to unification be in the Delta format.
- **Reduction in data corruption issues**: Reduces corrupted partitions and common data corruption issues caused by older formats such as CSV.
- **More reliable data management design**: Delta format doesn't require manual updates to manifests, schemas, and partition files.
- **Higher data validity**: Delta format provides atomicity, consistency, isolation, durability (ACID) transactions, and isolation levels in Spark.

You can use Delta format with the following connectors:

- [Azure Data Lake Delta tables](connect-delta-lake.md)
- [Microsoft Dataverse](connect-dataverse.md)

[!INCLUDE [delta-lake-info](./includes/delta-lake-info.md)]

## Data source attachment or import

A key consideration when choosing how to ingest your data is whether the connector attaches to the data or makes copies of the data. Customer Insights - Data recommends attaching to data because the data is directly accessed when it's time to process it. Copying the data causes delays when the data is updated.

The following data connectors attach to your data.

- [Azure Data Lake Delta tables](connect-delta-lake.md)
- [Azure Data Lake Storage Common Data Model tables](connect-common-data-model.md)
- [Microsoft Dataverse](connect-dataverse.md)
- [Azure Synapse Analytics (preview)](connect-synapse.md)

If you can't use one of the attached connectors, copy data with one of the [Power Query connectors](connect-power-query.md). Power Query provides a useful way to transform the data.

## Data profiling

When data is ingested, Customer Insights – Data performs some basic data profiling such as the frequency of repeated values in a column. You can use profile data to understand your data and address issues. For example, if you're matching on the column FullName, data profile can help you detect that a default value of "Enter your name" appears on 10K rows. Matching on this value would cause 10K rows to match that shouldn’t. You can enable data profiling for more columns when you add your Azure Data Lake, Delta tables, or Azure Synapse data sources.

After you ingest the data, view the results of data profiling:

Go to **Data** > **Tables** and select a table. Select the **Summary** icon for a field, such as DateOfBirth.

   :::image type="content" source="media/tables-summary-icon.png" alt-text="Tables page showing Summary icon highlighted on DateOfBirth.":::

View the details for any errors or missing values.

   :::image type="content" source="media/tables-dateofbirth.png" alt-text="Summary graph for DateOfBirth.":::

## Data sources page

The **Data Sources** page lists the data sources in two sections:

- **Managed by me**: Power Platform dataflows created and managed only by you. Other users can only view these dataflows but not edit, refresh, or delete them.
- **Managed by others**: Power Platform dataflows created by other admins. You can only view them. It lists the owner of the dataflow to reach out to for any assistance.

> [!NOTE]
> All tables can be viewed and used by other users. While data sources are owned by the user who created them, the resulting tables from the data ingestion can be used by every user of Customer Insights - Data.

:::image type="content" source="media/data-sources.png" alt-text="Screenshot of the Data sources screen.":::

## Next steps

- [Manage data sources](data-sources-manage.md)
- [Unify data sources](data-unification.md)
- [FastTrack blog: Data integration patterns - introduction](https://community.dynamics.com/blogs/post/?postid=f32d115e-d9cb-ee11-92bd-000d3a7e795a)

[!INCLUDE [footer-include](includes/footer-banner.md)]
