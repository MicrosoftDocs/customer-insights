---
title: "Data enrichment (preview) overview"
description: "Learn how enrichments can improve your data and your insights."
ms.date: 02/01/2024
ms.reviewer: mhart
ms.topic: conceptual
author: jodahlMSFT
ms.author: jodahl
ms.collection: get-started
ms.custom: bap-template
---

# Data enrichment (preview) overview

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

Having more complete and accurate data about your customers enables you to engage with them more effectively, increases your chances of delighting them, and ultimately allows you to improve your business.

Dynamics 365 Customer Insights - Data provides enrichments that clean up your data and augments it for a more consistent and complete view of your customers. Some enrichments, such as brand and interest enrichments, are based on Microsoft data and machine learning models - these enrichments are available for free with your Dynamics 365 Customer Insights - Data subscription. Other enrichments are provided by data providers, such as Experian and HERE Technologies - these enrichments require a subscription with the respective data providers.

Enrichments create separate enrichment tables with the enriched data. Enriched data relates to the unified customer profiles table through the customer ID. This separation lets you easily use the enriched data while keeping it separate from the original profile data.

## Fix missing and inconsistent address data

Customer profile data often has address information in the form of a text string without separation of address elements, such as street name, zip code, or city. Without address elements, it's difficult to build segments based on location and the data unification match precision is lower too. Also, spelling errors and nonstandardized notation for the same attribute (for example, US, USA, United States, or United States of America) are a common issue. The [**Enhanced addresses** enrichment](enrichment-enhanced-addresses.md) from Microsoft and [**Azure Maps** enrichments](enrichment-azure-maps.md) fix missing, misspelled, and inconsistent location data. All three enrichments can tokenize the address and split it into standardized attributes so that you can easily create segments based a city or a state.

[**Azure Maps** enrichments](enrichment-azure-maps.md) also validate the address and provide longitude and latitude values. You can use these values to create geolocation-based targeting. For example, by creating segments based on proximity to a store location.

## Augment and expand customer profiles

Marketers frequently don't have all the information that they need about each customer to create effective campaigns. For example, a retailer might be interested in whether a customer is likely to be interested in *wine* or *the outdoors*, so that they can create relevant offers. However, this information isn't always available. The [**Interest** enrichment from Microsoft](enrichment-microsoft.md) uses age, gender, and location information to predict a list of selected interests that are most likely to resonate with each customer. Marketers can use this information to target them with tailored offers. The [**Brands** enrichment](enrichment-microsoft.md) is similar to the **Interest** enrichment, but evaluates propensity based on the brands that the user selects.

The [**Experian** enrichment](enrichment-experian.md) provides demographic information such as likely income level, buying propensities, and more. This information can be invaluable to create effective segments for targeting.

## Configure enrichments

Enrichments are configured using [connections](connections.md), which an administrator sets up with credentials and provides consent for data transfers. The connections are used by administrators and contributors to configure enrichments.

You can also [enrich your source data before the data unification process](data-sources-enrichment.md) to help increase the quality of a data match and have fewer duplicates in your unified profiles.

## Enrich data for segments and multiple enrichments of the same type

While configuring the enrichment, you can choose the table to enrich. This feature lets you enrich only a subset of the customer profiles. For example, enrich data only for a specific segment. You can configure several enrichments of the same type and reuse the same connection. Some enrichments have limits to the number of enrichments of the same type that can be created. The limits and current use can be seen on each tile on the **Discover** tab of the **Enrichment** page.

## Next steps

- [Enrich a data source](data-sources-enrichment.md)
- [Enrich unified data](enrichment-manage.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
