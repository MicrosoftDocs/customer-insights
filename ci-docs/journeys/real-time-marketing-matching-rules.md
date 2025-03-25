---
title: Matching rules for Customer Insights - Journeys
description: Create custom matching rules to avoid creating duplicate records in forms and journeys.
ms.date: 03/17/2025
ms.topic: article
author: petrjantac
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Matching rules for forms and journeys

Maintaining a consistent customer database is crucial for business operations. Duplicate records can jeopardize this consistency. By using appropriate matching rules, you can ensure that existing lead and contact records are accurately updated. Matching rules can be applied in marketing and registration forms, and when creating new leads during a journey.

The list of all matching rules can be found in **Settings** > **Matching rules**.

## Create a new matching rule

Your custom matching rule can utilize multiple attributes of a lead or contact. For example, you can create a matching rule that updates an existing contact if both the email and phone number match the existing values.

To create a new matching rule:

1. Go to **Settings** > **Matching rules** and select **New** in the top ribbon.
1. Choose an intuitive name for your new rule. This name is used to select the rule when creating new forms or journeys.
1. Select the target entity, which can be a lead or contact.
1. Select the **Save** button. Your matching rule is created and you can now add **Matching Strategy Attributes**.
1. Select **Add Matching Strategy Attribute**.
1. Choose the attribute in the **Mapping** field and select **Save & Close**.
1. Repeat steps 5 & 6 to add more matching strategy attributes.
1. **Save** your matching rule.

:::image type="content" source="media/real-time-marketing-form-matching-strategy.png" alt-text="Create a new matching rule" lightbox="media/real-time-marketing-form-matching-strategy.png":::

 > [!TIP]
 > The **Match inactive records** toggle determines if inactive records are used for matching. Matching an inactive record doesn't reactivate the record. Inactive records have the same priority for matching as active ones. It's recommended to keep this toggle Off.

> [!IMPORTANT]
> If there's no existing record found by the matching rule, a new record is created. If there are multiple existing records found by the matching rule, the *latest updated* record is used.

## Matching existing records in marketing and registration forms

Matching rules can be used for both marketing and event registration form types. To prevent unexpected results, don't use empty values for matching. Make sure all form fields used for matching are set as required. All attributes used in the matching rule must be present in the form. Otherwise, the form publishing fails.

### Matching existing records using link tracking

When the existing user submitting a form is identified through [link tracking](real-time-marketing-link-tracking-mechanics.md) and the submitted values align with the matching rule, the existing record (contact or lead) identified by link tracking is updated.
If the submitted values do not align with the matching rule, the link tracking is not used, and the last modified record is updated.

:::image type="content" source="media/real-time-marketing-matching-tracking.png" alt-text="Matching a record with link tracking" lightbox="media/real-time-marketing-matching-tracking.png":::

### Matching existing records in lead & contact scenario

When the form submission targets the combined audience "Lead & Contact," there are separate matching rules for contacts and leads. The matching rule for contacts is applied first. If a child lead is found for the matched contact, the child lead is prioritized in the lead matching rule evaluation as long as the existing lead meets all the conditions defined in the lead matching rule. The Matching existing records using link tracking is also applied.

:::image type="content" source="media/real-time-marketing-matching-parent-contact.png" alt-text="Matching a record in lead with parent contact scenario" lightbox="media/real-time-marketing-matching-parent-contact.png":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]