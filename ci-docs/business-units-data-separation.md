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

# Business unit (BU) data separation and Role-based access control (Public preview)
Business unit (BU) data separation and Role-based access control (RBAC) allow administrators to regulate access to customer profiles, segments, and measures based on business units. Because these controls are applied to the data in Microsoft Dataverse, the integrity of those controls propagates to all other Dynamics 365 and Power Platform applications automatically.

A new role in Customer Insights, *Marketing contributor*, allows the administrator to grant a user access to only the customer profiles that belong to the business unit of the user. This role only has access to the *segments* and *measures* areas of Customer Insights.

## Prerequisites
* Business units and associated teams are defined in Dataverse -> [guide to setting up BUs in Dataverse.](https://learn.microsoft.com/en-us/power-platform/admin/create-edit-business-units) 
* Users are assigned to appropriate business units and teams -> [guide to managing users and teams in Dataverse.](https://learn.microsoft.com/en-us/power-platform/admin/users-settings)
* Business unit data separation is enabled by an admin in **Settings** > **System** > **Business unit data separation**. Notice that it is not possible to disable business unit data separation on an instance after it has been enabled. 
* All data sources that contribute to unification must have a column that holds a value that identifies the business unit for every row. 

## Access controls in Customer Insights
Data flows from upstream systems into Customer Insights, where it is processed. The processed data are then saved to Dataverse for activiation scenarios. The following details how access is controlled along this journey.

### Customer profiles, activities, customer measures, intelligence, enrichments
Access to a customer profile in Customer Insights is governed by which business unit owns the profile and the Customer Insights role of the user. The *Administrator* and *Contributor* roles have access to all profiles regardless of owning business unit. The *Marketing contributor* and *Viewer* roles only have access to customer profiles that belong to their business unit.

> [!NOTE]
   > * The **administrator** and **contributor** roles are highly privledged and **should only be given to users that belong to the *Org/Root* business unit**.

Ownership of the customer profiles is determined based on mappings that are configured in the Unify step:

1. Go to **Data** > **Unify** > **Business units**
2. Under **Business unit data separation**, select the column that identifies the business unit for each entity that contributes to unification. Note that additional unification rules cannot be added on these columns.
3. Under **Associate customer profiles with business units**, specify the mapping between the values in the columns that were selected above and business unit teams. For example, 'A' maps to the business unit A team, 'B' maps to the business unit B team, etc. 

![Screenshot of business unit mappings](media/BU_mappings.png)
*Screenshot of business unit mapping.*

Customer profiles are owned by teams within business units (as opposed to being owned by business units directly) to provide better control of data access. Only one team per business unit can be specified in the mapping rules. 

* Profiles will only be de-duplicated and unified if the business unit values match. 
* Profiles that do not match any of the mappings are assigned to the *Org* business unit.
* All profiles are assigned to the *Org* BU if BU data separation is not enabled.
* Profiles belong to exactly one business unit.
* The unification rules and customer profile schema are the same for all business units.

 > [!NOTE]
   > * Any changes to the BU data separation configuration will trigger a full refresh.
   
Data that are associated with a customer profile, e.g., activities, customer measures, intelligence output, and enrichments inherit the business unit ownership from the associated profile.
  
### Segments and business measures




## Customer Insights and Dataverse
Customer Insights is an integrated part of the Microsoft Dynamics ecosystem, which means that it leverages the rich and [expressive security model that is built into Dataverse](https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds). Access to data in Dataverse is determined by the intersection of the Dataverse role(s) the user has, the teams they belong to, and the ownership of the data in question. In the following, these concepts are described in the Customer Insights context.

### Assignment of ownership
Every piece of data that is stored in Dataverse has an owner, which is critical to how access to this data is governed. Both customer profiles, segments, and measures have ownership information attached to them as detailed below. 

#### Ownership of customer profiles


Access to customer profiles *within* Customer Insights is determined based on the business unit of the user and the owning business unit of the customer profile: Users have access to all customer profiles that belong to their business unit and any child business units.

#### Ownership of segments and business measures
Ownership of segments and measures is determined based on the user that created them. For example, if a user is member of business unit *A* then any segment and measure that user creates is owned by business unit *A*. 

#### Ownership of activities, enrichments, intelligence, and customer measures
Activities, enrichments, intelligence, and customer measures are tied to customer profiles, so they inherit the same owner as the associated customer profile.

Intelligence models are trained on all data, i.e., no business unit data separation is enforced on training data. 

### Roles and teams
Apart from ownership, the other components of determining access to data in Dataverse are the user's Dataverse role(s) and the teams they belong to.  

#### Dataverse security roles
To access any data from Customer Insights in Dataverse, the user needs to have the *Customer Insights Data Reader* security role in Dataverse. This role is assigned automatically to users that have any Customer Insights role. 

Click here for more information on [Dataverse security roles.](https://learn.microsoft.com/en-us/power-platform/admin/database-security)

#### Dataverse teams
To access data from Customer Insights, the user needs to be member of one of the teams that were specified in the business unit mapping step. Note, that a user can only belong to a team that belongs to the same business unit as the user.

Click here for more information on how to assign users to [teams.](https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds#teams-including-group-teams)

## Default configurations
An example of the default RBAC configuration is depicted below, where members of the Org business unit has access to all customer profiles, segments, and measures. Members of the child business units only have access to the customer profiles, segments, and measures that belong to their business unit and any child business units. For example, if a user creates a segment with all customers, then it will only contain the customers that are owned by the BU that the Marketing contributor belongs to and child business units. 

![Example of a BU structure with the Org parent business unit at the top and child business units A to D below](media/BU_structure_example.png)
*Example of a BU structure with the Org parent business unit at the top and child BUs A to D below*

 > [!NOTE]
   > * Only the default table configurations are currently supported. Altering RBAC settings in Dataverse can lead to unexpected results.

Customer profiles are not directly owned by business units - instead they are owned by teams as discussed above. This ensures more flexibility in how access control can be managed within business units. Note that only one team per business unit can be specified in the mapping rules.  

## Customer Insights roles 
The Customer Insights roles determine the user's access to Customer Insights functionality. Click [here](https://learn.microsoft.com/en-us/dynamics365/customer-insights/permissions) for more general and detailed information.

The **administrator** and **contributor** roles are highly privledged and **should only be given to users that belong to the *Org/Root* business unit**. These users are typically responsible for preparing the data estate, i.e., setting up data sources, business unit data separation rules, unification rules, enrichments, etc. 

The **marketing contributor** role leverages the data estate to create segments and measures, and activates those, for example, in Customer Journey Orchestration. This role has access to the following in Customer Insights:

* Segments (only *build your own*)
* Measures (only *build your own*)

The marketing contributor can only create measures on tables that have a relationship path to the customer profiles.

The **viewer** role has access to all parts of customer insights but it cannot make any changes. 

## Customer Insights and Customer Journey Orchestration
Customer Insights and Customer Journey Orchestration (CJO) are tightly integrated for a delightful activation journey. 

Marketing contributors in Customer Insights should be given the *Marketing Professional (BU level)* role in Dataverse to govern their access to data from Customer Journey Orchestration. When they go to CJO they will only have access to customer profiles and segments that belong to their business unit or child business units.

 > [!NOTE]
   > * Customer Journey Orchestration can only process segments that containt members that belong to one business unit and has an owner that belong to the same business unit.

## Customer Insights and Dataverse
Customer insights writes data into Dataverse with ownership and RBAC properties for easy activation, for example, through [model-driven applications](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-driven-app-overview). Using model-diven applications, data can easily be leveraged in customer service, sales, operations, and other business functions with the benefits of fine-grained RBAC controls.

## Notes

 > [!NOTE]
   > * A customer profile cannot be owned by more than one business unit. At the cost of a higher profile count, an additional global instance can be used if customers have business with more than one business unit and it is imperative to unify across business units. 
   > * Segments and measures cannot be owned by more than one business unit nor be shared with other business units.
   > * Synonyms in the BU mappings are not supported, i.e., the string that identifies the business unit must be idential for the same business unit - otherwise they will be parsed as different business units.
   > * Only *build your own* segments and measures are supported for the Marketing contributor role.
   > * Segments and Business measures are not stored in Dataverse yet.
   > * Modernized business units is not supported.


[!INCLUDE [footer-include](includes/footer-banner.md)]
