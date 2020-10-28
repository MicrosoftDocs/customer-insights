---
title: Roles and permissions
description: Overview of available roles and permissions for workspace members. 
ms.reviewer: ruthai
ms.author: v-salash
author: pickwick129
ms.date: 10/26/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Roles and permissions

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

You can assign members to your workspace and define their roles and permissions. The engagement insights capability supports **Environment admin** and **Workspace admin** roles.

## Permissions
  
The following chart identifies permissions for each role. 

| Permission | Environment admin | Workspace admin |
|--|--|--|
| Create environments (creator automatically becomes environment admin) | X* | X* |  |
| Configure environment (environment members, delete environment) | X |  |  |
| Create workspaces | X |  |  |
| Configure workspaces (workspace members, pre-defined reports, delete workspace) | X | X |  |
| Configure events and refined events | X | X |
| View workspace events and refined events | X | X |
| View workspace resources (reports, segments, and metric)| X | X |

*Can only create trial environments in preview. 

## Add members

You can add and remove members from workspaces and environments. For more information, see [Environments and workspaces](manage-environments-workspaces.md).
