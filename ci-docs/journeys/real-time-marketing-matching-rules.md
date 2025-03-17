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
1. Select the **Save** button. Your matching rule is created and you can access it in the **Rules** tab.

:::image type="content" source="media/real-time-marketing-create-matching-rule.png" alt-text="Create a new matching rule" lightbox="media/real-time-marketing-create-matching-rule.png":::

 > [!TIP]
 > The **Match inactive records** toggle determines if inactive records are used for matching. Matching an inactive record doesn't reactivate the record. Inactive records have the same priority for matching as active ones. It's recommended to keep this toggle Off.

You can define details of your matching rule in the **Rules** tab.

### Define matching rules

The matching rule builder consists of three parts:

- **Summary**: A human language interpretation of the logic created by your rules.
- **Main rule**: The main rule is always executed first to gather a group of the most relevant records. The main rule is a direct query to database, so the degree of match is always 100% (it isn't possible to set up fuzzy matching). You can add multiple attributes to the main rule. There's always an "OR" operator between the attributes of the rule.
- **Additional rules**: Additional rules are executed on the group of records filtered out by the main rule. You can add multiple attributes to every additional rule. There's always an "OR" operator between the attributes of the rule. You can create multiple additional rules. All rules are linked by an "AND" operator. You can set the "Degree of match," which defines if an exact match (100%) is required or what extent of fuzzy match is applied.

:::image type="content" source="media/real-time-marketing-define-matching-rule.png" alt-text="Define your matching rule" lightbox="media/real-time-marketing-define-matching-rule.png":::

> [!IMPORTANT]
> If there's no existing record found by the matching rule, a new record is created. If there are multiple existing records found by the matching rule, the *latest updated* record is used.

## Matching existing records in marketing and registration forms

Matching rules can be used for both marketing and event registration form types.

The following are important considerations for matching evaluation:

- When the existing user is identified through tracking (the tracking context can be used to find the right contact or lead ID) and the submitted values align with the matching rule, the existing user identified by tracking is updated.
- When the form submission targets the combined audience "Lead & Contact," there are separate matching rules for contacts and leads. The matching rule for contacts is applied first. If a child lead is found for the matched contact, the child lead is prioritized in the lead matching rule evaluation as long as the existing lead meets all the conditions defined in the lead matching rule.
- To prevent unexpected results, don't use empty values for matching. Make sure all form fields used for matching are set as required.
- All attributes used in the matching rule must be present in the form. Otherwise, the form publishing fails.

[!INCLUDE [footer-include](./includes/footer-banner.md)]