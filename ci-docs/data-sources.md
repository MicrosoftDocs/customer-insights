---
title: "Use data sources to ingest data"
description: "Learn how to import data from various sources."
ms.date: 05/31/2022

ms.subservice: audience-insights
ms.topic: overview
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-data-sources
  - ci-create-data-source
  - customerInsights
---

# Data sources overview

Dynamics 365 Customer Insights provides connections to bring data from a broad set of sources. Connecting to a data source is often referred to as the process of *data ingestion*. After ingesting the data, you can [unify](data-unification.md), generate insights, and activate the data for building personalized experiences.

## Add or edit data sources

You can attach or import data sources into Customer Insights. The links below provide instructions on adding and editing data sources.

**Attach a data source**

If you have data prepared in one of Microsoft's Azure data services, Customer Insights can easily connect to the data source without having to re-ingest the data. Select one of the following options:
- [Azure Data Lake Storage (csv or parquet files in a Common Data Model folder)](connect-common-data-model.md)
- [Azure Synapse Analytics (Lake databases)](connect-synapse.md)
- [Microsoft Dataverse data lake](connect-dataverse-managed-lake.md)

**Import and transform**

If you use on-premise data sources, Microsoft, or third-party data, import and transform the data using Power Query connectors.
- [Power Query connectors](connect-power-query.md)

## Review data sources

If your environment was configured to use Customer Insights storage and you use on-premise data sources, you use Power Platform dataflows. With Power Platform dataflows, you can view shared data sources and data sources managed by others. The **Data Sources** page lists the data sources in three sections:
- **Shared**: Data sources that can be managed by all Customer Insights admins. Power Platform dataflows, your own storage account, and attaching to a Dataverse-managed data lake are examples of shared data sources.
- **Managed by me**: Power Platform dataflows created and managed only by you. Other Customer Insights admins can only view these dataflows but not edit, refresh, or delete them.
- **Managed by others**: Power Platform dataflows created by other admins. You can only view them. It lists the owner of the dataflow to reach out to for any assistance.
> [!NOTE]
> All entities can be viewed and used by other users. While data sources are owned by the user who created them, the resulting entities from the data ingestion can be used by every user of Customer Insights.

If your environment does not use Power Platform dataflows, the **Data Sources** page contains only a list of all data sources. No sections display.

## Manage existing data sources

Go to **Data** > **Data sources** to view the name of each ingested data source, its status, and the last time the data was refreshed for that source. You can sort the list of data sources by every column.

Select the data source to see the available options. You can also select the vertical ellipsis (⋮) on a list item to see the options. If you added several data sources, you can use the search box to find it quickly.

:::image type="content" source="media/data_sources_showmore.png" alt-text="Data source added.":::

- **[Edit](#add-or-edit-data-sources** the data source.
- **[Refresh](#refresh-data-sources)** the data source.
- **[Enrich](data-sources-enrichment.md** the data source before unification.
- **Delete** the data source. A data source can be deleted only if the data is not used in any processing such as unification, insights, activations, or exports.

## Refresh data sources

Data sources can be refreshed on an automatic schedule or refreshed manually on demand. [On-premise data sources](connect-power-query.md#add-data-from-on-premises-data-sources) refresh on their own schedules which are set up during data ingestion. For attached data sources, data ingestion consumes the latest data available from that data source.

Go to **Admin** > **System** > [**Schedule**](system.md#schedule-tab) to configure system-scheduled refreshes of your ingested data sources.

To refresh a data source on demand:

1. Go to **Data** > **Data sources**.

1. Select the vertical ellipsis (&vellip;) next to the data source you want to refresh and select **Refresh** from the dropdown list. The data source is now triggered for a manual refresh. Refreshing a data source will update both the entity schema and data for all the entities specified in the data source.

1. Select **Stop refreshing** if you want to cancel an existing refresh and the data source will revert to its last refresh status.

[!INCLUDE [footer-include](includes/footer-banner.md)]
