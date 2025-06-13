---
title: Tailor follow-up strategies by leveraging multiple customer actions at once (preview)
description: Learn how to tailor follow-up strategies by leveraging multiple customer actions in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/12/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Tailor follow-up strategies by leveraging multiple customer actions at once (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

The multi-interaction branching feature in Customer Insights - Journeys lets marketers set up journey branches based on different customer responses from a single decision node in a journey. Whether an email *bounces*, is *blocked*, or a link is *selected*, multi-interaction branching lets you design more nuanced and intelligent journeys. Marketers can personalize customer experiences by evaluating several interaction outcomes at once through a single branching condition in a journey.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## What are marketing interactions? 

:::image type="content" source="media/multi-interaction-branching.png" alt-text="Screenshot of configuring journey branches based on multiple customer responses to marketing messages." lightbox="media/multi-interaction-branching.png":::

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## What are marketing interactions

Marketing interactions are signals generated when customers engage with outbound channels like email, SMS, push notifications, and voice calls. Signals like email opened, text message reply received, or push notification clicked show how customers engage with your communication. These interactions help you make quick decisions, respond dynamically based on behavior and intent, and optimize the customer journey.

## Benefits of multi-interaction branching

This capability makes journey design more flexible and sophisticated because a single branching node can evaluate and route customers based on multiple interaction conditions. It reduces design complexity and creates new opportunities for contextual messaging strategies tailored to real customer behavior.

Key benefits include:

* **Greater personalization**: Lets you make more sophisticated decisions at key moments of interaction
* **Simplified journey design**: Reduces the need for multiple branching nodes
* **Improved engagement and deliverability**: Improves follow-up messaging based on specific interaction outcomes

## Example use cases – Contoso Coffee 

Contoso Coffee, a premium coffee chain, uses multi-interaction branching to optimize how customers move through their journeys based on real-time engagement across multiple channels. For example, in an email campaign promoting a new espresso subscription, Contoso sets up a journey that reacts differently depending on how customers engage. If the email is delivered and opened, the customer gets a follow-up email with a personalized discount. If the email is delivered but not opened within 24 hours, a push notification goes out to re-engage interest. If the email bounces, the customer is flagged for data cleansing. If blocked, the customer is added to a suppression list for compliance review. 

In another scenario, Contoso Coffee starts an SMS-based feedback journey after a customer visit. If the customer replies to the text message, a "Thank You" message and next-visit coupon go out. If the customer selects the feedback link but doesn't finish the survey, a reminder email goes out. For customers who don't engage, a push notification goes out 48 hours later to encourage participation. 

When launching mobile push notifications for time-sensitive promotions like a weekend buy-one-get-one-free offer, Contoso Coffee uses branching to drive engagement. If a customer opens the notification and selects the offer link, they're directed to a confirmation page and logged as claimed the offer. If the notification is only opened, a banner shows in-app during the next session. Customers who don't take action get a follow-up SMS with the same promotional details. 

Contoso also runs reactivation campaigns using automated voice calls. If the call goes through and is answered, the customer hears a personalized message and can choose to speak with support. If the call doesn't go through because of technical issues, the contact goes into a manual call queue. If the call is blocked, the customer is excluded from future voice campaigns and flagged for channel preference updates. 

These examples show how Contoso Coffee uses multi-interaction branching to deliver personalized, responsive customer experiences across different touchpoints. This approach drives higher engagement, efficiency, and customer satisfaction.

> [!Note]
> You might notice that not all [interaction triggers][real-time-marketing-triggers.md#interaction-triggers] show up when you use this feature to make journey branching decisions. This is a known issue that can affect some orgs. For a quick fix, raise a support ticket.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
