---
title: "Data enrichment (preview) overview"
description: "Learn how enrichments can improve your data and your insights."
ms.date: 10/05/2023
ms.reviewer: mhart
ms.topic: conceptual
author: jodahlMSFT
ms.author: jodahl
ms.collection: get-started
ms.custom: bap-template
---

# Data enrichment (preview) overview

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Having more complete and accurate data about your customers enables you to engage with them more effectively, increases your chances of delighting them, and ultimately allows you to improve your business.

Dynamics 365 Customer Insights - Data provides a number of enrichments that clean up your data and augments it for a more consistent and complete view of your customers. Some enrichments, such as brand and interest enrichments, are based on Microsoft data and machine learning models - these enrichments are available for free with your Dynamics 365 Customer Insights - Data subscription. Other enrichements are provided by leading 3rd party data providers, such as Experian and HERE Technologies - these enrichments require a subscription with the respective data providers.

The enrichments create separate enrichment tables with the enriched data that are linked to the unified customer profiles table through a relationship on the customer ID, so that the enrichment data can easily be leveraged but still kept seperate from the original profile data.

## Correcting missing and inconsistent address data
Oftentimes, customer profile data have address information that is provided as one text string without any separation into street name, zip code, state, etc. This makes it difficult to build segments effectively based on location and also diminishes the data unification match precision. Also, spelling errors and non-standardized notation (e.g., US, USA, United States, United States of America, representing the same country) are common. The **Enhanced addresses** enrichment from Microsoft and the **HERE technologies**, and **Azure Maps** enrichments correct missing and inconsistent data. All three enrichments can tokenize the address, i.e., split it up into street name, zip code, state, etc., so that you can easily create a segment based on the city or state for example. They also correct some spelling mistakes and standardizes notation.

The **HERE technologies** and **Azure Maps** enrichments also validate the address, i.e., looks up whether the address actually exists, and they can provide longitude and latitude for each address which can be used for creating geo targeting and store proximity based segments.

## Augmenting and expanding customer profiles
Oftentimes, marketers do not have all the information that they need about each customer to create effective campaigns. For example, a reatiler might be interested in whether a customer is likely to be most interested in *wine* or *the outdoors*, so that they can effectively target offers, but this information is not always available. The **Interest**  enrichment from Microsoft uses age, gender, and location information to predict which of a list of selected interests that are most likely to resonate with each customer, so that you can target them with tailored offeres that have the highest likelihood of being engaging to the customers. The **Brands** enrichment is similar to the **Interest** enrichment, but evaluates propensity based on a number of brands that the user selects.

The **Experian** enrichment provides demographics information such as likely income level, buying propensities, etc., which can be invaluable for creating effective segments for targeting.

## How enrichments are configured
Enrichments are configured using [connections](connections.md), which an administrator sets up with credentials and provides consent for data transfers. The connections are used by administrators and contributors to configure enrichments.

You can also enrich your data before unification to help increase the quality of a data match and have fewer duplicates in your unified profiles.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Enrichment of segments and Multiple enrichments of the same type
The table to be enriched is specified during the enrichment configuration, which allows you to enrich only a subset of your profiles. For example, enrich data only for a specific segment. You can configure several enrichments of the same type and reuse the same connection. Some enrichments have limits to the number of enrichments of the same type that can be created. The limits and current use can be seen on each tile on the **Discover** tab of the **Enrichment** page.

## Next steps

- [Enrich a data source](data-sources-enrichment.md)
- [Enrich unified data](enrichment-manage.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
