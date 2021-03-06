---
title: Transactional churn prediction sample guide
description: Use this sample guide to try out the out of box transactional churn prediction model.
ms.date: 05/11/2022
ms.reviewer: mhart


ms.subservice: audience-insights
ms.topic: tutorial
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Transactional churn prediction sample guide

This guide will walk you through an end to end example of Transactional Churn prediction in Customer Insights using the data provided below. All data used in this guide is not real customer data and is part of the Contoso dataset found in the *Demo* environment within your Customer Insights Subscription.

## Scenario

Contoso is a company that produces high-quality coffee and coffee machines, which they sell through their Contoso Coffee website. Their goal is to know which customers who typically purchase their products on a regular basis, will stop being active customers in the next 60 days. Knowing which of their customers is **likely to churn**, can help them save marketing efforts by focusing on keeping them.

## Prerequisites

- At least [Contributor permissions](permissions.md) in Customer Insights.
- We recommend that you implement the following steps [in a new environment](manage-environments.md).

## Task 1 - Ingest data

Review the articles [about data ingestion](data-sources.md) and [importing data sources using Power Query connectors](connect-power-query.md) specifically. The following information assumes you familiarized with ingesting data in general. 

### Ingest customer data from eCommerce platform

1. Create a data source named **eCommerce**, choose the import option, and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts https://aka.ms/ciadclasscontacts.

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:

   - **DateOfBirth**: Date
   - **CreatedOn**: Date/Time/Zone

   :::image type="content" source="media/ecommerce-dob-date.PNG" alt-text="Transform DoB to Date.":::

1. In the **Name** field on the right-hand pane, rename your data source from **Query** to **eCommerceContacts**

1. Save the data source.

### Ingest online purchase data

1. Add another data set to the same **eCommerce** data source. Choose the **Text/CSV** connector again.

1. Enter the URL for **Online Purchases** data https://aka.ms/ciadclassonline.

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:

   - **PurchasedOn**: Date/Time
   - **TotalPrice**: Currency
   
1. In the **Name** field on the right-hand pane, rename your data source from **Query** to **eCommercePurchases**.

1. Save the data source.

### Ingest customer data from loyalty schema

1. Create a data source named **LoyaltyScheme**, choose the import option, and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts https://aka.ms/ciadclasscustomerloyalty.

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:

   - **DateOfBirth**: Date
   - **RewardsPoints**: Whole Number
   - **CreatedOn**: Date/Time

1. In the **Name** field on the right-hand pane, rename your data source from **Query** to **loyCustomers**.

1. Save the data source.

## Task 2 - Data unification

[!INCLUDE [sample-guide-unification](includes/sample-guide-unification.md)]

## Task 3 - Configure transaction churn prediction

With the unified customer profiles in place, we can now run the transaction churn prediction. For detailed steps, see the [Transaction churn prediction](predict-transactional-churn.md) article. 

1. Go to **Intelligence** > **Discover** and select to use the **Customer churn model**.

1. Select the **Transactional** option and select **Get started**.

1. Name the model **OOB eCommerce Transaction Churn Prediction** and the output entity **OOBeCommerceChurnPrediction**.

1. Define two conditions for the churn model:

   * **Prediction window**: **at least 60** days. This setting defines how far into the future do we want to predict customer churn.

   * **Churn definition**: **at least 60** days. The duration without purchase after which a customer is considered churned.

     :::image type="content" source="media/model-levers.PNG" alt-text="Select the model levers Prediction Window and Churn Definition.":::

1. Select **Purchase History (required)** and select **Add data** for purchase history.

1. Add the **eCommercePurchases : eCommerce** entity and map the fields from eCommerce to the corresponding fields required by the model.

1. Join the **eCommercePurchases : eCommerce** entity with **eCommerceContacts : eCommerce**.

   :::image type="content" source="media/model-purchase-join.PNG" alt-text="Join eCommerce entities.":::

1. Select **Next** to set the model schedule.

   The model needs to train regularly to learn new patterns when there is new data ingested. For this example, select **Monthly**.

1. After reviewing all the details, select **Save and Run**.

## Task 4 - Review model results and explanations

Let the model complete the training and scoring of the data. You can now review the churn model explanations. For more information, see [Review a prediction status and results](predict-transactional-churn.md#review-a-prediction-status-and-results).

## Task 5 - Create a segment of high churn-risk customers

Running the production model creates a new entity that you can see in **Data** > **Entities**.   

You can create a new segment based on the entity created by the model.

1.  Go to **Segments**. Select **New** and choose **Create from** > **Intelligence**. 

   :::image type="content" source="media/segment-intelligence.PNG" alt-text="Creating a segment with the model output.":::

1. Select the **OOBeCommerceChurnPrediction** endpoint and define the segment: 
   - Field: ChurnScore
   - Operator: greater than
   - Value: 0.6

You now have a segment that is dynamically updated which identifies high churn-risk customers.

For more information, see [Create and manage segments](segments.md).


[!INCLUDE [footer-include](includes/footer-banner.md)]
