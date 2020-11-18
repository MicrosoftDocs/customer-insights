---
title: Subscription churn prediction sample guide
description: Use this sample guide to try out the out of box subscription churn prediction model.
ms.date: 11/11/2020
ms.reviewer: digranad
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Subscription churn prediction (preview) sample guide

This guide will walk you through an end to end example of subscription churn prediction in Customer Insights using the sample data provided below. All data used in this guide is not real customer data and is part of the Contoso dataset found in the *Demo* environment within your Customer Insights subscription.

## Scenario

Contoso is a company that produces high-quality coffee and coffee machines, which they sell through their Contoso Coffee website. They recently started a subscription business for their customers to get coffee on a regular basis. Their goal is to understan which subscribed customers will stop being an active customer and cancel their subscription in the next few months. Knowing which of their customers is **likely to churn**, can help them save a marketin efforts by focusing on retaining them.

## Prerequisites

- At least [Contributor permissions](permissions.md) in Customer Insights.
- We recommend that you implement the following steps [in a new environment](manage-environments.md).

## Task 1 - Ingest Data

Review the articles [about data ingestion](data-sources.md) and [importing data sources using Power Query connectors](connect-power-query.md) specifically. The following information assumes you familiarized with ingesting data in general. 

### Ingest customer data from eCommerce platform

1. Create a data source named **eCommerce**, choose the import option and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts https://aka.ms/ciadclasscontacts.

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:

   - **DateOfBirth**: Date
   - **CreatedOn**: Date/Time/Zone

   [!div class="mx-imgBorder"]
   ![Transform DoB to Date](media/ecommerce-dob-date.PNG "transform date of birth to date")

1. In the 'Name' field on the right-hand pane, rename your data source from **Query** to **eCommerceContacts**

1. Save the data source.

### Ingest customer data from loyalty scheme

1. Create a data source named **LoyaltyScheme**, choose the import option and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts https://aka.ms/ciadclasscustomerloyalty.

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:

   - **DateOfBirth**: Date
   - **RewardsPoints**: Whole Number
   - **CreatedOn**: Date/Time

1. In the 'Name' field on the right-hand pane, rename your data source from **Query** to **loyCustomers**.

1. Save the data source.

### Ingest Csubscription information

1. Create a data source named **SubscriptionHistory**, choose the import option and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts https://aka.ms/ciadchurnsubscriptionhistory.

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:

   - **SubscriptioID**: Whole Number
   - **SubscriptionAmount**: Currency
   - **SubscriptionEndDate**: Date/Time
   - **SubscriptionStartDate**: Date/Time
   - **TransactionDate**: Date/Time
   - **IsRecurring**: True/False
   - **Is_auto_renew**: True/False
   - **RecurringFrequencyInMonths**: Whole Number

1. In the 'Name' field on the right-hand pane, rename your data source from **Query** to **SubscriptionHistory**.

1. Save the data source.

### Ingest customer data from website reviews

1. Create a data source named **Website**, choose the import option and select the **Text/CSV** connector.

1. Enter the URL for eCommerce contacts https://aka.ms/ciadchurnsubscriptionhistory.

1. While editing the data, select **Transform** and then **Use First Row as Headers**.

1. Update the datatype for the columns listed below:

   - **ReviewRating**: Whole Number
   - **ReviewDate**: Date

1. In the 'Name' field on the right-hand pane, rename your data source from **Query** to **webReviews**.

## Task 2 - Data unification

Having ingested the raw data from your data sources into ‘entities’ you will now begin the **Map, Match, Merge** process to create a unified customer profile by merging data from each customer profile source. For more information, see [Data unification](data-unification.md).

### Map

1. After ingesting the data, map contacts from eCommerce and Loyalty data to common data types. Go to **Data** > **Unify** > **Map**.

1. Select the entities that represent the customer profile – **eCommerceContacts** and **loyCustomers**. 

   [!div class="mx-imgBorder"]
   ![Unify eCommerce and Loyalty](media/unify-ecommerce-loyalty.PNG "unify ecommerce and loyalty datasources")

1. Select **ContactId** as the primary key for **eCommerceContacts** and **LoyaltyID** as the primary key for **loyCustomers**.

   [!div class="mx-imgBorder"]
   ![Unify LoyaltyId as primary key](media/unify-loyaltyid.PNG "unify loyaltyid primary key for loycustomers")

### Match

1. Go to the **Match** tab and select **Set Order**.

1. In the **Primary** drop-down list, choose **eCommerceContacts : eCommerce** as the primary source and include all records.

1. In the **Entity 2** drop-down list, choose **loyCustomers : LoyaltyScheme** and include all records.

   [!div class="mx-imgBorder"]
   ![Unify match eCommerce and Loyalty](media/unify-match-order.PNG "unify ecommerce and loyalty")

