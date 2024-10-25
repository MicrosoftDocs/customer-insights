---
title: End a journey
description: An overview of the journey end configuration in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/25/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# End a journey

By default, customers end the journey when they complete all the steps. You can set additional ways for customers to exit the journey by using triggers or segments.

- **Exit when an event occurs**: Customers who perform this trigger immediately exit the journey no matter where they are in the journey. This provides an easy way to remove customers who perform the trigger from the journey, ensuring that customers don't receive irrelevant messages from your customer journey.
- **Exit by segment**: Customers who are part of this segment immediately exit the journey. This capability is often referred to as a "suppression segment" and helps you ensure that members of this segment are suppressed from the customer journey. Exit by segment removes members of that segment from wherever they are in the customer journey. This is notably different from the *exclude by segment* property in journey start, which only excludes members of the exclusion segment from starting the journey.

## Journey goal

Journey goals let you track and [analyze the performance of the journey](real-time-marketing-analytics.md). You can use a trigger as the journey goal and measure the journey's success based on the customers who perform the trigger as they're going through the journey.

Journey goals also help you determine the winner of A/B tests and find the best channel for channel optimization. For more information about using A/B tests, see [A/B tests in Customer Insights - Journeys](real-time-marketing-ab-tests-in-marketing-journeys.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
