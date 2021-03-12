---
title: Segments based on prediction output
description: "Create a segments based on the output entity of a prediction model."
ms.date: 03/12/2021
ms.reviewer: zacook
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Create a segment based on a prediction model (preview)

The results of product recommendations, predicted customer churn, or predicted customer lifetime value can sometimes only apply to a subset of your customers. For example, identify customers that prefer a certain type of service and deliver specific recommendations to them. By creating segments based on model results, you can increase the personalization in the recommendations to your customers.

## Prerequisites

- At least [Contributor permissions](permissions.md) in Customer Insights.

- A product recommendation, transactional churn, subscription churn, or customer lifetime value model configured in Customer Insights. Review the requirements to set up the different models:

  - [Product recommendation model](predict-product-recommendation.md)
  - [Subscription churn model](predict-subscription-churn.md)
  - [Transactional churn model](predict-transactional-churn.md)
  - [Customer lifetime value model](predict-customer-lifetime-value.md)

## Create a customer segment based on predictions

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.

1. Select the vertical ellipses next to the model you want to review and select **View**.

1. On the results page, select **Create a customer segment**. For more information about the results page, review the article about the model.

1. Create a new segment based on the output entity of the selected model. For more information, see [Create and manage segments](segments.md).