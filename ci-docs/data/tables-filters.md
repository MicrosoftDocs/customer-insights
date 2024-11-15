---
title: Filter out unwanted data from your ingested data
description: Filter out unwanted rows from your ingested source data in Customer Insights - Data
ms.date: 11/15/2024
ms.reviewer: v-wendysmith
ms.topic: conceptual
author: Scott-Stabbert
ms.author: sstabbert
---

# Filter out unwanted data from your ingested data

Improve the quality of your unified customer profiles and insights by filtering out unwanted rows from your ingested source data. Filtering data that doesn’t provide value helps create higher quality insights in less time.

Key benefits include:

- **Improved processing time**: By removing unwanted rows, the system no longer processes data that isn’t needed, reducing time and resources.
- **Streamlined data sets**: Removing unnecessary data improves processing time, particularly with large data sets. Columns that aren’t used for matching or needed in the final output can now be filtered out before processing.
- **Targeted final output**: Filtering out irrelevant data, such as old records or data from regions where you don’t operate anymore, results in a more focused and relevant output.

Apply row filters directly to any source table you ingest, reducing the data scope to just what you need.

## Filter out unwanted rows

Select row filters for just the rows you need in any source table. Only the filtered tables are used across all processes in Customer Insights – Data. Processes include unification, segments, measures, activities, and predictive models.

1. Go to **Data** > **Tables**.

   :::image type="content" source="media/tables-source-tab.png" alt-text="Screenshot of the Source tab on the Tables page.":::

1. Select the **Source** tab.
1. Selec the row filter link for any table and set the filters. The type of data determines the filter options.

   :::image type="content" source="media/tables-filter-rows.png" alt-text="Screenshot of the Filter rows dialog box.":::

1. After setting the filter criteria, select **Apply**. All processes will use the filtered tables.