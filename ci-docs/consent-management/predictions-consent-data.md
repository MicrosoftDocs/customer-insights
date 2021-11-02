---
title: "Consent data in out-of-box predictions"
description: "Learn how to create prediction models that use consent data."
ms.date: 10/30/2021
ms.service: customer-insights
ms.topic: how-to
author: smithy7
ms.author: dimutako
ms.reviewer: mhart
manager: shellyha
---

# Use consent data in prediction models

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Build out-of-box prediction models in audience insights to predict customer churn or customer lifetime value. Use consent data from the consent management capability to increase the accuracy of the predictions. Understand the influence of customer consent on customer churn and the customer lifetime value. 

This article outlines how to use consent data in out-of-box models. The steps below focus on the transaction churn model. However, you can apply the same steps to the subscription churn and customer lifetime value models. 

## Required entities and fields

The following list includes the entities that are required and the fields these entities must contain. For more information, see [Prerequisites for a transaction model](../audience-insights/predict-transactional-churn.md).

1. *Subscription consent* entity
    - Primary key or ID: A primary key for each unique consent value. It needs unique values in each row. For example: email or customer ID. 
    - Customer ID: A customer identifier that links the consent entity to the customer entity and their transaction data. This identifier should be the same across all required entities. 
    - Consent start date: The date that consent was updated. This field can also include time.
    - Consent status: A consent value that indicates which customers consented.
    
2.	*Customer transaction* entity
    - Transaction ID: A primary key for each transaction.
    - Customer ID: A customer identifier that links the consent entity to the customer entity and their transaction data. This identifier should be the same across all required entities. 
    - Transaction date: Date of each transaction.
    - Value of transaction: Transaction amount of each transaction.
    - Label assigned to returns (optional): Boolean value that indicates if the transaction is a return.
    - Unique product ID (optional): ID that represents the product or service of the transaction. 

3.	*Customer* entity with a primary key representing each unique customer. This identifier should be the same across all required entities. 

## Set up instructions

This section outlines how to use consent data as activity data input to the transaction churn model. It involves setting up an activity based on consent data. Next, you set up the model as usual and add the consent activity as a customer activity in the model configuration.

### Step 1: Create a consent activity

[Create an activity](../audience-insights/activities.md) based on your consent entity. 

1. Start the guided experience to create an activity.
1. In the **Relationships** step, select the *Customer ID* of the *Consent* entity as the foreign key.
1. Choose the *Customer* entity to map to.
1. Select the *Customer ID* in the *Customer* entity as the primary key.
1. In the **Activity unification** step, select the **Consent status** from the *Consent* entity under the **Event activity** field. 
1. Select field that describes when consent was provided in the **Timestamp** field.

   :::image type="content" source="media/consent-activity-unification.png" alt-text="Step to create unified activity in activity set up process.":::

1. In the **Activity type** step, select **Create new** in the dropdown for **Activity Type**.
1. Enter a name for your consent activity.

   :::image type="content" source="media/new-consent-activity-type.png" alt-text="Create a new activity type for consent data.":::

1. Review and run the consent activity. Continue to the next step after a successful run. For more information about activities, see [Customer activities](../audience-insights/activities.md).

### Step 2: Configure and run the model 

Follow the instructions to [create a transaction model](../audience-insights/predict-transactional-churn.md) until you configure the additional data.

1. In the **Additional data (optional)** step of the model creation, select **Add data**. 

   :::image type="content" source="media/additional-data-choose-activity.png" alt-text="Choose consent activity in add data step.":::

1. Choose the consent activity created before and choose the corresponding *Consent* entity.
1. Select **ActualActivityId** as the primary key.
1. Select **ActivityTime** as the timestamp.
1. Select **ActivityName** as the activity event.

   :::image type="content" source="media/additional-data-map-attributes.png" alt-text="Map attributes when adding the consent activity.":::

1. Select **Save** and then **Next**. 
1. Choose how frequently the data will be updated and the model will be run. Then, select **Next**.
1. Review and confirm your settings and select **Run**.  

## View and interpret model results

View the model results to find insights.

- Training model performance: Indicates the performance of the prediction based on how many customers it predicted accurately. Adding consent data and other optional data helps increase the likelihood of precise predictions. 
- Likelihood to churn (number of customers): Groups of customers based on their predicted risk of churn. 
- Most influential factors: Lists the factors that affect the model results. Find out which influence the consent data had by looking at the **Activity** factors. Another way to gauge the influence of consent data is to set up a model without consent data and compare the results to this model.

:::image type="content" source="media/influential-factors-activity.png" alt-text="Influential factors in the model output.":::

For more information on model results, see [Transaction churn prediction](../audience-insights/predict-transactional-churn.md).

 

