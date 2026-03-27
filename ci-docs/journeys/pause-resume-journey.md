---
title: Pause and resume a journey
description: Learn how to pause and resume a journey in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/26/2026
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Pause and resume a journey

You can temporarily pause customer journeys in response to unplanned events, without stopping and recreating the journey. This feature helps protect your brand’s reputation and maintain customer trust during sensitive periods like natural disasters, service outages, or content errors.

## Why pause a journey?

You might want to pause a journey when:

- A mistake is discovered after the journey goes live.
- A call center or website goes offline.
- A product goes out of stock.
- A natural disaster or national emergency occurs.

## What happens when you pause a journey?

Pausing a journey prevents new entries and stops customers who have already entered the journey.

- `Pause` is fully supported at entry and message tiles.
- `Wait for trigger` and `segment membership support` pause within their configured time limit.
    - If a user meets the condition within the time limit and the journey resumes before the time limit expires, the contact moves to the branch where the condition is met.
    - If the time limit expires before the journey resumes, the user automatically moves to the branch where the condition isn't met.
- Users in any other tile move to the first tile where pause is supported and are paused there until the journey resumes.
- For one-time, segment-based journeys, customers in the original segment can't re-enter the journey after it resumes. Only the remaining members of the segment proceed.
- For repeating, segment-based journeys, repeating occurrences and segment evaluations are skipped while the journey is paused.

You can pause a journey for up to 21 days. If the journey isn't resumed within 21 days, the journey stops.

> [!NOTE]
> Trigger queues have a maximum capacity. If the queue is full, additional triggers are dropped.

## What happens when you resume a journey?

You can resume a journey in two ways:

- **Manual resume**: Resume the journey at any time within the 21-day pause window.
- **Scheduled resume**: Set a specific date and time for the journey to resume automatically.

Once resumed, new customers can enter the journey again, customers who are paused resume the journey, and queued triggers are processed.

## Editing during a pause

While a journey is paused, you can make edits using the same capabilities available in live editing. This includes:

- Adding or editing branches.
- Deleting or modifying message steps.
- Adjusting the resume schedule.

> [!TIP]
> Be mindful of how edits affect queued triggers and customer flow. Some changes can require publishing a new version of the journey.

## Example scenario

A national bank runs a campaign to contact borrowers at risk of foreclosure. When a hurricane strikes, the bank pauses the journey to avoid appearing insensitive. After the emergency passes, the bank resumes the journey without needing to rebuild or resegment the audience.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
