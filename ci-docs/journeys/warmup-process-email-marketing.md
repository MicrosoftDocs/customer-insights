---
title: Warm-up process for marketing senders
description: Plan a domain warm-up for marketing email senders in Dynamics 365 Customer Insights - Journeys. Follow the timeline to build sender reputation.
ms.date: 11/09/2026
ms.topic: article
author: udag
ms.author: udag
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Domain warm-up process for marketing email senders

Domain warm-up gradually increases email volume from a new domain over several days or weeks. This article explains how to plan marketing sends to build a positive sending reputation with mailbox providers.

The initial warm-up process is important for every sender. Warming up your domain together with your email service provider's IP addresses is crucial, whether you use a brand new domain (with no reputation) or an already in use domain (with good reputation) for your email campaigns. Warm-up is especially critical for senders who plan to use brand new domains and send large volumes of emails in their customer journeys (up to 500,000 emails per day or customer journey).

## Domain warm-up timeline and audience selection

Mailbox providers view email from a new domain as suspicious until the new address establishes a positive sending reputation. Achieving maximum deliverability takes four to eight weeks, depending on the targeted volume and engagement. Warming could take longer if mailbox providers don't perceive that email from the new domain is "wanted" by the recipient. For example, the mailbox provider might determine that an email isn't wanted if the recipient didn't explicitly sign up for the mailing list. Certain mailbox providers limit senders to thresholds (the number of messages delivered per day) until they establish a reputation.

You should start the warm-up process with your best performing messages – those sent to highly engaged recipients. Focus on warming up with your most engaged subscribers, then add older segments as you progress. Avoid tipping your reputation from good to bad by only adding older segments to the engaged segments in chunks of 15 percent of your existing volume. The goal during the warm-up process is to send to subscribers who are the least likely to complain and bounce. These subscribers comprise the most recent opt-ins and regular opens and clickers.

During the warm-up phase, the more consistent you are with volume, frequency, complaint, and bounce levels, the faster you establish a positive sending reputation. If you send infrequently (anything less than weekly), it takes longer to build a positive sender reputation.

## Domain warm-up plan for marketing email senders

### Choose subscribers by recent engagement
- During weeks 1-2, send to your most active subscribers – those who opened or clicked in the past 30 days.
- During weeks 3-4, expand your reach to subscribers who opened or clicked in the past 60 days.
- During the first six weeks, don't send to subscribers who didn't open or click in the past 90 days.

### Delivery issues during domain warm-up
As the warm-up process begins, expect some bulk (mailbox providers identifying marketing emails as spam) and blocking. The key is to stick with the plan. The following sections provide details of what you can expect and actions to take.
- **Bulk** at Yahoo, AOL, and Gmail typically clears up after a few sends with solid positive metrics, but it can take time to get inbox delivery. The key is to keep sending it to engaged subscribers.
- **Delays** at AOL, Microsoft, and Comcast. The delays (421 bounces) retry for 72 hours, and if not delivered, they bounce as a 5XX with the original 421 error in the bounce record. There's no need to be concerned as long as the emails are delivered. If emails are timed out in significant numbers, reduce your volumes to the mailbox provider by tightening your engagement window (the time since a recipient last interacted with one of your emails).
- Possible **blocking** by mailbox providers can occur if the list isn't engaged enough. The key is to segment carefully and tighten up engagement. Again, the key is to keep sending.

### Why is the warm-up process important?

| No warm-up: | Warm-up: |
|---|---|
| Mailbox providers see volume spikes | Mailbox providers see a gradual build in volume |
| Unknown senders | A good reputation develops over time |
| Blocks, filtering,   and rate limiting occur | Blocks, filtering, and rate limiting rarely occur (only occurs when engagement rates are low and complaint rates are high) |

Warm-up builds your sender reputation. Sender reputation is how mailbox providers view you and your mail.
- Email reputation controls access to the inbox
    - Bad reputation = spam folder or blocks
    - Good reputation = inbox
- Reputation can affect the domain or IP address and is based on:
    - Spam complaints
    - Invalid email addresses (hard bounces)
    - Spam trap hits
    - Authentication (SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail), DMARC (Domain-based Message Authentication, Reporting, and Conformance))
    - Third-party block listing
    - Engagement

| Positive effects on your reputation: | Negative effects on your reputation: |
|---|---|
| Opens | Poor or insufficient permission |
| Clicks | High recipient complaints (report as spam) |
| Authentication (DKIM, SPF, DMARC) | Poor list quality/hygiene (bad email addresses) |
|   | IP address and domain block listing |
|   | Spam trap hits |
|   | Large spikes in volume |

## Factors that affect sender reputation

Key takeaways:

- Opt-ins are the most important factor.
- If people don't want your mail, your reputation suffers.
- Mailbox providers and metrics are the judge and jury when it comes to getting delivered to the inbox.
- You can't transfer your reputation from one domain to another or from your previously used IPs to the ones you use in Dynamics Customer Insights - Journeys.
- If you use the same domain, your reputation can follow you. However, mailbox providers like Gmail use the reputation of the domain coupled with the reputation of the IP, so you still must follow the warm-up process.
- Dynamics Customer Insights - Journeys platform by default covers the IP part of warm-up by providing you with a high reputation set of IP addresses. So, you have a good base from the start to build up reputation for your domain.
- Mailbox providers trust metrics from their users and what they observe; no brand gets special treatment.
- B2B (business-to-business commerce) senders must follow the same warm-up process as B2C (Business to Consumer) senders, as many business domains are now hosted by Yahoo, Outlook, Gmail, AOL, and other popular email providers.