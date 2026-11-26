---
title: How contact point consent normalization works for email and phone
description: Learn how contact point consent normalization works for email and phone in Customer Insights - Journeys. Use these tips to keep cloud flows and imports consistent.
ms.date: 10/22/2026
ms.topic: concept-article
author: petrjantac
ms.author: udag
search.audienceType:
  - admin
  - customizer
ai-usage: ai-assisted
---

# How contact point consent normalization works for email and phone

Contact point consent normalization helps Customer Insights - Journeys find consent for email addresses and phone numbers written in different ways. For consent, Customer Insights - Journeys treats `Megan.Bowen@Contoso.com` and `megan.bowen@contoso.com` as the same email address, and `+1 (425) 555-0100` and `+14255550100` as the same phone number. To help journeys find consent for the right destination, Customer Insights - Journeys stores the email address or phone number in contact point consent records in a standard form. This process is called normalization. Normalization changes only the value stored in contact point consent records. It doesn't change the email and phone fields on contact records.

This article explains when normalization runs, how each channel is normalized, and what to keep in mind when you create contact point consent records with a Power Automate cloud flow, custom code, or a data integration tool.

## When normalization runs

Email addresses and phone numbers are normalized when a contact point consent record is created through the standard Dataverse create operation. When a journey sends an email or a text message, the recipient's email address or phone number is normalized the same way before consent is checked. If the value can't be normalized, consent is checked against the value as provided.

Contact point consent records that you create through Customer Insights - Journeys forms, preference centers, the consent center, and the **Communication** tab on contact records are normalized automatically, as long as the value can be normalized. Records that you create through the standard Dataverse create operation, for example by using the **Add a new row** action of the Microsoft Dataverse connector in a Power Automate cloud flow, are normalized automatically, too.

## How each channel is normalized

| Channel | How the value is normalized | Example |
|---|---|---|
| Email | Leading and trailing spaces and any display name are removed, and the address is converted to lowercase. | `"Megan Bowen" <Megan.Bowen@Contoso.com>` is stored as `megan.bowen@contoso.com`. |
| Text message and voice | Spaces, parentheses, and hyphens are removed, and the number is stored as `+` followed by its digits. The number must start with `+` or an international dialing prefix (`00`, `010`, or `011`), which is replaced by `+`. It must contain 4 to 20 digits, including any dialing prefix, and can contain only digits, spaces, parentheses, hyphens, and `+`. | `+1 (425) 555-0100` and `0014255550100` are both stored as `+14255550100`. |
| Custom channel | The value isn't changed. It's stored exactly as provided. | `Device-ABC` is stored as `Device-ABC`. |

## Values that can't be normalized

If an email address or phone number can't be normalized, a create request through the standard Dataverse create operation fails with **Invalid email address** or **Invalid phone number**, and the contact point consent record isn't saved. For example, a phone number that doesn't start with `+` or an international dialing prefix, such as `4255550100`, is rejected by the standard Dataverse create operation. On a [form](real-time-marketing-manage-forms.md) whose phone number field doesn't use the **Phone number** validation, a number in an incompatible format doesn't stop the submission, but no contact point consent record is created for it.

A national phone number that starts with `00`, `010`, or `011` isn't rejected. Those digits are read as an international dialing prefix, so the wrong number is stored. To avoid errors and wrong numbers, always provide phone numbers in international format with `+` and the country code.

## Create records without bypassing normalization

Normalization runs as part of the standard Dataverse create operation for the contact point consent table. If you create contact point consent records with custom code, a data integration tool, or a [cloud flow](consent-record-creation.md), don't bypass synchronous custom business logic, for example with the `BypassBusinessLogicExecution` optional parameter set to a value that includes `CustomSync`, or with the `BypassCustomPluginExecution` optional parameter. Records created that way can keep the value as provided.

> [!IMPORTANT]
> Because journeys look up email and text message consent by the normalized value, consent stored in records that weren't normalized might not be found, and the contact point is treated as if it has no consent record for that purpose or topic. Depending on the [consent enforcement model](real-time-marketing-compliance-settings.md#consent-enforcement-models), this can mean that an opt-out isn't honored, or that a message isn't sent because the opt-in isn't found.

## Fix records that weren't normalized

Updating the contact point value of an existing contact point consent record isn't supported. To fix records that were saved without normalization, re-create them through the standard create operation. Check with your privacy counsel before you re-create consent records.

1. Export the records. The new records have a new creation date and might show a different source, so keep the export if you need a history of when and how consent was given.
1. Check that each value is a valid email address or a phone number in international format, and correct it if it isn't, so the new record points to the right destination.
1. If two old records normalize to the same value with different consent statuses, decide which status is current.
1. Re-create each record through the standard create operation with the same channel, purpose or topic, business unit, and consent status, and delete the old record. The order depends on the stored value:
    - If the stored value differs from the normalized value only in letter case or trailing spaces, delete the old record first, because it blocks the new one. Until the new record exists, the contact point has no consent record for that purpose or topic, so do this while no journeys are sending to it.
    - Otherwise, create the new record before you delete the old one.

This article describes product behavior and isn't legal advice. Validate your consent design with your own privacy counsel.

## See also

- [Consent management overview](real-time-marketing-compliance-settings.md)
- [Create a consent record using a cloud flow](consent-record-creation.md)
- [Manage consent for email, SMS (text), voice, and custom channel messages](real-time-marketing-email-text-consent.md)
