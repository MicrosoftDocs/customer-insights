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
> **[Outbound marketing](user-guide.md) will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Consent is an essential requirement that allows customers of Customer Insights – Journeys to send marketing messages. Customers who already use outbound marketing can transition consent settings to real-time journeys. Consent management, however, is more sophisticated in real-time journeys. The differences and how to transition consent are described in: [Consent management and double opt-in transition guidance](real-time-marketing-consent-transition.md). This article also describes how to migrate subscription lists to real-time journeys to send out segment-based newsletters. For a more detailed discussion, see [Understanding consent management in Dynamics 365 Customer Insights - Journeys - Dynamics FastTrack Blogs](https://community.dynamics.com/blogs/post/?postid=8b2a4ee8-1069-ee11-a81c-000d3a7a1a66)

Customers going through the transition to real-time journeys are recommended to focus initially on moving the journeys and emails themselves, keeping the contact-based consent system in place in outbound marketing. Leveraging the ability to use the outbound marketing subscription centers (see [Use outbound subscription centers in Customer Insights - Journeys](real-time-marketing-outbound-subscription.md), emails will be able to respect the previously captured consent and keep updating regardless of whether the journey is built in outbound marketing or real-time journeys. Once all journeys have been transitioned, transition the consent by completing the following steps:
- Create a real-time journeys preference center based on a compliance profile.
- Configure topics that match subscription lists.
-	Use the Load Consent tool to copy consent from contacts and subscription lists.
-	Switch emails to use the newly created compliance profile.
-	Recreate segments based on topics (optional).

When capturing consent from contacts, implementing a double opt-in (DOI) feature is sometimes necessary. DOI isn't currently available in real-time journeys natively. However, the consent management and double opt-in article above also describes how DOI can be achieved using both modules (outbound marketing and real-time journeys). This DOI method could make sense, especially if you've already set up DOI in outbound marketing.

Customers who want to start with real-time journeys and need DOI implemented will need to wait until this feature becomes available.

## Relevant upcoming features

The features listed below may be of interest as you transition from outbound marketing to real-time journeys. These features provide parity, equivalent, or better functionality than what was available in outbound marketing.

- **Double opt-in**: Double opt-in enables explicit consent requests from customers, allowing you to meet data protection regulations. Double opt-in helps reduce spam, lowering bounce rates and enhancing your sender reputation. Learn more: [Improve engagement and compliance with double opt-in](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/improve-engagement-compliance-double-opt-in)
- **Consent management view**: Streamline consent management with a new unified view. Quickly update customer consents, see if a customer has opted out of communications, and understand their preferences across all mediums - emails, texts, and custom channels. Control and manage what messages your customers receive, all at a glance. Learn more: [Easily manage customer consent from contact and lead forms](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/easily-manage-customer-consent-contact-lead-forms)

> [!TIP]
> If you have questions or comments, visit the [Outbound to real-time transition community forum](https://community.dynamics.com/forums/thread/?partialUrl=Outbound-to-Real-Time-Transition)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
