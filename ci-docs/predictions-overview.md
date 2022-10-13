---
title: Predictions overview
description: "Prediction scenarios and options covered by the Dynamics 365 Customer Insights application."
ms.date: 09/29/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: overview
author: zacookmsft
ms.author: zacook
manager: shellyha

---

# Predictions overview

Dynamics 365 Customer Insights comes with a variety of options that leverage AI and machine learning to predict data.

## Out-of-box models

The easiest way to start with predicting data are predefined models, often referred to as out-of-box models. They only require certain data and structure to generate insights quickly. The following models are available:

# [Individual consumers (B-to-C)](#tab/b2c)

- [Customer lifetime value](predict-customer-lifetime-value.md): Predicts the potential revenue of a customer throughout the entire interaction with a business.
- [Product recommendation](predict-product-recommendation.md): Suggests sets of predictive product recommendations based on purchase behavior and customers with similar purchase patterns.
- [Subscription churn](predict-subscription-churn.md): Predicts whether a customer is at risk for no longer using your company’s subscription products or services.
- [Transactional churn](predict-transactional-churn.md): Predicts if an individual customer will no longer purchase your products or services in a certain time frame.
- [Sentiment analysis](sentiment-analysis.md): Analyzes sentiment of customer feedback and identifies business aspects that are frequently mentioned.

# [Business accounts (B-to-B)](#tab/b2b)

- [Transactional churn](predict-transactional-churn.md): Predicts if a customer account will no longer purchase your products or services in a certain time frame.

---

> [!TIP]
> We recommend that you regularly refresh out-of-the box models with updated data to ensure they accurately inform your business use case. Data is refreshed ad-hoc when the system ingests new or updated data sources. However, models will only rescore in this case and continue to use the existing training data.
>
> Configure an **Update schedule** by setting the model retraining schedule during configuration. The model will retrain and rescore on this schedule, which you can change at any time.

## Azure Machine Learning integration

If an organization already uses machine learning scenarios based on Azure Machine Learning experiments, the custom models feature in Customer Insights helps to connect the dots. Create workflows that help you choose the data you want to generate insights from and map the results to your unified customer profiles. For more information, see [Custom machine learning models](custom-models.md).

## Manage existing predictions

Go to the **Insights** > **Predictions** page. On the **My predictions** tab, view the predictions you created, their prediction type, output entity name, status, the last time the prediction was edited, and the last time the data was refreshed. You can sort the list of predictions by any column.

Select a prediction to view available actions.

:::image type="content" source="media/predictions.png" alt-text="My predictions page.":::

- **Edit** the prediction to change its properties.
- [**Refresh**](#refresh-a-prediction) the prediction to include the latest data.
- **View** the prediction details.
- [**Input data usability report**](#view-the-input-data-usability-report) to view errors, warnings, and recommendations.
- **Delete** the prediction.

### Refresh a prediction

Predictions can be refreshed on an automatic schedule or refreshed manually on demand. To manually refresh all predictions, select **Refresh all**. To manually refresh a prediction, select it and select **Refresh**. To [schedule an automatic refresh](schedule-refresh.md), go to **Admin** > **System** > **Schedule**.

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

### View the input data usability report

The input data usability report provides a consolidated view of the errors and warnings that your out-of-box predictions may be generating. It also gives recommendations on how to improve the model performance.

The report is available after a model has completed its training process. It's created for each model separately, regardless of whether it completed training successfully or not.

On the **My predictions** tab, select the prediction and choose **Input data usability report**. Or from the prediction details view, select **Input data usability report**.

:::image type="content" source="media/input-data-usability-report.png" alt-text="Example of an input data usability report showing a table with errors, warnings, and recommendations.":::

The report includes:

- **Name:** Descriptive name of the error, warning, or recommendation.
- **Step:** Model phase, train or score, the information refers to.
- **State:** Severity of the information (error, warning, recommendation).
- **Column name:** Column in an entity that needs to be modified to improve the model performance.
- **Entity name:** Name of the entity that needs to be modified to improve the model performance.
- **Details:** Details about the error, warning, or recommendation.

[!INCLUDE [footer-include](includes/footer-banner.md)]
