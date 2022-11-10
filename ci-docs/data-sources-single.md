---
title: "Experience Customer Insights in 5 minutes"
description: "Learn how to ingest data from a single file or from sample data"
ms.date: 11/3/2022

ms.subservice: audience-insights
ms.topic: overview
author: wmelewong
ms.author: wameng
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-data-sources
  - ci-create-data-source
  - customerInsights
---

# Experience Customer Insights in 5 minutes

Dynamics 365 Customer Insights provides ingestion of a single data source to get you up and running quickly. Provide your own data in a .csv or .xlsx file or choose sample data.

## Prerequisites

- File must be a CSV or Excel file
- File must contain more than 100 rows and 5 columns
- File must include at least one column of each data category:
  - Identity: Customer number, email, SSN
  - Demographics: Address, DOB, gender
  - Business: Loyalty points, total spending

## Ingest single data source

1. Select **Get started**.

   > [!TIP]
   > If you bypassed the Getting started page, select **Add data** from the **Add your first file** tile on the **Home** page.

1. To use your own data, browse or drag and drop your file. To use sample data, select **Download Microsoft’s sample data**.

   If the file meets the prerequisites, **Next** displays.

1. Click **Next**. Customer Insights checks the data quality.

   > [!TIP]
   > If an error occurs during data processing, Customer Insights explains the issue in a message and provides an action to take. For example, if required attributes needed to generate insights are not identified, click [**Map data**](#map-required-data).

1. Click **Next**. Customer Insights removes duplicate records, creates customer profiles, and generates insights such as segments and measures.

1. While waiting for your data to process, click the link to learn more about Customer Insights. Proceed through the tutorial.

1. Upon a successful completion, the **Results** page displays results from your file:
   - Data quality checks which can be viewed in a report
   - Number of mapped columns
   - Number of missing rows
   - Number of duplicate rows
   - Suggested segments and measures

1. To export the segments, select **export page**. Otherwise, select **Done** to go to the **Home** page.

### Map required data

1. Under the **Needs mapping** tab, select each field in your file that matches the list of fields displayed.

1. Review all mapped fields under **All mapped** tab and make changes if necessary.

1. Select **Next**.

[!INCLUDE [footer-include](includes/footer-banner.md)]
