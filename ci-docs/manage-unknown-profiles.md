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

Internet users are often unidentified or anonymous online. Even the most loyal customers may appear to be “unknown” if they aren't signed in across different devices. For many brands, known or authenticated users are the minority despite growing customer expectations around personalization. With the future of third-party cookies in question, managing user preferences based on first-party data instead, is crucial for achieving personalized experiences.

Memorable personalization depends on how well you know your customer and Customer Insights helps you do that by tracking all of your customers.  You don't have to limit or stop the use of data collected at the start of the customer journey. Customer Insights lets you bring your own data to create a customer profile for unknown users. You can then use that profile for further actions, despite missing contact information. Import first-party data from sources such as web, mobile, or CRM systems into Customer Insights to enrich customer profiles continuously. As you unify more interactions, [turn the *unknown* customer into a *known* customer](unknown-to-known.md).

## Sample Scenario

Assume a user uses their mobile device to browse your e-commerce site. The website assigns the visitor “mobile_guest123” as a unique identifier and you start collecting behavioral activities based on their online activity. For example, which pages they visited, how much time they spent on those pages, or which links they clicked. You don't know their name or email address, but this data can help provide brands meaningful insights about this specific user. In turn, you can put those insights to work the next time that user visits the site. Query Customer Insights for “mobile_guest123” to retrieve the user’s segment list, such as "organic", "mobile pre-order customers", "high-value customers", etc., or retrieve the profile to create personalized web experiences. You can also export the data to any activation system to do the same.

## Prerequisites

- Ingest first-party data into Customer Insights
- Each entity has a unique ID that is set as a primary key
- Each entity with a primary key for personalization is unified
- The content management system of your website can use APIs (for web personalization based on direct communication with Customer Insights)

The following table shows a simplified example how high-value web events could get captured.

|EventID|EventTimeStamp|UserID|PrimaryKey|EventName|
|--|--|--|--|--|
|1|09-15-2022 9:00:00|abc123|CookieID1|Product view|
|2|09-18-2022 10:05:00|abc123|CookieID1|Product view|
|3|09-18-2022 10:10:00|abc123|CookieID1|Add to cart|
|4|09-21-2022 09:05:00|abc123|CookieID1|Product view|

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

Example: An unknown user visits a website multiple times and visits product pages for various models of leather shoes. With that data available in Customer Insights, you can include the unknown user in the segment of people that are interested in leather shoes. Use this segment to inform your website build personalization for returning visitors. On the next visit, the site recognizes the unknown user and could offer them a 10% coupon on leather shoes.

[!INCLUDE [footer-include](includes/footer-banner.md)]
