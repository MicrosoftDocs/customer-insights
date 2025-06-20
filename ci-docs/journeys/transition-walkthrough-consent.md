---
title: Transition consent
description: Learn how to transition consent capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/08/2025
ms.topic: article
author: petrjantac
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition consent

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Consent lets Customer Insights – Journeys customers send marketing messages. If you use outbound marketing, you can move consent settings to real-time journeys. Consent management is more advanced in real-time journeys. Learn about the differences and how to move consent in [Consent management and double opt-in transition guidance](real-time-marketing-consent-transition.md). This article also explains how to move subscription lists to real-time journeys to send segment-based newsletters. For more information, see [Understanding consent management in Dynamics 365 Customer Insights - Journeys - Dynamics FastTrack Blogs](https://community.dynamics.com/blogs/post/?postid=8b2a4ee8-1069-ee11-a81c-000d3a7a1a66)

To move consent, follow these steps:

1. Create a real-time journeys compliance profile with a [preference center](real-time-marketing-preference-centers.md).
1. Set up topics that match subscription lists.
1. Use the **Load Consent** tool to copy consent from contacts and subscription lists.
1. Switch emails to use the new compliance profile.
1. Recreate segments based on topics if needed.

Sometimes, you need to use a double opt-in (DOI) process when you collect consent. Learn how to turn on DOI for your compliance profile in [Double opt-in in real-time journeys](real-time-marketing-double-opt-in.md).

## The outbound marketing subscription center isn't available after outbound marketing is removed

- The outbound marketing subscription center isn't available after outbound marketing is removed.
- You can't send emails that include an *Unsubscribe* link referring to the subscription center.
- The real-time journeys *compliance profile with subscription center* stops working after outbound marketing is removed.
- Existing real-time journeys that send emails using a *compliance profile with subscription center* stop after outbound marketing is removed.

> [!IMPORTANT]
> An **Unsubscribe** link in an already sent email that points to an *outbound marketing subscription center* can't be redirected to the real-time journeys preference center.
>
> After outbound marketing is removed, all *Unsubscribe* links associated with the outbound marketing subscription center stop working. This can lead to noncompliance with privacy regulations if you don't have an alternative approach in place.
>
> Start using the real-time journeys preference centers with enough transition time before outbound marketing is removed. This helps ensure continuity and compliance with data privacy requirements.

## Guidance on specific capabilities

This section gives guidance on capabilities that work differently in real-time journeys or aren't available yet. Capabilities not listed here aren't prioritized. Don't wait for these capabilities—finish your transition to real-time journeys with alternative approaches.

### Disable opting out of topics or purposes in marketing forms and unintentional opt-out

- **Details**: When a user submits a marketing or event registration form, they're automatically opted out of any purposes or topics they don't explicitly select on the form.
- **Guidance**: We're enhancing form configuration options so you can define whether marketing or event registration form submission results in an opt-out. The [form prefill](real-time-marketing-form-prefill.md) feature also helps prevent unintentional opt-outs.

### Embed a preference center on my own web page

- **Details**: The preference center is hosted on Dynamics 365 infrastructure to improve availability and ensure secure data transmission. You can't embed the preference center into your own server environment.
- **Guidance**: Use marketing forms with prefill to build a custom preference management experience hosted on your own server environment.

## Consent transition FAQ

### Can I continue using consent based on the contact `DoNotBulkEmail` attribute?

The `DoNotBulkEmail` and `DoNotEmail` attributes stay available even after outbound marketing is removed, because they're also used by other Dynamics 365 applications. However, the real-time journeys preference center can't update these attributes, and it's best to use the new consent model based on contact-point consent.

If you want your customers to update the `DoNotBulkEmail` attribute through an unsubscribe link in an email, create a compliance profile with an external link and use a marketing form with prefill enabled so users can manage their preferences. Make sure the "Check contact consent in real-time journeys" [feature switch](admin-feature-switches.md) in the settings is enabled. This makes sure that email sending respects the values of the `DoNotBulkEmail` and `DoNotEmail` attributes.

### Can I continue using the subscription list?

Your existing subscription lists aren't deleted when outbound marketing is removed. However, you can't subscribe or unsubscribe from these anymore. To keep a working preference management experience, use the **Load consent** feature to move existing subscription lists into topics supported by real-time journeys.

### How do you update contact or lead details with the preference center?

The preference center form can't update lead or contact details. If you need to update these records, use a marketing form with form prefill enabled.

### Can outbound marketing check contact point consent records to evaluate consent when sending messages?

No, outbound marketing does not check contact point consent records to evaluate consent when sending messages.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