1. Select **Create a new rule**

1. Add your first condition using FullName.

   * For eCommerceContacts select **FullName** in the drop-down.
   * For loyCustomers select **FullName** in the drop-down.
   * Select the **Normalize** drop down and choose **Type (Phone, Name, Address, ...)**.
   * Set **Precision Level**: **Basic** and **Value**: **High**.

1. Enter the name **FullName, Email** for the new rule.

   * Add a second condition for email address by selecting **Add Condition**
   * For entity eCommerceContacts, choose **EMail** in drop-down.
   * For entity loyCustomers, choose **EMail** in Field drop-down - Leave Normalize blank 
   * Set **Precision Level**: **Basic** and **Value**: **High**.

   [!div class="mx-imgBorder"]
   ![Unify match rule for name and email](media/unify-match-rule.PNG "unify match rule with name and email")

7. Select **Save** and **Run**.

### Merge

1. Go to the **Merge** tab.

1. On the **ContactId** for **loyCustomers** entity, change the display name to **ContactIdLOYALTY** to differentiate it from the other IDs ingested.

   [!div class="mx-imgBorder"]
   ![Rename contactid ](media/unify-merge-contactid.PNG "rename contactid from loyaltyid")

1. Select **Save** and **Run** to start the Merge Process.


## Task 3 - Configuring the Out of Box Subscription Churn prediction

With the unified customer profiles in plance, we can now run the subscription churn prediction. For detailed steps, see the [Subscription churn prediction (preview)](predict-subscription-churn.md) article. 

1. Go to **Intelligence** > **Discover** and select to use the **Customer churn model**.

1.. Select the **Subscription** option and select **Get started**.

   [!div class="mx-imgBorder"]
   ![Setup Subscription Churn Model](media/select-subscription-churn.PNG "select subscription churn model")

4. Name the model **OOB Subscription Churn Prediction** and the output entity **OOBSubscriptionChurnPrediction**.

   [!div class="mx-imgBorder"]
   ![Name the model](media/model-subs-name.PNG "add name to the model")

5. Define two conditions for the churn model:

   * **Days since subscription ended**: **at least 60** days. If a customer has not renewed their subscription for this long after their subscription ended, then they are considered churned. 

   * **Churn definition**: **at least 93** days. The model will try to predict this far into the future which customers may or may not churn. The further in the future you look, the less accurate the results.

     [!div class="mx-imgBorder"]
     ![Select the model levers Prediction Window and Churn Definition](media/model-subs-levers.PNG "select model prediction window and churn definition")

6. Select **Add required data** and select **Add data** for subscription history.

7. Add the **Subscription : SubscriptionHistory** entity and map the fields from eCommerce to the corresponding fields required by the model.

8. Join the **Subscription : SubscriptionHistory** entity with **eCommerceContacts : eCommerce**, name the relationship **eCommerceSubscription**.

   [!div class="mx-imgBorder"]
   ![Join eCommerce entities](media/model-subscription-join.PNG "join ecommerce entities")

9. Under Customer Activities, add the **webReviews : Website** entity and map the fields from webReviews to the corresponding fields required by the model. 

   [!div class="mx-imgBorder"]
   ![Map the Website Review entity](media/model-map-website-entity.PNG "map website review entity to model input")

11. Configure an activity for website reviews. Select the activity **Review** and join the **webReviews : Website** entity with **eCommerceContacts : eCommerce**.

    [!div class="mx-imgBorder"]
    ![Join eCommerce and webReviews entities](media/model-review-activity.PNG "join ecommerce entities")

12. Select **Next** to set the model schedule.

    The model needs to train with certain frequency so that it learns new patterns when there is new data ingested. For this example, select **Monthly**.

13. After reviewing all the details, select **Save and Run**.

## Task 4 - View model results and explanations

After the model has successfully completed the training and scoring of the data, you can view the subscription churn model explanations. For more information, see [Review a prediction status and results](predict-subscription-churn.md#review-a-prediction-status-and-results).

## Task 5 - Create a segment of high churn-risk customers

Running the production model creates a new entity that you can see in **Data** > **Entities**.   

You can create a new segment based on the entity created by the model.

1.  go to **Segments**. Select **New** and choose **Create from** > **Intelligence**. 

   [!div class="mx-imgBorder"]
   ![Creating a segment with the model output](media/segment-intelligence.PNG "Creating a segment with the model output")


1. Select the **OOBSubscriptionChurnPrediction** endpoint and define the segment you like to create.

You now have a segment that is dynamically updated which identifies high churn-risk customers for this subscription business.

For more information, see [Create and manage segments](segments.md).
