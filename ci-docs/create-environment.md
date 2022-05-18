---
title: "Create environments in Customer Insights"
description: "Steps to create environments with a licensed subscription for Dynamics 365 Customer Insights."
ms.date: 04/25/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: adkuppa
ms.author: adkuppa
manager: shellyha
ms.custom: intro-internal
searchScope: 
  - ci-home
  - customerInsights
---

# Create a new environment

After purchasing a subscription license for Customer Insights, the global administrator of the Microsoft 365 tenant receives an email that invites them to create the environment. Go to [https://home.ci.ai.dynamics.com/start](https://home.ci.ai.dynamics.com/start) to get started.

Organizations can create multiple environments for every Customer Insights license. If your organization purchases more than one license, [contact our support team](https://go.microsoft.com/fwlink/?linkid=2079641) to increase the number of available environments. For more information about capacity and add-on capacity, review the [Dynamics 365 licensing guide](https://go.microsoft.com/fwlink/?LinkId=866544).

> [!TIP]
> If you're looking to try the service, see [Set up a trial environment](trial-signup.md).

You need [administrator permissions](permissions.md) in Customer Insights to create or manage environments.
## Create a new environment


1. Open the environment picker and select **+ New**.
  
   :::image type="content" source="media/environment-picker.png" alt-text="Select the environment picker.":::

1. Follow the guided experience outlined in the following sections to gather all required information for a new environment. 

## Step 1: Provide environment information

In the **Basic information** step, choose whether you want to create an environment from scratch or [copy data from another environment](manage-environments.md#copy-the-environment-configuration).

   :::image type="content" source="media/environment-settings-dialog.png" alt-text="Dialog to create a new Customer Insights environment.":::

Provide the following details:
   - **Name**: The name for this environment. This field is already filled in if you've copied an existing environment, but you can change it.
   - **Choose your business**: Choose the primary audience for the new environment. You can work with individual consumers (B-to-C) or [business accounts](work-with-business-accounts.md) (B-to-B). If your organization mainly does business with individuals, such as a retailer or a coffee shop, choose individual consumers. In case your main audience are other companies, such as a car manufacturer or a paper company, choose business accounts.
   - **Type**: Select whether you want to create a production or sandbox environment. Sandbox environments don't allow scheduled data refresh and are intended for pre-implementation and testing. Sandbox environments use the same primary audience as the production environment that's currently selected.
   - **Region**: The region into which the service is deployed and hosted.

## Step 2: Configure data storage

In the **Data storage** step, choose where to store the Customer Insights data.

You'll have two options: 
- **Customer Insights storage** where the storage is managed by the Customer Insights team.
- **Azure Data Lake Storage** which lets you specify your own Azure Data Lake Storage account to store the data. For more information, see [Use your own Azure Data Lake Storage account](own-data-lake-storage.md).

By default, the Customer Insights storage option is selected.

:::image type="content" source="media/data-storage-environment.png" alt-text="Choose the preferred option to store your data.":::


## Step 3: Connect to Microsoft Dataverse
   
The **Microsoft Dataverse** step lets you connect Customer Insights with your Dataverse environment. Provide your own Dataverse environment to share data (profiles and insights) with business applications based on Dataverse, like Dynamics 365 Marketing or model-driven applications in Power Apps. 

Leave this field empty if you don't have your own Dataverse environment and we'll provision one for you.

For more information, see [Work with Customer Insights data in Microsoft Dataverse](customer-insights-dataverse.md).

:::image type="content" source="media/dataverse-provisioning.png" alt-text="data sharing with Microsoft Dataverse auto enabled for net new instances.":::

### Step 4: Finalize the settings

In the **Review** step, go through all the specified settings. When everything looks complete, select **Create** to set up the environment.

You can change most of the settings later. For more information, see [Manage environments](manage-environments.md).

## Work with your new environment

Review the following articles to help you get started with configuring Customer Insights: 

- [Add more users and assign permissions](permissions.md).
- [Ingest your data sources](data-sources.md) and run them through the [data unification process](data-unification.md) to get [unified customer profiles](customer-profiles.md).
- [Enrich the unified customer profiles](enrichment-hub.md) or [run predictive models](predictions-overview.md).
- [Create segments](segments.md) to group customers and [measures](measures.md) to review KPIs.
- [Set up connections](connections.md) and [exports](export-destinations.md) to process subsets of your data in other applications.
