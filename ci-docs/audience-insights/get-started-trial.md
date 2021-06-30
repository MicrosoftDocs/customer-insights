---
title: "Create and configure a trial of Customer Insights"
description: "Steps to get a trial subscription for Dynamics 365 Customer Insights and configure it."
ms.date: 06/29/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: MichelleDevaney
ms.author: midevane
manager: shellyha
---

# Set up a trial environment

A trial of Dynamics 365 Customer Insights lets you review key capability and learn more about the various features. A trial subscription expires after 30 days and is automatically deleted afterwards. Trial organizations are created by individual users who become administrator of their trial environment. They can invite more users to their trial and configure the various features.

## Create a trial environment

You can sign up for a trial on the [trial sign up page](https://dynamics.microsoft.com/get-started/free-trial/?appname=customerinsights). 

1. Choose the **Sign up for a free trial** option and select **Sign up now**.

1. Provide your work or school email address, tell us a more about yourself and select **Next**.

   :::image type="content" source="media/trial-signup-dialog.png" alt-text="Dialog to sign up for a trial instance":::

1. Provide a **Name** for your new environment. 

1. Select the trial type.

1. Choose the **Region** for your environment.

1. Optionally, if you are the admin of a Dynamics 365 organization: Select **Advanced settings** and provide the URL of your organization to use prediction features like customer churn prediction. 

1. Select **Create**. 

After setting up the trial, you'll see the **Demo** environment that lets you explore the app with fictitious data.

## Use industry-specific demo data sets in audience insights

Connecting real data sources is one of the critical steps in using the power of Customer Insights. To try features without interfering with your own data, you can use industry-specific demo data. There are a couple of demo data sets available for the following industries: 

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

For a fully customizable solution based on sample data, you can ingest the data in your environment. Administrator permissions are required to ingest data. 

1.	In audience insights, go to **Data** > **Data sources**.

2.	Choose the **Import from Datahub** option.

3.	Select the industry card that suits your scenario. 

4.	Review and optionally update the suggested name of the data source. 

5.	Select **Next** to ingest the sample data. 

You can now use the ingested data to tailor Customer Insights to your scenario. To see an environment specific to the ingested demo data, choose the **<Industry> Demo** option in the environment picker.

## Limitations in trials

- You can't use your own Azure Data Lake storage account during a trial.
- You can store a limited amount of data in Microsoft Dataverse. 

## Copy data from a trial to a paid subscription

Generally, we recommend starting fresh with your own data when upgrading to the paid version of Customer Insights. 

However, if you're the administrator of the Customer Insights trial and the global admin of your Microsoft 365 tenant, or the Dynamics 365 administrator in your organization there's a way to migrate the settings from a trial environment to a paid environment. 

After signing in to your paid instance of Customer Insights for the first time, you're asked to create a new environment. In this process, you can choose to copy the configuration from an existing environment and migrate most of the settings. For more information, see [Copy the environment configuration](manage-environments.md#copy-the-environment-configuration).

