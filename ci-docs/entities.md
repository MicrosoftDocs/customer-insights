---
title: "Entities in Customer Insights"
description: "View data on the Entities page."
ms.date: 08/04/2022
ms.reviewer: mhart
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

[!INCLUDE [footer-include](includes/footer-banner.md)]
