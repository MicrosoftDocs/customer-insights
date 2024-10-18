---
title: Data sources overview
description: Learn how to import or ingest data from various sources.
ms.date: 06/24/2024
ms.topic: overview
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Data sources overview

To configure Dynamics 365 Customer Insights - Data, first bring in source data for processing. Customer Insights - Data provides several types of data connectors to connect to and ingest data from a broad set of sources.

This article describes options that can affect the performance of data ingestion.

## Delta format

The Delta data format is the native processing format that Customer Insights – Data uses. If you can provide source data in the Delta format, there are many advantages.

- **Better efficiency with Customer Insights - Data**: Customer Insights - Data uses Delta format internally.
- **Faster data ingestion**: Delta format provides superior compression for faster data transfers.
- **Faster unification**: When the [Delta time travel feature](connect-delta-lake.md#delta-lake-time-travel-and-data-refreshes) is used, Customer Insights – Data unifies only data that changed. It doesn't reprocess the whole set of data. For incremental unification, all data inputs to unification must be in the Delta format.
- **Fewer data corruption issues**: Delta format reduces the corrupted partitions and common data corruption issues that are caused by older formats, such as comma-separated value (CSV) format.
- **More reliable data management design**: Delta format doesn't require manual updates to manifests, schemas, and partition files.
- **Higher data validity**: Delta format provides atomicity, consistency, isolation, durability (ACID) transactions, and isolation levels in Spark.

You can use Delta format with the following connectors:

- [Azure Data Lake Storage Delta tables](connect-delta-lake.md)
- [Microsoft Dataverse](connect-dataverse.md)

[!INCLUDE [delta-lake-info](./includes/delta-lake-info.md)]

## Data source attachment or import

When you're deciding how to ingest your data, a key consideration is whether the data connector attaches to the data or makes copies of it. When you use Customer Insights - Data, we recommend that you use a connector that attaches to the data. In this way, the data is directly accessed when it's time to process it. If you use a connector that copies the data, delays can occur when the data is updated.

The following data connectors attach to your data:

- [Azure Data Lake Storage Delta tables](connect-delta-lake.md)
- [Azure Data Lake Storage Common Data Model tables](connect-common-data-model.md)
- [Microsoft Dataverse](connect-dataverse.md)
- [Azure Synapse Analytics (preview)](connect-synapse.md)

If you can't use a connector that attaches to your data, copy the data by using one of the [Power Query connectors](connect-power-query.md). Power Query provides a useful way to transform the data.

## Data profiling

When data is ingested, Customer Insights – Data performs some basic data profiling. For example, it profiles the frequency of repeated values in a column. You can use profile data to understand your data and address issues. For example, if you're matching on the `FullName` column, data profiling can help you detect that the default value *Enter your name* appears in 10,000 rows. Therefore, if you match on this value, 10,000 rows that should not be matched will be matched. When you add your Azure data lake, Delta tables, or Azure Synapse data sources, you can enable data profiling for more columns.

After you ingest the data, you can view the results of data profiling.

1. Go to **Data** \> **Tables**, and select a table. Then, in the row for a field (for example, `DateOfBirth`), in the **Summary** column, select the **Summary** icon.

    :::image type="content" source="media/tables-summary-icon.png" alt-text="Screenshot of the Attributes tab on the page for the Customer table, highlighting the Summary icon for the DateOfBirth field.":::

1. Review the details for any errors or missing values.

    :::image type="content" source="media/tables-dateofbirth.png" alt-text="Screenshot that shows the summary for the DateOfBirth field, including the chart of top values by count.":::

## Data sources page

The **Data sources** page lists the data sources in two sections:

- **Managed by me**: Microsoft Power Platform dataflows that you created and manage. Other users can only view these dataflows. They can't edit, refresh, or delete them.
- **Managed by others**: Microsoft Power Platform dataflows that other admins created. You can only view these dataflows. This section shows the owner of each dataflow, so that you can contact them if you need any assistance.

> [!NOTE]
> Other users can view and use all tables. Although each *data source* is owned by the user who created it, every user of Customer Insights - Data can use all the *tables* that result from data ingestion.

:::image type="content" source="media/data-sources.png" alt-text="Screenshot of the Data sources page.":::

## Next steps

- [Manage data sources](data-sources-manage.md)
- [Unify data sources](data-unification.md)
- [FastTrack blog: Data integration patterns - introduction](https://community.dynamics.com/blogs/post/?postid=f32d115e-d9cb-ee11-92bd-000d3a7e795a)

[!INCLUDE [footer-include](includes/footer-banner.md)]
