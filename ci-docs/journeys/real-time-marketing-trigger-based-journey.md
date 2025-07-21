---
title: Create a trigger-based journey
description: Learn how to build a trigger-based journey in Dynamics 365 Customer Insights. Set up real-time responses to customer actions and drive engagement.
ms.date: 07/11/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:07/11/2025
---

# Create a trigger-based journey

Trigger-based customer journeys let you react to customer actions in real time. You can trigger journeys based on real-world interactions, like walking into a store and connecting to Wi-Fi, or virtual interactions, like visiting a shopping website. Because journeys are real time, you respond to customers and turn their interest into a sale.

Trigger-based journeys work best for triggers that your customers start, like selecting a website link, submitting a form, visiting a store, or making a purchase. These events usually happen at different times, not all at once. For business events, like when a billing cycle is ready or lottery results are available, use a segment-based journey. Make sure there's an attribute on the contact or lead that updates so they enter the segment and then the journey. If you use a trigger to start a journey for a business event, it raises the trigger for every contact or lead and likely goes over the fair use policy for triggers.

If you need to start a journey for a large group of customers based on a business trigger, see [Targeting volume communications based on contacts' products or services](https://community.dynamics.com/blogs/post/?postid=2928a2b3-684b-f011-877a-7c1e52027a5f) for best practices. 

## Create a trigger-based journey for abandoned cart reminders

This article shows how to create a personalized, multichannel, trigger-based journey that brings prospective buyers with abandoned carts back to your website to finish their purchase.  

## Prerequisites

### Create custom triggers

- Work with your website team to capture the customer's *Abandoned cart* and *Purchase completed* actions as custom triggers. For more information on creating custom events, see [Customer Insights - Journeys triggers](real-time-marketing-triggers.md).
- Raise the *Abandoned cart* trigger whenever a customer adds products to the cart but doesn’t finish the purchase.
- Raise the *Purchase completed* trigger whenever a customer finishes their purchase.

### Create email, text, and push notifications

Use three touchpoints across different channels to remind customers to finish their purchase:

- **Initial email reminder**: When a customer abandons a cart, they get an email to remind them to finish their purchase.
- **Second text reminder**: If the customer doesn't open their email one day after the initial reminder, send a text message.
- **Final push notification**: If the customer doesn't finish their purchase one day after the second reminder, send a final push notification.

Build the journey while the content is in the **Draft** state. To publish and go live with the journey, the content must be in the **Ready to send** state.

## Set the journey start

When you create a trigger-based journey, specify the following properties to set how customers start the journey:

- **Choose the type of journey**: You can select whether you want to create a trigger-based journey that responds to a customer action, or a segment-based journey that reaches out to a specific audience. Here, we want to create a trigger-based journey.
- **Choose the trigger**: Select the trigger that starts the journey. To start the journey when a customer abandons their cart, select the *Abandoned cart* event.

> [!div class="mx-imgBorder"]
> ![Screenshot of the Create a trigger-based journey page showing options to select the journey type and trigger event.](media/real-time-marketing-trigger-based-journey.png "Screenshot of the Create a trigger-based journey page showing options to select the journey type and trigger event.")

Find more options for starting the journey in the journey task pane. For details, see [Add an action in a journey](add-action.md).

## Add journey conditions

Personalize the trigger by adding data attributes (conditions) from the trigger’s core entity or table, or from entities or tables directly related to those attributes.

To add attributes, select a trigger, then select the **+Add condition** button. Add up to 29 attributes to the trigger. This lets you create highly personalized journeys using out-of-the-box triggers, without creating a custom trigger.

In the abandoned cart journey, add a condition to trigger a reminder only when the cart value exceeds $50. To do this, select **+Add condition**, then select the "Cart Total" attribute from the Cart Abandoned trigger. Set the operator to ">" and the value to "50."

> [!div class="mx-imgBorder"]
> ![Screenshot of adding a trigger condition in the real-time marketing interface.](media/real-time-marketing-trigger-attribute.png "Add a trigger condition screenshot")

To learn how to add conditions based on nested attributes in triggers, see [Personalize triggers using conditions](real-time-marketing-personalize-triggers.md).

## Set the journey goal

The goal for this journey is to drive a purchase. Use the *Purchase completed* trigger to track when users meet this goal. Set the **Amount of people needed for this goal** to 50 percent to indicate that you want at least 50 percent of customers who abandon carts and are targeted by this journey to complete the purchase.

> [!div class="mx-imgBorder"]
> ![Screenshot of the Set the journey goal pane showing the Amount of people needed for this goal field set to 50 percent.](media/real-time-marketing-trigger-based-journey-goal.png "Set the journey goal screenshot")

## Set the journey exit

By default, customers leave the journey when they’ve completed all the steps. However, you can set additional journey exits using triggers. Setting the journey exit to a trigger provides an easy way to remove customers who perform the trigger from the journey, ensuring that customers don’t receive irrelevant messages from your customer journey. For this journey, you want to make sure to only send reminder messages if customers haven’t yet completed their purchase. By setting the journey exit to the *Purchase completed* event, you can ensure that the moment any customer completes the purchase, they exit the journey and no longer receive the reminder messages.

> [!div class="mx-imgBorder"]
> ![Screenshot of the journey exit settings showing how to set a trigger-based exit for the customer journey.](media/real-time-marketing-trigger-based-journey-exit.png "Set journey exit screenshot")

## Add the abandoned cart reminders

On the journey canvas, select the plus sign (**+**) to add the abandoned cart reminders to your journey.

1. **Send an email**: Select the *Initial email reminder* email to send. For the **Send to** field, select the attribute that has the email address to send the email to.
1. **Add an if/then branch**: In the **Branch off this** field, select the previous email (*Initial email reminder*). Set the reminder to **Wait for** the *Email opened* trigger. Set the time limit to *1 day*. This if/then branch checks if the customer opens the *Initial email reminder* email within one day after it's sent. If the customer opens the email within one day, they go down the **Yes** branch. If the customer doesn't open the email one day after it's sent, they go down the **No** branch.
1. **Send a text message**: Under the **No** branch, send the *Second text reminder*. For the **Send to** field, select the attribute that has the phone number to send the text message to. This text message is sent only if the customer doesn't open the first email message within a day. Because the if/then branch already has a time limit of one day, the text message is sent one day after the email is sent.
1. **Add a wait**: Add a wait and select **A set amount of time**. Set the duration to **1 day**. This step ensures that customers wait for one day after the text message before moving to the next step.
1. **Send a push notification**: As the final step, send the *Final push notification* reminder.

> [!div class="mx-imgBorder"]
> ![Screenshot of the abandoned cart journey showing the sequence of email, if/then branch, text message, wait, and push notification steps.](media/real-time-marketing-trigger-based-abandoned-cart-journey.png "Abandoned cart journey screenshot")

## Publish the journey

After you add all the steps to the journey canvas, the journey is ready to go live and message real customers. Before you publish the journey, make sure all related content (email, text messages, and push notifications) is in the **Ready to send** state. Also, publish any triggers and integrate their code. To learn how to make changes to the journey after you publish it, see [Edit a live journey in Customer Insights - Journeys](real-time-marketing-edit-journey.md).

After you publish the journey, go to the journey [analytics page](real-time-marketing-analytics.md) to see how it's performing.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
