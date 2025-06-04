---
title: Transition overview
description: Transition from outbound marketing to real-time journeys in Dynamics 365 Customer Insights. Follow our guide to avoid interruptions before June 30, 2025.
ms.date: 03/07/2025
ms.topic: concept-article
author: alfergus
ms.author: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Transition overview

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date.

Dynamics 365 Customer Insights – Journeys includes two modules: outbound marketing and real-time journeys. Released in August 2021, real-time journeys offers advanced enterprise capabilities and has been the default offering to new customers since August 2023.  

In August 2024, Microsoft announced that outbound marketing will be removed as of June 30, 2025. To avoid any business continuity issues, all customers still using outbound marketing must transition to real-time journeys before this date. We removed social posting and LinkedIn lead generation capabilities on December 2, 2024. We don’t plan to support social posting in real-time journeys because it has low demand and usage. We're considering adding LinkedIn lead generation to real-time journeys in a future release.

## Guidance for trials

New trials can only be created with real-time journeys.

## Guidance for new customers

New customers who install Customer Insights - Journeys no longer see the outbound marketing module and can't install it. Because outbound marketing is being removed, new customers must use real-time journeys.

Here are some recommendations depending on your situation:

| Situation                                                                        | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I planned to implement outbound marketing | Outbound marketing will be removed on June 30, 2025. You should update your plans and implement real-time journeys. See [Why should I transition to real-time journeys?](transition-faqs.md#why-should-i-transition-to-real-time-journeys)                                                                                                                                                                                                                                                                                                     |
| I evaluated the real-time journeys module and determined that I can't use it    | Review the [transition functional areas](transition-walkthrough-functional.md) guide (it has feature-specific guidance, workarounds, and a roadmap) and the other [transition resources](transition-resources.md). Because outbound marketing will be removed, you should still implement real-time journeys even if there are some current gaps for your use cases, as we're adding new features all the time. We won't approve requests for adding outbound marketing. |

## Guidance for existing customers currently using outbound marketing

Existing customers still using outbound marketing must transition to real-time journeys before June 30, 2025 to avoid interruption and gain optimal performance, scale, ongoing product investments, and AI Copilot features. Learn more: [Customer Insights - Journeys transition FAQs](transition-faqs.md).

Here are some recommended actions for existing customers depending on their needs:

| Situation                                                                                                          | Action                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I provisioned a new org (or copied, migrated, or restored an existing org) and don't see outbound marketing                                             | This is expected. Outbound marketing is no longer included in new orgs. We strongly recommend using real-time journeys as outbound marketing will be removed on June 30, 2025. See [Why should I transition to real-time journeys?](transition-faqs.md#why-should-i-transition-to-real-time-journeys) |
| I'm planning to transition to real-time journeys soon but need outbound marketing until then  | You can add outbound marketing back using the **Enable** link available on the **Settings** > **Versions** page. <br><br> **Important**: To see the link and add outbound marketing, you need to be an admin. If you're not an admin, ask someone who is to do this step. If you still don't see the link, follow the guidance for [requesting outbound marketing to be added](transition-overview.md#if-the-enable-link-isnt-available-or-doesnt-work).                |

### If the "Enable" link isn't available or doesn't work

If you're an existing outbound marketing user, you should see the "Enable" outbound marketing link as described above. If you don't see the Enable link (and you confirmed that you have an admin role), fill out [the outbound marketing request form](https://go.microsoft.com/fwlink/?linkid=2251742). If the Enable link is available but didn't work, follow these steps:
  1. Sign in to Customer Insights - Journeys using a system admin user account.
  1. Go to **Settings** > **Versions** and select the **Manage + Update** link. This takes you to the marketing installation page.
  1. In the browser address bar, add `&redirecttolegacyexp=true` to the page URL and then reload the page.
  1. Go back to **Settings** > **Versions** in Customer Insights - Journeys and select the "Enable" link again. If this still doesn't work, complete the outbound marketing request form mentioned earlier and add this note: "Already completed the user token generation step, the Enable link still failed."

- The outbound marketing request form is only for existing customers currently using outbound marketing who are unable to use the "Enable" link as described above. Requests for all other reasons will be rejected.
- This request should only be made by customers who have already been using outbound marketing. Requests from customers who never had outbound marketing will be denied.
- The form is the only way to request outbound marketing. Don't contact support or use other channels as you'll be redirected to this form.
- This form requires an email address that will only be used to confirm receipt of the request, inform you when the request has been reviewed, and ask for additional information (if needed).
- If you need a new portal provisioned with your requested outbound marketing instance, you can ask for it in the same request. You can't attach an existing portal, you can only have a new one provisioned for your outbound marketing instance. If you need to add portals to other existing outbound orgs, don't use this form. Instead, follow the guidance at [Adding a Power Apps portal to an outbound marketing instance](portal-optional.md#adding-a-power-apps-portal-to-an-outbound-marketing-instance). 
- Most requests are reviewed in about five business days once all the required information is available.

## Past communications about outbound marketing removal

| Date       | Communication    | 
|------------|--------------------------------------------------------------------------------------------------------------------|
| December 2022   | [Transition playbook](https://community.dynamics.com/blogs/post/?postid=1b4394d5-7764-4484-aba9-c7f972292c10) published.                                                                                  |
| July 2023 | Announced that outbound marketing isn't available to new customers, will receive no new features, and is being removed in the future: [Transition to real-time marketing and transform your customer experience](https://www.microsoft.com/dynamics-365/blog/it-professional/2023/07/18/transition-to-real-time-marketing-and-transform-your-customer-experience/). |
| October 2023   | Added [transition resources](transition-resources.md) and area-specific [transition guidance](transition-walkthrough-functional.md).                                 |
| January 2024   | Transition blog: [Transition to real time journeys – the time is now](https://www.microsoft.com/dynamics-365/blog/it-professional/2024/01/09/transition-to-real-time-journeys-the-time-is-now/).                                   |
| August 2024   | Announced that outbound marketing is being [removed after June 30, 2025](real-time-marketing-overview.md). In-product banner announcing outbound marketing removal added. Admin email and message in the message center. |
| March 2025   | Email and message center notification to admins about product changes to support outbound marketing removal.          |

[!INCLUDE [transition-comments](./includes/transition-comments.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
