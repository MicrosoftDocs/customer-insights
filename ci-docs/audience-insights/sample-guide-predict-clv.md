---
title: Customer lifetime value prediction sample guide
description: Use this sample guide to try out the customer lifetime value prediction model.
ms.date: 05/25/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: tutorial
author: yashlundia
ms.author: yalundia        
manager: shellyha
---

# Customer lifetime value (CLV) prediction sample guide

This guide will walk you through an end to end example of Customer lifetime value (CLV) prediction in Customer Insights using sample data.

## Scenario

Contoso is a company that produces high-quality coffee and coffee machines. They sell the products through their Contoso Coffee website. The company wants to understand the value (revenue) that their customers can generate in the next 12 months. Knowing the expected value of their customers in the next 12 months will help them steer their marketing efforts on high value customers.

## Prerequisites

- At least [Contributor permissions](permissions.md) in audience insights.
- We recommend that you implement the following steps [in a new environment](manage-environments.md).

## Task 1 - Ingest data

Review the articles [about data ingestion](data-sources.md) and [importing data sources using Power Query connectors](connect-power-query.md). The following information assumes you familiarized with ingesting data in general.

### Ingest customer data from eCommerce platform

1. Create a data source named  **eCommerce** , choose the import option, and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts [https://aka.ms/ciadclasscontacts](https://aka.ms/ciadclasscontacts).

1. While editing the data, select  **Transform**  and then  **Use First Row as Headers**.

1. Update the datatype for the columns listed below:
   - **DateOfBirth** : Date
   - **CreatedOn** : Date/Time/Zone

   :::image type="content" source="media/ecommerce-dob-date.PNG" alt-text="Transform date of birth to date.":::

1. In the 'Name' field on the right-hand pane, rename your data source from **Query** to **eCommerceContacts**

1. **Save** the data source.

### Ingest online purchase data

1. Add another data set to the same **eCommerce** data source. Choose the **Text/CSV** connector again.

1. Enter the URL for **Online Purchases** data https://aka.ms/ciadclassonline.

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:
   - **PurchasedOn**: Date/Time
   - **TotalPrice**: Currency

1. In the **Name** field on the side pane, rename your data source from **Query** to **eCommercePurchases**.

1. **Save** the data source.

### Ingest customer data from loyalty schema

1. Create a data source named **LoyaltyScheme**, choose the import option, and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts https://aka.ms/ciadclasscustomerloyalty.

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:
   - **DateOfBirth**: Date
   - **RewardsPoints**: Whole Number
   - **CreatedOn**: Date/Time

1. In the **Name** field on the right-hand pane, rename your data source from **Query** to **loyCustomers**.

1. **Save** the data source.

### Ingest customer data from website reviews

1. Create a data source named **Website**, choose the import option, and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts https://aka.ms/CI-ILT/WebReviews.

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:

   - **ReviewRating**: Decimal number
   - **ReviewDate**: Date

1. In the 'Name' field on the right-hand pane, rename your data source from **Query** to **Reviews**.

1. **Save** the data source.

## Task 2 - Data unification

After ingesting the data, we now begin the data unification process to create a unified customer profile. For more information, see [Data unification](data-unification.md).

### Map

1. After ingesting the data, map contacts from eCommerce and Loyalty data to common data types. Go to **Data** > **Unify** > **Map**.

1. Select the entities that represent the customer profile – **eCommerceContacts** and **loyCustomers**. Then, select **Apply**.

   ![unify ecommerce and loyalty datasources.](media/unify-ecommerce-loyalty.png)

1. Select **ContactId** as the primary key for **eCommerceContacts** and **LoyaltyID** as the primary key for **loyCustomers**.

   ![Unify LoyaltyId as primary key.](media/unify-loyaltyid.png)

1. Select **Save**.

### Match

1. Go to the **Match** tab and select **Set Order**.

1. In the **Primary** drop-down list, choose **eCommerceContacts : eCommerce** as the primary source and include all records.

1. In the **Entity 2** drop-down list, choose **loyCustomers : LoyaltyScheme** and include all records.

   ![Unify match eCommerce and Loyalty.](media/unify-match-order.png)

1. Select **Add rule**

1. Add your first condition using FullName.

   - For eCommerceContacts select **FullName** in the drop-down.
   - For loyCustomers select **FullName** in the drop-down.
   - Select the **Normalize** drop-down and choose **Type (Phone, Name, Address, ...)**.
   - Set **Precision Level**: **Basic** and **Value**: **High**.

1. Enter the name **FullName, Email** for the new rule.

   - Add a second condition for email address by selecting **Add Condition**
   - For entity eCommerceContacts, choose **EMail** in drop-down.
   - For entity loyCustomers, choose **EMail** in the drop-down.
   - Leave Normalize blank.
   - Set **Precision Level**: **Basic** and **Value**: **High**.

   ![Unify match rule for name and email.](media/unify-match-rule.png)

1. Select **Done**.

1. Select **Save** and **Run**.

### Merge

1. Go to the **Merge** tab.

1. On the **ContactId** for **loyCustomers** entity, change the display name to **ContactIdLOYALTY** to differentiate it from the other IDs ingested.

   ![rename contactid from loyalty id.](media/unify-merge-contactid.png)

1. Select **Save** and **Run merge and downstream processes**.

## Task 3 - Configure customer lifetime value prediction

With the unified customer profiles in place, we can now run the customer lifetime value prediction. For detailed steps, see [Customer Lifetime Value prediction (preview)](predict-customer-lifetime-value.md).

1. Go to  **Intelligence**  > **Predictions**  and select the **Customer lifetime value model**.

1. Go through the information in the side pane and select **Get started**.

1. Name the model **OOB eCommerce CLV Prediction** and the output entity  **OOBeCommerceCLVPrediction**.

1. Define model preferences for the CLV model:
   - **Prediction time period**: **12 months or 1 year**. This setting defines how far into the future to predict customer lifetime value.
   - **Active customers**: Specify what active customers mean for your business. Set the historical time frame in which a customer must have had at least one transaction to be considered active. The model will only predict CLV for active customers. Choose between letting the model calculate the time period based on historical transaction data or provide a specific time frame. In this sample guide, we **let the model calculate purchase interval**, which is the default option.
   - **High value customers**: Define high value customers as a percentile of top-paying customers. The model uses this input to provide results that fit your business definition of high value customers. You can choose to let the model define high value customers. It uses a heuristic rule that derives the percentile. You can also define high value customers as a percentile of top future paying customers. In this sample guide, we manually define high value customers as **top 30% of active paying customers** and select **Next**.

    :::image type="content" source="media/clv-model-preferences.png" alt-text="Preferences step in the guided experience for the CLV model.":::

1. In the **Required Data** step, select **Add data** to provide the transaction history data.

1. Add the **eCommercePurchases : eCommerce** entity and map the attributes that are required by the model:
   - Transaction ID: eCommerce.eCommercePurchases.PurchaseId
   - Transaction date: eCommerce.eCommercePurchases.PurchasedOn
   - Transaction amount: eCommerce.eCommercePurchases.TotalPrice
   - Product ID: eCommerce.eCommercePurchases.ProductId

1. Select **Next**.

1. Set up the relationship between the **eCommercePurchases : eCommerce** entity and  **eCommerceContacts : eCommerce**.

1. The **Additional data (optional)** step allows you to add more customer activity data. This data can help to get more insights for customer interactions with your business, which can contribute to CLV. Adding key customer interactions like web logs, customer service logs, or rewards program history can improve the accuracy of predictions. Select **Add data** to include more customer activity data.

1. Add the customer activity entity and map its fields names to the corresponding fields required by the model:
   - Customer activity entity: Reviews:Website
   - Primary key: Website.Reviews.ReviewId
   - Timestamp: Website.Reviews.ReviewDate
   - Event (activity name): Website.Reviews.ActivityTypeDisplay
   - Details (amount or value): Website.Reviews.ReviewRating

1. Select **Next** and configure the activity and the relationship between the transaction data and the customer data:  
   - Activity type: Choose existing
   - Activity label: Review
   - Corresponding label: Website.Reviews.UserId
   - Customer entity: eCommerceContacts:eCommerce
   - Relationship: WebsiteReviews

1. Select **Next** to set the model schedule.

   The model needs to train regularly to learn new patterns when there's new data ingested. For this example, choose **Monthly**.

1. After reviewing all the details, select  **Save and Run**.

## Task 4 - Review model results and explanations

Let the model complete the training and scoring of the data. Next, you can review the CLV model results and explanations. For more information, see [Review a prediction status and results](predict-customer-lifetime-value.md#review-prediction-status-and-results).

## Task 5 - Create a segment of high value customers

Running the model creates a new entity, which is listed on **Data** > **Entities**. You can create a new customer segment based on the entity created by the model.

1. Go to **Segments**. 

1. Select  **New** and choose **Create from** > **Intelligence**.

   ![Creating a segment with the model output.](media/segment-intelligence.png)

1. Select the  **OOBeCommerceCLVPrediction** entity and define the segment:
  - Field: CLVScore
  - Operator: greater than
  - Value: 1500

1. Select **Review** and **Save** the segment.

You now have a segment that identifies customers who are predicted to generate more than $1500 of revenue in the next 12 months. This segment gets updated dynamically if more data is ingested.

For more information, see [Create and manage segments](segments.md).
