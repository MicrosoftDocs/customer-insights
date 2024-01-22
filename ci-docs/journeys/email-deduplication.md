---
title: "Preview: Prevent sending emails to duplicated email addresses"
description: Learn how to deduplicate email addresses in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/26/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Prevent sending emails to duplicated email addresses

> [!IMPORTANT]
> A preview feature is a feature that is not complete, but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.
> 
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won’t be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data or other data that are subject to legal or regulatory compliance requirements.

Email deduplication allows you to prevent sending the same email more than once to the same email address. Email deduplication is a general setting that applies only to segment-based journeys.

Email deduplication is enabled in journeys through the email tile. If deduplication isn't enabled, the email tile will:

- Execute multiple journeys simultaneously on the same email address.  
- Send the same email twice to an email address if the same email is used in two tiles in the customer journey.  
- If a customer journey is set to run "every week/day," for example, the same email will be sent to the same email address once per week/day. 

Email deduplication is disabled by default.

## How to enable email deduplication

1. Go to **Settings** and select **Feature switches**.

2. Enable the **Email deduplication** feature toggle in the "Email sending" section. 

> [!div class="mx-imgBorder"]
> ![Turn on the button for email deduplication.](media/enable-email-deduplication-button.png)

## How to view duplicated email addresses

You can view duplicated email addresses by going to your journey or email **Delivery and interaction details**.

When you view the insights, you'll see all duplicated email addresses in the **blocked** section, under the **Duplicate recipient address** category.

## Known issue

Currently, the deduplication feature doesn't remove the second customer profile from an applicable journey when a duplicated email address is detected.

An example of how this issue might affect you:

Let's say you have a customer who has two (or more) customer profiles (CP1 and CP2) with the same email address and you create a journey flow that says, "If my contact doesn't open an email, send a second email after a period of time."
-	The first email is sent only once (as duplication is detected).
-	If CP1 opens the first email, CP1 won't get the second email.
-	However, CP2 goes to “Not opened” branch and receives the second email.

[!INCLUDE [footer-include](./includes/footer-banner.md)]