---
title: Keep Customer Insights - Journeys up to date
description: Find out when an update for one or more Dynamics 365 Customer Insights - Journeys solutions is available and apply the update.
ms.date: 09/13/2023
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Keep Dynamics 365 Customer Insights - Journeys up to date

Microsoft is continuously developing and improving online services. Customer Insights - Journeys updates are [pushed to all customers automatically](https://cloudblogs.microsoft.com/dynamics365/it/2020/04/27/automatic-update-policy-for-dynamics-365-marketing/). Customer Insights - Journeys follows a phased deployment approach aligned with the platform deployment schedule. You can also update your solutions manually for early validations. Manual updates allow customers to apply and test updates on a sandbox instance before applying them to a production system.

This article gives an overview of how to update Customer Insights - Journeys and its related solutions.

## Solutions included with Customer Insights - Journeys

Customer Insights - Journeys is implemented using several *solutions*. A *solution* is a type of software package that adds functionality to model-driven apps in Dynamics 365 (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Customer Insights - Journeys, and Dynamics 365 Project Service Automation). Customer Insights - Journeys includes several solutions that are unique to the Customer Insights - Journeys app, plus a few more that are available as separate apps or in other app bundles.

When you install Customer Insights - Journeys, all its solutions are installed in the installation management area. However, when updating Customer Insights - Journeys, you'll need to monitor and update each of the following types of solutions separately:

- **Core Customer Insights - Journeys solutions**: These are the solutions that provide core features that are unique to Customer Insights - Journeys (including the Dynamics 365 Connector for LinkedIn Lead Gen Forms). Though there are several of these, you'll be able to maintain and update them all at once using the installation management area.
- **Dynamics 365 Customer Voice**: This solution enables model-driven apps in Dynamics 365 to host surveys and collect responses. It's also available as an add-on or bundle for other apps. You must update this solution separately from the other solutions included with Customer Insights - Journeys, using its own update program.
- **Power Apps portals** (outbound marketing only): This solution enables model-driven apps in Dynamics 365 to host interactive portals that display and collect Dynamics 365 data, including the events portal and marketing pages. Like Customer Voice, you must update this solution using its own update program.

## Find out when new updates are available

Microsoft releases updates to Customer Insights - Journeys every month or so, with a major refresh every six months. We announce monthly updates (and other news) in the [What's new in Dynamics 365 Customer Insights - Journeys](whats-new-marketing.md) page, where we also summarize all the new features and bug fixes included with each release. Future directions and major releases are described on the [Dynamics 365 and Power Platform Release Plans](/business-applications-release-notes/index) website.

You can also find out when an update is available by checking the status of your apps and solutions in the Customer Insights - Journeys settings, as described in the following sections.

## Find out which version of Customer Insights - Journeys you are running

Customer Insights - Journeys includes several solutions and services, each of which has its own version number. You'll often see versions of Dynamics 365 referred to by the month or season and year they came out, but to find a unique identifier for the version installed on your tenant, check the version number of your **Dynamics 365 Customer Insights - Journeys** solution as follows:

1. Go to the [installation management area](setup.md#install-uninstall-or-update-customer-insights).

1. Select **Update** next to the instance that you want to check the version on.

## Find and apply updates for core solutions

To find and apply available updates to all core Customer Insights solutions:

1. Go to [**admin.powerplatform.microsoft.com**](https://admin.powerplatform.microsoft.com). Find the Dynamics 365 apps list in the left-hand site map and select **Resources**.
    - Whether you have the legacy, standalone Dynamics 365 Customer Insights app or Dynamics 365 Marketing licenses (available to customers who purchased before September 2023) or the new, combined Dynamics 365 Customer Insights license that contains both the journey orchestration and customer data platform applications together in one SKU, you can find them listed in admin.powerplatform.microsoft.com under **Dynamics 365 apps** > **Resources**.

1. To open the installation management area, select the three dots dropdown ("**...**") then select **Manage**.

1. Select the **Update** button next to the instance you want to update. The update starts right away and will tell you when it's finished.

1. Repeat this procedure for each Customer Insights - Journeys organization that you have.

## Find and apply updates for shared Customer Insights - Journeys solutions

> [!WARNING]
> Always check for and apply core Customer Insights - Journeys solution updates using the installation management area (as described in the [previous section](#find-and-apply-updates-for-core-solutions) *before* you look for shared solution updates. You will also see core Customer Insights - Journeys solutions listed when you follow the instructions provided in this section, but you risk breaking your installation if you try to update core Customer Insights - Journeys solutions from here, even if they show an update is available.

To update shared (non-core Customer Insights - Journeys) solutions, including Customer Voice and Power Apps portals:

1. Go to [admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com), then go to **Environments** on the left navigation pane.

    ![Open the Environments page.](media/apply-updates-environments.png "Open the Environments page")

1. If you have more than one environment, each will be listed here. To select the environment where you have Customer Insights - Journeys installed, select the environment name.

    ![Select the Environment name.](media/apply-updates-environment-name.png "Select the Environment name")

1. You will now be on a page showing environment details include **Access** permissions, **Auditing** information, the database **Version**, **Updates**, and **Resources**. You also convert your environment to a sandbox or create a backup from this page. To view the solutions installed in this environment, go to **Resources** > **Dynamics 365 apps**.

    ![Select Dynamics 365 apps in your environment.](media/apply-updates-dynamics-365-apps.png "Select Dynamics 365 apps in your environment")

1. A list of solutions installed on your selected environment is shown. Look in the **Status** column for any solutions that show a value of "Update available." The solutions that are relevant for Customer Insights - Journeys are "Power Apps portals – Base Portal" and "Dynamics 365 Customer Voice."  

   > [!WARNING]
   > As mentioned at the start of this procedure, you must not update core Customer Insights - Journeys solutions from here. Always update the app from the installation management area first, before you start looking for shared-solution updates. Be sure not to update any of the core Customer Insights - Journeys solutions while you are updating the shared solutions, even if they show an update is available.

    ![Select a solution to update.](media/apply-updates-update-available.png "Select a solution to update")

1. Select a solution marked as having an update available and read the information shown in the side panel. Select the **update** button in the side panel and then follow the instructions on your screen to apply it.

1. Repeat this procedure for each solution that requires an update.

## Update event websites

If you have created a [Portal hosted event website](./developer/portal-hosted.md), you must [manually overwrite your sample website with the latest version](./developer/manually-overwriting-sample-website.md) to maintain functionality after applying any Customer Insights - Journeys update.

If your event website is [self-hosted](./developer/self-hosted.md), you must [install the latest self-hosted sample website](./developer/event-management-web-application.md) to maintain functionality after applying any Customer Insights - Journeys update.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
