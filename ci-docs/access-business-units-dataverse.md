---
title: "Access Customer Insights data in Dataverse (preview)"
description: "Learn how to use business units in Dataverse applications to separate data."
ms.date: 01/10/2023
ms.reviewer: mhart
ms.service: customer-insights
ms.topic: concept
author: jodahl
ms.author: jodahl
ms.custom: bap-template
---

# Access Customer Insights data in Dataverse

Customer Insights is an integrated part of the Microsoft Dynamics ecosystem, which means that it leverages the rich and [expressive security model that is built into Dataverse](https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds). 

### Dataverse security roles
To access any data from Customer Insights in Dataverse, the user needs to have the *Customer Insights Data Read Access* security role in Dataverse. This role cannot be modified. If different access is needed, for example, access to all profiles irrespectively of business unit you can create a custom role and assign it.

[Learn more about Dataverse security roles.](https://learn.microsoft.com/en-us/power-platform/admin/database-security)

### Dataverse teams
To access data from Customer Insights, the user needs to be member of one of the teams that were specified in the business unit mapping step. Note, that a user can only belong to a team that belongs to the same business unit as the user.

[Learn more about how to assign users to teams.](https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds#teams-including-group-teams)