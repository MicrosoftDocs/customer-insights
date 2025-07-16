---
title: Customer lifetime value (CLV) prediction sample guide
description: Use this sample guide to try out the customer lifetime value prediction model.
ms.date: 09/11/2023
ms.update-cycle: 180-days
ms.reviewer: v-wendysmith
ms.topic: article
author: joytaylor
ms.author: joytaylor
ms.custom: bap-template
ms.collection: bap-ai-copilot 
---

# Customer lifetime value (CLV) prediction sample guide

This guide walks you through an end-to-end example of Customer lifetime value (CLV) prediction in Dynamics 365 Customer Insights - Data using sample data. We recommend that you try this prediction [in a new environment](manage-environments.md).

## Scenario

Contoso is a company that produces high-quality coffee and coffee machines. They sell the products through their Contoso Coffee website. The company wants to understand the value (revenue) that their customers can generate in the next 12 months. Knowing the expected value of their customers in the next 12 months will help them steer their marketing efforts on high value customers.

## Prerequisites

- At least [Contributor permissions](user-roles.md).

## Task 1 - Ingest data

Review the articles [about data ingestion](data-sources.md) and [connecting to a Power Query data source](connect-power-query.md). The following information assumes you are familiar with ingesting data in general.

### Ingest customer data from eCommerce platform

1. Create a Power query data source named **eCommerce** and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts https://aka.ms/ciadclasscontacts.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:
   - **DateOfBirth**: Date
   - **CreatedOn**: Date/Time/Zone

   :::image type="content" source="media/ecommerce-dob-date.PNG" alt-text="Transform date of birth to date.":::

1. In the **Name** field on the right-hand pane, rename your data source to **eCommerceContacts**

1. **Save** the data source.

### Ingest online purchase data

1. Add another data set to the same **eCommerce** data source. Choose the **Text/CSV** connector again.

1. Enter the URL for **Online Purchases** data https://aka.ms/ciadclassonline.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:
   - **PurchasedOn**: Date/Time
   - **TotalPrice**: Currency

1. In the **Name** field on the side pane, rename your data source to **eCommercePurchases**.

1. **Save** the data source.

### Ingest customer data from loyalty schema

1. Create a data source named **LoyaltyScheme** and select the **Text/CSV** connector.

1. Enter the URL for loyalty customers https://aka.ms/ciadclasscustomerloyalty.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:
   - **DateOfBirth**: Date
   - **RewardsPoints**: Whole Number
   - **CreatedOn**: Date/Time

1. In the **Name** field on the right-hand pane, rename your data source to **loyCustomers**.

1. **Save** the data source.

### Ingest customer data from website reviews

1. Create a data source named **Website** and select the **Text/CSV** connector.

1. Enter the URL for website reviews https://aka.ms/CI-ILT/WebReviews.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:
   - **ReviewRating**: Decimal number
   - **ReviewDate**: Date

1. In the **Name** field on the right-hand pane, rename your data source to **Reviews**.

1. **Save** the data source.

## Task 2 - Data unification

Review the article [about data unification](data-unification.md). The following information assumes you are familiar with data unification in general.

[!INCLUDE [sample-guide-unification](includes/sample-guide-unification.md)]

## Task 3 - Create transaction history activity

Review the article [about customer activities](activities.md). The following information assumes you are familiar with creating activities in general.

1. Create activities with the *eCommercePurchases:eCommerce* table and the *Reviews:Website* table.

1. For *eCommercePurchases:eCommerce*, select **SalesOrderLine** for the **Activity Type** and **PurchaseId** for the **Primary key**.

1. For *Reviews:Website*, select **Review** for the **Activity Type** and **ReviewID** for the **Primary key**.

1. Enter the following information for the purchase activity:

   - **Activity name**: eCommercePurchases
   - **TimeStamp**: PurchasedOn
   - **EventActivity**: TotalPrice
   - **Order line ID**: PurchaseId
   - **Order date**: PurchasedOn
   - **Amount**: TotalPrice

1. Enter the following information for the web review activity:
   - **Activity name**: WebReviews
   - **Timestamp**: ReviewDate
   - **Event activity**: ActivityTypeDisplay
   - **Additional detail**: ReviewRating

1. Add a relationship between *eCommercePurchases:eCommerce* and *eCommerceContacts:eCommerce* with **ContactID** as the foreign key to connect the two tables.

1. Add a relationship between *Website* and *eCommerceContacts* with **UserId** as the foreign key.

1. Review your changes and then select **Create activities**.

## Task 4 - Configure customer lifetime value prediction

With the unified customer profiles in place and activity created, run the customer lifetime value (CLV) prediction. For detailed steps, see [Customer Lifetime Value prediction](predict-customer-lifetime-value.md).

1. Go to **Insights** > **Predictions**.

1. On the **Create** tab, select **Use model** on the **Customer lifetime value** tile.

1. Select **Get started**.

1. Name the model **OOB eCommerce CLV Prediction** and the output table  **OOBeCommerceCLVPrediction**.

1. Define model preferences:
   - **Prediction time period**: **12 months or 1 year** to define how far into the future to predict CLV.
   - **Active customers**: **Let model calculate purchase interval** which is the time frame in which a customer must have had at least one transaction to be considered active.
   - **High value customer**: manually define high value customers as **top 30% of active customers**.

    :::image type="content" source="media/clv-model-preferences.png" alt-text="Preferences step in the guided experience for the CLV model.":::

1. Select **Next**.

1. In the **Required Data** step, select **Add data** to provide the transaction history data.

    :::image type="content" source="media/clv-model-required.png" alt-text="Add required data step in the guided experience for the CLV model.":::

1. Select **SalesOrderLine** and the eCommercePurchases table and select **Next**. The required data is automatically filled in from the activity. Select **Save** and then **Next**.

1. The **Additional data (optional)** step allows you to add more customer activity data to get more insights for customer interactions. For this example, select **Add data** and add the web review activity.

1. Select **Next**.

1. In the **Data updates** step, select **Monthly** for the model schedule.

1. Select **Next**.

1. After reviewing all the details, select **Save and Run**.

## Task 5 - Review model results and explanations

Let the model complete the training and scoring of the data. Review the [CLV model results and explanations](predict-customer-lifetime-value.md#view-prediction-results).

## Task 6 - Create a segment of high value customers

Running the model creates a new table, which is listed on **Data** > **Tables** > **Output**. You can create a new customer segment based on the table created by the model.

1. On the results page, select **Create segment**.

1. Create a rule using the **OOBeCommerceCLVPrediction** table and define the segment:
   - **Field**: CLVScore
   - **Operator**: greater than
   - **Value**: 1500

1. Select **Save** and **Run** the segment.

You now have a segment that identifies customers who are predicted to generate more than $1500 of revenue in the next 12 months. This segment gets updated dynamically if more data is ingested. For more information, see [Create and manage segments](segments.md).

> [!TIP]
> You can also create a segment for a prediction model from the **Insights** > **Segments** page by selecting **New** and choosing **Create from** > **Insights**. For more information, see [Create a new segment with quick segments](segment-quick.md).

## Next steps

- [Predict customer lifetime value (CLV)](predict-customer-lifetime-value.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
