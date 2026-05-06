---
title: Web tracking and personalization overview (preview)
description: Learn how to provide personalized web interactions and experiences in real time with Customer Insights - Data.
ms.date: 03/24/2026
ms.topic: overview
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

<!-- I reversed the title in line 26 so it matches the content that follows - first unknown, then known. -->

# Web tracking and personalization overview (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Real-time web tracking and personalization in Customer Insights - Data captures and leverages website activity both for known and anonymous visitors.

Watch this brief video to learn more about real-time web personalization.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=0374bff9-f481-4324-8237-ebbaaffaed27]

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Unknown and known customers

**Anonymous customers**

Anonymous customer tracking lets you:

- Identify anonymous users who visit and later return to your website.

- Track the activities of anonymous users over time to understand their interests, such as the pages viewed and elements clicked.

- Personalize your website content when the customer returns based on their interests.

**Known customers**

An *unknown customer* becomes a *known customer* when they share identifying details (for example, an email address to download content, create an account, or place an order).

Converting an unknown customer to a known customer lets you:

- Keep all the activity history that was accrued when they were unknown, providing deeper insight.

- Combine unknown profiles and activity data from a person visiting from multiple machines into a single known customer profile.

- Unify customer data from your website with your other sources of customer data such as sales and support, giving you unprecedented ability to understand customer needs and how they interact with your brand.

> [!TIP]
> [Request access to the preview version](https://forms.office.com/r/TJEE62xTD3) of the real-time personalization features.

## Customer tracking

Customer Insights - Data uses cookies to recognize returning visitors and enrich profiles over time. Cookie IDs use a rolling one-year expiration that refreshes with each visit. When a customer authenticates on your site, Customer Insights - Data merges the anonymous and known profiles in real time.

For example, a retail store has a customer named Abbie in Customer Insights - Data who registered in person. When Abbie first visits your website, Customer Insights - Data creates an anonymous profile and tracks her web interactions. After Abbie authenticates, the profiles merge automatically. After the merge:

- The known profile gets all the unknown profile's web interactions and appears on the known profile timeline.
- The known profile gets the cookie ID as a new identifier.
- All downstream processes, such as segments, measures, and APIs, refer to the known profile going forward.
- The unknown profile expires.

## Examples

Use real-time web personalization to increase engagement and drive higher customer satisfaction in the following ways:

- Promote a premium coffee machine on your website if a customer browses other premium coffee machines.
- Offer a discount code on the website to all your customers who are members of the segment called "high lifetime value."
- Dynamically update the text on your website to add a welcome message to your loyal customers.
- Send an email to your customers promoting your premium coffee machines if they read the reviews of similar products in the last 30 days.

## How it works

Web personalization starts by assigning an anonymous tracking cookie, capturing activity in Dataverse, and unifying it into a known customer profile.

**Start anonymous visitor tracking**

- A visitor accesses your website and receives a web tracking GUID stored in a persistent cookie. If the same person visits from another device or browser, they receive a different GUID.

- The script streams the visitor’s events to Dataverse in real time and associates the activity with the tracking GUID.

- Unknown customers and their activity typically appear on the Customer Insights - Data **Customers** page in about 30 seconds. You can also see this information in Power Apps in the [Web tracking and personalization tables](tables.md#real-time-web-personalization-tables-preview).

- Your [website personalizes content](optimizely-integration.md) for the unknown visitor.

**Make unknown visitor known**

- The visitor provides an email address or phone number (for example, through a webinar sign-up, content download, or account creation).

- Your website process creates or updates the customer record in the customer tracking table (for example, `<WebCustomers>` table) and finds the record’s primary key (PK). The PK is typically a GUID or incremental integer (INT) and not the email.

- Your process calls the `setUser` function to associate the current web tracking GUID and its activity history with the PK from your `<WebCustomers>` table.

**Unify identities in Customer Insights - Data**

- On the next unification run, Customer Insights - Data merges the `<WebCustomers>` table and the linked web tracking GUID into a single unified profile.

- The unified profile preserves all earlier anonymous activity.

**Customer becomes known on second device**

- If the same customer deletes their cookies or uses a different device or browser and visits your website, they receive a new web tracking GUID.

- When the customer provides the same email address or phone number, your website finds the same PK and calls the `setUser` function.

- On the next unification run, Customer Insights - Data merges multiple web tracking GUIDs (and any related customer records) into a single unified profile.

## Next steps

- [Set up real-time web personalization](real-time-web-personalization.md)
- [Web tracking and personalization tables](tables.md#real-time-web-personalization-tables-preview)
