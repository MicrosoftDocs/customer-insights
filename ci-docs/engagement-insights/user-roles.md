---
title: Roles and permissions
description: Overview of available roles and permissions for workspace members. 
ms.reviewer: mhart
ms.author: jusali
author: jusali
ms.date: 06/09/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Roles and permissions

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A workspace is how you store and manage events and reports. A member is a user who can access a workspace. You can assign members to your workspace and define their roles and permissions. Engagement insights capability supports **Environment** and **Workspace admin** roles and **Environment** and **Workspace contributor** roles. The contributor roles are geared for an analyst who does not need to configure Engagement Insights.

## Permissions
  
The following chart identifies permissions for each role. 

| Permission | Environment admin | Workspace admin | Environment contributor | Workspace contributor | 
|--|--|--|--|--|
| Create environments (creator automatically becomes environment admin) | X* | X* | X* | X* |  
| Configure environment (environment members, delete environment) | X |  |  |  |  
| Create workspaces | X |  |  |  |  
| Configure workspaces (workspace members, delete workspace) | X | X |  |  |  
| Configure events and refined events | X | X | |  |  
| View workspace events and refined events | X | X | |  |  
| View workspace resources (reports, segments, and metric)| X | X | X | X |  
| Create custom reports and funnels | X | X | X | X |  
| Create base metrics and dimensions| X | X |  |  |  
| Create segments| X | X | X | X |  

*Can only create trial environments in preview. 

## Add members

You can add and remove members from workspaces and environments. For more information, see [Environments and workspaces](manage-environments-workspaces.md).


[!INCLUDE[footer-include](../includes/footer-banner.md)]
