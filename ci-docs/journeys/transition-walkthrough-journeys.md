---
title: Transition journeys
description: Transition your journeys to real-time journeys in Dynamics 365 Customer Insights - Journeys. Follow our guide to ensure a smooth transition.
ms.date: 12/08/2025
ms.update-cycle: 180-days
ms.topic: article
author: alfergus
ms.author: colinbirkett
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Transition journeys

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](transition-overview.md).

Journeys in real-time journeys are the equivalent of customer journeys in outbound marketing. Journeys are the container that define the sequence of marketing actions that contacts are involved in. The underlying architecture for journeys in the real-time journeys module is fundamentally different from outbound marketing, which is why journeys can't be transferred automatically and manual recreation of the journey is required.

Journey end dates behave differently in real-time journeys. In outbound marketing, if a journey had a set end date, customers who had already entered the journey would stop and not finish the journey. In contrast, in real-time journeys, customers who have already entered the journey complete the journey even if this takes them past the end date. However, no new customers are allowed to enter the journey after the end date.
 
Sending at a specific time (smart scheduling) has no equivalent in real-time journeys. 

In outbound marketing, you could create journeys with swimlanes, all visible in the same workspace. The equivalent implementation in real-time journeys is nested segmentation, whereby you create the segments you would have used for each swimlane in outbound marketing and then nest them in one segment. When you create the segment-based journey using the compound segment, you can use branches, each with a segment membership condition for the sub-segment, and each branch then represents what was a swimlane in outbound marketing.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
