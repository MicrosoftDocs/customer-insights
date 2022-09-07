---
title: Customer lifetime value (CLV) prediction
description: "Predict revenue potential for active customers in the future."
ms.date: 09/07/2022
ms.reviewer: mhart
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: wameng
manager: shellyha
searchScope: 
  - ci-predictions
  - ci-create-prediction
  - ci-custom-models
  - customerInsights
---

# Customer lifetime value (CLV) prediction

Predict potential value (revenue) that individual active customers will bring in to your business through a defined future time period. This prediction helps you achieve various goals:

- Identify high-value customers and process this insight.
- Create strategical customer segments based on their potential value to run personalized campaigns with targeted sales, marketing, and support efforts.
- Guide product development by focusing on features that increase customer value.
- Optimize sales or marketing strategy and allocate budget more accurately for customer outreach.
- Recognize and reward high-value customers through loyalty or rewards programs.

Before getting started, reflect what CLV means for your business. We support transaction-based CLV prediction. The predicted value of a customer is based on the history of business transactions. Since configuring and running a CLV model doesn't take much time, consider creating several models with varying input preferences and compare model results to see which model scenario best fits your business needs.

## Prerequisites

- At least [Contributor](permissions.md) permissions

### Data requirements

The following data is recommended for increased model performance. Fields marked as optional are still recommended. The more data the model can process, the more accurate the prediction will be. Therefore, we encourage you to ingest more customer activity data, if available.

- Customer Identifier: Unique identifier to match transactions to an individual customer

- Transaction History: Historical transactions log with the following semantic data schema:
  - **Transaction ID**: Unique identifier of each transaction
  - **Transaction date**: Date or time stamp of each transaction
  - **Transaction amount**: Monetary value (for example, revenue or profit margin) of each transaction
  - **Label assigned to returns** (optional): Boolean value signifying whether the transaction is a return
  - **Product ID** (optional): Product ID of product involved in the transaction

- Additional data (optional), for example:
  - Web activities: Website visit history, email history
  - Loyalty activities: Loyalty reward points accrual and redemption history
  - Customer service log: Service call, complaint, or return history
  - Customer profile information

- Data about customer activities (optional):
  - Activity identifiers to distinguish activities of the same type
  - Customer identifiers to map activities to your customers
  - Activity information containing the name and date of the activity
  - The semantic data schema for activities includes:
    - **Primary key**: A unique identifier for an activity
    - **Timestamp**: The date and time of the event identified by the primary key
    - **Event (activity name)**:  The name of event you want to use
    - **Details (amount or value)**: Details about the customer activity

- Suggested data characteristics:
  - Sufficient historical data: At least one year of transactional data. Preferably two to three years of transactional data to predict CLV for one year.
  - Multiple purchases per customer: Ideally, at least two to three transactions per customer ID, preferably across multiple dates.
  - Number of customers: At least 100 unique customers, preferably more than 10,000 customers. The model will fail with fewer than 100 customers and insufficient historical data.
  - Data completeness: Less than 20% missing values in required fields in the input data.

> [!NOTE]
> - The model requires the transaction history of your customers. Only one transaction history entity can be configured. If there are multiple purchase/transaction entities, combine them in Power Query before data ingestion.
> - Optionally, for additional customer activity data, add as many customer activity entities as you'd like for consideration by the model.

## Create a Customer Lifetime Value prediction

1. Go to **Intelligence** > **Predictions**.

1. On the **Create** tab, select **Use model** on the **Customer lifetime value** tile.

1. In the **Customer lifetime value** pane, select **Get started**.

1. **Name this model** and the **Output entity name** to distinguish them from other models or entities.

1. Select **Next**.

### Define model preferences

1. For the **Model preferences** step, set a **Prediction time period** to define how far into the future you want to predict the CLV. By default, the unit is set as months.

   > [!TIP]
   > To accurately predict CLV for the set time period, a comparable period of historical data is required. For example, if you want to predict CLV for the next 12 months, have at least 18 – 24 months of historical data.

1. Specify what **Active customers** mean for your business. Set the time frame in which a customer must have had at least one transaction to be considered active. The model only predicts CLV for active customers.
   - **Let model calculate purchase interval (recommended)**: The model analyzes your data and determines a time period based on historical purchases.
   - **Set interval manually**: If you have a specific business definition of an active customer, choose this option and set the time period accordingly.

