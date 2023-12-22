---
title: "Data sources overview"
description: "Learn how to import or ingest data from various sources."
ms.date: 12/08/2023
ms.topic: overview
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Data sources overview

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Dynamics 365 Customer Insights - Data provides connections to bring data from a broad set of sources. Connecting to a data source is often referred to as the process of *data ingestion*. After ingesting the data, you can [unify](data-unification.md), generate insights, and activate the data for building personalized experiences.

> [!TIP]
> To upload a single CSV file, unify the data, and automatically generate insights, go to [Get started using a single data source](data-sources-single.md).
> [!INCLUDE [single-file-us-only](includes/single-file-us-only.md)]

## Data source attachment or import

You can attach or import multiple data sources. The links below provide instructions on adding and editing data sources.

**Attach a data source**

If you have data prepared in one of Microsoft's Azure data services, you can easily connect to the data source without having to reingest the data. Select one of the following options:

- [Azure Data Lake Storage (csv or parquet files in a Common Data Model folder)](connect-common-data-model.md)
- [Azure Synapse Analytics (Lake databases)](connect-synapse.md)
- [Microsoft Dataverse data lake](connect-dataverse.md)
- [Delta Lake format from Azure Data Lake Storage (preview)](connect-delta-lake.md)

**Import and transform**

If you use on-premises data sources, Microsoft, or third-party data, import and transform the data using Power Query connectors.
- [Power Query connectors](connect-power-query.md)

## Data profiling

With data profiling, Customer Insights - Data looks at the frequency of values in a column and provides data to help you identify commonly duplicated values. When you have large numbers of duplicate values on a column that is expected to be unique, such as Email or Phone, it can skew your unification results. Enable data profiling when you add your Azure Data Lake, Delta tables, or Azure Synapse data sources.

After you have ingested the data, view the results of data profiling to look for duplicate values and also see analytics of your data. To view the results:

Go to **Data** > **Tables** and select a table. Select the **Summary** icon for a field, such as DateOfBirth.

   :::image type="content" source="media/tables-summary-icon.png" alt-text="Tables page showing Summary icon highlighted on DateOfBirth.":::

View the details for any errors or missing values.

   :::image type="content" source="media/tables-dateofbirth.png" alt-text="Summary graph for DateOfBirth.":::

## Data sources page

If your environment was configured to use the default system storage and you use on-premises data sources, you use Power Platform dataflows. The **Data Sources** page lists the data sources in two sections:

- **Managed by me**: Power Platform dataflows created and managed only by you. Other users can only view these dataflows but not edit, refresh, or delete them.
- **Managed by others**: Power Platform dataflows created by other admins. You can only view them. It lists the owner of the dataflow to reach out to for any assistance.

> [!NOTE]
> All tables can be viewed and used by other users. While data sources are owned by the user who created them, the resulting tables from the data ingestion can be used by every user of Customer Insights - Data.

## Next steps

- [Manage data sources](data-sources-manage.md)
- [Unify data sources](data-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
