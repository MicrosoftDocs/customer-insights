---
title: Create a new environment in Customer Insights - Data
description: Create a new environment in Dynamics 365 Customer Insights by choosing storage, Dataverse settings, and region. Follow these steps to get started.
ms.date: 11/24/2026
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Create a new environment

After [your organization purchases a license for Dynamics 365 Customer Insights](paid-license.md), the administrator of the Microsoft 365 tenant receives an email that invites them to create an environment and [add users from their organization as administrators](permissions.md). These administrators can then manage users and Customer Insights environments. A user assigned the Administrator role in Customer Insights - Data is automatically assigned the System Administrator role in the Dataverse environment. You need the System Administrator role to create, manage, and delete Power Platform dataflow connections.

> [!IMPORTANT]
> For first-time set up, you must install Customer Insights - Data through [Power Platform admin center](../journeys/setup.md).

For subsequent environments, you can create an environment directly through Customer Insights - Data or through Power Platform admin center.

You must use Customer Insights - Data for the following scenarios:

- You want the new environment to use your [own Azure Data Lake Storage Account](own-data-lake-storage.md).
- You want to [enable data sharing](own-data-lake-storage.md#enable-data-sharing-with-dataverse-from-your-own-azure-data-lake-storage-preview) between your own Data Lake Storage Account and Microsoft Dataverse.
- You want to [create a copy of an existing environment configuration](manage-environments.md#copy-the-environment-configuration).

## Prerequisites

- [Administrator permissions](user-roles.md#admin) in Customer Insights - Data.
- You must have an existing Dataverse environment.

## Create an environment in Customer Insights - Data

1. Open the environment picker and select **+ New**.
  
   :::image type="content" source="media/environment-picker.png" alt-text="Screenshot of the environment picker.":::

1. Follow the guided experience outlined in the following sections and provide all required information for a new environment.

### Step 1: Provide basic information

1. Choose whether you want to create an environment from scratch or copy data from another environment. [Copying data from another environment](manage-environments.md#copy-the-environment-configuration) requires extra steps.

1. Provide the following details:

   - **Name**: Name for this environment. This field is already filled in if you copied an existing environment, but you can change it.
   - **Type**: Type of environment: production or sandbox.
     - Select **Sandbox** for a development and testing environment. Sandbox environments don't support scheduled refreshes.
     - Select **Production** for your production environment or for any environment that you want to mirror your production environment. Production environments provide the maximum scale and performance.
   - **Region**: Region into which the service is deployed and hosted. To [use your own Azure Data Lake Storage account](own-data-lake-storage.md) install on an existing Microsoft Dataverse organization, all environments must be in the same region.

1. Select **Next**.

### Step 2: Configure data storage

1. Choose where to store the data:

   - **Customer Insights storage**: Data storage is managed automatically. It's the default option and unless there are specific requirements to store data in your own storage account, use this option.
   - **Azure Data Lake Storage Gen2**: Your own Azure Data Lake Storage account to store the data so you have full control over where the data is stored. Follow the steps in [Use your own Azure Data Lake Storage account](own-data-lake-storage.md).

1. Select **Next**.

### Step 3: Choose Dataverse environment

Select an existing Dataverse environment that doesn't already have a Customer Insights - Data environment installed on it. [Learn more about the required permissions](#prerequisites).

If you chose to use your own Azure Data Lake storage in the previous step, you can [enable data sharing with Dataverse](own-data-lake-storage.md#enable-data-sharing-with-dataverse-from-your-own-azure-data-lake-storage-preview). You can use it with business applications based on Dataverse or model-driven applications in Power Apps.

:::image type="content" source="media/dataverse-provisioning.png" alt-text="Screenshot of data sharing with Microsoft Dataverse autoenabled for new environments.":::

1. Choose an existing Dataverse environment from the drop-down that you want to install Customer Insights - Data. To create a new environment, go to the Power Platform admin center and [create it](/power-platform/admin/create-environment#create-an-environment-with-a-database). Then, refresh the list of environments and select the newly created environment.

1. If you're using your own Data Lake Storage account:
   1. Select **Enable data sharing** with Dataverse.
   1. Enter the **Permissions identifier**. To get the permission identifier, [enable data sharing with Dataverse from your own Azure Data Lake Storage](own-data-lake-storage.md#enable-data-sharing-with-dataverse-from-your-own-azure-data-lake-storage-preview).

1. Select **Next**.

### Step 4: Finalize the settings

Review the specified settings. When everything looks complete, select **Create** to set up the environment.

To change some of the settings later, see [Manage environments](manage-environments.md).

## Work with your new environment

Review the following articles to help you get started:

- [Add more users and assign permissions](permissions.md).
- [Ingest several of your data sources](data-sources.md) and run them through the [data unification process](data-unification.md) to get [unified customer profiles](customer-profiles.md).
- [Enrich the unified customer profiles](enrichment-manage.md) or [run predictive models](predictions.md).
- [Create segments](segments.md) to group customers and [measures](measures.md) to review KPIs.
- [Set up connections](connections.md) and [exports](export-manage.md) to process subsets of your data in other applications.

## Next steps

- [Assign user permissions](permissions.md)
- [Data sources overview](data-sources.md)
- [Data unification overview](data-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
