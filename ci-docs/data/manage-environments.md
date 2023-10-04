---
title: "Manage environments"
description: Learn how to to manage environments as an admin.
ms.date: 09/01/2023
ms.topic: how-to
ms.reviewer: mhart
author: kishorem-ms
ms.author: kishorem
ms.custom: bap-template
---

# Manage environments

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Administrators [create](create-environment.md) and manage environments. They can change some settings in existing environments. Region, storage option, and Dataverse settings are fixed after creating the environment. If you want to change these settings, [reset the environment](#reset-an-existing-environment-preview) or [create a new environment](create-environment.md).

## Edit an existing environment

Edit details of an existing environment such as the name or setting the default environment.

1. Select the **Environment** picker in the header of the app.

1. Select the **Edit** icon.

   :::image type="content" source="media/edit-environment.png" alt-text="Icon to edit the environment settings.":::

1. In the **Edit environment** pane, update the environment settings.

1. Select **Review and finish**, then **Update** to apply the changes.

## Copy the environment configuration

You can copy the configuration of an existing environment when [creating a new one](create-environment.md). Select the source from the list of all available environments in your organization.

:::image type="content" source="media/environment-settings-dialog.png" alt-text="Screenshot of the settings options in the environment settings.":::

The following configuration settings are copied:

- Data sources imported via Power Query
- Data unification configuration
- Segments
- Measures
- Relationships
- Activities
- Search & filter index
- Exports
- Refresh schedule
- Enrichments
- Prediction models
- Role assignments

### Set up a copied environment

When you copy the environment configuration, a confirmation message displays when the copied environment has been created. Perform the following steps to confirm credentials.

1. Select **Go to data sources** to see the list of data sources. All the data sources show **Credentials Required** status.

   :::image type="content" source="media/data-sources-copied.png" alt-text="List of data sources that were copied and need authentication.":::

1. Edit the data sources and enter the credentials to refresh them. Data sources from the Common Data Model folder and Dataverse must be created manually with the same name as in the source environment.

1. After refreshing the data sources, go to **Data** > **Unify**. Here you find settings from the source environment. Edit them as needed or select **Unify** > **Unify customer profiles and dependencies** to start the data unification process and create the unified customer table.

1. When the data unification is complete, go to **Insights** > **Measures** and **Insights** > **Segments** to refresh them.

1. Go to **Settings** > **Connections** to reauthenticate the connections in your new environment.

1. Go to **Data** > **Enrichment** and **Data** > **Exports** to reactivate them.

## Change the owner of an environment

Several users can have admin permissions but only one user is the owner of an environment. By default, it's the admin who creates an environment initially. As an admin of an environment, you can assign ownership to another user with admin permissions.

1. Select the **Environment** picker in the header of the app.

1. Select the **Edit** icon.

1. In the **Edit environment** pane, go to the **Basic information** step.

1. In the **Change owner of environment** field, choose the new owner of the environment.  

1. Select **Review and finish**, then **Update** to apply the changes.

## Claim ownership of an environment

If the user account of the owner is deleted or suspended, the environment has no owner. Any admin user can claim the ownership and become the new owner. The owner admin can continue to own the environment or [change the ownership to another admin](#change-the-owner-of-an-environment).

To claim ownership, select the **Take ownership** button that shows at the top of every page in Dynamics 365 Customer Insights - Data when the original owner left the organization.

We recommend having at least one other user with admin permissions in addition to the owner to enable smooth ownership transfer if the owner leaves the organization.

## Reset an existing environment (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

As the owner of an environment, reset an environment to an empty state if you want to delete all configurations and remove the ingested data.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

1. Select the **Environment** picker in the header of the app.

1. Select the environment you want to reset and select the vertical ellipsis (&vellip;).

1. Choose **Reset (preview)**.

   :::image type="content" source="media/reset-environment.png" alt-text="Control to reset an environment.":::

1. Choose whether you want to reset the entire environment, everything except the data sources, or anything that is configured on top of the unified customer profile.

1. To confirm, enter the environment name and select **Reset**.

## Delete an existing environment

As the owner of an environment, you can delete it.

We recommend to [use the **Uninstall** option Power Platform admin center](../journeys/setup.md) to decommission a Customer Insights - Data environment.

> [!IMPORTANT]
> Deleting a Customer Insights - Data environment does not remove the Customer Insights dependencies from the Dataverse environment. If you plan to use same Dataverse environment to install Customer Insights - Data in the future, you must [remove all dependencies to the Dataverse environment](#remove-customer-insights---data-dependencies-from-a-dataverse-environment).

1. Select the **Environment** picker in the header of the app.

1. Select the environment you want to delete and select the vertical ellipsis (&vellip;).

1. Choose **Delete**.

   :::image type="content" source="media/delete-environment.png" alt-text="Control to delete the environment.":::

1. To confirm the deletion, enter the environment name and select **Delete**.

## Remove Customer Insights - Data dependencies from a Dataverse environment

Deleting a Customer Insights - Data environment doesn't remove dependencies from the Dataverse environment. Before you can reinstall Customer Insights - Data on a Dataverse environment, all dependencies must be removed.

> [!NOTE]
> You must be a global administrator on the Dataverse environment. It can take a couple of hours for the dependencies removal to take effect.

1. Go to [Power Apps](https://make.powerapps.com).
1. Select the environment from the environment picker.
1. If you have Dynamics 365 Customer Insights - Journeys installed on the Dataverse environment, and you have [it connected to your Customer Insights - Data environment](/dynamics365/marketing/real-time-marketing-ci-profile), remove this connection first. Otherwise, skip this step and proceed to step 4.
    1. Go to **Tables**.
    1. Find the table *msdynmkt_configuration*.
    1. Go to the *CXPConfig* row in this table.
    1. Go to the *Customer Insights Status* column and change the value from *Configured* to *NotConfigured*.
    1. Go to **Solutions**.
    1. Uninstall the following Dynamics 365 Customer Insights - Journeys solutions:
        - DynamicsMKT_AttachCIApplicationUser (*DynamicsMKT_AttachCIApplicationUser*)
        - Dynamics Marketing Consent For Customer Insights (*DynamicsMKT_ConsentAttachCI*)
        - DynamicsMKT_OrchestrationEngineAttachCI (*DynamicsMKT_OrchestrationEngineAttachCI*)
1. Go to **Solutions**.
1. Uninstall the following Customer Insights - Data solutions:
   - Dynamics 365 Customer Insights Base (*msdyn_CustomerInsightsAnchor*)
   - Dynamics 365 Customer Insights Data Tables (*msdyn_CustomerInsightsDataTables*)
   - Dynamics 365 Customer Insights (*msdyn_CustomerInsights*)
   - Dynamics 365 Customer Insights Customer Card (*CustomerInsightsCustomerCard*)
   - Dynamics 365 Customer Insights Prod First Party App User Management (*msdyn_CustomerInsightsAppUserManagementProd*)

If the removal of the connection fails due to other dependencies, you need to remove these dependencies too. For more information, see [Removing dependencies](/power-platform/alm/removing-dependencies).

## Next steps

- [Create a new environment](create-environment.md)
- [Data sources overview](data-sources.md)
- [Data unification overview](data-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
