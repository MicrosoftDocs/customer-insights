---
title: Transaction churn prediction (contains video)
description: "Predict whether a customer is at risk for no longer purchasing your products or services."
ms.date: 09/12/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: zacookmsft
ms.author: zacook
manager: shellyha
---

# Predict transaction churn

Transactional churn prediction helps predict if a customer will no longer purchase your products or services in a given time window.

You must have business knowledge to understand what churn means for your business. We support time-based churn definitions, meaning a customer is considered to have churned after a period of no purchases.

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWN6Eg]

For environments based on business accounts, we can predict transactional churn for an account and also a combination of account and another level of information like product category. For example, adding a dimension can help determine how likely it is that the account "Contoso" will stop buying the product category "office stationery." In addition, for business accounts, we can also use AI to generate a list of potential reasons why an account is likely to churn for a category of secondary level information.

> [!TIP]
> Try the tutorial for a transaction churn prediction using sample data: [Transaction churn prediction sample guide](sample-guide-predict-transactional-churn.md).

## Prerequisites

- At least [Contributor permissions](permissions.md).
- Customer Identifier, a unique identifier to match transactions to your customers.
- Transaction history must include:
  - **Transaction ID**: Unique identifier of a purchase or transaction.
  - **Transaction Date**: Date of the purchase or transaction.
  - **Value of the transaction**: Currency or numerical value amount of the transaction.

### Recommended data

The following data is optional, but recommended for increased model performance. The more data the model can process, the more accurate the prediction. Therefore, we encourage you to ingest more customer activity data, if available.

# [Individual consumers (B-to-C)](#tab/b2c)

- Transaction history data:
  - **Unique product ID**: ID of the product or service purchased if your data is at a line item level.
  - **Whether this transaction was a return**: A true/false field that identifies if the transaction was a return or not. If the **Value of the transaction** is negative, we infer a return.
- Customer activity data:
  - Customer Identifier, a unique identifier to map activities to your customers.
  - **Primary key:** Unique identifier for an activity. For example, a website visit or a usage record showing the customer tried a sample of your product.
  - **Timestamp:** Date and time of the event identified by the primary key.
  - **Event:** Name of the event you want to use. For example, a field called "UserAction" in a grocery store might be a coupon use by the customer.
  - **Details:** Detailed information about the event. For example, a field called "CouponValue" in a grocery store might be the currency value of the coupon.

# [Business accounts (B-to-B)](#tab/b2b)


---

- Suggested data characteristics:
  - Sufficient historical data: Transaction data for at least double the selected time window. Preferably, two to three years of transaction history.
  - Multiple purchases per customer: Ideally at least two transactions per customer.
  - Number of customers: At least 10 customer profiles, preferably more than 1,000 unique customers. The model will fail with fewer than 10 customers and insufficient historical data.
  - Data completeness: Less than 20% of missing values in the data field of the entity provided.

> [!NOTE]
> For a business with high customer purchase frequency (every few weeks) it's recommended to select a shorter prediction window and churn definition. For low purchase frequency (every few months or once a year), choose a longer prediction window and churn definition.

The following data is optional, but recommended for increased model performance.

- **Unique product ID** (optional): ID of the product or service purchased if your data is at a line item level.
- **Whether this transaction was a return** (optional): A true/false field that identifies if the transaction was a return or not. If the **Value of the transaction** is negative, we infer a return.

  
- Data about customer activities (optional):
  - Activity identifiers to distinguish activities of the same type.
  - Customer identifiers to map activities to your customers.
  - Activity information containing the name and date of the activity.
  - The following semantic data schema for customer activities:
    - **Primary key:** Unique identifier for an activity. For example, a website visit or a usage record showing the customer tried a sample of your product.
    - **Timestamp:** Date and time of the event identified by the primary key.
    - **Event:** Name of the event you want to use. For example, a field called "UserAction" in a grocery store might be a coupon use by the customer.
    - **Details:** Detailed information about the event. For example, a field called "CouponValue" in a grocery store might be the currency value of the coupon.
- Data about your customers (optional):
  - This data should align toward more static attributes to ensure the model performs best.
  - The following semantic data schema for customer data:
    - **CustomerID:** Unique identifier for a customer.
    - **Created Date:** Date the customer was initially added.
    - **State or Province:** State or province location of a customer.
    - **Country:** Country of a customer.
    - **Industry:** Industry type of a customer. For example, a field called "Industry" in a coffee roaster might indicate if the customer was retail.
    - **Classification:** Categorization of a customer for your business. For example, a field called "ValueSegment" in a coffee roaster might be the tier of customer based on the customer size.


