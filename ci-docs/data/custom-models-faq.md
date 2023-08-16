---
title: "Custom machine learning FAQ"
description: "Frequently asked questions when using custom models in Dynamics 365 Customer Insights."
ms.date: 09/01/2023
ms.reviewer: v-wendysmith
ms.topic: faq
author: radsay01
ms.author: rsayyaparaju
ms.custom: bap-template
---

# Custom machine learning FAQ

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

## Why can't I see my pipeline when setting up a custom model workflow?

This issue is frequently caused by a configuration issue in the pipeline. Ensure the [input parameter is configured](azure-machine-learning-experiments.md#dataset-configuration) and the [output datastore and path parameters](azure-machine-learning-experiments.md#import-pipeline-data) are also configured.

## What does the error "Couldn't save intelligence workflow" mean?

This error message typically occurs because the user doesn't have Owner, Admin, or Contributor privileges on the workspace. The user initially needs a higher level of permissions to enable Dynamics 365 Customer Insights - Data to process the workflow as a service.

## Can I use a private endpoint with my custom model from Azure Machine Learning?
  
Customer Insights - Data does not currently support private endpoints with custom models out of the box. Please contact support for details.

[!INCLUDE [footer-include](includes/footer-banner.md)]
