---
title: "Use unified profiles in Dynamics 365 Marketing"
description: "Learn how to integrate unified profiles and segments with Dynamics 365 Marketing."
ms.date: 03/09/2023
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
---

# Use unified customer profiles in Dynamics 365 Marketing

[Dynamics 365 Marketing](/dynamics365/marketing/overview) elevates customer experiences, allowing you to orchestrate personalized journeys across all touchpoints to strengthen relationships and earn loyalty. The Dynamics 365 Marketing app works seamlessly with Dynamics 365 Sales, Dynamics 365 Customer Insights, Microsoft Teams, and other products and allows you to make faster and better decisions using the power of data and AI.

By connecting Customer Insights data with Marketing, you can:

- Target unified customer profiles and segments. This enables you to engage every customer, regardless of the location of the customer's data.
- Base dynamic content (such as personalized tokens) in emails, SMS, and push notifications on measures such as loyalty status, subscription renewal date, parent account, or any other measure you've captured in the unified Customer Insights profile.
- Load data from Marketing into Customer Insights and combine it with customer data from other sources.
- Apply Customer Insights data cleansing, enrichment, and fuzzy matching tools.

## Use rich customer profiles in real-time marketing

Real-time marketing allows you to creates customer journeys based on events or segments. The more personalized your data, the more relevant and personalized your journeys will be. If both applications use the same Microsoft Dataverse environment, you can [establish a seamless connection](/dynamics365/marketing/real-time-marketing-ci-profile). Data is automatically updated for both applications thanks to the shared data service. As soon as a segment in Customer Insights refreshes, it's already available in Marketing. This is what makes combining Marketing and Customer Insights so powerful. You can [unify data](data-unification.md) from any source, then use it to fuel hyper-personalized customer journeys.

Learn more: [Use Customer Insights profiles and segments in real-time marketing](/dynamics365/marketing/real-time-marketing-ci-profile)

## Export segments to use in outbound marketing

Customer Insights allows you to refine data from many sources and combine it into aggregated customer segments. By [connecting Customer Insights and exporting segments to outbound marketing](export-dynamics365-marketing.md), you make customer segments available in Marketing. These segments get updated based on the export cadence you define.

Learn more: [Use segments from Dynamics 365 Customer Insights with Dynamics 365 Marketing](/dynamics365/marketing/customer-insights-segments)

## Pull data from your own Azure Data Lake Storage

You aren't limited to cloud storage if you want to use Customer Insights data with Marketing. If you already have your own Azure Data Lake Storage set up, you can connect with Customer Insights, then share the data with the Marketing app just as you would with a cloud-based setup.

Learn more: [Enable data sharing with Dataverse from your own Azure Data Lake Storage](customer-insights-dataverse.md#enable-data-sharing-with-dataverse-from-your-own-azure-data-lake-storage-preview)
