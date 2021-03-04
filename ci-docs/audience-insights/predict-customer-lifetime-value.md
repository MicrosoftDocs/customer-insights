---
title: Customer lifetime value (CLV) prediction
description: "Predict revenue potential for active customers in the future."
ms.date: 02/05/2021
ms.reviewer: wameng
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Customer lifetime value (CLV) prediction (Preview)

Predict potential value (revenue) that individual active customers will bring in to your business through a defined future time period. This feature can help you achieve various goals: 
- Identify high-value customers and process this insight
- Create strategical customer segments based on their potential value to run personalized campaigns with targeted sales, marketing, and support efforts
- Guide product development by focusing on features tht increase customer value
- Optimize sales or marketing strategy and allocate budget more accurately for customer outreach
- Recognize and reward high-value customers through loyalty or rewards programs 

## Prerequisites

Before getting started, reflect what CLV means for your business. Currently, we support transaction-based CLV prediction. The predicted value of a customer is based on history of business transactions. To create the prediction, you need at least [Contributor](permissions.md) permissions.

Since configuring and running a CLV model doesn't take much time, consider creating several models with varying input preferences and compare model results to see which model scenario best fits your business needs.

###  Data requirements

The following data is required, and where marked optional, recommended for increased model performance. The more data the model can process, the more accurate the prediction will be. Therefore, we encourage you to ingest more customer activity data, if available.

- Customer Identifier: Unique identifier to match transactions to an individual customer

- Transaction History: Historical transactions log with below semantic data schema
    - Transaction ID: Unique identifier of each transaction
    - Transaction date: Date, preferably a time stamp of each transaction
    - Transaction amount: Monetary value (for example, revenue or profit margin) of each transaction
    - Label assigned to returns (optional): Boolean value signifying whether the transaction is a return 
    - Product ID (optional): Product ID of product involved in the transaction

- Additional data (optional), for example
    - Web activities: website visit history, email history
    - Loyalty activities: loyalty reward points accrual and redemption history
    - Customer service log, service call, complaint, or return history
- Data about customer activities (optional):
    - Activity identifiers to distinguish activities of the same type
    - Customer identifiers to map activities to your customers
    - Activity information containing the name and date of the activity
    - The semantic data schema for activities includes: 
        - Primary key: A unique identifier for an activity
        - Timestamp: The date and time of the event identified by the primary key
        - Event (activity name):  The name of event you want to use
        - Details (amount or value): Details about the customer activity

## Create a Customer Lifetime Value prediction

1. In audience insights, go to **Intelligence** > **Predictions**.

1. Select the **Customer lifetime value** tile and select **Use model**. 

1. In the **Customer lifetime value (preview)** pane, select **Get started**.

1. **Name this model** and the **Output entity name** to distinguish them from other models or entities.

1. Select **Next**.

### Define model preferences

1. Set a **Prediction time period** to define how far into the future you want to predict the CLV.    
   By default, the unit is set as months. You can change it to years to look further in the future.

   > [!TIP]
   > To accurately predict CLV for the time period you set, you need a comparable period of historical data. For example, if you want to predict for the next 12 months, it is recommended that you have at least 18 – 24 months of historical data.

1. Specify what **Active customers** mean for your business. Set the time frame in which a customer must have had at least one transaction to be considered active. The model will only predict CLV for active customers. 
   - **Let model calculate purchase interval (recommended)**: The model analyzes your data and determines a time period based on historical purchases.
   - **Set interval manually**: If you have a specific business definition of an active customer, choose this option and set the time period accordingly.

