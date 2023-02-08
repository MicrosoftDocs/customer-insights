---
title: "Get started with Customer Insights using a single data source"
description: "Learn how to ingest data from a single file or from sample data"
ms.date: 02/07/2023
ms.topic: overview
author: wmelewong
ms.author: wameng
ms.reviewer: v-wendysmith
ms.custom: bap-template
searchScope: 
  - ci-data-sources
  - ci-create-data-source
  - customerInsights
---

# Get started with Customer Insights using a single data source

Dynamics 365 Customer Insights provides ingestion of a single data source to get you up and running quickly. Provide your own data in a .csv file or choose sample data.

## Prerequisites

- File must be a CSV file with only letters, numbers, and _ in the file name
- File must contain more than 100 rows and 5 columns
- File must include at least one column of each data category:
  - Identity: Customer number, email, SSN
  - Demographics: Address, DOB, gender
  - Business: Loyalty points, total spending

## Upload a single data source

1. From the **Home** page, select **Add data** on the **Get insights in mins** card. From the Getting Started page, select **Add data**.

   :::image type="content" source="media/get-started.png" alt-text="Screenshot of Getting started for getting insights in minutes.":::

1. Select **Get started**.

   :::image type="content" source="media/get-started-add-data.png" alt-text="Screenshot of Getting Started - Add Data to add your single CSV file.":::

1. To use your own data, browse or drag and drop your file. To use sample data, select **Download Microsoft’s sample data** and load the sample file. If the file meets the prerequisites, **Next** displays.

1. Select **Next**. Customer Insights identifies a unique key for your data source called the primary key.

1. Select **Yes** to verify the primary key or choose another field as the primary key for your data source. Select **Next**. Customer Insights checks the data quality.

   > [!TIP]
   > If an error occurs during data processing, Customer Insights explains the issue in a message and provides an action to take. For example, if required attributes needed to generate insights are not identified, click [**Map data**](#map-required-data).

   After the data quality checks, Customer Insights removes duplicate records, creates customer profiles, and generates insights such as segments and measures.

1. Upon a successful completion, the **Results** page displays results from your file:
   - Unique number of customers
   - Number of duplicate rows
   - Suggested segments and measures

   :::image type="content" source="media/get-started-results.png" alt-text="Screenshot of Getting Started - Results.":::

1. Select **Done** to go to the **Home** page.

### Map required data

1. Under the **Needs mapping** tab, select each field in your file that matches the list of fields displayed.

1. Review all mapped fields under the **All mapped** tab and make changes if necessary.

1. Select **Next**.

## Next steps

- [Review generated segments or create new ones](segments.md)
- [Review generated measures or create new ones](measures.md)
- [Export your data to various business apps and tools](export-destinations.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
