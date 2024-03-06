---
title: Set up real-time web personalization (preview)
description: Learn how to track web interactions and personalize experiences in real-time with Customer Insights - Data.
ms.date: 03/06/2024
ms.topic: overview
author: srivas15
ms.author: shsri
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Set up real-time web personalization (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Let Customer Insights - Data automatically create unknown profiles for your visitors and track their website interactions (page views and page clicks) in real time. Set up web tracking, merge customers with their known profiles when they authenticate on your website, and then personalize your customers web experience.

Learn more: [Real-time web personalization overview](real-time-web-personalization-overview.md).

## Prerequisites

- Source data that contains your website customers are [ingested](data-sources.md) and [unified](data-unification.md). Customer Insights - Data uses the primary key from the unified customer profile to identify your website visitors. The primary key should be a field that uniquely identifies a customer such as  email, phone, or loyaltyId.

  For example, in Customer Insights - Data you have a source table called **LoyaltySignUps** with **LoyaltyId** as the primary key that uniquely identifies a customer in that table.

## Set up web tracking

1. Sign in to Customer Insights - Data and select **Web tracking & personalization**.

   :::image type="content" source="media/web-tracking-personalization.png" alt-text="Screenshot of Web tracking & personalization.":::

   <!--- Sharoon, when and why would they select Save? --->

1. Select the table that the tracking script should use to identify your customers when they [authenticate](#authenticate-unknown-customers-and-merge-them-to-known).

1. **Copy** the tracking script and paste it in the `<head>` tag of your website.

   If you're using a tag manager such as Google Tag Manager, go to the Google Tag Manager portal. Select **Add new tag** > **Tag configuration** > **Custom HTML** > **paste the Customer Insights - Data tracking script** > **Save**.

   If you're using a Content Management System (CMS) such as Wordpress, your CMS provider should have an easy way to add a script to the header. Example from Wordpress: [https://wordpress.com/support/adding-code-to-headers/](https://wordpress.com/support/adding-code-to-headers/).

1. Browse your website like a visitor.

1. To view the unknown profiles, go to the **Customers** page and select **Unknown**. All unknown profiles have a cookieId as an identifier and the website interactions on the timeline automatically display.

   <!--- need screenshot --->

1. To validate the web events in Dataverse, sign in to [https://make.powerapps.com/](https://make.powerapps.com). Select **Tables** > **All** and select the **PersonalizationView** and **PersonalizationAction** tables.

## Authenticate unknown customers and merge them to known

To have Customer Insights - Data automatically merge an [unknown profile](real-time-web-personalization-overview.md#unknown-customer-profiles) into a known profile, select the source  table you used to identify your website customers.

1. Sign in to Customer Insights - Data and select **Web tracking & personalization**.

1. Select the desired table.

1. Define the *setUser* function on your website. Typically, you only define this function on the page that authenticates visitors.

   ```
   <script>
       function setUser() {
           window["MSCI"].setUser({ "authId": "<identifier>" });
    }
   </script>
   ```
   where the *identifier* is the visitor ID. For example, Loyalty1.

1. Call the *setUser* function when a visitor authenticates.

   ```
   <button type="submit" onclick="setUser()">Submit</button>
   ```

## Personalize your customers web experience

There are two ways to personalize your customers web experience:

- [No-code web personalization using Optimizely](optimizely-integration.md)

- Pro-code web personalization using APIs

  To personalize the web experience of your visitors using APIs, query any of the [Customer Insights - Data APIs](dv-odata.md) that allow you to retrieve rich information about each customer such as demographic information, web interactions, activities, segments, and measures.

  Since the cookieIds are also used to uniquely identify a customer (unknown or known), you can also use the cookieId to query a profile. To query a profile, retrieve the Customer Insights - Data web tracking cookie on the server side of your website. Customer Insights - Data cookies are stored as "_msci" in the request. If using C#, the cookie of the current visitor can be accessed:

  ```
  string cookieId = Request.Cookies["_msci"]; //CI-D cookie
  ```
  This cookie can then be used as an identifier to query any of the Customer Insights - Data APIs.

## See also

- [Real-time web personalization overview](real-time-web-personalization-overview.md)
- [No-code web personalization using Optimizely](optimizely-integration.md)
- [Known and unknown customers](customer-profiles.md#known-and-unknown-customers)

[!INCLUDE [footer-include](includes/footer-banner.md)]
