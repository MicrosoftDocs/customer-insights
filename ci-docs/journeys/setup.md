---
title: Install and manage Customer Insights
description: Learn how to install, uninstall, and manage Dynamics 365 Customer Insights environments with step-by-step guidance and troubleshooting tips.
ms.date: 04/16/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:04/16/2025
---

# Install and manage Dynamics 365 Customer Insights

This article explains how to access and use the installation management area for Customer Insights. In this one-stop experience, you can manage to install and uninstall the Customer Insights - Journeys and Customer Insights - Data applications.

All of your Dataverse environments for the geo you selected in the Power Platform Admin Center are listed in the installation management area by type (**Production** or **Trial**). You can see where Customer Insights – Journeys and Customer Insights – Data are installed and take action to install or uninstall.

## Prerequisites and requirements

To install Customer Insights, ensure you meet all the following requirements:

- Make sure you already have a Microsoft 365 tenant.
- Ensure your tenant has a Dynamics 365 Customer Insights, Dynamics 365 Marketing, or Dynamics 365 Customer Insights – Standalone license.
- Sign into your tenant with a user account that has all the following:
   - A security role (such [_Service support admin_](/power-platform/admin/use-service-admin-role-manage-tenant)) that allows you to modify the target Dynamics 365 environment. (If you're reinstalling Customer Insights on an environment where Customer Insights was previously installed, then _Service support admin_ users [_Dynamics 365 administrator_ or _Power Platform administrator_] must use the same user ID as was used for the initial install.
   - Permissions to register applications in Azure. See [Do I have permissions to register applications on Azure?](setup-troubleshooting.yml#register-apps-azure) for information about how to confirm this setting for your account.
   - A Dynamics 365 license with the _System Administrator_ security role assigned on your target Dynamics 365 environment. (The Customer Insights license agreement doesn't legally require the installing user to have this license, but a known technical issue currently makes it necessary.)
- You must be located in a country/region where the product is supported. To read the latest list of countries/regions where you can use Customer Insights, download the [Microsoft Dynamics 365 International Availability](https://go.microsoft.com/fwlink/p/?linkid=875097) document (PDF).
- You must disable the [Block unmanaged customizations](/power-platform/admin/settings-features#block-unmanaged-customizations) setting in your environment. To do so, go to [admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com) > **Environments** and select the three dots ("**...**") next to the environment name. Then go to **Settings** > **Product** > **Features**, and set the toggle next to **Block unmanaged customizations** to **Off**. Learn more: [Block unmanaged customizations in Dataverse](/power-platform/alm/block-unmanaged-customizations)

Before starting the installation, close all other browser windows and tabs, and clear your browser cache. If you run into trouble while installing, see the [Administration and setup FAQ](setup-troubleshooting.yml) for some possible solutions.

## Install, uninstall, or update Customer Insights

The following sections explain how to install, uninstall, or update the Customer Insights apps.

### Install

Customer Insights - Journeys is installed as a **paid installation** or **trial** that includes the services and lets you send messages, execute journeys, and use the other functionalities in the app. If you have paid licenses, you can install Customer Insights - Journeys or Customer Insights - Data on sandbox and production environments. If you have an admin trial license, you can install on subscription-based trial environments.  

If you **Uninstall** Customer Insights - Journeys (paid or trial), the services disconnect, and the environment only includes the user experience solutions without the services needed to send emails, process segments, or use other features. If your environment is in this state, you see a banner at the top of the application indicating that the environment only has the user experience solutions installed but not the services. To make the environment functional, install the application.

> [!NOTE]
> As of June 30, 2024 there are no longer application installation limits for Dynamics 365 Customer Insights - Journeys (real-time only) or Dynamics 365 Customer Insights - Data. Outbound marketing solutions are still limited to the prior application installation limits. If you own a legacy Dynamics 365 Marketing license, you're allowed one outbound marketing solution installation per license purchased. If you own the current Dynamics 365 Customer Insights license, you can add outbound marketing up to four times per base license.

#### Set up or access a Customer Insights - Journeys environment

If you don't already have one, you must first create an environment in [Microsoft Power Platform admin center](/power-platform/admin/). Follow these steps to create an environment:

1. Go to [admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com) and create an environment of the desired type: production, sandbox, or subscription-based trial.
1. Turn on the "Enable Dataverse" and "Enable D365 Apps" toggles for the environment to allow apps. 

Learn more: [Create and manage environments in the Power Platform admin center](/power-platform/admin/create-environment)

#### Install Customer Insights - Journeys and Customer Insights - Data

1. On the [admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com) page, find **Resources** in the left-hand site map and select **Dynamics 365 apps**.
1. Select the geo in the upper-right corner of the Power Platform Admin Center that matches the target environments for installation. Find either **Dynamics 365 Customer Insights** or **Dynamics 365 Marketing** in the list and select the three dots ("**...**") next to the app name, then select **Manage**.
1. In the installation management area, you see your available environments listed and can choose where you want to install Customer Insights - Journeys or Customer Insights - Data. To install either application, select **Install**. If you don't own any paid licenses and want to learn how to buy, select **Buy now**. If you have trial licenses, use the **Trial** tab to install on a subscription-based trial environment or manage a viral trial.
1. If the installation fails, select **Diagnose** to learn more about the failure and check if you need to do anything differently. If no actionable reason exists for the failure, select **Retry**.

:::image type="content" source="media/new-installation.png" alt-text="Installation management area screenshot." lightbox="media/new-installation.png":::

#### Connect Customer Insights - Journeys and Customer Insights - Data on the same environment

After you've installed the Customer Insights - Journeys and Customer Insights - Data apps on the same environment, you need to finish connecting them.

##### Create the connection

To connect the apps: 

1. Go to **Customer Insights - Journeys** then go to **Settings** > **Data Management** > **Customer Insights** and select the **Connect** button.
1. This may have been done automatically if it's the first time you're connecting this environment. This completes the data sync for segmentation between the two applications.

##### Finish the setup in Customer Insights - Data

In Customer Insights - Data there are a few more steps to connect the Dataverse environment and start generating profiles based on the contact and lead entities in Dataverse, in addition to adding more data sources.

1. On the installation management page, select the **checkmark** icon ![Checkmark icon](media/check-icon.png "Checkmark icon") next to the "Installed" text to find a link to open the Customer Insights - Data environment. In Customer Insights - Data, go to **Data** > **Data sources**, select **Add Data Source**, and choose **Dataverse**. Populate the URL with the environment URL from the Customer Insights - Journeys Dataverse environment. Select the contact and lead tables only, then select **Save**. Learn more: [Connect to Dataverse](/dynamics365/customer-insights/data/connect-dataverse#connect-to-dataverse)
1. In **Unify**, to add the Customer Insights - Journeys contacts and leads to the profile and proceed with unification settings, choose the contact from the tables you ingested with *ContactId* as the primary key and fields like "email address" and "phone number" in the deduplication rules. Choose the lead with *LeadID* as the primary key and fields like "email address" and "phone number" as deduplication rules. Learn more: [Data unification overview](/dynamics365/customer-insights/data/data-unification)

##### Clear the connection

You might need to clear the connection between the apps if you uninstall and reinstall Customer Insights - Data with a new instance ID.

To clear the connection: 

1. Uninstall Customer Insights - Data from the environment, then go to [the Power Apps Maker portal](https://make.powerapps.com) and select **Tables**. 
1. Find the table labeled **msdynmkt_configurations** and set the **CXPConfig row column name "Customer Insights Status"** attribute to **NotConfigured**. This resets the connection and allows you to select **Connect** again after you've reinstalled a new instance of Customer Insights - Data.  

#### Troubleshooting a failed installation

Installations can fail for many reasons unrelated to or undetectable by the Dynamics 365 Customer Insights - Journeys application. When you request an installation, Microsoft decrements your application quota (in case you start multiple installations at a time) and requests the package installation from the platform. Once the platform tries to install the package, it can run into any number of issues in your specific environment including plugins that need to be disabled, dependencies in the Dataverse entity model that the journeys application relies on such as for leads or contacts, dependencies, security, or customizations.

If your installation fails, select **Learn more** or **Diagnose** to get details about the failure. You see a **Retry** link where the **Install** link was. Before you **Retry**, you can do some checking on your environment to see if there's anything you need to do to prepare it to allow the solution installation.

- Select **Learn More** to receive directions on the installation failure and steps you can take to resolve it. 
- You must have a paid license on the tenant.
- You must be the admin of the environment to install the application. 
- Disable any custom plug-ins before installing.
- If users own records in Dataverse and have left the company, those records may be locked and the installation is unable to write to them, for example, the DataLake folder which analytics must access. Update the ownership of these records to an active user. 
- Check your solutions using the solution checker to learn what failed. You may have customizations or plugins which need to be disabled. Learn more: [Troubleshoot issues with Solution Health Hub](troubleshoot-marketing-solution-health.md)
- You can go to the solutions history view in the Maker portal to see what failed and what actions you can take to prepare your environment for a successful install. Learn more: [View the history of a solution](/power-apps/maker/data-platform/solution-history/)

If your installation fails and you want to abandon the installation, you must achieve a successful installation so that you can run the uninstall process to free up the license and disconnect any services that may have succeeded during the parts of the installation process that didn't fail. If you still can't resolve the issue after attempting using the solution checker or visiting the solution history in the Maker portal, you should [file a support ticket](troubleshoot-faq.md#how-can-i-create-a-support-ticket-from-the-power-platform-admin-center) and get help to achieve a successful installation.

### Uninstall

Find detailed guidance for [uninstalling Dynamics 365 Customer Insights - Journeys](uninstall.md).

### Update

Dynamics 365 Customer Insights - Journeys releases updates every month with new features and fixes. When there's a new release available, you can see it in **Settings** > **Versions**. Select **Manage+Update** to launch the installation management page. Select **Check version** to see if any updates are available. Select **Update packages** if updates are available.

## Maintain or update your installation

Use the installation management area to modify, maintain, or update your installation after installing Customer Insights for the first time. You can:

- Check for and apply [updates](apply-updates.md)
- Fix installation issues
- Connect a disconnected instance to marketing services
- Clean up after a [copy or restore operation](copy-or-restore.md)
- [Uninstall](uninstall.md) Customer Insights - Journeys

## Privacy notice

[!INCLUDE [cc-privacy-marketing-fre](./includes/cc-privacy-marketing-fre.md)]

### Collecting feedback data

To refine and improve the experience, Microsoft might collect feedback data from users within the app. Admins can disable survey feedback by using a PowerShell command to set the **disableSurveyFeedback** flag to **true**. For more information, see the [list of tenant settings](/power-platform/admin/list-tenantsettings).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
