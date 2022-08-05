---
title: Personalize your experiences with data about known and unknown users
description: Incorporate the information about formerly unknown users when you know their identity.
ms.date: 07/07/2022
ms.reviewer: mhart
ms.subservice: audience-insights
ms.topic: conceptual
author: mukeshpo
ms.author: mukeshpo
manager: shellyha
searchScope: 
  - ci-system-diagnostic
  - customerInsights
---

# Personalize your experiences with data about known and unknown users

Managing customer data isn't a new challenge but it's increasingly becoming more difficult as users navigate the various digital channels brands offer. A user who is known (authenticated) in one channel becomes unknown (unauthenticated) in another if not signed in. The problem often is that unauthenticated (unknown) users don't have a common ID. It could be used to associate meaningful profiles attributes and generate unified customer profiles. Customer Insights helps solve this problem by ingesting data from tracking methods on your source systems. Consolidate unknown and known profiles provide organizations with a complete view of up-to-date profiles and their historical transactions, behaviors, and demographics. It even goes a step further by providing identity resolution that allows you to unify customer activity across multiple channels, including your website, in-store purchase, loyalty programs, and so on.

## Sample scenario

Let's think about a coffee chain, which has a broad customer base that purchases coffee and food in stores and orders products online. Often, online visitors aren't authenticated when browsing the products, making them "unknown users". It's difficult for the coffee chain to deliver personalized offers and experiences if users are unknown. On the other hand, customers can sign into their account and become "known users" to the company by joining a loyalty system, which in turn allows more personalized experiences. Customer Insights can help the coffee chain get insights about known and previously unknown users.

With Customer Insights, the company can combine customer profiles with activity data from unauthenticated (unknown) sessions after a user signs in and becomes known. The coffee chain can bring data from other data sources using built-in connectors into Customer Insights to merge identities for customers from various channels.

## Prerequisites

- Web data is collected and contains “visitor IDs” for all visitors.
- Web data contains "authenticated user IDs" for signed in visitors. These IDs are linked with the loyalty system.
- High value events data such as “Product view” and “Checkout” are defined and included in the source data along with the timestamp of the event and an event ID.

The following table shows a simplified example how high value web events could get captured.

|EventID|EventTimeStamp|UserID|LoyaltyID|EventName|
|--|--|--|--|--|
|1|07-23-2022 10:00:00|abc123|--|Product view|
|2|07-23-2022 10:05:00|abc123|707|Loyalty sign-in|
|3|07-23-2022 10:10:00|abc123|707|Checkout|
|4|07-23-2022 10:20:00|xyz789|--|Product view|

## Data ingestion

Data about customers can originate from your website as event data and it can be stored in your own in-house or third-party data analytics services. The web data contains known and unknown users if the website has an authentication flow that integrates with an authentication service. For example, an eCommerce system that requires users to provide their complete details to finish a purchase transaction. Or a loyalty system that requires authentication to confirm a valid recipient of the rewards discounts.

The event data in our example above contains the distinct profile IDs of the known and unknown users. In event 1 and 4, the users are unknown while in event 2 and 3 the user with the ID abc123 signs up to a loyalty program.

:::image type="content" source="media/website-data-source.png" alt-text="Data sources including the Contoso website.":::

For more information about the available options for data ingestion, see [Data sources overview](data-sources.md).

## Data unification

Converging unknown identities with known identities helps enable personalization based on user behaviors, irrespective of their profile state (known or unknown). Personalized content for all users helps customers quickly get to the most relevant products or services that they're interested in at that moment.

Since some of the users in our data are known, we can use Customer Insights to combine that data with the user's profile. For more information about unifying customer profiles, see [Data unification overview](data-unification.md).

1. Select the source fields from the web data entity. Use the profile data that is stored in your web data and select the fields that represent Ids with demographic data.

   :::image type="content" source="media/website-source-fields.png" alt-text="Source fields for the web data source.":::

1. Add rules to merge duplicate records. For web data, choose the most filled data.

1. Configure match rules and conditions. The web profiles event data in this example will be matched on IDs with the profiles from the other data sources that contain customer information. Set up exact match rules on IDs as separate rules with each of the other profile entities that have a corresponding primary key or ID match. In the example, web event profile data is used as the last matching entity so that other profile data is combined first.
   1. Not checking **Include all records** creates unified profiles for known users and includes their corresponding unknown user IDs. It's helpful in scenarios when you're interested in viewing the past behavioral activities of known users when they were still unknown.
   1. Checking **Include All records** creates separate profile records for unknown users. Unknown users get a unique customer ID. In the future when a known profile is associated in the web events profile data, then the newly known user’s journey can be viewed and used for personalization based on past unknown behavioral data too.

:::image type="content" source="media/website-match-rule.png" alt-text="Match rule for the website data source entity.":::

## Get insights

If customer profiles are created for unknown and known users, the high value web event data can be used as [activities](activities.md). These activities can be used to create more insights. For example, customers that visited a website six months ago (when they were still unknown) or customers that don't have a loyalty ID never completed a checkout.

:::image type="content" source="media/website-known-unknown.png" alt-text="Screenshot of the customer page with known and unknown customers.":::

[Enrich](enrichment-hub.md) your data, build [measures](measures.md), and create [segments](segments.md) for further activation.

For example, you can create segments of known users that looked at some products but never completed the checkout.

For more information, see [Segments overview](segments.md).

## Activate insights

There are several ways to export your data and take action based on the underlying insights.

For more information, see [Exports overview](export-destinations.md).
