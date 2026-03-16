---
title: Set message expiration in real-time journeys
description: Learn how to set a message expiration for real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/16/2026
ms.topic: article
author: Joni-M
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Set message expiration in real-time journeys

Customers can enter a real-time journey at any time. If your journey includes time-sensitive content such as event reminders, limited-time offers, or expiring coupons, you can prevent outdated messages from being sent by setting an expiration on a message tile. When a message expires, customers who reach that message after the expiration time don’t receive it and continue through the rest of the journey without interruption.

## What is a message expiration?

Message expirations let you define conditions that determine when a message should no longer be sent in a real-time journey. Once a message reaches its expiration condition:

- The message is skipped for customers who reach it after the expiration time.
- Customers continue to the next step in the journey.
- The skipped message is tracked in analytics as **Message expired**.

Message expirations help you keep communications accurate and relevant without needing to frequently update or republish your journeys.

## Supported channels

Message expirations are supported for the following message types in real-time journeys:

- Email
- SMS
- Push notifications
- Custom channels

## How message expirations work

When you enable message expiration on a message tile:

- You choose how the expiration time is determined.
- Expiration always uses the journey’s time zone.
- You must set expiration conditions to a time in the future.
- If an audience member reaches the message after the expiration time, the message isn’t sent and the audience member continues to the next step in the journey.

## Ways to define when a message expires

You can define message expiration in two ways: by a **fixed date and time**, or **relative to a time provided by a trigger**.

### Option 1: Expire at a selected date and time

Use this option when you know the expiration in advance.

- You select a specific date and time when the message expires.
- The message expires at that exact moment in the journey’s time zone.

This option is useful for scenarios such as campaign end dates or fixed deadlines.

### Option 2: Expire relative to a trigger-specified time

Use this option when the expiration depends on a time value coming from the trigger (for example, a birthday). When you choose this option, you select how the message expiration relates to the trigger time:

- **Before the specified time** and you chose an offset.
- **At the specified time**.
- **After the specified time** and you chose an offset.

This option is useful for scenarios such as reminders before an event, messages valid only during an event window, or follow-up messages that should stop sending after a certain period.

## Set a message expiration

1. Open your real-time journey.
1. Select a message tile (email, SMS, push, or custom).
1. In the message properties pane, go to the **Message expiry** section and choose how the expiration time is defined:
:::image type="content" source="media/message-expiration-section.png" alt-text="Screenshot of the quiet times settings applied in a journey, showing messages held due to quiet times." lightbox="media/message-expiration-section.png":::
    1. **Expire on a specific data and time**.
    :::image type="content" source="media/message-expiration-date.png" alt-text="Screenshot of the quiet times settings applied in a journey, showing messages held due to quiet times." lightbox="media/message-expiration-date.png":::
    1. **Expire at a time specified by a trigger**, with the desired timing option (before, at, or after).
    :::image type="content" source="media/message-expiration-trigger.png" alt-text="Screenshot of the quiet times settings applied in a journey, showing messages held due to quiet times." lightbox="media/message-expiration-trigger.png":::

> [!IMPORTANT]
> If a live journey uses the **Expire at a time specified by a trigger** option and the trigger date is more than one year in the past (for example, a birthday), the system automatically adjusts the date to the current year when evaluating the message expiration.

[!INCLUDE [footer-include](./includes/footer-banner.md)]