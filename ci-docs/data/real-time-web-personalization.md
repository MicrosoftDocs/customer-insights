---
title: "Real-Time Web Personalization"
description: "Learn how to track web interactions and personalize experiences in real-time"
ms.date: 02/16/2024
ms.topic: overview
author: srivas15
ms.author: shsri
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Real-time web personalization

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

As customers engage with your business, they constantly provide signals about their interests and preferences, such as adding a product to a cart, viewing your pricing, signing up for a trial, and more. It's crucial to build on these signals as they happen so you can deliver the right personalized experiences in the right moment.

Customer Insights - Data can update customer profiles real-time based on web signals. This capability helps you to provide the most targeted and personalized experiences to your customers as they browse your web properties. Foster loyalty, increase engagement, enhance satisfaction, and drive higher conversion rates.

Customer Insights - Data enables you to:

- Track your customer's website interactions in real-time

- Automatically let the system create [unknown profiles](unknown-to-known.md) if your customers are not authenticated 

- Continuously enhance your customer profiles when they return to your website with progressive profiling

- Seamlessly merge unknown profiles into known profiles in real-time, so you can always have the 360-degree view of your customers

- Personalize your customer's web experience in real-time and engage with them in the moments that matter

This enables you to achieve the following scenarios:

- Promote a premium coffee machine on your website if a customer browses other premium coffee machines 

- Offer a discount code on the website to all your customers who are members of the 'high lifetime value' segment

- Dynamically update the text on your website to add a welcome message to your loyal customers 

- Send an email to your customers promoting your premium coffee machines if they read the reviews of similar products in the last 30 days

## Set up Web Tracking

To configure web personalization, set up web tracking.

1. Go to Customer Insights - Data and select **Web tracking & personalization**.

   :::image type="content" source="media/web-tracking-personalization.png" alt-text="Screenshot of Web tracking & personalization.":::

   <!--- Sharoon, when and why would they select Save? --->

1. Select the table that the tracking script should use to identify your customers when they authenticate (read more link).

1. **Copy** the tracking script and paste it in the `<head>` tag of your website.

   If you're using a tag manager such as Google Tag Manager, go to the Google Tag Manager portal. Select **Add new tag** > **Tag configuration** > **Custom HTML** > **paste the Customer Insights - Data tracking script** > **Save**. If you're using a Content Management System (CMS) such as Wordpress, your CMS provider should have an easy way to add a script to the header. Example from Wordpress: https://wordpress.com/support/adding-code-to-headers/

1. Once you've added the tracking script to your website, browse the website like a visitor. You will see Customer Insights - Data automatically create unknown profiles for your visitors. All unknown profiles will have the cookieId as an identifier and will display the web interactions on the timeline automatically. You can also validate the incoming web events in Dataverse: <add link to table>. <read more link about schema of tables>

<disclaimer here about cookies -> including retention, purpose, how to enable/disable tracking>

## Authenticate customers 


## Personalize your customers web experience

There are two ways to personalize your customers web experience:

- [No-code web personalization using Optimizely](optimizely-integration.md)

- Pro-code web personalization using APIs

[!INCLUDE [footer-include](includes/footer-banner.md)]
