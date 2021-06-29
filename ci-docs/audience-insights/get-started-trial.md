---
title: "Create and configure a trial of Customer Insights"
description: "Steps to get a trial subscription for Dynamics 365 Customer Insights and configure it ."
ms.date: 06/29/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: midevane
ms.author: midevane
manager: shellyha
---

# Set up a trial environment

<to do>
- Prerequisites
- Limitations (DV storage, duration etc.)
- Options to convert?

## Create a trial environment

You can sign up for a trial on the [trial sign up page](https://dynamics.microsoft.com/get-started/free-trial/?appname=customerinsights). 

> [!NOTE]
> Trials expire after 30 days.

1. Choose the **Sign up for a free trial** option and select **Sign up now**.

1. Provide your work or school email address, tell us a more about yourself and select **Next**.

   :::image type="content" source="media/trial-signup-dialog.png" alt-text="Dialog to sign up for a trial instance":::

1. Provide a **Name** for your new environment. 

1. Select the trial type.

1. Choose the **Region** for your environment.

1. Optionally, for admins of a Dynamics 365 organization: Select **Advanced settings** and provide the URL of your organization to use prediction features like customer churn.

1. Select **Create**. 

After the environment was created, you'll see the **Demo** environment which lets you explore the app with fictitious data.

## Use scenario-specific demo data sets in audience insights

Connecting real data sources is one of the critical steps in leveraging the power of Customer Insights. Sometimes, you might just want to try out some feature without interfering with your own data. There are a couple of demo data sets available at your disposal to quickly try a scenario or review a new feature with fictitious data for the following scenarios: 

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

For a read-only version of Customer Insights, tailored to a specific industry or scenario, go to the Demo environment. 
 
1.	In audience insights, choose the Demo environment in the environment picker.
2.	On Home, choose an option from the Select an industry demo drop-down menu.

### Create scenario-specific demo data in your own environment

For a fully customizable solution based on sample data, you first need to ingest the data in your environment. Administrator permissions are required to ingest data. 

IMPORTANT: 
Ingested demo data can’t be removed. We strongly recommend creating a new sandbox environment before ingesting demo data. 

1.	In audience insights, go to Data > Data sources.
2.	Choose the Import from Datahub option.
3.	Select the card that suits your scenario. 
4.	Review and optionally update the suggested name of the data source. 
5.	Select Next to ingest the data source. 

Repeat the steps above to ingest additional data sets.
You can now use the ingested data to tailor Customer Insights to your scenario. To see an environment specific to the ingested demo data, choose the <Industry> Demo option in the environment picker.
