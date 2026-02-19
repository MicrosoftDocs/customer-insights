---
title: Transition overview
description: Transition from outbound marketing to real-time journeys in Dynamics 365 Customer Insights. Follow our guide to avoid interruptions.
ms.date: 02/18/2026
ms.update-cycle: 180-days
ms.topic: concept-article
author: alfergus
ms.author: alfergus
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Transition overview

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](transition-overview.md).

Dynamics 365 Customer Insights – Journeys includes two modules: outbound marketing and real-time journeys. Released in August 2021, real-time journeys offers advanced enterprise capabilities and is the default offering to new customers since August 2023.

In August 2024, Microsoft announced that outbound marketing would be removed after June 30, 2025. To avoid business continuity issues, all customers still using outbound marketing must transition to real-time journeys as we're [now in the last phase of removing outbound](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working). Review the [real-time journeys transition FAQs](transition-faqs.md), which covers common questions about transition to real-time. 

## Guidance for trials

You can create new trials only with real-time journeys.

## Guidance for new customers

New customers who install Customer Insights - Journeys no longer see the outbound marketing module. They must use real-time journeys; outbound marketing is unavailable to them.

## Guidance for existing customers currently using outbound marketing

Existing customers still using outbound marketing must transition to real-time journeys *immediately* to avoid interruption to their live journeys, forms, or events. 

We're gradually hiding, disabling, and removing outbound marketing from individual environments. If you're using custom UI or APIs, they'll stop working without further warning or notice. We're past the period where in-product banners and admin messages about outbound removal were being sent.

Here are some recommended actions for existing customers based on their needs:

| Situation                                                                                                          | Action                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I have an existing environment that previously had outbound marketing, but doesn't anymore. | This is expected unless you have an approved extension to continue using outbound marketing beyond its end of life. For more information, see [What will happen after June 30, 2025? Will outbound marketing stop working?](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working-updated-november-21-2025). You can no longer request extensions or add outbound marketing. If you have an approved extension and outbound marketing isn't visible, reply to the approval email you received previously from the obmextension@microsoft.com mailbox to report the issue. Don't create a support ticket. |
| I provisioned a new org, or copied, migrated, restored an existing org, and don't see outbound marketing. | This is expected. Outbound marketing isn't included in new environments (also known as “orgs”) and cannot be added. |
| I'm doing tenant migration as part of the transition.  | Finish transiting to real-time journeys before tenant migration. |
| Any other situation. | Requests to add outbound marketing are prohibited. Don't create a support ticket.|


## Past communications about outbound marketing removal

| Date       | Communication    | 
|------------|--------------------------------------------------------------------------------------------------------------------|
| December 2022   | [Transition playbook](https://community.dynamics.com/blogs/post/?postid=1b4394d5-7764-4484-aba9-c7f972292c10) published.                                                                                  |
| July 2023 | Announced that outbound marketing isn't available to new customers, will receive no new features, and is being removed in the future: [Transition to real-time marketing and transform your customer experience](https://www.microsoft.com/dynamics-365/blog/it-professional/2023/07/18/transition-to-real-time-marketing-and-transform-your-customer-experience/). |
| October 2023   | Added [transition resources](transition-resources.md) and area-specific [transition guidance](transition-walkthrough-functional.md).                                 |
| January 2024   | Transition blog: [Transition to real time journeys – the time is now](https://www.microsoft.com/dynamics-365/blog/it-professional/2024/01/09/transition-to-real-time-journeys-the-time-is-now/).                                   |
| August 2024   | Announced that outbound marketing is being [removed after June 30, 2025](real-time-marketing-overview.md). In-product banner announcing outbound marketing removal added. Admin email and message in the message center. |
| March 2025   | Email and message center notification (MC1025068) to admins about product changes to support outbound marketing removal.          |
| June 2025 | Users creating new outbound marketing journeys, segments, or forms get a message dialog asking them to create these assets in real-time journeys instead of outbound marketing. |
| July 2025 | Email and message center notification (MC1119263) to admins about start of the [phased removal process](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working-updated-november-21-2025). |
| November 2025 | Email and message center notification (MC1189547) to admins about the start of the outbound marketing removal [phased removal process](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working-updated-november-21-2025). |
| January 2026 | Email and message center notification (MC1214404) to admins about next phase of outbound marketing removal where live journeys, forms, events, and more will be stopped. |

[!INCLUDE [footer-include](./includes/footer-banner.md)]
