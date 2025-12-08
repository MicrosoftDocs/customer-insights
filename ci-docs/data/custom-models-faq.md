---
title: Custom models FAQ
description: Learn answers to frequently asked questions about using custom machine learning models in Dynamics 365 Customer Insights - Data.
ms.date: 12/08/2025
ms.update-cycle: 180-days
ms.topic: faq
author: radsay01
ms.author: rsayyaparaju
ms.reviewer: v-wendysmith
ms.custom: bap-template
ms.collection: bap-ai-copilot 
---

# Custom models FAQ

## Why can't I see my pipeline when I'm setting up a custom model workflow?

If you can't see a pipeline when you set up a workflow with a custom machine learning model, the cause is often an issue with the pipeline's configuration. Make sure the [input parameter](azure-machine-learning-experiments.md#dataset-configuration) and the [output datastore and path parameters](azure-machine-learning-experiments.md) are configured.

## What does the error "Couldn't save intelligence workflow" mean?

This error message usually means the user doesn't have Owner, Admin, or Contributor privileges in the workspace, which are required for Customer Insights - Data to process the workflow as a service.

## Can I use a private endpoint with my custom model from Azure Machine Learning?
  
Customer Insights - Data doesn't allow the use of private endpoints with custom models out of the box.

[!INCLUDE [footer-include](includes/footer-banner.md)]
