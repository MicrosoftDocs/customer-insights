---
uid: topics/first-run-experience
title: First run experience
author: ruthaisabokhae
description: First run experience through the product
ms.author: ruthai
ms.date: 07/15/2020
ms.service: product-insights
ms.topic: conceptual
---

# First run experience

[!INCLUDE [cc-beta-prerelease-disclaimer]( includes/cc-beta-prerelease-disclaimer.md)]

This article explains how to create a Dynamics 365 Product Insights instance and how to set up an environment.

## Sign up for Product Insights and create a project

1. In your browser, go to the [Dynamics 365 Product Insights](https://pi.dynamics.com/) website. Create a new account, or sign in with your existing credentials.
2. Once signed in, you'll see the **Get started with Product Insights!** tutorial appear. Select your current region, and use the checkbox to indicate whether you want to opt in to receive updates and offers via email.
3. Review the **Product Insights Preview Terms of Service** and **Privacy Statement**, then select **Next** to accept them.
4. Select the type of activity that you want your project to measure. Currently, **Website activity** is the only available choice. **App activity** and **Device activity** will become available in future releases. Select **Next** to confirm and create the project.
5. You'll see a success message, and a code snippet that must be added to your website in order for Product Insights to start receiving data. You can implement this right away, or **share the code** and instructions for implementing it with your webmaster via email. You can always find this code again later by navigating to **Admin** -> **Data** -> **Code** in the Project Insights menu. Select **Done** to go to your Product Insights instance.

Note that data will not begin flowing until the above code has been implemented on your website.

## Add members to an existing project

By default, only the person who created the Product Insights instance will have access. You can add other users from your organization to an existing project at any time.

1. Select **Admin** -> **Settings** -> **Members** in the navigation menu.
2. Select **+ Add members**. Use the **Members** field to search for other people in your organization. You can add multiple new members at once.
3. Select a **Role** to assign to the new members. Currently, **Owner** is the only available selection. Other role will be added in future releases.
4. Select **Add** to confirm and return to the **Members** page.

To remove members from a project, simply select **...** next to their name on the **Members** page, then select **Delete** from the dropdown menu.

## Edit an existing project

You can edit the details of existing projects at any time.

1. Select **Admin** -> **Settings** -> **General** in the navigation menu.
2. Enter an updated **Name** or **Description** for your project, then **Save** your changes.

## Add another new project

You can create additional projects, which may be helpful in compartmentalizing your data.

1. Select the **Organization name** symbol in the bottom-left corner of Product Insights.
2. Select **+ New project**.
3. Enter a **Name** and optional **Description**, then select **Create**.

## Switch between projects

If you are a member of multiple projects, switch between them at any time by selecting the **Organization name** symbol in the bottom-left corner of Product Insights, and then selecting your desired project from the menu that appears.
