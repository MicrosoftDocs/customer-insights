---
title: "Create and configure a paid license of Customer Insights"
description: "Steps to get a licensed subscription for Dynamics 365 Customer Insights and configure it."
ms.date: 07/22/2021
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
Organizations can create *two* environments for every Customer Insights license. If your organization purchases more than once license, please [contact our support team](https://go.microsoft.com/fwlink/?linkid=2079641) to increase the number of available environments. For more information about capacity and add-on capacity, download the [Dynamics 365 licensing guide](https://go.microsoft.com/fwlink/?LinkId=866544).

If you're looking to try the service and the features, see [Set up a trial environment](get-started-trial.md).

## Create a new environment

A guided experience helps you through the steps to gather all required information for a new environment. You need [administrator permissions](permissions.md) in audience insights to crate or manage environments.

1. In audience insights, open the environment picker and select **+ New**

1. Follow the guided experience outlined in the following sections.

### Step 1: Provide basic information

In the **Basic information** step, choose whether you want to create an environment from scratch or if you want to [copy data from another environment](manage-environments.md#copy-the-environment-configuration).

   :::image type="content" source="media/environment-settings-dialog.png" alt-text="Dialog to create a new Customer Insights environment.":::

Provide the following details:
   - **Name**: The name for this environment. This field is already filled in if you've copied an existing environment, but you can change it.
   - **Region**: The region into which the service is deployed and hosted.
   - **Type**: Select whether you want to create a production or sandbox environment. Sandbox environments don't allow scheduled data refresh and are intended for pre-implementation and testing.

### Step 2: Configure data storage
   
In the **Data storage** step, choose where you store the data from audience insights.

   You'll have two options: **Customer Insights storage** (an Azure Data Lake managed by the Customer Insights team) and **Azure Data Lake Storage** (your own Azure Data Lake Storage). By default, the Customer Insights storage option is selected.

     > [!NOTE]
     > By saving data to Azure Data Lake Storage, you agree that data will be transferred to and stored in the appropriate geographic location for that Azure storage account, which may differ from where data is stored in Dynamics 365 Customer Insights. [Learn more at the Microsoft Trust Center.](https://www.microsoft.com/trust-center)
     >
     > Currently, ingested entities from Power BI dataflows are stored in the Microsoft Dataverse-managed Data Lake. 
     > 
     > We support only Azure Data Lake Storage accounts from the same Azure region you selected when creating the environment. 
     > 
     > We support only Azure Data Lake Storage accounts that have hierarchical namespace enabled.


For the Azure Data Lake Storage option, you can choose between a resource-based option and a subscription-based option for authentication. For more information, see [Connect audience insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md). The **Container** name can't be changed and will be `customerinsights`.

When system processes like data ingestion complete, the system creates corresponding folders in the storage account you specified. Data files and model.json files are created and added to folders based on the process name.

If you create multiple environments of Customer Insights and choose to save the output entities from those environments in your storage account, separate folders will be created for each environment with ci_<environmentid> in the container.

### Step 3: Connect to Microsoft Dataverse
   
To use [out-of-box prediction models](predictions-overview.md#out-of-box-models), configure data sharing with Microsoft Dataverse, or enable data ingestion from on-premises data sources, provide the Microsoft Dataverse environment URL that your organization administers. Select **Enable data sharing** to share Customer Insights output data with a Microsoft Dataverse Managed Data Lake.

   > [!NOTE]
   > - Data sharing with Microsoft Dataverse Managed Data Lake is currently not supported when you save all data to your own Azure Data Lake Storage.
   > - [Prediction of missing values in an entity](predictions.md) is currently not supported when you enable data sharing with Microsoft Dataverse Managed Data Lake.

:::image type="content" source="media/Datasharing-with-DataverseMDL.png" alt-text="Configuration options to enable data sharing with Microsoft Dataverse.":::

### Step 4: Review and finalize the settings

In the Review step, go through the specifyed settings. If everything looks good, select **Create** to set up the environment. 

## Next steps to work with the environment

Review the following articles to help you getting started with configuring Customer Insights. 

- [Add more users and assign permissions](permissions.md).
- [Ingest your data sources](data-sources.md) and run them through the [data unification process](data-unification.md) to get [unified customer profiles](customer-profiles.md).
- [Enrich the unified customer profiles](enrichment-hub.md) or [run predictive models](predictions-overview.md).
- Create [segments](segments.md) to group customers and [measures](measures.md) review KPIs.
- Set up [connections](connections.md) and [exports](export-destinations.md) to process subsets of your data in other applications.
