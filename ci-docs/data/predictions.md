---
title: Create and manage predictions
description: Learn how to create and manage predictions in Dynamics 365 Customer Insights - Data."
ms.date: 12/08/2025
ms.update-cycle: 180-days
ms.reviewer: alfergus
ms.topic: how-to
author: radsay01
ms.author: rsayyaparaju 
ms.collection: bap-ai-copilot 
ms.custom:
  - bap-template
  - sfi-image-nochange
---

# Create and manage predictions

Dynamics 365 Customer Insights - Data comes with various options that use AI and machine learning to predict data.

Predictions offer capabilities to create better customer experiences, improve business capabilities, and revenue streams. We strongly recommend you balance the value of your prediction against the effect it has and biases that might be introduced in an ethical manner. Learn more about how Microsoft is [addressing Responsible AI](https://www.microsoft.com/ai/responsible-ai?activetab=pivot1%3aprimaryr6).

## Generate insights using out-of-box prediction models

The easiest way to start with predicting data are predefined models, often referred to as out-of-box models. They only require certain data and structure to generate insights quickly.

The following models are available:

- [Customer lifetime value](predict-customer-lifetime-value.md): Predicts the potential revenue of a customer throughout the entire interaction with a business.
- [Product recommendation](predict-product-recommendation.md): Suggests sets of predictive product recommendations based on purchase behavior and customers with similar purchase patterns.
- [Subscription churn](predict-subscription-churn.md): Predicts whether a customer is at risk for no longer using your company’s subscription products or services.
- [Transactional churn](predict-transactional-churn.md): Predicts if an individual customer might no longer purchase your products or services in a certain time frame.
- [Sentiment analysis](sentiment-analysis.md): Analyzes sentiment of customer feedback and identifies business aspects that are frequently mentioned.

To understand the readiness of your data to produce insights, see [Data prep report overview](data-prep-overview.md).

> [!TIP]
> We recommend that you regularly refresh out-of-the-box models with updated data to ensure they accurately inform your business use case. Data is refreshed ad-hoc when the system ingests new or updated data sources. However, models will only rescore in this case and continue to use the existing training data.
>
> Configure an **Update schedule** by setting the model retraining schedule during configuration. The model will retrain and rescore on this schedule, which you can change at any time.

## Manage existing predictions

Go to the **Insights** > **Predictions** page. On the **My predictions** tab, view the predictions you created, their prediction type, output table name, status, the last time the prediction was edited, and the last time the data was refreshed. You can sort the list of predictions by any column.

To view available actions, select a prediction.

:::image type="content" source="media/predictions.png" alt-text="My predictions page.":::

- **Edit** the prediction to change its properties.
- [**Refresh**](#refresh-a-prediction) the prediction to include the latest data.
- **View** the prediction details.
- [**Input data usability report**](#view-the-input-data-usability-report) to view errors, warnings, and recommendations.
- **Delete** the prediction.

### Refresh a prediction

Predictions can be refreshed on an automatic schedule or refreshed manually on demand. To manually refresh all predictions, select **Refresh all**. To manually refresh a prediction, select it and select **Refresh**. To [schedule an automatic refresh](schedule-refresh.md), go to **Settings** > **System** > **Schedule**.

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

### View the input data usability report

The input data usability report provides a consolidated view of the errors and warnings that your out-of-box predictions might be generating. It also gives recommendations on how to improve the model performance.

The report is available after a model completed its training process. Each model gets a separate report, regardless of whether it completed training successfully or not.

On the **My predictions** tab, select the prediction and choose **Input data usability report**. Or from the prediction details view, select **Input data usability report**.

:::image type="content" source="media/input-data-usability-report.png" alt-text="Example of an input data usability report showing a table with errors, warnings, and recommendations.":::

The report includes:

- **Name:** Descriptive name of the error, warning, or recommendation.
- **Step:** Model phase, train or score, and the information refers to.
- **State:** Severity of the information (error, warning, recommendation).
- **Column name:** Column in a table that needs to be modified to improve the model performance.
- **Table:** Name of the table that needs to be modified to improve the model performance.
- **Details:** Details about the error, warning, or recommendation.

[!INCLUDE [footer-include](includes/footer-banner.md)]
