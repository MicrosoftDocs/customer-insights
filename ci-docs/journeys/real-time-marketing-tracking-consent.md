---
title: Tracking consent in Customer Insights - Journeys
description: Learn how to configure tracking consent in Dynamics 365 Customer Insights - Journeys to support privacy requirements for tracking pixels in email.
ms.date: 08/14/2026
ms.topic: how-to
author: petrjantac
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
---

# Tracking consent in Dynamics 365 Customer Insights - Journeys

In 2026, privacy regulators issued additional guidance regarding the use of tracking pixels in email. They apply to private and public organizations that use tracking pixels, and to their technical service providers.

For Customer Insights - Journeys, the practical effect is that using tracking pixels for certain purposes may require the recipient's prior consent.

As described in this article, Customer Insights - Journeys offers configuration options that you can use to help meet these requirements.

> [!IMPORTANT]
> This summary is general information, not legal advice. Consult your own privacy counsel on how the recommendation applies to your organization.

## Configure tracking consent requirements

1. Set the **Tracking** purpose to the **Restrictive** enforcement model where warranted based on your use of Customer Insights - Journeys and applicable law. This setting ensures no tracking occurs unless the recipient explicitly opts in. Or create a new compliance profile for countries or regions you select without the **Use previously captured consent** option, so it gets the compliance profile's own tracking purpose that can be set to **Restrictive** without affecting other regions. If the **Use previously captured consent** option is enabled, the new profile shares the source profile's tracking purpose, and the enforcement model change applies globally.
    
    You must decide global or region-specific application at creation time. Unlike commercial and transactional purposes, a tracking purpose can't be linked to another profile later, and there's no standard way to unlink it. Because the compliance profile is selected per message and per form, region separation also implies region-specific messages and forms. Customers should validate their consent design with their own privacy counsel—setups vary significantly and Microsoft can't prescribe per-customer steps.

    To learn more about compliance profiles, purposes, and enforcement models, see [Consent management overview](real-time-marketing-compliance-settings.md).

1. Add the **Tracking** purpose to [marketing forms](real-time-marketing-manage-forms.md) and [preference centers](real-time-marketing-preference-centers.md) as its own checkbox, not pre-checked and not bundled with other consents you obtain, with a plain-language description of your tracking. Tracking consent controls:

    - Email open tracking through tracking pixels
    - Link click tracking in messages
    - UTM parameters added to URLs
    - Form prefill, where known users don't need to re-enter information already stored in Customer Insights - Journeys

    In addition, if **Tracking** consent is set to **Restrictive**, your users' website interactions aren't recorded unless the user both consented to your cookie banner and the **Tracking** purpose made available through Customer Insights - Journeys. Customer Insights - Journeys provides you with the option to obtain consent for tracking. You must determine whether and how to obtain consent(s) for your processing.

1. Review your existing consent records. Recipients whose email addresses you collected before you introduced the tracking checkbox won't have an explicit tracking opt-in, so under a restrictive enforcement model they aren't tracked until they opt in. Use the **Consent Center** to review consent records and import them in bulk, or the **Communication** tab of an individual contact or lead to edit a single record. See [Manage consent for email, SMS (text), and custom channel messages](real-time-marketing-email-text-consent.md).

1. Tell recipients that you use tracking pixels and make it easy for them to object. Describe in plain language your tracking in appropriate locations. In Customer Insights - Journeys, you can inform recipients whose email you previously collected of your tracking and grant them an opportunity to stop tracking by adding the **Tracking** purpose to your preference center and linking to that preference center from your messages.

## Understand how tracking consent affects engagement data

- Expect lower identified opens, clicks, web events, journey triggers, lead scoring, and engagement-based segmentation.

    For recipients who opt out before you send a message, the system doesn't insert a tracking pixel or tracking links, so it doesn't record opens or clicks. It also doesn't record website visits or link clicks.  

    For recipients who opt in before you send a message but opt out before selecting a link, the system records their interactions without a customer profile reference, so you can't later associate their interactions with a recipient. Because the system caches tracking consent for 24 hours, an interaction can still be recorded with a customer profile reference within 24 hours of opting out.

- Consent changes aren't instant. After someone revokes consent, link and open tracking can remain non-anonymous for up to 24 hours, and form prefill can continue for up to 15 minutes.

## Related consent and tracking resources

[Consent management overview](real-time-marketing-compliance-settings.md)  
[Manage consent for email, SMS (text), and custom channel messages](real-time-marketing-email-text-consent.md)  
[Customer Insights - Journeys link tracking mechanics](real-time-marketing-link-tracking-mechanics.md)  
[Customize your preference centers](real-time-marketing-preference-centers.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]