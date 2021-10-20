---
title: Transaction churn prediction
description: "Predict whether a customer is at risk for no longer purchasing your products or services."
ms.date: 10/20/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: zacookmsft
ms.author: zacook
manager: shellyha
---

# Transaction churn prediction (preview)

Transactional churn prediction helps predict if a customer will no longer purchase your products or services in a given time window. You can create new churn predictions on **Intelligence** > **Predictions**. Select **My predictions** to see other predictions that you've created. 

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWN6Eg]

For environments based on business accounts, we can predict transactional churn for an account and also a combination of account and another level of information like product category. Adding a dimension can help find out how likely it is that the account "Contoso" will stop buying the product category "office stationery." In addition, for business accounts, we can also use AI to generate a list of potential reasons why an account is likely to churn for a category of secondary level information.

> [!TIP]
> Try the tutorial for a transaction churn prediction using sample data: [Transaction churn prediction (preview) sample guide](sample-guide-predict-transactional-churn.md).

## Prerequisites

# [Individual consumers (B-to-C)](#tab/b2c)

- At least [Contributor permissions](permissions.md) in Customer Insights.
- Business knowledge to understand what churn means for your business. We support time-based churn definitions, meaning a customer is considered to have churned after a period of no purchases.
- Data about your transactions/purchases and their history:
    - Transaction identifiers to distinguish purchases/transactions.
    - Customer identifiers to match transactions to your customers.
    - Transaction event dates, which define the dates the transaction occurred on.
    - The semantic data schema for purchases/transactions requires the following information:
        - **Transaction ID**: A unique identifier of a purchase or transaction.
        - **Transaction Date**: The date of the purchase or transaction.
        - **Value of the transaction**: The currency/numerical value amount of the transaction/item.
        - (Optional) **Unique product ID**: The ID of the product or service purchased if your data is at a line item level.
        - (Optional) **Whether this transaction was a return**: A true/false field that identifies if the transaction was a return or not. If the **Value of the transaction** is negative, we will also use this information to infer a return.
- (Optional) Data about customer activities:
    - Activity identifiers to distinguish activities of the same type.
    - Customer identifiers to map activities to your customers.
    - Activity information containing the name and date of the activity.
    - The semantic data schema for customer activities includes:
        - **Primary key:** A unique identifier for an activity. For example, a website visit or a usage record showing the customer tried a sample of your product.
        - **Timestamp:** The date and time of the event identified by the primary key.
        - **Event:** The name of the event you want to use. For example, a field called "UserAction" in a grocery store might be a coupon use by the customer.
        - **Details:** Detailed information about the event. For example, a field called "CouponValue" in a grocery store might be the currency value of the coupon.

# [Business accounts (B-to-B)](#tab/b2b)

- At least [Contributor permissions](permissions.md) in Customer Insights.
- Business knowledge to understand what churn means for your business. We support time-based churn definitions, meaning a customer is considered to have churned after a period of no purchases.
- Data about your transactions/purchases and their history:
    - Transaction identifiers to distinguish purchases/transactions.
    - Customer identifiers to match transactions to your customers.
    - Transaction event dates, which define the dates the transaction occurred on.
    - The semantic data schema for purchases/transactions requires the following information:
        - **Transaction ID**: A unique identifier of a purchase or transaction.
        - **Transaction Date**: The date of the purchase or transaction.
        - **Value of the transaction**: The currency/numerical value amount of the transaction/item.
        - (Optional) **Unique product ID**: The ID of the product or service purchased if your data is at a line item level.
        - (Optional) **Whether this transaction was a return**: A true/false field that identifies if the transaction was a return or not. If the **Value of the transaction** is negative, we will also use this information to infer a return.
- (Optional) Data about customer activities:
    - Activity identifiers to distinguish activities of the same type.
    - Customer identifiers to map activities to your customers.
    - Activity information containing the name and date of the activity.
    - The semantic data schema for customer activities includes:
        - **Primary key:** A unique identifier for an activity. For example, a website visit or a usage record showing the customer tried a sample of your product.
        - **Timestamp:** The date and time of the event identified by the primary key.
        - **Event:** The name of the event you want to use. For example, a field called "UserAction" in a grocery store might be a coupon use by the customer.
        - **Details:** Detailed information about the event. For example, a field called "CouponValue" in a grocery store might be the currency value of the coupon.
