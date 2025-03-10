---
title: "Predict subscription churn"
description: "Predict whether a customer is at risk for no longer using your company’s subscription products or services."
ms.date: 11/30/2023
ms.reviewer: mhart
ms.topic: how-to
author: joytaylor
ms.author: joytaylor
ms.custom: bap-template
ms.collection: bap-ai-copilot
---

# Predict subscription churn

Predict whether a customer is at risk for no longer using your company’s subscription products or periodic services. Subscription data includes active and inactive subscriptions for each customer so there can be multiple entries per customer ID. To find the churn risk for customers not making scheduled purchases, use the [Transaction churn model.](predict-transactional-churn.md)

You must have business knowledge to understand what churn means for your business. For instance, a business with annual events can define their churn measured in years, while a business that caters to weekly sales may measure churn in months. We support time-based churn definitions, meaning a customer is considered to have churned a period of time after their subscription has ended.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=e4c2c0ea-d39c-493e-aae9-56c096cccf19]

For example, Contoso offers a monthly coffee service. They want to know which customers might be questioning service renewal so they can offer a discount. Through the subscription churn model, Contoso can see which customers might not renew the service next year and how large that population might be.  

> [!TIP]
> Try the subscription churn prediction using sample data: [Subscription churn prediction sample guide](sample-guide-predict-subscription-churn.md).

## Prerequisites

- At least [Contributor permissions](user-roles.md).
- At least 1,000 customer profiles within the desired prediction window.
- Customer Identifier, a unique identifier to match subscriptions to your customers.
- Subscription data for at least double the selected time window. Preferably, two to three years of subscription data. Subscription history must include:
  - **Subscription ID:** Unique identifier of a subscription.
  - **Subscription End Date:** Date the subscription expires for the customer.
  - **Subscription Start Date:** Date the subscription starts for the customer.
  - **Transaction Date:** Date a subscription change happened. For example, a customer buying or canceling a subscription.
  - **Is it a recurring subscription:** Boolean true/false field that determines if the subscription will renew with the same subscription ID without customer intervention.
  - **Recurrence Frequency (in months):** For recurring subscriptions, the month the subscription will renew. For example, a yearly subscription that automatically renews for a customer every year for another year has the value 12.
  - **Subscription Amount**: Amount of currency a customer pays for the subscription renewal. It can help identify patterns for different levels of subscriptions.
- At least two activity records for 50% of the customers you want to calculate churn for. Customer activities must include:
  - **Primary key:** Unique identifier for an activity. For example, a website visit or a usage record showing the customer viewed a TV show episode.
  - **Timestamp:** Date and time of the event identified by the primary key.
  - **Event:** Name of the event you want to use. For example, a field called "UserAction" in a streaming video service could have the value of "Viewed".
  - **Details:** Detailed information about the event. For example, a field called "ShowTitle" in a streaming video service could have the value of a video a customer watched.
- Less than 20% missing values in the data field of the provided table.

## Create a subscription churn prediction

Select **Save draft** at any time to save the prediction as a draft. The draft prediction displays in the **My predictions** tab.

1. Go to **Insights** > **Predictions**.

1. On the **Create** tab, select **Use model** on the **Customer churn model** tile.

1. Select **Subscription** for the type of churn and then **Get started**.

1. **Name this model** and the **Output table name** to distinguish them from other models or tables.

1. Select **Next**.

### Define customer churn

1. Enter the number of **Days since subscription ended** that your business considers a customer to be in a churned state. This period is typically linked to business activities like offers or other marketing efforts trying to prevent losing the customer.

1. Enter the number of **Days to look into future to predict churn**. For example, predict the risk of churn for your customers over the next 90 days to align to your marketing retention efforts. Predicting churn risk for longer or shorter periods of time can make it more difficult to address the factors in your churn risk profile, depending on your specific business requirements.

1. Select **Next**.

### Add required data

1. Select **Add data** for **Subscription history**.

1. Select the semantic activity type **Subscription** that contains the required subscription history information. If the activity hasn't been set up, select **here** and create it.

1. Under **Activities**, if the activity attributes were semantically mapped when the activity was created, choose the specific attributes or table you'd like the calculation to focus on. If semantic mapping didn't occur, select **Edit** and map your data.
  
   :::image type="content" source="media/subscription-churn-required.png" alt-text="Add required data for Subscription churn model":::

1. Select **Next** and review the attributes required for this model.

1. Select **Save**.

1. Select **Add data** for **Customer activities**.

1. Select the semantic activity type that provides the customer activity information. If the activity hasn't been set up, select **here** and create it.

1. Under **Activities**, if the activity attributes were semantically mapped when the activity was created, choose the specific attributes or table you'd like the calculation to focus on. If semantic mapping didn't occur, select **Edit** and map your data.

1. Select **Next** and review the attributes required for this model.

1. Select **Save**.

1. Add more activities or select **Next**.

### Set update schedule

1. Choose the frequency to retrain your model. This setting is important to update the accuracy of predictions as new data is ingested. Most businesses can retrain once per month and get a good accuracy for their prediction.

1. Select **Next**.

### Review and run the model configuration

The **Review and run** step shows a summary of the configuration and provides a chance to make changes before you create the prediction.

1. Select **Edit** on any of the steps to review and make any changes.

1. If you're satisfied with your selections, select **Save and run** to start running the model. Select **Done**. The **My predictions** tab displays while the prediction is being created. The process may take several hours to complete depending on the amount of data used in the prediction.

[!INCLUDE [progress-details](includes/progress-details-pane.md)]

## View prediction results

1. Go to **Insights** > **Predictions**.

1. In the **My predictions** tab, select the prediction you want to view.

There are three primary sections of data within the results page:

- **Training model performance**: Grades A, B, or C indicate the performance of the prediction and can help you make the decision to use the results stored in the output table.
  
  :::image type="content" source="media/subscription-churn-modelperformance.PNG" alt-text="Image of the model score information box with the grade A.":::

  Grades are determined based on the following rules:
  - **A** when the model accurately predicted at least 50% of the total predictions, and when the percentage of accurate predictions for customers who churned is greater than the historical average churn rate by at least 10%.
  - **B** when the model accurately predicted at least 50% of the total predictions, and when the percentage of accurate predictions for customers who churned is up to 10% greater than the historical average churn rate.
  - **C** when the model accurately predicted less than 50% of the total predictions, or when the percentage of accurate predictions for customers who churned is less than the historical average churn rate.
  
- **Likelihood to churn (number of customers)**: Groups of customers based on their predicted risk of churn. Optionally, [create segments of customers](prediction-based-segment.md) with high churn risk. Such segments help to understand where your cutoff should be for segment membership.  

  :::image type="content" source="media/subscription-churn-resultdistribution.PNG" alt-text="Graph showing distribution of churn results, broken into ranges from 0-100%":::

- **Most influential factors:** There are many factors that are taken into account when creating your prediction. Each of the factors has its importance calculated for the aggregated predictions a model creates. Use these factors to help validate your prediction results. Or use this information later to [create segments](.//prediction-based-segment.md) that could help influence churn risk for customers.

  :::image type="content" source="media/subscription-churn-influentialfactors.PNG" alt-text="List showing influential factors and their importance in predicting the churn result.":::

> [!NOTE]
> In the output table for this model, *ChurnScore* is the predicted probability of churn and *IsChurn* is a binary label based on *ChurnScore* with 0.5 threshold. If this default threshold doesn't work for your scenario, [create a new segment](segments.md) with your preferred threshold. To view the churn score, go to **Data** > **Tables** and view the data tab for the output table you defined for this model.

[!INCLUDE [footer-include](includes/footer-banner.md)]
