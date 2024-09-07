---
title: "Preview: Control how fast customers can enter a journey"
description: Control how fast customers can enter a journey in Customer Insights - Journeys
ms.date: 09/04/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Control how fast customers can enter a journey

There are times when you want to reach a large audience. However, sending one message to the entire audience at the same time can cause certain problems such as overwhelming  call centers or your website. To solve this issue, you might want to control how fast audience members enter the journey, avoiding thousands of simultaneous phone calls or website visits at the same time.

With journey rate limiting, you can space out message sending or other actions over time. This is done by specifying the number of audience members that can enter the journey on a per hour or per day basis. You can also control which days of the week audience members can enter the journey.  

To set rate-limit, open the journey in the journey designer and select the entry tile and then settings tab from the toolbar.

:::image type="content" source="media/rate-limit.png" alt-text="Enable a rate limit to control how fast audience members enter this journey.":::

A few key points to note:

* This capability is only available for one-time segment-based journeys. It isn't available for other journey types (that is, recurring or ongoing segment-based journeys or trigger-based journeys).  

* When the journey is configured to a have rate-limit, the first batch of eligible audience members enters the journey when it starts. The next batch of eligible members enters the journey at the next period (that is, the next hour or next day) until all members have entered the journey.

* The rate limitation only controls how many audience members can enter the journey in the specified interval (per hour or per day). It doesn't evenly spread out those who are allowed to enter. This can result in bursts of audience members entering the journey. For example, if 60 members are allowed to enter per hour, those 60 members enter as fast as possible and won't be spread out as 1 per minute.

* Rate limiting may lead to bursts of messages sent when quiet times end. During quiet times, audience members may enter the journey but their messages are queued. All those queued messages are sent as soon as quiet time ends. This can result in more messages being delivered than the configured journey rate limit. For example, if the journey is rate limited to 100 members per hour and there's a message with an 8 hour quiet window, no messages are delivered for those 8 hours. After this period, 800 messages will be delivered in a burst.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
