---
title: Manage workspaces and environments
description: How to create, rename, and delete a workspaces and environments.
author: pickwick129
ms.reviewer: ruthai
ms.author: v-salash
ms.date: 12/11/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha
---

# Manage environments and workspaces

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

## Overview

A workspace is a space to store and manage events and reports. When you create a workspace, you select the type of data to send to the workspace. Currently, only web data is supported.

An environment is a space where you manage your workspaces and connections. How you use environments depends on your organization and your use case.

For example, you can create:

- A single environment.
- Separate environments for test and production.
- Separate environments that correspond to specific teams or departments in your organization, containing the relevant events for each audience.
- Separate environments for different global branches of your company.
- Connections to Customer Insights audience insights capability.

## Connect your data

 When you set up your first workspace in engagement insights, you'll need to set up a connection to create a workspace and start to receive data.

To create your first workspace

1. In engagement insights, select **Connect your data** to start the wizard. 

:::image type="content" source="media/banner.png" alt-text="Customer Insights page with connect your data button":::

2. Choose the type of activity that you want to measure in a new workspace. Currently, only **Website activity** is available. **App activity** and **Device activity** will become available in future releases.

1. Select **Next** to confirm and create the workspace.

1. Add a code snippet to your website to start receiving data in engagement insights. You can implement this right away or share the code and instructions with your website admin. To find the code snippet later, go to **Admin**>**Data**> **Code**.

   > [!IMPORTANT]
   > Data will not show in the workspace until the code has been implemented on your website.

1. Select **Done** to open your new workspace.  


## Manage a workspace

You can maintain multiple workspaces concurrently in an environment. As a workspace admin, you can rename existing workspaces, or delete them. 

To edit, delete, or switch between workspaces, select the workspace from the workspace switcher.

:::image type="content" source="media/select-workspace.png" alt-text="Workspace switcher highlighted in engagement insights user interface":::

### Edit a workspace

1. Go to **Admin** > **Settings** > **General**.

1. In the **Workspace name** box, enter a new name and optionally add a **Description** for your workspace.

1. Select **Save** to apply your changes.

### Delete a workspace

Deleting a workspace will permanently remove all of its content, data, settings, and permissions. It can't be undone.

1. Go to **Admin** > **Settings** > **General**.

1. Select **Delete Workspace**. 

1. In the **Delete workspace** dialog, enter **CONFIRM DELETE**. 

1. Select **Delete** to permanently delete the workspace.

### Manage workspace members

1. Go to **Admin** > **Settings** > **Members**.

1. Select **Add members** to update members and [assign roles](user-roles.md). Currently, only **Workspace admin** is available.

1. Select the check box if you want **Allow access to profile data**. This selection enables the member to see reports based on user profiles if you set up the [connection to audience insights](configure-connections.md).

1. Select **Add members** to add them to your workspace.

## Manage an environment

The admin center lets you manage engagement insights environments. It currently includes options to configure general settings, other environment admins, workspaces, and [connections to audience insights](configure-connections.md).

To access the environment admin center, you need to have an environment admin role.

Switch between the different areas in the admin center by selecting the corresponding tabs.

:::image type="content" source="media/environment-admin-center-tabs.png" alt-text="Environment admin center with callout on tabs":::

### Choose the environment to configure

1. Go to **Admin** > **Settings** > **General**.

1. Select **Go to admin center**.

   :::image type="content" source="media/open-admin-center.png" alt-text="Highlight on link to go to the admin center":::

1. To change an environment, select **Environments** in the navigation pane.

1. In the list, select the environment you want to configure.

### Rename an environment

1. Go to **Admin** > **Settings** > **General**.

1. Select **Go to admin center**.

1. Select **General**.

1. Update the **Environment name** and select **Save** to apply your changes.

### Manage environment members

1. Go to **Admin** > **Settings** > **General**.

1. Select **Go to admin center**.

1. Select **Members**.

1. Select **Add members** to update members and [assign roles](user-roles.md). Currently, only **Environment admin** is available.

1. Select the check box if you want **Allow access to profile data**. This selection enables the member to see reports based on user profiles if you set up the [connection to audience insights](configure-connections.md).

1. Select **Add members** to add them to your environment.

### Manage workspaces

1. Go to **Admin** > **Settings** > **General**.

1. Select **Go to admin center**.

1. Select **Workspaces**.

1. Select **...** next to the workspace name and choose one of the available options:
   - Choose **Edit name** to change the name of a workspace.
   - Choose **Delete** to remove a workspace.

### Manage connections

Establishing connections to audience insights lets you see reports in engagement insights based on unified customer profiles. 

For more information, see [Configure connections](configure-connections.md).

### Manage personal data

To protect your customer's personal data, you can delete or export end user identifiable data.

For more information, see [Delete and export event data containing personal information](delete-export-personal-data.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]