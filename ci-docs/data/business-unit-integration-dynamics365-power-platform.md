---
title: Customer Insights business unit integration with Dynamics 365 applications and Power Platform (preview)
description: "Learn how to use business units with Dynamics 365 applications and Power Platform."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.service: customer-insights
ms.topic: article
author: jodahl
ms.author: jodahl
ms.custom: bap-template
---

# Customer Insights business unit integration with Dynamics 365 applications and Power Platform (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

## Customer Insights - Data with Customer Insights - Journeys

Dynamics 365 Customer Insights - Data and Customer Insights - Journeys are tightly integrated for a streamlined activation journey.

Marketing contributors in Customer Insights - Data should get the *Marketing Professional (BU level)* role in Dataverse to govern their access to data from Dynamics 365 Customer Insights - Journeys. In Customer Insights - Journeys, they have access to customer profiles and segments that belong to their business unit. The *Marketing Professional (BU level)* role also needs to be granted to the business unit teams that the profiles are mapped to in the unification configuration.

> [!NOTE]
> Customer Insights - Journeys can only process segments that contain members that belong to one business unit and has an owner that belongs to the same business unit.

## Extensibility with Dataverse

Customer Insights - Data writes data into Dataverse with ownership and role-based access controls for easy activation, for example, through [model-driven applications](/power-apps/maker/model-driven-apps/model-driven-app-overview). Dataverse lets organizations easily use data in model-driven apps for customer service, sales, and other business functions with the benefits of fine-grained permission controls.

Currently, business unit ownership from the associated customer profile is applied in Dataverse on the following tables: CustomerProfile, UnifiedActivity, SegmentMembership and CustomerMeasure. All records are assigned to the root business unit for the rest of the tables that are written to Dataverse.

## Data consumption APIs

To maintain business unit data separation, all API based data consumption scenarios must call [Dataverse APIs](/power-apps/developer/data-platform/webapi/overview). Customer Insights APIs aren't supported for these scenarios.

## Next steps

- [Business unit support and role-based access control (preview)](business-units-data-separation.md)
- [Data and security roles in Dataverse (preview)](access-business-units-dataverse.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
