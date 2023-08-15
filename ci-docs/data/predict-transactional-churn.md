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

[!INCLUDE [predict-transaction-churn-note](includes/predict-transaction-churn-note.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
