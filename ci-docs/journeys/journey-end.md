---
title: Journey end
description: An overview of the Journey end configuration in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/12/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Journey end

By default, customers end the journey when they complete all the steps. You can set additional ways for customers to exit the journey by using triggers or segments.

- **Exit when an event occurs**: Customers who perform this trigger will immediately exit the journey no matter where they are in the journey. This provides an easy way to remove customers who perform the trigger from the journey, ensuring that customers don't receive irrelevant messages from your customer journey.
- **Exit by segment**: Customers who are part of this segment will immediately exit the journey. This capability is often referred to as a suppression segment and helps you ensure that members of this segment are suppressed from the customer journey. Exit by segment removes members of that segment from wherever they are in the customer journey. This is notably different from the *exclude by segment* property in journey start, which will only exclude members of the exclusion segment from starting the journey.
