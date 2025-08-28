---
title: Matching rules for Customer Insights - Journeys
description: Create custom matching rules to avoid creating duplicate records in forms and journeys.
ms.date: 08/26/2025
ms.topic: how-to
author: petrjantac
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Matching rules for forms and journeys

Maintaining a consistent customer database is crucial for business operations. Duplicate records can jeopardize this consistency. By using appropriate matching rules, you can ensure that existing lead and contact records are accurately updated. Matching rules can be applied in marketing and registration forms, and when creating new leads during a journey.

Find all matching rules in **Settings** > **Matching rules**.

## Create a new matching rule

Your custom matching rule can utilize multiple attributes of a lead or contact. For example, you can create a matching rule that updates an existing contact if both the email and phone number match the existing values.

To create a new matching rule:

1. Go to **Settings** > **Matching rules**, and select **New** in the top ribbon.
1. Enter a name for your new rule. This name is used to select the rule when creating new forms or journeys.
1. Select the target entity, which can be a lead or contact.
1. Select the **Save** button. The matching rule is created, and you access it in the **Conditions** tab.

:::image type="content" source="media/real-time-marketing-create-matching-rule.png" alt-text="Create a new matching rule" lightbox="media/real-time-marketing-create-matching-rule.png":::

 > [!TIP]
 > The **Match inactive records** toggle determines if inactive records are used for matching. Matching an inactive record doesn't reactivate the record. Inactive records have the same priority for matching as active ones. It's recommended to keep this toggle Off.

Define the details of your matching rule in the **Conditions** tab.

### Define matching conditions

The matching rule builder consists of three parts:

- **Summary**: A human language interpretation of the logic created by your rules.
- **Main condition**: The main condition is always executed first to gather a group of the most relevant records. The main rule is a direct query to database, so the degree of match is always *Exact* (it isn't possible to set up fuzzy matching). You can add multiple attributes to the main condition. There's always an **OR** operator between the attributes of the condition.
- **Additional conditions**: Additional conditions are executed on the group of records filtered out by the main condition. You can add multiple attributes to every additional condition. There's always an **OR** operator between the attributes of the rule. You can create multiple additional conditions. All conditions are linked by an **AND** operator. You can set the **Degree of match**, which defines if an exact match (100%) is required or what extent of fuzzy match is applied. The possible degrees of match are:
  - **Exact**: All characters must match.
  - **High**: Almost all characters must match.
  - **Medium**: At least half of the characters must match.
  - **Low**: At least 25 % of characters must match.
- You can build complex matching rules by combining multiple conditions with various attributes.

:::image type="content" source="media/real-time-marketing-define-matching-rule.png" alt-text="Define your matching rule" lightbox="media/real-time-marketing-define-matching-rule.png":::

#### Example 1: Update the existing record if email AND phone match

Use `emailaddress1` as the attribute in the main condition. Add an additional condition with the `mobilephone` attribute.

:::image type="content" source="media/real-time-marketing-define-matching-rule-and-example.png" alt-text="Matching rule with email address and phone number" lightbox="media/real-time-marketing-define-matching-rule-and-example.png":::

**Result:** The existing lead or contact record is updated if the email address and phone number match the values stored in the record.

#### Example 2: Update the existing record if email OR phone match

Use `emailaddress1` as the attribute in the main condition. Add `mobilephone` as an additional attribute to the same condition.

:::image type="content" source="media/real-time-marketing-define-matching-rule-or-example.png" alt-text="Matching rule with email address or phone number" lightbox="media/real-time-marketing-define-matching-rule-or-example.png":::

**Result:** The existing lead or contact record is updated if the email address or phone number match the values stored in the record.

> [!IMPORTANT]
> If the matching rule doesn't find an existing record, a new record is created. If the matching rule finds multiple existing records, the latest updated record is used.

## Matching existing records in marketing and registration forms

Matching rules can be used for marketing and event registration form types. To prevent unexpected results, don't use empty values for matching. Make sure all form fields used for matching are set as required. All attributes used in the matching rule must be present in the form, otherwise, the form publishing fails.

### Matching existing records using link tracking

When an existing user submits a form and is identified through [link tracking](real-time-marketing-link-tracking-mechanics.md), and the submitted values match the matching rule, the existing record (contact or lead) identified by link tracking is updated. If the submitted values don't match the matching rule, link tracking isn't used, and the last modified record is updated.

:::image type="content" source="media/real-time-marketing-matching-tracking.png" alt-text="Diagram that shows matching a record with link tracking." lightbox="media/real-time-marketing-matching-tracking.png":::

### Matching existing records in a "Lead & Contact" scenario

When the form submission targets the combined audience "Lead & Contact," separate matching rules apply for contacts and leads. The matching rule for contacts is applied first. If a child lead is found for the matched contact, the child lead is prioritized in the lead matching rule evaluation if the existing lead meets all the conditions defined in the lead matching rule. Link tracking is also considered in the matching process.

:::image type="content" source="media/real-time-marketing-matching-parent-contact.png" alt-text="Diagram that shows matching a record in a lead with parent contact scenario." lightbox="media/real-time-marketing-matching-parent-contact.png":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]
