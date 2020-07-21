---
uid: topics/onboarding-guidance
title: Onboarding to the Private Preview
author: ruthaisabokhae
description: Framework for onboarding
ms.author: ruthai
ms.date: 07/13/2020
ms.service: product-insights
ms.topic: conceptual
---

# Onboarding to the Private Preview

The goal of this onboarding document is to give Private Preview customers visibility to our product features, documentation, scenarios to validate, known issues and how to engage with Microsoft throughout the Private Preview.

## Onboarding Guidance 
*	Review NDA/ Partner Agreement with Microsoft.  
*	Review capabilities outlined in this document for Private Preview.  
*	Review and understand the limitations/known issues of our Private Preview.  
*	Validate the core scenarios and provide feedback to Microsoft.

## Private Preview Expectations 
*	Private Preview exists for testing purposes only. Environments may be torn down at the end of the testing period to make way for a Public Preview release.  
*	Private Preview is not for production use, and strictly for prototyping and providing feedback. We are likely to delete data and rebuild environments at any point during the Private Preview but will ensure communication of any changes to avoid disruption in testing.  
*	We will work closely with you to seek feedback, incorporate product changes. We expect to establish a cadence for this interaction during the period of Private Preview and will communicate that subsequently.  
*	Private Preview is expected to run approximately for two months (August and September 2020) during which time we appreciate your active participation. We plan to take all relevant feedback into our future releases.  
*	Please reach out to your assigned PM first or use the alias pirequest@microsoft.com to provide feedback and report issues. We will triage reported issues, prioritize, and track them, and share status with you regularly.  


## Prerequisites
*	Access to a production website with authentication for your customers to instrument the Product Insights SDK.
*	Access to a Test environment for Customer Insights to be able to test the full customer 360 integration of data.
*	Access to (or ability to create) an ADLS storage account (for export).

## User consent for your site
*	Please refer to the **Manage cookies and user consent** section.
*	The **Getting started** section highlights that the code auto collects view and actions.
*	After reviewing these documents, you must evaluate if there is need for an update to your user consent notification. If you previously had no "non-essential" cookies, then this will likely require an update to your site policy, etc.

## Public Preview Features

### First run experience
* The starting point for any user logging into Product Insights in which the Organization is generated and your own environment and workspace are created. This is where you will be able to start sending you web analytics data into.

### Web SDK
* The JavaScript library to be instrumented on your website to measure user interaction also provides sample code.

### Web analytics and reports
* The Out-of-the-Box reports showing the events coming through from the Web SDK is pre-defined visualizations and dashboards.

### Derived signals
* The ability to create a derived signal from the web analytics data, filter it and export it to ADLS. That then allows for importing the data into [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-us/ai/customer-insights/).

## Product use cases for customers to test
### First run experience
  * Follow the account creation process - set up your organization and environment, creat your workspace and add members.
  * Instrument website with the SDK to see telemetry arriving into your workspace.
  *	View web real time report showing active users by device, page view trend, top pages, top referrers, and users’ geographic locations.

### Exporting from Product Insights
  *	Custom website instrumentation – ensure to send an authid for your customers logging into your site.
  *	Create a derived signal for export activities data.
  *	Export the data into your ADLS gen 2 storage.
  *	Optional: Consume Product Insights data export as activities in Customer Insights and view it as part of a customer profile.

## Setup/ Provisionings Steps
*	Before you start, please ensure you have read and agree to the **Preview Terms of Service** provided.
*	Login to the Dynamics 365 Product Insights portal using your Microsoft AAD user accounts.
*	Follow the process defined in the **Getting Started** section of the document to setup your organization environment, and workspace.
*	Please refer to the **Known Issues** section.

## Known issues
As we continue to work on the product and refine the experience, we are aware of a few outstanding issues, so please bear these in mind as you experience the product.

**Note: A list of the known bugs and workaround will be made available before this documentation is provided to the customer.**


