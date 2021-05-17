---
title: Shared tasks for prediction scenarios
description: "Learn how to manage, troubleshoot, and refine predictions."
ms.date: 05/17/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: diegogranados
ms.author: digranad
manager: shellyha
---

# Manage predictions

This article discusses some tasks that most prediction scenarios share.

## Input data usability report

The input data usability report provides a consolidated view of the errors and warnings that your out-of-box predictions may be generating. It also gives recommendations how to improve the model performance.

The report is available after a model has completed its training process. It's created for each model separately, regardless if it completed successfully or not.

> [!NOTE]
> Currently, this feature only works for the CLV model.

### View the input data usability report

After an out-of-box model has completed its training step, view the report:
- Select the ellipses next to the model name and choose **Input data usability report**.
- Select the status of a model select **See Input data usability report** in the side pane.
- Selecting one of the models in the list and select **Input data usability report** in the command bar.
- Open the model results page and select **Input data usability report** in the command bar.

### Information in the input data usability report

The following columns in the report contain helpful information to improve the data for the model.

:::image type="content" source="media/input-data-usability-report.png" alt-text="Example of an input data usability report showing a table with errors, warnings, and recommendations.":::

- Name: Descriptive name of the error, warning, or recommendation.
- Step: Model phase, train or score, the information refers to.
- State: Severity of the information (error, warning, recommendation).
- Column name: Column in an entity that needs to be modified to improve the model performance.
- Entity name: Name of the entity that needs to be modified to improve the model performance.
- Details: Details about the error, warning, or recommendation.

## Troubleshoot a failed prediction

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.

1. Select the vertical ellipses next to the prediction you want to view error logs for.

1. Select **Logs**.

1. Review all the errors. There are several types of errors that can occur, and they describe what condition caused the error. For example, an error that there's not enough data to accurately predict is typically resolved by loading additional data into Customer Insights.

## Refresh a prediction

Predictions will automatically refresh on the same [schedule your data refreshes](system.md#schedule-tab) as configured in settings. You can refresh them manually too.

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.

1. Select the vertical ellipses next to the prediction you want to refresh.

1. Select **Refresh**.

## Delete a prediction

Deleting a prediction also removes its output entity.

1. Go to **Intelligence** > **Predictions** and select the **My predictions** tab.

1. Select the vertical ellipses next to the prediction you want to delete.

1. Select **Delete**.