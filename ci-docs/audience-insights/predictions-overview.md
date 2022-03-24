---
title: Overview about supported prediction scenarios
description: "Prediction scenarios and options covered by the Dynamics 365 Customer Insights application."
ms.date: 03/24/2022
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

The easiest way to start with predicting data are predefined models, often referred to as out-of-box models. They only require certain data and structure to generate insights quickly. Currently, the following models are available: 

# [Individual consumers (B-to-C)](#tab/b2c)

- [Customer lifetime value](predict-customer-lifetime-value.md): Predicts the potential revenue of a customer throughout the entire interaction with a business.
- [Product recommendation](predict-product-recommendation.md): Suggests sets of predictive product recommendations based on purchase behavior and customers with similar purchase patterns.
- [Subscription churn](predict-subscription-churn.md): Predicts whether a customer is at risk for no longer using your company’s subscription products or services.
- [Transactional churn](predict-transactional-churn.md): Predict if a customer will no longer purchase your products or services in a certain time frame.
- [Sentiment analysis](sentiment-analysis.md): Analyze sentiment of customer feedback and identify business aspects that are frequently mentioned.

# [Business accounts (B-to-B)](#tab/b2b)

- [Transactional churn](predict-transactional-churn.md): Predict if a customer will no longer purchase your products or services in a certain time frame.

---

> [!TIP]
> We recommend that you regularly refresh the our out-of-the box models with your data to ensure they accurately inform your business use case. Data is refreshed ad-hoc when the system ingests new or updated data sources. However, the model will only rescore in this case and continue to use the existing training data.
> 
> You can configure an **Update schedule** by setting the model retraining schedule in the configuration experience. The model will retrain and rescore on this schedule, which you can change at any time.


## Azure Machine Learning integration

If an organization already uses machine learning scenarios based on Azure Machine Learning experiments, the custom models feature in Customer Insights helps to connect the dots. Create workflows that help you choose the data you want to generate insights from and map the results to your unified customer profiles. For more information, see [Custom machine learning models](custom-models.md).

## AI Builder prediction

Sometimes, data sets are incomplete and some values are missing. Customer Insights can help to predict missing values for the Customer entity and segments. For more information, see [Complete your partial data with predictions](predictions.md).
