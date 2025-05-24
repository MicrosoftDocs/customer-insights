---
title: Prefill values for forms and event registration
description: Form prefill in Dynamics 365 Customer Insights - Journeys auto-fills known values for customers. Discover setup steps and security best practices.
ms.date: 05/23/2025
ms.topic: article
author: petrjantac
ms.author: colinbirkett
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:05/23/2025
---

# Prefill values for forms and event registration

The form prefill feature improves the customer experience by automatically filling form fields with known values for existing customers. This feature works for both *marketing* and *event registration* forms. Preference center forms use a different method for prefilling.

The system identifies an existing customer based on the prefill token in the URL, `msdynmkt_prefill`, which comes from a link in an email. The form is prefilled only if the customer selects the link in the email. The prefill token in the email link is valid for 30 days. If the customer selects a link in an email older than 30 days, the form isn't prefilled. The form is also prefilled only if the customer gives consent for tracking. Let your customers know that forwarding an email with a prefilled form link can expose their personal information.

The form replaces default field values with prefilled values.

## Set up form prefill

To increase the security of the form prefill feature, follow these steps:

1. [Enable your domain for form prefill](#enable-your-domain-for-form-prefill)
1. [Configure prefill in the form editor](#configure-prefill-in-the-form-editor)
1. [Check your consent model configuration](#check-your-consent-model-configuration)

### Enable your domain for form prefill

Enable your domain for form prefill in Settings > Domains. The default domain for forms hosted as a standalone page is enabled for form hosting by default. Contact technical support if you want to disable form prefill for this domain.
  
:::image type="content" source="media/real-time-marketing-enable-prefill-for-domain.png" alt-text="Enable your domain for form prefill." lightbox="media/real-time-marketing-enable-prefill-for-domain.png":::

> [!IMPORTANT]
> Enable form prefill only for trusted and secure domains that you control. Don't enable prefill for shared domains.

You don't need to verify ownership of the domain enabled for prefill of real-time journeys forms.

### Configure prefill in the form editor

Open the form editor and enable form prefill in the form settings. When you enable form prefill, all fields in that form are prefilled. You can also enable or disable prefill for a specific field in the field's properties. The form editor shows which fields are prefilled with an icon and displays the total count of prefilled fields.

:::image type="content" source="media/real-time-marketing-configure-form-prefill.png" alt-text="Set up form prefill in form editor." lightbox="media/real-time-marketing-configure-form-prefill.png":::

### Check your consent model configuration

Prefill requires the customer to consent to the *Tracking* purpose. The state of the Tracking purpose is cached for 15 minutes in the prefill scenario. This means the form can be prefilled for up to 15 minutes after the customer revokes consent for the Tracking purpose.

Form prefill maintains the consent already provided for specific topics and purposes. If a purpose or topic is linked to multiple channels, like email and text, form prefill selects the consent checkbox as if consent is given for all linked channels. For example, the Commercial purpose appears in the form as a single checkbox linked to both email and text channels. If the customer gives consent for the Commercial purpose via the email channel but not the text channel, submitting the prefilled form gives consent for both channels.

## Form prefill security

The form prefill feature uses multiple layers of security to protect data and control access. Communication between the Customer Insights - Journeys backend and Dynamics 365 uses a dedicated application account for the forms service, identified by `<applicationuser applicationuserid="6f3cf30e-6475-4505-a216-bce9d18e477f">`. All data transmissions use secure HTTPS connections. The system generates a unique form prefill token (`msdynmkt_prefill`) with a 30-day validity for each email. When a form loads, the system enforces a CORS (Cross-Origin Resource Sharing) check, and prefill access requires both the prefill token and CRM and Dataverse configuration that explicitly authorize the domain hosting the form. This multi-step validation makes sure that only trusted sources can use prefilled data.

## Troubleshooting form prefill

The following sections explain how to troubleshoot issues with form prefill.

### My form isn't prefilled

Form fields are prefilled only when you open the page containing the form by selecting a link in email. Check if the page URL has the msdynmkt_prefill parameter, which is automatically added to email links if there's valid consent for Tracking purpose. Double-check all steps in [Set up form prefill](#set-up-form-prefill).

### "Prefill marketing form" is enabled on the contact record, but the form isn't prefilled

The "Prefill marketing form" attribute works only for outbound marketing forms. Real-time journeys forms use the [Tracking purpose](real-time-marketing-email-text-consent.md#consent-to-track-user-behavior) as consent for prefill.