## Create a transaction churn prediction

1. Go to **Intelligence** > **Predictions**.

1. On the **Create** tab, select **Use model** on the **Customer churn model** tile.

1. Select **Transaction** for the type of churn and then **Get started**.

1. **Name this model** and the **Output entity name** to distinguish them from other models or entities.

1. Select **Next**.

### Define customer churn

1. For the **Preferences** step, set the **Prediction window**. For example, predict the risk of churn for your customers over the next 90 days to align to your marketing retention efforts. Predicting churn risk for a longer or shorter period of time can make it more difficult to address the factors in your churn risk profile, but it depends on your specific business requirements.

   > [!TIP]
   > Select **Save draft** at any time to save the prediction as a draft. The draft prediction displays in the **My predictions** tab.

1. Enter the number of days to define churn in the **Churn definition** field. For example, if a customer has made no purchases in the last 30 days, they might be considered as churned for your business.

1. Select **Next**.

### Add required data

1. For the **Purchase history (required)** step, select **Add data** for **Customer transaction history**.

1. Select the semantic activity type, **SalesOrder** or **SalesOrderLine**, that contains the transaction history information. If the activity has not been set up, select **here**.

   :::image type="content" source="media/transaction-churn-select-activity.PNG" alt-text="Side pane showing choosing specific activities under the semantic type.":::

1. Under **Activities**, if the activity attributes were semantically mapped when the activity was created, choose the specific attributes or entity you'd like the calculation to focus on. If semantic mapping did not occur, select **Edit** and map your data.

1. Select **Next** and review the attributes required for this model.

1. Select **Save**.

1. Select **Next** to proceed if you don't want to add more activities.


# [Individual consumers (B-to-C)](#tab/b2c)

### Add additional data (optional)

1. For the **Add additional data (optional)** step, select **Add data** for **Customer activities**.

1. Select the semantic activity type that contains the data you would like to use. If the activity has not been set up, select **here**.

1. Under **Activities**, if the activity attributes were semantically mapped when the activity was created, choose the specific attributes or entity you'd like the calculation to focus on. If semantic mapping did not occur, select **Edit** and map your data.

1. Select **Next** and review the attributes required for this model.

1. Select **Save**.

1. Select **Next**

# [Business accounts (B-to-B)](#tab/b2b)

### Select prediction level

Most predictions are created at the customer level. In some situations, that may not be granular enough to address your business needs. Use this feature to predict churn for a branch of a customer, for example, rather than for the customer as a whole.

1. Select **Select entity for a secondary level**. If the option is not available, ensure you have completed the previous section.

1. Expand the entities you would like to choose the secondary level from, or use the search filter box to filter the selected options.

1. Choose the attribute you would like used as a secondary level, then select **Add**.

1. Select **Next**.

> [!NOTE]
> The entities available in this section are shown because they have a relationship to the entity you chose in the previous section. If you don't see the entity you want to add, ensure it has a valid relationship present in **Relationships**. Only one-to-one and many-to-one relationships are valid for this configuration.

### Add additional data (optional)

1. For the **Add additional data (optional)** step, select **Add data** for **Customer activities**.

1. Select the semantic activity type that contains the data you would like to use. If the activity has not been set up, select **here**.

1. Under **Activities**, if the activity attributes were semantically mapped when the activity was created, choose the specific attributes or entity you'd like the calculation to focus on. If semantic mapping did not occur, select **Edit** and map your data.

1. Select **Next** and review the attributes required for this model.

1. Select **Save**.

1. Select **Next**

1. Optionally, select **Add data** for **Customers data**.

1. Map the semantic attributes to fields in your own customer data as identified. The data in the fields used should not change often to ensure the model's best performance. For example, selecting a field for "Classification" that changed every month would only have the last value used in the prediction, even though historically the same value might not apply to the customer when building the prediction patterns.

1. Select **Next**.

### Provide an optional list of benchmark accounts

