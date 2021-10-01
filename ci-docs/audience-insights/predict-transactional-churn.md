---
title: Transactional churn prediction
description: "Predict whether a customer is at risk for no longer purchasing your products or services."
ms.date: 09/29/2021
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

For environments based on business accounts, we can predict transactional churn for an account and also a combination of account and another level of information like product category. Adding a dimension can help find out how likely it is that the account 'Contoso' will stop buying the product category 'office stationary'. In addition, for business accounts, we can also use AI to generate a list of potential reasons why an account is likely to churn for a category of secondary level information.

> [!TIP]
> Try the tutorial for a transactional churn prediction using sample data: [Transactional churn prediction (preview) sample guide](sample-guide-predict-transactional-churn.md).

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
- Suggested data characteristics:
    - Sufficient historical data: Transaction data for at least double the selected time window. Preferably, two to three years of transaction history. 
    - Multiple purchases per customer: Ideally at least two transactions per customer.
    - Number of customers: At least 10 customer profiles, preferably more than 1,000 unique customers. The model will fail with fewer than 10 customers and insufficient historical data.
    - Data completeness: Less than 20% of missing values in the data field of the entity provided.

> [!NOTE]
> For a business with high customer purchase frequency (every few weeks) it's recommended to select a shorter prediction window and churn definition. For low purchase frequency (every few months or once a year), choose a longer prediction window and churn definition.

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

### Provide an optional list of benchmark accounts (business accounts only)

Add a list of your business customers and accounts that you want to use as benchmarks. You will be able to see additional details for these benchmark accounts (in the model results screen) including their churn score and most influential features that impacted their churn prediction.

1. Select **+ Add customers**.

1. Choose the customers that act as a benchmark.

1. Select **Next** to continue.

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
     In the output entity, *ChurnScore* is the predicted probability of churn and *IsChurn* is a binary label based on *ChurnScore* with 0.5 threshold. The default threshold might not work for your scenario. [Create a new segment](segments.md#create-a-new-segment) with your preferred threshold.
     Not all customers are necessarily active customers. Some of them may not have had any activity for a long time and are considered as churned already, based on you churn definition. Predicting the churn risk for customers who already churned isn't useful because the are not the audience of interest.
   - **Predicted field:** This field is populated only for some types of predictions, and isn't used in churn prediction.
   - **Status:** Status of the prediction run.
        - **Queued:** Prediction is waiting for other processes to run.
        - **Refreshing:** Prediction is currently running to produce results that will flow into the output entity.
        - **Failed:** Prediction run has failed. [Review the logs](manage-predictions.md#troubleshoot-a-failed-prediction) for more details.
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


1. For business accounts, you'll find an **Influential feature analysis** information page. It contains four sections of data:

    1. The item selected in the right pane determines the content on this page. Select an item from **Top customers** or **Benchmark customers**. Both lists are ordered by decreasing value of the churn score, whether the score is just for the customer or a combined score for customers and a secondary level like product category.
        
        1. **Top customers**: List of 10 customers that are at highest risk of churn and lowest risk of churn based on their churn scores. 
        2. **Benchmark customers**: List of upto 10 customers that were selected while configuring the model.
 
    1. **Churn score:** Shows the churn score for the selected item in the right pane.
    
    1. **Churn risk distribution:** Shows the churn risk distribution across customers and the percentile in which the selected customer is. 
    
    1. **Top features increasing and decreasing churn risk:** For the selected item in the right pane, the top 5 features that increased and decreased the churn risk are highlighted. For every influential feature, you will be shown the value of the feature for that item as well as its impact or contribution towards the churn score. Moreover, the average value of each feature across low, medium and high churn customer segments is also shown. This will help you better contextualize the values of the top influential features for the selected item and compare it with low, medium and high churn customer segments.
     
    The low, medium and high churn segments are defined as follows:
    *Low = All accounts or combinations of account and secondary level whose churn score lies between 0 and 0.33
    *Medium = All accounts or combinations of accounts and secondary levels whose churn score lies between 0.33 and 0.66
    *High = All accounts or combinations of accounts and secondary levels whose churn score is greater than 0.66
    
    When you choose to predict churn at the account level, all accounts are considered in deriving the average feature values for low, medium and high churn segments. When churn predictions are made at the secondary level (e.g. product category) for every account, then the derivation of low, medium and high churn segments depends on the secondary level of the item selected in the side panel. For instance, if an item has a secondary level of product category = office supplies, then only the items having office supplies as the product category are considered when deriving the average feature values for low, medium and high churn segments. This is done to ensure a fair comparison of the item's feature values with the average values across low, medium and high churn segments.
    
    Note: In some cases, you might see that the average value of low, medium or high churn segments is "-" or not available. This might be due to the fact that there are no items that belong to the corresponding low, medium or high churn segments based on the above definition.

## Manage predictions

It's possible to optimize, troubleshoot, refresh, or delete predictions. Review an input data usability report to find out how to make a prediction faster and more reliable. For more information, see [Manage predictions](manage-predictions.md).


[!INCLUDE[footer-include](../includes/footer-banner.md)]
