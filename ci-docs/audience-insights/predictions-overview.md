---
title: Overview about supported prediction scenarios
description: "Prediction scenarios and options covered by the Dynamics 365 Customer Insights application."
ms.date: 09/06/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: get-started
author: zacookmsft
ms.author: zacook
manager: shellyha
ms.custom: intro-internal
---

# Predictions overview

Dynamics 365 Customer Insights comes with a variety of options that leverage AI and machine learning to predict data. 

## Out-of-box models

The easiest way to start with predicting data are predefined models, often referred to as out-of-box models. They only require certain data and structure to generate insights quickly. Currently, the following models are available: 

# [Individual consumers (B2C)](#tab/b2c)

- [Customer lifetime value](predict-customer-lifetime-value.md): Predicts the potential revenue of a customer throughout the entire interaction with a business.
- [Product recommendation](predict-product-recommendation.md): Suggests sets of predictive product recommendations based on purchase behavior and customers with similar purchase patterns.
- [Subscription churn](predict-subscription-churn.md): Predicts whether a customer is at risk for no longer using your company’s subscription products or services.
- [Transactional churn](predict-transactional-churn.md): Predict if a customer will no longer purchase your products or services in a certain time frame.

# [Business accounts (B-to-B)](#tab/b2b)

- [Transactional churn](predict-transactional-churn.md): Predict if a customer will no longer purchase your products or services in a certain time frame.

---


## Azure Machine Learning integration

If an organization already uses machine learning scenarios based on Azure Machine Learning experiments, the custom models feature in Customer Insights helps to connect the dots. Create workflows that help you choose the data you want to generate insights from and map the results to your unified customer profiles. For more information, see [Custom machine learning models](custom-models.md).

## AI Builder prediction

Sometimes, data sets are incomplete and some values are missing. Customer Insights can help to predict missing values for the Customer entity and segments. For more information, see [Complete your partial data with predictions](predictions.md).
