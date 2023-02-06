---
title: Subscription churn prediction sample guide
description: Use this sample guide to try out the out of box subscription churn prediction model.
ms.date: 09/19/2022
ms.reviewer: v-wendysmith

ms.topic: tutorial
author: m-hartmann
ms.author: wameng
searchScope: 
  - ci-create-prediction
  - customerInsights
---

# Subscription churn prediction sample guide

This guide will walk you through an end-to-end example of subscription churn prediction using sample data. We recommend that you try this prediction [in a new environment](manage-environments.md).

## Scenario

Contoso is a company that produces high-quality coffee and coffee machines. They sell the products through their Contoso Coffee website. They recently started a subscription business for their customers to get coffee on a regular basis. Their goal is to understand which subscribed customers might cancel their subscription in the next few months. Knowing which of their customers is **likely to churn** can help them save marketing efforts by focusing on keeping them.

## Prerequisites

- At least [Contributor permissions](permissions.md) in Customer Insights.

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

1. Save the data source.

### Ingest customer data from loyalty schema

1. Create a data source named **LoyaltyScheme** and select the **Text/CSV** connector.

1. Enter the URL for loyalty customers https://aka.ms/ciadclasscustomerloyalty.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:
   - **DateOfBirth**: Date
   - **RewardsPoints**: Whole Number
   - **CreatedOn**: Date/Time

1. In the **Name** field on the right-hand pane, rename your data source to **loyCustomers**.

1. Save the data source.

### Ingest subscription information

1. Create a data source named **SubscriptionHistory** and select the **Text/CSV** connector.

1. Enter the URL for subscriptions https://aka.ms/ciadchurnsubscriptionhistory.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:
   - **SubscriptioID**: Whole Number
   - **SubscriptionAmount**: Currency
   - **SubscriptionEndDate**: Date/Time
   - **SubscriptionStartDate**: Date/Time
   - **TransactionDate**: Date/Time
   - **IsRecurring**: True/False
   - **Is_auto_renew**: True/False
   - **RecurringFrequencyInMonths**: Whole Number

1. In the **Name** field on the right-hand pane, rename your data source to **SubscriptionHistory**.

1. Save the data source.

### Ingest customer data from website reviews

1. Create a data source named **Website** and select the **Text/CSV** connector.

1. Enter the URL for website reviews https://aka.ms/ciadclasswebsite.

1. While editing the data, select **Transform** and then **Use first row as headers**.

1. Update the datatype for the columns listed below:
   - **ReviewRating**: Whole Number
   - **ReviewDate**: Date

1. In the **Name** field on the right-hand pane, rename your data source to **webReviews**.

## Task 2 - Data unification

Review the article [about data unification](data-unification.md). The following information assumes you are familiar with data unification in general.

[!INCLUDE [sample-guide-unification](includes/sample-guide-unification.md)]

## Task 3 - Create transaction history activity

Review the article [about customer activities](activities.md). The following information assumes you are familiar with creating activities in general.

1. Create an activity called **SubscriptionHistory** with the  *Subscription* entity and its primary key, **CustomerId**.

1. Create a relationship between *SubscriptionHistory:Subscription* and *eCommerceContacts:eCommerce* with **CustomerID** as the foreign key to connect the two entities.

1. Select **SubscriptionType** for the **EventActivity** and **SubscriptionEndDate** for the **TimeStamp**.

1. Select **Subscription** for the **Activity Type** and semantically map the activity data.

1. Run the activity.

1. Add another activity and map its fields names to the corresponding fields:
   - Customer activity entity: Reviews:Website
   - Primary key: Website.Reviews.ReviewId
   - Timestamp: Website.Reviews.ReviewDate
   - Event (activity name): Website.Reviews.ActivityTypeDisplay
   - Details (amount or value): Website.Reviews.ReviewRating

1. Run the activity.

## Task 4 - Configure the subscription churn prediction

With the unified customer profiles in place and activity created, run the subscription churn prediction. For detailed steps, see  [Subscription churn prediction](predict-subscription-churn.md).

1. Go to **Intelligence** > **Predictions**.

1. On the **Create** tab, select **Use model** on the **Customer churn model** tile.

1. Select **Subscription** for the type of churn and then **Get started**.

1. Name the model **OOB Subscription Churn Prediction** and the output entity **OOBSubscriptionChurnPrediction**.

1. Define model preferences:
   - **Days since subscription ended**: **60** days to indicate that a customer is considered churned if they don't renew the subscription in this period after their subscription ended.
   - **Days to look into future to predict churn**: **93** days which is the duration the model predicts which customers might churn. The further in the future you look, the less precise the results.

   :::image type="content" source="media/model-subs-levers.PNG" alt-text="Select the model preferences and churn definition.":::

1. Select **Next**.

1. In the **Required Data** step, select **Add data** to provide subscription history.

1. Select **Subscription** and the SubscriptionHistory entity and select **Next**. The required data is automatically filled in from the activity. Select **Save**.

1. Under Customer Activities, select **Add data**.

1. For this example, add the web review activity.

1. Select **Next**.

1. In the **Data updates** step, select **Monthly** for the model schedule.

1. After reviewing all the details, select **Save and Run**.

## Task 5 - Review model results and explanations

Let the model complete the training and scoring of the data. Review the subscription churn model explanations. For more information, see [View prediction results](predict-subscription-churn.md#view-prediction-results).

## Task 6 - Create a segment of high churn-risk customers

Running the model creates a new entity, which is listed on **Data** > **Entities**. You can create a new segment based on the entity created by the model.

1. On the results page, select **Create segment**.

1. Create a rule using the **OOBSubscriptionChurnPrediction** entity and define the segment:
   - **Field**: ChurnScore
   - **Operator**: greater than
   - **Value**: 0.6

1. Select **Save** and **Run** the segment.

You now have a segment that is dynamically updated which identifies high churn-risk customers for this subscription business. For more information, see [Create and manage segments](segments.md).

> [!TIP]
> You can also create a segment for a prediction model from the **Segments** page by selecting **New** and choosing **Create from** > **Intelligence**. For more information, see [Create a new segment with quick segments](segment-quick.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
