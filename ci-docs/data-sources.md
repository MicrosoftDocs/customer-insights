---
title: "Data sources overview"
description: "Learn how to import or ingest data from various sources."
ms.date: 08/04/2022

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

Go to **Data** > **Data sources** to view the name of each ingested data source, its status, and the last time the data was refreshed for that source. You can sort the list of data sources by any column or use the search box to find the data source you want to manage.

Select a data source to view available actions.

:::image type="content" source="media/data_sources_showmore.png" alt-text="Data source added.":::

- [**Edit**](#add-or-edit-data-sources) the data source to change its properties.
- [**Refresh**](#refresh-data-sources) the data source to include the latest data.
- [**Enrich**](data-sources-enrichment.md) the data source before unification.
- **Delete** the data source. A data source can be deleted only if the data is not used in any processing such as unification, insights, activations, or exports.

## Refresh data sources

Data sources can be refreshed on an automatic schedule or refreshed manually on demand. [On-premise data sources](connect-power-query.md#add-data-from-on-premises-data-sources) refresh on their own schedules which are set up during data ingestion. For attached data sources, data ingestion consumes the latest data available from that data source.

Go to **Admin** > **System** > [**Schedule**](system.md#schedule-tab) to configure system-scheduled refreshes of your ingested data sources.

To refresh a data source on demand:

1. Go to **Data** > **Data sources**.

1. Select the data source you want to refresh and select **Refresh**. The data source is now triggered for a manual refresh. Refreshing a data source will update both the entity schema and data for all the entities specified in the data source.

1. Select the status to open the **Progress details** pane and view the progress. To cancel the job, select **Cancel job** at the bottom of the pane.

## Corrupted data sources

Fields from an ingested data source can contain corrupted data. Records with corrupted fields are exposed in system-created entities. Knowing about corrupted records helps you identify which data to review and update on the source system. After the next refresh of the data source, the corrected records are ingested to Customer Insights and passed on to downstream processes. Customer Insights still processes corrupted records. However, they might cause issues when working with the unified data.

For example, a 'birthday' column has the datatype set as 'date'. A customer record has their birthday entered as '01/01/19777'. The system will flag this record as corrupted. Someone can now change the birthday in the source system to '1977'. After an automated refresh of data sources, the field now has a valid format and the record will be removed from the corrupted entity.

The following checks run on the ingested data to expose corrupted records:

- The value of a field doesn't match with the data type of its column.
- Fields contain characters that cause the columns to not match the expected schema. For example: incorrectly formatted quotes, unescaped quotes, or newline characters.
- If there are datetime/date/datetimeoffset columns, their format must be specified in the model if it doesn't follow the standard ISO format.

### Fix corrupted data

1. Go to **Data** > **Entities** and look for the corrupted entities in the **System** section. The naming schema of corrupted entities: 'DataSourceName_EntityName_corrupt'.

1. Select a corrupted entity to identify the corrupted fields and the reason at the individual record level.

   :::image type="content" source="media/corruption-reason.png" alt-text="Corruption reason.":::

1. Fix the corrupted data. For example, for Azure Data Lake data sources, fix the data in the Data Lake Storage or in the manifest/model.json file. For Power Query data sources, fix the data in the source file and correct the data type in the transformation step on the **Power Query - Edit queries** page.

After the next refresh of the data source, the corrected records are ingested to Customer Insights and passed on to downstream processes.

### Common reasons for corrupted data

- Datetime fields in the wrong format

  The datetime fields in the entity are not in ISO or en-US formats. Ideally, all the datetime fields in an entity should be in the same format, but Customer Insights can work with different columns being in different formats if they are in the ISO format. However, if it is not possible to use ISO or en-US formats, Customer Insights supports an entity with a different format, but the datetime formats must be annotated in the manifest/model.

  > [!TIP]
  > The default datetime format in Customer Insights is en-US format.

- Schema mismatch
  - Data that does not conform to the schema can be caused by a difference in the number of columns in the data vs the schema or differences in the data types between the data and the schema. Correct either the source data or the schema.
  - The presence of newline characters in the data splits the row into multiple rows at unintended locations causing data from different rows to be present in different rows.

[!INCLUDE [footer-include](includes/footer-banner.md)]
