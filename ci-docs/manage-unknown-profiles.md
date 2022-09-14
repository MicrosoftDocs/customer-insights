---
title: Manage unknown profiles with Customer Insights
description: Work with unknown customer profiles that are created and managed in Dynamics 365 Customer Insights.
ms.date: 09/14/2022
ms.reviewer: mhart
ms.subservice: audience-insights
ms.topic: conceptual
author: andtapia
ms.author: andreatapia
manager: shellyha
---

# Manage unknown profiles with Customer Insights

Internet users are often unidentified and anonymous online. If they aren't signed in because they use different devices or channels, it's even true for the most loyal customers. With third-party cookies likely going away soon, managing user preferences based on first-party data is crucial to achieve differentiated personalized experiences. For many brands, known or authenticated users are the minority despite growing customer expectations around personalization. This makes the importance of knowing who your customers are, based on reliable, detailed, and unified data, more valuable than ever.

Memorable personalization depends on the richness and completeness of your customer data and Customer Insights helps you achieve these goals. You don't have to limit or stop the use of data collected at the start of the customer journey. Customer Insights enables you to ingest the data you own to create a customer profile for unknown users that you can use for further actions, despite missing contact information. Import first-party data from sources such as web, mobile, or CRM systems into Customer Insights to enrich customer profiles continuously. As you unify more interactions, [turn the *unknown* customer into a *known* customer](unknown-to-known.md).

## Sample Scenario

E-commerce is the fastest-growing channel over the last decade. Assume a user uses their mobile device to browse your e-commerce site. The website assigns the visitor “mobile_guest123” as a unique identifier and you start collecting behavioral activities based on their online activity. For example, which pages they visited, how much time they spent on those pages, or which links they clicked. You don't know their name or email address, but this data can help provide brands meaningful insights about this specific user. In turn, you can put those insights to work the next time that user visits the site by querying Customer Insights for “mobile_guest123” to retrieve the user’s segment list or profile to create personalized web experiences. You can also export the data to any activation system to do the same.

## Prerequisites

- Ingest first-party data into Customer Insights
- Each entity has a unique ID that is set as a primary key
- Each entity with a primary key for personalization is unified
- The content management system of your website is capable of using APIs

## Data ingestion

For more information about the available options for data ingestion, see [Data sources overview](data-sources.md).

## Data unification

For more information about unifying customer profiles, see [Data unification overview](data-unification.md).

## Get insights

[Enrich](enrichment-hub.md) your data, build [measures](measures.md), and create [segments](segments.md) for further activation.

For example, you can create segments of unknown users that browsed the same product pages but never completed the checkout.

## Activation

With your data in Customer Insights and your insights ready to get to work, you can use Customer Insights for personalization:

1. Use the [OData API](apis.md) to retrieve a segment membership or customer profile For more examples, see [OData query examples for Customer Insights APIs](odata-examples.md).

1. [Export](export-destinations.md) your data to your activation systems.

For example, an unknown user visits a website multiple times and visits product pages for various models of leather shoes. With that data available in Customer Insights, you can include the unknown user in the segment of people that are interested in leather shoes. Use this segment to inform your website build personalization for returning visitors. On the next visit, the site recognizes the unknown user and could offer them a 10% coupon on leather shoes.

[!INCLUDE [footer-include](includes/footer-banner.md)]
