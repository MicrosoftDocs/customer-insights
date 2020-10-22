---
title: Roles and permissions
description: An overview of the user roles and permissions available for public preview. 
ms.reviewer: ruthai
ms.author: v-salash
author: pickwick129
ms.date: 10/21/2020
ms.service: customer-insights
ms.subservice: 
ms.topic: conceptual
ms.manager: shellyha
---

# Member roles

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]
You can assign members to your workspace and define their roles and permissions. For public preview, engagement insights capability supports **Environment admin** and **Workspace admin** roles.


## Roles and permissions
  
The following chart identifies permissions for each role. 

| Role | Environment admin | Workspace admin |
|--|--|--|
| Create Environments (Creator automatically made Environment admin) | X* | X* |  |
| Configure Environment (Environment members, Delete)) | X |  |  |
| Create Workspaces | X |  |  |
| Configure Workspaces (Workspace members, Out-of-the-box (OOB) reports, Delete) | X | X |  |
| Configure Events and Refined Events | X | X |
| View Workspace Events and Refined events | X | X |
| View Workspace Resources (Reports, Segments, and Metric)| X | X |

*Can only create trial environments during public preview. 

## Workspace administration

You can add and remove members from workspaces and environments. To access the Environment Members page, you need to be an Environment Administrator of at least one Environment. 

To add and remove Workspace admin members
1. In the navigation pane, use the **Workspace picker** to select the workspace you want to work in.
1. Select **Admin** > **Settings** to access **Workspace Settings**.
1. Select **Members** and then **+Add members** to update members and assign roles.

To add and remove Environment admin members
1. In the navigation pane, select **Admin** > **Settings** to access **Workspace Settings**.
1. Select **General** and then **Go to admin center**.
1. Select the environment you want to work in and then select **Members** to update Environment administrators. 

