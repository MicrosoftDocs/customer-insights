---
title: "Real-Time Web Personalization"
description: "Learn how to track web interactions and personalize experiences in real-time"
ms.date: 12/07/2023
ms.topic: overview
author: srivas15
ms.author: srivas15
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Real-Time Web Personalization

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

As customers engage with your business, they constantly provide signals about their interests and preferences, such as adding a product to a cart, viewing your pricing quote, signing up for a trial, and more. It's crucial to build on these signals as they happen so you can deliver the right experience at the right time.
With Customer Insights - Data, you can now ensure customer profiles are updated in real-time based on these signals, allowing you to provide the most targeted and personalized experience to your customers as they engage with your website. This empowers you to foster loyalty, increase engagement, enhance satisfaction, and drive higher conversion rates.

Customer Insights - Data enables you to:
1. Track your customer's website interactions in real-time
2. Automatically let the system create [unknown profiles](link_to_unknown_profiles.md) if your customers are not authenticated 
3. Continuously enhance your customer profiles when they return to your website with progressive profiling
4. Seamlessly merge unknown profiles into known profiles in real-time, so you can always have the 360-degree view of your customers
5. Personalize your customer's web experience in real-time and engage with them in the moments that matter

This enables you to achieve the following scenarios:
1. Promote a premium coffee machine on your website if a customer browses other premium coffee machines 
2. Offer a discount code on the website to all your customers who are members of the 'high lifetime value' segment
3. Dynamically update the text on your website to add a welcome message to your loyal customers 
4. Send an email to your customers promoting your premium coffee machines if they read the reviews of similar products in the last 30 days

> [!TIP]
> To upload a single CSV file, unify the data, and automatically generate insights, go to [Get started using a single data source](data-sources-single.md).
> [!INCLUDE [single-file-us-only](includes/single-file-us-only.md)]

## Data source attachment or import

You can attach or import multiple data sources. The links below provide instructions on adding and editing data sources.

**Attach a data source**

If you have data prepared in one of Microsoft's Azure data services, you can easily connect to the data source without having to reingest the data. Select one of the following options:

- [Azure Data Lake Storage (csv or parquet files in a Common Data Model folder)](connect-common-data-model.md)
- [Azure Synapse Analytics (Lake databases)](connect-synapse.md)
- [Microsoft Dataverse data lake](connect-dataverse.md)
- [Delta Lake format from Azure Data Lake Storage (preview)](connect-delta-lake.md)

**Import and transform**

If you use on-premises data sources, Microsoft, or third-party data, import and transform the data using Power Query connectors.
- [Power Query connectors](connect-power-query.md)

## Data sources page

If your environment was configured to use the default system storage and you use on-premises data sources, you use Power Platform dataflows. The **Data Sources** page lists the data sources in two sections:

- **Managed by me**: Power Platform dataflows created and managed only by you. Other users can only view these dataflows but not edit, refresh, or delete them.
- **Managed by others**: Power Platform dataflows created by other admins. You can only view them. It lists the owner of the dataflow to reach out to for any assistance.

> [!NOTE]
> All tables can be viewed and used by other users. While data sources are owned by the user who created them, the resulting tables from the data ingestion can be used by every user of Customer Insights - Data.

## Next steps

- [Manage data sources](data-sources-manage.md)
- [Unify data sources](data-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
