---
title: About workspace and members
description: How to create a workspace and add members
author: pickwick129
ms.reviewer: ruthai
ms.author: v-salash
ms.date: 10/13/2020
ms.service: customer-insights
ms.subservice: 
ms.topic: conceptual
ms.manager: shellyha
---

# Workspaces and members

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A workspace is how you store and manage events and reports. When you create a workspace, you select the type of data you will send to the workspace. During public preview, engagement insights capability only supports web workspaces.

The workspace is where you can view user activity in real time. You can add members to an existing workspace at any time.

## Create a workspace

:::image type="content" source="media/workspace-switcher.png" alt-text="Customer insights page with callout on navigation pane and description":::

1. In the navigation pane, choose **+New workspace**. 

2. Enter a name for your workspace in the **Name** box and optionally add text in **Description**.

3. Choose **Create** to confirm and create the workspace.

## Add members

The **Members** page is where you can assign members to your workspaces, and define their roles and permissions.

:::image type="content" source="media/add-members.png" alt-text="Members page with callout on Add Members button":::

To add members to your workspace, follow these steps:

1. Go to **Admin** > **Settings** > **Members** and select **Add members**.

1. In the **Add members** pane, find the person that you want to add to the workspace. You can search by name or email address.

1. Choose the new member's **Role** from the drop-down list.

   > [!NOTE]
   > The only **Role** currently available is **Workspace admin**. Security groups and distribution groups are currently not supported.

1. When you are done adding members, select **Add members** to confirm.

### Member permissions

<!-- TODO - link to members article -->

**Workspace admin** is only role currently available. It has the following permissions enabled:

- Create projects
- Configure projects (members, delete)
- Configure events and refined events
- View project resources (reports)
