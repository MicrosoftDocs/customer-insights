---
title: Requirements for bulk senders
description: Learn about Google and Yahoo requirements for bulk email senders.
ms.date: 05/02/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Requirements for bulk senders

In October 2023, Google and Yahoo announced that they would require email senders to start supporting email authentication, alignment, one-click unsubscribe, and include a visible unsubscribe link in the message body for all promotional emails. Google made it a specific requirement for any sender who sends more than 5,000 emails per day.

Email providers presently utilize the presence of this information to determine spam and reputation scores for email senders, even if it isn't a strict requirement. Effective February 2024, Gmail and Yahoo require the following from bulk email senders:

1. **Authenticate your email**: For Dynamics 365 Customer Insights – Journeys customers, this means that you should review already authenticated domains and finish the [domain authentication](domain-authentication.md) process for new ones.
1. **Make the unsubscribe process easy for your recipients**: Make the unsubscribe link visible and easily accessible for your recipients and make sure you have enabled the [one-click unsubscribe](one-click-unsubscribe.md) for all your emails.
    > [!IMPORTANT]
    > You may not see the unsubscribe button in Gmail or Yahoo if you're sending non-bulk emails or if Gmail or Yahoo thinks your domain is untrustworthy. Review the message headers. The header should include the words "List-Unsubscribe-Post: List-Unsubscribe=One-Click." This means that one-click unsubscribe was set up correctly and it's only up to the mailbox provider to show the button or not.
1. **Ensure that you’re sending a wanted email**: A clear spam rate threshold that senders must stay under is enforced to ensure that Gmail recipients aren’t bombarded with unwanted messages. The spam rate (identified using Google Postmaster Tools) should remain under 0.30% for bulk senders.  
1. **Never use gmail.com or yahoo.com as a "from" address for bulk mailing**: Gmail will begin using a DMARC quarantine enforcement policy. Impersonating Gmail "From:" headers might impact your email delivery.