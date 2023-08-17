---
title: Predict transaction churn (contains video)
description: "Predict whether a customer is at risk for no longer purchasing your products or services."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: zacookmsft
ms.author: zacook
---

# Predict transaction churn

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Transactional churn prediction helps predict if a customer will no longer purchase your products or services in a given time window.

You must have business knowledge to understand what churn means for your business. We support time-based churn definitions, meaning a customer is considered to have churned after a period of no purchases.

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWN6Eg]

## Prerequisites

[!INCLUDE [prediction-transaction-prereqs](includes/predict-transaction-prereqs.md)]

## Create a transaction churn prediction

[!INCLUDE [prediction-transaction-create](includes/predict-transaction-create.md)]

### Add additional data (optional)

1. Select **Add data** for **Customer activities**.

1. Select the semantic activity type that contains the data you would like to use. If the activity has not been set up, select **here** and create it.

1. Under **Activities**, if the activity attributes were semantically mapped when the activity was created, choose the specific attributes or table you'd like the calculation to focus on. If semantic mapping did not occur, select **Edit** and map your data.

1. Select **Next** and review the attributes required for this model.

1. Select **Save**.

1. Select **Next**

[!INCLUDE [predict-transaction-create-last-steps](includes/predict-transaction-create2.md)]

[!INCLUDE [progress-details](includes/progress-details-pane.md)]

## View prediction results

1. Go to **Insights** > **Predictions**.

1. In the **My predictions** tab, select the prediction you want to view.

There are three primary sections of data within the results page:

[!INCLUDE [predict-transaction-results](includes/predict-transaction-results.md)]

> [!NOTE]
 > In the output table for this model, *ChurnScore* shows the predicted probability of churn and *IsChurn* is a binary label based on *ChurnScore* with 0.5 threshold. If this default threshold doesn't work for your scenario, [create a new segment](../segments.md) with your preferred threshold. Not all customers are necessarily active customers. Some of them may not have had any activity for a long time and are considered as churned already, based on you churn definition. Predicting the churn risk for customers who already churned isn't useful because they are not the audience of interest.
>
> To view the churn score, go to **Data** > **Tables** and view the data tab for the output table you defined for this model.

[!INCLUDE [footer-include](includes/footer-banner.md)]
