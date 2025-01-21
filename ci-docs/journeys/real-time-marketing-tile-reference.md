---
title: Real-time journeys tile reference
description: Learn about tiles in Dynamics 365 Customer Insights - Journeys.
ms.date: 12/04/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Real-time journeys tile reference

This article describes the various journey capabilities available in Customer Insights - Journeys. For complete examples of creating customer journeys, see [Create a trigger-based journey](real-time-marketing-trigger-based-journey.md) and [Create a segment-based journey](real-time-marketing-segment-based-journey.md).

## Journey start

The journey start configuration lets you define how customers can start the journey.

### Trigger-based journey

- **Trigger to start the journey**: Customers start the journey as soon as the selected trigger occurs.  
- **Repeating the journey**: Lets you configure how soon customers can repeat the journey if the trigger to start the journey occurs again. You can allow customers to repeat the journey immediately, or only allow them to repeat the journey after a delay interval.
- **Exclude this segment**: Members of this segment won't be allowed to start the journey. This is an easy way to filter out certain segments of customers from starting the journey, even if they performed the trigger to start the journey.  
- **Journey Timing**: Lets you specify the time window in which customers can start the journey. Customers must perform the journey start trigger after the start time to enter the journey. No new customers will be allowed to start the journey after the end time. The end time only affects when customers can start the journey. If a customer is already in the journey, they'll be allowed to continue the journey even after the end time.
- **Handling unresolved profile**: This option is only available for trigger-based journeys that target Customer Insights - Data profiles. It takes time to create a full Customer Insights - Data profile. If the full profile isn’t available at the time the person triggers the journey, they can either start the journey immediately using defaults for any missing profile data or wait for the full profile to be available before starting the journey. To successfully communicate with someone without a profile, the trigger must specify email (contactpoint_email) or phone (contactpoint_phone) attributes. See [Create a custom trigger](real-time-marketing-custom-triggers.md). <br>
For journeys such as sending purchase order confirmations, both new customers and existing customers can trigger the journey. A new customer may not have a full profile when they make the purchase. By selecting the option to start the journey immediately even if the full profile isn't available, you can ensure new users get the order confirmation immediately without having to wait. All profile attributes for these new users will be treated as empty, so it's important to always include default fallbacks in personalized content as well as attribute branches.

### Segment-based journey

- **Audience**: The audience property lets you specify the segment of people that start the journey. Segment-based journeys [support segments from outbound marketing as well as segments created in Dynamics 365 Customer Insights - Data](real-time-marketing-segments.md). The journey uses audience data based upon the segment selected. For example, if the journey is started with an outbound marketing segment that contains a segment of **Contacts**, the journey uses Contacts as its Audience data. Similarly, if the journey is started using a Customer Insights - Data segment that is a segment of **Customer Profiles**, the journey uses Customer Profile as its Audience data. Once an audience segment has been selected, all other segments used in the journey must be of the same type (segment from outbound marketing or Customer Insights - Data segment).
- **Exclude this segment**: Members of this segment won't be allowed to start the journey. Specifying an exclusion segment lets you remove anyone from the Audience that starts the journey.
- **Frequency**: Lets you specify whether the journey should repeat.
  - *One time*: One time journeys run only once with a static audience segment. This is useful for scenarios like one-time email blasts that are sent on a specific date to a fixed set of customers.
  - *Ongoing*: Ongoing journeys run only once with a dynamic audience segment. This is useful for scenarios like nurture campaigns where anyone who gets added to the audience segment can start the journey as soon as they're added to the segment.
  - *Repeating*: These journeys repeat based on the time interval specified. Every time the journey repeats, all the members of the audience segment go through the journey. If any new members get added to the segment between the repeat interval, those new members will only go through the journey the next time the journey repeats. This type of journey is useful for scenarios like renewal reminders, where you might want to send people through the journey every time they're up for a renewal.

## Journey end

By default, customers end the journey when they complete all the steps. You can set additional ways for customers to exit the journey by using triggers or segments.

- **Exit when an event occurs**: Customers who perform this trigger will immediately exit the journey no matter where they are in the journey. This provides an easy way to remove customers who perform the trigger from the journey, ensuring that customers don't receive irrelevant messages from your customer journey.
- **Exit by segment**: Customers who are part of this segment will immediately exit the journey. This capability is often referred to as a suppression segment and helps you ensure that members of this segment are suppressed from the customer journey. Exit by segment removes members of that segment from wherever they are in the customer journey. This is notably different from the *exclude by segment* property in journey start, which will only exclude members of the exclusion segment from starting the journey.
- **End on a date**: You can set a date to stop accepting new customers into the journeys. After this end date, customers that have already entered the journey will complete all the steps but no new customers will enter the journey. If you were previously using the legacy, outbound marketing module, this behavior differs in that in the outbound marketing module, customers mid-journey would stop and not complete the remaining steps after the end date.

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

[!INCLUDE [footer-include](./includes/footer-banner.md)]
