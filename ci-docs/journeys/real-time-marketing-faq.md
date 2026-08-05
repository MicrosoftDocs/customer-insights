---
title: FAQs for Customer Insights - Journeys
description: Find answers to frequently asked questions about channel A/B testing, channel optimization, and engagement rate in Customer Insights - Journeys.
ms.date: 08/04/2026
ms.topic: faq
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# FAQs for Customer Insights - Journeys

Read this article to find answers to frequently asked questions about channel A/B testing and channel optimization in Customer Insights - Journeys.

## Channel A/B testing

### Why is the audience split not exactly the same as when I was authoring the A/B test?

If your A/B test audience is set to 50-50 across the audience, the app will attempt to respect the distribution, but the split will not always be exact. An uneven split is the result of A/B test performance optimization. The overall results of determining a winner variant are not affected.

### I see that the inflow before the A/B test is 85, but the split across version A and B is 63 and 16. What happened to the rest of the audience?

Some audience members may not have proper consent permissions to receive the message through the channel indicated in the A/B test. The missing audience members could also be due to a system failure.

## Channel optimization

### How is channel optimization related to a goal?

Setting a journey goal is a prerequisite for using channel optimization. The goal metric used to define your journey's success is what the AI model uses to optimize in channel optimization. It is important to use an accurate goal metric so that you can attain the best results with channel optimization.

### How does channel optimization use AI to determine the best channel?

When enabled, channel optimization uses each customer's individual interaction data (such as unique clicks, opens, and other engagement metrics) and the journey goal to calculate the likely best channel for that customer to interact with. The AI model only collects historical data like email opens, clicks, and unsubscribes to determine the level of that person's engagement with a specific channel. The model doesn't collect transactional or any other data from your customers.

### What does the default channel do?

The default channel acts as a control group, so 10 percent of your audience funnels through the default channel without any AI applied. This setup helps you compare the performance of the control group audience versus the audience that the AI recommends. This comparison is based on which group achieved the journey goal.

### How is the engagement rate determined in channel optimization?

- **Push notifications**: Number of unique people that open or clicked a link divided by total number of push notifications sent.
- **Email**: The number of unique people that opened or clicked a link divided by total number of emails sent.
- **SMS**: The number of unique people that clicked a link divided by the total number of SMS (text) messages sent.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
