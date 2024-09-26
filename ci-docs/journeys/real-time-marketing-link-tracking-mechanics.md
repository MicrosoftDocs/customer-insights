---
title: Customer Insights - Journeys link tracking mechanics
description: Learn about link tracking mechanics in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/10/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Customer Insights - Journeys link tracking mechanics

> [!IMPORTANT]
> Starting on October 10, 2024, links in messages that were sent more than six months prior will no longer produce tracking results, but will otherwise function correctly. Links in messages sent less than six months prior will continue to generate tracking analytics.

When executing customer journeys, all relevant hyperlinks are replaced with trackable links. If the content of a message is HTML, we also create an invisible pixel inside the message body. The invisible pixel is necessary to determine whether a user clicked on a link or opened the message.

Replaced links have the following format:

`https://[geo-specific].dynamics.com/api/orgs/[hashed organization-identifier]/r/[link identifier]`

Links are replaced when the following conditions are met:

- The links aren't marked as **non-trackable** inside the message editor.
- The recipient customer profile indicates that the customer has consented to tracking.

When the recipient selects a link or opens a message with a tracking pixel, two things happen:

1. The recipient is redirected to the original URL.
1. The link click interaction is recorded.

If the recipient previously opted out from tracking, the interaction is generated as anonymous. When the recipient has opted out, the interaction doesn't store a customer profile reference. The consent for tracking is cached for 24 hours. That means the interaction can be stored as non-anonymous although the customer has opted out in the past 24 hours.

> [!NOTE]
> All links generated in the [text message channel](real-time-marketing-outbound-text-messaging.md) are shortened, regardless of whether they are replaced with tracking links.

## See Also
[Manage user compliance settings in Customer Insights - Journeys](real-time-marketing-compliance-settings.md)
[Manage consent for email and text messages in Customer Insights - Journeys](real-time-marketing-email-text-consent.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
