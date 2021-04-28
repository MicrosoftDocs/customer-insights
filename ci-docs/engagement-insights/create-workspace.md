---
title: Create a workspace and add members
description: How to create a first workspace and add members to it.
author: pickwick129
ms.reviewer: ruthai
ms.author: v-salash
ms.date: 11/11/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha
---

# Create the first workspaces and add members

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A workspace is how you can view user activity in real time to better understand your audience. It's where you store and manage events and reports.

When you create a workspace, you select the type of data that you want to focus on. You can add other users, or members, to an existing workspace at any time. During public preview, engagement insights capability only supports web workspaces.

## Create a workspace

The process of creating a workspace includes setting up the *environment* to organize your workspace. An environment is space that can contain one or more workspaces. You can use an environment to manage your workspaces and connections to Customer Insights audience insights capability.

:::image type="content" source="media/workspace-switcher.png" alt-text="Customer insights page with callout on navigation pane and description":::

1. Select **New workspace**.

1. Choose the type of environment you want, enter an **Environment name**, and select **Next**.

1. Enter a **Workspace name** and select **Next**.

1. Select **Finish** if you're done. 

1. If you want to add members to the workspace, enter a name in the **Members** box. You can search by name or email address.

1. Choose the new member's **Role** from the drop-down list. For more information, see [Roles and permissions](user-roles.md)

   > [!NOTE]
   > The only **Role** currently available is **Workspace admin**. Security groups and distribution groups are currently not supported.

1. Select **Next** and follow the instructions on the page to add data to your workspace.

1. Select **Done** when you're finished. 

## Add members

After you create a workspace, you can add members and define their roles and permissions on the **Members** page.

:::image type="content" source="media/add-members.png" alt-text="Members page with callout on Add Members button":::

To add members to your workspace

1. Go to **Admin** > **Workspace** > **Members** and select **Add members**.

1. In the **Add members** pane, find the person that you want to add to the workspace. You can search by name or email address.

1. Choose the new member's **Role** from the drop-down list. 

1. When you're done adding members, select **Add members** to confirm.

For more information, see [manage environments and workspaces](manage-environments-workspaces.md).

[!INCLUDE[footer-include](../includes/footer-banner.md)]
