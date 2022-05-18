---
title: "Create and manage environments"
description: "Learn how to sign up for the service and how to manage environments."
ms.date: 05/17/2022
ms.subservice: audience-insights
ms.topic: how-to
ms.reviewer: mhart
author: adkuppa
ms.author: adkuppa
manager: shellyha
searchScope: 
  - ci-system-about
  - customerInsights
---

# Manage environments

## Switch environments

Select the **Environment** control in the upper-right corner of the page to change environments.

:::image type="content" source="media/home-page-environment-switcher.png" alt-text="Screenshot of the control to switch environments.":::

Administrators can [create](create-environment.md) and manage environments.

## Edit an existing environment

You can edit some of the details of existing environments.

1.	Select the **Environment** picker in the header of the app.

2.	Select the **Edit** icon.

3. In the **Edit environment** box, you can update the environment settings.

For more information on environment settings, see [Create a new environment](create-environment.md).

## Change the owner of an environment

While several users can have admin permissions in Customer Insights, only one user is the owner of an environment. By default, it's the admin who creates an environment initially. As the admin of an environment, you can assign ownership to another user with admin permissions.

1. Select the **Environment** picker in the header of the app.

1. Select the **Edit** icon.

1. In the **Edit environment** box, go to the **Basic information** step.

1. In the **Change owner of environment** field, choose the new owner of the environment.  

1. Select **Review and finish**, then **Update** to apply the changes. 

## Claim ownership of an environment

If the owner of an environment leaves the organization or their user account is deleted, the environment will have no owner. A user with admin permissions can claim the ownership and become the new owner. They can continue to own the environment or [change the ownership to another admin](#change-the-owner-of-an-environment). 

To claim ownership, select the **Take ownership** button that shows at the top of every page in Customer Insights when the original owner left the organization.

## Reset an existing environment

As the owner of an environment, you can reset an environment to an empty state if you want to delete all configurations and remove the ingested data.

1.	Select the **Environment** picker in the header of the app. 

2.	Select the environment you want to reset and select the ellipsis (**...**). 

3. Choose the **Reset** option. 

4.	To confirm the deletion, enter the environment name and select **Reset**.

## Copy the environment configuration

As an admin, you can choose to copy the configuration from an existing environment when you create a new one. 

:::image type="content" source="media/environment-settings-dialog.png" alt-text="Screenshot of the settings options in the environment settings.":::

You'll see a list of all available environments in your organization where you can copy data from.

The following configuration settings are copied:

- Ingested/imported data sources
- Data unification configuration
- Segments
- Measures
- Relationships
- Activities
- Search & filter Index
- Export destinations
- Scheduled refresh
- Enrichments
- Model management
- Role assignments

## Set up a copied environment

When you copy the environment configuration, the following data is *not* copied:

- Customer profiles.
- Data source credentials. You'll have to provide the credentials for every data source and refresh the data sources manually.
- Data sources from the Common Data Model folder and Dataverse-managed data lake. You'll have to create those data sources manually with the same name as in the source environment.
- Connection secrets that are used for exports and enrichments. You have to reauthenticate the connections and then reactivate enrichments and exports. 

You'll see a confirmation message when the copied environment has been created. Select **Go to data sources** to see the list of data sources.

All the data sources will show a **Credentials Required** status. Edit the data sources and enter the credentials to refresh them.

:::image type="content" source="media/data-sources-copied.png" alt-text="List of data sources that were copied and need authentication.":::

After refreshing the data sources, go to **Data** > **Unify**. Here you'll find settings from the source environment. Edit them as needed or select **Run** to start the data unification process and create the unified customer entity.

When the data unification is complete, go to **Measures** and **Segments** to refresh them too.

Before you reactivate exports and enrichments, go to **Admin** > **Connections** to reauthenticate the connections in your new environment.

## Delete an existing environment

As the owner of an environment, you can delete an environment you administer.

1.	Select the **Environment** picker in the header of the app.

2.	Select the environment you want to reset and select the ellipsis (**...**). 

3. Choose the **Delete** option. 

4.	To confirm the deletion, enter the environment name and select **Delete**.

> [!NOTE]
> Deleting an environment does not remove the association to a Dataverse environment. Learn how to [remove an existing connection to a Dataverse environment](customer-insights-dataverse.md#remove-an-existing-connection-to-a-dataverse-environment).



[!INCLUDE [footer-include](includes/footer-banner.md)]
