---
title: Transition consent
description: Learn how to transition consent capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 11/16/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition consent

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Consent is an essential requirement that allows customers of Customer Insights – Journeys to send marketing messages. Customers who already use outbound marketing can transition consent settings to real-time journeys. Consent management, however, is more sophisticated in real-time journeys. The differences and how to transition consent are described in: [Consent management and double opt-in transition guidance](real-time-marketing-consent-transition.md). This article also describes how to migrate subscription lists to real-time journeys to send out segment-based newsletters. For a more detailed discussion, see [Understanding consent management in Dynamics 365 Customer Insights - Journeys - Dynamics FastTrack Blogs](https://community.dynamics.com/blogs/post/?postid=8b2a4ee8-1069-ee11-a81c-000d3a7a1a66)

Customers going through the transition to real-time journeys are recommended to focus initially on moving the journeys and emails themselves, keeping the contact-based consent system in place in outbound marketing. Leveraging the ability to use the outbound marketing subscription centers (see [Use outbound subscription centers in Customer Insights - Journeys](real-time-marketing-outbound-subscription.md), emails will be able to respect the previously captured consent and keep updating regardless of whether the journey is built in outbound marketing or real-time journeys. Once all journeys have been transitioned, transition the consent by completing the following steps:
- Create a real-time journeys preference center based on a compliance profile.
- Configure topics that match subscription lists.
-	Use the Load Consent tool to copy consent from contacts and subscription lists.
-	Switch emails to use the newly created compliance profile.
-	Recreate segments based on topics (optional).

When capturing consent from contacts, implementing a double opt-in (DOI) feature is sometimes necessary. You can [activate the DOI for your compliance profile in real-time journeys](real-time-marketing-double-opt-in.md).

## Consent transition FAQ

### Can I continue using outbound marketing's subscription center after outbound is removed?
The outbound marketing subscription center isn't available once outbound marketing is removed.

### Can I embed a preference center on my own web page?
Not at this time. 
 
[!INCLUDE [transition-comments](./includes/transition-comments.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
