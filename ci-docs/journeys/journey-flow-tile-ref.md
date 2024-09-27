---
title: Journey flow and tile reference
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

# Journey flow and tile reference

This article describes the various journey capabilities available in Customer Insights - Journeys. For complete examples of creating customer journeys, see [Create a trigger-based journey](real-time-marketing-trigger-based-journey.md) and [Create a segment-based journey](real-time-marketing-segment-based-journey.md).

## Journey start

The journey start configuration lets you define how customers can start the journey. There are two types of journeys you can create: [Trigger-based journeys](journey-start.md#trigger-based-journey) and [Segment-based journeys](journey-start.md#segment-based-journey). For more information, see [Start a journey](journey-start.md).

## Journey goal

Journey goals let you track and [analyze the performance of the journey](real-time-marketing-analytics.md). You can use a trigger as the journey goal and measure the success of the journey based on the customers who perform the trigger as they're going through the journey.

Journey goals can also help you determine the winner of A/B tests and find the best channel for channel optimization. For more information about using A/B tests, see [A/B tests in Customer Insights - Journeys](real-time-marketing-ab-tests-in-marketing-journeys.md).

## Messaging customers

Customer Insights - Journeys customer journeys let you reach customers through various channels including:

- [Send an email](real-time-marketing-email.md)
- [Send a text message](real-time-marketing-outbound-text-messaging.md)
- [Send a push notification](push-messages.md)

### A/B test

A/B tests allow you to measure which channel or content messaging strategy leads to higher success. For more information about using A/B tests, see [A/B tests in Customer Insights - Journeys ](real-time-marketing-ab-tests-in-marketing-journeys.md).

### Channel optimization

Channel optimization uses AI to find the best channel to reach each individual customer and improve your engagement. To learn more about channel optimization, see [Use AI-driven run-time channel optimization](real-time-marketing-channel-optimization.md).

## Branching the customer journey

### If/then branch

The if/then branch lets you branch the customer journey based on customer actions like opening an email or completing a purchase. The if/then branch waits for the customer to perform the trigger within the time limit specified. If the customer performs the trigger, they'll immediately proceed down the yes branch. If the customer doesn't perform the trigger within the time limit specified, they'll proceed down the no branch after the time limit has passed.

For example, you can configure the if/then branch to wait for the *Email opened* event on a previously sent email. If the time limit is set to *1 day*, the if/then branch waits for the customer to open the email within that day. If the customer opens the email within that day, they'll immediately proceed down the yes branch. If the customer doesn't open the email within that day, they'll proceed down the no branch after one day.

### Attribute branch

The attribute branch lets you branch the journey based on various attributes including:

- **Customer's attributes**: You can branch the journey based on the customer's attributes like address or age. The journey's audience defines which attributes will be shown. For example, if the journey is for Contacts, only attributes for Contacts will be shown.
- **Customer's segment membership**: You can branch the journey based on whether the customer is part of a segment. The journey's audience defines which segments will be shown. For example, only Contacts-based segments will be shown for journeys that are meant for Contacts.
- **Attributes in triggers**: You can branch the journey based on attribute values in triggers. For attribute values to be shown, the trigger must have previously occurred in the journey. Thus, you can only check the attribute values for a trigger that starts a trigger-based journey, or triggers being used in an if/then branch.

The attribute branch checks for attribute values the moment a customer enters this step. For example, when a customer enters the attribute branch step, the segment membership condition will check whether the customer is part of the specified segment at that instant.

### Audience split

The audience split tile allows you to divide your audience to give a unique set of experiences to random sets of the audience. You can split by percentage or split by number. Learn more: [Preview: Split your audience into groups](real-time-marketing-split-audience.md)

## Activate a custom trigger

Triggering a custom event allows you to use activate a custom event at any point in the customer journey. Additional journeys or [Power Automate flows](/power-automate) connected to the custom event will be triggered immediately when a customer reaches the tile. This includes custom triggers used in exit criteria, goals, and if/then branches for journeys.

When using a custom trigger, you can choose which data to send as part of the trigger. You can choose customer profile data (for instance, attributes of the target audience such as contacts, leads, etc.) and data from other triggers used in the journey (for instance, attributes of the trigger that starts the journey).

For example, a loan application journey could have various steps that require a human agent’s approval. By creating a separate customer journey or Power Automate Flow for loan exception approval, you can trigger it from various points in the loan application journeys where exceptions can occur. The data you send with the trigger can be used to populate dynamic content or as inputs to other Flow actions.

To learn more about triggering a custom event, see [Preview: Trigger an action outside of a journey](real-time-marketing-custom-actions.md).

## Wait

The wait step holds the customer in the journey for the specified wait period.

> [!IMPORTANT]
> The maximum time a wait tile can wait for is 90 days or 12 weeks. The maximum time limitation applies whether selecting an amount of time or setting a fixed date.

You can configure the wait step using the following parameters:

- **A set amount of time**: Customers wait for the specified amount of time (for example, one hour or one day). The time period starts as soon as customers enter the wait step.
- **Until a specific date and time**: Customers wait until the specified date and time. If the date and time are already in the past, customers will immediately proceed to the next step.
- **Until a time specified by a trigger**: For trigger-based journeys, customers wait for the date and time specified by a trigger attribute. This configuration is useful for scenarios like appointment reminders, where you can choose to wait one day before the appointment to send a reminder. The date and time information must be included in the trigger that started the journey for the customer.

## Journey end

[!INCLUDE [footer-include](./includes/footer-banner.md)]
