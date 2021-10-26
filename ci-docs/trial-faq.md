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

## Sign-up

### What are the system requirements for the trial?

This app is a cloud-based service that doesn't require special software other than an up-to-date web browser, although some restrictions apply. For the best trial experience, avoid accessing the trial site in incognito mode and choose the trial location closest to you. [Learn more about web application requirements.](/power-platform/admin/web-application-requirements)

### How do I sign up for the trial without a Microsoft 365 tenant?

You can enter a non-work email address and we will create an account and tenant for you.

### Can I sign up for multiple Dynamics 365 apps such as Sales, Marketing, and Customer Service?

Yes, you can. To view all available trials, [visit the trial hub page](https://dynamics.microsoft.com/dynamics-365-free-trial). You can use the same email account to sign up for different trials. However, it is not possible to have multiple apps on the same trial site. Each trial will be on a different org and URL. The trial data won’t be shared across apps.

## Trial app

### I didn't receive the trial details email after signing up, what should I do?

When you sign up for the trial, you'll receive an email with the trial details. If you don't see the email in your inbox, check your spam folder. Alternatively, use the following steps to access your app:

1. Go to the trial site and select **Try for free**.
1. Enter the email ID that you used to sign up for the trial. You'll be redirected to your trial app.

### How do I add more users to a trial?

To add users, go to the [Microsoft 365 admin center](https://admin.microsoft.com) using the trial admin account. Follow the [admin center guidance](/microsoft-365/admin/add-users/add-users) to add users up to the trial license limit. If the user you are adding already has a Microsoft 365 account, assign them an appropriate security role in the trial org. For more information, see [Assign a security role to a user](/power-platform/admin/create-users-assign-online-security-roles#assign-a-security-role-to-a-user).

### How many users can I add to my trial environment?

You can add an unlimited number of users to the trial environment.

### How do I reset the trial environment?

You can't reset the trial environment. However, you can wait for the trial period to end and then sign up again for a new trial.

## Trial expiration and extension

### How do I extend the trial?

You can extend the trial in the app directly. You can extend your trial once.

### Can I convert the trial to a paid license?

Generally, we recommend starting fresh with your own data when upgrading to the paid version of Customer Insights. 

Optionally, if you only use audience insights, you can copy your data from a trial environment if you purchase Customer Insights. You must be the administrator of the Customer Insights trial and the global admin of your Microsoft 365 tenant, or the Dynamics 365 administrator in your organization to migrate the settings from a trial environment to a paid environment. 

After signing in to your paid instance of Customer Insights for the first time, you're asked to create a new environment. In this process, you can choose to copy the configuration from an existing environment and migrate most of the settings. If you have the permissions mentioned above, the trial environment will show in this list. For more information, see [Copy the environment configuration](audience-insights/manage-environments.md#copy-the-environment-configuration).

### What are the trial limits and quotas?

- You can't use your own Azure Data Lake storage account to store output data during a trial of audience insights. However, you can ingest data from a Data Lake storage account.
- You can store a up to 3 GB of data in the Dataverse environment that gets provisioned automatically when you start a Customer Insights trial.

## Customer Insights-specific questions

### How do I start using the trial?

After you sign up for the trial, you will arrive on the app's main screen. The main screen provides links to user guides and tutorials. To learn more, visit the links in the [Additional resources](trial-signup.md#additional-resources) on the trial sign-up page.

### What features are available in the trial?

Most features of the Customer Insights capabilities are available in the trial.

The following feature is not available: 
- You can't create new environments that use your own Azure Data Lake storage account.

### How long does the trial last?

The Customer Insights trial lasts 30 days. You can extend the trial once after 23 days when you sign in to your trial environment.

### How do I remove sample data from the trial?

You can't remove the sample data from the trial.
