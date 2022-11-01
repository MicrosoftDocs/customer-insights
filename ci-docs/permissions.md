---
title: "Assign user permissions"
description: "Learn about permissions and user roles."
ms.date: 11/15/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: NimrodMagen
ms.author: nimagen
manager: shellyha
searchScope: 
  - ci-permissions
  - ci-system-security
  - customerInsights
---

# Assign user permissions

Access to Customer Insights is restricted to users in your organization that are added to the application by an admin. An admin can add, edit, or remove users. A user can be a single user, group, or application. There are three types of roles a user can have:

## Viewer

- Explore insights and segments within the **Home** and **Segments** pages.
- Search and filter customer profiles using the **Customers** page. Fields must be searchable.
- View and explore the **Enrichment** page.
- Explore and export tables using the **Tables** page.
- View the status of system processes using the **System** page.
- View exports in the **Exports** page.
- Install and use the **Power BI Customer Insights** dashboard.

## Contributor

- All permissions available to the Viewer.
- Load and transform data using the **Data sources** page.
- Complete **Data Unification** which result in the unified customer profile table.
- Define **Relationships** and **Activities**.
- Create segments using the **Segments** page.
- Create measures using the **Measures** page.
- Manage configuration and enrich customer profiles from the **Enrichment** page (for first party enrichments only).
- Manage and create exports based on [connections shared with contributors](connections.md#allow-contributors-to-use-a-connection-for-exports).

## Admin

- All permissions available to the Contributor.
- Change settings on the **System** page, including the working language, refresh schedules for your system processes, and exporting diagnostic logs.
- Change settings on the **Permissions** page, including users, API keys, private links, and key vault.
- Set search and filter definitions for the Customers page using the **Search & filter index** page (accessible via the **Customers** page).
- Manage connections and allow them for other user roles on **Connections** page.
- Manage configuration and enrich customer profiles from the **Enrichment** page (for all enrichments).
- Manage and create exports on the **Exports** page.
- Install and use the **Customer Card Add-in**.
- Add and use the **Power Apps connector**.
- Enable usage of [Customer Insights APIs](apis.md).
- [Assign environment ownership](manage-environments.md#change-the-owner-of-an-environment) to another admin.

## Admin (owner)

- All permissions available to the Admin.
- [Reset and delete](manage-environments.md#reset-an-existing-environment-preview) the environment.

## Add users

1. Go to **Settings** > **Permissions** and select the **Users** tab.

1. Select **Add users** to open the **Add/Edit permissions** pane.

1. Use the **Search** field to find the Azure Active Directory user or group you want to add. Select a **Role** to assign to that user or group.

1. Select **Save**. The current environment is automatically shared with the user or members of the group. Users can access the Customer Insights app and work according to their specified role.

## View current permissions

Go to **Settings** > **Permissions** and select the **Users** tab to view the list of active users and their role assignments. You can sort the list of users by any column or use the search box to find a particular user.

## Manage current users

Go to **Settings** > **Permissions** and select the **Users** tab. You can sort the list of users by any column or use the search box to find the user you want to manage.

Select a user to view available actions.

- **Edit** to edit the user's role in Customer Insights. Select **Save** to confirm the change.
- **Remove** to remove the user from having access to Customer Insights. Select **Delete** to confirm the deletion.

[!INCLUDE [footer-include](includes/footer-banner.md)]
