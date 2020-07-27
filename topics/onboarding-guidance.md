---
uid: topics/onboarding-guidance
title: Onboarding to the Private Preview
author: ruthaisabokhae
description: Framework for onboarding
ms.author: ruthai
ms.date: 07/27/2020
ms.service: product-insights
ms.topic: conceptual
---

# Onboard to the Private Preview of Product Insights

[!INCLUDE [cc-beta-prerelease-disclaimer]( includes/cc-beta-prerelease-disclaimer.md)]

The goal of this onboarding article is to give Private Preview participants visibility to the product features, documentation, scenarios to validate, known issues, and how to engage with Microsoft throughout the Private Preview. Nothing in this documentation is meant to, or should be construed to, modify the terms of your agreements with Microsoft, including your Preview Terms.

## Onboarding overview

*	Review and agree to NDA/Preview Agreement with Microsoft.  
*	Review [capabilities outlined in this article](#private-preview-features) for Private Preview.  
*	Review and understand the [expectations](#private-preview-expectations) and [known issues](#known-issues) of the Private Preview.  
*	Validate the [core scenarios](#product-use-cases-to-test) and provide feedback to Microsoft.

## Private Preview expectations

*	Private Preview is for testing purposes only. Environments may be taken down at the end of the testing period to make way for future releases. See the [Preview Terms](preview-terms.md) for more disclosures and limitations.  
*	Private Preview is not for production use, and strictly for prototyping and providing feedback. We are likely to delete data and rebuild environments at any point during the Private Preview but will make reasonable efforts to ensure communication of any changes to avoid disruption in testing.  
*	We will work closely with you to seek feedback and incorporate product changes. We expect to establish a cadence for this interaction during the period of Private Preview and will communicate that subsequently.  
*	Private Preview is expected to run approximately for two months (August and September 2020) and we appreciate your active participation. We plan to consider all relevant feedback into our future releases.  
*	Please reach out to your assigned product manager first or use the email **[pirequest@microsoft.com](mailto:pirequest@microsoft.com)** to provide feedback and report issues. We will use reasonable efforts to triage reported issues, prioritize them, track them, and share a status with you regularly.  

## Prerequisites

*	Access to a production website with authentication for your customers to instrument the Product Insights SDK.
*	Access to a Test environment for [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/ai/customer-insights/) to test the integration of data.
*	Access to (or ability to create) an Azure Data Lake Storage (ADLS) Gen 2 account (for export).

## User consent for use of cookies on your site

*	For more information, see [Manage cookies and user consent](user-consent-storage.md).
*	The [Getting started](first-run-experience.md) article highlights that the code automatically collects page views and actions.
*	After reviewing these documents, you must evaluate if there is need for an update to your user consent notification. If you previously had no "non-essential" cookies, then this will likely require an update to your site policy, etc.

## Private Preview features

### First run experience

The starting point for any user signing in to Product Insights in which the organization is generated and your own environment and workspace are created. This is where you'll be able to start sending you web analytics data.

### Web SDK

The JavaScript library for your website to measure user interaction with the provided sample code.

### Web analytics and reports

The out-of-the-box reports show the events coming through from the Web SDK with predefined visualizations and dashboards.

### Derived signals

The capability to create a derived signal from the web analytics data, filter it and export it to your Azure Data Lake Storage. The exported data in ADLS can get imported into Customer Insights as a data source.

## Product use cases to test

## Setup and provisioning steps

*	Before you start, please ensure you have read and agree to the [Preview Terms of Service](preview-terms.md) provided.
*	Sign in to the Dynamics 365 Product Insights portal using your Microsoft Azure Active Directory user accounts.
*	Follow the steps in the [Getting started](first-run-experience.md) article to set up your organization, environment, and workspace.
*	Review the [Known issues](#known-issues) section.

### First run experience

* Follow the account creation process. Set up your organization and environment, create your workspace and add members.
* Instrument website with the SDK to see telemetry arriving into your workspace.
*	View the real-time report showing active users by device, page view trend, top pages, top referrers, and users’ geographic locations.

### Export data from Product Insights

  *	Custom website instrumentation: ensure to send an *authid* for each user signing in to your site.
  *	Create a derived signal for export activities data.
  *	Export the data into your ADLS Gen 2 storage.
  *	Optional: Ingest Product Insights data export as activities in Customer Insights and view it as part of a customer profile.

## Known issues

We'll add a list of known issues in the coming days.

<!-- As we continue to work on the product and refine the experience, we are aware of a few outstanding issues, so please bear these in mind as you experience the product. -->