Add a list of your business customers and accounts that you want to use as benchmarks. The [details for these benchmark accounts](#view-prediction-results) include their churn score and most influential features that impacted their churn prediction.

1. Select **+ Add customers**.

1. Choose the customers that act as a benchmark.

1. Select **Next**.

---

### Set update schedule

1. For the **Data updates** step, choose a frequency to retrain your model. This setting is important to update the accuracy of predictions as new data is ingested into Customer Insights. Most businesses can retrain once per month and get a good accuracy for their prediction.

1. Select **Next**.

### Review and run the model configuration

The **Review and run** step shows a summary of the configuration and provides a chance to make changes before you create the prediction.

1. Select **Edit** on any of the steps to review and make any changes.

1. If you are satisfied with your selections, select **Save and run** to start running the model. Select **Done**. The **My predictions** tab displays while the prediction is being created. The process may take several hours to complete depending on the amount of data used in the prediction.

[!INCLUDE [progress-details](includes/progress-details-pane.md)]

## View prediction results

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.

1. Select the prediction you want to review.

There are three primary sections of data within the results page:
- **Training model performance**: Grades A, B, or C indicate the performance of the prediction and can help you make the decision to use the results stored in the output entity.

  Grades are determined based on the following rules:
  - **A** when the model accurately predicted at least 50% of the total predictions, and when the percentage of accurate predictions for customers who churned is greater than the baseline rate by at least 10%.
  - **B** when the model accurately predicted at least 50% of the total predictions, and when the percentage of accurate predictions for customers who churned is up to 10% greater than the baseline.
  - **C** when the model accurately predicted less than 50% of the total predictions, or when the percentage of accurate predictions for customers who churned is less than the baseline.
  - **Baseline** takes the prediction time window input for the model (for example, one year), and creates different fractions of time by dividing it by 2 until it reaches one month or less. It uses these fractions to create a business rule for customers who have not purchased in this time frame. These customers are considered as churned. The time-based business rule with the highest ability to predict who is likely to churn is chosen as the baseline model.

- **Likelihood to churn (number of customers)**: Groups of customers based on their predicted risk of churn. Optionally, [create segments of customers](segments.md) with high churn risk. Such segments help to understand where your cutoff should be for segment membership.

- **Most influential factors**: There are many factors that are taken into account when creating your prediction. Each of the factors has its importance calculated for the aggregated predictions a model creates. Use these factors to help validate your prediction results. Or use this information later to [create segments](segments.md) that could help influence churn risk for customers.

For business accounts, an **Influential feature analysis** information page contains four sections of data:

- In the right pane, select an item from **Top customers** or **Benchmark customers**. Both lists are ordered by decreasing value of the churn score, whether the score is just for the customer or a combined score for customers and a secondary level like product category. The item selected determines the content on this page.

  - **Top customers**: List of 10 customers that are at highest risk of churn and lowest risk of churn based on their churn scores.
  - **Benchmark customers**: List of up to 10 customers that were selected while configuring the model.

- **Churn score:** Shows the churn score for the selected item in the right pane.

- **Churn risk distribution:** Shows the churn risk distribution across customers and the percentile the selected customer is in.

- **Top features increasing and decreasing churn risk:** Lists the top five features that increased and decreased the churn risk for the selected item in the right pane. Shows the value of the feature for that item and its influence on the churn score for every influential feature. The average value of each feature across low, medium, and high churn customer segments is also shown. It helps to better contextualize the values of the top influential features for the selected item and compare it with low, medium, and high churn customer segments.

  - Low: accounts or combinations of account and secondary level with a churn score between 0 and 0.33.
  - Medium: accounts or combinations of accounts and secondary levels with a churn score between 0.33 and 0.66.
  - High: accounts or combinations of accounts and secondary levels with a churn score greater than 0.66.

  When you predict churn at the account level, all accounts are considered in deriving the average feature values for churn segments. For churn predictions at the secondary level for every account, the derivation of churn segments depends on the secondary level of the item selected in the side pane. For example, if an item has a secondary level of product category = office supplies, then only the items having office supplies as the product category are considered when deriving the average feature values for churn segments. This logic is applied to ensure a fair comparison of the item's feature values with the average values across low, medium, and high churn segments.

  In some cases, the average value of low, medium, or high churn segments is empty or not available because there are no items that belong to the corresponding churn segments based on the above definition.

  > [!NOTE]
  > The interpretation of values under the average low, medium, and high columns is different for categorical features like country or industry. Because the notion of "average" feature value doesn't apply to categorical features, the values in these columns are the proportion of customers in low, medium, or high churn segments that have the same value of the categorical feature as compared to the item selected in the side panel.

In addition to these results, the output entity contains scoring data. Go to **Data** > **Entities** and view the data tab for the output entity you defined for this model. *ChurnScore* is the predicted probability of churn and *IsChurn* is a binary label based on *ChurnScore* with 0.5 threshold. The default threshold might not work for your scenario. If not, [create a new segment](segments.md#create-a-segment) with your preferred threshold. Not all customers are necessarily active customers. Some of them may not have had any activity for a long time and are considered as churned already, based on you churn definition. Predicting the churn risk for customers who already churned isn't useful because they are not the audience of interest.

[!INCLUDE [footer-include](includes/footer-banner.md)]
