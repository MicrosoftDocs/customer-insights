---
title: Transition overview
description: Overview of the transition process from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/12/2024
ms.topic: article
author: alfergus
ms.author: alfergus
ms.collection: bap-ai-copilot
---

# Transition overview

> [!IMPORTANT]
> **[Outbound marketing](user-guide.md) will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date.

Dynamics 365 Customer Insights – Journeys includes two modules: outbound marketing and real-time journeys. Released in August 2021, real-time journeys offers advanced enterprise capabilities and has been the default offering to new customers since August 2023.  

In August 2024, Microsoft announced that outbound marketing will be removed as of June 30, 2025. To avoid any business continuity issues, all customers still using outbound marketing must transition to real-time journeys before this date. We'll also remove social posting and LinkedIn lead generation capabilities on December 2, 2024. We don’t plan to support social posting in real-time journeys because it has low demand and usage. We're considering adding LinkedIn lead generation to real-time journeys in a future release.

## Guidance for trials

New trials can only be created with real-time journeys.

## Guidance for new customers

New customers who install Customer Insights - Journeys no longer see the outbound marketing module and can't install it. Because outbound marketing is being removed as described above, we require new customers to adopt real-time journeys.

Here are some recommendations depending on your situation:

| Situation                                                                        | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I had planned to implement outbound marketing | Outbound marketing will be removed on June 30, 2025. You should update your plans and implement real-time journeys. See [Why should I transition to real-time journeys?](transition-faqs.md#why-should-i-transition-to-real-time-journeys)                                                                                                                                                                                                                                                                                                     |
| I evaluated the real-time journeys module and determined that I can't use it    | Review the [transition functional areas](transition-walkthrough-functional.md) guide (it has feature-specific guidance, workarounds, and a roadmap) and the other [transition resources](transition-resources.md). Given that outbound marketing will be removed, you should still implement real-time journeys even if there are some current gaps for your use cases, as we're adding new features all the time. We won't approve requests for adding outbound marketing. |

## Guidance for existing customers currently using outbound marketing

Existing customers still on outbound marketing must transition to real-time journeys before June 30, 2025 to avoid interruption and gain optimal performance, scale, ongoing product investments, and AI Copilot features. Learn more: [Customer Insights - Journeys transition FAQs](transition-faqs.md)

Here are some recommendation actions for existing customers depending on your needs:

| Situation                                                                                                          | Action                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I provisioned a new org (or copied, migrated, or restored an existing org) and don't see outbound marketing                                             | This is expected; outbound marketing is no longer included in new orgs. We strongly recommend using real-time journeys as outbound marketing will be removed on June 30, 2025. See [Why should I transition to real-time journeys?](transition-faqs.md#why-should-i-transition-to-real-time-journeys) |
| I'm planning to transition to real-time journeys soon but need outbound marketing until then.  | You can add outbound marketing back using the **Enable** link available on the **Settings** > **Versions** page. <br><br> **Important**: To see the link and add outbound marketing, you need to be an admin. If you're not an admin, ask someone who is to do this step. If you still don't see the link, follow the guidance for [requesting outbound marketing to be added](transition-overview.md#request-an-exception-to-enable-outbound-marketing).                 |

## Request an exception to enable outbound marketing (existing outbound customers only)

If you're an existing outbound marketing user and require outbound marketing to be enabled in your environment, you can request an exception by filling out [the outbound marketing request form](https://go.microsoft.com/fwlink/?linkid=2251742).

Note the following parameters:
- This request should only be made by customers who already have been using outbound marketing. Requests from customers who never had outbound marketing will be denied.
- Don't create support tickets or use other channels for the same requests; you'll be redirected to this form.
- This form requires an email address. The email address is used to communicate receipt of the request, confirming when the request has been processed, and if needed, ask for additional information.
- Most requests are processed in about three business days once all required information is available.

> [!TIP]
> If you have questions or comments, visit the [Outbound to real-time transition community forum](https://community.dynamics.com/forums/thread/?partialUrl=Outbound-to-Real-Time-Transition)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
