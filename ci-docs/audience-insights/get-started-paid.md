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

This article explains how to create a new environment after your organization has purchased a Dynamics 365 Customer Insights subscription. If you'd like to purchase Customer Insights, our contact options are listed on the [Dynamics 365 Customer Insights website](https://dynamics.microsoft.com/ai/customer-insights/). 

If you're looking to try the service and the features, see [Set up a trial environment](get-started-trial.md).

## Create an environment in an existing organization

After purchasing a subscription license for Customer Insights, the global administrator of the Microsoft 365 tenant receives an email that invites them to create the environment. Go to [https://home.ci.dynamics.com/start](https://home.ci.dynamics.com/start) to get started. 

Customer Insights is not licensed per user, so it won't show in the Licenses area. If you're looking for the license in the Microsoft 365 admin center, go to **Your products**. 

> [!NOTE]
> Organizations can create *two* environments for every Customer Insights license. If your organization purchases more than once license, please [contact our support team](https://go.microsoft.com/fwlink/?linkid=2079641) to increase the number of available environments. For more information about capacity and add-on capacity, download the [Dynamics 365 licensing guide](https://go.microsoft.com/fwlink/?LinkId=866544).

To create an environment:

1. In the **Create an environment** dialog, select **New environment**.

   :::image type="content" source="media/environment-settings-dialog.png" alt-text="Dialog to create a new Customer Insights environment.":::

   We recommend to start setting up an environment from scratch. However, if you are an admin or member of a trial environment, you could [copy data from another environment](manage-environments.md#copy-the-environment-configuration), by choosing **Copy from existing environment**. You'll see a list of all available environments in your organization where you can copy data from.

1. Provide the following details:
   - **Name**: The name for this environment. This field is already filled in if you've copied an existing environment, but you can change it.
   - **Region**: The region into which the service is deployed and hosted.
   - **Type**: Select whether you want to create a production or sandbox environment. Sandbox environments don't allow scheduled data refresh and are intended for pre-implementation and testing.
   
1. Optionally, you can select **Advanced settings**:

   - **Save all data to**: Specifies where you want to store the output data generated from Customer Insights. You'll have two options: **Customer Insights storage** (an Azure Data Lake managed by the Customer Insights team) and **Azure Data Lake Storage** (your own Azure Data Lake Storage). By default, the Customer Insights storage option is selected.

     > [!NOTE]
     > By saving data to Azure Data Lake Storage, you agree that data will be transferred to and stored in the appropriate geographic location for that Azure storage account, which may differ from where data is stored in Dynamics 365 Customer Insights. [Learn more at the Microsoft Trust Center.](https://www.microsoft.com/trust-center)
     >
     > Currently, ingested entities from Power BI dataflows are stored in the Microsoft Dataverse-managed Data Lake. 
     > 
     > We support only Azure Data Lake Storage accounts from the same Azure region you selected when creating the environment. 
     > 
     > We support only Azure Data Lake Storage accounts that have hierarchical namespace enabled.


   - For the Azure Data Lake Storage option, you can choose between a resource-based option and a subscription-based option for authentication. For more information, see [Connect audience insights to an Azure Data Lake Storage Gen2 account with an Azure service principal](connect-service-principal.md). The **Container** name can't be changed and will be `customerinsights`.
   
   - If you want to use [out-of-box models](predictions-overview.md#out-of-box-models), configure data sharing with Microsoft Dataverse, or enable data ingestion from on-premises data sources, provide the Microsoft Dataverse environment URL under **Configure data sharing with Microsoft Dataverse and enable additional capabilities**. Select **Enable data sharing** to share Customer Insights output data with a Microsoft Dataverse Managed Data Lake.

     > [!NOTE]
     > - Data sharing with Microsoft Dataverse Managed Data Lake is currently not supported when you save all data to your own Azure Data Lake Storage.
     > - [Prediction of missing values in an entity](predictions.md) is currently not supported when you enable data sharing with Microsoft Dataverse Managed Data Lake.

     > [!div class="mx-imgBorder"]
     > ![Configuration options to enable data sharing with Microsoft Dataverse.](media/datasharing-with-DataverseMDL.png)

   When system processes like data ingestion complete, the system creates corresponding folders in the storage account you specified. Data files and model.json files are created and added to folders based on the process name.

   If you create multiple environments of Customer Insights and choose to save the output entities from those environments in your storage account, separate folders will be created for each environment with ci_<environmentid> in the container.

1. Select **Create** to set up the environment. 

## Configure an environment

Review the following articles to help you getting started with configuring Customer Insights. 

- [Add more users and assign permissions](permissions.md).
- [Ingest your data sources](data-sources.md) and run them through the [data unification process](data-unification.md) to get [unified customer profiles](customer-profiles.md).
- [Enrich the unified customer profiles](enrichment-hub.md) or [run predictive models](predictions-overview.md).
- Create [segments](segments.md) to group customers and [measures](measures.md) review KPIs.
- Set up [connections](connections.md) and [exports](export-destinations.md) to process subsets of your data in other applications.
