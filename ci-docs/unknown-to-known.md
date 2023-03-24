---
title: Personalize your experiences with data about known and unknown users
description: Incorporate the information about formerly unknown users when you know their identity.
ms.date: 11/15/2022
ms.reviewer: mhart
ms.topic: conceptual
author: andtapia
ms.author: andreatapia
searchScope: 
  - ci-system-diagnostic
  - customerInsights
---

# Personalize your customer experiences with data for unknown and known users

Managing data gets increasingly challenging as customers interact with brands across different digital touchpoints. **Known users** (customer profiles with contact information) are often **signed in** or **authenticated** in one channel but **unknown users** (without contact information) and **unauthenticated** in others. This leads to disjointed customer experiences instead of seamless personalization across channels. Personalization becomes even more challenging for unknown customers who do not have unique identifiers.

Dynamics 365 Customer Insights helps collect meaningful profile attributes and create unified customer profiles for unknown and known users. With Customer Insights, you can import data to generate insights and create seamless experiences for all your customers. Over time, with the collection of historical transactions, behaviors, and demographics, unknown customers can become known customers. Their identities can be merged into one complete 360° view. Customer Insights allows you to unify customer activity across channels, including websites, loyalty programs, CRM systems, and more.

## Sample scenario

Let's think about a coffee chain that has a broad customer base, which purchases coffee and food in stores and online. Some web visitors are not signed into their accounts while browsing for decaffeinated coffee beans. So the are "unknown users". It is difficult for the coffee chain to deliver personalized offers if the user is unknown. However, with the coffee chain being able to identify this visitor is unknown, the company can extend a personalized offer to receive 15% off the next order. If the unknown users signs up for the offer, the unknown user becomes known, and now the coffee chain can email the customer with a newsletter about decaffeinated coffee.

With Customer Insights, the company can combine customer profiles with activity data from unauthenticated (unknown) sessions after the offer is activated. The coffee chain can import their data from other sources using out of the box connectors to merge identities for customers across all channels.

## Prerequisites

- Web data contains unique visitor IDs for all visitors.
- Web data contains authenticated user IDs for visitors who are signed in. These IDs can be linked to any first-party data source (for example a loyalty system).
- High value events data such as “Product view” and “Checkout” are defined and included in the source data along with the timestamp of the event and an event ID.

The following table shows a simplified example how high value web events could get captured.

|EventID|EventTimeStamp|UserID|LoyaltyID|EventName|
|--|--|--|--|--|
|1|07-23-2022 10:00:00|Unknown1|--|Product view|
|2|07-23-2022 10:05:00|Auth234|707|Loyalty sign-in|
|3|07-23-2022 10:10:00|Auth234|707|Checkout|
|4|07-23-2022 10:20:00|Unkonwn5|--|Product view|

## Data ingestion

Customer data can originate from your website as event data and it can be stored in your own in-house or third-party data analytics services. The web data can contain known and unknown users if the website has an authentication flow that integrates with an authentication service. Examples can include an eCommerce system that requires users to provide their contact details to complete a transaction, or a loyalty system that requires authentication to confirm a valid recipient of a rewards discount.

The event data in the example above contains the distinct profile IDs of the known and unknown users. In event 1 and 4, the users are unknown while in event 2 and 3 the user with the ID Auth234 signs up for the loyalty program.

:::image type="content" source="media/website-data-source.png" alt-text="Data sources including the Contoso website.":::

For more information about the available options for data ingestion, see [Data sources overview](data-sources.md).

## Data unification

Converging unknown identities with known identities helps enable personalization based on user behaviors, irrespective of their profile state (known or unknown). Personalized content for all users helps customers quickly get to the most relevant products or services that they're interested in at that moment.

Since some of the users in our data are known, we can use Customer Insights to combine that data with the user's profile. For more information about unifying customer profiles, see [Data unification overview](data-unification.md).

1. Select the source fields from the web data table. Use the profile data that is stored in your web data and select the fields that represent Ids with demographic data.

   :::image type="content" source="media/website-source-fields.png" alt-text="Source fields for the web data source.":::

1. Add rules to merge duplicate records. For web data, choose the most filled data.

1. Configure match rules and conditions. The web profiles event data in this example will be matched on IDs with the profiles from the other data sources that contain customer information. Set up exact match rules on IDs as separate rules with each of the other profile tables that have a corresponding primary key or ID match. In the example, web event profile data is used as the last matching table so that other profile data is combined first.
   1. Not checking **Include all records** creates unified profiles for known users and includes their corresponding unknown user IDs. It's helpful in scenarios when you're interested in viewing the past behavioral activities of known users when they were still unknown.
   1. Checking **Include All records** creates separate profile records for unknown users. Unknown users get a unique customer ID. In the future when a known profile is associated in the web events profile data, then the newly known user’s journey can be viewed and used for personalization based on past unknown behavioral data too.

:::image type="content" source="media/website-match-rule.png" alt-text="Match rule for the website data source table.":::

> [!TIP]
>
> - Set the unique IDs for unknown customers (for example, *Unknown1*) as primary keys.
> - Primary keys from each source table become an alternate key.
> - Alternate keys create the keyring for each unified customer profile ID.
> - Ensure unknown customer data sources become part of the customer table.

## Get insights

If customer profiles are created for unknown and known users, the high value web event data can be used as [activities](activities.md). These activities can be used to create more insights. For example, customers that visited a website six months ago (when they were still unknown) or customers that don't have a loyalty ID never completed a checkout.

:::image type="content" source="media/website-known-unknown.png" alt-text="Screenshot of the customer page with known and unknown customers.":::

[Enrich](enrichment-hub.md) your data, build [measures](measures.md), and create [segments](segments.md) for further activation.

For example, you can create segments of known users that looked at some products but never completed the checkout.

For more information, see [Segments overview](segments.md).

## Activate insights

There are several ways to export your data and take action based on the underlying insights.

For more information, see [Exports overview](export-destinations.md).
