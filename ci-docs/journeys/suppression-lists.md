---
title: How Customer Insights - Journeys uses suppression lists for email deliverability
description: Learn how Customer Insights - Journeys uses suppression lists to protect email sending reputations.
ms.date: 12/13/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# How Customer Insights - Journeys uses suppression lists for email deliverability

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

A suppression list is a powerful backend tool that ensures your sending reputation stays healthy. Suppression lists prevent email messages from being sent to harmful recipient addresses.

This article discusses types of harmful address, then details how suppression lists prevent your emails from reaching these addresses.

## Recipient addresses that affect your sending reputation

### Hard-bounced addresses

Sending frequent emails to hard-bounced, invalid email addresses alerts remote spam filters to potential “spammy” behavior. These alerts affect your inbox placement and deliverability results. Sending multiple hard bounces to the same email provider in the same batch may even lead to the email provider completely blocking a sender, which can affect valid recipients.

### Addresses that mark your mail as spam (feedback loop/spam complaint)

Another type of address that's important to avoid is an email address that has marked your emails as spam. Or, in other words, an email address that has generated complaints. Continuing to send emails to a person who has marked your email campaigns as spam negatively affects your sending reputation and labels you as a spam source. Additionally, emails that generate spam complaints/feedback loops are generally to recipients that don't want to receive your emails, or even recipients that never subscribed to your mailing.

### Soft-bounced emails

Sending emails to addresses that soft bounce continuously may also harm your sending reputation. If you know that an email has bounced multiple times in a row, it doesn't make sense to send additional emails. Five consecutive sending attempts to the same email address that result in soft-bounces will result in the email address being added to suppression list similarly to a hard-bounce.

## How the suppression list works

A suppression list is an automated backend tool that protects your sending reputation.

- When customers start sending emails, the system automatically checks if any of the recipients’ email addresses are already in the suppression list and blocks sending emails to these email addresses.
- The suppression list works based on the bounce or feedback loop/spam complaint type of interactions that our platform receives from the remote recipient's mail system and doesn't block legit email addresses. The suppression list functions at an email address level, not at a contact or lead level.

The list is divided into three scopes of operation:

### Bounce suppression

Hard bounced email addresses are collected and stored in the suppression list. The hard bounce portion of the suppression list is a per organization list. The list stores cumulative information from organization sending statistics, making the list broad and reliable.

Soft bounced email addresses may also be listed in this suppression list. After five sequential failed attempts to deliver to the same email address, soft bounce addresses are also added to the suppression list. More details on bounce reasons and categories can be found here: [Email bounce categories](email-bounce-categories.md)

To keep the list up-to-date, the backend tool stores information about hard bounced addresses for 180 days (about six months). In rare cases, a hard bounced address may become valid again.

### Spam complaint suppression (feedback loop)

The spam complaint suppression list stores information about spam complaints (*feedback loop* reports) that were received regarding a specific organization and prevents such addresses from being sent to. Spam complaints are stored only for the specific organization that received a complaint. Spam complaint listings in the suppression list don't expire automatically.

### Pattern suppression

The pattern suppression is a manual list maintained by the deliverability engineers. It contains domains or email addresses that may not be a good idea to send to. For example, test mailboxes that will never read emails or domains that host temporary or disposable email addresses. Such mailboxes and domains are accessible to anyone and sending to them may harm your sending reputation.

## How to delist email addresses

### Addresses eligible for delisting:

1. Soft-bounced email addresses where the underlying issue causing the bounce has been fixed.
1. Hard-bounced email addresses that have the same domain as the sending domain.
    - For example: From [admin@contoso.com](mailto:admin@contoso.com) To: [John.Doe@contoso.com](mailto:John.Doe@contoso.com)
        - The hard bounced [John.Doe@contoso.com](mailto:John.Doe@contoso.com) address is eligible for delisting because the user owns the contoso.com domain and the recipient is considered “internal.” The user can confirm that the reason for the hard bounce has already been mitigated from their end.

Eligible email addresses will have an automatic expiration date that will remove the email address from the suppression list once the date comes, each time the same email address enters the suppression list, the default expiration time increases.

> [!NOTE]
> Email addresses listed due to feedback loop/spam complaints will never be eligible for delisting due to privacy and data protection regulations. Such emails can only be requested to be removed by the recipient owner of the email address. Senders cannot get approval to remove such addresses.

## Removing eligible email addresses (Preview)

To enable the feature:
1. Go to **Settings** and select **Feature switches**.
1. Enable the **Ability to remove email addresses from suppression** in the **Email sending** section.

Once enabled, you can remove eligible email addresses out of the suppression list by navigating to Contacts and then select the communication tab.

> [!div class="mx-imgBorder"]
> ![Use communication tab to select email addresses to remove from suppression lists](media/select-email-addresses-to-remove.png "Use communication tab to select email addresses to remove from suppression lists")

In the communication tab, email addresses will belong to one of the following categories:
1. Not in the suppression list
It means that the email address isn't listed in the suppression list, and you can send emails to this email address.
1. On suppression list
It means that the email address is in the suppression list due to Hard bounce or multiple soft bounces. Email addresses under this category are removable, and you can remove them by clicking on **Remove from suppression list**.
1. Permanently blocked
It means that the email address is in the suppression list due to a permanent issue or due to a direct spam complaint from your recipient. Email addresses under this category aren't removable, as it’s either ineligible to remove them (e.g., spam complaints) or removing them will not solve the problem and they will go again to the suppression once you try to contact them (e.g., invalid mailbox).
More details on bounce reasons and categories can be found here: [Email bounce categories](email-bounce-categories.md).

> [!IMPORTANT]
> Please note that you have a limited number of attempts to remove email addresses, so if you face a big amount of suppression after executing a journey (e.g., 100s or 1000s of suppressions), please open a support request to engage our deliverability teams as this is abnormal behavior and will require further investigation to identify the root cause of the problem.

**In the support request, provide the following required information**:
- A list of the email addresses in question.
- Justification as to why you believe each email address was listed by mistake.
- You should also provide proof that each email address is valid and can be reached by any other email provider by sending a screenshot of such an email or forwarding a copy of an email received from the email address in question.
- Measures taken to prevent same bounces for those addresses (if applicable).

After that, our deliverability team will review the request and determine if the addresses are eligible for removal.

> [!NOTE]
> If you have a typo in an email address listed in the suppression list, correcting the email address in the contact will fix the issue without the need to remove the incorrect email address from the suppression list. Deliverability is not affected by incorrect email addresses in the suppression list.

> [!NOTE]
> If an email address of contact is removed from a suppression list that is used in a live journey, the changes will take effect in the next iteration of the journey (if the journey is recurring), not in the current one.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
