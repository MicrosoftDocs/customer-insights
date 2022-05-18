---
title: Product recommendation prediction sample guide
description: Use this sample guide to try out the out of box product recommendation prediction model.
ms.date: 05/16/2022
ms.reviewer: mhart
ms.subservice: audience-insights
ms.topic: tutorial
author: m-hartmann
ms.author: wameng
manager: shellyha
searchScope: 
  - ci-predictions
  - ci-create-prediction
  - customerInsights
---

# Product recommendation prediction sample guide

We'll walk you through an end to end example of product recommendation prediction using the sample data provided below.

## Scenario

Contoso is a company that produces high-quality coffee and coffee machines, which they sell through their Contoso Coffee website. Their goal is to understand which products should they recommend to their recurring customers. Knowing what customers are more **likely to purchase**, can help them save marketing efforts by focusing on specific items.

## Prerequisites

- At least [Contributor permissions](permissions.md) in Customer Insights.
- We recommend that you implement the following steps [in a new environment](manage-environments.md).

## Task 1 - Ingest data

Review the articles [about data ingestion](data-sources.md) and [importing data sources using Power Query connectors](connect-power-query.md) specifically. The following information assumes you familiarized with ingesting data in general.

### Ingest customer data from eCommerce platform

1. Create a data source named **eCommerce**, choose the import option, and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts: [https://aka.ms/ciadclasscontacts](https://aka.ms/ciadclasscontacts).

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:
   - **DateOfBirth**: Date
   - **CreatedOn**: Date/Time/Zone

   :::image type="content" source="media/ecommerce-dob-date.PNG" alt-text="Transform date of birth to date.":::

1. In the 'Name' field on the right-hand pane, rename your data source from **Query** to **eCommerceContacts**

1. **Save** the data source.

### Ingest online purchase data

1. Add another data set to the same **eCommerce** data source. Choose the **Text/CSV** connector again.

1. Enter the URL for **Online Purchases** data [https://aka.ms/ciadclassonline](https://aka.ms/ciadclassonline).

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:
   - **PurchasedOn**: Date/Time
   - **TotalPrice**: Currency

1. In the **Name** field on the side pane, rename your data source from **Query** to **eCommercePurchases**.

1. **Save** the data source.

### Ingest customer data from loyalty schema

1. Create a data source named **LoyaltyScheme**, choose the import option, and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts [https://aka.ms/ciadclasscustomerloyalty](https://aka.ms/ciadclasscustomerloyalty).

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:
   - **DateOfBirth**: Date
   - **RewardsPoints**: Whole Number
   - **CreatedOn**: Date/Time

1. In the **Name** field on the right-hand pane, rename your data source from **Query** to **loyCustomers**.

1. **Save** the data source.

## Task 2 - Data unification

[!INCLUDE [sample-guide-unification](includes/sample-guide-unification.md)]

## Task 3 - Configure product recommendation prediction

With the unified customer profiles in place, we can now run the product recommendation prediction.

1. Go to **Intelligence** > **Prediction** choose **Product recommendation**.

1. Select **Get started**.

1. Name the model **OOB Product Recommendation Model Prediction** and the output entity **OOBProductRecommendationModelPrediction**.

1. Define three conditions for the model:

   - **Number of products**: Set this value to **5**. This setting defines how many products you want to recommend to your customers.

   - **Repeat purchases expected**: Select **Yes** to indicate that you want to include products in the recommendation that your customers have purchased before.

   - **Look back window:** Select at least **365 days**. This setting defines how far the model will look back at the customer's activity to use it as input to their recommendations.

   :::image type="content" source="media/product-recommendation-model-preferences.png" alt-text="Model preferences for the product recommendation model.":::

1. In the **Add required data** step, select **Add data**.

1. In the **Add data** pane, choose the **SalesOrderLine** as the purchase history entity. At this point, it's likely not yet configured. Open link in the pane to create the activity with the following steps:
   1. Enter an **Activity name** and choose *eCommercePurchases:eCommerce* as **Activity entity**. The **Primary key** is *PurchaseId*.
   1. Define and name the relationship to the *eCommerceContacts:eCommerce entity* and choose **ContactId** as the foreign key.
   1. For Activity unification, set **Event activity** as *TotalPrice* and Timestamp to *PurchasedOn*. You can specify more fields as outlined in [Customer activities](activities.md).
   1. For **Activity type**, choose *SalesOrderLine*. Map the following activity fields:
      - Order line ID: PurchaseId
      - Order ID: PurchaseId
      - Order data: PurchasedOn
      - Product ID: ProductId
      - Amount: TotalPrice
   1. Review and finish the activity before going back to the model configuration.

1. Back in the **Select activities** step, choose the newly created activity in the **Activities** section. Select **Next** and the attribute mapping is already filled out. Select **Save**.

1. In this sample guide, we skip the **Add product information** and **Product filters** set because we don't have product information data.

1. In the **Data updates** step, set the model schedule.

   The model needs to train regularly to learn new patterns when there is new data ingested. For this example, select **Monthly**.

1. After reviewing all the details, select **Save and Run**. It will take a few minutes to run the model the first time.

## Task 4 - Review model results and explanations

Let the model complete the training and scoring of the data. You can now review the product recommendation model explanations. For more information, see [Review a prediction status and results](predict-transactional-churn.md#review-a-prediction-status-and-results).

## Task 5 - Create a segment of high purchased products

Running the production model creates a new entity that you can see in **Data** > **Entities**.

You can create a new segment based on the entity created by the model.

1. Go to **Segments**. Select **New** and choose **Create from Intelligence**.

   ![Creating a segment with the model output.](media/segment-intelligence.png)

1. Select the **OOBProductRecommendationModelPrediction** endpoint and define the segment:

   - Field: ProductID
   - Value: Select the top three product IDs

   :::image type="content" source="media/product-recommendation-quick-segment.png" alt-text="Create a segment from the model results.":::

You now have a segment that is dynamically updated which identifies the customers who might be interested to purchase the three most recommended products.

For more information, see [Create and manage segments](segments.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
