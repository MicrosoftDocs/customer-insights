---  
title: "Trial FAQ - Dynamics 365 Customer Insights"
description: "Solutions to common questions related to Customer Insights trial setup and management. Learn how to resolve platform and app-specific issues."
author: m-hartmann
ms.author: mhart
ms.date: 09/30/2021
ms.topic: get-started
ms.service: customer-insights
ms.custom: template-trial-faq
ms.reviewer: jeffhar
manager: shellyha
---

# Dynamics 365 Customer Insights trial FAQ

[!INCLUDE[trial-faq-platform](includes/trial-faq-platform.md)]

### Can I convert the trial to a paid license?

Generally, we recommend starting fresh with your own data when upgrading to the paid version of Customer Insights. 

Optionally, if you only use audience insights, you can copy your data from a trial environment if you purchase Customer Insights. You must be the administrator of the Customer Insights trial and the global admin of your Microsoft 365 tenant, or the Dynamics 365 administrator in your organization to migrate the settings from a trial environment to a paid environment. 

After signing in to your paid instance of Customer Insights for the first time, you're asked to create a new environment. In this process, you can choose to copy the configuration from an existing environment and migrate most of the settings. If you have the permissions mentioned above, the trial environment will show in this list. For more information, see [Copy the environment configuration](audience-insights/manage-environments.md#copy-the-environment-configuration).

### What are the trial limits and quotas?

- You can't use your own Azure Data Lake storage account to store output data during a trial. However, you can ingest data from a Data Lake storage account.
- You can store a up to 3 GB data in the Dataverse environment that gets provisioned automatically when you start a Customer Insights trial.

## Customer Insights-specific questions

### How do I start using the trial?

After you sign up for the trial, you will arrive on the app's main screen. The main screen provides links to user guides and tutorials. To learn more, visit the links in the [Additional resources](trial-signup.md#additional-resources) on the trial set up page.

### What features are available in the trial?

Most features of the Customer Insights capabilities are available in the trial.

The following features are not available: 
- You can't link audience insights and engagement insights environments.
- You can't create new environments that use your own Azure Data Lake storage account.

### How long does the trial last?

The Customer Insights trial lasts 30 days. You can extend the trial once after 23 days when you sign in to your trial environment.

### How do I remove sample data from the trial?

You can't remove the sample data from the trial.
