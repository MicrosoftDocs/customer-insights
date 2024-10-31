---  
title: "Dynamics 365 Customer Insights trial FAQ"
description: "Solutions to common questions related to Customer Insights trial setup and management. Learn how to resolve platform and app-specific issues."
author: JimsonChalissery
ms.author: jimsonc
ms.date: 10/25/2024
ms.topic: get-started
ms.custom: template-trial-faq
ms.reviewer: mhart
---

# Dynamics 365 Customer Insights trial FAQ

## Sign-up

### What are the system requirements for the trial?

This app is a cloud-based service that doesn't require special software other than an up-to-date web browser, although some restrictions apply. For the best trial experience, avoid accessing the trial site in incognito mode and choose the trial location closest to you. [Learn more about web application requirements.](/power-platform/admin/web-application-requirements)

### How do I sign up for the trial without a Microsoft 365 tenant?

You can enter a non-work email address and we will create an account and tenant for you.

### Can I sign up for multiple Dynamics 365 apps such as Sales and Customer Service?

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

Once you have a paid license, you can't convert your trial instance of Customer Insights - Data to production. To save your work, as the administrator, you can copy the trial settings to a production instance. 

To copy the trial settings to a production instance, you must begin with a **Production** type Power Platform environment. You can create a production environment once you have a paid Dynamics 365 Customer Insights license on your tenant: 
1. Go to [admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com) and create an environment of the desired type (production, sandbox, or subscription-based trial).
1. To install Dynamics 365 applications, you must activate the "Enable Dataverse" and "Enable D365 Apps" toggles for the environment to allow apps.

Back in Customer Insights - Data, you can create a new instance and associate it with the new production environment you just created and copy the settings and configuration you created in the trial: 
1. In Customer Insights - Data, in the upper right corner open the environment chooser and select **+ New**. 
1. Choose the "Copy from existing environment" checkbox and select your trial environment from the dropdown to copy data from.
1. When it asks you which Dataverse environment to associate with, choose the new production environment you created. 

After signing in to your paid environment of Customer Insights for the first time, you're asked to create a new environment. In this process, you can choose to copy the configuration from an existing environment and migrate most of the settings. If you have the permissions mentioned above, the trial environment will show in this list. For more information, see [Copy the environment configuration (preview)](manage-environments.md#copy-the-environment-configuration-preview).

### What are the trial limits and quotas?

- You can't use your own Azure Data Lake Storage account to store output data during a trial of Customer Insights. However, you can ingest data from a Data Lake Storage account.
- You can store a up to 3 GB of data in the Dataverse environment that gets provisioned automatically when you start a Customer Insights trial.

## Customer Insights-specific questions

### How do I start using the trial?

After you sign up for the trial, you will arrive on the app's main screen. The main screen provides links to user guides and tutorials. To learn more, visit the links in the [What to try](trial-signup.md#what-to-try) on the trial sign-up page.

### What features are available in the trial?

Most features of the Customer Insights capabilities are available in the trial.

The following features are **not available**:

- You can't create new environments that use your own Azure Data Lake Storage account.
- You can't delete the trial environment.

### How long does the trial last?

The Customer Insights trial lasts 30 days. You can extend the trial once after 23 days when you sign in to your trial environment.

### How do I remove sample data from the trial?

You can't remove the sample data from the trial.
