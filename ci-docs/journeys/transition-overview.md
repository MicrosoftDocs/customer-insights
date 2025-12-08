---
title: Transition overview
description: Transition from outbound marketing to real-time journeys in Dynamics 365 Customer Insights. Follow our guide to avoid interruptions.
ms.date: 12/08/2025
ms.update-cycle: 180-days
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
> **The [outbound marketing](user-guide.md) module is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](transition-overview.md).

Dynamics 365 Customer Insights – Journeys includes two modules: outbound marketing and real-time journeys. Released in August 2021, real-time journeys offers advanced enterprise capabilities and is the default offering to new customers since August 2023.

In August 2024, Microsoft announced that outbound marketing would be removed after June 30, 2025. To avoid business continuity issues, all customers still using outbound marketing must transition to real-time journeys as we're [taking steps](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working-updated-november-21-2025) to reduce usage of outbound marketing, and eventually remove it.  Review the [real-time journeys transition FAQs](transition-faqs.md), which covers common topics including what to do if you're unable to complete the transition in time.

## Guidance for trials

You can create new trials only with real-time journeys.

## Guidance for new customers

New customers who install Customer Insights - Journeys no longer see the outbound marketing module. They must use real-time journeys; they can't add outbound marketing or request to add it.

Here are some recommendations depending on your situation:

| Situation                                                                        | Action                                                                             |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I planned to implement outbound marketing. | Update your plans and implement real-time journeys. Learn more: [Why should I transition to real-time journeys?](transition-faqs.md#why-should-i-transition-to-real-time-journeys)                             |
| I evaluated the real-time journeys module and determined that I can't use it.    | Review the [transition functional areas](transition-walkthrough-functional.md) guide (it has feature-specific guidance, workarounds, and a roadmap) and other [transition resources](transition-resources.md). Because outbound marketing is being removed, implement real-time journeys even if there are current gaps for your use cases, as new features are added all the time. Requests to add outbound marketing for new customers aren't accepted. |

## Guidance for existing customers currently using outbound marketing

Existing customers still using outbound marketing must transition to real-time journeys to avoid interruption and gain optimal performance, scale, ongoing product investments, and AI Copilot features. Learn more: [Customer Insights - Journeys transition FAQs](transition-faqs.md).

### What changes will I see in outbound marketing environments?

We'll gradually remove outbound marketing from individual environments as outbound campaigns and events end in those environments. Users will see various in-product banners and message dialogs during different phases as described here: [What will happen after June 30, 2025? Will outbound marketing stop working?](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working-updated-november-21-2025).

Here are some recommended actions for existing customers based on their needs:

| Situation                                                                                                          | Action                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I have an existing environment that previously had outbound marketing, but doesn't anymore. | This is expected unless you have an approved extension to continue using outbound marketing beyond its end of life. See [What will happen after June 30, 2025? Will outbound marketing stop working?](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working-updated-november-21-2025) You can no longer request extensions. Requests to add or enable outbound marketing for such environments are no longer approved. If you have an approved extension and outbound marketing is still hidden, reply to the approval email you received previously from the obmextension@microsoft.com mailbox and report the issue. Don't create a support ticket. |
| I provisioned a new org (or copied, migrated, or restored an existing org) and don't see outbound marketing. | This is expected. Outbound marketing isn't included in new environments (also called “orgs”). If you have an approved extension to continue using outbound marketing beyond its end of life, you can add outbound marketing using the **Enable** link on the **Settings** > **Versions** page. See the next section if you have the approval, but don't see this link or it doesn't work. If you don't have an approved extension, you can't add outbound marketing.  |
| I'm doing tenant migration as part of the transition.  | Request outbound marketing to be added (see the next section). The tenant-to-tenant migration plan should allow five to seven business days for this request to be processed. This allows time for potential troubleshooting delays because of unforeseen issues and time zone differences. |
| Any other situation. | Requests to add outbound marketing generally aren't approved. Don't create a support ticket.|

### If the "Enable" link isn't available or doesn't work

> [!NOTE]
> This section only applies if you have an approved extension to use outbound marketing beyond its end of life.

The enable link appears only if there's at least one other environment in the same tenant that has outbound marketing and you have an admin role. If both conditions are true and you still don't see the enable link, create a request to add outbound marketing (see the next section) and add this note in the form: "Don't see enable link. Confirming that I have an admin role and there's at least one other environment with the org ID `<provide ID>` in this tenant with outbound marketing."
 
If the enable link is available but doesn't work (and you have an admin role), follow these steps:

1. Sign in to Customer Insights - Journeys using a system admin user account.
1. Go to **Settings** > **Versions** and select the **Manage + Update** link to open the installation page.
1. In the browser address bar, add `&redirecttolegacyexp=true` to the page URL, and then reload the page.
1. Go back to **Settings** > **Versions** in Customer Insights - Journeys and select the "Enable" link again.

If this still doesn't work, complete the outbound marketing request form (see the next section) and add this note: "Already finished the user token generation step and the enable link still failed."

### Requesting outbound marketing to be added

An outbound marketing request is considered only if all four of the following conditions are met:

1. The environment is in a tenant that's approved for using outbound marketing (see [requesting an extension](transition-faqs.md#i-need-more-time-to-complete-the-transition-can-i-request-an-extension)).
1. You have an admin role.
1. You don't see the enable link, or it doesn't work (even after following the steps in the previous section).
1. You're in one of these situations: (a) You're doing a tenant migration, or (b) you had only one environment in the tenant with outbound marketing that was used as a production system.

Read these important notes before you submit a request:

- Make sure you meet the eligibility criteria described above.
- This form is the only way to request outbound marketing. Don't contact support or use other channels, as you'll be redirected to this form.
- This form requires an email address that is only used to confirm receipt of the request, inform you when the request has been reviewed, and ask for additional information (if needed). Multiple email addresses are okay if they're separated by a semicolon (don't use any other separator or you won't receive the automated acknowledgment email.)
- If you need a new portal provisioned with your requested outbound marketing instance, you can ask for it in the same request. You can't attach an existing portal; you can only have a new one provisioned for your outbound marketing instance. If you need to add portals to other existing outbound orgs, don't use this form. Instead, follow this guidance: [Adding a Power Apps portal to an outbound marketing instance](portal-optional.md#adding-a-power-apps-portal-to-an-outbound-marketing-instance). 
- Most requests are reviewed in about five business days once all the required information is available. Adding outbound marketing is done by a specialized team that's currently available during India business hours only. Time zone differences (and holidays) can lead to additional delays. Use the email address provided in the acknowledgment email when you submit the form if you need to update any information or have a question. Don't contact support or use other channels, as they won't be able to help.

Once you've reviewed the above notes and confirmed your eligibility, fill out [the outbound marketing request form](https://go.microsoft.com/fwlink/?linkid=2251742). 

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

[!INCLUDE [footer-include](./includes/footer-banner.md)]
