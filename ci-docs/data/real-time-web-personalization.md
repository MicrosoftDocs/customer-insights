---
title: "Real-Time Web Personalization"
description: "Learn how to track web interactions and personalize experiences in real-time"
ms.date: 02/29/2024
ms.topic: overview
author: srivas15
ms.author: shsri
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Real-time web personalization

As customers engage with your business, they constantly provide signals about their interests and preferences, such as adding a product to a cart, viewing your pricing, signing up for a trial, and more. It's crucial to build on these signals as they happen so you can deliver the right personalized experiences in the right moment.

Customer Insights - Data can update customer profiles real-time based on web signals. This capability helps you to provide the most targeted and personalized experiences to your customers as they browse your web properties. Foster loyalty, increase engagement, enhance satisfaction, and drive higher conversion rates.

Customer Insights - Data enables you to:

- Track your customer's website interactions in real-time

- Automatically let the system create [unknown customer profiles](customer-profiles.md#known-and-unknown-customers) if your customers are not authenticated 

- Continuously enhance your customer profiles when they return to your website with progressive profiling

- Seamlessly merge unknown profiles into known profiles in real-time, so you can always have the 360-degree view of your customers

- Personalize your customer's web experience in real-time and engage with them in the moments that matter

This enables you to achieve the following scenarios:

- Promote a premium coffee machine on your website if a customer browses other premium coffee machines 

- Offer a discount code on the website to all your customers who are members of the segment called high lifetime value

- Dynamically update the text on your website to add a welcome message to your loyal customers 

- Send an email to your customers promoting your premium coffee machines if they read the reviews of similar products in the last 30 days

## Set up Web Tracking

To configure web personalization, set up web tracking.

1. Go to Customer Insights - Data and select **Web tracking & personalization**.

   :::image type="content" source="media/web-tracking-personalization.png" alt-text="Screenshot of Web tracking & personalization.":::

   <!--- Sharoon, when and why would they select Save? --->

1. Select the table that the tracking script should use to identify your customers when they [authenticate](#authenticate-unknown-customers-and-convert-to-known).

1. **Copy** the tracking script and paste it in the `<head>` tag of your website.

   If you're using a tag manager such as Google Tag Manager, go to the Google Tag Manager portal. Select **Add new tag** > **Tag configuration** > **Custom HTML** > **paste the Customer Insights - Data tracking script** > **Save**. If you're using a Content Management System (CMS) such as Wordpress, your CMS provider should have an easy way to add a script to the header. Example from Wordpress: [https://wordpress.com/support/adding-code-to-headers/](https://wordpress.com/support/adding-code-to-headers/).

1. Once you've added the tracking script to your website, browse the website like a visitor.

   Customer Insights - Data automatically creates unknown profiles for your visitors and tracks their website interactions (page views and page clicks) in real-time. Customer Insights - Data uses cookies to identify returning visitors so profiles continue to get enhanced over time, even when a visitor ends a web session and comes back.

1. To view the unknown profiles, go to the **Customers** page and select **Unknown**. All unknown profiles have a cookieId as an identifier and the website interactions on the timeline automatically display.

1. To validate the web events in Dataverse, sign in to [https://make.powerapps.com/](https://make.powerapps.com). Select **Tables** > **All** and select the **PersonalizationView** and **PersonalizationAction** tables. <!---read more link about schema of tables--->

<!--- disclaimer here about cookies - including retention, purpose, how to enable/disable tracking --->

## Authenticate unknown customers and convert to known

Customer Insights - Data seamlessly merges an unknown profile with a known profile in real-time when a visitor authenticates on your website. For example, you have a known customer named Abbie in Customer Insights - Data who registered her profile in-person. When she visits your website for the first time, a new unknown profile is created for her and all her web interactions are tracked to that profile. When Abbie authenticates on your website, her unknown profile merges with her known profile in real-time. This means:

- The existing known profile gets all the web interactions that were associated to the unknown profile. These web interactions appear on the timeline of the known profile.

- The existing known profile gets the cookieId as a new identifier.

- All downstream processes refer to the known profile instead of the unknown profile going forward (segments, measures, APIs) which allows you to take action on the 360-degree of your customers.

- The unknown profile expires.

To merge an unknown profile into a known profile, perform the following steps:

1. Go to Customer Insights - Data and select **Web tracking & personalization**.

1. Select the desired table.

   > [!NOTE]
   > You can only select tables in the dropdown that were used as one of the source tables in unification. Customer Insights - Data automatically uses the primary key of this table to identify the visitor. Customer Insights - Data does not restrict which column to use as the primary key, but it should be a field that uniquely identifies a customer such as  email, phone, or loyaltyId.

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

The selected table is used to identify and merge an unknown profile with a known profile. For example, in Customer Insights - Data you have a source table called **LoyaltySignUps** with **LoyaltyId** as the primary key which uniquely identifies a customer in that table. The value in the **LoyaltyId** column contains Loyalty1, Loyalty2, Loyalty3, and so on. If you select the **LoyaltySignUps** table to identify and merge unknown and known profiles, give Customer Insights - Data the **LoyaltyId** of the visitor when they authenticate on your website. For example, to merge Abbie's unknown profile to her known profile, give Customer Insights - Data the **LoyaltyId** of Abbie when she authenticates on your website. This is done by calling the 'setUser' function.

## Personalize your customers web experience

There are two ways to personalize your customers web experience:

- [No-code web personalization using Optimizely](optimizely-integration.md)

- Pro-code web personalization using APIs

To personalize the web experience of your visitors using APIs, query any of the [Customer Insights - Data APIs](dv-odata.md) that allow you to the retrieve rich information about each customer such as demographic information, web interactions, activities, segments, and measures.

Since the cookieIds are also used to uniquely identify a customer (unknown or known), you can also use the cookieId to query a profile. To do this, retrieve the Customer Insights - Data web tracking cookie on the server side of your website. Customer Insights - Data cookies are stored as "_msci" in the request. If using C#, the cookie of the current visitor can be accessed:

```
string cookieId = Request.Cookies["_msci"]; //CI-D cookie
```
This cookie can then be used as an identifier to query any of the Customer Insights - Data APIs. 

- [No-code web personalization using Optimizely](optimizely-integration.md)

- Pro-code web personalization using APIs

[!INCLUDE [footer-include](includes/footer-banner.md)]
