---
title: Control how fast customers enter a journey
description: Control how fast customers can enter a journey in Customer Insights - Journeys
ms.date: 10/17/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Control how fast customers enter a journey

There are times when you want to reach a large audience. However, sending one message to the entire audience at the same time can cause issues such as overwhelming call centers or your website. To solve this, you might want to control how fast audience members enter a journey, avoiding thousands of simultaneous phone calls or website visits.

With journey rate limiting, you can space out message sending or other actions over time. This is done by specifying the number of audience members that can enter the journey on a per hour or per day basis. You can also control which days of the week audience members can enter the journey.  

To set a rate limit, open a journey in the journey designer, select the entry tile, and then select the **Settings** tab from the toolbar.

:::image type="content" source="media/rate-limit.png" alt-text="Screenshot of the Settings tab in the journey designer showing options to enable a rate limit and control how fast audience members enter the journey." lightbox="media/rate-limit.png":::

## Considerations when setting a rate limit

- The rate limit only controls how many audience members can enter the journey in the specified interval (per hour or per day). It doesn't evenly spread out those who can enter. This can result in bursts of audience members entering the journey. For example, if 60 members can enter per hour, those 60 members enter as fast as possible and aren't spread out as one member per minute.
e.
- Rate limiting can lead to bursts of messages sent when quiet times end. During quiet times, audience members can enter the journey, but their messages are queued. The queued messages are sent as soon as quiet time ends. This can result in more messages being delivered than the configured journey rate limit. For example, if the journey is rate limited to 100 members per hour and there's a message with an eight hour quiet window, no messages are delivered for those eight hours. After this period, 800 messages are delivered in a burst.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
