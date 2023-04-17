---
title: "Business unit data separation and Role-based access control (Public preview)"
description: "Learn how to use buiness units in Customer Insights to separate data."
ms.date: 01/10/2023
ms.reviewer: mhart
ms.service: customer-insights
ms.topic: concept
author: jodahl
ms.author: jodahl
ms.custom: bap-template
---

# Business unit (BU) data separation and Role-based access control (Public preview)
Business unit data separation and Role-based access control (RBAC) allow administrators to regulate access to customer profiles, segments, and measures based on business units. [Learn more about business units and role-based access control in Dataverse](https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds).

## Prerequisites
* Business units and associated teams are defined in Dataverse. [Learn more about setting up business units in Dataverse.](https://learn.microsoft.com/en-us/power-platform/admin/create-edit-business-units) 
* Users are assigned to appropriate business units and teams. [Learn more about managing users and teams in Dataverse.](https://learn.microsoft.com/en-us/power-platform/admin/users-settings)
* Business unit data separation is enabled by an admin in **Settings** > **System** > **Business unit data separation**. 
* All data sources that contribute to unification must have a column that holds a value that identifies the business unit for every row of data. 
* A B2C Customer Insights (Individual customers) environment.

> [!NOTE]
   > * B2B (Business accounts) environments are not supported.
   > * It is not possible to disable business unit data separation on an environment after it has been enabled. 

## Access controls in Customer Insights

### Customer profiles, activities, customer measures, intelligence, enrichments
Access to a customer profile in Customer Insights is governed by which business unit team owns the profile and the Customer Insights role of the user. The *Administrator*, *Contributor*, and *Viewer* roles have access to all profiles regardless of owning business unit team. The *Marketing contributor* role has access only to customer profiles that belong to their business unit.

Note that the *Marketing contributor* role has access to only Segments (*build your own*) and Measures (*build your own*) in the Customer Insights user interface. [Learn more about user roles in Customer Insights](https://learn.microsoft.com/en-us/dynamics365/customer-insights/permissions)

> [!NOTE]
   > * The **administrator** and **contributor** roles are highly privledged and **should only be given to users that belong to the *Root* business unit**. They have access to all data, segments, measures, etc. regardless of business unit ownership and all functionality of Customer Insights. These users are typically responsible for preparing the data estate, i.e., setting up data sources, business unit data separation rules, unification rules, enrichments, intelligence models etc.
   > * The **viewer** role is not bound by business unit and should not be used in production if business unit data separation is enabled.

Ownership of the customer profiles is determined based on mappings that are configured in the Unify step:

1. Go to **Data** > **Unify** > **Business units**
2. Under **Business unit data separation**, select the column that identifies the business unit for each entity that contributes to unification. Note that additional unification rules cannot be added on the selected columns.
3. Under **Associate customer profiles with business units**, specify the mapping between the values in the columns that were selected above and business unit teams (Only teams that have the *Customer Insights Data Read Access* role are available for selection). For example, 'A' maps to the business unit A team, 'B' maps to the business unit B team, etc. 

![Screenshot of business unit mappings](media/BU_mappings.png)
*Screenshot of business unit mapping.*

Customer profiles are owned by teams within business units (as opposed to being owned by business units directly) to provide better control of data access. Only one team per business unit can be specified in the mapping rules. 

* Profiles will only be de-duplicated and unified if the business unit values match. 
* Profiles that do not match any of the mappings are assigned to the *Org* business unit.
* All profiles are assigned to the *Org* business unit if business unit data separation is not enabled.
* A profile belongs to exactly one business unit.
* The unification rules and customer profile schema are the same for all business units.

 > [!NOTE]
   > * Any changes to the BU data separation configuration will trigger a full refresh. If your instance is in incremental mode, then a [full refresh](https://learn.microsoft.com/en-us/dynamics365/customer-insights/incremental-refresh-data-sources#run-a-one-time-full-refresh-for-azure-data-lake-data-sources) needs to be triggered manually after changes have been made.
   
Data that are tied to a customer profile, for example, activities, customer measures, intelligence output, and enrichments inherit the business unit ownership from the associated profile. 

Intelligence models are trained on all data, i.e., no business unit data separation is enforced on training data. 

## Default configurations
A typical business unit structure is depicted below. Marketing contributor users have access only to customer profiles that are owned by their business unit team. For example, if a marketing contributor user creates a segment with all customers, then it will only contain the customers that are owned by the business unit that the Marketing contributor belongs to. All other Customer Insights roles have access to all customer profiles in Customer Insights regardless of owning business unit.


![Example of a business unit structure with the Org parent business unit at the top and child business units A to D below](media/BU_structure_example_Root.png)
*Example of a business unit structure with the Org parent business unit at the top and child business units A to D below*
### Segments and business measures
Segments and measures are owned by the business unit of the user that created them. For example, if a user is member of business unit *A* then any segment and measure that user creates is owned by business unit *A*. Access is controlled by the RBAC settings on the segments definitions and measures definitions tables in Dataverse. The default setting is that segments and measures can be seen, edited, and deleted by other users that belong to the same business unit.

> [!NOTE]
   > * Segments and measures cannot be owned by more than one business unit nor be shared with other business units.
   > * Only *build your own* segments and measures (no projected attributes) are supported for the Marketing contributor role.
   > * Segments and Business measures are not stored in Dataverse yet.
   > * Projected attributes are not supported for the marketing contributor role.

## Access Customer Insights data in Dataverse
Customer Insights is an integrated part of the Microsoft Dynamics ecosystem, which means that it leverages the rich and [expressive security model that is built into Dataverse](https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds). 

### Dataverse security roles
To access any data from Customer Insights in Dataverse, the user needs to have the *Customer Insights Data Read Access* security role in Dataverse. This role cannot be modified. If different access is needed, for example, access to all profiles irrespectively of business unit you can create a custom role and assign it.

[Learn more about Dataverse security roles.](https://learn.microsoft.com/en-us/power-platform/admin/database-security)

### Dataverse teams
To access data from Customer Insights, the user needs to be member of one of the teams that were specified in the business unit mapping step. Note, that a user can only belong to a team that belongs to the same business unit as the user.

[Learn more about how to assign users to teams.](https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds#teams-including-group-teams)


[!INCLUDE [footer-include](includes/footer-banner.md)]
