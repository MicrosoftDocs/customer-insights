---
title: User roles
description: Learn about user roles and what permissions they have in Customer Insights - Data.
ms.date: 03/19/2024
ms.reviewer: mhart
ms.topic: conceptual
author: jodahl
ms.author: jodahl
ms.custom: bap-template
---

# User roles

The user role assigned to a user determines what the user can access within Customer Insights - Data. There are different types of roles a user can have.

The table provides an overview of the different roles. For  details, see each individual role.

| Action/View                                 | Viewer | Marketing Contributor\* | Contributor | Administrator | Administrator (environment owner) |
| ------------------------------------------- | ------ | ----------------------- | ----------- | ------------- | --------------------------------- |
| Access and explore Home page                | x      |                         | x           | x             | x                                 |
| Access and explore Customer page            | x      | x                       | x           | x             | x                                 |
| Access and explore Data sources page        | x      |                         | x           | x             | x                                 |
| Access and explore Enrichments page         | x      |                         | x           | x             | x                                 |
| Access and explore Tables page              | x      | x                       | x           | x             | x                                 |
| Access and explore System page              | x      |                         | x           | x             | x                                 |
| Access and explore Exports page             | x      | x                       | x           | x             | x                                 |
| Power BI Dashboard                          |        |                         | x           | x             | x                                 |
| Access, explore and configure segments      |        | x                       | x           | x             | x                                 |
| Access, explore and configure measures      |        | x                       | x           | x             | x                                 |
| Access, explore and configure predictions   |        |                         | x           | x             | x                                 |
| Access, explore and configure data sources  |        |                         | x           | x             | x                                 |
| Access, explore and configure Unification   |        |                         | x           | x             | x                                 |
| Accees, explore and configure Activities    |        |                         | x           | x             | x                                 |
| Access, explore and configure Relationships |        |                         | x           | x             | x                                 |
| Access, explore and configure Enrichments   |        |                         | x           | x             | x                                 |
| Access, explore and configure Exports       |        | x                       | x           | x             | x                                 |
| Access, explore and configure Web Tracking  |        |                         | x           | x             | x                                 |
| Access, explore and configure System        |        |                         | x           | x             | x                                 |
| Access, explore and configure Connections   |        |                         |             | x             | x                                 |
| Access, explore and configure Permissions   |        |                         |             | x             | x                                 |
| Reset environment                           |        |                         |             |               | x                                 |
| Delete environment                          |        |                         |             |               | x                                 |

*The Marketing Contributor role is only available in [business unit enabled environments](business-units-data-separation.md). All actions and views for the Marketing Contributor are limited to the business unit(s) they have access to.

## Viewer

- Explore insights and segments within the **Home** and **Segments** pages.
- Search and filter customer profiles using the **Customers** page. Fields must be searchable.
- View and explore the **Enrichment** page.
- Explore and export tables using the **Tables** page.
- View the status of system processes using the **System** page.
- View exports in the **Exports** page.
- Install and use the **Power BI Customer Insights** dashboard.

## Marketing contributor (preview)

- Can only access customer profiles that belong to the business unit of the user.
- Create segments using the **Segments** page (only *Build your own*, no projected attributes).
- Create measures using the **Measures** page (only *Build your own*). Can only create measures on tables that have a relationship path to customer profiles.
- Admins can create connections and share them with specific Marketing contributors.
- Use the shared connections to create and run exports for segments they own.

> [!NOTE]
> Marketing contributors can only create segments and measures from customer profiles, unified activities, segments, and customer measures. This permission has limited functionality in some areas compared to the Contributor role.
> Marketing contributors cannot search for customers in the *customers* view. They also cannot see measures and activities on the customer card in the *customers* view.

### Marketing contributor role examples

The following examples demonstrate the use of the Marketing contributor role.

#### Multi-geo example

Contoso has two lines of businesses - Real Estate and Retail in two different countries – USA and Canada. They have different sets of marketing users for each country who are tasked to tailor specific marketing campaigns that are unique to a country. These users are interested in seeing the unified view of customers across the two businesses (Real Estate and Retail) within the same country. Even though the probability of customers shopping in both the countries is low, the business wants to ensure that the profiles are unified within a country and not across. There are no restrictions or limitations for viewing the data across businesses and countries and they prefer a single Customer Insights - Data environment rather than setting up one environment for each country.

#### Multi-brand example

An organization owns two different lines of businesses Automobile and Luxury retail. They own car dealerships including Sales and Services for six car brands and have five luxury retail stores with online presence. A single marketing team operates within the organization across these two different lines of businesses. This marketing team would like to unify profiles within each line of business. The same marketing team is working on the data and there's no specific access control or compliance requirement. They would like to work on a single environment of Customer Insights - Data and don't wish to create one environment for each line of business.

## Contributor

- All permissions available to the Viewer.
- Load and transform data using the **Data sources** page.
- Complete **Data Unification that results in the unified customer profile table.
- Define **Relationships** and **Activities**.
- Create segments using the **Segments** page.
- Create measures using the **Measures** page.
- Manage configuration and enrich customer profiles from the **Enrichment** page (for first party enrichments only).
- Manage and create exports based on [connections shared with contributors](connections.md#allow-contributors-to-use-a-connection-for-exports).

## Admin

- All permissions available to the Contributor.
- Change settings on the **System** page, including the working language, refresh schedules for your system processes, giving consent for Copilot, and exporting diagnostic logs.
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
- [Reset and delete](manage-environments.md#reset-an-existing-environment) the environment.

## Next steps

- [Assign user permissions](permissions.md)
- [Business unit data separation](business-units-data-separation.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
