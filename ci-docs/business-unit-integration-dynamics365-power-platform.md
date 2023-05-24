---
title: "Customer Insights business unit integration with Dynamics 365 applications and Power Platform (preview)"
description: "Learn how to use business units with Dynamics 365 applications and Power Platform."
ms.date: 05/05/2023
ms.reviewer: mhart
ms.service: customer-insights
ms.topic: concept
author: jodahl
ms.author: jodahl
ms.custom: bap-template
---

# Customer Insights business unit integration with Dynamics 365 applications and Power Platform (preview)

## Customer Insights with Dynamics 365 Marketing

Customer Insights and Dynamics 365 Marketing are tightly integrated for a delightful activation journey.

Marketing contributors in Customer Insights should be given the *Marketing Professional (BU level)* role in Dataverse to govern their access to data from Dynamics 365 Marketing. In Dynamics 365 Marketing, they have access to customer profiles and segments that belong to their business unit. The *Marketing Professional (BU level)* role also needs to be granted to the business unit teams that the profiles are mapped to in the unification configuration. 

 > [!NOTE]
> Dynamics 365 Marketing can only process segments that contain members that belong to one business unit and has an owner that belongs to the same business unit.

## Customer Insights extensibility with Dataverse

Customer Insights writes data into Dataverse with ownership and role-based access controls for easy activation, for example, through [model-driven applications](/power-apps/maker/model-driven-apps/model-driven-app-overview). Dataverse lets organizations easily use data in model-driven apps for customer service, sales, and other business functions with the benefits of fine-grained permission controls.

Currently, business unit ownership from the associated customer profile is applied in Dataverse on the following tables: CustomerProfile, UnifiedActivity, SegmentMembership and CustomerMeasure. All records are assigned to the root business unit for the rest of the tables that are written to Dataverse.

## Customer Insights data consumption APIs

To maintain business unit data separation, all API based data consumption scenarios must call [Dataverse APIs](/power-apps/developer/data-platform/webapi/overview). Customer Insights APIs aren't supported for these scenarios.

[!INCLUDE [footer-include](includes/footer-banner.md)]
