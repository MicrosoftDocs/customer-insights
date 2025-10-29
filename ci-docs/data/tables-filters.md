---
title: Filter out unwanted data from your ingested data (preview)
description: Filter out unwanted rows from your ingested source data in Customer Insights - Data
ms.date: 10/29/2025
ms.reviewer: v-wendysmith
ms.topic: conceptual
author: Scott-Stabbert
ms.author: sstabbert
---
# Filter out unwanted data from your ingested data (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

Remove unwanted rows from your source data before processing in Customer Insights - Data to improve the performance and quality of your unified customer profiles and insights.

Key benefits include:

- **Improved processing time**: Filtering out unnecessary data like old or obsolete rows can reduce the time required to process the data. Filtering out a significant percentage of unwanted rows can substantially improve performance.
- **Simplified data configuration**: Removing unwanted data at the source eliminates the need to create rules in multiple locations to avoid incorporating the unwanted data. Unification, segments, measures, activities, and predictive insights will use the filtered source data.
- **Improved data quality**: Removing old or obsolete data at the source prevents it from being accidentally included in your results, such as when a new team member creates a segment that includes obsolete data.

Preview limitations include:

- [The preview of a source table's data](tables.md#explore-a-specific-tables-data) shows the full, unfiltered data.
- The export of a source table ingested in .csv or .parquet format contains the full, unfiltered data.

## How conditions are evaluated

When you add multiple conditions, all conditions must be true for a record to be included. This means conditions are combined using AND logic.

**Example**:

- **Field A** is not null
- **Field B** > 0

Result: Only rows where **Field A is not null AND Field B > 0** are processed.

> [!NOTE]
> Customer Insights - Data doesn't support combining conditions with OR across different fields. For example, you can’t filter rows where either Field A or Field B is true.

### Use "Any of" for string values

For string fields, you can use the **Any of** condition to apply OR logic within a single field.

**Example**:

- **Field A** is any of ("x", "y", "z")

Result: Rows are included if **Field A = "x" OR Field A = "y" OR Field A = "z"**.

### Combine AND and OR

You can combine AND logic across fields with OR logic within a single field.

**Example**:

- **Field A** is not null
- **Field B** is any of ("x", "y")

Result: Rows are included if **Field A is not null AND (Field B = "x" OR Field B = "y")**.

### Limitations

- OR logic is supported only within a single field using **Any of**.
- **Any of** isn't supported for numeric values.

## Filter out unwanted rows

After [configuring your data sources](data-sources.md), apply row filters before processing. Only the filtered table data is then processed when running unification, segments, measures, activities, and predictive models.

1. Go to **Data** > **Tables**.

   :::image type="content" source="media/tables-source-tab.png" alt-text="Screenshot of the Source tab on the Tables page.":::

1. Select the row filter link for any table and set the filters. The type of data determines the filter options.

   :::image type="content" source="media/tables-filter-rows.png" alt-text="Screenshot of the Filter rows dialog box.":::

1. After you set the filter criteria, select **Apply**. All processes use the filtered tables.

[!INCLUDE [footer-include](includes/footer-banner.md)]
