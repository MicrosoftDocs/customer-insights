---
title: Customer Insights - Journeys link tracking mechanics
description: Learn how link tracking mechanics work in Dynamics 365 Customer Insights - Journeys, including trackable links, consent, and anonymous interactions.
ms.date: 09/02/2026
ms.topic: article
author: Joni-M
ms.author: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Customer Insights - Journeys link tracking mechanics

This article explains Customer Insights - Journeys link tracking mechanics, including how the system replaces relevant hyperlinks with trackable links and adds an invisible pixel to HTML messages. Use this information to understand how the application detects message opens and link clicks based on recipient consent.

As of June 10, 2026, replaced links use the following format:

`https://[hashed-organization-identifier-without-dashes].[island-number-specific].[geo-specific].prod.marketingusercontent.com/api/orgs/[hashed-organization-identifier]/r/[link-identifier]`

The application replaces links when the following conditions are met:

- The links aren't marked as **non-trackable** inside the message editor.
- The recipient customer profile shows that the customer consents to tracking.

When the recipient selects a link or opens a message with a tracking pixel, two things happen:

1. The recipient is redirected to the original URL.
1. The application records the link click interaction.

If the recipient previously opted out of tracking, the system generates the interaction as anonymous. When the recipient opts out, the interaction doesn't store a customer profile reference. The system caches the consent for tracking for 24 hours, which means the interaction can be stored as non-anonymous even if the customer opted out in the past 24 hours.

> [!NOTE]
> All links generated in the [text message channel](real-time-marketing-outbound-text-messaging.md) are shortened, regardless of whether the application replaces them with tracking links.

## See also

- [Manage user compliance settings in Customer Insights - Journeys](real-time-marketing-compliance-settings.md)  
- [Manage consent for email and text messages in Customer Insights - Journeys](real-time-marketing-email-text-consent.md)
