---
title: Real-time web personalization overview (preview)
description: Learn about web interactions and personalized experiences in real time with Customer Insights - Data.
ms.date: 06/14/2024
ms.topic: overview
author: srivas15
ms.author: shsri
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Real-time web personalization overview (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

When customers interact with websites, they constantly provide signals about their interests and preferences. For example, adding a product to a cart, viewing pricing details, signing up for a trial, and more. It's crucial to build on these signals as they happen so you can deliver the right personalized experiences in the right moment.

Customer Insights - Data can update customer profiles in real time based on web signals. This capability helps you provide the most targeted and personalized experiences to your customers as they browse your web properties. Foster loyalty, increase engagement, enhance satisfaction, and drive higher conversion rates.

> [!TIP]
> Sign up to [request access to the preview version](https://forms.office.com/r/6NK6uj6f7f) of the real-time personalization features.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

Once you [set up real-time web personalization](real-time-web-personalization.md), Customer Insights - Data enables you to:

- Track your customer's website interactions in real-time.

- Automatically create [unknown customer profiles](customer-profiles.md#known-and-unknown-customers) if your customers aren't authenticated.

- Continuously enhance your customer profiles when they return to your website with progressive profiling.

- Seamlessly merge [unknown profiles into known profiles](#unknown-customer-profiles) in real time, so that you can always have a 360-degree view of your customers.

- Personalize your customer's web experience in real time and engage with them in the moments that matter.

## Unknown customer profiles

Customer Insights - Data uses cookies to identify returning visitors so profiles continue to get enhanced over time, even when a visitor ends a web session and comes back. The expiration for a cookieId is rolling one year, meaning the one year expiration is refreshed every time the customer visits your website.

If the customer authenticates on your website, Customer Insights - Data merges their unknown profile with their known profile in real time. For example, you have a known customer named Abbie in Customer Insights - Data who registered their profile in person. When Abbie visits your website for the first time, a new unknown profile is created for Abbie and all their web interactions are tracked to that profile. When Abbie authenticates on your website, their unknown profile automatically merges with their known profile.

This means:

- The existing known profile gets all the web interactions that were associated to the unknown profile. These web interactions appear on the timeline of the known profile.

- The existing known profile gets the cookieId as a new identifier.

- All downstream processes refer to the known profile instead of the unknown profile going forward (segments, measures, APIs) which allows you to take action.

- The unknown profile expires.

## Scenarios

Through real-time web personalization, you can personalize your customers experience to help you achieve increased engagement and higher customer satisfaction. For example:

- Promote a premium coffee machine on your website if a customer browses other premium coffee machines.

- Offer a discount code on the website to all your customers who are members of the segment called high lifetime value.

- Dynamically update the text on your website to add a welcome message to your loyal customers.

- Send an email to your customers promoting your premium coffee machines if they read the reviews of similar products in the last 30 days.

## Next steps

[Set up real-time web personalization](real-time-web-personalization.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
