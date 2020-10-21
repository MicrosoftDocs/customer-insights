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

A workspace is how you group data and reports in Dynamics 365 Customer Insight engagement insights capability. It's where you can view user activity in real time. You can add members to an existing project at any time. 

## Create a workspace

1. In the navigation pane, choose **+New workspace**. 

2. Enter a name for your workspace in the **Name** box and optionally add text in **Description**.

3. Choose **Create** to confirm and create the workspace.


## Add members

The **Members** page is where you can assign members to your workspaces, and define their roles and permissions.

:::image type="content" source="media/add-members.png" alt-text="Members page with callout on Add Members button":::

To add members to your workspace, follow these steps:

1. In the navigation pane, choose **Settings** > **Members**, and then select **+Add members**.

2. In the **Members** box, enter the name of the person that you want to add to the workspace. You can search by name or email address.

   > [!NOTE]
   > The only **Role** currently available is **Owner**. Security groups and distribution groups are currently not supported.

3. When you are done adding users, choose **Add members** to confirm.

### Member permissions
**Owner** is only role currently available. It has the following permissions enabled:

- Create projects
- Configure projects (members, delete)
- Configure events and refined events
- View project resources (reports)
