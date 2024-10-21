---
title: Journey flow
description: Learn about journey flow and tiles in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/02/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Journey flow

This article describes the various journey capabilities available in Customer Insights - Journeys. For complete examples of creating customer journeys, see [Create a trigger-based journey](real-time-marketing-trigger-based-journey.md) and [Create a segment-based journey](real-time-marketing-segment-based-journey.md).

## Journey start

The journey start configuration lets you define how customers can start the journey. There are two types of journeys you can create: [Trigger-based journeys](journey-start.md#trigger-based-journey) and [Segment-based journeys](journey-start.md#segment-based-journey). For more information, see [Start a journey](journey-start.md).

## Branching the customer journey

### If/then branch

The if/then branch lets you branch the customer journey based on customer actions like opening an email or completing a purchase. The if/then branch waits for the customer to perform the trigger within the time limit specified. If the customer performs the trigger, they'll immediately proceed down the yes branch. If the customer doesn't perform the trigger within the time limit specified, they'll proceed down the no branch after the time limit has passed.

For example, you can configure the if/then branch to wait for the *Email opened* event on a previously sent email. If the time limit is set to *1 day*, the if/then branch waits for the customer to open the email within that day. If the customer opens the email within that day, they'll immediately proceed down the yes branch. If the customer doesn't open the email within that day, they'll proceed down the no branch after one day.

## Journey end

By default, customers end the journey when they complete all the steps. You can set additional ways for customers to exit the journey by using triggers or segments such as when an event occurs. For more information, see [End a journey](journey-end.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
