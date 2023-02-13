---
title: Create a segment based on a prediction model
description: "Create segments based on the output entity of a prediction model."
ms.date: 09/19/2022
ms.reviewer: mhart

ms.topic: how-to
author: zacookmsft
ms.author: zacook
---

# Create a segment based on a prediction model (preview)

The results of predictions sometimes only apply to a subset of your customers. Increase the personalization of recommendations by creating segments from results of prediction models. For example, you may want to give specific recommendations to customers that prefer a certain type of service.

## Prerequisites

- At least [Contributor permissions](permissions.md) in Customer Insights.

- A product recommendation, transactional churn, subscription churn, or customer lifetime value model configured in Customer Insights. Review the requirements to set up the different models:

  - [Product recommendation model](predict-product-recommendation.md)
  - [Subscription churn model](predict-subscription-churn.md)
  - [Transactional churn model](predict-transactional-churn.md)
  - [Customer lifetime value model](predict-customer-lifetime-value.md)

## Create a customer segment based on predictions

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.

1. Select the model you want to review and select **View**.

1. On the results page, select **Create segment**. For more information about the results page, review the article about the model.

   :::image type="content" source="media/prediction-create-segment.png" alt-text="Screenshot of the prediction results page with highlight on the Create segment action.":::

1. Create a new segment using attributes from the output entity of the selected model. For more information, see [Create and manage segments](segments.md).

> [!TIP]
> You can also create a segment for a prediction model from the **Segments** page by selecting **New** and choosing **Create from** > **Intelligence**. For more information, see [Create a new segment with quick segments](segment-quick.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
