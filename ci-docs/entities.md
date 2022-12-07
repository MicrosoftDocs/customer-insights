---
title: "Tables in Customer Insights"
description: "View data on the Tables page."
ms.date: 12/7/2022
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

# Tables in Customer Insights

After [configuring your data sources](data-sources.md), go to the **Tables** page to evaluate the quality of the ingested data. Tables are considered datasets and were previously called entities. Multiple capabilities of Dynamics 365 Customer Insights are built around these tables. Reviewing them closely can help you validate the output of those capabilities.

As you work in Customer Insights enriching your data or creating segments, measures, and activities, the tables that are created from those actions display on the **Tables** page.

## View a list of tables

Go to **Data** > **Tables** to view a list of tables. The following information displays for each table.

- **Name**: Name of the data table. If you see a warning symbol next to a table name, it means that the data for that table didn't load successfully.
- **Source**: Type of data source that ingested the table.
- **Updated**: Time the table was last updated.
- **Status**: Details about the last update of the table.

For more information about the **Relationships** tab, see [Relationships](relationships.md).

## Explore a specific table's data

1. Go to **Data** > **Tables**.
1. Select a table to open the details page.  
1. Explore the different fields and records included for that table.

- The **Attributes** tab is selected by default and shows details for the selected table, such as field names, data types, and types. The **Type** column shows Common Data Model associated types, which are either auto-identified by the system or [manually mapped](map-entities.md) by users. These types are semantic types that can differ from the attributes' data types. For example, the field *Email* below has a data type *String* but its (semantic) Common Data Model type might be *Email*, *EmailAddress*, or *Identity.Service.Email*.

   :::image type="content" source="media/data-manager-entities-fields.png" alt-text="Fields table.":::

   > [!NOTE]
   > This page shows only a sample of your table's data. To view the full data set, go to the **Data sources** page, select a table, select **Edit**, and then view this table's data with the Power Query editor as explained in [Data sources](data-sources.md).

   To learn more about the data ingested in the table, the **Summary** column provides some important data characteristics, such as nulls, missing values, unique values, counts, and distributions, whatever is applicable to your data. Select the chart icon to see the summary of the data.

- The **Data** tab shows details about individual records of the table. Details listed depend on the table's data type.

   :::image type="content" source="media/data-manager-entities-data.png" alt-text="Select a table.":::

- The **Reports** tab (available for some tables) enables you to visualize your data by creating a report, which includes these columns:

  - **Report name**: Name of the report.
  - **Created by**: Name of the person who created the table.
  - **Created**: Date and time of the table creation.
  - **Edited by**: Name of the person who modified the table.
  - **Edited**: Date and time of the table modification.

[!INCLUDE [footer-include](includes/footer-banner.md)]
