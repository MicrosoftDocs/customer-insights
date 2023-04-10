---
title: Data preparation overview
description: "Discover the overall quality of ingested and unified data and if it can generate predictions."
ms.date: 04/17/2023
ms.reviewer: v-wendysmith
ms.topic: overview
author: radsay01
ms.author: rsayyaparaju 
ms.custom: bap-template
---

# Data preparation overview

The data preparation model in Customer Insights helps you understand the overall data quality, the readiness of your data to produce insights, and helps you improve your data to unlock more and better predictions for whatever sales or marketing strategy you have in mind. It includes an automated data preparation report as well as contextual information on your data to support you during scenarios and tasks across the product.

## Prerequisites

Data preparation automatically runs if the following prerequisites have been met:

- [Ingestion](data-sources.md) completed with customer and transaction data.
- [Unification](data-unification.md) completed.
- [Activities](activities.md) and relationships mapped.
- [System data preparation setting](data-prep-admin.md) turned **On**, which is the default.
- At least 100 customer records, preferably 1,000 records.
- At least one year of transaction history, preferably two to three years. Ideally two to three transactions per customer ID, preferably across multiple dates.
- Customer identifier: A unique identifier to match transactions to to your customers.
- Less than 20% missing values in required fields

## Data preparation report

After unification is completed, Customer Insights automatically generates the data preparation report and analyzes contextual information on your data. You can access the data preparation report from the **Home** page, the **Data sources** page and the **Predictions**.

There are three primary sections within the data preparation report.

- **Data quality grade**: The grade indicates overall health of your data. The grade is calculated as an aggregated percentage (value ranging from 0-100%) with a corresponding level (high, medium, or low data quality), derived from averaging scores across a set of data quality rules within seven industry-standard data quality pillars (completeness, consistency, uniqueness, accuracy, timeliness, validity, and integrity). If you have a high grade and corresponding high level of data quality, you can assume the quality of your data is sufficient to generate most of the insights available in the product with high confidence in meaningful results.

- **Insights readiness**: Data insights readiness indicates whether or not you have met the requirements to generate a specific insight. It is determined by comparing the baseline data requirements of each insight with the issues present in your data. When any issue violates any data requirement for an insight, the insight is deemed not ready to use. If an insight is deemed ready to use, it is likely to generate meaningful results.

- **Data quality issues and recommendations**: These issues and recommendations provide comprehensive guidance on the issues surfaced in your data, including severity, which insights are impacted, and what recommendations for remediation to act upon. Issues are derived from the data quality rules within the same seven industry-standard data quality pillars as the data quality grade. Any violation of these rules results in an issue. The less issues present, especially critical severity issues, the more likely you are to have a high data quality grade and have all insights labeled as ready to use.

  > [!TIP]
  > The default view provides the most critical issues present in your data. To see all issues, organized by severity, select **Expand**. To alter the view to show issues organized by other options, select **Group by**.

## Contextual information on your data

In addition to the data preparation report, Customer Insights provides contextual information related to the **Predictions** page. Use this information to understand which prediction models are best suited to your data, before you go through the time and effort of configuration and running the model. Models labeled as **Ready to use** are most suited to your data while those labeled as **Not ready to use** are not. For any **Not ready to use** models, click the model card to see more contextual information, review the full data preparation report, and make the necessary fixes to your data per the guidance of the Issues and recommendations section.

Details on which prediction models are ready or not to use are available in each out-of-box model card. Information on the data quality impacting each prediction model is available in the right-side pane when a model is selected. The header shows a data quality grade specific to prediction models with a link to the full data preparation report.

## Next steps

- [Data preparation report FAQ](Data-prep-faq.md)
- [Predictions overview](predictions-overview.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
