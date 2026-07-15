---
title: Prefill values for forms and event registration
description: Form prefill auto-fills known values on Customer Insights - Journeys forms for contacts and leads, based on tracking consent and security checks.
ms.date: 07/15/2026
ms.topic: article
author: petrjantac
ms.author: alfergus
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

> [!NOTE]
> Form prefill only supports **Contact** and **Lead** records. If a journey targets a Customer Insights - Data profile audience, forms opened from email links in that journey can't be prefilled.

## Set up form prefill

To increase the security of the form prefill feature, follow these steps:

1. [Enable your domain for form prefill](#enable-your-domain-for-form-prefill)
1. [Configure prefill in the form editor](#configure-prefill-in-the-form-editor)
1. [Check your consent model configuration](#check-your-consent-model-configuration)

### Enable your domain for form prefill

Enable your domain for form prefill in Settings > Domains. The default domain for forms hosted as a standalone page is enabled for form hosting by default. Contact technical support if you want to disable form prefill for this domain.

:::image type="content" source="media/real-time-marketing-enable-prefill-for-domain.png" alt-text="Screenshot of the Domains settings page showing the option to enable form prefill for a domain." lightbox="media/real-time-marketing-enable-prefill-for-domain.png":::

> [!IMPORTANT]
> Enable form prefill only for trusted and secure domains that you control. Don't enable prefill for shared domains.

You don't need to verify ownership of the domain enabled for prefill of real-time journeys forms.

### Configure prefill in the form editor

Open the form editor and enable form prefill in the form settings. When you enable form prefill, all fields in that form are prefilled. You can also enable or disable prefill for a specific field in the field's properties. The form editor shows which fields are prefilled with an icon and displays the total count of prefilled fields.

:::image type="content" source="media/real-time-marketing-configure-form-prefill.png" alt-text="Screenshot of the form editor showing the form prefill setting and prefilled field icons." lightbox="media/real-time-marketing-configure-form-prefill.png":::

### Check your consent model configuration

Prefill requires the customer to consent to the *Tracking* purpose. The state of the Tracking purpose is cached for 15 minutes in the prefill scenario. This means the form can be prefilled for up to 15 minutes after the customer revokes consent for the Tracking purpose.

Form prefill populates consent checkboxes based on the customer's current consent state. The prefilled state reflects the [enforcement-model](real-time-marketing-compliance-settings.md#consent-enforcement-models)-based consent decision, not just the stored consent record. For example, when a channel uses a **Disabled** enforcement model, the checkbox is always prefilled as opted in - even if an opt-out record exists for that contact point.

#### How consent checkbox prefill is calculated

The system uses a two-stage calculation for each consent checkbox on the form.

**Stage 1 – Consent decision (per channel)**

For each channel the checkbox covers (for example, email or text), the system resolves an *will send* or *will not send* decision from the purpose's enforcement model and the stored consent record:

| Enforcement model | Opted in | Opted out | Not set |
|---|---|---|---|
| **Restrictive** | Will send | Will not send | Will not send |
| **Non-restrictive** | Will send | Will not send | Will send |
| **Disabled** | Will send | Will send | Will send |

- **Restrictive**: The message is sent only if an explicit opt-in record exists. An opt-out or not set value means the message isn't sent.
- **Non-restrictive**: The message isn't sent only if an explicit opt-out record exists. An opt-in or not set value means the message is sent.
- **Disabled**: The message is always sent. The stored consent record isn't consulted.

You configure enforcement models per channel, so the same purpose can have different enforcement models for email and text. Learn more about [consent enforcement models](real-time-marketing-compliance-settings.md#consent-enforcement-models).

If a *checkbox covers multiple channels*, the system combines the per-channel results by using **OR** logic. The checkbox is treated as opted in if the customer is opted in on *any* of the linked channels.

For example, if the commercial purpose appears as a single checkbox linked to both email and text, and the customer is opted in for email but opted out for text, the checkbox is prefilled as opted in.

> [!IMPORTANT]
> Because of the **OR** logic, submitting the prefilled form gives consent for all linked channels. In the example preceding, the customer also gains consent for the text channel after submitting the form.

**Stage 2 – Checkbox state**

The system combines the Stage 1 consent decision with the form field's **When checked** setting to determine whether the checkbox appears checked or unchecked:

- **Opt user in** (default): The checkbox is checked when the consent decision is *Will send*, and unchecked when *Will not send*.
- **Opt user out**: The checkbox is checked when the consent decision is *Will not send*, and unchecked when *Will send*. This setting inverts the checked state compared to the default.

For example, if a checkbox uses **Opt user out** and the customer's consent decision is *Will send*, the checkbox appears unchecked. Learn more about the [When checked setting](real-time-marketing-manage-forms.md).

## Form prefill security

The form prefill feature uses multiple layers of security to protect data and control access. Communication between the Customer Insights - Journeys backend and Dynamics 365 uses a dedicated application account for the forms service, identified by `<applicationuser applicationuserid="6f3cf30e-6475-4505-a216-bce9d18e477f">`. All data transmissions use secure HTTPS connections. The system generates a unique form prefill token (`msdynmkt_prefill`) with a 30-day validity for each email. When a form loads, the system enforces a CORS (Cross-Origin Resource Sharing) check, and prefill access requires both the prefill token and Customer Relationship Management (CRM) and Dataverse configuration that explicitly authorize the domain hosting the form. This multistep validation ensures that only trusted sources can use prefilled data.

## How form prefill works with different audience types

Form prefill matches each field's target audience with the record type of the customer who opens the form. Only fields with a matching target audience are prefilled.

Each form field is associated with one of the following target audience values:
**Contact**, **Lead**, or **Lead & Contact** (mapped to both entities).

- **Contact** fields are prefilled only when the customer is recognized as an
  existing contact record.
- **Lead** fields are prefilled only when the customer is recognized as an
  existing lead record.
- **Lead & Contact** fields are prefilled only when the customer is recognized
  as a contact. If the customer is recognized as a lead, these fields are
  skipped and not prefilled.

### Form prefill audience example

A form contains three fields:

| Field         | Target audience  | Prefilled for contact? | Prefilled for lead? |
|---------------|------------------|:----------------------:|:-------------------:|
| First Name    | Contact          | ✅ Yes                 | ❌ No               |
| Company Name  | Lead             | ❌ No                  | ✅ Yes              |
| Email         | Lead & Contact   | ✅ Yes                 | ❌ No               |

> [!NOTE]
> Fields that don't match the customer's record type remain empty and can be filled manually by the customer.

## Troubleshooting form prefill

The following sections explain how to troubleshoot issues with form prefill.

### My form isn't prefilled

Form fields are prefilled only when you open the page containing the form by selecting a link in email. Check if the page URL has the msdynmkt_prefill parameter, which is automatically added to email links if there's valid consent for Tracking purpose. Double-check all steps in [Set up form prefill](#set-up-form-prefill).

### "Prefill marketing form" is enabled on the contact record, but the form isn't prefilled

The "Prefill marketing form" attribute works only for legacy outbound marketing forms. Real-time journeys forms use the [Tracking purpose](real-time-marketing-email-text-consent.md#consent-to-track-user-behavior) as consent for prefill.

### Step-by-step troubleshooting

To enable form prefill, ensure that all the following requirements are correctly configured:

  1. Form prefill is enabled on domain settings level (in case the form is embedded into your own domain).
  2. Form prefill is enabled on a form level and for each field respectively.
  3. The end user who is opening a website with a form has provided tracking consent.
  4. The link that redirects to a prefilled form must be created as a Customer Insights - Journeys tracking link generated from a real customer journey (not from a test send). After clicking the tracking link, the URL must include the required tracking parameters, such as:
  `website_url/path#msdynmkt_trackingcontext=[some_guid]&msdynmkt_prefill=[some_text]`

[!INCLUDE [footer-include](./includes/footer-banner.md)]