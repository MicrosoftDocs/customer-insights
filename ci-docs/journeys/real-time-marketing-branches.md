---
title: When to use attribute versus if/then branches
description: Compare attribute versus if/then branches in Customer Insights - Journeys to choose the right path for dates, triggers, and customer actions. Explore examples.
ms.date: 11/03/2026
ms.topic: article
author: udag
ms.author: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# When to use attribute versus if/then branches

Attribute versus if/then branches in Customer Insights - Journeys help you route customers based on profile data or actions. Learn when to use each branch for dates, triggers, and follow-up emails.

A general rule of thumb is that attribute branches are best for things that already happened (attributes in your customer’s profile). If/then branches, on the other hand, evaluate based on a desired customer behavior occurring or not.

Here are some use cases:

## Case 1: Attribute branching for dates and special events

Let’s assume you want to branch your audience based on a specific contact profile attribute like a birthday. Use the relative date format to add contacts to a journey on a yearly cycle.

The relative date format evaluates birthdays when the customer reaches this point of the journey, regardless of when the journey goes live. Assume the journey goes live on February 1 and John Doe was born on March 1 (one month from February 1). If John goes through the attribute branch on March 1, they go through the **yes** branch. But if John reaches the attribute branch before or after March 1, or the journey goes live after March 1, John is always directed to the **no** branch.

:::image type="content" source="media/real-time-marketing-branches-birthday.png" alt-text="Screenshot of an attribute branch configured with the relative date format for a birthday attribute." lightbox="media/real-time-marketing-branches-birthday.png":::

Use the partial date format for special events that occur annually, such as an anniversary.

:::image type="content" source="media/real-time-marketing-branches-partial.png" alt-text="Screenshot of an attribute branch configured with the partial date format for a recurring annual event." lightbox="media/real-time-marketing-branches-partial.png":::

Actual dates add contacts to a journey on a specific day, month, and year, so you can’t use them with recurring events.

## Case 2: Attribute branch for triggers

Now, assume you're creating an onboarding journey. You might start the journey with an event when an opportunity is created and send two different messages when the opportunity is won versus when it’s still open.

Use an attribute branch to check the attribute values for a trigger that starts a trigger-based journey.

The attribute picker doesn't show custom triggers used in **Wait for trigger** tiles, even on the **Yes** path.

:::image type="content" source="media/real-time-marketing-branches-trigger.png" alt-text="Screenshot of an attribute branch checking attribute values from a trigger that starts a journey." lightbox="media/real-time-marketing-branches-trigger.png":::

## Case 3: If/then branch to follow up with your customers

Finally, assume you're creating a journey for customers that raise a support ticket. You want to send a survey email when the ticket is closed asking about their experience.

Use an if/then branch to wait for a survey email open event. If you set the limit for one day, the if/then branch waits for the customer to open the email within that one day. If the customer opens the email, they funnel down the **yes** branch, otherwise they go in the **no** branch.

:::image type="content" source="media/real-time-marketing-branches-if-then.png" alt-text="Screenshot of an if/then branch waiting one day for a customer to open a survey email." lightbox="media/real-time-marketing-branches-if-then.png":::
