---
title: Add an action within a Journey
description: An overview of possible actions within a journey in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/12/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Add an action within Journey

This page provides an overview of all the possible actions one can do in a Journey.

:::image type="content" source="media/journeys-actions.png" alt-text="An overview of all possible actions in a Journey." lightbox="media/journeys-actions.png":::

## Types of actions

WIthin Customer Inisghts - Journeys, you can do a variety of actions. Some of these actions include sending messages, channel optmiziation, conditon actions, audience splitting, and more.

Main actions are grouped under [messages](#messages), [AI-powered actions](#ai-powered-actions), [conditions](#conditions), [activities](#activities), and [connectors](#connectors). You can see all available Journeys actions under each section below.

### Messages

Customer Insights - Journeys lets you reach customers through common messaging capabilities such as email, text message, push notifications, and more. See common mesaging actions below.

#### Email

You can send personalized emails to capture your customers' attention. For more information, see [send an email](real-time-marketing-email.md)

#### Text message

You can send a text message (SMS) from Dynamics 365 Customer Insights - Journeys by signing up with a provider such as Azure Communication Services, Infobip, LINK Mobility, Telesign, Twilio, or Vibes and configuring Customer Insights - Journeys to work with the provider. For more information, see [send a text message](real-time-marketing-outbound-text-messaging.md)

#### Push notifcations

You can send push notifcations. Push messages allow you to quickly convey offers, messages, or other information directly to users of your app. For more information, see [send a push notification](push-messages.md)

#### Other channel

You can also send other types of channels.

### AI powered actions

You can better cultivate messages to customers in Customer Insights - Journeys through AI-powered actions such as A/B testing and channel optimization. See available AI-powered actions below. 

#### A/B test

A/B tests allow you to measure which channel or content messaging strategy leads to higher success. For more information about using A/B tests, see [A/B tests in Customer Insights - Journeys ](real-time-marketing-ab-tests-in-marketing-journeys.md).

#### Channel optimization

Channel optimization uses AI to find the best channel to reach each individual customer and improve your engagement. To learn more about channel optimization, see [Use AI-driven run-time channel optimization](real-time-marketing-channel-optimization.md).

### Conditions

You can set conditions throughout customers' journeys such as scheduling wait times at specific times, waiting for a specific trigger from a customer, setting up attribute branches, or splitting an audience by number or percentage. See available conditions below. 

#### Wait time

The wait step holds the customer in the journey for the specified wait period.

> [!IMPORTANT]
> The maximum time a wait tile can wait for is 90 days or 12 weeks. The maximum time limitation applies whether selecting an amount of time or setting a fixed date.

You can configure the wait step using the following parameters:

- **A set amount of time**: Customers wait for the specified amount of time (for example, one hour or one day). The time period starts as soon as customers enter the wait step.
- **Until a specific date and time**: Customers wait until the specified date and time. If the date and time are already in the past, customers will immediately proceed to the next step.

#### Wait for a trigger

For trigger-based journeys, customers wait for the date and time specified by a trigger attribute. This configuration is useful for scenarios like appointment reminders, where you can choose to wait one day before the appointment to send a reminder. The date and time information must be included in the trigger that started the journey for the customer.

#### Series

Send a series of messages until certain conditions are met.

#### Attribute branch

The attribute branch lets you branch the journey based on various attributes including:

- **Customer's attributes**: You can branch the journey based on the customer's attributes like address or age. The journey's audience defines which attributes will be shown. For example, if the journey is for Contacts, only attributes for Contacts will be shown.
- **Customer's segment membership**: You can branch the journey based on whether the customer is part of a segment. The journey's audience defines which segments will be shown. For example, only Contacts-based segments will be shown for journeys that are meant for Contacts.
- **Attributes in triggers**: You can branch the journey based on attribute values in triggers. For attribute values to be shown, the trigger must have previously occurred in the journey. Thus, you can only check the attribute values for a trigger that starts a trigger-based journey, or triggers being used in an if/then branch.

The attribute branch checks for attribute values the moment a customer enters this step. For example, when a customer enters the attribute branch step, the segment membership condition will check whether the customer is part of the specified segment at that instant.

#### Audience split

The audience split tile allows you to divide your audience to give a unique set of experiences to random sets of the audience. You can split by percentage or split by number. Learn more: [Preview: Split your audience into groups](real-time-marketing-split-audience.md)

### Activities

You can create activities for customers at specific instances in a journey such as creating and assigning a phone call or task activity. See available activities below. 

#### Phone call

You can create and assign a phone call for customers to sales.

#### Task

You can create and assign a task activity for customers.

### Connectors

Connectors provide additional features beyond actions above. For example, you can activate a custom trigger where additional journeys or [Power Automate flows](/power-automate) connected to a custom event will be triggered when a customer does a specific action.

#### Activate a custom trigger

Triggering a custom event allows you to use activate a custom event at any point in the customer journey. Additional journeys or [Power Automate flows](/power-automate) connected to the custom event will be triggered immediately when a customer reaches the tile. This includes custom triggers used in exit criteria, goals, and if/then branches for journeys.

When using a custom trigger, you can choose which data to send as part of the trigger. You can choose customer profile data (for instance, attributes of the target audience such as contacts, leads, etc.) and data from other triggers used in the journey (for instance, attributes of the trigger that starts the journey).

For example, a loan application journey could have various steps that require a human agent’s approval. By creating a separate customer journey or Power Automate Flow for loan exception approval, you can trigger it from various points in the loan application journeys where exceptions can occur. The data you send with the trigger can be used to populate dynamic content or as inputs to other Flow actions.

To learn more about triggering a custom event, see [Preview: Trigger an action outside of a journey](real-time-marketing-custom-actions.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]