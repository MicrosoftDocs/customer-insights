---
title: Pause and resume a journey
description: Learn how to pause and resume a journey in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/26/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Pause and resume a journey

The pause and resume feature lets you temporarily pause customer journeys in response to unplanned events, without stopping and recreating the journey. This feature helps protect your brand’s reputation and maintain customer trust during sensitive periods like natural disasters, service outages, or content errors.

## Why pause a journey?

You might want to pause a journey when:

- A mistake is discovered after the journey goes live.
- A call center or website goes offline.
- A product goes out of stock.
- A natural disaster or national emergency occurs.
- You want to temporarily suspend outreach to avoid appearing insensitive.

## What happens when you pause a journey?

When a journey is paused:

- No new customers enter the journey.
For the public preview, customers who have already started the journey will complete it during the paused period. 
- For the general availability update of this feature, any journey step that causes the customer to wait, such as a wait for time, trigger, or segment membership, will pause customers at the next message step.  
- You can pause a journey for up to 21 days.

> [!NOTE]
> For one-time, segment-based journeys, customers in the original segment can't re-enter the journey after it resumes. Only the remaining members of the segment proceed.

## What happens when you resume a journey?

You can resume a journey in two ways:

- **Manual resume**: Resume the journey at any time within the 21-day pause window.
- **Scheduled resume**: Set a specific date and time for the journey to resume automatically.

Once resumed, new customers can enter the journey again and queued triggers are processed.

## Editing during a pause

While a journey is paused, you can make edits using the same capabilities available in live editing. This includes:

- Adding or editing branches.
- Deleting or modifying message steps.
- Adjusting the resume schedule.

> [!TIP]
> Be mindful of how edits affect queued triggers and customer flow. Some changes can require publishing a new version of the journey.

## Known limitations

- The pause duration is limited to 21 days from the original pause date. If the journey isn't resumed within 21 days, the journey stops.
- Trigger queues have a maximum capacity. If the queue is full, additional triggers are dropped.
- In preview, customers are paused only at specific steps. General availability expands this to include message tiles.

## Example scenario

A national bank runs a campaign to contact borrowers at risk of foreclosure. When a hurricane strikes, the bank pauses the journey to avoid appearing insensitive. After the emergency passes, the bank resumes the journey without needing to rebuild or resegment the audience.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
