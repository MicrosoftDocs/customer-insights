---
title: Rename and delete a workspace
description: How to rename and delete a workspace
author: pickwick129
ms.reviewer: ruthai
ms.author: v-salash
ms.date: 10/26/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Environments and workspaces

## Overview

Environments and workspaces are used to store and manage your reports, events, and other data assets. An environment can contain one or more workspaces. Workspaces are used to manage your analytics and store your data like reports and events. 

### Environments

An environment is a space to manage your workspaces and manage connections to Dynamcis 365 Customer Insights audience insights. How you opt to use environments depends on your organization and the apps you're trying to build. 

For example: 
- Choose to have a single environment.
- Create separate environments for test and production.
- Create separate environments that correspond to specific teams or departments in your organization, containing the relevant events for each audience.
- Create separate environments for different global branches of your company.

### Workspaces 

A workspace is a space to store and manage events and reports. When you [create a workspace](create-workspace.md) you select what kind of data you will be sending the workspace. Currently, only web data is supported. Workspaces come with pre-defined reports and let you create custom reports using web metrics and dimensions.

## Manage a workspace

You can maintain multiple workspaces concurrently in an environment. You can rename existing workspaces, or delete them. 

To edit or delete a workspace, you have to select the workspace from the workspace switcher. 

:::image type="content" source="media/select-workspace.png" alt-text="Workspace switcher highlighted in engagement insights user interface":::

### Rename a workspace

1. Go to **Admin** > **Settings** > **General**.
1. In the **Workspace name** field, enter the new name.
1. Select **Save**.

:::image type="content" source="media/manage-workspace.png" alt-text="Rename or delete a workspace":::

### Delete a workspace

Deleting a workspace will permanently remove all of its content, data, settings, and permissions. It can't be undone.

1. Go to **Admin** > **Settings** > **General**.
1. Select **Delete Workspace**. 
1. In the **Delete workspace** dialog, enter **CONFIRM DELETE**. 
1. Select **Delete** to permanently delete the workspace
