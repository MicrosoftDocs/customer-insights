---
title: Roles and permissions
description: Overview of avaialable roles and permissions for workspace members. 
ms.reviewer: ruthai
ms.author: v-salash
author: pickwick129
ms.date: 10/23/2020
ms.service: customer-insights
ms.subservice: 
ms.topic: conceptual
ms.manager: shellyha
---

# Member roles

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]
You can assign members to your workspace and define their roles and permissions. The engagement insights capability supports **Environment admin** and **Workspace admin** roles.


## Permissions
  
The following chart identifies permissions for each role. 

| Permission | Environment admin | Workspace admin |
|--|--|--|
| Create environments (creator automatically becomes environment admin) | X* | X* |  |
| Configure environment (Add/remove environment members, delete environment) | X |  |  |
| Create workspaces | X |  |  |
| Configure workspaces (Add/remove workspace members, pre-defined reports, delete workspace) | X | X |  |
| Configure events and refined events | X | X |
| View workspace events and refined events | X | X |
| View workspace resources (reports, segments, and metric)| X | X |

*Can only create trial environments in preview. 

## Workspace administration

You can add and remove members from workspaces and environments. To access the Environment Members page, you need to be an environment admin of at least one environment. 

<!-- TODO - can we link this to the manage-workspace article and not duplicate the procedur? -->

### Manage workspace members

1. In the navigation pane, use the **Workspace picker** to select the workspace you want to work in.
1. Select **Admin** > **Settings** to access **Workspace Settings**.
1. Select **Members** and then **+Add members** to update members and assign roles.

<!-- TODO - create a new article to manage environments and link this there? I think it's in one of the drafts shared on 10/22 -->

### Manage environment members

1. In the navigation pane, select **Admin** > **Settings** to access **Workspace Settings**.
1. Select **General** and then **Go to admin center**.
1. Select the environment you want to work in and then select **Members** to update Environment administrators. 

