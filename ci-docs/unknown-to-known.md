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

Managing customer data is not a new challenge but it is increasingly becoming more difficult. The problem often is that these unauthenticated (known) users do not have a common ID that could be used to associate meaningful profiles attributes into customer profiles. Customer Insights helps solve this problem by ingesting data from tracking methods on your source systems. Consolidated unknown and known profiles provide organizations with a complete view of up-to-date profiles and their historical transactions, behaviors, and demographics. It even goes a step further by providing identity resolution that allows you to unify customer activity across multiple channels, including your website, in-store purchase, loyalty programs, etc.

## Sample scenario

Let's think about a coffee chain, which has a broad customer base that purchases coffee and food in stores and also orders products online. Often, online visitors are not authenticated when browsing the products, making them "unknown users". It's difficult for the coffee chain to deliver personalized offers and experiences if users are unknown. On the other hand, customers can sign in to their account and become "known users" to the company by joining a loyalty system, which in turn allows more personalized experiences. Customer Insights can help the coffee chain get insights about known and unknown users.

The company can use Customer Insights to combine customer profiles with activity data from unauthenticated (unknown) sessions after a user signs in and becomes known. The coffee chain can bring data from other data sources using built-in connectors into Customer Insights to merge identities for customers from various channels.

## Prerequisites

- Web data is collected and contains “visitor IDs” that are assigned to all users.
- Web data contains "authenticated user IDs" for visitors that are signed in. These IDs are linked with the loyalty system.
- High value events data such as “Product view” and “Checkout” are defined and included in the source data along with the timestamp of the event and an event ID.

The following table shows a simplified example how high value web events could get captured.

|EventID|EventTimeStamp|UserID|LoyaltyID|EventName|
|--|--|--|--|--|
|1|07-23-2022 10:00:00|abc123|--|Product view|
|2|07-23-2022 10:05:00|abc123|707|Loyalty sign-in|
|3|07-23-2022 10:10:00|abc123|707|Checkout|
|4|07-23-2022 10:20:00|xyz789|--|Product view|

## Data ingestion

Data about customers can originate from your website as event data and it can be stored in your own in-house or third-party data analytics services. The web data collected contains known and unknown users based on whether the website has an authentication flow integrated with an authentication service, such as an eCommerce system that requires users to provide their complete details to finish a purchase transaction, or a Loyalty system that requires authentication to confirm a valid recipient of the rewards discounts.

The event data in our example above contains the distinct profile ids of the known and unknown users. In event 1 and 4, the users are unknown while in event 2 and 3 the user with the ID abc123 signs up to a loyalty program.

For more information about the available options for data ingestion, see [Data sources overview](data-sources.md).

## Data unification

Converging unknown identities with known identities is helps enable personalization based on user behaviors, irrespective of their profile state (i.e., known or unknown). Personalizing content for all users helps customers quickly get to the most relevant products or services that they are interested in at that moment.

Since some of the users in our data are known, we can use Customer Insights to combine that data with the user's profile.

1.	Select Webdata as a Source: Use the Profile data that is stored from your web data (ex. WebEvents – HomePagevisits) and select the fields that represent the demographic data (IDs  - contactID, Signal.SessionID, Signal.User.AuthId)
 
 
2.	Add rules to merge duplicate records: For the WebEvents profile data, specify the merge preferences to keep the most filled data. 
 
3.	Setup Matching rules and conditions: The web profiles event data in this example will be matched on IDs with the profiles from the other data sources that have authenticated users.
a.	Setup exact match rules on IDs as separate rules with each of the other profile entities that has a corresponding primary key or ID match. 
b.	In the example below, web event profile data is used as the last matching entity so that a known profile is matched first. You can start with the web event profile data first as well. 
c.	Include All records unchecked will create profile records for known users and will also include their corresponding unknown user ids. This is helpful in scenarios when you are interested in viewing the past behavioral activities of known users when they were not authenticated yet i.e., unknown. 
d.	Include All records checked will create profile records for unknown users without any demographic data (if not present within the web event data source only). This generates a unique customer id for the unknown profile. In the future when a known profile is associated in the web events profile data, then the newly known user’s journey can be viewed and used for personalization based on past unknown behavioral data as well. 
 
4.	Unknown and Known Profiles: Both unknown and known profiles are generated with a unified Customer ID. The additional high value web event data such as home page visits, checkout, etc. can be brought in as behavioral activities when the user was unknown as well as known. That can now be used for creating more insights, such as Loyalty customers that visited the home page six months ago (when they were still unknown) or Customers that do not have loyalty ids and have abandoned cart.  

## Get insights

Enrich your data, build measures, and create segments for further activation.

For example, you can create segments of known that looked at some products but never completed the checkout.

For more information, see [Segments overview](segments.md).

## Activate insights

There are several ways to export your data and take action based on the underlying insights.

For more information, see [Exports overview](export-destinations.md).
