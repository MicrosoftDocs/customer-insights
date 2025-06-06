---
title: Troubleshooting email engagement drops
description: Learn how to resolve email engagement drops in Dynamics 365 Customer Insights – Journeys. Explore privacy impacts, diagnose issues, and improve your email strategy.
ms.date: 06/05/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:06/05/2025
---

# Troubleshooting email engagement drops

In email marketing, tracking metrics has been the key to understanding and improving campaign effectiveness. Traditionally, the open rate has been a fundamental metric in email marketing. However, the accuracy of open rates is becoming more questionable due to privacy concerns and changes in how email clients handle images. To adapt, it's essential to employ a dual approach, by improving how to measure engagement and applying strategies to improve engagement itself. Engagement metrics in Dynamics 365 Customer Insights – Journeys offer a more complete picture than open rates alone. Diversify engagement metrics by evaluating other indicators such as select-through rates, conversion rates, and return on investment.

## Privacy updates 2025

New privacy regulations like the General Data Protection Regulation (GDPR), California Consumer Privacy Act (CCPA), and Digital Markets Act (DMA) affect email tracking. These regulations reinforce user rights to opt out of tracking.

- **Apple Mail Privacy Protection (MPP)**: This feature shields your privacy by preventing email senders from tracking your activity (such as when an email is opened).
- **Google and Microsoft continuous privacy improvements**: Google and Microsoft are enhancing user privacy with stricter cookie policies and email tracking limitations.
- **Regulatory updates**: The GDPR, CCPA, and DMA are enforcing user rights to opt out of tracking.

## How these changes affect email marketers

Here are some of the ways these privacy regulations affect email marketers:

- **Diminished open rate accuracy**: With Apple and Google privacy features, open rates might be artificially inflated or impossible to track accurately.
- **Reduced select tracking effectiveness**: Stricter privacy settings might prevent accurate, selective tracking in emails.
- **Increased dependence on first party data**: Senders need to rely more on their own data and behavior insights rather than third-party tracking data.
- **Stronger emphasis on content-based marketing**: Regulations require explicit consent for tracking. This limits email service providers' (ESP) ability to gather accurately data.

## How to troubleshoot engagement drops

There are two scenarios for engagement drops: 

- **New customers**: If you've recently onboarded or have a short history with Customer Insights - Journeys, be advised that Customer Insights - Journeys utilizes the latest techniques to filter out nonhuman interactions (NHI). Filtering NHI provides accurate data to our senders, especially with traffic directed to Microsoft 365. If you onboarded and haven't changed your sending domains, audience, or dramatically altered your email templates, but are still experiencing a sudden drop in engagement, then it's likely not an issue with your sending reputation or the platform's efficiency. Rather, it's a more accurate representation of your current engagement rate. We advise you to continue monitoring your engagement rates and watch for any progressive and continuous drops.
- **Existing customers**: If you've been a customer for some time and have noticed a consistent drop in your engagement rates, read the section below.

## Diagnosing an unexpected drop in engagement rates

To diagnose an unexpected drop in engagement rates:

