---
title: "Custom machine learning FAQ"
description: "Frequently asked questions when using custom models in Dynamics 365 Customer Insights."
ms.date: 05/30/2023
ms.reviewer: v-wendysmith
ms.topic: faq
author: radsay01
ms.author: rsayyaparaju
ms.custom: bap-template
searchScope: 
  - ci-custom-models
  - customerInsights
---

# Custom machine learning FAQ

## Why can't I see my pipeline when setting up a custom model workflow?

This issue is frequently caused by a configuration issue in the pipeline. Ensure the [input parameter is configured](azure-machine-learning-experiments.md#dataset-configuration) and the [output datastore and path parameters](azure-machine-learning-experiments.md#import-pipeline-data-into-customer-insights) are also configured.

## What does the error "Couldn't save intelligence workflow" mean?

Users usually see this error message if they don't have Owner or User Access Administrator privileges on the workspace. The user needs a higher level of permissions to enable Customer Insights to process the workflow as a service rather than using the user credentials for subsequent runs of the workflow.

## Can I use a private endpoint with my custom model from Azure Machine Learning?
  
Customer Insights does not currently support private endpoints with custom models out of the box. Please contact support for details.

[!INCLUDE [footer-include](includes/footer-banner.md)]
