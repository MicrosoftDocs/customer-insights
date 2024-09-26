---
title: Manage environments
description: Learn how to to manage environments as an admin.
ms.date: 09/26/2024
ms.topic: how-to
ms.reviewer: mhart
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Manage environments

Administrators [create](create-environment.md) and manage environments. They can change some settings in existing environments. Region, storage option, and Dataverse settings are fixed after creating the environment. If you want to change these settings, [reset the environment](#reset-an-existing-environment) or [create a new environment](create-environment.md).

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
- Data sources based on Azure Data Lake Storage
- Data sources based on Delta tables
- Data sources based on Dataverse tables
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

> [!CAUTION]
> Don't use the [Copy an environment operation](/power-platform/admin/copy-environment#copy-an-environment-1) in Power Platform admin center if you have Customer Insights - Data installed in the target environment, because that operation removes all artifacts from the existing installation. You can't recover any deleted data.

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

## Reset an existing environment

You can reset an environment to an empty state for a fresh start. To reset an environment, you need to be the owner of the Customer Insights - Data environment and have a system administrator role on the Dataverse environment. Depending on the reason for resetting, consider backing up your environment and your data to avoid data loss. Essentially, it's a quick way to [uninstall and install Customer Insights - Data](../journeys/setup.md) from the user interface.

When you reset Customer Insights - Data environment, several things happen:

- The system deletes all your configurations. Except [your Azure Data Lake Storage Gen 2 connection](own-data-lake-storage.md) (if configured). However, after the reset, you need to [enable data sharing](own-data-lake-storage.md#enable-data-sharing-with-dataverse-from-your-own-azure-data-lake-storage-preview) (if configured) again.
- Data stored outside the Dataverse environment, such as your source data or data in your [own Data Lake](own-data-lake-storage.md) is not removed. So if you want to change data sources, consider creating a new environment.
- The system removes permissions from users that had access to the environment. The user who initiated the reset becomes the owner and admin of the reset environment.

The reset operation assigns a new instance ID to your environment. Therefore, update bookmarks for your Customer Insights - Data environment.

1. Select the **Environment** picker in the header of the app.

1. Select the environment you want to reset and select the vertical ellipsis (&vellip;).

1. Choose **Reset**.

1. To confirm, enter the environment name and select **Reset**.

## Delete an existing environment

As the owner of an environment, you can delete it.

We recommend to [use the **Uninstall** option Power Platform admin center](../journeys/setup.md) to decommission a Customer Insights - Data environment.

1. Select the **Environment** picker in the header of the app.

1. Select the environment you want to delete and select the vertical ellipsis (&vellip;).

1. Choose **Delete**.

1. To confirm the deletion, enter the environment name and select **Delete**.

After deleting the environment, you can reinstall a new Customer Insights - Data environment on the same Microsoft Dataverse environment. Removing dependencies as isn't required to reinstall.

## Remove Customer Insights - Data dependencies from a Dataverse environment

Deleting a Customer Insights - Data environment doesn't remove dependencies from the Dataverse environment. However, if you want to remove all dependencies to Customer Insights - Data, go through the following steps.

> [!NOTE]
> It can take a couple of hours for the dependencies removal to take effect.

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
1. Uninstall all solutions that start with *msdyn_CustomerInsights*.

If the removal of the connection fails due to other dependencies, you need to remove these dependencies too. For more information, see [Removing dependencies](/power-platform/alm/removing-dependencies).

## Next steps

- [Create a new environment](create-environment.md)
- [Data sources overview](data-sources.md)
- [Data unification overview](data-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
