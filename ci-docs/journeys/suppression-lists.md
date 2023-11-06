---
title: How Customer Insights - Journeys uses suppression lists 
description: Learn how Customer Insights - Journeys uses suppression lists to protect email sending reputations.
ms.date: 11/06/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# How Dynamics 365 Customer Insights - Journeys uses suppression lists

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

A suppression list is a powerful backend tool that ensures your sending reputation stays healthy. Suppression lists prevent email messages from being sent to harmful recipient addresses.

This article discusses types of harmful address, then details how suppression lists prevent your emails from reaching these addresses.

## Recipient addresses that affect your sending reputation

### Hard-bounced addresses

Sending frequent emails to hard-bounced, invalid email addresses alerts remote spam filters to potential “spammy” behavior. These alerts affect your inbox placement and deliverability results. Sending multiple hard bounces to the same email provider in the same batch may even lead to the email provider completely blocking a sender, which can affect valid recipients.

### Addresses that mark your mail as spam (Feedback Loop/Spam Complaint)

Another type of address that is important to avoid is an email address that has marked your emails as spam, or, in other words, an email address that has generated complaints. Continuing to send emails to a person who has marked your email campaigns as spam - negatively affects your sending reputation and labels you as a spam source. Additionally, emails that generate Spam Complaint/Feedback Loop are generally a message from recipient that he doesn’t want to receive your emails, or even never subscribed to your mailing. 

### Soft-bounced emails 

Sending emails to addresses that soft bounce continuously may also harm your sending reputation. Knowing that email bounces multiple times in a row makes no sense in sending another email again. After five consecutive sending attempts to the same email address that result in soft-bounce will be added to suppression list similarly as a hard-bounce. 

## How the suppression list works

A suppression list is an automated backend tool that protects your sending reputation. The list is divided into three scopes of operation:

When customers start sending emails, the system will automatically check if any of the recipients’ email addresses are already in the suppression list and will block sending emails to these email addresses.

The suppression list works based on the Bounce or Feedback Loop/Spam Complaint type of interactions that our platform receives from the remote recipient mail system and doesn't block legit email addresses itself. The suppression list functions at an email address level, not at a contact or lead level.

The list is divided into three scopes of operation:

### Bounce suppression

Hard bounced email addresses are collected and stored in the suppression list. The hard bounce portion of the suppression list is a per-organization list. The list stores cumulative information from organization sending statistics, making the list broad and reliable.

Soft bounced email addresses may also be listed in this suppression list. After five sequential failed attempts to deliver to the same email address, soft bounce addresses are also being added to suppression. More details on bounce reasons and categories can be found here: [Email bounce categories](email-bounce-categories.md).

To keep the list up-to-date, the backend tool stores information about hard bounced addresses for 180 days (about six months). In rare cases, a hard bounced address may become valid again.

### Spam complaint suppression (Feedback Loop)

The spam complaint suppression list stores information about spam complaints (*feedback loop* reports) that were received regarding a specific organization and prevents such addresses from being sent to. Spam complaints are stored only for the specific organization that received a complaint. Spam complaint listings in the suppression list don't expire automatically.

### Pattern suppression

The pattern suppression is a manual list maintained by the deliverability engineers. It contains domains or email addresses that may not be a good idea to send to. For example, test mailboxes that will never read emails or domains that host temporary or disposable email addresses. Such mailboxes and domains are accessible to anyone and sending to them may harm your sending reputation.

## How to delist email addresses

**What addresses are eligible for delisting**:
1. Soft-bounced email addresses which customer have already fixed the underlying issue causing the bounce. 
1. Hard-bounced email addresses that are of the same domain as customers use as sending domain.
    - For example: From [admin@contoso.com](mailto:admin@contoso.com) To: [John.Doe@contoso.com](mailto:John.Doe@contoso.com)
    - Hard bounced [John.Doe@contoso.com](mailto:John.Doe@contoso.com) address is eligible for delisting because customer owns domain contoso.com and recipient is considered as “internal” and customer can confirm that reason for hard bounce has already been mitigated from their end. 

> [!NOTE]
> Please be informed that email addresses listed due to Feedback Loop/Spam Complaints will never be eligible for delisting due to privacy and data protection regulations. Such emails can be only requested to be removed by the recipient – owner of the email address. Senders cannot get approval to remove such addresses.

**The process of delisting an email address**:

If you find an email address that matches the eligibility criteria from above, you may submit a delist request, by opening a Support Request.

**In the support request, please provide all the required information**:
-	A list of the email addresses in question.
-	Justification as to why you believe each email address was listed by mistake. 
-	You should also provide proof that each email address is valid and can be reached by any other email provider by sending us a screenshot of such an email or forwarding us a copy of email received from the email address in question.
-	Measures taken to prevent same bounces for those addresses (if applicable)

After that, our deliverability team will review the request and determine if the addresses are eligible for removal. 

> [!IMPORTANT]
> If you have a typo in an email address listed in the suppression list, you can correct the email address in the contact or lead by yourself without the need for a support request. Deliverability is not affected by incorrect email addresses in the suppression list. 

> [!NOTE]
> If an email address of contact is removed from a suppression list that is used in a live journey, the changes will take effect in the next iteration of the journey (if the journey is recurring), not in the current one.

## How to prevent email addresses from being listed

To prevent your email addresses from being listed on suppression lists, it's crucial to pay close attention to your email bounce rates. Bounce rates are the number of emails that couldn't be delivered to the recipient's inbox. A [high bounce rate](fix-high-bounce-rate.md) can indicate several issues including invalid email addresses, incorrect email formatting, or email content that triggers spam filters. Addressing these issues can help improve your email deliverability rates and prevent your email addresses from being listed on suppression lists.

Here are some tips to avoid email suppression lists:

1. **Maintain a clean email list**: Regularly clean your email list by removing invalid or inactive email addresses. It's also essential to validate email addresses before adding them to your list to avoid sending emails to fake or spam email addresses.
1. **Send relevant and valuable content**: Deliver emails with relevant and valuable content to your subscribers. This reduces the likelihood of recipients marking your emails as spam.
1. **Test your emails**: Test your emails before sending them to ensure that they're well-formatted and don't trigger spam filters.
1. **Monitor your email deliverability rates**: Keep an eye on your email deliverability rates and investigate any sudden changes. Sudden [drop in deliverability](email-troubleshooting.md) rates could indicate that your emails might have some potential issues.
1. **Follow email [marketing best practices](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/get-ready-email-marketing)**: Adhere to email marketing best practices such as including an unsubscribe link in your emails and ensure that your email content complies with anti-spam laws.

It's the sender's responsibility to maintain a clean email list and ensure that their email campaigns comply with email marketing best practices. By following these tips, you can avoid having your email addresses bounced and listed on suppression lists and maintain a healthy email reputation.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
