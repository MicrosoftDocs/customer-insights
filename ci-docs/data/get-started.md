---
title: Get started with Dynamics 365 Customer Insights - Data
description: An overview of help resources to get started quickly. 
ms.reviewer: mhart
ms.author: nikeller
author: Nils-2m
ms.date: 06/24/2024
ms.topic: how-to
ms.custom: bap-template
---

# Get started with Dynamics 365 Customer Insights - Data

Customer Insights - Data can help you build a deeper understanding of your customers. Connect data from various transactional, behavioral, and observational sources to create a 360-degree customer view. Use these insights to drive customer-centric experiences and processes. Unify and understand customer data and harness it for intelligent insights and actions.

## Step 1: Create an environment

1. If you want to install Customer Insights - Data on an existing Dynamics 365 environment, visit [this page](..\journeys\setup.md) for instructions. If you don't have a paid license, you can sign up for a [free trial](trial-signup.md) or [purchase a license](paid-license.md).

1. In most cases with global tenant admin permissions, to install Customer Insights - Data, you should create an environment in the Power Platform Admin Center and [follow these steps](..\journeys\setup.md). If you want to create an environment from the Customer Insights - Data application, you must be a global tenant admin and you can follow the steps in [Create an environment](create-environment.md). After the environment is created, the **Home** page displays.

   :::image type="content" source="media/home-page.svg" alt-text="Screenshot of the Home screen.":::

## Step 2: Import data

1. Select **Add data sources** on the **Home** page.

1. Import your data. Choose between:

   - [Delta tables in Azure Data Lake](connect-delta-lake.md)
   - [Azure Data Lake Storage, including Common Data Model](connect-common-data-model.md)
   - [Microsoft Dataverse](connect-dataverse.md)
   - [Azure Synapse Analytics (Preview)](connect-synapse.md)
   - [Power Query connectors](connect-power-query.md).

   For more information on these options, see [Data sources overview](data-sources.md)

## Step 3: Unify the data and set up relationships

To combine unified profiles, run the data unification process. Unified profiles are the foundation to get insights and take action on the data. Specify relationships between the ingested tables and use enrichment features to add information to the profiles.

1. Run the [data unification process](data-unification.md) by identifying the [source fields](data-unification-map-tables.md), removing [duplicates](data-unification-duplicates.md), [matching conditions](data-unification-match-tables.md), and [unifying fields](data-unification-merge-tables.md).

1. Get familiar with the [tables the system creates](tables.md) and create [relationships between the ingested tables](relationships.md).

## Step 4: Enhance unified profiles with predictions, activities, and measures

With unified profiles set up, enhance your data and further increase the information they provide.

1. Choose from an expanding library of enrichment providers to [enrich your customer data](enrichment-manage.md).

1. Use [out-of-box models](predictions.md) to predict churn likelihood or expected revenues.

1. [Configure activities](activities.md) based on ingested data and visualize interactions with your customers in a chronological timeline.

1. [Build measures](measures.md) to gauge your business goals and KPIs.

## Step 5: Create segments and activate data through various export options

Now that your data is complete and contains a wide range of information about your customers, look for ways to take action on that data.

1. [Create segments](segments.md), subsets of your customer base, to ensure your actions are relevant for the targeted customers.

1. Browse the expanding catalog of [export options](export-destinations.md) where you can use customer data. For example, you can use data to manage promotions and reach out with digital marketing.

1. Review integration options, for example to other Dynamics 365 apps with the [Customer Card add-in](customer-card-add-in.md).  

[!INCLUDE [footer-include](includes/footer-banner.md)]
