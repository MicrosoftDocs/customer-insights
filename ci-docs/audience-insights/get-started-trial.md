---
title: "Create and configure a trial of Customer Insights"
description: "Steps to get a trial subscription for Dynamics 365 Customer Insights and configure it."
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

# Set up a trial environment 

A trial of Dynamics 365 Customer Insights lets you review key capability and learn more about the various features. A trial subscription is deleted after expiring. Trial environments are created by individual users who become administrator of their trial environment. They can invite more users to their trial and configure the various features.

## Create a trial environment

You can sign up for a trial on the [trial sign up page](https://dynamics.microsoft.com/get-started/free-trial/?appname=customerinsights). 

1. Choose the **Sign up for a free trial** option and select **Sign up now**.

1. Provide your work or school email address, tell us a more about yourself and select **Get started**.

   :::image type="content" source="media/trial-signup-dialog.png" alt-text="Dialog to sign up for a trial instance":::

1. Review the terms and conditions and select **Continue** to confirm.

1. Provide a **Name** for your new environment. 

1. Set the environment **Type** as **Trial**.

1. In the **Select an industry demo** field, you can optionally choose an industry-specific data set. You can also [change to an industry demo](#use-industry-specific-demo-data-sets-in-audience-insights) later and start with the default data set.

1. Choose the **Region** for your environment.

1. Optionally, if you are the admin of a Dynamics 365 organization: Select **Advanced settings** and provide the URL of your organization to use prediction features like customer churn prediction. 

1. Select **Create**. 

It takes a few moments to complete the environment setup. After completion, you're redirected to the demo environment or the industry demo you choose in the step above. You can now explore the app with read-only demo data. To add your own data to the environment, see [Create scenario-specific demo data in your own environment](#create-scenario-specific-demo-data-in-your-own-environment).

:::image type="content" source="media/trial-environment.png" alt-text="Screenshot of a newly created trial environment.":::

## Use industry-specific demo data sets in audience insights

Connecting real data sources is one of the critical steps in using the power of Customer Insights. To try features without interfering with your own data, you can optionally use industry-specific demo data. There are a couple of demo data sets available for the following industries: 

-	Automotive
-	Banking
-	Consumer goods
-	Government
-	Healthcare
-	Hospitality
-	Insurance
-	Manufacturing
-	Professional services
-	Retail

### See industry-specific demo data in trials

For a read-only version of Customer Insights, tailored to a specific industry or scenario, start in the Demo environment. 
 
1.	In audience insights, choose the **Demo** environment in the environment picker.

2.	On **Home**, choose an option from the Select an industry demo drop-down menu.

:::image type="content" source="media/trial-select-industry-demo.png" alt-text="Choose an industry for the trial environment.":::

### Create scenario-specific demo data in your own environment

As an administrator, select the environment picker in the app header to create a new environment. In the new environment, you can configure your own data sources and set up the app according to your requirements. 

1.	In audience insights, go to **Data** > **Data sources**.

2.	To import your own data sources, go to the [guide on data ingestion](data-sources.md).     
   If you prefer working with sample data that lets you try out data ingestion, you can ingest the industry demo data in your environment. Choose the **Import from Datahub** option and follow the steps below.

3.	Select the industry card that suits your scenario. 

4.	Review and optionally update the suggested name of the data source. 

5.	Select **Next** to ingest the sample data. 

You can now use the ingested data to tailor Customer Insights to your scenario. To see an environment specific to the ingested demo data, choose the **<Industry> Demo** option in the environment picker.

## Limitations in trials

- Trials are active for 30 days by default. However, you can extend them after day 23 when you sign in to your trial.
- You can't use your own Azure Data Lake storage account to store output data during a trial. However, you can ingest data from a Data Lake storage account.
- You can store up to 3 GB data in the Dataverse environment that gets provisioned automatically when you start a Customer Insights trial.

## Copy data from a trial to a paid subscription

Generally, we recommend starting fresh with your own data when upgrading to the paid version of Customer Insights. 

Optionally, you can copy your data from a trial environment if you purchase Customer Insights. You must be the administrator of the Customer Insights trial and the global admin of your Microsoft 365 tenant, or the Dynamics 365 administrator in your organization to migrate the settings from a trial environment to a paid environment. 

After signing in to your paid instance of Customer Insights for the first time, you're asked to create a new environment. In this process, you can choose to copy the configuration from an existing environment and migrate most of the settings. If you have the permissions mentioned above, the trial environment will show in this list. For more information, see [Copy the environment configuration](manage-environments.md#copy-the-environment-configuration).

## Next steps

Review the following articles to help you getting started with configuring Customer Insights. 

- [Add more users and assign permissions](permissions.md).
- [Ingest your data sources](data-sources.md) and run them through the [data unification process](data-unification.md) to get [unified customer profiles](customer-profiles.md).
- [Enrich the unified customer profiles](enrichment-hub.md) or [run predictive models](predictions-overview.md).
- Create [segments](segments.md) to group customers and [measures](measures.md) review KPIs.
- Set up [connections](connections.md) and [exports](export-destinations.md) to process subsets of your data in other applications.
