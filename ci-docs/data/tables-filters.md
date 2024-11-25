---
title: Filter out unwanted data from your ingested data
description: Filter out unwanted rows from your ingested source data in Customer Insights - Data
ms.date: 11/25/2024
ms.reviewer: v-wendysmith
ms.topic: conceptual
author: Scott-Stabbert
ms.author: sstabbert
---

# Filter out unwanted data from your ingested data

Remove unwanted rows from your source data before processing in Customer Insights – Data to improve the performance and quality of your unified customer profiles and insights.

Key benefits include:

- **Improved processing time**: Filtering out unnecessary data like old or obsolete rows can reduce the time required to process the data. Filtering out a significant percentage of unwanted rows can substantially improve performance.
- **Simplify data configuration**: Removing unwanted data at the source eliminates the need to create rules in multiple locations to avoid incorporating the unwanted data. Unification, segments, measures, activities, and predictive insights will use the filtered source data.
- **Improve data quality**: Removing old or obsolete data at the source prevents it from being accidentally included in your results, such as when a new team member creates a segment that includes obsolete data.

## Filter out unwanted rows

After [configuring your data sources](data-sources.md), apply row filters before processing. Only the filtered table data is then processed when running unification, segments, measures, activities, and predictive models.

1. Go to **Data** > **Tables**.

   :::image type="content" source="media/tables-source-tab.png" alt-text="Screenshot of the Source tab on the Tables page.":::

1. Select the row filter link for any table and set the filters. The type of data determines the filter options.

   :::image type="content" source="media/tables-filter-rows.png" alt-text="Screenshot of the Filter rows dialog box.":::

1. After setting the filter criteria, select **Apply**. All processes will use the filtered tables.

> [!NOTE]
> If you export a source table ingested in .csv or .parquet format, the export includes the full, unfiltered data.

[!INCLUDE [footer-include](includes/footer-banner.md)]
