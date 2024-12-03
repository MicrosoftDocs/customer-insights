---
title: Add an action in a journey
description: An overview of possible actions you can do in a journey in Dynamics 365 Customer Insights - Journeys.
ms.date: 11/28/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Add an action in journey

This page provides an overview of all the possible actions you can do in a journey. 

To get to the Add an action dashboard, go to Customer Insights - Journeys > **Journeys** and select your desired journey or create a new journey by selecting **+New journey**. To add an action once in your journey, select **+Add an action** under the Journey start node.

## Types of actions

Within real-time journeys, you can launch various actions. Some of these actions include sending messages, channel optimization, condition actions, audience splitting, and more.

:::image type="content" source="media/journeys-actions.png" alt-text="An overview of all possible actions in a journey." lightbox="media/journeys-actions.png":::

The main actions are grouped under [messages](#messages), [AI-powered actions](#ai-powered-actions), [conditions](#conditions), [activities](#activities), and [connectors](#connectors). You can see all available actions under each section below.

### Messages

Customer Insights - Journeys lets you reach customers through common messaging capabilities such as email, text message, push notifications, and more. See common messaging actions below.

##### Email

You can send personalized emails to capture your customers' attention. For more information, see [send an email](real-time-marketing-email.md).

##### Text message

You can send a text message (SMS) from Customer Insights - Journeys by signing up with a provider such as Azure Communication Services, Infobip, LINK Mobility, Telesign, Twilio, or Vibes and configuring Customer Insights - Journeys to work with the provider. For more information, see [send a text message](real-time-marketing-outbound-text-messaging.md).

##### Push notifications

You can send push notifications. Push messages allow you to quickly convey offers, messages, or other information directly to users of your app. For more information, see [send a push notification](push-messages.md).

##### Other channel

You can also send messages through custom channels to capture customers' attention. For more information, see [create custom channels](real-time-marketing-create-custom-channels.md).

### AI-powered actions

You can cultivate customer-specific messages in Customer Insights - Journeys through AI-powered actions such as A/B testing and channel optimization.

##### A/B test

A/B tests allow you to measure which channel or content messaging strategy leads to higher success. For more information about using A/B tests, see [A/B tests in Customer Insights - Journeys](real-time-marketing-ab-tests-in-marketing-journeys.md).

##### Channel optimization

Channel optimization uses AI to find the best channel to reach each individual customer and improve your engagement. To learn more about channel optimization, see [Use AI-driven run-time channel optimization](real-time-marketing-channel-optimization.md).

### Conditions

You can set conditions throughout customers' journeys such as scheduling wait times at specific times, waiting for a specific trigger from a customer, setting up attribute branches, or splitting an audience by number or percentage. See available conditions below. 

##### Wait time

The wait step holds the customer in the journey for the specified wait period.

> [!IMPORTANT]
> The maximum time a wait tile can wait for is 90 days or 12 weeks. The maximum time limitation applies whether selecting an amount of time or setting a fixed date.

You can configure the wait step using the following parameters:

- **A set amount of time**: Customers wait for the specified amount of time (for example, one hour or one day). The time period starts as soon as customers enter the wait step.
- **Until a specific date and time**: Customers wait until the specified date and time. If the date and time are already in the past, customers will immediately proceed to the next step.

##### Wait for a trigger

For trigger-based journeys, customers wait for the date and time specified by a trigger attribute. This configuration is useful for scenarios like appointment reminders, where you can choose to wait one day before the appointment to send a reminder. The date and time information must be included in the trigger that started the journey for the customer.

##### Series

Send a series of messages until certain conditions are met.

#### Branching the customer journey 

There are two ways to create a branch in a journey:

- Branch based on whether a certain action was taken or not. A common example is branching based on whether or not the customer opened the last email that was sent. This type of branching is achieved by the [Wait for trigger](#wait-for-trigger-branch) tile.  

- Branch based on current information such as customer’s demographic (for example, gender) or other related information (for example, loyalty program tier). This type of branching is achieved by the [Attribute branch](#attribute-branch).  

The key differences between these two branching methods are: 

Wait for trigger branch supports specifying a duration for how long to wait until the desired action is taken. Wait for trigger branching also supports simple 2-way branching. This is why the tile is also referred to as an “if/then branch”. 

Attribute branch does not have a provision for waiting. Attribute branches use the data available at the time of execution and allows for multiple way branching.

##### Wait for trigger branch

The "wait for trigger" branch lets you branch the customer journey based on customer actions such as opening an email or completing a purchase. The "wait for trigger" branch waits for the customer to perform the trigger within the time limit specified. If the customer performs the trigger, they immediately proceed down the yes branch. If the customer doesn't perform the trigger within the time limit specified, they proceed down the no branch after the time limit has passed.

For example, you can configure the "wait for trigger" branch to wait for the *Email opened* event on a previously sent email within a specific time period (such as one day). The customer opens the email within that period. The customer immediately proceeds down the yes branch. If the customer doesn't open the email within that period, they proceed down the no branch after the period is over.

##### Wait for segment membership

The wait for segment membership feature allows for more complex set of actions to take place beyond a single trigger. For example, you may want to create a branch based on how much customer spent through multiple transactions in a specific period. In this scenario, rather than wait for a specific trigger, you can simply define a dynamic segment such as 'big purchaser' and wait for the customer to become a member of that segment.

> [!IMPORTANT]
> This feature is a preview and won't be available until December 9th, 2024. A preview feature is a feature that is not complete, but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.
> 
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won’t be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data or other data that are subject to legal or regulatory compliance requirements.

##### Attribute branch

An attribute branch lets you branch the journey based on various attributes including:

- **Customer's attributes**: You can branch the journey based on the customer's attributes like address or age. The journey's audience defines which attributes are shown. For example, if the journey is for contacts, only attributes for contacts are shown.
- **Customer's segment membership**: You can branch the journey based on whether the customer is part of a segment. The journey's audience defines which segments are shown. For example, only contacts-based segments are shown for journeys that are meant for contacts.
- **Attributes in triggers**: You can branch the journey based on attribute values in triggers. For attribute values to be shown, the trigger must have previously occurred in the journey. Thus, you can only check the attribute values for a trigger that starts a trigger-based journey, or triggers being used in an "wait for trigger" branch.

The attribute branch checks for attribute values the moment a customer enters this step. For example, when a customer enters the attribute branch step, the segment membership condition checks whether the customer is part of the specified segment at that instant.

Attribute branch supports multi-way branching. For example, if you have 'customer spend' as an attribute, you can create different branches for different ranges of spending. For more details, see [Personalize journey variations using multiple journey branches](real-time-marketing-multiple-branches.md).

##### Audience split

The audience split tile allows you to divide your audience to give a unique set of experiences to random portions of the audience. You can split by percentage or split by number. Learn more: [Preview: Split your audience into groups](real-time-marketing-split-audience.md).

### Activities

You can create activities for customers at specific instances in a journey such as creating and assigning a phone call or task activity. See available activities below. 

##### Phone call

You can create and assign a phone call for customers to sales.

##### Task

You can create and assign a task activity for customers.

### Connectors

Connectors provide additional features beyond actions above. For example, you can activate a custom trigger where additional journeys or [Power Automate flows](/power-automate) connected to a custom event are triggered when a customer does a specific action.

##### Activate a custom trigger

Triggering a custom event allows you to use activate a custom event at any point in the customer journey. Additional journeys or [Power Automate flows](/power-automate) connected to the custom event are triggered immediately when a customer reaches the tile. This includes custom triggers used in exit criteria, goals, and "wait for trigger" branches for journeys.

When using a custom trigger, you can choose which data to send as part of the trigger. You can choose customer profile data (for instance, attributes of the target audience such as contacts, leads, etc.) or data from other triggers used in the journey (for instance, attributes of the trigger that starts the journey).

For example, a loan application journey could have various steps that require a human agent’s approval. By creating a separate customer journey or Power Automate Flow for loan exception approval, you can trigger it from various points in the loan application journeys where exceptions can occur. The data you send with the trigger can be used to populate dynamic content or as inputs to other Flow actions.

To learn more about triggering a custom event, see [Preview: Trigger an action outside of a journey](real-time-marketing-custom-actions.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
