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

In August 2024, Microsoft announced that outbound marketing will be removed after June 30, 2025. To avoid any business continuity issues, all customers still using outbound marketing must transition to real-time journeys as we are [taking steps](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working) to reduce usage of outbound and eventually remove it.  Please review [Real-time journeys transition FAQs](transition-faqs.md) that covers common topics including what to do if you are unable to complete this transition in time.

## Guidance for trials

New trials can only be created with real-time journeys.

## Guidance for new customers

New customers who install Customer Insights - Journeys no longer see the outbound marketing module. They must use real-time journeys as they cannot add outbound themselves or request it to be added. 

Here are some recommendations depending on your situation:

| Situation                                                                        | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I planned to implement outbound marketing | You should update your plans and implement real-time journeys. See [Why should I transition to real-time journeys?](transition-faqs.md#why-should-i-transition-to-real-time-journeys)                                                                                                                                                                                                                                                                                                     |
| I evaluated the real-time journeys module and determined that I can't use it    | Review the [transition functional areas](transition-walkthrough-functional.md) guide (it has feature-specific guidance, workarounds, and a roadmap) and the other [transition resources](transition-resources.md). Because outbound marketing will be removed, you must implement real-time journeys even if there are some current gaps for your use cases, as we're adding new features all the time. Weno longer accept requests for adding outbound marketing for new customers. |

## Guidance for existing customers currently using outbound marketing

Existing customers still using outbound marketing must transition to real-time journeys to avoid interruption and gain optimal performance, scale, ongoing product investments, and AI Copilot features. Learn more: [Customer Insights - Journeys transition FAQs](transition-faqs.md).

### What changes will I see in outbound environments?
We will gradually remove outbound from individual environments as outbound campaigns/events end in those environments. Users will see various in-product banners and message dialogs during different phases as described in the [How and when outbound will be removed?](transition-faqs.md#how-and-when-outbound-will-be-removed)

Here are some recommended actions for existing customers depending on their needs:

| Situation                                                                                                          | Action                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I provisioned a new org (or copied, migrated, or restored an existing org) and don't see outbound marketing                                             | This is expected. Outbound marketing is no longer included in new emvironments (also called “orgs”). You can add outbound marketing using the **Enable** link available on the **Settings > Versions** page. See below if you don’t see this link or if it doesn’t work.  |
| I am doing tenant migration as part of transition  | You will need to request outbound marketing to be added (see below). The overall tenant-to-tenant migration plan should allow for 5–7 business days for this request to be processed (this is to allow time for potential troubleshooting delays due to unforeseen issues and time zone differences). |
| Any other situation | Requests for adding outbound marketing will generally not be approved. |

### If the "Enable" link isn't available or doesn't work

Enable link is shown only if there is at least one more environment in the same tenant that has outbound AND you have admin role. If both these conditions are true and you still do not see Enable link, please request outbound to be added (see below) and add this note in the form "Do not see enable link, Confirming that I have admin role and there is at least one other environment with org id <provide ID> in this tenant with outbound"
 
If the Enable link is available but didn't work (and you jave admin role), then follow these steps:
  1. Sign in to Customer Insights - Journeys using a system admin user account.
  2. Go to **Settings** > **Versions** and select the **Manage + Update** link. This takes you to the marketing installation page.
  3. In the browser address bar, add `&redirecttolegacyexp=true` to the page URL and then reload the page.
  4. Go back to **Settings** > **Versions** in Customer Insights - Journeys and select the "Enable" link again.
If this still doesn't work, complete the outbound marketing request form (see below) and add this note: "Already completed the user token generation step, the Enable link still failed."

### Requesting outbound to be added

Add outbound marketing request will be considered only if all 4 of the following conditions are met:
1. The environment is in a tenant that is currently approved for using outbound (see [requesting extension](transition-faqs.md#i-cant-transition-by-the-outbound-marketing-removal-date-can-i-request-an-extension)) 
2. You have admin role
3. You do not see Enable link or it doesn't work (even after completing the steps outined above)
4. You are in one of these situations (a) You are doing tenant migration, or (b) You had only one environment in this tenant with outbound that wsa previously being used as a production system

Please read these important notes before you submit the request:
- Make sure you meet the eligibility criteria described above.
- This form is the only way to request outbound marketing. Don't contact support or use other channels as you'll be redirected to this form.
- This form requires an email address that will only be used to confirm receipt of the request, inform you when the request has been reviewed, and ask for additional information (if needed). Multiple email addresses are okay if they are separated by semi-colon (do not use any other separator, you will not receive the automated acknowledgement email)
- If you need a new portal provisioned with your requested outbound marketing instance, you can ask for it in the same request. You can't attach an existing portal, you can only have a new one provisioned for your outbound marketing instance. If you need to add portals to other existing outbound orgs, don't use this form. Instead, follow the guidance at [Adding a Power Apps portal to an outbound marketing instance](portal-optional.md#adding-a-power-apps-portal-to-an-outbound-marketing-instance). 
- Most requests are reviewed in about five business days once all the required information is available. Adding outbound is done by a specialized team that is currently available during India business hours only and time zone differences (and holidays) can lead to additional delays. Use the email address provided in the acknowledgement email when you submit the form if you need to update any information or have question. Do not contact support or use other channels as they will not be able to help.

Once you have reviewed the above notes and confirmed your eligibility, fill out [the outbound marketing request form](https://go.microsoft.com/fwlink/?linkid=2251742). 



## Past communications about outbound marketing removal

| Date       | Communication    | 
|------------|--------------------------------------------------------------------------------------------------------------------|
| December 2022   | [Transition playbook](https://community.dynamics.com/blogs/post/?postid=1b4394d5-7764-4484-aba9-c7f972292c10) published.                                                                                  |
| July 2023 | Announced that outbound marketing isn't available to new customers, will receive no new features, and is being removed in the future: [Transition to real-time marketing and transform your customer experience](https://www.microsoft.com/dynamics-365/blog/it-professional/2023/07/18/transition-to-real-time-marketing-and-transform-your-customer-experience/). |
| October 2023   | Added [transition resources](transition-resources.md) and area-specific [transition guidance](transition-walkthrough-functional.md).                                 |
| January 2024   | Transition blog: [Transition to real time journeys – the time is now](https://www.microsoft.com/dynamics-365/blog/it-professional/2024/01/09/transition-to-real-time-journeys-the-time-is-now/).                                   |
| August 2024   | Announced that outbound marketing is being [removed after June 30, 2025](real-time-marketing-overview.md). In-product banner announcing outbound marketing removal added. Admin email and message in the message center. |
| March 2025   | Email and message center notification to admins about product changes to support outbound marketing removal.          |
| June 2025 | Users creating new outbound journeys, segments, forms, etc.get a message dialog asking them to create these assets in real-time instead of outbound |

[!INCLUDE [footer-include](./includes/footer-banner.md)]
