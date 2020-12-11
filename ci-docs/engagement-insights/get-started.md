---
title: Get started with engagement insights capability
description: An overview of help resources to get started quickly. 
ms.reviewer: ruthai
ms.author: v-salash
author: pickwick129
ms.date: 10/30/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Get started with Dynamics 365 Customer Insights engagement insights capability (public preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Engagement insights capability enables business users to measure and understand customer behavior on websites. With the deep integration with audience insights, you can see rich real-time behavioral analytics alongside customer profile reports. The links in this article help you quickly configure and set up your environment.

## Recommended preparations

Review the following articles before setting up a workspace.

- Review and agree to the [Terms of Service](terms-of-service.md) with Microsoft.  
- Read the [Manage cookies and user consent](user-consent-storage.md) article. After reviewing this article, evaluate whether you need to update your user consent notification. If you previously had no "non-essential" cookies, you'll likely need to update your site policy.
- Review the [glossary](glossary.md) to get a quick introduction about key terms and concepts. 

## Set up a workspace
The starting point for any user is to set up a workspace. The workspace is where you'll start ingesting web analytics data.

1. Sign in to the [engagement insights capability portal](https://pi.dynamics.com) using your Microsoft Azure Active Directory user account.
1. [Create a workspace](create-workspace.md) and add members.

## Start viewing data

1. [Instrument your website](instrument-website.md) with an SDK to see telemetry arriving into your workspace.

1. View a [real-time report](view-reports.md) showing active users by browser, device, operating system, location, and language. You can also create [custom reports](custom-reports.md) to create your own visualizations.
	
## Export events

An event records when a user views a page (view event) or interacts with content (action event). You can create refined events from web analytics data, filter it, and export it to your Azure Data Lake Storage. You can ingest the exported data as a data source in audience insights.

1. [Create refined events](refined-events.md) for export.

1. [Export the data](export-events.md) to Data Lake Storage.

1. Learn how to [delete and export event data containing personal information](delete-export-personal-data.md).
 
## Stay connected

We appreciate your active participation and plan to consider all relevant feedback in developing future releases. Share your feedback and report issues by one of these channels:
- [Community](https://go.microsoft.com/fwlink/?linkid=2141648)
- [Provide feedback](https://go.microsoft.com/fwlink/?linkid=2143222)
- [Request support](https://go.microsoft.com/fwlink/?linkid=2145734) 
