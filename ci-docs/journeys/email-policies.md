---
title: Email policies and suspension standards
description: Learn about Dynamics 365 Customer Insights - Journeys email policies and what to do if your account is suspended.
ms.date: 02/14/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Email policies and suspension standards

Dynamics 365 Customer Insights - Journeys has a deliverability protection system that detects excessive hard bounces, spam reports, spam traps hits block listing, abuse complaints or direct complaints from either recipients or third-party email security solutions. This system protects our entire customer base. If email criteria are violated, accounts will be suspended or terminated.

## Stages of review

-   *Suspended*

    Email sending is suspended when the deliverability protection system detects that one or multiple email limits were breached on your email recipients, or fraudulent account activity was detected.

    When email sending is suspended, you see a warning banner in your email tool about a problem detected by the deliverability protection system. The banner contains details about the problem and recommendations to improve future email messages.

    If your email sending is suspended, create a support ticket first and then reach out directly to our [Email Deliverability team](mailto:dynmktdeliverability@microsoft.com). When it is proven that you have taken sufficient steps to address the cause of suspension, we will reinstate your account.

-   *Terminated*

    In case we detect concrete signs of abuse or lack of cooperation we will terminate your account sending capabilities.

## Suspension criteria for Dynamics 365 Customer Insights - Journeys?

-   *Hard bounces*: The hard bounce limit is 8%. The preferred bounce rate is less than 2%.
-   *Spam reports*: The spam complaint rate limit is 0.3% (1 in 1,000 messages sent).
-   *Direct complaints*: Direct complaints are sent to the Dynamics 365 abuse desk and are reviewed on a case by case basis.
-   *Spamtrap hits:* Spam traps are a tool used by ISPs or Email Filters to identify unsolicited traffic. It cannot be identified by the sender and can cause IP blocks and delivery incidents especially on a shared environment.
-   Lists scraped, purchased, or rented from third party providers are prohibited and are grounds for termination.

## Other reasons that can cause account suspensions

-   A violation of our [terms of use](https://www.microsoft.com/en-US/servicesagreement).
-   Usage of the [default domain feature](domain-authentication.md#the-default-authenticated-domain) for bulk email sending.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
