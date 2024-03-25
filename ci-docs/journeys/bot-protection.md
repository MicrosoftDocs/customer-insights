---
title: Exclude bot interactions (Preview)
description: Learn how to exclude bot and non-human interactions on your emails in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/24/2024
ms.topic: article
author: srivas15
ms.author: shsri
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Exclude bot interactions (Preview)

Your team relies on analytics to evaluate campaign performance and to drive future improvements. Having reliable analytics data is critical to achieve this. Bot protection in Customer Insights - Journeys captures and filters out bot clicks on your emails. This provides a more reliable view of your analytiucs data and also prevents unexpected outcomes such as inflated metrics, incorrect journeys, fraudulent double opt-ins, etc. 

## How to enable
To enable bot protection, go to Settings -> Feature switches -> and switch on the toggle for 'Bot Protection (preview)'

## Impact of bot protection
Once bot protection is enabled, suspected bot clicks are filterd out going forward and no historical data is impacted. You may observe a drop in the click rate in your email analytics going forward. 

Since bot protection filters out non-human link clicks, some journey triggers and branching conditions that use 'email clicked' may be impacted. Bot protection does not impact email open rates. 

## How bots are detected
<need to add 2-3 lines about fingerprinting and also mention IP based filtering which is not impacted>

[!INCLUDE [footer-include](./includes/footer-banner.md)]
