---
title: Data enrichment (preview) overview
description: Data enrichment in Dynamics 365 Customer Insights - Data cleans addresses and augments customer profiles with interests, brands, demographics, and more.
ms.date: 08/11/2026
ms.reviewer: v-wendysmith
ms.topic: concept-article
author: Scott-Stabbert
ms.author: sstabbert
ms.collection: get-started
ms.custom:
 - ai-gen-docs-bap
 - ai-seo-date: 08/11/2026
ai-usage: ai-assisted
---

# Data enrichment (preview) overview

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

Dynamics 365 Customer Insights - Data enrichments improve unified customer profiles by standardizing address data and adding attributes such as predicted interests, brand affinities, and demographics. Enriched data can improve data matching, support more precise customer segments, and help personalize customer engagement.

Microsoft enrichments are included with a Customer Insights - Data subscription. Enrichments from providers such as Experian and HERE Technologies require separate provider subscriptions. Customer Insights - Data stores enrichment results in separate tables linked to unified customer profiles by customer ID, preserving the original profile data.

Enrichments create separate enrichment tables with the enriched data. Enriched data relates to the unified customer profiles table through the customer ID. This separation lets you easily use the enriched data while keeping it separate from the original profile data.

## Fix missing and inconsistent address data

Customer profile data often has addresses as a single text string, making it difficult to segment customers by location and reducing data unification match accuracy. In addition, inconsistent or misspelled location values, such as "US," "USA," and "United States," can create data quality issues.

The [**Enhanced addresses** enrichment](enrichment-enhanced-addresses.md) from Microsoft and [**Azure Maps** enrichments](enrichment-azure-maps.md) fix missing, misspelled, and inconsistent location data and split addresses into standardized attributes such as street, city, state, and postal code.

[**Azure Maps** enrichments](enrichment-azure-maps.md) also validates addresses and adds longitude and latitude values. You can use these values to create geolocation-based targeting such as  creating segments within a specified distance of a store.

## Augment and expand customer profiles

Marketers frequently don't have all the information that they need about each customer to create effective campaigns. For example, a retailer might be interested in whether a customer is likely to be interested in *wine* or *the outdoors*, so that they can create relevant offers. However, this information isn't always available. The [**Interest** enrichment from Microsoft](enrichment-microsoft.md) uses age, gender, and location information to predict a list of selected interests that are most likely to resonate with each customer. Marketers can use this information to target them with tailored offers. The [**Brands** enrichment](enrichment-microsoft.md) is similar to the **Interest** enrichment, but evaluates propensity based on the brands that the user selects.

The [**Experian** enrichment](enrichment-experian.md) provides demographic information such as likely income level, buying propensities, and more. This information can be invaluable to create effective segments for targeting.

## Configure enrichments

You configure enrichments by using [connections](connections.md). An administrator sets up connections with credentials and provides consent for data transfers. Administrators and contributors use the connections to configure enrichments.

You can also [enrich your source data before the data unification process](data-sources-enrichment.md) to help increase the quality of a data match and have fewer duplicates in your unified profiles.

## Enrich data for segments and multiple enrichments of the same type

While configuring the enrichment, you can choose the table to enrich. This feature lets you enrich only a subset of the customer profiles. For example, enrich data only for a specific segment. You can configure several enrichments of the same type and reuse the same connection. Some enrichments have limits to the number of enrichments of the same type that you can create. You can see the limits and current use on each tile on the **Discover** tab of the **Enrichment** page.

## Next steps

- [Enrich a data source](data-sources-enrichment.md)
- [Enrich unified data](enrichment-manage.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
