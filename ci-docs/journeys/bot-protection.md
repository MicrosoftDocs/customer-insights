---
title: "Preview: Exclude bot interactions"
description: Learn how to exclude bot and nonhuman interactions on your emails in Dynamics 365 Customer Insights - Journeys.
ms.date: 04/08/2024
ms.topic: article
author: srivas15
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Preview: Exclude bot interactions

> [!IMPORTANT]
> A preview feature is a feature that is not complete, but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.
>
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won’t be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data or other data that are subject to legal or regulatory compliance requirements.

Teams rely on email analytics to evaluate campaign performance and to drive future improvements. Having reliable analytics data is critical to achieve this. Bot protection in Customer Insights - Journeys captures and filters out bot clicks on emails. This provides a more reliable view of analytics data and prevents unexpected outcomes such as inflated metrics, incorrect journeys, and fraudulent double opt-ins.

## Enable bot protection

To enable bot protection, go to **Settings** > **Feature switches** and enable the **Bot Protection (preview)** toggle.

## Impact of bot protection

Once bot protection is enabled, suspected bot clicks are filtered out going forward and no historical data is impacted. After bot protection is enabled, you may observe a drop in the click rate in your email analytics.

Because bot protection filters out nonhuman link clicks, some journey triggers and branching conditions that use "email clicked" may be impacted. Bot protection doesn't impact email open rates.

## How bots are detected

When bot protection is enabled, any time a link is selected, it goes through an intermediate page. Customer Insights - Journeys runs some checks on the intermediate page to determine if the click was made by a bot or a human. 

[!INCLUDE [footer-include](./includes/footer-banner.md)]
