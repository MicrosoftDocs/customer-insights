---
title: "Business unit data separation and Role-based access control (Public preview)"
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

# Business unit data separation and Role-based access control (Public preview)
Business unit (BU) data separation and Role-based access control (RBAC) allow administrators to regulate access to customer profiles, segments, and measures based on business units. Because these controls are applied to the data in Microsoft Dataverse, the integrity of those controls propagates to all other Dynamics 365 and Power Platform applications automatically.

## Prerequisites
* Business units and associated teams are defined in Dataverse -> link to guide to setting up BUs in Dataverse.
* Users are assigned to appropriate business units and teams -> link to guide to managing users and teams in Dataverse.
* Business unit data separation is enabled by an admin in **Settings** > **System** > **Business unit data separation**. Notice that it is not possible to disable business unit data separation on an instance after it has been enabled. 
* All data sources that contribute to unification must have a column that holds a value that identifies the business unit for every row. 

## Customer Insights and Dataverse
Customer Insights is an integrated part of the Microsoft Dynamics ecosystem, which means that it leverages the rich and expressive security model that is built into [Dataverse]([(https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)]). Access to data is determined by the intersection of the Dataverse role(s) the user has, the teams they belong to, and the ownership of the data in question. In the following, these concepts are described in the Customer Insights context.

### Assignment of ownership
Every piece of data that is stored in Dataverse has an owner, which is critical to how access to this data is governed. When business data separation is enabled, both customer profiles, segments, and measures have ownership information attached to them as detailed below. 

#### Assignment of ownership to customer profiles
Ownership of the customer profiles is determined based on mappings that are configured in the Unify step:

1. Go to **Data** > **Unify** > **Business units**
2. Select the column that identifies the business unit for each entity that contributes to unification. 
3. Specify the mapping between the values in the columns that were selected above and business unit teams. For example, 'A' maps to the A business unit team, 'B' maps to the B business unit team, etc. 

Customer profiles are owned by teams within business units (as opposed to being owned by business units directly) to provide better control of data access.   

 > [!NOTE]
   > * Profiles will only be de-duplicated and unified if the business unit values match. 
   > * Profiles that do not match any of the mappings are assigned to the Org business unit.
   > * Profiles belong to exactly one business unit.
   > * The unification rules are the same for all business units.

#### Assignment of ownership to segments and measures
Ownership of segments and measures is determined based on the user that created them. For example, if a user is member of the US business unit then any segment and measure that user creates is owned by the US business unit. At this time it is not possible to assign segments nor measures to other business units.

### Roles and teams
Apart from ownership, the other components of determining access to data in Dataverse are the user's Dataverse role(s) and the teams they belong to.  

#### Dataverse roles
To have access to any data from Customer Insights, the user needs to have the *Customer Insights Data Reader* role in Dataverse. This role is assigned automatically to users that has any Customer Insights role as detailed below. 

Click here for more information on Dataverse roles.

#### Dataverse teams
To have access to any data from Customer Insights, the user needs to be member of one of the teams that were specified in the business unit mapping step. Note, that a user can only belong to a team that belongs to the same business unit as the user.

Click here for more information on how to assign users to teams in Dataverse.

## Default business unit configurations
The default configuration is depicted below, where members of the Org business unit has access to all customer profiles, segments, and measures. Members of the other business units only have access to the customer profiles, segments, and measures that belong to their business unit. 

![Example of a BU structure with the Org parent business unit at the top and child business units A to D below](media/BU_structure_example.png)
*Example of a BU structure with the Org parent business unit at the top and child BUs A to D below*

 > [!NOTE]
   > * Only the default configurations are currently supported. Altering RBAC settings in Dataverse can lead to unexpected results.

## Customer Insights roles
The Customer Insights roles determine the user's access to Customer Insights functionality.

### The administrator role
The administrator role has access to all of Customer Insights, including all customer profiles, segments, and measures regardless of the user's business unit. 
This role can:

* Prepare data estate by configuring data sources and unification.
* Create segments and measures.
* Configure enrichments and intelligence.
  * Outputs of enrichments and ML models are tied to the customer profiles. Therefore, the outputs inherit the business unit ownership from the profiles.  
* Configure exports
* Manage Customer Insights users

 > [!NOTE]
   > * This is a highly privledged role.
   > * This role should only be grated to users that belong to the *Org* business unit.

### The contributor role
The contributor role has the same rights as the administrator role except that it cannot manage Customer Insights users.

 > [!NOTE]
   > * This is a highly privledged role.
   > * This role should only be grated to users that belong to the *Org* business unit.

### The BU contributor role
When business unit data separation is enabled, it is the responsibility of the administrators and/or contributors on the *Org* level to prepare the data state. The BU contributor role is given to users that belong to the child business units. This role can:

* Create segments
* Create measures

This role can only access customer profiles that belong to their BU and any child BUs. For example, if a BU contributor creates a segment with all customers then it will only contain the customers that are owned by the BU that the BU contributor belongs to.

With the default Dataverse RBAC settings, this role can only see segments and measures that belong to the same business unit as the user belongs to.

### The viewer role
The viewer role can view all data regardless of the user's business unit, but it cannot make any changes. This role is primarily meant for demo scenarios.

## Activation scenarios

### Customer Insights and Customer Journey Orchestration

### 3rd party activation scenarios


## Next steps

## Limitations
A customer profile, segment, or measure has *one* BU as the owner. This means that if a customer is represented in data that spans more than one BU, then the customer 

* Only build your own segments and measures are supported.

* Synonyms in the BU mappings are not supported.

* Customer measures are not stored in Dataverse yet.

* 
When business unit data separation is enabled, Customer Insights populates Dataverse tables with data with ownership information, so that data consumption from Dataverse (e.g., in other Dynamics apps, such as Dynamics Marketing, model-driven apps, etc.) is governed by Dataverse RBAC settings.

[!INCLUDE [footer-include](includes/footer-banner.md)]
