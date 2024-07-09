---
title: Real-time web personalization overview (preview)
description: Learn how to provide personalized web interactions and experiences in real time with Customer Insights - Data.
ms.date: 06/14/2024
ms.topic: overview
author: srivas15
ms.author: shsri
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Real-time web personalization overview (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

When customers interact with websites&mdash;for example, adding a product to a cart, viewing pricing details, or signing up for a trial&mdash;they provide signals about their interests and preferences. It's crucial to build on these signals as they happen so that you can deliver the right personalized experiences in the right moment. Customer Insights - Data can update customer profiles in real time based on these web signals, helping you provide targeted, personalized experiences to your customers as they browse, fostering loyalty, increasing engagement, enhancing satisfaction, and driving higher conversion rates.

Watch this brief video to learn more about real-time web personalization.

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RW1hyhp]

> [!TIP]
> Sign up to [request access to the preview version](https://forms.office.com/r/6NK6uj6f7f) of the real-time personalization features.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

Real-time web personalization in Customer Insights - Data enables you to:

- Track your customer's website interactions in real time.
- Personalize your customers' web experience in real time and engage with them in the moments that matter.
- Automatically create profiles for customers who aren't authenticated. Learn more in [View customer profiles](customer-profiles.md#known-and-unknown-customers).
- Seamlessly merge [unknown profiles with known profiles](#unknown-customer-profiles) in real time, so that you can always have a 360-degree view of your customers.
- Use progressive profiling to continuously enhance your customer profiles when customers return to your website.

For example, you might use real-time web personalization to help you increase engagement and drive higher customer satisfaction in the following ways:

- Promote a premium coffee machine on your website if a customer browses other premium coffee machines.
- Offer a discount code on the website to all your customers who are members of the segment called "high lifetime value."
- Dynamically update the text on your website to add a welcome message to your loyal customers.
- Send an email to your customers promoting your premium coffee machines if they read the reviews of similar products in the last 30 days.

## Unknown customer profiles

Customer Insights - Data uses cookies to identify returning visitors so that profiles continue to get enhanced over time when visitors end a web session and come back. The expiration for a cookieId is rolling one year, meaning the one year expiration is refreshed every time the customer visits your website. If the customer authenticates on your website, Customer Insights - Data merges the customer's unknown and known profiles in real time.

For example, let's say your retail store has a customer named Abbie in Customer Insights - Data who registered in person. When Abbie visits your website for the first time, Customer Insights - Data creates an unknown profile for Abbie and tracks all Abbie's web interactions to that profile. When Abbie authenticates on your website, both profiles merge automatically, allowing you to use signals from both before and after Abbie authenticated.

This means:

- The known profile gets all the web interactions that were associated with the unknown profile. These web interactions appear on the timeline of the known profile.
- The known profile gets the cookieId as a new identifier.
- All downstream processes, such as segments, measures, and APIs, refer to the known profile instead of the unknown profile going forward, which allows you to take action.
- The unknown profile expires.

## Next steps

[Set up real-time web personalization](real-time-web-personalization.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
