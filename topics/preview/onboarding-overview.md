---
title: Onboarding to the private preview
author: ruthaisabokhae
description: Learn what you need to do to take advantage of the private preview capabilities of Dynamics 365 Product Insights
ms.author: ruthai
ms.date: 08/13/2020
ms.service: product-insights
ms.topic: conceptual
robots: noindex,nofollow
---

# Onboard to the Product Insights private preview

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

This onboarding article describes Dynamics 365 Product Insights' private preview product features, documentation, scenarios to validate, and known issues, and explains how to engage with Microsoft throughout the private preview. Nothing in this documentation is meant to&mdash; or should be construed to&mdash; modify the terms of your agreements with Microsoft, including your preview terms.

## Onboarding overview

1.	Review and agree to the [nondisclosure and preview agreement](preview-terms-of-service.md) with Microsoft.  
2.	Review [capabilities outlined in this article](#private-preview-capabilities) for private preview.  
3.	Review and understand[expectations](#private-preview-expectations) described in the following section, and [known issues](known-issues.md) of the private preview.  
4.	Validate the [core scenarios](#product-use-cases-to-test) and provide feedback to Microsoft.

## Private preview expectations

*	Private preview is for testing purposes only. Environments might be taken down at the end of the testing period to make way for future releases. See the [Preview terms of service](../preview/preview-terms-of-service.md) for more disclosures and limitations.  
*	Private preview isn't for production use, but rather is strictly for prototyping and providing feedback. We're likely to delete data and rebuild environments at any point during the private preview, but we'll make reasonable effort to ensure that we communicate any changes to avoid disruption in testing.   
*	We',ll work closely with you to seek feedback and incorporate product changes. We expect to establish a cadence for this interaction during the period of private preview and we'll communicate that when we do.  
*	Private preview is expected to run for approximately two months (August through September, 2020). We appreciate your active participation, and plan to consider all relevant feedback  in developing future releases.  
*	Reach out to your assigned product manager first, or use the email **[pirequest@microsoft.com](mailto:pirequest@microsoft.com)**, to provide feedback and report issues. We 'll use reasonable effort to triage reported issues, prioritize them, track them, and share their status with you regularly.  
	
## Prerequisites

*	Access to a production website with authentication for your customers to instrument the Product Insights SDK.
*	Access to a test environment for [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/ai/customer-insights/) to test the integration of data.
*	Access to, or ability to create, an Azure Data Lake Storage account for export.

## User consent for use of cookies

1.	Read the [Manage cookies and user consent](user-consent-storage.md) article.
2.	After reviewing this article, you must evaluate whether you need to update your user consent notification. If you previously had no "non-essential" cookies, you'll likely need to update your site policy.

## Private preview capabilities

### First-run experience

The starting point for any user is signing in to Product Insights in which the organization is generated and your own environment and projects are created. This is where you'll be able to start ingesting your web analytics data.

### Web SDK

The JavaScript library for your website to measure user interaction with the provided sample code.

### Web analytics and reports

The out-of-the-box reports show the events coming through from the Web SDK with predefined visualizations and dashboards.

### Refined events

The capability to create a refined event from the web analytics data, filter it, and export it to your Data Lake Storage. The exported data in Data Lake Storage can be imported into Customer Insights as a data source.

## Product use cases to test

### Setup and provisioning steps

1.	Before you start, ensure you've read and agreed to the [Preview terms of service](preview-terms-of-service.md).
2.	Sign in to the [Dynamics 365 Product Insights portal](https://pi.dynamics.com) using your Microsoft Azure Active Directory user account.
3.	Follow the steps in the [quickstart](quickstart-product-insights.md) article to set up your project.
4.	Review the [known issues](known-issues.md).

### First-run experience

1.	 Follow the account creation process. Set up and create your project, and then add members.
2.	 Instrument website with the SDK to see telemetry arriving into your project.
3.	 View the real-time report showing active users by device, page view trend, top pages, top referrers, and users’ geographic locations.


### Export data from Product Insights

  1.	Customize your website instrumentation by ensuring that you send an *authid* for each user signing in to your site.
  2.	Create a refined event for export activities data.
  3.	Export the data to Data Lake Storage.
  4.	Optional: Ingest Product Insights data export as activities in Customer Insights, and view it as part of a customer profile.
  
