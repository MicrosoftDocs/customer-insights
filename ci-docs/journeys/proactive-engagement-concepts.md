---
title: Conversational journeys concepts (preview)
description: Conversational journeys in Dynamics 365 Customer Insights – Journeys helps you automate personalized customer interactions across channels. Learn key concepts and get started.
ms.date: 05/29/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:05/27/2025
---

# Conversational journeys concepts (preview)

[!INCLUDE [Preview banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Conversational journeys use existing capabilities from Dynamics 365 Customer Insights – Journeys and Dynamics 365 Contact Center. This article introduces several concepts that you use when working with conversational journeys.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## Journey

A [journey](journeys-overview.md) in Customer Insights – Journeys is a visual, automated workflow that guides how a customer moves through a series of interactions. It orchestrates personalized experiences across channels like voice, email, SMS, push notifications, and more, based on user behavior and business logic.

## Interaction

An [interaction](license-setup.md#how-is-customer-insights---journeys-licensed) is any time a customer engages with your brand, like opening an email, selecting a link, or answering a voice call. The system tracks interactions to inform journey progression and analytics.

## Segment

A [segment](real-time-marketing-segments.md) is a defined group of customers that share common attributes or behaviors. Segments are used to target specific audiences within journeys, enabling tailored messaging and actions.

## Trigger

A [trigger](real-time-marketing-trigger-based-journey.md) is an event or condition that starts or moves a customer through a journey. For example, a trigger can be a form submission, a product purchase, or a link click.

## Conversational voice

Conversational voice is a step in the customer journey that calls the customer using an AI agent or a customer service representative. This step needs integration with Contact Center, where both AI and human agents are managed.

## Proactive engagement

Proactive engagement is a table in Contact Center that has settings, configurations, and behaviors that control how agent queues are managed, which phone numbers are used, and whether calls are automatically recorded and transcribed.

## Wait for trigger branch

The [Wait for Trigger](add-action.md#wait-for-trigger-branch) action pauses a journey until a specific event occurs. This action lets the journey respond dynamically to customer behavior, like waiting for a voice call to end before sending a follow-up email.

## Attribute branch

[Attribute branching](add-action.md#attribute-branch) is a decision point in a journey that routes customers based on specific attributes (for example, outcomes of a voice call). It enables personalized paths within the same journey.

## Analytics

[Analytics](analytics-overview.md) is reporting and insights for journeys, segments, and interactions. It includes metrics like call-attempted rates, delivery rates, click-through rates, conversion rates, and journey performance.

## Quiet time

[Quiet times](real-time-marketing-quiet-times.md) are set periods when no messages are sent to customers. This approach respects time zones, holidays, and preferred customer hours.

## Frequency cap

[Frequency capping](real-time-marketing-frequency-cap.md) limits how often a contact receives messages within a certain timeframe. This helps prevent sending too many messages and lowers the risk of unsubscribes or spam complaints.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
