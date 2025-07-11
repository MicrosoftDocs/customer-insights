---
title: Optimize segment refresh
description: Optimize segment refresh in Dynamics 365 Customer Insights – Journeys for accurate, up-to-date audience data and improved system performance.
ms.date: 02/18/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-seo-date:02/18/2025
  - ai-gen-description
---

# Automated segment management

To minimize the impact of unused segments on active campaigns and improve processing speed for segments in use, we're optimizing how segments are refreshed in Dynamics 365 Customer Insights – Journeys. Starting February 17, 2025, segments refresh dynamically based on usage, ensuring that marketers always have accurate, up-to-date audience data while optimizing system performance.

## Automated segment management

- **Newly created unused segments**: Segments that aren't actively used in a journey now refresh every 30 minutes for the first 24 hours to ensure initial accuracy. After this period, they transition to a 24-hour refresh cycle unless they become actively used.
- **Segments in active journeys without interaction filters**: Segments actively used in a journey or referenced by another segment or emails continue refreshing every 30 minutes, ensuring that they stay updated with the latest audience data.
- **Segments in active journeys with at least one interaction filter**: Segments actively used in a journey or referenced by another segment or emails continue refreshing every 60 minutes, ensuring that they stay updated with the latest audience data.
- **Segments exiting a journey**: Once a segment is no longer used in a journey, it moves to a 24-hour refresh cycle, ensuring that it remains relevant while optimizing system performance.

## Why this matters

These updates ensure that marketers can rely on automated segment management to:
- Maintain timely and relevant audience updates for active campaigns.
- Optimize system performance by reducing unnecessary refreshes for inactive segments.
- Streamline audience management, allowing teams to focus on strategy while the system ensures data freshness.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
