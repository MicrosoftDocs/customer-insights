---
title: Exclude bot interactions
description: Learn how to exclude bot and nonhuman interactions on your emails in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/14/2024
ms.topic: article
author: srivas15
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Exclude bot interactions

Teams rely on channel analytics to evaluate campaign performance and to drive future improvements. Having reliable analytics data is critical to achieve this. Bot protection in Customer Insights - Journeys captures and filters out bot clicks on emails, text messages, push notifications, and custom channels. This provides a more reliable view of analytics data and prevents unexpected outcomes such as inflated metrics, incorrect journeys, and fraudulent double opt-ins.

## Enable bot protection

To enable bot protection, go to **Settings** > **Feature switches** and enable the **Bot Protection** toggle.

> [!IMPORTANT]
> - Organizations created after July 22, 2024 have advanced bot protection enabled by default.
> - Bot protection doesn't apply to email opens. Learn more about the challenges of relying solely on email opens to measure campaign performance: [Rethinking email marketing metrics: The evolving landscape of ‘Open Rate’](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2024/10/16/rethinking-email-metrics-the-evolving-landscape-of-open-rates/).

## Impact of bot protection

Once bot protection is enabled, suspected bot clicks are filtered out going forward and no historical data is impacted. After bot protection is enabled, you may observe a drop in the click rate in your email or other channel analytics.

Because bot protection filters out nonhuman link clicks, some journey triggers and branching conditions that use "email clicked" may be impacted. Bot protection doesn't impact email or push notification open rates.

## How bots are detected

When bot protection is enabled, any time a link is selected, it goes through an intermediate page. Customer Insights - Journeys runs some checks on the intermediate page to determine if the click was made by a bot or a human. 

## Frequently asked questions

| Question                      | Answer               | 
|:-----------------------------------|:------------------------------|
| Why do I see multiple email open interactions for the same contact with the exact same timestamp? | Bot protection doesn't apply to email opens. This could be due to bot-related activity, resulting in multiple open interactions. | 
| I’ve noticed an inflated email open rate recently. What’s happening? | Because bot protection doesn't apply to email opens, nonhuman traffic can increase the open rate. Learn more about improving engagement measurement: [Rethinking email marketing metrics: The evolving landscape of ‘Open Rate’](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2024/10/16/rethinking-email-metrics-the-evolving-landscape-of-open-rates/).|
| Why are no or limited email opens being recorded? | Many modern email clients block image loading by default to protect user privacy. Since email open tracking relies on images being loaded, this may limit the ability to accurately capture email open interactions. [Learn more](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2024/10/16/rethinking-email-metrics-the-evolving-landscape-of-open-rates/). |
| Why are there no email opens or clicks recorded? | Ensure compliance profiles are correctly configured and tracking is allowed for the contacts, leads, or Customer Insights - Data profiles that received the email. Learn more: [Consent management overview](real-time-marketing-compliance-settings.md). | 

[!INCLUDE [footer-include](./includes/footer-banner.md)]
