---
title: Automated segment management
description: Learn about how segments are automatically managed in Customer Insights - Journeys.
ms.date: 01/15/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

To enhance the customer experience by minimizing the impact of unused segments on active campaigns and improving processing speed for segments in use, we are optimizing how segments are refreshed in Dynamics 365 Customer Insights – Journeys.
Starting February 17, 2025, segment refreshes will dynamically adjust based on usage to ensure marketers always have accurate, up-to-date audience data while optimizing system performance.

# Automated segment management
Newly Created Unused Segments: Segments that are not actively used in a journey will refresh every 30 minutes for the first 24 hours to ensure initial accuracy. 
After this period, they will transition to a 24-hour refresh cycle unless they become actively used.
Segments in Active Journeys: Segments actively used in a journey or referenced by another segment or emails will continue refreshing every 30 minutes, ensuring they stay updated with the latest audience data.
Segments Exiting a Journey: Once a segment is no longer used in a journey, it will move to a 24-hour refresh cycle, ensuring it remains relevant while optimizing system performance.

# Why This Matters
These updates ensure that marketers can rely on automated segment management to:
✅ Maintain timely and relevant audience updates for active campaigns.
✅ Optimize system performance by reducing unnecessary refreshes for inactive segments.
✅ Streamline audience management, allowing teams to focus on strategy while the system ensures data freshness.
