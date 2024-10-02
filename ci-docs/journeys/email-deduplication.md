---
title: "Preview: Prevent sending emails to duplicated email addresses"
description: Learn how to deduplicate email addresses in Dynamics 365 Customer Insights - Journeys.
ms.date: 02/01/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Preview: Prevent sending emails to duplicated email addresses

> [!IMPORTANT]
> A preview feature is a feature that is not complete, but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.
> 
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won’t be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data or other data that are subject to legal or regulatory compliance requirements.

Email deduplication allows you to avoid sending duplicate emails when multiple contacts share the same email address. Email deduplication is a general setting that applies only to segment-based journeys and is disabled by default.

When email deduplication is enabled, the journey checks the email addresses of the contacts in the segment (once they reach the email tile) and only send one email to each unique address. For example, if three contacts have the same email address, only one of them receives the email. The other two are reported as **blocked** under the **Duplicate recipient address** category in the **Delivery and interaction details**.

When email deduplication is disabled (default), the journey sends the email to every contact in the segment, even if they share an email address.

## How to enable email deduplication

1. Go to **Settings** and select **Feature switches**.

2. Enable the **Email deduplication** feature toggle in the "Email sending" section.

> [!div class="mx-imgBorder"]
> ![Turn on the button for email deduplication.](media/enable-email-deduplication-button.png)

## How to view duplicated email addresses

You can view duplicated email addresses by going to your journey or email **Delivery and interaction details**.

When you view the insights, you see all duplicated email addresses in the **blocked** section under the **Duplicate recipient address** category.

## Known issues

Deduplication prevents sending an email more than once to the same email address, but it doesn't exclude other contacts sharing the same email from the journey logic.

For example, if two contacts share the same email address and the journey is set to "send a follow-up email if the contact doesn't open the first email":

- The initial email is sent to only one of the contacts (because of deduplication).
- If the contact who received the email opens it, the contact doesn't receive the follow-up email.
- However, the other contact sharing the same email address goes into the "not opened" branch and gets the follow-up email.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
