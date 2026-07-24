---
title: Fix a high email bounce rate
description: Learn the acceptable email bounce rate threshold and how to diagnose and fix a high bounce rate in Customer Insights - Journeys.
ms.date: 07/23/2026
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Fix a high email bounce rate

If you receive a notification that a past campaign's bounce rate surpassed the acceptable bounce limit, your email campaign requires special attention.

## What is the email bounce rate?

In email marketing, the bounce rate refers to the percentage of emails in your contact list that didn't receive an email message because it was returned by the recipient server. The bounce rate is calculated by dividing the number of bounced emails by the number of sent emails and multiplying by 100.

In most cases, an acceptable bounce rate shouldn't be higher than 2%. In Dynamics 365 Customer Insights - Journeys, the acceptable bounce rate threshold is up to 8%. For more information, see [Email policies and suspension standards](email-policies.md).

## What does a high bounce rate mean for you as a sender?

Generally, a spike in bounces can lead to potential issues for your email sending reputation. That’s why it's important to keep your bounce rates at a low level.

The most common reasons for an increased bounce rate are the following reasons:

- **Problems with a contact list (hard bounces)**: Old, invalid, or inactive contacts in the list, a list that you purchased from a third party, or a broken list that has invalid contact data.
- **Reputation/blocklist issues**: Bounces due to sender IP or domain reputation, spam content decisions from the recipient side.
- **Temporary or technical issues on the recipient side**: A full recipient mailbox, recipient server failures, or networking issues.

You can check out a detailed explanation of all bounce categories in the [email bounce categories](email-bounce-categories.md) article.

## How can you lower your bounce rates?

First and foremost, keep your contact data clean and up to date. Regularly clean your segments of old and invalid contacts that already hard bounced. It's also a good idea to monitor open and click rates for your contacts. If a contact doesn't open or interact with your emails for a long time, exclude the contact from sending.

Second, keep your email flow consistent. Don't change the frequency, volume, content, subjects, or media assets of your campaigns often, since spam filters might decide that your email is exhibiting spammy behavior.

From a deliverability perspective, sending emails regularly to approximately the same segment size is better than sending once a month to one large segment.

Finally, always monitor your delivery results. Check your bounce rates and engagement rates (opens and clicks) regularly so that you don't miss any potential slow growth of bounces across your campaigns. Monitoring these rates helps you prevent damage to your sending reputation and keep your contact data up to date.

Bounce rate is a key indicator of your contact list health. There will always be a few bounces in every campaign. It is expected and normal. But preventing a large number of bounces is key to maintaining your sender reputation and is achievable with consistent monitoring.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
