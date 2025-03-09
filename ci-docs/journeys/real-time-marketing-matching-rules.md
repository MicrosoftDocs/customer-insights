---
title: Matching rules Customer Insights - Journeys
description: Create custom matching rules to avoid creation of duplicate records in forms and journeys
ms.date: 03/09/2025
ms.topic: article
author: petrjantac
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Matching rules for forms and journeys

Maintaining a consistent customer database is crucial for business operations. Duplicate records can jeopardize this consistency. By using appropriate matching rules, you can ensure that existing records of leads or contacts are accurately updated. These matching rules can be applied in marketing and registration forms, as well as when creating new leads during a journey.

The list of all matching rules can be found in Settings -> Matching rules.

## Create a new matching rule

Your custom matching rule can utilize multiple attributes of a lead or contact. For example, you can create a matching rule that updates an existing contact if both the email and phone number match the existing values.

To create a new matching rule, navigate to Settings -> Matching rules, and select button New in the top ribbon.

Choose an intuitive name for your new rule, as this name will be used to select the rule when creating new forms or journeys. Select target entity, which can be lead or contact. Once you select the **Save** button, your matching rule will be created and you can access the **Rules** tab.

:::image type="content" source="media/real-time-marketing-create-matching-rule.png" alt-text="Create a new matching rule" lightbox="media/real-time-marketing-create-matching-rule.png":::

 > [!TIP]
 > The **Match inactive records** toggle determines if inactive records will be used for matching. Matching an inactive record does not reactivate the record. Inactive records have the same priority for matching as active ones. It is recommended to keep this toggle off.

You can define details of your matching rule in the **Rules** tab.



## Matching existing records in marketing and registration forms

tracking context