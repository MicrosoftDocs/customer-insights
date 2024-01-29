---
title: "Real-Time Web Personalization"
description: "Learn how to track web interactions and personalize experiences in real-time"
ms.date: 12/07/2023
ms.topic: overview
author: srivas15
ms.author: shsri
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Real-Time Web Personalization

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

As customers engage with your business, they constantly provide signals about their interests and preferences, such as adding a product to a cart, viewing your pricing quote, signing up for a trial, and more. It's crucial to build on these signals as they happen so you can deliver the right personalized experiences in the right moment.
Customer Insights - Data can update customer profiles real-time based on web signals. This capability helps you to provide the most targeted and personalized experiences to your customers as they browse your web properties. Foster loyalty, increase engagement, enhance satisfaction, and drive higher conversion rates.

Customer Insights - Data enables you to:
1. Track your customer's website interactions in real-time
2. Automatically let the system create [unknown profiles](unknown-to-known.md) if your customers are not authenticated 
3. Continuously enhance your customer profiles when they return to your website with progressive profiling
4. Seamlessly merge unknown profiles into known profiles in real-time, so you can always have the 360-degree view of your customers
5. Personalize your customer's web experience in real-time and engage with them in the moments that matter

This enables you to achieve the following scenarios:
1. Promote a premium coffee machine on your website if a customer browses other premium coffee machines 
2. Offer a discount code on the website to all your customers who are members of the 'high lifetime value' segment
3. Dynamically update the text on your website to add a welcome message to your loyal customers 
4. Send an email to your customers promoting your premium coffee machines if they read the reviews of similar products in the last 30 days

## Setting up Web Tracking
To configure web personalization, you need to first set up web tracking. To do this, go to Customer Insights - Data > Web tracking and personalization. From the dropdown, select the Table that the tracking script should use to identify your customers when they authenticate (read more below). Copy the tracking script, and paste it in the `<head>` tag of your website. If you're using a tag manager such as Google Tag Manager, go to the Google Tag Manager portal > add new tag > tag configuration > custom HTML > paste the Customer Insights - Data tracking script > Save. If you're using a Content Management System (CMS) such as Wordpress, your CMS provider should have an easy way to add a script to the header. Example from Wordpress: https://wordpress.com/support/adding-code-to-headers/

Once you've added the tracking script to your website, browse the website like a visitor. You will see Customer Insights - Data automatically create unknown profiles for your visitors and tracks their website interactions (page views and page clicks) in real-time. Moreover, Customer Insights - Data uses cookies to identify returning visitors due to which profiles continue to get enhanced over time even when a visitor ends a web session and comes back. To view the unknown profiles, go to the Customers tab > Unknown. All unknown profiles will have the cookieId as an identifier and will display the website interactions on the timeline automatically. You can also validate the web events in Dataverse by going to https://make.powerapps.com/ > Tables > All > PersonalizationView and PersonalizationAction tables. <read more link about schema of tables>

<disclaimer here about cookies -> including retention, purpose, how to enable/disable tracking>

## Authenticating customers and unknown to known
Customer Insights - Data seamlessly merges an unknown profile with a known profile in real-time when a visitor authenticates on your website. For example, let's say you have a known customer Abbie in Customer Insights - Data who registered her profile in-person. When she visits your website for the first time, a new unknown profile is created for her and all her web interactions are tracked to that profile. When Abbie authenticates on your website, her unknown profile merges with her known profile in real-time. This means:
1. The existing known profile gets all the web interactions that were associated to the unknown profile. These web interactions also show up on the timeline of the known profile.
2. The existing known profile gets the cookieId as a new identifier
3. All downstream processes will refer to the known profile instead of the unknown profile going forward (segments, measures, APIs) which allows you to take action on the 360-degree of your customers
4. The unknown profile expires

To merge an unknown profile into a known profile, you need to do the following:
1. Select the desired table in the dropdown on the 'Web tracking and personalization' tab on Customer Insights - Data
2. Define the 'SetUser' function on your website
3. Call the SetUser function when a visitor authenticates

The table selected in the dropdown is used to identify and merge an unknown profile with a known profile. For example, let's say you have a source table 'LoyaltySignUps' in Customer Insights - Data that has contains the 'LoyaltyId' as the primary key which uniquely identifies a customer in that table. The value in the LoyaltyId column is like - Loyalty1, Loyalty2, Loyalty3, and so on. If you select the LoyaltySignUps table to identify and merge unknown and known profiles, you will need to tell Customer Insights - Data what the LoyaltyId is of the visitor when they authenticate on your website. So in the above example, to merge Abbie's unknown profile to her known profile, you need to tell Customer Insights - Data the LoyaltyId of Abbie when she authenticates on your website. This is done by calling the 'SetUser' function. 

First, define the SetUser function on your website. This is usually only done on the page that authenticates visitors. 
```
<script>
    function setUser() {
        window["MSCI"].setUser({ "authId": "<identifier>" });
    }
</script>
```
Here, you need to tell Customer Insights - Data the identifier for the visitor. In the above example, it would be something like Loyalty1. 

Second, when a visitor authenticates, call the SetUser function like:
```
<button type="submit" onclick="setUser()">Submit</button>
```

> [!NOTE]
> You can only select tables in the dropdown that were used as one of the source tables in Unification. Customer Insights - Data automatically uses the primary key of this table to identify the visitor and the merge logic is the same as Map, Match, Merge. Customer Insights - Data does not restrict which column to use as the primary key - it could be email, phone, loyaltyId, etc. 


## Personalizing your customers web experience
There are two ways to personalize your customers web experience:
1. [No-code web personalization using Optimizely](optimizely-integration.md)
2. Pro-code web personalization using APIs

To personalize the web experience of your visitors using APIs, you can simply query any of the [Customer Insights - Data APIs](https://learn.microsoft.com/en-us/dynamics365/customer-insights/data/dv-odata) that allow you the retrieve rich information about each customer such as - demographic information, web interactions, activities, segments, measures, and more. 

Since the cookieIds are also used to uniquely identify a customer (unknown or known), you can use the cookieId to query a profile as well. To do this, you can retrieve the Customer Insights - Data web tracking cookie on the server side of your website. Customer Insights - Data cookies are stored as "_msci" in the request. If using C#, the cookie of the current visitor can be access as such:
```
string cookieId = Request.Cookies["_msci"]; //CI-D cookie
```
This cookie can then be used as an identifier to query any of the Customer Insights - Data APIs. 


## Creating segments and measures


## Common ways to debug



[!INCLUDE [footer-include](includes/footer-banner.md)]
