---
title: Funnel reports
description: How to use funnel reports to understand how audience makes decisions.
ms.reviewer: mhart
ms.author: kamacdon
author: kamacdon
ms.date: 04/14/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# Create and manage funnel reports

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A funnel report collects information about the steps that occur during a customer journey through your website. It helps you understand how an audience progresses through a process and identifies drop-off points. For example, you can use a funnel report to identify paths and touchpoints your customers are taking before they make a purchase. A funnel report provides data to inform decisions and identify areas for optimization and process improvements.

## Create a funnel report

To create the funnel report, specify the steps that you want to include and the activity for each step. An activity is an [event](glossary.md) that represents user behavior. The funnel report displays the number of users who completed each defined step. 

1. Go to **Funnels** and select **+New funnel** to start a funnel report.

1. In the **Funnel Editor**, under **Steps** select **+Add step.** 

1. Enter a name in  **Step title**.

   :::image type="content" source="media/new-funnel-report.png" alt-text="New funnel report":::

1. Select an **Activity**. An activity records when a user views a page (**View** activity) or interacts with content (**Action** activity).

1. Use **Step criteria** to specify the activity's dimension. Dimensions are attributes that can describe, filter, or group data.

1. Select **Add step** until you complete all the steps you want in the report.

1. Select **Save**, name the report, and **Save** again. 

### Example: Fourth Coffee company funnel report

The following scenario demonstrates one way of using a funnel report. An analyst with the Fourth Coffee company wants to understand the impact of a recent promotion on subscription rates. She creates a funnel report to identify customer activity. It starts when customers arrive on the company home page until they use the subscription promotion code. The analyst creates a funnel report with the following steps:

Step 1: Customers who land on the homepage   
Step 2: Customers who make a purchase   
Step 3: Customers who use the promotion code to get a discount on a subscription   
Step 4: Subscription sign-up   

:::image type="content" source="media/funnel-report-example.png" alt-text="funnel report example":::
  
This funnel lets you see the number of users who used the promotion code after a one-time purchase to sign up for the subscription program.

## Manage funnel reports

You can review funnel reports to analyze data, track performance, and gather insights.

> [!NOTE]
> - Engagement insights funnel reports currently support scenarios in which all users in the funnel are anonymous or all users are authenticated. 
> - Historical data in funnel reports is available for the last 30 days.

### View funnel reports

1. Go to **Funnels** to open the **Funnels library**.
1. Select a name to open the report.    

### See the data collected for a report   

To see information about a phase

- Point to a step in the report.

:::image type="content" source="media/funnel-step-data.png" alt-text="funnel data":::

### Change the date range for the funnel report

1. Go to **Funnels** to open the **Funnels library**.

1. Select a name to open the report.

1. Open the **time range** and select a new time period from the list or **Fixed date range** to specify a date range.

## Edit or delete funnel reports

You can change the name of a funnel report, delete it, or modify the steps in the report.

### Rename or delete a funnel report

1. Go to **Funnels** to open the **Funnels library**. 

1. Select **More** next to the report you want to change and choose **Edit name** or **Delete**.

### Edit a funnel step  

1. Go to **Funnels** to open the **Funnels library**. 

1. Select a name to open the report.

1. Select the step that you want to edit.

1. Select **Edit**.

1. In the **Funnel Editor**, update the information you want to change.  

1. Select **Save**.

### Reorder a funnel step

1. Go to **Funnels** to open the **Funnels library**. 

1. Select a name to open the report.

1. Select the step that you want to reorder.

1. Select **Move**, and then **Up**, **Down**, **To top**, or **To bottom**, to move the step.

### Delete a funnel step

1. Go to **Funnels** to open the **Funnels library**. 

1. Select a name to open the report.

1. Select the step that you want to remove and select **Delete**.
