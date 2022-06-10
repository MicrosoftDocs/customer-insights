---
title: How to - Create a new environment
description: Steps to create environments in Dynamics 365 Customer Insights.
ms.date: 05/31/2022
ms.reviewer: mhart
ms.subservice: audience-insights
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
manager: shellyha
ms.custom: intro-internal
searchScope: 
  - ci-home
  - customerInsights
---

# How to: Create a new environment

After [purchasing a subscription license for Dynamics 365 Customer Insights](paid-license.md), the global administrator of the Microsoft 365 tenant receives an email that invites them to create the environment. Go to [https://home.ci.ai.dynamics.com/start](https://home.ci.ai.dynamics.com/start) to get started. In this scenario, you can go directly to [Step 1: Provide basic information](#step-1-provide-basic-information).

After the first environment is created, the global administrator of the Microsoft 365 tenant can [add users form their organization as administrators](permissions.md). Moving forward, these administrators can manage users and environments. If your organization purchases more than one license for Customer Insights, [contact our support team](https://go.microsoft.com/fwlink/?linkid=2079641) to increase the number of available environments. For more information about capacity and add-on capacity, review the [Dynamics 365 licensing guide](https://go.microsoft.com/fwlink/?LinkId=866544).

> [!TIP]
> If you're looking to try the service, see [Set up a trial environment](trial-signup.md).

## Prerequisites

You need [administrator permissions](permissions.md) in Customer Insights to create or manage environments.

## Start the environment creation process

1. Open the environment picker and select **+ New**.
  
   :::image type="content" source="media/environment-picker.png" alt-text="Select the environment picker.":::

1. Follow the guided experience outlined in the following sections to provide all required information for a new environment. If you configured an environment earlier, you can also [copy the configuration](#copy-the-environment-configuration).

## Step 1: Provide basic information

In the **Basic information** step, choose whether you want to create an environment from scratch or [copy data from another environment](#copy-the-environment-configuration).

   :::image type="content" source="media/environment-settings-dialog.png" alt-text="Dialog to create a new Customer Insights environment.":::

Provide the following details:

- **Name**: The name for this environment. This field is already filled in if you've copied an existing environment, but you can change it.
- **Choose your business**: Choose the primary audience for the new environment. You can work with individual consumers (B-to-C) or [business accounts](work-with-business-accounts.md) (B-to-B). If your organization mainly does business with individuals, such as a retailer or a coffee shop, choose individual consumers. In case your main audience are other companies, such as a car manufacturer or a paper company, choose business accounts.
- **Type**: Select whether you want to create a production or sandbox environment. Sandbox environments don't allow scheduled data refresh and are intended for pre-implementation and testing. Sandbox environments use the same primary audience as the production environment that's currently selected.
- **Region**: The region into which the service is deployed and hosted. To [use your own Azure Data Lake Storage account](own-data-lake-storage.md) or [connect to an existing Microsoft Dataverse organization](customer-insights-dataverse.md), the Customer Insights environment must be in the same region.

## Step 2: Configure data storage

In the **Data storage** step, choose where to store the Customer Insights data.

There are two options you can choose from:

- **Customer Insights storage**: Data storage is managed by the Customer Insights team. It's the default option and unless there are specific requirements to store data in your own storage account, we recommend using this option.
- **Azure Data Lake Storage**: Specify your own Azure Data Lake Storage account to store the data so you have full control where the data is stored. For more information, see [Use your own Azure Data Lake Storage account](own-data-lake-storage.md).

:::image type="content" source="media/data-storage-environment.png" alt-text="Choose the preferred option to store your data.":::

## Step 3: Connect to Microsoft Dataverse

The **Microsoft Dataverse** step lets you connect Customer Insights with your Dataverse environment. Share data with Dataverse to use it with business applications based on Dataverse, like Dynamics 365 Marketing or model-driven applications in Power Apps.

Leave this field empty if you don't have your own Dataverse environment and we'll create one for you.

For more information, see [Work with Customer Insights data in Microsoft Dataverse](customer-insights-dataverse.md).

:::image type="content" source="media/dataverse-provisioning.png" alt-text="data sharing with Microsoft Dataverse auto-enabled for net new environments.":::

### Step 4: Finalize the settings

In the **Review** step, go through all the specified settings. When everything looks complete, select **Create** to set up the environment.

You can change some of the settings later. For more information, see [Manage environments](manage-environments.md).

## Work with your new environment

Review the following articles to help you get started with configuring Customer Insights:

- [Add more users and assign permissions](permissions.md).
- [Ingest your data sources](data-sources.md) and run them through the [data unification process](data-unification.md) to get [unified customer profiles](customer-profiles.md).
- [Enrich the unified customer profiles](enrichment-hub.md) or [run predictive models](predictions-overview.md).
- [Create segments](segments.md) to group customers and [measures](measures.md) to review KPIs.
- [Set up connections](connections.md) and [exports](export-destinations.md) to process subsets of your data in other applications.

## Copy the environment configuration

As an admin, you can choose to copy the configuration from an existing environment when you create a new one.

:::image type="content" source="media/environment-settings-dialog.png" alt-text="Screenshot of the settings options in the environment settings.":::

You'll see a list of all available environments in your organization where you can copy data from.

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

## Set up a copied environment

When you copy the environment configuration, you have to go through some extra steps to confirm credentials:

- Customer profiles. First, authenticate and ingest your data sources and run the data unification to recreate the customer profiles.
- Data source credentials. You have to provide the credentials for every data source to authenticate and refresh the data sources manually.
- Data sources from the Common Data Model folder and Dataverse. You have to create those data sources manually with the same name as in the source environment.
- Connection secrets that are used for exports and enrichments. You have to reauthenticate the connections and then reactivate enrichments and exports.

You'll see a confirmation message when the copied environment has been created. Select **Go to data sources** to see the list of data sources.

All the data sources will show a **Credentials Required** status. Edit the data sources and enter the credentials to refresh them.

:::image type="content" source="media/data-sources-copied.png" alt-text="List of data sources that were copied and need authentication.":::

After refreshing the data sources, go to **Data** > **Unify**. Here you'll find settings from the source environment. Edit them as needed or select **Run** to start the data unification process and create the unified customer entity.

When the data unification is complete, go to **Measures** and **Segments** to refresh them too.

Before you reactivate exports and enrichments, go to **Admin** > **Connections** to reauthenticate the connections in your new environment.

[!INCLUDE [footer-include](includes/footer-banner.md)]