1. **Start by identifying the most affected ISP**: Try to identify the exact timeframe when the engagement rates drop started. It's uncommon for engagement drops to happen all over the board. Typically, only a few ISPs are affected.
1. **Verify sender authentication settings**: Double check that your DNS entries for Sender Policy Framework (SPF), Domain Keys Identified Mail (DKIM), and Domain-based Message Authentication Reporting & Conformance (DMARC) are correctly configured (compare them with the DNS records provided by Customer Insights - Journeys inside the domain authentication panel). If your authentication is broken, deliverability is impacted.
1. **Analyze DMARC reports**: If you enforce DMARC, review DMARC reports to detect unauthorized email senders using your domain. Utilize DMARC Analyzer tools for better interpretation.
1. **Monitor sender reputation**: Your sender reputation provides crucial insights, even if it doesn’t offer all the answers. Utilize tools like Google Postmaster or Yahoo’s Sender Hub to track sender reputation. Any dips, even if temporary, could indicate spam complaints, bounces, or issues with a specific campaign that requires further investigation. For an in-depth guide on Google postmaster, see [Google Postmaster Tools - What it's and how it can help you](google-postmaster.md).
1. **Review email strategy changes**: Assess recent changes in email strategy, including new subscriber lists, template modifications, and automation settings. Unexpected changes can trigger spam filters.
1. **Conduct inbox placement and blocklist tests**: One way to assess your deliverability is through an inbox placement test. This test helps you determine where your emails are landing (inbox or spam). By monitoring your inbox placement rates over time, you can identify when issues arise. These tools aren't perfect because they track a limited number of inboxes, but each mailbox is unique. An email that lands in the spam folder for one mailbox might land in the primary inbox for another. Therefore, it's essential to use these tools with other email metrics to gain a comprehensive understanding of your email deliverability. Unfortunately, we can't recommend any specific third-party provider. However, you can always create test accounts for the top three to five ISP from your audience and use those ISPs to track your placement.
1. **Check your list hygiene**: Maintain list hygiene by avoiding old or inactive lists and ensuring proper opt-in strategies.

    There are numerous factors that could contribute to a drop in engagement. Maintaining a clean list is essential, but even the most diligent senders can encounter issues. For example, you might be sending to an outdated list that should have been archived or you have forgotten about a form that is adding spammy subscribers to your list. Additionally, you possibly didn't implement an opt-in strategy that keeps your list clean, or you uploaded inactive lists or segments that haven't been emailed in a long time.

    It's also important to consider spam complaints based on domain. An issue with spam complaints might begin with an inbox provider that represents only a small percentage of your list. As you gain more readers on that ISP, the issue could become more significant. For more information, see [Best practices for email marketing](get-ready-email-marketing.md).
1. **Review bounce data**: Always review and interpret the raw bounce errors and bounce categories. You can find valuable insights into your sending reputation. Pay attention to ISP-specific reputation-related bounces to determine if there are any spikes in temporary rejections.

    Bounces are a great source of truth; they provide deep insights into the health of your email list. Many senders assume that bounces are only due to full mailboxes or nonexistent addresses, but they can often indicate more serious issues. For example, a bounce might suggest that an ISP blocked the email due to suspected spam. These types of bounces serve as warnings that your sender reputation could be at risk and help you identify which ISPs you need to address.

    Monitoring bounce messages closely is crucial. Inboxes sometimes provide valuable feedback through "bounce codes," such as "blocked due to spam-like content" or "too many complaints from this domain." Ignoring these signals can lead to broader deliverability issues.

    Pay special attention to whether your bounces are concentrated around one or two ISPs. If a significant percentage of your bounces come from a single ISP (for example, Microsoft), it could indicate specific issues with that provider. This might be due to content triggers, reputation problems, or list hygiene issues that are more sensitive to that ISP's spam filters.

    When you regularly review bounce data, especially by ISP, you can better identify and resolve targeted deliverability problems before they spread to other inbox providers.
1. **Audit**: Regularly review automations to ensure relevance.  

**Recommended next steps**: Take a methodical approach to diagnose and fix deliverability issues. Consult with a deliverability specialist for additional insights if necessary.

## When and how the Microsoft Dynamics 365 Customer Insights email deliverability team can assist

Note the following before reaching out to the Microsoft Dynamics 365 Customer Insights email deliverability team for assistance with engagement drop issues:

- As a prerequisite, you must do the analysis outlined above for us to be able to assist you. You can reach out to the deliverability team after you've finished your investigation. The Customer Insights email deliverability team needs you to verify (i) a clear pattern of the engagement drop, (ii) the period when the engagement drops started, and (iii) which ISPs are the most affected.
- The deliverability team can assist mostly in specific cases where you see a spam placement decision on one of your inbox tests or when a recipient is complaining that they received your emails in their spam box. For us to help in this case, we need an email sample of the incident. We require you to either provide full email headers or the email in question saved as an .eml attachment. Any type of email forwarding removes essential headers required for such an investigation.

[!INCLUDE [footer-include](./includes/footer-banner.md)]