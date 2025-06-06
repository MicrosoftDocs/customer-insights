---
title: Transition journeys
description: Transition your journeys to real-time journeys in Dynamics 365 Customer Insights - Journeys. Follow our guide to ensure a smooth transition.
ms.date: 06/06/2025
ms.topic: article
author: alfergus
ms.author: colinbirkett
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Transition journeys

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Journeys in real-time journeys are the equivalent to customer journeys in outbound marketing. Journeys are the container that define the sequence of marketing actions that contacts are involved in. The underlying architecture for journeys in the real-time journeys module is fundamentally different from outbound marketing, which is why journeys can't be transferred automatically and manual recreation of the journey is required.

Using quiet times, you can control when messages get delivered, increasing engagement and meeting customer preferences. Quiet times allow you to comply with regulations by only reaching customers at their preferred times or by preventing nighttime, weekend, or holiday deliveries. For more information, see [Improve communication timing by setting up quiet times](real-time-marketing-quiet-times.md).

Journey end dates behave differently in real-time journeys. In outbound marketing, if a journey had a set end date, customers who already entered the journey would stop and not finish the journey. In contrast, in real-time journeys, customers who have already entered the journey complete the journey even if this takes them past the end date. However, no new customers are allowed to enter the journey after the end-date.
 
Send at a specific time (that is, 'Smart scheduling') has no equivalent in real-time journeys. 

## Relevant upcoming features or workarounds in real-time journeys

The features listed below may be of interest as you transition from outbound marketing to real-time journeys. These features provide parity, equivalent, or better functionality than what was available in outbound marketing.

- **Journey split by percentage or absolute number**: Split your audience into branches to provide a subset of your audience with unique experiences. Split your audience by percentages (for cases where you need randomness) or by number (for cases where you want to deliver specific experiences to a set of people). For more information, see [Provide varied experiences in one journey using journey split tiles](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/provide-varied-experiences-one-journey-using-journey-split-tiles).
- **Web tracking**: Trigger journeys and make decisions based on all known user interactions, from messages to web pages, making it even easier to create consistent personalized experiences across your brand's digital touch-points. For example, you can engage your customers when they show interest by sending a personalized offer after they visit your website. For more information, see [Engage customers with content and follow-ups based on website interactions](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/engage-customers-content-follow-ups-based-website-interactions).
- **Use email deliverability status for journey orchestration branching**: Start a journey or branch within a journey based on email delivery statuses, such as "delivered" or "bounced." For more information, see [Wait for a trigger](add-action.md#wait-for-a-trigger).
- **Journeys with swimlanes**: In outbound marketing, you could create journeys with swimlanes, all visible in the same workspace. The equivalent implementation in real-time journeys is nested segmentation, whereby you create the segments you would have used for each swimlane in outbound marketing and then nest them in one segment. When you create the segment-based journey using the compound segment, you can use branches, each with a segment membership condition for the sub-segment, and each branch then represents what was a swimlane in outbound marketing. 

[!INCLUDE [transition-comments](./includes/transition-comments.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
