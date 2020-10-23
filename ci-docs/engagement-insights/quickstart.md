---
title: Quickstart product introduction 
description: First-run experience for the product
author: pickwick129
ms.reviewer: ruthai
ms.author: v-salash
ms.date: 10/23/2020
ms.service: customer-insights
ms.subservice: 
ms.topic: conceptual
ms.manager: shellyha
---

# First run experience

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

This article explains how to sign up and do an initial setup of engagement insights, a capability of Dynamics 365 Customer Insights.

## Sign up for a demo of engagement insights

You must have an active  Microsoft Azure Active Directory user account. 
1. Open the [engagement insights capability](https://pi.dynamics.com/) website. 

1. Sign in with your school or work account.

1. Select your region, and use the check box to indicate whether you want to opt in to receive updates and offers via email.

1. Review the **engagement insights (preview) Terms of Use** and **Privacy Statement**, and select **Explore the demo** to accept them.

1. Explore the product using a set of sample data. 

## Set up your first workspace in engagement insights

You can use the setup wizard to connect your own data.

1. In engagement insights, select **Connect your data** to start the wizard. 

:::image type="content" source="media/connect-your-data.png" alt-text="Customer Insights page with connect your data button":::

1. Choose the type of activity that you want to measure in a new workspace. Currently, only **Website activity** is available. **App activity** and **Device activity** will become available in future releases.

1. Select **Next** to confirm and create the workspace.

1. You must add a code snippet to your website to start receiving data in engagement insights. You can implement this right away or share the code and instructions with your website admin. To find the code snippet later, go to **Admin**>**Data**> **Code**.

   > [!IMPORTANT]
   > Data will not show in the workspace until the code has been implemented on your website.

1. Select **Done** to open your new workspace. 

## Add members to an existing workspace

By default, only the person who created the workspace has access to it. You can add other users from your organization to an existing workspace at any time.

:::image type="content" source="media/add-members.png" alt-text="Members page with callout on Add Members button":::

1. Go to **Admin** > **Settings** > **Members**.
2. Select **+ Add members**. Use the  **Members** box to add other people in your organization. You can add multiple members at once.
3. Select a **Role** to assign to the new members. Currently, **Owner** is the only available selection. Other roles will be added in future releases.
4. Choose **Add** to confirm.

To remove members from a workspace, select **...** next to their names on the **Members** page and then select **Delete** from the drop-down menu.

## Edit an existing workspace

You can edit the details of existing workspaces at any time.

:::image type="content" source="media/manage-workspace.png" alt-text="Workspace settings page with callout on workspace name and description":::

1. Go to **Admin** > **Settings** > **General**.
1. Use the  **Name** box to enter a name and optionally add a **Description** for your workspace.
1. Choose **Save** to apply your changes.

## Add another new workspace

:::image type="content" source="media/workspace-switcher.png" alt-text="Customer insights page with callout on navigation pane and description":::
You can create additional workspaces to classify your data.

1. Select the **workspace switcher** in the navigation pane.
2. Select **+ New workspace**.
3. Enter a **Name** and an optional **Description**.
4. Select **Create**.

## Switch between workspaces

To view your workspaces, select the **workspace switcher** in the navigation pane. You can switch between workspaces, create a new one, or select **Web Sample** to try our reports and features using sample data. 

