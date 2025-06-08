---
title: Transition consent
description: Learn how to transition consent capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/08/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition consent

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Consent is an essential requirement that allows customers of Customer Insights – Journeys to send marketing messages. Customers who already use outbound marketing can transition consent settings to real-time journeys. Consent management, however, is more sophisticated in real-time journeys. The differences and how to transition consent are described in: [Consent management and double opt-in transition guidance](real-time-marketing-consent-transition.md). This article also describes how to migrate subscription lists to real-time journeys to send out segment-based newsletters. For a more detailed discussion, see [Understanding consent management in Dynamics 365 Customer Insights - Journeys - Dynamics FastTrack Blogs](https://community.dynamics.com/blogs/post/?postid=8b2a4ee8-1069-ee11-a81c-000d3a7a1a66)

You can transition the consent by completing the following steps:

1. Create a real-time journeys compliance profile with preference center.
1. Configure topics that match subscription lists.
1. Use the Load Consent tool to copy consent from contacts and subscription lists.
1. Switch emails to use the newly created compliance profile.
1. Recreate segments based on topics (optional).

When capturing consent from contacts, implementing a double opt-in (DOI) feature is sometimes necessary. You can [activate the DOI for your compliance profile in real-time journeys](real-time-marketing-double-opt-in.md).

## Outbound marketing subscription center is no longer available after outbound is removed

- The outbound marketing subscription center isn't available once outbound marketing is removed.
- It won't be possible to send emails including *Unsubscribe* link referring to subscription center.
- The real-time journey *compliance profile with subscription center* stops working after outbound is removed.
- The existing real-time journey sending emails using *compliance profile with subscription center* are stopped after outbound is removed.

> [!IMPORTANT]
> The **Unsubscribe** link in an already sent email that points to the *outbound marketing subscription center* cannot be redirected to the *real-time journeys preference center*
>
> **Once outbound marketing is removed:**
>
> - All *Unsubscribe* links associated with the outbound subscription center will cease to function.
> - This may lead to non-compliance with privacy regulations if no alternative is in place.
>
> **Begin using real-time journeys preference centers with a sufficient transition window ahead of outbound marketing removal. This ensures continuity and compliance with data privacy requirements.**

## Guidance on specific capabilities

See below for guidance on specific capabilities that are done differently in real-time or are not yet available. Capabilities not listed here are currently not prioritized. We strongly recommend that you do not wait for these capabilities and complete your transition to real-time using alternative approaches.

### Disable opting out of topic or purpose in Marketing forms, unintentional opt-out

- **Details:**
  When a user submits a marketing or event registration form, they are automatically opted out of any purposes or topics that they do not explicitly select on the form.

- **Guidance:**
  We plan to enhance form configuration options to let you define whether marketing or event registration form submission can result in an opt-out. The [form prefill](real-time-marketing-form-prefill.md) feature also helps prevent unintentional opt-outs.

### Embed a preference center on my own web page

- **Details:**
  The preference center is hosted on Dynamics infrastructure to improve availability and ensure secure data transmission. It is not possible to embed preference center into your own server environment.

- **Guidance:**
  You can use marketing form with prefill to build a custom preference management experience hosted on your own server environment.

## Consent transition FAQ

### Can I continue using consent based on the Contact DoNotBulkEmail attribute?

The `DoNotBulkEmail` and `DoNotEmail` attributes will remain available even after outbound marketing is removed, as they are also used by other Dynamics applications. However, the real-time journeys preference center cannot update these attributes and it is recommended to use the new consent model based on contact point consent.

In case you need to allow your customers to update the `DoNotBulkEmail` attribute through the Unsubscribe link in email, you can create a *compliance profile with external link* and use a marketing form with prefill enabled to allow users to manage their preferences. Ensure the "Check contact consent in real-time journeys" feature switch in setting is enabled. This ensures that email sending respects the values of the DoNotBulkEmail and DoNotEmail attributes.

### Can I continue using the subscription list?

The subscription list will not be deleted when outbound marketing is removed; however, it will no longer be possible to subscribe or unsubscribe from it. To maintain a functional preference management experience, it is recommended to use the Load consent feature to transition existing subscription lists into Topics supported by real-time marketing.

### How to update contact or lead details with preference center?

The preference center form cannot update lead or contact details. For scenarios requiring updates to these records, use a marketing form with form prefill enabled.

[!INCLUDE [transition-comments](./includes/transition-comments.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
