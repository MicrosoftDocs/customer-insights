---
title: Transactional churn prediction
description: "Predict whether a customer is at risk for no longer purchasing your products or services."
ms.date: 11/12/2020
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: zacookmsft
ms.author: zacook
manager: shellyha
---

# Transactional churn prediction (preview)

Transactional churn prediction helps predict if a customer will no longer purchase your products or services in a given time window. You can create new churn predictions on **Intelligence** > **Predictions**. Select **My predictions** to see other predictions that you've created.

> [!TIP]
> Try the tutorial for a translactional churn prediction using sample data: [Transactional churn prediction (preview) sample guide](sample-guide-predict-transactional-churn.md).

## Prerequisites

- At least [Contributor permissions](permissions.md) in Customer Insights.
- Business knowledge to understand what churn means for your business. We support time-based churn definitions, meaning a customer is considered to have churned after a period of no purchases.
- Data about your transactions/purchases and their history:
    - Transaction identifiers to distinguish purchases/transactions.
    - Customer identifiers to match transactions to your customers.
    - Transaction event dates, which define the dates the transaction occurred on.
    - The semantic data schema for purchases/transactions requires the following information:
        - **Transaction ID:** A unique identifier of a purchase or transaction.
        - **Transaction Date:** The date of the purchase or transaction.
        - **Value of the transaction:** The currency/numerical value amount of the transaction/item.
        - (Optional) **Unique product ID:** The ID of the product or service purchased if your data is at a line item level.
        - (Optional) **Whether this transaction was a return:** A true/false field that identifies if the transaction was a return or not. If the **Value of the transaction** is negative, we will also use this information to infer a return.
- (Optional) Data about customer activities:
    - Activity identifiers to distinguish activities of the same type.
    - Customer identifiers to map activities to your customers.
    - Activity information containing the name and date of the activity.
    - The semantic data schema for customer activities includes:
        - **Primary key:** A unique identifier for an activity. For example, a website visit or a usage record showing the customer tried a sample of your product.
        - **Timestamp:** The date and time of the event identified by the primary key.
        - **Event:** The name of the event you want to use. For example, a field called "UserAction" in a grocery store might be a coupon use by the customer.
        - **Details:** Detailed information about the event. For example, a field called "CouponValue" in a grocery store might be the currency value of the coupon.

## Create a transactional churn prediction

1. In Customer Insights, go to **Intelligence** > **Predictions**.

1. Select the **Customer churn model (preview)** tile and select **Use this model**.
   
1. In the **Customer churn model** pane, choose **Transactional** and select **Get started**.

:::image type="content" source="media/select-transaction-churn.PNG" alt-text="Screenshot with selected transactional option in Customer churn model pane.":::

### Name model

1. Provide a name for the model to distinguish it from other models.

1. Provide a name for the output entity using letters and numbers only, without any spaces. That's the name that the model entity will use. 

1. Select **Next**.

### Define customer churn

1. Set a window of days to predict churn for in the **Identify customers who may churn in the next** field. For example, predict the risk of churn for your customers over the next 90 days to align to your marketing retention efforts. Predicting churn risk for a longer or shorter period of time can make it more difficult to address the factors in your churn risk profile, but it depends on your specific business requirements. 
   >[!TIP]
   > You can select **Save and close** at any time to save the prediction as a draft. You'll find the draft prediction in the **My predictions** tab to continue.

1. Enter the number of days to define churn in the **A customer has churned if they've made no purchases in:** field. For example, if a customer has made no purchases in the last 30 days, they might be considered as churned for your business. 

1. Select **Next** to continue

### Add required data

