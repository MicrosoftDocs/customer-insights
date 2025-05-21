---
title: Preview: Proactive engagement concepts"
description: Learn more about proactive engagement concepts in in Dynamics 365 Customer Insights - Journeys.
ms.date: 05/08/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Preview: Concepts

> [!IMPORTANT]
> A preview feature is a feature that isn't complete but is made available before it’s officially released so customers can get early access and provide feedback. Preview features aren’t meant for full use and may have limited or restricted functionality.
>
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won't be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data, or other data that are subject to legal or regulatory compliance requirements.

**Conversational journeys** leverage existing capabilities from both **Customer Insights – Journeys** and **Contact Center**. This article introduces several concepts that are commonly used when working with conversational journeys.

## Journey
A [journey](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/journeys-overview) in Dynamics 365 Customer Insights – Journeys is a visual, automated workflow that guides how your customer moves through a series of interactions. It orchestrates personalized experiences across channels like voice, email, SMS, push notifications, and more, based on user behavior and business logic.

## Interaction
An interaction is any engagement a customer has with your brand, such as opening an email, clicking a link, or answering a voice call. These are tracked and used to inform journey progression and analytics.

## Segment
A [segment](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/real-time-marketing-segments) is a defined group of customers that share common attributes or behaviors. Segments are used to target specific audiences within journeys, enabling tailored messaging and actions.

## Trigger
A [trigger](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/real-time-marketing-trigger-based-journey) is an event or condition that initiates or advances a customer through a journey. For example, a trigger could be a form submission, a product purchase, or a link click.

## Conversational voice

## Proactive engagement

## Wait for trigger branch
The [wait for trigger](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/add-action#wait-for-trigger-branch) action pauses a journey until a specific event occurs. This allows the journey to respond dynamically to customer behavior, such as waiting for a voice call to end before sending a follow-up email.

## Attribute branch
[Attribute branching](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/add-action#attribute-branch) is a decision point in a journey that routes customers based on specific attributes (e.g., outcomes of a voice call). It enables personalized paths within the same journey.

## Analytics
[Analytics](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/analytics-overview) refers to the reporting and insights available for journeys, segments, and interactions. It includes metrics like call-attempted rates, delivery rates, click-through rates, conversion rates, and journey performance.

## Quiet time
[Quiet times](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/real-time-marketing-quiet-times) are configured periods during which no messages are sent to customers. This ensures communications are respectful of time zones, holidays, or preferred customer hours.

## Frequency cap
[Frequency capping](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/real-time-marketing-frequency-cap) limits how often a contact receives messages within a certain timeframe. This helps prevent over-communication and reduces the risk of unsubscribes or spam complaints.
