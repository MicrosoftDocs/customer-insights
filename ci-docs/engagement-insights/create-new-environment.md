---
title: Create a new environment
description: The purpose of an environment and how to create a new one.
author: jusali
ms.reviewer: mhart
ms.author: jusali
ms.date: 10/04/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha
---

# Create a new environment 

## Overview

An environment is a space where you manage your workspaces and connections. How you use environments depends on your organization and your use case. For example, you can create:

- A single environment.
- Separate environments for test and production.
- Separate environments for specific teams or departments in your organization that contain relevant events for each audience.
- Separate environments for different global branches of your company.
- Connections to Customer Insights audience insights capability.

## Create a new environment

1. On the right side of the main banner, select the environment picker, and then **+New**.

   :::image type="content" source="media/environment-picker.png" alt-text="Select the environment picker.":::

1. In the **Setup** pane, type an **Environment name**.

   :::image type="content" source="media/new-environment.png" alt-text="Specify the environment details.":::

1. Choose the **Type** of account, depending upon your plan type.

1. Choose the **Region** and select **Next**. 

1. Type a **Workspace name**, which enables you to collect data for specific website or apps. For more information, see [Create a workspace](create-workspace.md).

1. Choose the **Workspace type** (Web or Mobile) that you want to create. 

1. Select **Show advanced settings** to enable or disable these optional settings:

   - Toggle **Unknown to known** to "enabled" to associate web events with users who previously authenticated. For more information, see [Recognize web events from previously authenticated visitors](unknown-to-known.md)
   - Toggle **Filter bot traffic** to "enabled" to remove web traffic by bots for this workspace. 

1. Select **Complete** when you're done. 

1. Install the code snippet to start receiving data, and then select **Finish** to create the workspace. For more information, see [Developer resources overview](developer-resources.md).

> [!NOTE]
> You can now add members and assign their permission level from the **Role** list. For more information, see [Roles and permissions](user-roles.md). 

For more information, see [Manage environments and workspaces](manage-environments-workspaces.md).

## Work with your new environment

- [Create a workspace](engagement-insights/create-workspace.md) and add members.
- [Add code to your website](engagement-insights/instrument-website.md) or [mobile app](engagement-insights/developer-resources.md#capture-events-from-mobile-apps).
- View a [real-time report](engagement-insights/view-reports.md) or create [custom reports](engagement-insights/custom-reports.md).
- [Create refined events](engagement-insights/refined-events.md) for export.
- [Export the data](engagement-insights/export-events.md) to Data Lake Storage.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
