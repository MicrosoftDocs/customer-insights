---
title: Manage workspaces and environments
description: How to create, rename, and delete workspaces and environments.
author: jusali
ms.reviewer: mhart
ms.author: jusali
ms.date: 10/01/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha
---

# Manage environments and workspaces

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

## Overview

This topic discusses how to manage workspaces and environments once they've already been created. 

- A *workspace* is a space to store and manage events and reports. It’s where you can view user activity in real time. When you create a workspace, you select the type of data to send to the workspace. Currently, web data and mobile apps are supported. For more information, see [Create a new workspace and add members](create-workspace.md).

- An *environment* is a space where you manage your workspaces and connections. For more information, see [Create a new environment](create-new-environment.md).

## Manage an existing workspace

You can maintain multiple workspaces concurrently in an environment. Your [role](user-roles.md) determines how you can work in them. 

 - You must be an environment admin or a workspace admin to manage the workspace.
 - As a workspace admin, you can rename existing workspaces or delete them. 

:::image type="content" source="media/workspace-edit.png" alt-text="Workspace admin center.":::

### Edit a workspace name

1. Go to **Admin** > **Workspace** and select **Settings**.

1. In the **Workspace name** box, enter a new name.

1. Select **Save** to apply your changes.

### Delete a workspace

Deleting a workspace permanently removes all of its content, data, settings, and permissions. It can't be undone.

1. Go to **Admin** > **Workspace** and select **Settings**.

1. Select **Delete workspace**. 

1. In the **Delete workspace** dialog, enter **CONFIRM DELETE** in all caps. 

1. Select **Delete** to permanently delete the workspace.

### Manage workspace members

1. Go to **Admin** > **Workspace** and select **Members**.

1. Select **Add members** to give access and [assign roles](user-roles.md). Currently, only **Workspace admin** is available.

1. Select **Add members** to add them to your workspace.

## Manage an existing environment

As an environment admin, you can access an environment from the left navigation pane. You can configure environment settings, other environment admins, and workspaces. Select tabs to move between different areas in the admin center.

:::image type="content" source="media/environment-edit.png" alt-text="Environment admin center.":::



<!-- editor's comment: Suggest changing the following heading to "Edit an environment name" to follow the pattern set above with workspaces. -->


### Rename an environment

1. Go to **Admin** > **Environment** and select **Settings**.

1. Update the **Environment name** and select **Save** to apply your changes.



<!-- editor's comment: Switch the order of Manage and Delete to be consistent with the order of the workspace procedures above. -->


### Manage environment members

1. Go to **Admin** > **Environment** and select **Members**.

1. Select **Add members** to update members and [assign roles](user-roles.md). Currently, only **Environment admin** is available.

1. Select **Add members** to add them to your environment.

### Delete an environment

Environment admins can delete environments. Before you can delete an environment, you must remove all workspaces under it.

1. Go to **Admin** > **Environment** and select **Settings**.

1. Select **Delete environment**. 

1. In the **Delete workspace** dialog, enter **CONFIRM DELETE** in all caps. 

1. Select **Delete** to permanently delete the environment.

## Manage connections

Establishing connections to audience insights lets you see reports in engagement insights based on unified customer profiles. 

For more information, see [Create a link between audience insights and engagement insights](integrate-audience-insights-engagement-insights.md).

## Manage personal data

To protect your customer's personal data, you can delete or export end-user identifiable data.


<!-- editor's comment: On the following link, you have to scroll way down on the linked page to get to that subject. I thought I was on the wrong page at first. But I couldn't figure out how to link directly to that subject. Maybe it would be helpful to say "For more information, see the section "Deleting and exporting event data containing end user identifiable information" in [Data Subject Rights (DSR) requests under GDPR](xxxxx).  --> 


For more information, see [Delete and export event data containing personal information](delete-export-personal-data.md).


[!INCLUDE[footer-include](../includes/footer-banner.md)]
