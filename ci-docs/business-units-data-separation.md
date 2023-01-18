---
title: "Business unit data separatation and Role-based access control"
description: "Learn how to use buiness units in Customer Insights to separate data."
ms.date: 01/10/2023
ms.reviewer: mhart
ms.service: customer-insights
ms.topic: concept
author: jodahl-msft
ms.author: jodahl
manager: skumm
ms.custom: bap-template
---

# Business unit data separatation and Role-based access control
Business unit data separatation and Role-based access control (RBAC) allow administrators to regulate access to customer profiles, segments, and measures based on business units. Because these controls are applied to the data in Microsoft Dataverse, the integrity of those controls propagates to all other Dynamics 365 and Power Platform applications automatically.

## Customer Insights and Dataverse
Customer Insights populates Dataverse tables with data with ownership information, so that data consumption from Dataverse (e.g., in other Dynamics apps, such as Dynamics Marketing, model-driven apps, etc.) is governed by [Dataverse RBAC settings]([https://www.google.com](https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)). 



### Dataverse roles
Access to data in dataverse is governed by the ownership of the information and the Dataverse role of the user.

## Customer Insights roles

### The administrator role
Prepares data estate
Exports
Enrichments
Intelligence
### The BU contributor role

### Recommended roles setup
Admins need to be in top level BU

## Business unit ownership of customer profiles
Setting BU ownership on data and metadata

## Business unit ownership of segments and measures

## Customer Insights and Customer Journey Orchestration



## Next steps

[!INCLUDE [footer-include](includes/footer-banner.md)]