1. Select **Add data** for **Purchase history** and choose the entity that provides the transaction/purchase history information as described in the [prerequisites](#prerequisites).

1. Map the semantic fields to attributes within your purchase history entity and select **Next**. For descriptions of the fields, have a look at the [prerequisites](#prerequisites).

   :::image type="content" source="media/model-map-purchase-entity.PNG" alt-text="Map semantic fields of the purchase entity.":::

1. If the fields below aren't populated, configure the relationship from your purchase history entity to the Customer entity.
    1. Select the **Purchase history entity**.
    1. Select the **Field** that identifies the customer in the purchase history entity. It needs to relate to the primary customer ID of your Customer entity.
    1. Select the **Customer entity** that matches your primary customer entity.
    1. Enter a name that describes the relationship.

    :::image type="content" source="media/model-purchase-join.PNG" alt-text="Purchase history page showing the creation of a relationship to customer.":::
   
1. Select **Next**.

1. Optionally, select **Add data** for **Customer activities**. Choose the entity that provides the customer activity information as described in the prerequisites.

1. Map the semantic fields to attributes within your customer activity entity and select **Next**. For descriptions of the fields, have a look at the [prerequisites](#prerequisites).

   :::image type="content" source="media/map-transaction-data-fields.png" alt-text="Map customer fields for transactional data.":::

1. Select an activity type that matches to the type of customer activity you're configuring. Select **Create new** and choose an available activity type or create a new type.

1. You'll need to configure the relationship from your customer activity entity to the Customer entity.
    1. Select the field that identifies the customer in the customer activity table. It can be directly related to the primary customer ID of your Customer entity.
    1. Select the Customer entity that matches your primary Customer entity
    1. Enter a name that describes the relationship.

1. Select **Save**.

1. If you have any other customer activities you would like to include, repeat the steps above.

1. Select **Next**.

### Set schedule and review configuration

1. Set a frequency to retrain your model. This setting is important to update the accuracy of predictions as new data is ingested. Most businesses can retrain once per month and get a good accuracy for their prediction.

1. Select **Next**.

1. Review the configuration of the prediction. You can go back to prior steps by selecting **Edit** under the shown value. Or you can select a configuration step from the progress indicator.

1. If all values are configured correctly, select **Save and run** to begin the prediction process. On the **My predictions** tab, you can see the status of your predictions. The process may take several hours to complete depending on the amount of data used in the prediction.

## Review a prediction status and results

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.

1. Select the prediction you want to review.
   - **Prediction name:** Name of the prediction provided when creating it.
   - **Prediction type:** Type of model used for the prediction
   - **Output entity:** Name of the entity to store the output of the prediction. You can find an entity with this name on **Data** > **Entities**.
   - **Predicted field:** This field is populated only for some types of predictions, and isn't used in churn prediction.
   - **Status:** Status of the prediction run.
        - **Queued:** Prediction is waiting for other processes to run.
        - **Refreshing:** Prediction is currently running to produce results that will flow into the output entity.
        - **Failed:** Prediction run has failed. [Review the logs](#troubleshoot-a-failed-prediction) for more details.
        - **Succeeded:** Prediction has succeeded. Select **View** under the vertical ellipses to review the prediction
   - **Edited:** The date the configuration for the prediction was changed.
   - **Last refreshed:** The date the prediction refreshed results in the output entity.

1. Select the vertical ellipses next to the prediction you want to review results for and select **View**.

   :::image type="content" source="media/model-subs-view.PNG" alt-text="View control to see results of a prediction.":::   

1. There are three primary sections of data within the results page:
    1. **Training model performance:** A, B, or C are possible scores. This score indicates the performance of the prediction, and can help you make the decision to use the results stored in the output entity. Scores are determined based on the following rules:
         
         - **A** when the model accurately predicted at least 50% of the total predictions, and when the percentage of accurate predictions for customers who churned is greater than the baseline rate by at least 10%.
            
         - **B** when the model accurately predicted at least 50% of the total predictions, and when the percentage of accurate predictions for customers who churned is up to 10% greater than the baseline.
            
         - **C** when the model accurately predicted less 50% of the total predictions, or when the percentage of accurate predictions for customers who churned is less than the baseline.
               
         - **Baseline** takes the prediction time window input for the model (for example, one year) and the model creates different fractions of time by dividing it by 2 until it reaches one month or less. It uses these fractions to create a business rule for customers who have not purchased in this time frame. These customers are considered as churned. The time-based business rule with the highest ability to predict who is likely to churn is chosen as baseline model.
            
    1. **Likelihood to churn (number of customers):** Groups of customers based on their predicted risk of churn. This data can help you later if you want to create a segment of customers with high churn risk. Such segments help to understand where your cutoff should be for segment membership.
       
    1. **Most influential factors:** There are many factors that are taken into account when creating your prediction. Each of the factors has its importance calculated for the aggregated predictions a model creates. You can use these factors to help validate your prediction results. Or you can use this information later to [create segments](segments.md) that could help influence churn risk for customers.

## Troubleshoot a failed prediction

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.

1. Select the vertical ellipses next to the prediction you want to view error logs for.

1. Select **Logs**.

1. Review all the errors. There are several types of errors that can occur, and they describe what condition caused the error. For example, an error that there's not enough data to accurately predict is typically resolved by loading additional data into Customer Insights.

## Refresh a prediction

Predictions will automatically refresh on the same [schedule your data refreshes](system.md#schedule-tab) as configured in settings. You can refresh them manually too.

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.

1. Select the vertical ellipses next to the prediction you want to refresh.

1. Select **Refresh**.

## Delete a prediction

Deleting a prediction also removes its output entity.

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.

1. Select the vertical ellipses next to the prediction you want to delete.

1. Select **Delete**.


[!INCLUDE[footer-include](../includes/footer-banner.md)]