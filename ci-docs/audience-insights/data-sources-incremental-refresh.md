---
title: "Incremental refresh for Azure data lake and Databricks data sources"
description: "Refresh new and updated data for large data sources."
ms.date: 03/07/2022
ms.reviewer: v-wendysmith

ms.subservice: audience-insights
ms.topic: how-to
author: v-wendysmith
ms.author: v-wendysmith
manager: shellyha
searchScope: 
  - ci-system-schedule
  - customerInsights
---

# Incremental refresh for Azure data lake and Databricks data sources

This article discusses how to configure incremental refresh for Azure data lake and Databricks delta lake data sources. Customer Insights allows incremental refresh for data sources that support incremental ingestion. For example, Azure SQL databases with date and time fields, which indicate when data records were last updated.

Incremental refresh for data sources provides the following advantages:

- **Faster refreshes** - Only data that has changed gets refreshed. For example, you might refresh only the past five days of a historical dataset.
- **Increased reliability** - With smaller refreshes, you don't need to maintain connections to volatile source systems for as long, reducing the risk of connection issues.
- **Reduced resource consumption** - Refreshing only a subset of your total data leads to more efficient use of computing resources and decreases the environmental footprint.

## Configure incremental refresh

You can configure incremental refresh when adding the data source or later when editing the data source.

1. When adding or editing a data source, navigate to the attributes pane.

1. Review the attributes. Make sure a created or last updated date attribute is set up with a *dateTime* **Data format** and a *Calendar.Date* **Semantic type**. Edit the attribute if necessary.

1. From the **Select Entities** pane, edit the entity.

1. Select the **Incremental refresh** checkbox.

1. Select a date timestamp.

1. Select **X** to save and close the pane.

1. Continue with adding or editing the data source.
