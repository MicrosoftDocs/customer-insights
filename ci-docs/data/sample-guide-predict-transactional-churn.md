---
title: Transactional churn prediction sample guide
description: This sample guide demonstrates transactional churn prediction end to end, covering data ingestion, unification, model setup, and segment creation.
ms.date: 07/10/2026
ms.update-cycle: 180-days
ms.reviewer: alfergus
ms.topic: article
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
ms.collection: bap-ai-copilot
---

# Transactional churn prediction sample guide

Transactional churn prediction identifies customers who are likely to stop purchasing based on their transaction history. This guide walks you through an end-to-end example of transactional churn prediction using sample data. We recommend that you try this prediction [in a new environment](manage-environments.md).

## Scenario

Contoso is a company that produces high-quality coffee and coffee machines. They sell the products through their Contoso Coffee website. Their goal is to know which customers who typically purchase their products on a regular basis, will stop being active customers in the next 60 days. Knowing which of their customers is **likely to churn**, can help them save marketing efforts by focusing on keeping them.

## Prerequisites

- At least [Contributor permissions](user-roles.md).

## Task 1 - Ingest data

Review the articles [about data ingestion](data-sources.md) and [connecting to a Power Query data source](connect-power-query.md). The following information assumes you are familiar with ingesting data in general.

### Ingest customer data from eCommerce platform

1. Create a data source named **eCommerce** and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts: `https://aka.ms/ciadclasscontacts`.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:

   - **DateOfBirth**: Date
   - **CreatedOn**: Date/Time/Zone

   :::image type="content" source="media/ecommerce-dob-date.PNG" alt-text="Screenshot of transforming the DateOfBirth column data type to Date.":::

1. In the **Name** field on the right-hand pane, rename your data source to **eCommerceContacts**

1. Save the data source.

### Ingest online purchase data

1. Add another data set to the same **eCommerce** data source. Choose the **Text/CSV** connector again.

1. Enter the URL for online purchases data: `https://aka.ms/ciadclassonline`.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:

   - **PurchasedOn**: Date/Time
   - **TotalPrice**: Currency

1. In the **Name** field on the right-hand pane, rename your data source to **eCommercePurchases**.

1. Save the data source.

### Ingest customer data from loyalty schema

1. Create a data source named **LoyaltyScheme** and select the **Text/CSV** connector.

1. Enter the URL for loyalty scheme contacts: `https://aka.ms/ciadclasscustomerloyalty`.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:

   - **DateOfBirth**: Date
   - **RewardsPoints**: Whole Number
   - **CreatedOn**: Date/Time

1. In the **Name** field on the right-hand pane, rename your data source to **loyCustomers**.

1. Save the data source.

## Task 2 - Data unification

Review the article [about data unification](data-unification.md). The following information assumes you are familiar with data unification in general.

[!INCLUDE [sample-guide-unification](includes/sample-guide-unification.md)]

## Task 3 - Create transaction history activity

Review the article [about customer activities](activities.md). The following information assumes you are familiar with creating activities in general.

1. Create an activity with the *eCommercePurchases:eCommerce* table.

1. Select **SalesOrderLine** for the **Activity Type** and **PurchaseId** for the **Primary key**.

1. Enter the following information for the activity:

   - **Activity name**: eCommercePurchases
   - **TimeStamp**: PurchasedOn
   - **EventActivity**: TotalPrice
   - **Order line ID**: PurchaseId
   - **Order date**: PurchasedOn
   - **Amount**: TotalPrice

1. Create a relationship between *eCommercePurchases:eCommerce* and *eCommerceContacts:eCommerce* with **ContactID** as the foreign key to connect the two tables.

1. Review your changes and then select **Create activities**.

## Task 4 - Configure transactional churn prediction

With the unified customer profiles and activity in place, run the transactional churn prediction.

1. Go to **Insights** > **Predictions**.

1. On the **Create** tab, select **Use model** on the **Customer churn model**.

1. Select **Transactional** for the type of churn and then **Get started**.

1. Name the model **OOB eCommerce Transaction Churn Prediction** and the output table **OOBeCommerceChurnPrediction**.

1. Select **Next**.

1. Define model preferences:

   - **Prediction window**: **60** days to define how far into the future we want to predict customer churn.

   - **Churn definition**: **60** days to indicate the duration without purchase after which a customer is considered churned.

     :::image type="content" source="media/model-levers.PNG" alt-text="Screenshot of the model preferences for Prediction window and Churn definition.":::

1. Select **Next**.

1. Select **Purchase History (required)** and select **Add data** for purchase history.

1. Select **SalesOrderLine** and the eCommercePurchases table and select **Next**. The required data is automatically filled in from the activity. Select **Save** and then **Next**.

   :::image type="content" source="media/model-purchase-join.PNG" alt-text="Screenshot of joining the eCommerce purchase and contact tables for the churn model.":::

1. Skip the **Additional data (optional)** step.

1. In the **Data updates** step, select **Monthly** for the model schedule.

1. After reviewing all the details, select **Save and Run**.

## Task 5 - Review model results and explanations

Let the model complete the training and scoring of the data. Review the churn model explanations. For more information, see [View prediction results](predict-transactional-churn.md#view-prediction-results).

## Task 6 - Create a segment of high churn-risk customers

Running the production model creates a new table, which is listed on **Data** > **Tables** > **Output**. You can create a new segment based on the table created by the model.

1. On the results page, select **Create segment**.

1. Create a rule using the **OOBeCommerceChurnPrediction** table and define the segment:
   - **Field**: ChurnScore
   - **Operator**: greater than
   - **Value**: 0.6

1. Select **Save** and **Run** the segment.

You now have a segment that is dynamically updated which identifies high churn-risk customers. For more information, see [Create and manage segments](segments.md).

> [!TIP]
> You can also create a segment for a prediction model from the **Insights** > **Segments** page by selecting **New** and choosing **Create from** > **Insights**. For more information, see [Create a new segment with quick segments](segment-quick.md).

## Next steps

- [Predict transactional churn](predict-transactional-churn.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