1. Define percentile of **High-value customer** to enable the model to provide results that fit your business definition.
    - **Model calculation (recommended)**: The model analyzes your data and determines what a high value customer might be for your business based on your customers’ transaction history. The model uses a heuristic rule (inspired by the 80/20 rule or pareto principle) to find the proportion of high-value customers. The percentage of customers that contributed to 80% cumulative revenue for your business in the historical period are considered high-value customers. Typically, less than 30-40% customers contribute to 80% cumulative revenue. However, this number might vary depending on your business and industry.    
    - **Percent of top active customers**: Define high-value customers for your business as a percentile of top active paying customers. For example, you can use this option to define high-value customers as top 20% of future paying customers.

    If your business defines high value customers in a different way, [let us know as we would love to hear](https://go.microsoft.com/fwlink/?linkid=2074172).

1. Select **Next** to proceed to the next step.

### Add required data

1. In the **Required data** step, select **Add data** for **Customer transaction history** and choose the entity that provides the transaction history information as described in the [prerequisites](#prerequisites).

1. Map the semantic fields to attributes within your purchase history entity and select **Next**.

   :::image type="content" source="media/clv-add-customer-data-mapping.png" alt-text="Image of the configuration step to map data attributes for the required data.":::
 
1. If the fields below aren't populated, configure the relationship from your purchase history entity to the *Customer* entity and select **Save**.
    1. Select the transaction history entity.
    1. Select the field that identifies a customer in the purchase history entity. It needs to relate to the primary customer ID of your Customer entity.
    1. Select the entity that matches your primary customer entity.
    1. Enter a name that describes the relationship.

      :::image type="content" source="media/clv-add-customer-data-relationship.png" alt-text="Image of configuration step to define the relationship with the customer entity.":::

1. Select **Next**.

### Add optional data

Data reflecting key customer interactions (like web, customer service, and event logs) adds context to transaction records. More patterns found in your customer activity data can improve the accuracy of the predictions. 

1. In the **Additional data (optional)** step, select **Add data**. Choose the customer activity entity that provides the customer activity information as described in the [prerequisites](#prerequisites).

1. Map the semantic fields to attributes within your customer activity entity and select **Next**.

   :::image type="content" source="media/clv-additional-data-mapping.png" alt-text="Image of the configuration step to map fields for additional data.":::

1. Select an activity type that matches the type of customer activity you're adding. Choose from existing activity types or add a new activity type.

1. Configure the relationship from your customer activity entity to the *Customer* entity.
    
    1. Select the field that identifies the customer in the customer activity table. It can be directly related to the primary customer ID of your *Customer* entity.
    1. Select the *Customer* entity that matches your primary *Customer* entity.
    1. Enter a name that describes the relationship.

   :::image type="content" source="media/clv-additional-data.png" alt-text="Image of the step in the configuration flow to add additional data and configure the activity with filled in examples.":::

1. Select **Save**.    
    Add more data if there are other customer activities you want to include.

1. Select **Next**.

### Set update schedule

1. In the **Data update schedule** step, choose the frequency to retrain your model based on the latest data. This setting is important to update the accuracy of predictions as new data is ingested in audience insights. Most businesses can retrain once per month and get a good accuracy for their prediction.

1. Select **Next**.


### Review and run the model configuration

1. In the **Review your model details** step, validate the configuration of the prediction. You can go back to any part of the prediction configuration by selecting **Edit** under the shown value. You can also select a configuration step from the progress indicator.

1. If all values are configured correctly, select **Save and run** to start running the model. On the **My predictions** tab, you can see the status of the prediction process. The process may take several hours to complete depending on the amount of data used in the prediction.

## Review prediction status and results

### Review prediction status

1.	Go to **Intelligence** > **Predictions** and select the **My predictions** tab.
2.	Select the prediction you want to review.

- **Prediction name**: Name of the prediction provided when creating it.
- **Prediction type**: Type of model used for the prediction
- **Output entity**: Name of the entity to store the output of the prediction. Go to **Data** > **Entities** to find the entity with this name.
- **Predicted field**: This field is populated only for some types of predictions, and isn't used in customer lifetime value prediction.
- **Status**: Status of the prediction run.
    - **Queued**: Prediction is waiting for other processes to complete.
    - **Refreshing**: Prediction is currently running to create results that will flow into the output entity.
    - **Failed**: Prediction run has failed. [Review the logs](#troubleshoot-a-failed-prediction) for more details.
    - **Succeeded**: Prediction has succeeded. Select **View** under the vertical ellipses to review the prediction results.
- **Edited**: The date the configuration for the prediction was changed.
- **Last refreshed**: The date the prediction refreshed results in the output entity.


### Review prediction results

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.

1. Select the prediction you want to review results for.

There are three primary sections of data within the results page.

- **Training model performance**: A, B, or C are possible grades. This grade indicates the performance of the prediction and can help you make the decision to use the results stored in the output entity. Select **Learn about this score** to better understand the underlying model performance metrics and how the final model performance grade was derived.
  
  :::image type="content" source="media/clv-model-score.png" alt-text="Image of the model score information box with the grade A.":::

  Using the definition of high value customers provided while configuring the prediction, the system assess how the AI model performed in predicting the high value customers as compared to a baseline model.    

  Grades are determined based on the following rules:
  - A when the model accurately predicted at least 5% more high-value customers as compared to the baseline model.
  - B when the model accurately predicted between 0-5% more high-value customers as compared to the baseline model.
  - C when the model accurately predicted fewer high-value customers as compared to the baseline model.

  The **Model rating** pane shows further details about the AI model performance and the baseline model. The baseline model uses a non-AI based approach to calculate customer lifetime value based primarily on historical purchases made by customers.     
  The standard formula used to calculate CLV by the baseline model:    

  *CLV for each customer = Average monthly purchase made by the customer in the active customer window * Number of months in the CLV prediction period * Overall retention rate of all customers*

  The AI model is compared to the baseline model based on two model performance metrics.
  
  - **Success rate in predicting high-value customers**

    See the difference in predicting high-value customers using the AI model compared to the baseline model. For example, 84% success rate means that out of all the high-value customers in the training data, the AI model was able to accurately capture 84%. We then compare this success rate with the success rate of the baseline model to report the relative change. This value is used to assign a grade to the model.

  - **Error metrics**
    
    Another metric lets you review the overall performance of the model in terms of error in predicting future values. We use the overall Root Mean Squared Error (RMSE) metric to assess this error. RMSE is a standard way to measure the error of a model in predicting quantitative data. The AI model’s RMSE is compared to the RMSE of the baseline model and the relative difference is reported.

  The AI model prioritizes the accurate ranking of customers according to the value they bring to your business. So only the success rate of predicting high-value customers is used to derive the final model grade. The RMSE metric is sensitive to outliers. In scenarios where you have a small percentage of customers with extraordinarily high purchase values, the overall RMSE metric might not give the full picture of the model performance.   

- **Value of customers by percentile**: Using your definition of high-value customers, customers are grouped into low-value and high-value, based on their CLV predictions, and shown in a chart. By hovering over the bars in the histogram, you can see the number of customers in each group and the average CLV of that group. This data can help if you want to [create segments of customers](segments.md) based on their CLV predictions.

- **Most influential factors**: Various factors are considered when creating your CLV prediction based on the input data provided to the AI model. Each of the factors has their importance calculated for the aggregated predictions a model creates. You can use these factors to help validate your prediction results. These factors also provide more insight about the most influential factors that contributed towards predicting CLV across all your customers.

## Refresh a prediction

Predictions automatically refresh on the same [schedule your data refreshes](system.md#schedule-tab) as configured in settings. You can refresh them manually too.

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.
2. Select the vertical ellipses next to the prediction you want to refresh.
3. Select **Refresh**.

## Delete a prediction

Deleting a prediction also removes its output entity.

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.
2. Select the vertical ellipses next to the prediction you want to delete.
3. Select **Delete**.

## Troubleshoot a failed prediction

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.
2. Select the vertical ellipses next to the prediction you want to view error logs for.
3. Select **Logs**.
4. Review all the errors. There are several types of errors that can occur, and they describe what condition caused the error. For example, an error that there's not enough data to accurately predict is typically resolved by loading more data into audience insights.


[!INCLUDE[footer-include](../includes/footer-banner.md)]