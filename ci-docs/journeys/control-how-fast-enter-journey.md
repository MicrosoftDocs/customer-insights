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

There are times when you want to reach a large audience, but sending a message to the entire audience at the same time would cause problems such as overwhelming your call center or website (if your customers are expected to call or visit the website to view a page/fill a form). Instead, you may want to control how fast audience members enter the journey, avoiding thousands of phone calls or website visits at the same time.

With journey rate limiting, you can space out message sending or other actions over time by specifying number of audience members that can enter the journey on a per hour or per day basis. You can also control which days of the week they can enter the journey.  

To set rate-limit, open the journey in the journey designer and select the entry tile and then settings tab from the toolbar.

:::image type="content" source="media/rate-limit.png" alt-text="Enable a rate limit to control how fast audience members enter this journey.":::

A few key points to note:

* This capability is only available for one-time segment-based journeys.  It is not available for other journey types (i.e., recurring or ongoing segment-based journeys or trigger-based journeys).  

* When journey is configured to have rate-limit, the first batch of eligible audience members enter the journey when it starts. The next batch of eligible members enter the journey at the next period (i.e., next hour or next day) until all members have entered the journey.

* The rate limitation only controls how many audience members can enter the journey in the specified interval (per hour or per day). It does not evenly spread out those who are allowed to enter. This can result in bursts of audience members entering the journey. For example, if 60 members are allowed to enter per hour, those 60 members will enter as fast as possible (and will not be spread out as 1 per minute).

* Rate limiting and quiet times may lead to bursts of messages sent when quiet times end. During quiet times, audience members may enter the journey, but their messages will be queued. All those queued messages will be sent as soon as the quiet time ends. This can result in more messages being delivered than the configured journey rate limit. For example, if the journey is rate limited to 100 members per hour and there is a message with 8 hours quiet window, no messages will be delivered for those 8 hours but then, at the end of that period, 800 messages will be delivered in a burst.
