---
title: "Create a new environment"
description: Steps to create environments in Dynamics 365 Customer Insights.
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
ms.custom: bap-template
---

# Create a new environment

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

After [purchasing a subscription license for Dynamics 365 Customer Insights](paid-license.md), the global administrator of the Microsoft 365 tenant receives an email that invites them to create the environment.

After the first environment is created, the global administrator of the Microsoft 365 tenant can [add users from their organization as administrators](permissions.md). These administrators can then manage users and environments. If your organization purchases more than one license for Customer Insights, [contact our support team](https://go.microsoft.com/fwlink/?linkid=2079641) to increase the number of available environments. For more information about capacity and add-on capacity, review the [Dynamics 365 licensing guide](https://go.microsoft.com/fwlink/?LinkId=866544).

> [!IMPORTANT]
> In most cases, creating an environment or installing Customer Insights - Data on an existing environment should be done with the consolidated provisioning experience.  <!-- link to SPA doc-->

Use the environments creation experience in Customer Insights - Data for the following scenarios:

- Use your [own Azure Data Lake Storage Account](own-data-lake-storage.md) AND [Azure Private Link](private-link.md)
- [Enable data sharing](own-data-lake-storage.md#enable-data-sharing-with-dataverse-from-your-own-azure-data-lake-storage-preview) between your own Data Lake Storage Account and Microsoft Dataverse
- [Create a copy of an existing environment configuration](#copy-the-environment-configuration)

## Prerequisites

- [Administrator permissions](permissions.md) in Customer Insights - Data.
- A global administrator role set up in the Dataverse environment. Verify if this [Dataverse environment is associated](/power-platform/admin/control-user-access#associate-a-security-group-with-a-dataverse-environment) to certain security groups and make sure you're added to those security groups.
- A Dataverse [license is assigned](/power-platform/admin/create-users#to-assign-a-license) to you to get Read-Write access mode. Unlicensed administrators get Administrative access mode only.
- No other Customer Insights - Data environment already associated with the Dataverse environment you want to connect. Learn how to [remove an existing connection to a Dataverse environment](manage-environment.md#remove-an-existing-connection-to-a-dataverse-environment).
- A Microsoft Dataverse environment connected to a single storage account if you configure the environment to [use your Azure Data Lake Storage](own-data-lake-storage.md).

## Dataverse storage capacity entitlement

A Customer Insights - Data subscription entitles you to extra capacity for your organization's existing [Dataverse storage capacity](/power-platform/admin/capacity-storage). The added capacity depends on the number of profiles that your subscription uses. Customer Insights - Data writes some output tables to Dataverse. For more information, see [Customer Insights - Data tables in Dataverse](tables.md#customer-insights---data-tables-in-dataverse).

**Example:**

Assuming you get 15-GB database storage and 20-GB file storage per 100,000 customer profiles. If your subscription includes 300,000 customer profiles, your total storage capacity is 45 GB (3 x 15 GB) database storage and 60-GB file storage (3 x 20 GB).

Log capacity isn't incremental and fixed for your organization.

For more information about the detailed capacity entitlements, see [Dynamics 365 Licensing Guide](https://go.microsoft.com/fwlink/?LinkId=866544).

## Create an environment in Customer Insights - Data

We recommend to use the consolidated environment manager for Customer Insights to create new environment by default.
<!-- add link to SPA doc-->

1. Open the environment picker and select **+ New**.
  
   :::image type="content" source="media/environment-picker.png" alt-text="Select the environment picker.":::

1. Follow the guided experience outlined in the following sections to provide all required information for a new environment.

### Step 1: Provide basic information

1. Choose whether you want to create an environment from scratch or copy data from another environment. [Copying data from another environment](#copy-the-environment-configuration) requires additional steps.

   :::image type="content" source="media/environment-settings-dialog.png" alt-text="Dialog to create a new environment.":::

1. Provide the following details:

   - **Name**: Name for this environment. This field is already filled in if you've copied an existing environment, but you can change it.
   - **Type**: Type of environment: production or sandbox. Sandbox environments don't allow scheduled data refresh and are intended for pre-implementation and testing. Sandbox environments use the same primary audience as the production environment that's currently selected.
   - **Region**: Region into which the service is deployed and hosted. To [use your own Azure Data Lake Storage account](own-data-lake-storage.md) or connect to an existing Microsoft Dataverse organization, all environments must be in the same region.

1. Select **Next**.

### Step 2: Configure data storage

1. Choose where to store the data:

   - **Customer Insights storage**: Data storage is managed automatically. It's the default option and unless there are specific requirements to store data in your own storage account, we recommend using this option.
   - **Azure Data Lake Storage Gen2**: Your own Azure Data Lake Storage account to store the data so you have full control where the data is stored. Follow the steps in [Use your own Azure Data Lake Storage account](own-data-lake-storage.md).

   :::image type="content" source="media/data-storage-environment.png" alt-text="Choose the preferred option to store your data.":::

1. Select **Next**.

### Step 3: Connect to Microsoft Dataverse

Select an existing Dataverse environment that doesn't already have a Customer Insights - Data environment attached to it. Or you can choose to have a new Microsoft Dataverse environment created and attached. Additionally, if you chose to use your own Azure Data Lake storage in the previous step, you can enable data sharing with Dataverse to use it with business applications based on Dataverse or model-driven applications in Power Apps.

:::image type="content" source="media/dataverse-provisioning.png" alt-text="data sharing with Microsoft Dataverse auto-enabled for new environments.":::

1. Provide the URL to your Dataverse environment or leave blank to have one created for you.

   [Power Platform admins can control who can create a new Dataverse environments](/power-platform/admin/control-environment-creation). If you're trying to set up a new environment and can't, the admin might have disabled the creation of Dataverse environments for everyone except admins.

1. If you're using your own Data Lake Storage account:
   1. Select **Enable data sharing** with Dataverse.
   1. Enter the **Permissions identifier**. To get the permission identifier, [enable data sharing with Dataverse from your own Azure Data Lake Storage](own-data-lake-storage.md#enable-data-sharing-with-dataverse-from-your-own-azure-data-lake-storage-preview).

### Step 4: Finalize the settings

Review the specified settings. When everything looks complete, select **Create** to set up the environment.

To change some of the settings later, see [Manage environments](manage-environments.md).

## Work with your new environment

Review the following articles to help you get started:

- [Get started in minutes with a single CSV file](data-sources-single.md).

  > [!NOTE]
  > [!INCLUDE [single-file-us-only](includes/single-file-us-only.md)]

- [Add more users and assign permissions](permissions.md).
- [Ingest several of your data sources](data-sources.md) and run them through the [data unification process](data-unification.md) to get [unified customer profiles](customer-profiles.md).
- [Enrich the unified customer profiles](enrichment-hub.md) or [run predictive models](predictions.md).
- [Create segments](segments.md) to group customers and [measures](measures.md) to review KPIs.
- [Set up connections](connections.md) and [exports](export-manage.md) to process subsets of your data in other applications.

## Copy the environment configuration

As an admin, if you chose to copy the configuration from an existing environment, select from the list of all available environments in your organization.

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

1. After refreshing the data sources, go to **Data** > **Unify**. Here you'll find settings from the source environment. Edit them as needed or select **Unify** > **Unify customer profiles and dependencies** to start the data unification process and create the unified customer table.

1. When the data unification is complete, go to **Insights** > **Measures** and **Insights** > **Segments** to refresh them.

1. Go to **Settings** > **Connections** to reauthenticate the connections in your new environment.

1. Go to **Data** > **Enrichment** and **Data** > **Exports** to reactivate them.

## Next steps

- [Assign user permissions](permissions.md)
- [Data sources overview](data-sources.md)
- [Data unification overview](data-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
