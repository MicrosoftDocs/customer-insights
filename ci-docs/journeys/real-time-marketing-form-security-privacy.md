---
title: Customer Insights - Journeys forms security & privacy
description: Understand the security and privacy management of forms in Dynamics 365 Customer Insights - Journeys. 
ms.date: 02/03/2026
ms.update-cycle: 180-days
ms.topic: how-to
author: petrjantac
ms.author: alfergus
---

# Security and Privacy of Customer Insights - Journeys Forms

Security and privacy are foundational principles at Microsoft, built on the belief that customer data belongs to the customer and must be protected by design, by default, and throughout its entire lifecycle. Customer Insights - Journeys forms are designed with security and privacy as first‑class principles. All data collected through Customer Insights - Journeys forms is protected using Microsoft’s privacy‑by‑design and security‑by‑design practices, including encryption of data in transit and at rest, strong identity and access controls, and continuous security validation. Forms and their underlying services are regularly assessed through automated security testing, vulnerability scanning, and penetration testing as part of Microsoft’s Secure Development Lifecycle. Customer Insights - Journeys forms follow GDPR requirements and align with globally recognized security and privacy standards, ensuring that personal data is processed only for its intended purpose, remains under customer control, and is handled in a compliant, transparent, and secure manner throughout its lifecycle.

## Customer Insights - Journeys Forms Security

Security is an important aspect of marketing and event registration forms. Customer Insights - Journeys takes the following precautions to avoid any security risks:

- The Customer Insights - Journeys app accepts form submissions only from [domains allowed for external form hosting](domain-authentication.md). This security precaution applies for both forms and form capture.
- Forms can be rendered only on domains allowed for external form hosting.
- The out-of-box domain for forms hosted as a standalone page is enabled for external form hosting by default. Learn more: [Publish your form](real-time-marketing-form-create.md#publish-your-form)
- To avoid form submissions by bots, you should protect forms with a captcha. The form editor includes an out-of-the-box captcha option, but you can use any other third-party captcha service to improve the user experience. Learn more: [Integrate a custom captcha service with Customer Insights - Journeys forms](real-time-marketing-form-custom-captcha.md)
- The Customer Insights - Journeys app infrastructure contains necessary precautions to minimize the consequences of a possible DDoS attack. To prevent DDoS attacks, there's a limit of 2,000 requests/minute per org. The request limit includes visits, lookups, CAPTCHA, and form submissions. The limit allows around 100 to 500 submissions/minute, depending on the form.

### Protecting Forms from Bots with captcha

> [!IMPORTANT]
> To improve security, accessibility, and ease of use, the existing HIP captcha used in Customer Insights – Journeys (CI‑J) forms is being retired and replaced with a new reCAPTCHA experience.

#### HIP CAPTCHA Deprecation and New reCAPTCHA Experience

##### What’s changing

- The **HIP captcha** currently available in CI‑J forms will be **deprecated in March 2026** and fully **removed by June 30, 2026**.
- A new, improved reCAPTCHA experience is being introduced as the replacement.
- The new reCAPTCHA can be added to forms using the same drag‑and‑drop experience as the existing captcha—no developer involvement is required.

##### Why this change is happening

The new reCAPTCHA experience provides:

- Improved security against automated abuse
- Better accessibility and usability
- A simplified setup and authoring experience for form creators

This change ensures Customer Insights - Journeys forms continue to meet modern security and accessibility expectations.

##### Timeline and impact

**February 2026 release**

- The new reCAPTCHA becomes available in the Form Editor as a drag‑and‑drop element.
Administrators must complete a one‑time configuration by providing:
  - reCAPTCHA **Site key**
  - reCAPTCHA **Secret key**

- Once configured, form authors can add reCAPTCHA to forms without any additional setup.

> [!NOTE]
> If you configured reCAPTCHA before February 2026, you still need to enter the Site key in Form settings for the reCAPTCHA element in the Form Editor to work correctly.

> [!WARNING]
> In some cases, forms that were created using an earlier reCAPTCHA setup may not fully recognize the new drag‑and‑drop reCAPTCHA element. If this happens, remove the existing reCAPTCHA from the form and add it again using the reCAPTCHA element in the Form Editor.

**March 2026 release**

- The HIP captcha is removed from the Form Editor.
- Only reCAPTCHA can be added to:
  - New forms
  - Existing forms that are edited and republished

**By June 30, 2026**

- The HIP captcha is automatically removed from all forms, including:
  - Forms that haven’t been edited since the deprecation
  - Forms will continue to function without HIP captcha, but no bot protection will be applied unless reCAPTCHA is added.

##### What you need to do

**If you create or manage forms**

- Starting February 2026, use reCAPTCHA instead of HIP captcha for all new forms.
- Before June 30, 2026, update existing forms to include reCAPTCHA if bot protection is required.

**If you administer Customer Insights ‑ Journeys**

- Complete the one‑time reCAPTCHA configuration as soon as the February 2026 release is available.
- Share guidance with form authors about switching to reCAPTCHA.

##### Frequently asked questions

**Q: Will my existing forms stop working?**

- **A:** No. Existing forms will continue to work. However, once HIP captcha is removed (by June 30, 2026), forms that haven’t been updated will no longer have captcha protection unless reCAPTCHA is added.

**Q: Do I need to change form code or HTML?**

- **A:** No. The new reCAPTCHA is added through the Form Editor UI using drag‑and‑drop. No custom code or developer involvement is required. In some cases, you need to remove the old reCAPTCHA implementation by editing the HTML code.

**Q: Can I keep using HIP captcha after March 2026?**

- **A**: No. Starting in March 2026, HIP captcha will no longer be available in the Form Editor, and by June 30, 2026 it will be removed from all forms.

## Customer Insights - Journeys Forms Privacy

- Marketing and event registration forms don't use any cookies by default. Form visit and form submit interactions use a [journey link tracking mechanism](real-time-marketing-link-tracking-mechanics.md) to get details about known users.
- Cookies for tracking end users are used only when the **Web tracking** feature is turned on in Form settings. If Web tracking is disabled, no tracking cookies are set.
