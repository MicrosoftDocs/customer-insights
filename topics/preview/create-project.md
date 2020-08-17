---
title: Create a project
author: ruthaisabokhae
description: How to create a project in Dynamics 365 Product Insights
ms.author: ruthai
ms.date: 07/31/2020
ms.service: product-insights
ms.topic: conceptual
robots: noindex,nofollow
---

# Create a project

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

To create a new project, follow these steps:

1. Select **+New Project** in the lower-left corner of the portal.

2. Enter your project's **Name** and an optional **Description** text.

3. Select **Create** to confirm and create the project.

## Add members

The **Members** page is where you'll assign members to your projects, and define their roles and permissions.

:::image type="content" source="media/add-members.png" alt-text="Members page with callout on Add Members button":::

To add members to your project, follow these steps:

1. Select **Settings** > **Members**, and then select **+Add members**.

2. Use the **Members** field to find users who you want to add to your team. You can search by name or email address. Under **Role**, the only currently available option is **Owner**.

   > [!NOTE]
   > Security groups and distribution groups are currently not supported.

3. When you are done adding users, select **Add** to confirm.

### Member permissions

Product Insights has only the role of **Owner** currently available, with the following permissions enabled:

- Create projects
- Configure projects (members, delete)
- Configure events and refined events
- View project resources (reports)
