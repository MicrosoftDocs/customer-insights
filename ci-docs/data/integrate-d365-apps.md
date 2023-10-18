---
title: Integrate with Dynamics 365 applications (preview)
description: Learn how Customer Insights - Data can be used with other Dynamics 365 applications
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.topic: conceptual
ms.date: 10/18/2023
ms.custom: bap-template
---

# Integrate with Dynamics 365 applications (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

You can easily use unified data, measures, and other insights from Customer Insights - Data in Dynamics 365 applications.

When you import and unify customer data from Dataverse and other sources, the unification process appends a new lookup column called CustomerID on the Dataverse tables. This lookup column creates a relationship to the unified Customer profile table, allowing contacts, leads, and other Dataverse records to natively reference their associated unified customer profile. In addition, the customer profile table has relationships to measure tables, making measures easily accessible.

Examples of using this native linking include:

- Marketing teams can personalize the experience of customers with segments and dynamic content based on their lifetime value, irrespective of where they are on the buying journeys and whether they’re targeted as a lead or a contact.

- Sales and account reps can win more deals and foster stronger relationships, knowing their customer’s interests, activity history, insights such as churn risk or predictions such as propensity to buy—all accessible seamlessly in their contact/lead view.

- Service reps can provide personalized service knowing the customer’s loyalty tier or prediction to churn.

## Limitations

- Only Dataverse tables imported through the Microsoft Dataverse connector or the Power Query Dataverse connector are supported.

- Only the customer profile table attributes and measure tables attributes are supported.
