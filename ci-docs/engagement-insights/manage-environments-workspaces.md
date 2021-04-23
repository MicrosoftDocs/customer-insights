---
title: Manage workspaces and environments
description: How to create, rename, and delete workspaces and environments.
author: pickwick129
ms.reviewer: mhart
ms.author: jusali
ms.date: 4/23/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha
---

# Manage environments and workspaces

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

## Overview

A workspace is a space to store and manage events and reports. It’s where you can view user activity in real time. When you create a workspace, you select the type of data to send to the workspace. Currently, only web data is supported.

An environment is a space where you manage your workspaces and connections. How you use environments depends on your organization and your use case.
For example, you can create:

-	A single environment.
-	Separate environments for test and production.
-	Separate environments for specific teams or departments in your organization that contain relevant events for each audience.
-	Separate environments for different global branches of your company.
-	Connections to Customer Insights audience insights capability.


## Choose an environment and create a workspace 

 Every workspace needs to be in an environment. You can select a pre-existing environment or make a new one when you create a workspace. Then you can choose to add workspace members and start collecting data.

To create your first workspace

1. In engagement insights, select **New** from the workspace switcher. 

:::image type="content" source="media/New-workspace.png" alt-text="Customer Insights page workspace picker":::

2. Choose an environment from the list or select **Create new environment**.
1. Enter a name in **Workspace name**. 
1. You can add members and assign their permission level from the **Role** list. Then select **Finish** to create the workspace or **Next** to install code. 
1. Install the code snippet to start receiving data and then select **Done**. 



## Manage a workspace

You can maintain multiple workspaces concurrently in an environment. Your  [role](user-roles.md)  determines how you can work in them. 

 - As a Workspace admin, you can rename existing workspaces or delete them. 
 - You must be an Environment admin or a Workspace admin to manage the workspace.

### Edit a workspace name

1. Go to **Admin** > **Workspace** > and select **Settings**.

1. In the **Workspace name** box, enter a new name.

1. Select **Save** to apply your changes.

### Delete a workspace

Deleting a workspace will permanently remove all of its content, data, settings, and permissions. It can't be undone.

1. Go to **Admin** > **Workspace** > and select **Settings**.

1. Select **Delete Workspace**. 

1. In the **Delete workspace** dialog, enter **CONFIRM DELETE**. 

1. Select **Delete** to permanently delete the workspace.

### Manage workspace members

1. Go to **Admin** > **Workspace** > and select **Members**.

1. Select **Add members** to give access and [assign roles](user-roles.md). Currently, only **Workspace admin** is available.

1. If you set up a [connection to audience insights](configure-connections.md), you can select **Allow access to profile data** to allow the member to see reports based on [user profiles](profile-reports.md).

1. Select **Add members** to add them to your workspace.

## Manage an environment

As an Environment admin, you can access an environment from the left navigation pane. You can configure environment settings, other Environment admins, workspaces, and [connections to audience insights](configure-connections.md). Select tabs to move between different areas in the admin center.


:::image type="content" source="media/New-environment.png" alt-text="Environment admin center":::

### Configure an environment

At this time, you must first select a workspace that belongs to the environment. 
 - Go to **Admin** > **Environment**.

### Rename an environment

1. Go to **Admin** > **Environment** > and select **Settings**.

1. Update the **Environment name** and select **Save** to apply your changes.



### Manage environment members

1. Go to **Admin** > **Environment** > and select **Members**.

1. Select **Add members** to update members and [assign roles](user-roles.md). Currently, only **Environment admin** is available.

1. If you set up a [connection to audience insights](configure-connections.md), you can select  **Allow access to profile data** to allow the member to see reports based on [user profiles](profile-reports.md).

1. Select **Add members** to add them to your environment.

## Manage connections

Establishing connections to audience insights lets you see reports in engagement insights based on unified customer profiles. 

For more information, see [Configure connections](configure-connections.md).

## Manage personal data

To protect your customer's personal data, you can delete or export end-user identifiable data.

For more information, see [Delete and export event data containing personal information](delete-export-personal-data.md).


[!INCLUDE[footer-include](../includes/footer-banner.md)]
