---
title: Prefill values for forms and event registration
description: Prefill values for forms in Dynamics 365 Customer Insights - Journeys.
ms.date: 04/29/2025
ms.topic: article
author: petrjantac
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Prefill values for forms and event registration

The form prefill feature enhances customer experience by automatically filling in form fields with known values for existing customers. This feature is available for both *marketing* and *event registration* forms. However, preference center forms use a different method for prefilling.

An existing customer is identified based on the prefill token in the URL (msdynmkt_prefill), which is derived from a link in an email. Therefore, the form can only be prefilled if the customer arrives at the page by clicking a link in the email. The prefill token in the email link is valid for 30 days. If the customer selects a link in an email older than 30 days, the visited form won't be prefilled. Additionally, the form can only be prefilled if the existing customer provided consent for the tracking purpose. You should inform your customers that, by forwarding an email containing a link to a prefilled form, they might inadvertently expose their personal information.

The default values of form fields are replaced by the prefilled values.

## Set up form prefill

To increase the level of security of the form prefill feature there are several steps to enable this feature:

1. [Enable your domain for form prefill](#enable-your-domain-for-form-prefill)
1. [Configure prefill in the form editor](#configure-prefill-in-the-form-editor)
1. [Check your consent model configuration](#check-your-consent-model-configuration)

### Enable your domain for form prefill

You can enable your domain for form prefill in Settings -> Domains. The out-of-the-box domain for forms hosted as a standalone page is enabled for form hosting by default. You can contact technical support if you want to disable form prefill for this domain.
  
:::image type="content" source="media/real-time-marketing-enable-prefill-for-domain.png" alt-text="Enable your domain for form prefill." lightbox="media/real-time-marketing-enable-prefill-for-domain.png":::

> [!IMPORTANT]
> Make sure you enable the form prefill only for trusted and secure domains that you control. Do not enable prefill for shared domains.

You aren't required to verify ownership of the domain enabled for prefill of real-time journeys forms.

### Configure prefill in the form editor

Open the form editor and enable form prefill in the form settings. Enabling form prefill in the settings makes all fields of that specific form prefilled. You can also enable or disable prefill for a specific field in the fields properties. The form editor indicates which fields are prefilled with an icon and the editor also shows the total count of prefilled fields.

:::image type="content" source="media/real-time-marketing-configure-form-prefill.png" alt-text="Set up form prefill in form editor." lightbox="media/real-time-marketing-configure-form-prefill.png":::


### Check your consent model configuration

The prefill requires the customer to consent with the *Tracking* purpose. The state of Tracking purpose is cached for 15 minutes for prefill scenario. That means the form can be prefilled up to 15 minutes after the customer revoked the consent for the Tracking purpose.

The goal of form prefill is to maintain the consent already provided for specific topics and purposes. If a purpose or topic is linked to multiple channels (such as email and text), the form prefill sets the consent checkbox as if consent was given for all linked channels. For example, the Commercial purpose is represented in the form by a single checkbox linked to both email and text channels. If the customer provided consent for the Commercial purpose via the email channel but not the text channel, submitting the prefilled form results in consent being provided for both channels.

## Troubleshooting form prefill

The following sections explain how to troubleshoot issues with form prefill.

### My form isn't prefilled

The form fields are prefilled only when the page containing the form is accessed by clicking a link in email. Check if the page URL contains the msdynmkt_prefill parameter, which is automatically added to email links if there's valid consent for Tracking purposes. Double check all steps in [Set up form prefill](#set-up-form-prefill).

### "Prefill marketing form" is enabled on the contact record, but the form isn't prefilled

The "Prefill marketing form" attribute only works for outbound marketing forms. Real-time journeys forms use the [Tracking purpose](real-time-marketing-email-text-consent.md#consent-to-track-user-behavior) as the consent for prefill.
