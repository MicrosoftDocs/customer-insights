---
title: Requirements for bulk senders
description: Learn the requirements for bulk senders on Gmail and Yahoo, including authentication, one-click unsubscribe, and spam rates. Review your email setup.
ms.date: 11/09/2026
ms.topic: article
author: udag
ms.author: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Requirements for bulk senders

In October 2023, Google and Yahoo announced requirements for bulk senders that cover email authentication, alignment, one-click unsubscribe, and a visible unsubscribe link in promotional emails. Review these requirements to help protect email delivery, especially if you send more than 5,000 emails per day, which is Google's bulk-sender threshold.

Email providers currently use the presence of this information to determine spam and reputation scores for email senders, even if it isn't a strict requirement. Effective February 2024, Gmail and Yahoo require the following from bulk email senders:

1. **Authenticate your email**: For Dynamics 365 Customer Insights – Journeys customers, this requirement means that you should review already authenticated domains and finish the [domain authentication](domain-authentication.md) process for new ones.
1. **Make the unsubscribe process easy for your recipients**: Make the unsubscribe link visible and easily accessible for your recipients. Ensure you enable the [one-click unsubscribe](one-click-unsubscribe.md) for all your emails.
    > [!IMPORTANT]
    > You might not see the unsubscribe button in Gmail or Yahoo if you're sending non-bulk emails or if Gmail or Yahoo thinks your domain is untrustworthy. Review the message headers. The header should include the words "List-Unsubscribe-Post: List-Unsubscribe=One-Click." This wording means that one-click unsubscribe is set up correctly. It's only up to the mailbox provider to show the button or not.
1. **Ensure that you’re sending a wanted email**: To ensure that Gmail recipients aren't bombarded with unwanted messages, Gmail enforces a clear spam rate threshold that senders must stay under. The spam rate (identified using Google Postmaster Tools) should remain under 0.30% for bulk senders.  
1. **Never use gmail.com or yahoo.com as a "from" address for bulk mailing**: Gmail will begin using a DMARC quarantine enforcement policy. Impersonating Gmail "From:" headers might impact your email delivery.  