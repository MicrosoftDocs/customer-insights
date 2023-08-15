---
title: Predict transaction churn for business accounts
description: "Predict whether an account is at risk for no longer purchasing your products or services in Dynamics 365 Customer Insights."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: zacookmsft
ms.author: zacook
---

# Predict transaction churn for business accounts

[!INCLUDE [consolidated-sku](../includes/consolidated-sku.md)]

Transactional churn prediction helps predict if an account will no longer purchase products or services in a given time window.

We can predict transactional churn for an account and also a combination of account and another level of information like product category. For example, adding a dimension can help determine how likely it is that the account "Contoso" will stop buying the product category "office stationery." In addition, for business accounts, we can also use AI to generate a list of potential reasons why an account is likely to churn for a category of secondary level information.

You must have business knowledge to understand what churn means for your business. We support time-based churn definitions, meaning a customer is considered to have churned after a period of no purchases.

## Prerequisites

[!INCLUDE [prediction-transaction-prereqs](../includes/predict-transaction-prereqs.md)]

Add customer data aligned toward more static attributes to ensure the model performs best:
- **CustomerID:** Unique identifier for a customer.
- **Created Date:** Date the customer was initially added.
- **State or Province:** State or province location of a customer.
- **Country:** Country of a customer.
- **Industry:** Industry type of a customer. For example, a field called "Industry" in a coffee roaster might indicate if the customer was retail.
- **Classification:** Categorization of a customer for your business. For example, a field called "ValueSegment" in a coffee roaster might be the tier of customer based on the customer size.

> [!NOTE]
> For a business with high customer purchase frequency (every few weeks) it's recommended to select a shorter prediction window and churn definition. For low purchase frequency (every few months or once a year), choose a longer prediction window and churn definition.

## Create a transaction churn prediction for business accounts

[!INCLUDE [prediction-transaction-create](../includes/predict-transaction-create.md)]

### Select prediction level

Most predictions are created at the customer level. In some situations, that may not be granular enough to address your business needs. Use this feature to predict churn for a branch of a customer, for example, rather than for the customer as a whole.

1. Select **Select table for a secondary level**. If the option is not available, ensure you have completed the previous section.

1. Expand the tables you would like to choose the secondary level from, or use the search filter box to filter the selected options.

1. Choose the attribute you would like used as a secondary level, then select **Add**.

1. Select **Next**.

> [!NOTE]
> The tables available in this section are shown because they have a relationship to the table you chose in the previous section. If you don't see the table you want to add, ensure it has a valid relationship present in **Relationships**. Only one-to-one and many-to-one relationships are valid for this configuration.

### Add additional data (optional)

1. Select **Add data** for **Customer activities**.

1. Select the semantic activity type that contains the data you would like to use. If the activity has not been set up, select **here** and create it.

1. Under **Activities**, if the activity attributes were semantically mapped when the activity was created, choose the specific attributes or table you'd like the calculation to focus on. If semantic mapping did not occur, select **Edit** and map your data.

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

[!INCLUDE [predict-transaction-create-last-steps](../includes/predict-transaction-create2.md)]

[!INCLUDE [progress-details](../includes/progress-details-pane.md)]

## View prediction results

1. Go to **Insights** > **Predictions**.

1. In the **My predictions** tab, select the prediction you want to view.

There are three primary sections of data within the results page:

[!INCLUDE [predict-transaction-results](../includes/predict-transaction-results.md)]

An **Influential feature analysis** information page contains four sections of data:

- In the right pane, select an item from **Top customers** or **Benchmark customers**. Both lists are ordered by decreasing value of the churn score, whether the score is just for the customer or a combined score for customers and a secondary level like product category. The item selected determines the content on this page.

  - **Top customers**: List of 10 customers that are at highest risk of churn and lowest risk of churn based on their churn scores.
  - **Benchmark customers**: List of up to 10 customers that were selected while configuring the model.

- **Churn score:** Shows the churn score for the selected item in the right pane.

- **Churn risk distribution:** Shows the churn risk distribution across customers and the percentile the selected customer is in.

- **Top features increasing and decreasing churn risk:** Lists the top five features that increased and decreased the churn risk for the selected item in the right pane. Shows the value of the feature for that item and its influence on the churn score for every influential feature. The average value of each feature across low, medium, and high churn customer segments is also shown. It helps to better contextualize the values of the top influential features for the selected item and compare it with low, medium, and high churn customer segments.

  - Low: accounts or combinations of account and secondary level with a churn score between 0 and 0.33.
  - Medium: accounts or combinations of accounts and secondary levels with a churn score between 0.33 and 0.66.
  - High: accounts or combinations of accounts and secondary levels with a churn score greater than 0.66.

  When you predict churn at the account level, all accounts are considered in deriving the average feature values for churn segments. For churn predictions at the secondary level for every account, the derivation of churn segments depends on the secondary level of the item selected in the side pane. For example, if an item has a secondary level of product category (office supplies), then only the items having office supplies as the product category are considered when deriving the average feature values for churn segments. This logic is applied to ensure a fair comparison of the item's feature values with the average values across low, medium, and high churn segments.

  In some cases, the average value of low, medium, or high churn segments is empty or not available because there are no items that belong to the corresponding churn segments based on the above definition.

  The interpretation of values under the average low, medium, and high columns is different for categorical features like country or industry. Because the notion of "average" feature value doesn't apply to categorical features, the values in these columns are the proportion of customers in low, medium, or high churn segments that have the same value of the categorical feature as compared to the item selected in the side panel.

[!INCLUDE [predict-transaction-churn-note](../includes/predict-transaction-churn-note.md)]
