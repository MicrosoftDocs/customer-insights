---
title: "Data sources overview"
description: "Learn how to import or ingest data from various sources."
ms.date: 06/07/2023
ms.topic: overview
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
ms.custom: bap-template
searchScope: 
  - ci-data-sources
  - ci-create-data-source
  - customerInsights
---

# Data sources overview

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Dynamics 365 Customer Insights provides connections to bring data from a broad set of sources. Connecting to a data source is often referred to as the process of *data ingestion*. After ingesting the data, you can [unify](data-unification.md), generate insights, and activate the data for building personalized experiences.

> [!TIP]
> To upload a single CSV file, unify the data, and automatically generate insights, go to [Get started with Customer Insights using a single data source](data-sources-single.md).
> [!INCLUDE [single-file-us-only](includes/single-file-us-only.md)]

## Data source attachment or import

You can attach or import multiple data sources into Customer Insights. The links below provide instructions on adding and editing data sources.

**Attach a data source**

If you have data prepared in one of Microsoft's Azure data services, Customer Insights can easily connect to the data source without having to reingest the data. Select one of the following options:

- [Azure Data Lake Storage (csv or parquet files in a Common Data Model folder)](connect-common-data-model.md)
- [Azure Synapse Analytics (Lake databases)](connect-synapse.md)
- [Microsoft Dataverse data lake](connect-dataverse-managed-lake.md)

**Import and transform**

If you use on-premises data sources, Microsoft, or third-party data, import and transform the data using Power Query connectors.
- [Power Query connectors](connect-power-query.md)

## Data sources page

If your environment was configured to use Customer Insights storage and you use on-premises data sources, you use Power Platform dataflows. The **Data Sources** page lists the data sources in two sections:

- **Managed by me**: Power Platform dataflows created and managed only by you. Other Customer Insights admins can only view these dataflows but not edit, refresh, or delete them.
- **Managed by others**: Power Platform dataflows created by other admins. You can only view them. It lists the owner of the dataflow to reach out to for any assistance.

> [!NOTE]
> All tables can be viewed and used by other users. While data sources are owned by the user who created them, the resulting tables from the data ingestion can be used by every user of Customer Insights.

## Next steps

- [Manage data sources](data-sources-manage.md)
- [Unify data sources](data-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
