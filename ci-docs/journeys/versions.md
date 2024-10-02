---
title: Use the versions page to enable outbound marketing
description: Learn how to enable outbound marketing and troubleshoot version control in Dynamics 365 Customer Insights - Journeys.
ms.date: 05/16/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Use the versions page to enable outbound marketing

This article addresses troubleshooting issues related to the versions page and enabling outbound marketing.

## What's on the versions page?

The versions page shows you the current version of the solutions on your environment and the status of those solutions relative to what's been released. You can also see if outbound marketing is available to enable using a self-service link or request form. If there are new solution updates available, select **Manage+Update** to launch the installation management page. Find the environment you'd like to update and select **Check Versions** and then choose **Update**.

## How do I enable outbound marketing?

If you have outbound marketing installed on one or more of your environments in the same geography, you see a self-service link to **Enable outbound marketing** on the current environment. Otherwise, you can request it [through this form](https://go.microsoft.com/fwlink/?linkid=2272241) and, if you qualify, outbound marketing can be enabled for you. If you need Power Apps portals provisioned on your outbound marketing instance, you can provide the details in [this request form](https://go.microsoft.com/fwlink/?linkid=2272236) and portals can be added to outbound marketing for you. 

In the following scenarios, you need to re-enable outbound marketing solutions:
- If you've performed a copy, backup, or restore of an environment, you only see the real-time journeys solutions in the user experience and don't have any of the services turned on. To add outbound marketing back to the user experience, per the instructions for [copy, backup, and restore](copy-or-restore.md), go to the **Versions** page, choose **Manage+Update**, find the copy or backup environment, and choose **Install**. Once installation has completed, go back to the **Versions** page and select "Enable outbound marketing."
- If you started with a free, solutions-only installation of Customer Insights - Journeys and you decide to **Install** Customer Insights - Journeys to get the services, you must re-enable the outbound marketing user experience on the **Versions** page after the services have been installed.

## Why don't I see the option to enable outbound marketing?

- The check to see if other environments had outbound marketing doesn't cross geographic boundaries. Therefore, if you had outbound marketing in one geo and are creating a new environment in another geo, the new geo won't know about outbound marketing usage in the other geo. In this case, follow the guidance for [requesting outbound marketing to be added](transition-overview.md#if-the-enable-link-isnt-available-or-doesnt-work)
- You have a trial. Trials will never have outbound marketing.
- You didn't have any environments in the same geography as the current environment with outbound marketing installed.
- Solutions-only environments don't have the services, only the user experience solutions. The free installation of the solutions includes the outbound marketing user experience and the real-time journeys user experience but none of the services to allow segmentation, journey orchestration, and message execution. If you want to install the services, select **Manage+Update**, find the environment, and choose **Install** for the Customer Insights - Journeys app. Back on the **Versions** page, you then see the option to enable the outbound marketing user experience and can turn it back on.
