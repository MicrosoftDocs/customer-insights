---
title: "Create and configure a paid license of Customer Insights"
description: "Steps to get a licensed subscription for Dynamics 365 Customer Insights and configure it."
ms.date: 10/12/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: MichelleDevaney
ms.author: midevane
manager: shellyha
ms.custom: intro-internal
---

# Get started with a paid subscription

This article explains how to create a new environment after your organization has purchased a Dynamics 365 Customer Insights subscription. 

Organizations can create *two* environments for every Customer Insights license. If your organization purchases more than one license, please [contact our support team](https://go.microsoft.com/fwlink/?linkid=2079641) to increase the number of available environments. For more information about capacity and add-on capacity, download the [Dynamics 365 licensing guide](https://go.microsoft.com/fwlink/?LinkId=866544).

> [!NOTE]
> If you're looking to try the service, see [Set up a trial environment](get-started-trial.md).

## Create a new environment

After purchasing a subscription license for Customer Insights, the global administrator of the Microsoft 365 tenant receives an email that invites them to create the environment. Go to [https://home.ci.ai.dynamics.com/start](https://home.ci.ai.dynamics.com/start) to get started. 

A guided experience helps you through the steps to gather all required information for a new environment. You need [administrator permissions](permissions.md) in audience insights to create or manage environments.

1. In audience insights, open the environment picker and select **+ New**.
  
   :::image type="content" source="media/environment-picker.png" alt-text="Select the environment picker.":::

1. Follow the guided experience outlined in the following sections.

### Step 1: Provide environment information

In the **Basic information** step, choose whether you want to create an environment from scratch or [copy data from another environment](manage-environments.md#copy-the-environment-configuration).

   :::image type="content" source="media/environment-settings-dialog.png" alt-text="Dialog to create a new Customer Insights environment.":::

Provide the following details:
   - **Name**: The name for this environment. This field is already filled in if you've copied an existing environment, but you can change it.
   - **Region**: The region into which the service is deployed and hosted.
   - **Type**: Select whether you want to create a production or sandbox environment. Sandbox environments don't allow scheduled data refresh and are intended for pre-implementation and testing. Sandbox environments use the same primary audience like the production environment that's currently selected.
   - Choose the primary audience for the new environment. You can work with individual customers (B2C) or [business accounts](work-with-business-accounts.md) (B2B).

### Step 2: Configure data storage

In the **Data storage** step, choose where to store the data from audience insights.

You'll have two options: **Customer Insights storage** (an Azure Data Lake managed by the Customer Insights team) and **Azure Data Lake Storage** (your own Azure Data Lake Storage). By default, the Customer Insights storage option is selected.

By saving data to Azure Data Lake Storage, you agree that data will be transferred to and stored in the appropriate geographic location for that Azure storage account. This location may differ from where data is stored in Dynamics 365 Customer Insights. Learn more at the [Microsoft Trust Center](https://www.microsoft.com/trust-center).

> [!NOTE]
> Customer Insights currently supports the following:
> - Ingested entities from Power BI dataflows that are stored in a Microsoft Dataverse-managed Data Lake.  
> - Azure Data Lake Storage accounts from the same Azure region that you selected when creating the environment.
> - Azure Data Lake Storage accounts that have *hierarchical namespace* enabled.

For the Azure Data Lake Storage option, you can choose between a resource-based option and a subscription-based option for authentication. For more information, see [Connect audience insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md). Note that the **Container** name will be `customerinsights` and can't be changed.

When system processes such as data ingestion is complete, the system creates corresponding folders in the storage account you specified. Data files and *model.json* files are created and added to folders based on the process name.

If you create multiple environments of Customer Insights and choose to save the output entities from those environments to your storage account, Customer Insights creates separate folders for each environment with `ci_<environmentid>` in the container.

### Step 3: Connect to Microsoft Dataverse
   
To use [out-of-box prediction models](predictions-overview.md#out-of-box-models), configure data sharing with Microsoft Dataverse. Or you can enable data ingestion from on-premises data sources, providing the Microsoft Dataverse environment URL that your organization administers. Select **Enable data sharing** to share Customer Insights output data with a Microsoft Dataverse Managed Data Lake.

:::image type="content" source="media/Datasharing-with-DataverseMDL.png" alt-text="Configuration options to enable data sharing with Microsoft Dataverse.":::

> [!NOTE]
> Customer Insights does not support the following data sharing scenarios:
> - If you save all data to your own Azure Data Lake Storage, you won't be able to enable data sharing with a Microsoft Dataverse Managed Data Lake.
> - If you enable data sharing with a Microsoft Dataverse Managed Data Lake, you won't be able to [create predicted or missing values in an entity](predictions.md).

### Step 4: Finalize the settings

In the Review step, go through all of the specified settings. When everything looks complete, select **Create** to set up the environment. 

## Work with your new environment

Review the following articles to help you getting started with configuring Customer Insights. 

- [Add more users and assign permissions](permissions.md).
- [Ingest your data sources](data-sources.md) and run them through the [data unification process](data-unification.md) to get [unified customer profiles](customer-profiles.md).
- [Enrich the unified customer profiles](enrichment-hub.md) or [run predictive models](predictions-overview.md).
- [Create segments](segments.md) to group customers and [measures](measures.md) review KPIs.
- [Set up connections](connections.md) and [exports](export-destinations.md) to process subsets of your data in other applications.
