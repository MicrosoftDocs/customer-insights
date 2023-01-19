---
title: "Business unit data separatation and Role-based access control (Public preview)"
description: "Learn how to use buiness units in Customer Insights to separate data."
ms.date: 01/10/2023
ms.reviewer: mhart
ms.service: customer-insights
ms.topic: concept
author: jodahl
ms.author: jodahl
manager: skumm
ms.custom: bap-template
---

# Business unit data separatation and Role-based access control (Public preview)
Business unit data separatation and Role-based access control (RBAC) allow administrators to regulate access to customer profiles, segments, and measures based on business units. Because these controls are applied to the data in Microsoft Dataverse, the integrity of those controls propagates to all other Dynamics 365 and Power Platform applications automatically.

## Pre-requisites
* Business units and associated teams defined in Dataverse -> link to guide to setting up BUs in Dataverse.
* Business unit data separation is enabled by an admin in **Settings** > **System** > **Business unit data separation**. Notice that it is not possible to disable business unit data separation on an instance after it has been enabled. 

## Customer Insights and Dataverse
Customer Insights is an integrated part of the Microsoft Dynamics ecosystem, which means that it leverages the rich and expressive security model that is built into [Dataverse]([(https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)]). Access to data is determined by the intersection of the Dataverse role(s) the user has and the ownership of the data in question. In the following, both concepts are described in the Customer Insights context.

### Assignment of ownership
Every piece of data that is stored in Dataverse has an owner, which is critical to how access to this data is governed. When business data separation is enabled, both customer profiles, segments, and measures have ownership information attached to them as detailed below. 

#### Assignment of ownership to customer profiles
Ownership of the customer profiles is determined based on mappings that are configured in the Unify step:

1. Go to **Data** > **Unify** > **Business units**
2. Select the column that identifies the business unit for each entity that contributes to unification. 
3. Specify the mapping between the values in the columns that were selected above and business units. For example, 'US' maps to the US business unit, 'Mexico' maps to the Mexican business unit, etc.

Profiles will only be de-duplicated and unified if the business unit values match.

Profiles that do not match any of the mappings are assigned to the Org business unit.

#### Assignment of ownership to segments and measures

### Roles

#### Dataverse roles
Access to data in dataverse is governed by the ownership of the information and the Dataverse role of the user.

#### Customer Insights roles

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

## Activation scenarios

### Customer Insights and Customer Journey Orchestration

### 3rd party activation scenarios

![Example of a BU structure with the Org parent business unit at the top and child BUs A to D below](media/BU_structure_example.png)
*Example of a BU structure with the Org parent business unit at the top and child BUs A to D below*

## Next steps

## Limitations
A customer profile, segment, or measure has *one* BU as the owner. This means that if a customer is represented in data that spans more than one BU, then the customer 

Customer measures are not stored in Dataverse yet.

Only build your own segments and measures are supported.

When business unit data separation is enabled, Customer Insights populates Dataverse tables with data with ownership information, so that data consumption from Dataverse (e.g., in other Dynamics apps, such as Dynamics Marketing, model-driven apps, etc.) is governed by Dataverse RBAC settings.

[!INCLUDE [footer-include](includes/footer-banner.md)]
