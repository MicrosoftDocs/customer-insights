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

Engagement insights capability enables business users to measure and understand customer behavior on websites, in mobile apps, and across connected products. The links in this article help you quickly configure and set up your environment.

## Recommended preparations
The following articles explain engagement insights capability prerequisites.

1. Review and agree to the [terms of agreement](preview-terms-of-service.md) with Microsoft.  
4. Review [known issues](known-issues.md).
1. Read the [Manage cookies and user consent](user-consent-storage.md) article. After reviewing this article, you must evaluate whether you need to update your user consent notification. If you previously had no "non-essential" cookies, you'll likely need to update your site policy.

## Set up a workspace
The starting point for any user is set up a workspace. The workspace is where you'll start ingesting web analytics data.

1. Sign in to the [engagement insights capability portal](https://pi.dynamics.com) using your Microsoft Azure Active Directory user account.
1. [Create a workspace](create-workspace.md) and add members.

## Start viewing data

1. Instrument your website with an SDK to see telemetry arriving into your workspace.
1. View a [real-time report](view-reports.md) showing active users by browser, device, operating system, location, and language.
	
## Export events
An event records when a user views a page (view event) or interacts with content (action event). You can create a refined event from web analytics data, filter it, and export it to your Azure Data Lake Storage. You can bring the exported data back into an engagement insights capability as a data source.

1. Create a [refined event](create-modify-refined-events.md) for export activities data.
2. Export the [data](export-events.md) to Data Lake Storage.
3. Learn how to [delete export event data](delete-export-EUII-data.md) containing user personal information.
  
