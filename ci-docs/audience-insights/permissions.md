---
title: "User permissions in Dynamics 365 Customer Insights | Microsoft Docs"
description: "Learn about permissions and user roles in Dynamics 365 Customer Insights."
ms.date: 09/28/2020
ms.reviewer: nimagen
ms.service: dynamics-365-ai
ms.topic: "get-started-article"
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# User permissions

The **Permissions** page is where you'll set up roles and permissions for using Dynamics 365 Customer Insights across your organization.

You need to have administrator permissions to see the page. To access the permissions page in Customer Insights, go to **Admin** > **Permissions**.

Customer Insights includes three types of roles:

## Viewer

- Explore insights and segments within the **Home** and **Segments** pages.
- Search and filter customer profiles using the **Customers** page. Fields must be searchable.
- View and explore the **Enrichment** page.
- Explore and export entities using the **Entities** page.
- View the status of system processes  using the **System** page.
- Export segments from the **Segments** page to either a .CSV file or to a Dynamics 365 Sales destination.
- Install and use the **Power BI Customer Insights** dashboard to seek insights on your customers.

## Contributor

- All permissions available to the Viewer.
- Load and transform data using the **Data sources** page.
- Complete the *Data Unification* sections (**Map**, **Match**, and **Merge**) which result in the unified customer profile entity.
- Define **Relationships** and **Activities**.
- Create segments using the **Segments** page.
- Create measures using the **Measures** page.
- Manage configuration and enrich customer profiles from the **Enrichment** page (for first party enrichments only).

## Administrator

- All permissions available to the Contributor.
- Change settings on the **System** page, including the working language and refresh schedules for your system processes.
- View and add permissions using the **Permissions** page.
- Set search and filter definitions for the Customers page using the **Search & filter index** page (accessible via the **Customers** page).
- Define Dynamics 365 Sales segment destinations using the **Export destinations** page.
- Manage configuration and enrich customer profiles from the **Enrichment** page (for all enrichments).
- Install and use the **Customer Card Add-in**.
- Add and use the **Power Apps connector** to create apps with Customer Insights data.

## Assign roles and permissions

Administrators may use the **Permissions** page to grant user role assignments within Customer Insights.

1. On the **Permissions** page, select **Add users** to open the **Add/Edit permissions** pane.

2. Use the **Search** field to find the Azure Active Directory user or group whose permissions you want to adjust. Select a **Role** to assign to that user or group.

3. Select **Save**. The current work instance will automatically be shared with the user or members of the group whose permissions you've changed. Users can access the Customer Insights app and work according to their specified role.

## View current permissions

Go to **Admin** > **Permissions** page to see what role assignments are currently active.

- The **Type** column specifies a single user, group, or application. The system supports individual users and groups.
- Roles are specified under the **Role** column.
- Select any column title to sort the results by that column's value.
- Use the **Search** field at the top of the page to locate specific users.