- (Optional) Data about your customers:
    - This data should only rarely, and should align toward more static attributes to ensure the model performs best.
    - The semantic data schema for customer data includes:
        - **CustomerID:** A unique identifier for a customer.
        - **Created Date:** The date the customer was initially added.
        - **State or Province:** The state or province location of a customer.
        - **Country:** The country of a customer.
        - **Industry:** The industry type of a customer. For example, a field called "Industry" in a coffee roaster might indicate if the customer was retail.
        - **Classification:** The categorization of a customer for your business. For example, a field called "ValueSegment" in a coffee roaster might be the tier of customer based on the customer size.

---

- Suggested data characteristics:
    - Sufficient historical data: Transaction data for at least double the selected time window. Preferably, two to three years of transaction history. 
    - Multiple purchases per customer: Ideally at least two transactions per customer.
    - Number of customers: At least 10 customer profiles, preferably more than 1,000 unique customers. The model will fail with fewer than 10 customers and insufficient historical data.
    - Data completeness: Less than 20% of missing values in the data field of the entity provided.

> [!NOTE]
> For a business with high customer purchase frequency (every few weeks) it's recommended to select a shorter prediction window and churn definition. For low purchase frequency (every few months or once a year), choose a longer prediction window and churn definition.

## Create a transaction churn prediction

1. In Customer Insights, go to **Intelligence** > **Predictions**.

1. Select the **Customer churn model (preview)** tile and select **Use this model**.

1. In the **Customer churn model** pane, choose **Transaction** and select **Get started**.

:::image type="content" source="media/select-transaction-churn.PNG" alt-text="Screenshot with selected transaction option in Customer churn model pane.":::

### Name model

1. Provide a name for the model to distinguish it from other models.

1. Provide a name for the output entity using letters and numbers only, without any spaces. That's the name that the model entity will use. 

1. Select **Next**.

### Define customer churn

1. Set a window of days to predict churn for in the **Identify customers who may churn in the next** field. For example, predict the risk of churn for your customers over the next 90 days to align to your marketing retention efforts. Predicting churn risk for a longer or shorter period of time can make it more difficult to address the factors in your churn risk profile, but it depends on your specific business requirements.
   >[!TIP]
   > You can select **Save and close** at any time to save the prediction as a draft. You'll find the draft prediction in the **My predictions** tab to continue.

1. Enter the number of days to define churn in the **A customer has churned if they've made no purchases in:** field. For example, if a customer has made no purchases in the last 30 days, they might be considered as churned for your business. 

1. Select **Next** to continue.

### Add required data

1. Select **Add data** and choose the activity type in the side pane that contains the required transaction or purchase history information.

1. Under **Choose the activities**, choose the specific activities from the selected activity you'd like the calculation to focus on.

   :::image type="content" source="media/product-recommendation-select-semantic-activity.PNG" alt-text="Side pane showing choosing specific activities under the semantic type.":::

1. If you haven't mapped the activity to a semantic type yet, select **Edit** to do so. The guided experience to map semantic activities opens. Map your data to the corresponding fields in the selected activity type.

   :::image type="content" source="media/product-recommendation-set-activity-type.PNG" alt-text="Page setting activity type.":::

1. After mapping the activity to the corresponding semantic type, select **Next** to proceed

1. Map the semantic attributes to the fields that are required to run the model. If the fields below aren't populated, configure the relationship from your purchase history entity to the *Customer* entity.

1. Select **Next**.

# [Individual consumers (B-to-C)](#tab/b2c)

### Add additional data (optional)

Configure the relationship from your customer activity entity to the *Customer* entity.

1. Select the field that identifies the customer in the customer activity table. It can be directly related to the primary customer ID of your *Customer* entity.

1. Select the entity that is your primary *Customer* entity.

1. Enter a name that describes the relationship.

#### Customer activities

1. Optionally, select **Add data** for **Customer activities**.

1. Select the semantic activity type that contains the data you would like to use, then select one or more activities in the **Activities** section.

1. Select an activity type that matches to the type of customer activity you're configuring. Select **Create new** and choose an available activity type or create a new type.

1. Select **Next**, then **Save**.

1. If you have any other customer activities you would like to include, repeat the steps above.

# [Business accounts (B-to-B)](#tab/b2b)

### Select prediction level

Most predictions are created at the customer level. In some situations, that may not be granular enough to address your business needs. You can use this feature to predict churn for a branch of a customer, for example, rather than for the customer as a whole.

1. To create a prediction at a more granular level than the customer, select **Select entity for a secondary level**. If the option is not available, ensure you have completed the previous section.

1. Expand the entities you would like to choose the secondary level from, or use the search filter box to filter the selected options.

1. Choose the attribute you would like used as a secondary level, then select **Add**.

1. Select **Next**.

