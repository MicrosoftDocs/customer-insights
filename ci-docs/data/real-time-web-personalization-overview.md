---
title: Real-time web personalization overview (preview)
description: Learn how to provide personalized web interactions and experiences in real time with Customer Insights - Data.
ms.date: 03/24/2026
ms.topic: overview
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Real-time web personalization overview (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

The real-time web personalization feature in Customer Insights – Data is a powerful tool to capture and leverage customer activity on your website. The feature captures data for both unknown and known customers. Use this data to provide targeted, personalized experiences to your customers as they browse.

Watch this brief video to learn more about real-time web personalization.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=0374bff9-f481-4324-8237-ebbaaffaed27]

> [!TIP]
> [Request access to the preview version](https://forms.office.com/r/TJEE62xTD3) of the real-time personalization features.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Unknown and known customers

By tracking unknown customers, you can:

- Identify anonymous or unknown users who visit and later return to your website.

- Track the activities of anonymous users over time to understand their interests, such as the pages viewed and elements clicked.

- Personalize your website content when the customer returns based on their interests.

An unknown user becomes a known user when they provide identifiable details, such as an email address to download a resource, create an account, or order a product. When a person signs in from multiple machines, they initially appear as separate unknown customers. As they become known on each machine, the unknown profiles and activity data combine into a single known customer profile.

When you convert an unknown user to a known customer, you keep all the activity history you accrued when they were unknown, providing deeper insight.

When you unify customer data from your website with other sources of customer data, such as sales and support, you gain unprecedented ability to understand customer needs and how they interact with your brand.

## Customer tracking

Customer Insights - Data uses cookies to identify returning visitors so that profiles continue to get enhanced over time when visitors end a web session and come back. The expiration for a cookie ID is rolling one year, which means the one-year expiration refreshes every time the customer visits your website. If the customer authenticates on your website, Customer Insights - Data merges the customer's unknown and known profiles in real time.

For example, suppose your retail store has a customer named Abbie in Customer Insights - Data who registered in person. When Abbie visits your website for the first time, Customer Insights - Data creates an unknown profile for Abbie and tracks all Abbie's web interactions to that profile. When Abbie authenticates on your website, both profiles merge automatically, so you can use signals from both before and after Abbie authenticated.

This process means:

- The known profile gets all the web interactions that were associated with the unknown profile. These web interactions appear on the timeline of the known profile.
- The known profile gets the cookie ID as a new identifier.
- All downstream processes, such as segments, measures, and APIs, refer to the known profile instead of the unknown profile going forward, which you can take action on.
- The unknown profile expires.

## Examples

Use real-time web personalization to increase engagement and drive higher customer satisfaction in the following ways:

- Promote a premium coffee machine on your website if a customer browses other premium coffee machines.
- Offer a discount code on the website to all your customers who are members of the segment called "high lifetime value."
- Dynamically update the text on your website to add a welcome message to your loyal customers.
- Send an email to your customers promoting your premium coffee machines if they read the reviews of similar products in the last 30 days.

## How it works

The web personalization process flow starts with assigning an anonymous tracking cookie, capturing activity in Dataverse, and unifying it into a known customer profile.

1. **Start anonymous visitor tracking**

   - A visitor accesses your website and receives a web tracking GUID stored in a persistent cookie. If the same person visits from another device or browser, they receive a different GUID.

   - The script streams the visitor’s events to Dataverse in real time and associates the activity with the tracking GUID.

   - Unknown customers and their activity typically appear on the Customer Insights - Data **Customers** page in about 30 seconds. You can also see this information in Power Apps in the [Web tracking and personalization tables](tables.md#real-time-web-personalization-tables-preview).

   - Your [website personalizes content](real-time-web-personalization.md#personalize-your-customers-web-experience) for the unknown visitor.

1. **Make unknown visitor known**

   - The visitor provides an email address or phone number (for example, through a webinar sign-up, content download, or account creation).

         - Your website process creates or updates the customer record in the customer tracking table (for example, `<WebCustomers>` table) and finds the record’s primary key (PK). The PK is typically a GUID or incremental integer (INT) and not the email.

   - Your process calls the `setUser` function to associate the current web tracking GUID and its activity history with the PK from your `<WebCustomers>` table.

1. **Unify identities in Customer Insights – Data**

   - On the next unification run, Customer Insights – Data merges the `<WebCustomers>` table and the linked web tracking GUID into a single unified profile.

   - The unified profile preserves all earlier anonymous activity.

1. **Customer becomes known on second device**

   - If the same customer deletes their cookies or uses a different device or browser and visits your website, they receive a new web tracking GUID.

   - When the customer provides the same email address or phone number, your website finds the same PK and calls the `setUser` function.

   - On the next unification run, Customer Insights – Data merges multiple web tracking GUIDs (and any related customer records) into a single unified profile.

## Next steps

- [Set up real-time web personalization](real-time-web-personalization.md)
- [Web tracking and personalization tables](tables.md#real-time-web-personalization-tables-preview)
