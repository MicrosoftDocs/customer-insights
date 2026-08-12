---
title: Customer Insights - Journeys forms security and privacy
description: Learn about security and privacy protections for Customer Insights - Journeys forms, including reCAPTCHA setup and error troubleshooting.
ms.date: 08/11/2026
ms.topic: how-to
author: petrjantac
ms.author: alfergus
---

# Security and privacy for Customer Insights - Journeys forms

Microsoft builds its products based on strong security and privacy principles. Customer data belongs to the customer, and Microsoft protects it by design and by default throughout its lifecycle.

Customer Insights - Journeys forms treat security and privacy as core features. Microsoft protects all form data with encryption in transit and at rest, strong identity and access controls, and ongoing security validation. Microsoft regularly tests forms and related services through automated security checks, vulnerability scanning, and penetration testing as part of the Secure Development Lifecycle (SDL).

Customer Insights - Journeys forms align with global security and privacy standards. Customers stay in control of their data, and Microsoft processes personal data only for its intended purpose in a secure and transparent way.

This article applies to both marketing forms and event registration forms, unless differences are explicitly noted.

## Customer Insights - Journeys forms security

Security is an important aspect of marketing and event registration forms. Customer Insights - Journeys takes the following precautions to avoid any security risks:

- The Customer Insights - Journeys app accepts form submissions only from [domains allowed for external form hosting](domain-authentication.md). This security precaution applies for both forms and form capture.
- Forms can be rendered only on domains allowed for external form hosting.
- The out-of-the-box domain for forms hosted as a standalone page is enabled for external form hosting by default. Learn more: [Publish your form](real-time-marketing-form-create.md#publish-your-form).
- To avoid form submissions by bots, protect forms with a captcha. The form editor includes a reCAPTCHA option, but you can use any other third-party captcha. Learn more: [Customize form submission validation](real-time-marketing-form-customize-submission-validation.md).
- The Customer Insights - Journeys app infrastructure contains necessary precautions to minimize the consequences of a possible DDoS (Distributed Denial of Service) attack. Learn more: [Service protection and request limits](real-time-marketing-form-overview.md#service-protection-and-request-limits-for-marketing-forms).

### Protect forms from bots with reCAPTCHA

reCAPTCHA helps protect your forms from automated submissions and abuse by ensuring that responses come from real people. This protection preserves data quality and system reliability. For this reason, use reCAPTCHA on all publicly accessible forms.

To add reCAPTCHA to your form, go to the **Elements** section in the right pane, and then drag and drop the **reCAPTCHA** tile onto the canvas.

:::image type="content" source="media/real-time-marketing-form-add-recaptcha.png" alt-text="Screenshot of the reCAPTCHA element added to a form in the Customer Insights - Journeys form editor." lightbox="media/real-time-marketing-form-add-recaptcha.png":::

> [!IMPORTANT]
> To set up reCAPTCHA, enter the `Site key` and `Secret key` in the [default form configuration](real-time-marketing-form-global-settings.md#recaptcha).

#### HIP captcha removal

The earlier HIP captcha was removed from Customer Insights - Journeys forms in June 2026. reCAPTCHA replaced it to improve security, accessibility, and ease of use. Forms that used HIP captcha still work, but they have no bot protection until you add the reCAPTCHA element and republish them.

### Troubleshoot reCAPTCHA

For common reCAPTCHA configuration errors and how to resolve them, see [Troubleshoot reCAPTCHA issues in forms](/troubleshoot/dynamics-365/customer-insights/journeys/forms/troubleshoot-recaptcha).

## Customer Insights - Journeys forms privacy

- Marketing and event registration forms don't use any cookies by default. Form visit and form submit interactions use a [journey link tracking mechanism](real-time-marketing-link-tracking-mechanics.md) to get details about known users.
- The system uses cookies for tracking end users only when you turn on the **Web tracking** feature in Form settings. If you disable **Web tracking**, the system doesn't set any tracking cookies.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