> [!NOTE]
> The entities available in this section are shown because they have a relationship to the entity you chose in the previous section. If you don't see the entity you want to add, ensure it has a valid relationship present in **Relationships**. Only one-to-one and many-to-one relationships are valid for this configuration.

### Add additional data (optional)

Configure the relationship from your customer activity entity to the *Customer* entity.

1. Select the field that identifies the customer in the customer activity table. It can be directly related to the primary customer ID of your *Customer* entity.

1. Select the entity that is your primary *Customer* entity.

1. Enter a name that describes the relationship.

#### Customer activities

1. Optionally, select **Add data** for **Customer activities**.

1. Select the semantic activity type that contains the data you would like to use, then select one or more activities in the **Activities** section.

1. Select an activity type that matches to the type of customer activity you're configuring. Select **Create new** and choose an available activity type or create a new type.

1. Select **Next**, then **Save**.

1. If you have any other customer activities you would like to include, repeat the steps above.

#### Customers data

1. Optionally, select **Add data** for **Customers data**.

1. Map the semantic attributes to fields in your own customer data as identified. The data in the fields used should not change often to ensure the model's best performance. For example, selecting a field for "Classification" that changed every month would only have the last value used in the prediction, even though historically the same value might not apply to the customer when building the prediction patterns.

1. Select **Next**.

### Provide an optional list of benchmark accounts

Add a list of your business customers and accounts that you want to use as benchmarks. You'll get [details for these benchmark accounts](#review-a-prediction-status-and-results) including their churn score and most influential features that impacted their churn prediction.

1. Select **+ Add customers**.

1. Choose the customers that act as a benchmark.

1. Select **Next** to continue.

---

### Set schedule and review configuration

1. Set a frequency to retrain your model. This setting is important to update the accuracy of predictions as new data is ingested. Most businesses can retrain once per month and get a good accuracy for their prediction.

1. Select **Next**.

1. Review the configuration of the prediction. You can go back to prior steps by selecting **Edit** under the shown value. Or you can select a configuration step from the progress indicator.

1. If all values are configured correctly, select **Save and run** to begin the prediction process. On the **My predictions** tab, you can see the status of your predictions. The process may take several hours to complete depending on the amount of data used in the prediction.

## Review a prediction status and results

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.

