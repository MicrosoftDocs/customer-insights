---
title: Create a new workspace
description: The purpose of a workspace and how to create a new one.
author: jusali
ms.reviewer: mhart
ms.author: jusali
ms.date: 10/01/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha
---

# Create a new workspace and add members

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A workspace is how you can view user activity in real time to better understand your audience. It's where you store and manage events and reports.

When you create a workspace, you select the type of data that you want to focus on. You can add other users, or members, to an existing workspace at any time. 

## Create a new workspace

The process of creating a workspace includes setting up the *environment* to organize your workspace. An environment is space that can contain one or more workspaces. You can use an environment to manage your workspaces and connections to Customer Insights audience insights capability.

1. Select **New** from the workspace switcher.

   :::image type="content" source="media/new-workspace.png" alt-text="Customer insights page with callout on navigation pane and description.":::

1. In the **Workspace** pane, enter a **Workspace name**.

   :::image type="content" source="media/workspace-name.png" alt-text="Type a workspace name.":::

1. Choose the platform type (Web or mobile) that you want to measure.

1. Select **Show advanced settings** to enable or disable these optional settings:

   - Toggle **Unknown to known** to "enabled" to associate web events with users who previously authenticated. For more information, see [Recognize web events from previously authenticated visitors](unknown-to-known.md)
   - Toggle **Filter bot traffic** to "enabled" to remove web traffic by bots for this workspace. 

1. Select **Complete** when you're done. 

1. Install the code snippet to start receiving data, and then select **Finish** to create the workspace. For more information, see [Developer resources overview](developer-resources.md).

> [!NOTE]
> You can now add members and assign their permission level from the **Role** list. For more information, see [Roles and permissions](user-roles.md). 

For more information, see [Manage environments and workspaces](manage-environments-workspaces.md).


[!INCLUDE[footer-include](../includes/footer-banner.md)]
