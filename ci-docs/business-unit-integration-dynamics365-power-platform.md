---
title: "Customer Insights business unit integration with Dynamics 365 applications and Power Platform (preview)"
description: "Learn how to use business units with Dynamics 365 applications and Power Platform."
ms.date: 01/10/2023
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

Marketing contributors in Customer Insights should be given the *Marketing Professional (BU level)* role in Dataverse to govern their access to data from Dynamics 365 Marketing. In Dynamics 365 Marketing they'll only have access to customer profiles and segments that belong to their business unit.

 > [!NOTE]
> Dynamics 365 Marketing can only process segments that contain members that belong to one business unit and has an owner that belongs to the same business unit.

## Customer Insights extensibility with Dataverse

Customer Insights writes data into Dataverse with ownership and RBAC properties for easy activation, for example, through [model-driven applications](/power-apps/maker/model-driven-apps/model-driven-app-overview). Using model-driven applications, data can easily be used in Customer Service, Sales, and other business functions with the benefits of fine-grained RBAC controls.

Currently, business unit ownership from the associated customer profile is applied in Dataverse on the following tables: CustomerProfile, UnifiedActivity, SegmentMembership and CustomerMeasure. All records are assign to the root business unit for the rest of the tables that are written to Dataverse.

## Customer Insights data consumption APIs

To maintain business unit data separation, all API based data consumption scenarios must call [Dataverse APIs](/power-apps/developer/data-platform/webapi/overview). Customer Insights APIs are not supported for these scenarios.

[!INCLUDE [footer-include](includes/footer-banner.md)]