1. Select the prediction you want to review.
   - **Prediction name**: Name of the prediction provided when creating it.
   - **Prediction type**: Type of model used for the prediction
   - **Output entity**: Name of the entity to store the output of the prediction. You can find an entity with this name on **Data** > **Entities**.
     In the output entity, *ChurnScore* is the predicted probability of churn and *IsChurn* is a binary label based on *ChurnScore* with 0.5 threshold. The default threshold might not work for your scenario. [Create a new segment](segments.md#create-a-new-segment) with your preferred threshold.
     Not all customers are necessarily active customers. Some of them may not have had any activity for a long time and are considered as churned already, based on you churn definition. Predicting the churn risk for customers who already churned isn't useful because they are not the audience of interest.
   - **Predicted field**: This field is populated only for some types of predictions, and isn't used in churn prediction.
   - **Status**: Status of the prediction run.
        - **Queued**: Prediction is waiting for other processes to run.
        - **Refreshing**: Prediction is currently running to produce results that will flow into the output entity.
        - **Failed**: Prediction run has failed. [Review the logs](manage-predictions.md#troubleshoot-a-failed-prediction) for more details.
        - **Succeeded**: Prediction has succeeded. Select **View** under the vertical ellipses to review the prediction
   - **Edited**: The date the configuration for the prediction was changed.
   - **Last refreshed**: The date the prediction refreshed results in the output entity.

1. Select the vertical ellipses next to the prediction you want to review results for and select **View**.

   :::image type="content" source="media/model-subs-view.PNG" alt-text="View control to see results of a prediction.":::

# [Individual consumers (B-to-C)](#tab/b2c)

1. There are three primary sections of data within the results page:
   - **Training model performance**: A, B, or C are possible scores. This score indicates the performance of the prediction and can help you make the decision to use the results stored in the output entity. Scores are determined based on the following rules: 
        - **A** when the model accurately predicted at least 50% of the total predictions, and when the percentage of accurate predictions for customers who churned is greater than the baseline rate by at least 10%.
            
        - **B** when the model accurately predicted at least 50% of the total predictions, and when the percentage of accurate predictions for customers who churned is up to 10% greater than the baseline.
            
        - **C** when the model accurately predicted less 50% of the total predictions, or when the percentage of accurate predictions for customers who churned is less than the baseline.
               
        - **Baseline** takes the prediction time window input for the model (for example, one year), and the model creates different fractions of time by dividing it by 2 until it reaches one month or less. It uses these fractions to create a business rule for customers who have not purchased in this time frame. These customers are considered as churned. The time-based business rule with the highest ability to predict who is likely to churn is chosen as baseline model.
            
    - **Likelihood to churn (number of customers)**: Groups of customers based on their predicted risk of churn. This data can help you later if you want to create a segment of customers with high churn risk. Such segments help to understand where your cutoff should be for segment membership.
       
    - **Most influential factors**: There are many factors that are taken into account when creating your prediction. Each of the factors has its importance calculated for the aggregated predictions a model creates. You can use these factors to help validate your prediction results, or you can use this information later to [create segments](segments.md) that could help influence churn risk for customers.


# [Business accounts (B-to-B)](#tab/b2b)

1. There are three primary sections of data within the results page:
   - **Training model performance**: A, B, or C are possible scores. This score indicates the performance of the prediction and can help you make the decision to use the results stored in the output entity. Scores are determined based on the following rules: 
        - **A** when the model accurately predicted at least 50% of the total predictions, and when the percentage of accurate predictions for customers who churned is greater than the baseline rate by at least 10%.
            
        - **B** when the model accurately predicted at least 50% of the total predictions, and when the percentage of accurate predictions for customers who churned is up to 10% greater than the baseline.
            
        - **C** when the model accurately predicted less 50% of the total predictions, or when the percentage of accurate predictions for customers who churned is less than the baseline.
               
        - **Baseline** takes the prediction time window input for the model (for example, one year), and the model creates different fractions of time by dividing it by 2 until it reaches one month or less. It uses these fractions to create a business rule for customers who have not purchased in this time frame. These customers are considered as churned. The time-based business rule with the highest ability to predict who is likely to churn is chosen as baseline model.
            
    - **Likelihood to churn (number of customers)**: Groups of customers based on their predicted risk of churn. This data can help you later if you want to create a segment of customers with high churn risk. Such segments help to understand where your cutoff should be for segment membership.
       
    - **Most influential factors**: There are many factors that are taken into account when creating your prediction. Each of the factors has its importance calculated for the aggregated predictions a model creates. You can use these factors to help validate your prediction results, or you can use this information later to [create segments](segments.md) that could help influence churn risk for customers.


1. For business accounts, you'll find an **Influential feature analysis** information page. It contains four sections of data:

    - The item selected in the right pane determines the content on this page. Select an item from **Top customers** or **Benchmark customers**. Both lists are ordered by decreasing value of the churn score, whether the score is just for the customer or a combined score for customers and a secondary level like product category.
        
        - **Top customers**: List of 10 customers that are at highest risk of churn and lowest risk of churn based on their churn scores. 
        - **Benchmark customers**: List of up to 10 customers that were selected while configuring the model.
 
    - **Churn score:** Shows the churn score for the selected item in the right pane.
    
    - **Churn risk distribution:** Shows the churn risk distribution across customers and the percentile in which the selected customer is. 
    
    - **Top features increasing and decreasing churn risk:** For the selected item in the right pane, the top five features that increased and decreased the churn risk are listed. For every influential feature, you find the value of the feature for that item and its influence on the churn score. The average value of each feature across low, medium, and high churn customer segments is also shown. It helps to better contextualize the values of the top influential features for the selected item and compare it with low, medium, and high churn customer segments.

       - Low: accounts or combinations of account and secondary level with a churn score between 0 and 0.33
       - Medium: accounts or combinations of accounts and secondary levels with a churn score between 0.33 and 0.66
       - High: accounts or combinations of accounts and secondary levels with a churn score greater than 0.66
    
       When you predict churn at the account level, all accounts are considered in deriving the average feature values for churn segments. For churn predictions at the secondary level for every account, the derivation of churn segments depends on the secondary level of the item selected in the side pane. For example, if an item has a secondary level of product category = office supplies, then only the items having office supplies as the product category are considered when deriving the average feature values for churn segments. This logic is applied to ensure a fair comparison of the item's feature values with the average values across low, medium, and high churn segments.

       In some cases, the average value of low, medium, or high churn segments is empty or not available because there are no items that belong to the corresponding churn segments based on the above definition.

---

## Manage predictions

It's possible to optimize, troubleshoot, refresh, or delete predictions. Review an input data usability report to find out how to make a prediction faster and more reliable. For more information, go to [Manage predictions](manage-predictions.md).

[!INCLUDE[footer-include](../includes/footer-banner.md)]
