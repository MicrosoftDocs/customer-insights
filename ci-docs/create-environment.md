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

# Create an environment in Customer Insights

This article explains how to create a new environment after your organization has purchased a Dynamics 365 Customer Insights subscription. 

Organizations can create multiple environments for every Customer Insights license. If your organization purchases more than one license, [contact our support team](https://go.microsoft.com/fwlink/?linkid=2079641) to increase the number of available environments. For more information about capacity and add-on capacity, review the [Dynamics 365 licensing guide](https://go.microsoft.com/fwlink/?LinkId=866544).

> [!NOTE]
> If you're looking to try the service, see [Set up a trial environment](trial-signup.md).

## Create a new environment

After purchasing a subscription license for Customer Insights, the global administrator of the Microsoft 365 tenant receives an email that invites them to create the environment. Go to [https://home.ci.ai.dynamics.com/start](https://home.ci.ai.dynamics.com/start) to get started. 

A guided experience helps you through the steps to gather all required information for a new environment. You need [administrator permissions](permissions.md) in Customer Insights to create or manage environments.

1. Open the environment picker and select **+ New**.
  
   :::image type="content" source="media/environment-picker.png" alt-text="Select the environment picker.":::

1. Follow the guided experience outlined in the following sections.

### Step 1: Provide environment information

In the **Basic information** step, choose whether you want to create an environment from scratch or [copy data from another environment](manage-environments.md#copy-the-environment-configuration).

   :::image type="content" source="media/environment-settings-dialog.png" alt-text="Dialog to create a new Customer Insights environment.":::

Provide the following details:
   - **Name**: The name for this environment. This field is already filled in if you've copied an existing environment, but you can change it.
   - **Choose your business**: Choose the primary audience for the new environment. You can work with individual consumers (B-to-C) or [business accounts](work-with-business-accounts.md) (B-to-B).
   - **Type**: Select whether you want to create a production or sandbox environment. Sandbox environments don't allow scheduled data refresh and are intended for pre-implementation and testing. Sandbox environments use the same primary audience as the production environment that's currently selected.
   - **Region**: The region into which the service is deployed and hosted.

### Step 2: Configure data storage

In the **Data storage** step, choose where to store the Customer Insights data.

You'll have two options: **Customer Insights storage** (an Azure data lake managed by the Customer Insights team) and **Azure Data Lake Storage** (your own Azure Data Lake Storage). By default, the Customer Insights storage option is selected.

:::image type="content" source="media/data-storage-environment.png" alt-text="Choose the Azure Data Lake Storage to store your data.":::

By saving data to Azure Data Lake Storage, you agree that data will be transferred to and stored in the appropriate geographic location for that Azure storage account. This location may differ from where data is stored in Dynamics 365 Customer Insights. Learn more at the [Microsoft Trust Center](https://www.microsoft.com/trust-center).

> [!NOTE]
> Customer Insights currently supports the following:
> - Ingested entities from Power BI dataflows that are stored in a Microsoft Dataverse-managed Data Lake.  
> - Azure Data Lake Storage accounts from the same Azure region that you selected when creating the environment.
> - Azure Data Lake Storage accounts that are Gen2 and have *hierarchical namespace* enabled. Azure Data Lake Gen1 storage accounts are not supported.

For the Azure Data Lake Storage option, you can choose between a resource-based option and a subscription-based option for authentication. For more information, see [Connect to an Azure Data Lake Storage account by using an Azure service principal](connect-service-principal.md). A container named `customerinsights` has to exist on the storage account.

When system processes such as data ingestion is complete, the system creates corresponding folders in the storage account you specified. Data files and *model.json* files are created and added to folders based on the process name.

If you create multiple environments of Customer Insights and choose to save the output entities from those environments to your storage account, Customer Insights creates separate folders for each environment with `ci_environmentID` in the container.

### Step 3: Connect to Microsoft Dataverse
   
The **Microsoft Dataverse** step lets you connect Customer Insights with your Dataverse environment.

Provide your own Microsoft Dataverse environment to share data (profiles and insights) with business applications based on Dataverse, like Dynamics 365 Marketing or model-driven applications in Power Apps. Leave this field empty if you don't have your own Dataverse environment and we'll provision one for you.

Connecting to your Dataverse environment also enables you to [ingest data from on-premises data sources using Power Platform dataflows and gateways](data-sources.md#add-data-from-on-premises-data-sources). You can also use [out-of-box prediction models](predictions-overview.md?tabs=b2c#out-of-box-models) by connecting to a Dataverse environment.

> [!IMPORTANT]
> 1. Customer Insights and Dataverse have to be in the same region to enable data sharing.
> 1. You must have a global administrator role in the Dataverse environment. Verify if this [Dataverse environment is associated](/power-platform/admin/control-user-access#associate-a-security-group-with-a-dataverse-environment) to certain security groups and make sure you are added to those security groups.
> 1. No existing Customer Insights environment is already associated with that Dataverse environment. Learn how to [remove an existing connection to a Dataverse environment](manage-environments.md#remove-an-existing-connection-to-a-dataverse-environment).

:::image type="content" source="media/dataverse-provisioning.png" alt-text="data sharing with Microsoft Dataverse auto enabled for net new instances.":::

For more information about enabling data sharing with Microsoft Dataverse from your own Azure Data Lake Storage, see [Connect to Microsoft Dataverse](manage-environments.md#connect-to-microsoft-dataverse).

Customer Insights does not support the following data sharing scenarios:
- If you enable data sharing with Dataverse, you won't be able to [create predicted or missing values in an entity](predictions.md).

### Step 4: Finalize the settings

In the **Review** step, go through all of the specified settings. When everything looks complete, select **Create** to set up the environment. 

You can also change most of the settings later. For more information, see [Manage environments](manage-environments.md).

## Work with your new environment

Review the following articles to help you get started with configuring Customer Insights: 

- [Add more users and assign permissions](permissions.md).
- [Ingest your data sources](data-sources.md) and run them through the [data unification process](data-unification.md) to get [unified customer profiles](customer-profiles.md).
- [Enrich the unified customer profiles](enrichment-hub.md) or [run predictive models](predictions-overview.md).
- [Create segments](segments.md) to group customers and [measures](measures.md) to review KPIs.
- [Set up connections](connections.md) and [exports](export-destinations.md) to process subsets of your data in other applications.
