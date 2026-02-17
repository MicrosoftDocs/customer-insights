---
title: "Use unified profiles in Dynamics 365 Customer Insights - Journeys"
description: "Learn how to integrate unified profiles and segments with Dynamics 365 Customer Insights - Journeys."
ms.date: 02/17/2026
ms.topic: article
author: JimsonChalissery
ms.author: sstabbert
ms.reviewer: v-wendysmith
---

# Use unified customer profiles in Dynamics 365 Customer Insights - Journeys

[Dynamics 365 Customer Insights - Journeys](/dynamics365/marketing/overview) elevates customer experiences, allowing you to orchestrate personalized journeys across all touchpoints to strengthen relationships and earn loyalty. The Customer Insights - Journeys app works seamlessly with Dynamics 365 Sales, Dynamics 365 Customer Insights - Data, Microsoft Teams, and other products and allows you to make faster and better decisions using the power of data and AI.

By connecting both Customer Insights applications, you can:

- Target unified customer profiles and segments and engage with every customer, regardless of the location of the customer's data.
- Base dynamic content (such as personalized tokens) in emails, SMS, and push notifications on measures such as loyalty status, subscription renewal date, parent account, or any other measure.
- Load data from Customer Insights - Journeys into Customer Insights - Data and combine it with customer data from other sources.
- Apply Customer Insights data cleansing, enrichment, and fuzzy matching tools.

Depending on how you plan to work with Customer Insights - Journeys, there are two ways to use the two apps together.

For real-time marketing, use the [integration through Microsoft Dataverse](#use-rich-customer-profiles-in-real-time-marketing).
For outbound marketing, [export Customer Insights - Data segments](#use-unified-segments-with-outbound-customer-journeys).

## Use rich customer profiles in real-time marketing

Real-time marketing allows you to create [custom triggers](/dynamics365/marketing/real-time-marketing-custom-triggers) that launch customer journeys based on any customer action. The more personalized your data, the more relevant and personalized your journeys are. You can [unify data](data-unification.md) from any source, then use it to fuel hyper-personalized customer journeys.

Learn more: [Use Customer Insights - Data profiles and segments in real-time marketing.](/dynamics365/marketing/real-time-marketing-ci-profile)

## Use unified segments with outbound customer journeys

Customer Insights - Data allows you to refine data from many sources and combine it into aggregated customer segments.

Learn more: [Use segments from Customer Insights - Data with Customer Insights - Journeys.](/dynamics365/marketing/customer-insights-segments)

## Pull data from your own Azure Data Lake Storage

You aren't limited to cloud storage if you want to use both Customer Insights apps. If you already have your own Azure Data Lake Storage set up, you can connect with Customer Insights - Data, then share the data with Customer Insights - Journeys just as you would with a cloud-based setup.

Learn more: [Enable data sharing with Dataverse from your own Azure Data Lake Storage.](own-data-lake-storage.md#enable-data-sharing-with-dataverse-from-your-own-azure-data-lake-storage-preview)

## Connect Customer Insights - Data to Customer Insights - Journeys

To use unified customer profiles in Dynamics 365 Customer Insights - Journeys, [set up your environments](./journeys/real-time-marketing-ci-profile.md).

### Common connection issues

| Problem | Cause | Solution |
|---------|-------|----------|
| "There was a problem setting up the Customer Insights - Data connection" | Customer Insights - Data not provisioned on the same environment | Provision Customer Insights - Data on the same Dataverse environment as Journeys |
| Customer Insights connector works in UAT but not Production | Different environments or license assignments | Verify Production has the same setup as UAT |
| Trigger-based journey not sending emails | Using Customer Insights - Journeys feature, not Customer Insights - Data | Verify you're configuring in the correct application |
| Cannot see Customer Insights - Data segments in Journeys | Dataverse sync disabled or segment not active | Enable Dataverse data sharing; activate and refresh the segment |
| Segment shows 0 members in Journeys | Segment hasn't synced to Dataverse yet | Wait for the next scheduled refresh to complete |

## See also

- [Use segments in Customer Insights - Journeys](segments.md#use-segments-in-customer-insights---journeys)
- [Create and manage segments](segments.md)
- [Exports overview](export-destinations.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
