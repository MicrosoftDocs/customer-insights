---
title: Create an event from another event
description: Describes how to create an event from another event when creating a new event in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/18/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Create an event from another event

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> To use event management in the real-time journeys area of Customer Insights - Journeys, you must enable the feature switch. To enable the feature switch:
>
> 1. Go to **Settings** > **Overview** > **Feature switches**.
> 1. Enable the **Enable events creation in real-time journeys** feature switch toggle.

You can copy your existing event by using the **Save as** command on the toolbar.

This operation will copy most of the entities from your existing event to a new one. The copied entities include:

- Pass
- Session
- Session Track
- Speaker Engagement
- Sponsorship
- Event Custom Registration Field
- Business Process Flow
- Team Members
- Session Tracks

> [!NOTE]
> Registrations are excluded from the copy operation to prevent potential issues that could arise in the capacity management and ticketing of new events. Child events of a recurrent event are also not copied to the new event. Learn more: [Known issues and workarounds](known-issues.md#event-management).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
