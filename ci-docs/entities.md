---
title: "Entities in Customer Insights"
description: "View data on the Entities page."
ms.date: 12/06/2021
ms.reviewer: mhart
ms.subservice: audience-insights
ms.topic: conceptual
author: mukeshpo
ms.author: mukeshpo
manager: shellyha
searchScope: 
  - ci-entities
  - customerInsight
---

# Entities in Customer Insights

After [configuring your data sources](data-sources.md), go to the **Entities** page to evaluate the quality of the ingested data. Entities are considered datasets. Multiple capabilities of Dynamics 365 Customer Insights are built around these entities. Reviewing them closely can help you validate the output of those capabilities.

As you work in Customer Insights enriching your data or creating segments, measures, and activities, the entities that are created from those actions display on the **Entities** page.

## View a list of entities

Go to **Data** > **Entities** to view a list of entities. The following information displays for each entity.

- **Name**: Name of the data entity. If you see a warning symbol next to an entity name, it means that the data for that entity didn't load successfully.
- **Source**: Type of data source that ingested the entity.
- **Updated**: Time the entity was last updated.
- **Status**: Details about the last update of the entity.

## Explore a specific entity's data

1. Go to **Data** > **Entities**.
1. Select an entity to open the details page.  
1. Explore the different fields and records included for that entity.

- The **Attributes** tab is selected by default and shows details for the selected entity, such as field names, data types, and types. The **Type** column shows Common Data Model associated types, which are either auto-identified by the system or [manually mapped](map-entities.md) by users. These types are semantic types that can differ from the attributes' data types. For example, the field *Email* below has a data type *String* but its (semantic) Common Data Model type might be *Email*, *EmailAddress*, or *Identity.Service.Email*.

   :::image type="content" source="media/data-manager-entities-fields.png" alt-text="Fields table.":::

   > [!NOTE]
   > This page shows only a sample of your entity's data. To view the full data set, go to the **Data sources** page, select an entity, select **Edit**, and then view this entity's data with the Power Query editor as explained in [Data sources](data-sources.md).

   To learn more about the data ingested in the entity, the **Summary** column provides some important data characteristics, such as nulls, missing values, unique values, counts, and distributions, whatever is applicable to your data. Select the chart icon to see the summary of the data.

   :::image type="content" source="media/data-manager-entities-summary.png" alt-text="Data summary table.":::

- The **Data** tab shows details about individual records of the entity. Details listed depend on the entity's data type.

   :::image type="content" source="media/data-manager-entities-data.png" alt-text="Select an entity.":::

- The **Reports** tab (available for some entities) enables you to visualize your data by creating a report, which includes these columns:

  - **Report name**: Name of the report.
  - **Created by**: Name of the person who created the entity.
  - **Created**: Date and time of the entity creation.
  - **Edited by**: Name of the person who modified the entity.
  - **Edited**: Date and time of the entity modification.

## Entity-specific information

The following section provides information about some system-created entities.

### Corrupted data sources

Fields from an ingested data source can contain corrupted data. Records with corrupted fields are exposed in system-created entities. Knowing about corrupted records helps you identify which data to review and update on the source system. After the next refresh of the data source, the corrected records are ingested to Customer Insights and passed on to downstream processes. 

For example, a 'birthday' column has the datatype set as 'date'. A customer record has their birthday entered as '01/01/19777'. The system will flag this record as corrupted. Someone can now change the birthday in the source system to '1977'. After an automated refresh of data sources, the field now has a valid format and the record will be removed from the corrupted entity.

Go to **Data** > **Entities** and look for the corrupted entities in the **System** section. Naming schema of corrupted entities: 'DataSourceName_EntityName_corrupt'. Select a corrupted entity to identify the corrupted fields and the reason at the individual record level.

   :::image type="content" source="media/corruption-reason.png" alt-text="Corruption reason.":::

Customer Insights still processes corrupted records. However, they might cause issues when working with the unified data.

The following checks run on the ingested data to expose corrupted records:

- The value of a field doesn't match with the data type of its column.
- Fields contain characters that cause the columns to not match the expected schema. For example: incorrectly formatted quotes, unescaped quotes, or newline characters.
- If there are datetime/date/datetimeoffset columns, their format needs to be specified in the model if it doesn't follow the standard ISO format.

[!INCLUDE [footer-include](includes/footer-banner.md)]
