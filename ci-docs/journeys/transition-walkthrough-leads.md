---
title: Lead management and scoring
description: Learn how to transition lead management and scoring capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/27/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Lead management, scoring, and LinkedIn Lead Gen

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)


## Lead management and scoring

Creating scoring models to identify the best leads is an important aspect of lead management. As of the September 2023 Customer Insights - Journeys release, lead scoring is available in real-time journeys. You can enable the real-time journeys lead scoring feature in the feature switches area in the settings. Improvements compared to the outbound marketing scoring models are:
-	Simpler and more intuitive design canvas.
-	Ability to score leads without a parent contact. Because it's possible to market directly to leads in real-time journeys, there's no need for a parent contact.
-	Ability to target a specific audience when creating the scoring model.
-	New set of insights.

The main difference in the real-time journeys lead scoring functionality compared to outbound marketing is in how marketers signal to their sales team that the lead is ready for them. This is called "Marketing Qualification" in real-time journeys. In outbound marketing, leads were marketing-qualified within the context of a scoring model (“update sales-ready flag if lead reaches 50 points”). In real-time journeys, leads are qualified in a separate feature. This provides extra flexibility (“update sales-ready if score model 1 > 50 points and/or score model 2 > 30 points") and is the foundation for more sophisticated qualification conditions. In the future, we're adding qualification based on high-value actions or attributes without the need for a scoring model.

Unfortunately, there's no way to transfer existing scoring models from outbound marketing to real-time journeys. Moving scoring models requires manual effort to rebuild the models and the processes in real-time journeys. However, the fact that the real-time journeys lead scoring entity is the same as in outbound marketing, helps facilitate migration, especially for customizations.

## Relevant upcoming features

The features listed below may be of interest as you transition from outbound marketing to real-time journeys. These features provide parity, equivalent, or better functionality than what was available in outbound marketing.

- **Signal sales for qualified leads**: Easily route qualified leads identified by the marketing team to a seller without customized solutions or manual intervention. This boosts marketing and sales teams' productivity while maintaining focus on the right customers. Learn more: [Increase lead conversions by routing to the correct sales rep](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/increase-lead-conversions-routing-correct-sales-rep)

[!INCLUDE [transition-comments](./includes/transition-comments.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
