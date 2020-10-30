---
title: Create a workspace and add members
description: How to create a first workspace and add members to it.
author: pickwick129
ms.reviewer: ruthai
ms.author: v-salash
ms.date: 10/30/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Workspaces and members

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A workspace is how you store and manage events and reports. When you create a workspace, you select the type of data you will send to the workspace. During public preview, engagement insights capability only supports web workspaces.

The workspace is where you can view user activity in real time. You can add members to an existing workspace at any time.

## Create a workspace

:::image type="content" source="media/workspace-switcher.png" alt-text="Customer insights page with callout on navigation pane and description":::

1. In the workspace selector, select **New workspace**. 

2. Enter a **Name** for the new workspace and optionally add a **Description**.

3. Select **Create** to confirm and create the workspace.

## Add members

The **Members** page is where you add members to your workspaces, and define their roles and permissions.

:::image type="content" source="media/add-members.png" alt-text="Members page with callout on Add Members button":::

To add members to your workspace, follow these steps:

1. Go to **Admin** > **Settings** > **Members** and select **Add members**.

1. In the **Add members** pane, find the person that you want to add to the workspace. You can search by name or email address.

1. Choose the new member's **Role** from the drop-down list. For more information, see [Roles and permissions](user-roles.md)

   > [!NOTE]
   > The only **Role** currently available is **Workspace admin**. Security groups and distribution groups are currently not supported.

1. When you are done adding members, select **Add members** to confirm.