1. Define the percentile of your active customers you consider to be **High-value customer**.
    - **Model calculation (recommended)**: The model analyzes your data and determines what a high value customer might be for your business based on your customers’ transaction history. The model uses a heuristic rule (inspired by the 80/20 rule or pareto principle) to find the proportion of high-value customers. The percentage of customers that contributed to 80% cumulative revenue for your business in the historical period are considered high-value customers. Typically, less than 30-40% customers contribute to 80% cumulative revenue. However, this number might vary depending on your business and industry.
    - **Percent of top active customers**: If you have a specific percentile for a high-value customer, choose this option and set the percentile. For example, use this option to define high-value customers as the top 20% of future paying customers.

    If your business defines high value customers in a different way, [let us know as we would love to hear](https://go.microsoft.com/fwlink/?linkid=2074172).

1. Select **Next**.

### Add required data

1. For the **Required data** step, select **Add data** for **Customer transaction history**.

1. Select **SalesOrder** or **SalesOrderLine** that contains the transaction history information. If the activity has not been set up, select **here**.

1. Under **Activities**, choose the specific activities or entity you'd like the calculation to focus on and select **Next**.

1. Select **Save**.

1. Select **Next**.

### Add optional activity data

Data reflecting key customer interactions (like web, customer service, and event logs) adds context to transaction records. More patterns found in your customer activity data can improve the accuracy of the predictions.

1. For the **Additional data (optional)** step, select **Add data** under **Boost model insights with additional activity data**.

1. Select an activity type and entity that matches the type of customer activity you're adding. Choose from existing activity types or add a new activity type. Select **Next**.

1. Map the attributes if they are not already mapped and select **Save**.

1. [Add optional customer data](#add-optional-customer-data) or select **Next** and go to [Set update schedule](#set-update-schedule).

### Add optional customer data

Select from 18 commonly used customer profile attributes to include as an input to the model. These attributes can lead to more personalized, relevant, and actionable model results for your business use cases.

For example: Contoso Coffee wants to predict customer lifetime value to target high value customers with a personalized offer related to the launch of their new espresso machine. Contoso uses the CLV model and adds all 18 customer profile attributes to see which factors influence their highest value customers. They find customer location is the most influential factor for these customers.
With this information, they organize a local event for the launch of the espresso machine and partner with local vendors for personalized offers and a special experience at the event. Without this information, Contoso might have only sent generic marketing emails and missed the opportunity to personalize for this local segment of their high value customers.

1. Select **Add data** under **Boost model insights even further with additional customer data**.

1. For **Entity**, choose **Customer : CustomerInsights** to select the unified customer profile that maps to customer attribute data. For **Customer ID**, choose **System.Customer.CustomerId**.

1. Map more fields if the data is available in your unified customer profiles.

   :::image type="content" source="media/clv-optional-customer-profile-mapping.png" alt-text="Example of mapped fields for customer profile data.":::

1. Select **Save**.

1. Select **Next**.

### Set update schedule

1. For the **Data update schedule** step, choose the frequency to retrain your model based on the latest data. This setting is important to update the accuracy of predictions as new data is ingested into Customer Insights. Most businesses can retrain once per month and get a good accuracy for their prediction.

1. Select **Next**.

### Review and run the model configuration

The **Review your model details** step shows a summary of the configuration and provides a chance to make changes before you create the prediction.

1. Select **Edit** on any of the steps to review and make any changes.

1. If you are satisfied with your selections, select **Save and run** to start running the model. Select **Done**. The **My predictions** tab displays while the prediction is being created. The process may take several hours to complete depending on the amount of data used in the prediction.

[!INCLUDE [progress-details](includes/progress-details-pane.md)]

## View prediction results

1. Go to **Intelligence** > **Predictions**.

1. In the **My predictions** tab, select the prediction you want to view.

There are three primary sections of data within the results page.

- **Training model performance**: Grades A, B, or C indicate the performance of the prediction and can help you make the decision to use the results stored in the output entity.
  
  :::image type="content" source="media/clv-model-score.png" alt-text="Image of the model score information box with the grade A.":::

  Customer Insights assesses how the AI model performed in predicting the high value customers as compared to a baseline model.

  Grades are determined based on the following rules:
  - **A** when the model accurately predicted at least 5% more high-value customers as compared to the baseline model.
  - **B** when the model accurately predicted between 0-5% more high-value customers as compared to the baseline model.
  - **C** when the model accurately predicted fewer high-value customers as compared to the baseline model.
  
  Select [**Learn about this score**](#learn-about-the-score) to open the **Model rating** pane which shows further details about the AI model performance and the baseline model. It will help you better understand the underlying model performance metrics and how the final model performance grade was derived. The baseline model uses a non-AI based approach to calculate customer lifetime value based primarily on historical purchases made by customers.

- **Value of customers by percentile**: Low-value and high-value customers display in a chart. Hover over the bars in the histogram to see the number of customers in each group and the average CLV of that group. Optionally, [create segments of customers](segments.md) based on their CLV predictions.

- **Most influential factors**: Various factors are considered when creating your CLV prediction based on the input data provided to the AI model. Each of the factors has their importance calculated for the aggregated predictions a model creates. You can use these factors to help validate your prediction results. These factors also provide more insight about the most influential factors that contributed towards predicting CLV across all your customers.

### Learn about the score

The standard formula used to calculate CLV by the baseline model:

  _**CLV for each customer** = Average monthly purchase made by the customer in the active customer window * Number of months in the CLV prediction period * Overall retention rate of all customers_

The AI model is compared to the baseline model based on two model performance metrics.
  
- **Success rate in predicting high-value customers**

  See the difference in predicting high-value customers using the AI model compared to the baseline model. For example, 84% success rate means that out of all the high-value customers in the training data, the AI model was able to accurately capture 84%. We then compare this success rate with the success rate of the baseline model to report the relative change. This value is used to assign a grade to the model.

- **Error metrics**

  See the overall performance of the model in terms of error in predicting future values. We use the overall Root Mean Squared Error (RMSE) metric to assess this error. RMSE is a standard way to measure the error of a model in predicting quantitative data. The AI model’s RMSE is compared to the RMSE of the baseline model and the relative difference is reported.

The AI model prioritizes the accurate ranking of customers according to the value they bring to your business. So only the success rate of predicting high-value customers is used to derive the final model grade. The RMSE metric is sensitive to outliers. In scenarios where you have a small percentage of customers with extraordinarily high purchase values, the overall RMSE metric might not give the full picture of the model performance.

[!INCLUDE [footer-include](includes/footer-banner.md)]
