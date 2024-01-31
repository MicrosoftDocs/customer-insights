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

Having more complete and accurate data about your customers enables you to engage with them more effectively and ultimately allows you to improve your business. Dynamics 365 Customer Insights - Data provides a number of enrichments that cleans up your data and augments it for a more consistent and complete view of your customers. Some enrichments, such as brand and interest enrichemtns, are based on Microsoft data and machine learning models - these enrichments are available for free with your Dynamics 365 Customer Insights - Data subscription. Other enrichements are provided by leading 3rd party data providers, such as Azure Maps and HERE Technologies.

that  way and ultimately allows you to Data enrichment uses data from sources like Microsoft and other partners to enrich your unified customer data in Dynamics 365 Customer Insights - Data. Enriched data provides better insights into your customers which in turn provides you better opportunities to serve them. Enrichments are configured using [connections](connections.md), which an administrator sets up with credentials and provides consent for data transfers. The connections are used by administrators and contributors to configure enrichments.

You can also enrich your data before unification to help increase the quality of a data match and have fewer duplicates in your unified profiles.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## How data enrichment improves your data and your customer experience

Contoso captures customer data from various customer sources across its lines of business (LOB) - from sales and marketing to support. Each LOB has different processes and systems, resulting in siloed and varying representations of customer data. They use Customer Insights - Data to break these data silos and build a unified view of their customer data. However, they realize their data sources have missing, inconsistent, and sparse data.

### Data enrichment for missing and inconsistent data

Contoso set up matching rules across different data sources using personal data fields such as Name, E-mail, and Address. The data is inconsistent across their data sources with many customer records either missing this information or having typos and other errors. The result is a low match rate and duplicates in their unified customer data, causing poor customer experiences such as customers getting duplicate messages. By applying data enrichments on their data sources before unification, Contoso can leverage external datasets to normalize and fill in missing values in their addresses with [Enhanced addresses](enrichment-enhanced-addresses.md). They can resolve identity issues in the available personal data with [Identity by LiveRamp](enrichment-liveramp.md). Now Contoso unifies cleaner and richer source data for higher match rates and fewer duplicates.

### Data enrichment for sparse data

Contoso LOB systems capture basic contact and transactional information and not much else so their unified customer data doesn’t have much data except the basic personal and activity data. This sparse data limits their ability to gain a deeper understanding of who their customers are from several perspectives such as a demographic, behavioral, and geographical. Contoso can leverage datasets from Microsoft and other third parties to enrich their unified customer data. [Brand and Interests enrichments](enrichment-microsoft.md) enable Contoso to understand which of their customers are likely to prefer a given brand or interest. [Demographics enrichment](enrichment-experian.md) enables Contoso to understand their customers' household size, income, and other factors.

With these data enrichments, Contoso has a wealth of insights about their customers and their behaviors, and can now delight their customers at every touchpoint.

## Multiple enrichments of the same type

The table to be enriched is specified during the enrichment configuration, which allows you to enrich only a subset of your profiles. For example, enrich data only for a specific segment. You can configure several enrichments of the same type and reuse the same connection. Some enrichments have limits to the number of enrichments of the same type that can be created. The limits and current use can be seen on each tile on the **Discover** tab of the **Enrichment** page.

## Next steps

- [Enrich a data source](data-sources-enrichment.md)
- [Enrich unified data](enrichment-manage.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
