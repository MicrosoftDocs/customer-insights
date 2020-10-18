---
title: Get started with Dynamics 365 Customer Insights engagement insights capability (public preview)
description: An overview of resources to get started quickly. 
ms.reviewer: ruthai
ms.author: v-salash
author: pickwick129
ms.date: 10/18/2020
ms.service: customer-insights
ms.subservice: 
ms.topic: conceptual
ms.manager: shellyha
---

# Get started with Dynamics 365 Customer Insights engagement insights capability (public preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Welcome to the public preview of engagement insights capability. Engagement insights capability enables business users to measure and understand customer behavior on websites, in mobile apps, and across connected products. This article  provides links to articles so you can quickly set up your environment and get started.

## Prerequisites
The following topics explain service prerequisites and how to set up your environment.

1. Review and agree to the [nondisclosure and preview agreement](preview-terms-of-service.md) with Microsoft.  
2. Sign in to the [Dynamics 365 Customer Insights engagement insights capability portal](https://pi.dynamics.com) using your Microsoft Azure Active Directory user account.
4. Review [known issues](known-issues.md).
1. Read the [Manage cookies and user consent](user-consent-storage.md) article. After reviewing this article, you must evaluate whether you need to update your user consent notification. If you previously had no "non-essential" cookies, you'll likely need to update your site policy.

## Set up a workspace and add members
The starting point for any user is set up a workspace. The workspace is where you'll start ingesting web analytics data.

1. [Create a workspace](create-workspace.md) and add members.
1. Instrument the website with an SDK to see telemetry arriving into your project.
1. View a [real-time report](view-reports.md) showing active users by device, page view trend, top pages, top referrers, and users’ geographic locations.
	
## Export events
An event records when a user views a page (view event) or interacts with content (action event). You can create a refined event from the web analytics data, filter it, and export it to your Data Lake Storage. The exported data in Data Lake Storage can be imported into an engagement insights capability as a data source.

1. Create a [refined event](create-modify-refined-events.md) for export activities data.
2. Export the [data](export-events.md) to Data Lake Storage
3. Learn how to [delete export event data](delete-export-EUII-data.md) containing end user identifiable information
  
