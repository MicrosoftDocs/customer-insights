---
title: Roles and permissions
description: Overview of available roles and permissions for workspace members. 
ms.reviewer: mhart
ms.author: jusali
author: jusali
ms.date: 10/01/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Roles and permissions

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A workspace is where you store and manage events and reports. For more information, see [Create a workspace and add members](create-workspace.md). 

A workspace can include the following roles and permissions:

- *Member* roles are users who can access a workspace. You can assign members to your workspace and define their roles and permissions. 
- *Administrator* roles manage workspaces and environments an configure engagement insights for other users. 
- *Contributor* roles are geared towards analysts who don't not need to configure engagement insights but want to create their own reports, funnels, or segments.

## Permissions
  
The following table identifies permissions for each role. 

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
