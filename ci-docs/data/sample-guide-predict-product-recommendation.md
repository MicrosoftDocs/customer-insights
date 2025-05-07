---
title: Product recommendation prediction sample guide
description: Use this sample guide to try out the out of box product recommendation prediction model.
ms.date: 09/11/2023
ms.reviewer: mhart
ms.topic: article
author: joytaylor
ms.author: joytaylor
ms.custom: bap-template
ms.collection: bap-ai-copilot 
---

# Product recommendation prediction (preview) sample guide

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

This guide walks you through an end-to-end example of product recommendation prediction using sample data. We recommend that you try this prediction [in a new environment](manage-environments.md).

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Scenario

Contoso is a company that produces high-quality coffee and coffee machines. They sell the products through their Contoso Coffee website. Their goal is to understand which products should they recommend to their recurring customers. Knowing what customers are more **likely to purchase** can help them save marketing efforts by focusing on specific items.

## Prerequisites

- At least [Contributor permissions](user-roles.md) in Dynamics 365 Customer Insights - Data.

## Task 1 - Ingest data

Review the articles [about data ingestion](data-sources.md) and [connecting to a Power Query data source](connect-power-query.md). The following information assumes you are familiar with ingesting data in general.

### Ingest customer data from eCommerce platform

1. Create a Power query data source named **eCommerce** and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts: https://aka.ms/ciadclasscontacts.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:
   - **DateOfBirth**: Date
   - **CreatedOn**: Date/Time/Zone

   :::image type="content" source="media/ecommerce-dob-date.PNG" alt-text="Transform date of birth to date.":::

1. In the **Name** field on the right-hand pane, rename your data source to **eCommerceContacts**.

1. **Save** the data source.

### Ingest online purchase data

1. Add another data set to the same **eCommerce** data source. Choose the **Text/CSV** connector again.

1. Enter the URL for online purchases data https://aka.ms/ciadclassonline.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:
   - **PurchasedOn**: Date/Time
   - **TotalPrice**: Currency

1. In the **Name** field on the side pane, rename your data source to **eCommercePurchases**.

1. **Save** the data source.

### Ingest customer data from loyalty schema

1. Create a data source named **LoyaltyScheme** and select the **Text/CSV** connector.

1. Enter the URL for loyal customers https://aka.ms/ciadclasscustomerloyalty.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:
   - **DateOfBirth**: Date
   - **RewardsPoints**: Whole Number
   - **CreatedOn**: Date/Time

1. In the **Name** field on the right-hand pane, rename your data source to **loyCustomers**.

1. **Save** the data source.

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

## Task 4 - Configure product recommendation prediction

With the unified customer profiles in place and activity created, run the product recommendation prediction.

1. Go to **Insights** > **Predictions**.

1. On the **Create** tab, select **Use model** on the **Product recommendations (preview)** tile.

1. Select **Get started**.

1. Name the model **OOB Product Recommendation Model Prediction** and the output table **OOBProductRecommendationModelPrediction**.

1. Select **Next**.

1. Define model preferences:
   - **Number of products**: **5** to define how many products you want to recommend to your customers.
   - **Repeat purchases expected**: **Yes** to include previously purchased products in the recommendation.
   - **Look back window:** **365 days** to define how far the model will look back before recommending a product again.

   :::image type="content" source="media/product-recommendation-model-preferences.png" alt-text="Model preferences for the product recommendation model.":::

1. Select **Next**.

1. In the **Add purchase history** step, select **Add data**.

1. Select **SalesOrderLine** and the eCommercePurchases table and select **Next**. The required data is automatically filled in from the activity. Select **Save** and then **Next**.

1. Skip the **Add product information** and **Product filters** steps because we don't have product information data.

1. In the **Data updates** step, select **Monthly** for the model schedule.

1. Select **Next**.

1. After reviewing all the details, select **Save and Run**.

## Task 5 - Review model results and explanations

Let the model complete the training and scoring of the data. Review the [product recommendation model explanations](predict-transactional-churn.md#view-prediction-results).

## Task 6 - Create a segment of high purchased products

Running the model creates a new table, which is listed on **Data** > **Tables**. You can create a new segment based on the table created by the model.

1. On the results page, select **Create segment**.

1. Create a rule using the **OOBProductRecommendationModelPrediction** table and define the segment:
   - **Field**: ProductID
   - **Value**: Select the top three product IDs

1. Select **Save** and **Run** the segment.

You now have a segment that is dynamically updated which identifies the customers who might be interested in purchasing the five most recommended products. For more information, see [Create and manage segments](segments.md).

> [!TIP]
> You can also create a segment for a prediction model from the **Insights** > **Segments** page by selecting **New** and choosing **Create from** > **Insights**. For more information, see [Create a new segment with quick segments](segment-quick.md).

## Next steps

- [Prediction product recommendations (preview)](predict-product-recommendation.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
