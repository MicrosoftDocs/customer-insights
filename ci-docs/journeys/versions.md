---
title: Enable outbound marketing and troubleshoot
description: Learn how to enable outbound marketing and troubleshoot version control in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/25/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# What's on the Versions page?
The version page shows you the current version of the solutions on your environment and the status of those solutions relative to what has been released. If there are new solution updates available, select **Manage+Update** to launch the installation management page. Find the environment you'd like to update and select **Check Versions** and then choose **Update**.

# How do I enable outbound marketing?
If you owned the standalone Dynamics 365 Marketing licenses and used the outbound marketing module on your environments prior to September 2023,  you may also see the option to Enable outbound marketing on this environment. In the following scenarios you need to re-enable outbound marketing solutions: 
- If you have performed a copy, backup, or restore of an environment it will show only the real-time journeys solutions in the user experience and will not have any of the services turned on. To add outbound marketing back to the user experience, per the instructions for [copy, backup, and restore](copy-or-restore.md) from the **Versions** page choose **Manage+Update**, find the copy or backup environment and choose **Install**. Once installation has completed, back on the **Versions** page, Enable outbound marketing.
- If you started with a free, solutions only installation of Customer Insights - Journeys and you decide to **Install** journeys to get the services, you must re-enable the outbound marketing user experience on the **Versions** page after the serivces have been installed. 

# Why don't I see the option to enable outbound marketing?
- The check to see if other environments had outbound marketing does not cross geo boundaries. Therefore, if you had outbound marketing in one geo and are creating a new envrionment in another geo, the new geo won't know about outbound marketing usage in the other geo. You must contact support to get outbound marketing enabled in this case. 
- You have a trial. Trials will never have outbound marketing.
- You didn't have any environments which used outbound marketing prior to September, 2023. 
- Solutions only environments do not have the services, only the user experience solutions. The free installation of the solutions includes the outbound marketing user experience and the real-time journeys user experience but none of the services to allow segmentation, journey orchestration, and message execution. If you want to install the services, select **Manage+Update**, find the environment and choose **Install** for the journeys app. Back on the **Versions** page, you see the option to enable outbound marketing user experience and can turn it back on. 
