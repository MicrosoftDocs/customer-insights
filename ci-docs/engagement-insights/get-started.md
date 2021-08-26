---
title: Get started with engagement insights capability
description: An overview of help resources to get started quickly. 
ms.reviewer: mhart
ms.author: jefhar
author: mochimochi016
ms.date: 12/21/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
ms.custom: intro-internal
---

# Get started with Dynamics 365 Customer Insights engagement insights capability (public preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Engagement insights capability lets you collect and measure customer behavior on your website. It integrates with audience insights capability so you can see rich real-time behavioral analytics alongside customer profile reports. The links in this article help you quickly configure and set up your environment.

## Step 1: Review prerequisites

First, you must have an active Microsoft Azure Active Directory user account. Then, read the following articles before setting up an engagements insights workspace.

- Review and agree to the [Terms of Service](terms-of-service.md) with Microsoft.  
- Read the [Manage cookies and user consent](user-consent-storage.md) article. After reviewing this article, evaluate whether you need to update your user consent notification. If you previously had no "non-essential" cookies, you'll likely need to update your site policy.
- Review the [glossary](glossary.md) for a quick introduction to key terms and concepts.

## Step 2: Explore engagement insights

The first time you visit engagement insights you can configure settings, review policies, and explore the product.

1. Sign in to the [engagement insights capability portal](https://pi.dynamics.com) using your Microsoft Azure Active Directory user account. (It can be your school or work account.)

1. Select your region, and use the check box to indicate whether you want to opt in to receive updates and offers via email.

1. Review the **engagement insights (preview) Terms of Use** and **Privacy Statement**, and then select **Explore the demo** to accept them.

1. Explore the product using a set of sample data.

##  Step 3: Set up a workspace and add code to your website

The workspace is where you can view user activity in real time, and store and manage reports. Add code to your website to start collecting *events*, the activity data that comes in from users.

1. [Create a workspace](create-workspace.md) and add members.

1. [Add code to your website](instrument-website.md) or [mobile app](developer-resources.md#capture-events-from-mobile-apps) to see user activity arriving into your workspace.

1. View a [real-time report](view-reports.md) showing active users by browser, device, operating system, location, and language. You can also create [custom reports](custom-reports.md) to create your own visualizations.
	
## Step 4: Export data to other channels

You can create *refined events* (a virtual view) of your web analytics data. Then filter and export the data to Azure Data Lake Storage. You can ingest the exported data as a data source. For more information, see [Create a link between audience insights and engagement insights](integrate-audience-insights-engagement-insights.md).

1. [Create refined events](refined-events.md) for export.

1. [Export the data](export-events.md) to Data Lake Storage.

1. Learn how to [delete and export event data containing personal information](delete-export-personal-data.md).
 
## Step 5: Stay connected

We appreciate your active participation and plan to consider all relevant feedback in developing future releases. Share your feedback and report issues by one of these channels:
- [Community](https://go.microsoft.com/fwlink/?linkid=2141648)
- [Provide feedback](https://go.microsoft.com/fwlink/?linkid=2143222)
- [Request support](https://go.microsoft.com/fwlink/?linkid=2145734) 


[!INCLUDE[footer-include](../includes/footer-banner.md)]
