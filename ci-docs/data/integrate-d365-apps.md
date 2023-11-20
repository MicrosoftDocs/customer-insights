---
title: Integrate with Dynamics 365 applications (preview)
description: Learn how Customer Insights - Data can be used with other Dynamics 365 applications
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.topic: conceptual
ms.date: 11/20/2023
ms.custom: bap-template
---

# Integrate with Dynamics 365 applications (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Dynamics 365 customers can access more data and insights made available by the unified customer profile while working with a contact or lead. When unification is run, Customer Insights – Data creates a relationship from each contact or lead to the associated customer profile table by creating a standard Dataverse lookup column called CustomerID that links the records. From this link, you can view the details of a contact or lead and easily access the extended information and insights for that contact or lead from Customer Insights – Data.

To link contacts or leads to a unified customer profile, the contact or lead tables must be imported to Customer Insights – Data through the [Microsoft Dataverse connector](connect-dataverse.md) or the [Power Query Dataverse connector](connect-power-query.md) and [unified.](data-unification.md) Other data connector types will be supported in the upcoming months. When unification runs, a relationship is created between the Dataverse tables that were unified and the customer profile table. Contacts, leads, and other Dataverse records can natively reference their associated unified customer profile using the Dataverse relationship. In addition, the customer profile table provides relationships to [measures](measures.md) tables, making measures easily accessible.

Examples of using this native linking include:

- A sales team member viewing a lead can see additional information from the unified profile such as the customer lifetime value, lifetime purchases, churn risk, and other data. The team member can make better decisions on which leads to pursue and has access to data to help foster stronger relationships, knowing their customer’s interests, activity history, and insights. All of this information is accessible seamlessly in their contact/lead view.

- A marketing team can personalize email communications and thoughtfully branch a journey based on data in the unified profile, providing a distinct journey experience for customers based on data not previously available in Dynamics 365.

- Service reps can provide personalized service knowing the customer’s loyalty tier or prediction to churn.

[!INCLUDE [footer-include](includes/footer-banner.md)]
