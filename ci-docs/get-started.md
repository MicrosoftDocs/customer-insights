---
title: Get started with Dynamics 365 Customer Insights
description: An overview of Customer Insights help resources to get started quickly. 
ms.reviewer: mhart
ms.author: mhart
author: m-hartmann
ms.date: 08/31/2021
ms.subservice: audience-insights 
ms.topic: conceptual
ms.manager: shellyha
ms.custom: intro-internal
searchScope: 
  - ci-home
  - customerInsights
---

# Get started with Dynamics 365 Customer Insights

Customer Insights can help you build a deeper understanding of your customers. Connect data from various transactional, behavioral, and observational sources to create a 360-degree customer view. Use these insights to drive customer-centric experiences and processes. Unify and understand customer data and harness it for intelligent insights and actions.

## Step 1: Create an environment

To start, you first have to create an environment to work in. If your organization already purchased a license, see [Create an environment](create-environment.md). To start a trial for Customer Insights, see [Set up a trial environment](trial-signup.md). 

## Step 2: Explore Customer Insights

The first time you sign in to Customer Insights, you can configure settings and explore the product.

1. [Sign in to Customer Insights](https://home.ci.ai.dynamics.com) using your Microsoft Azure Active Directory (AAD) user account.

1. [Change the environment](manage-environments.md#switch-environments) to see demo data and [explore Customer Insights](home.md).

##  Step 3: Ingest, unify, and set up relationships for your data

Unified profiles are the foundation to get insights and take action on the data. Bring in data from various sources and run the data unification process to combine unified profiles. Specify relationships between the ingested entities use enrichment features to add information to the profiles. 

1. Ingest data by creating data sources from multiple options. Choose between [Power Query connectors](connect-power-query.md), a [Common Data Model folder](connect-common-data-model.md), or [Microsoft Dataverse](/dynamics365/customer-insights/audience-insights/connect-dataverse-managed-lake). 

1. Run the [data unification process](data-unification.md) by going through the [map](map-entities.md), [match](match-entities.md), and [merge](merge-entities.md) phases.

1. Get familiar with the [entities the system creates](entities.md) and create [relationships between the ingested entities](relationships.md).
	
## Step 4: Enhance unified profiles with predictions, activities, and measures

With unified profiles set up, you can enhance your data and further increase the information they provide.

1. Choose from an expanding library of enrichment providers to [enrich your customer data](enrichment-hub.md).

1. Use [out-of-box models](predictions-overview.md) to predict churn likelihood or expected revenues.

1. [Configure activities](activities.md) based on ingested data and visualize interactions with your customers in a chronological timeline. 

1. [Build measures](measures.md) to gauge your business goals and KPIs.
 
## Step 5: Create segments and activate data through various export options

Now that your data is complete and contains a wide range of information about your customers, it's time to look for ways to take action on that data. 

1. [Create segments](segments.md), subsets of your customer base, to ensure your actions are relevant for the targeted customers.

1. Browse the expanding catalog of [export options](export-destinations.md) where you can use customer data. For example, you can use data to manage promotions and reach out with digital marketing.

1. Review integration options, for example to other Dynamics 365 apps with the [Customer Card add-in](customer-card-add-in.md).  


[!INCLUDE [footer-include](includes/footer-banner.md)]