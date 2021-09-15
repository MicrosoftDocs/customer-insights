---
title: Funnel reports
description: How to use funnel reports to understand how audience makes decisions.
ms.reviewer: mhart
ms.author: kamacdon
author: kamacdon
ms.date: 06/23/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# Create and manage funnel reports

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A funnel report collects information about the steps that occur during a customer journey through your website or mobile app. It helps you understand how an audience progresses through a process and identifies drop-off points. For example, you can use a funnel report to identify paths your customers take before they make a purchase. A funnel report provides data to inform decisions and identify areas for optimization and process improvements.

## Create a funnel report

To create the funnel report, specify the steps that you want to include and the activity for each step. An activity is an [event](glossary.md) that represents user behavior. The funnel report displays the number of users who completed each defined step. 

1. Go to **Funnels** and select **+New funnel** to start a funnel report.

1. In the **Funnel Editor**, under **Steps** select **+Add step.** 

1. Enter a name in  **Step title**.

   :::image type="content" source="media/new-funnel-report.png" alt-text="New funnel report.":::

1. Select an **Activity**. An activity records when a user views a page (**View** activity) or interacts with content (**Action** activity).

1. Use **Step criteria** to specify the activity's dimension. [Dimensions](dimensions.md) are attributes that can describe, filter, or group data.

1. Optionally, you can configure multi-condition funnel steps. Select **Add condition** to specify more dimensions in a step. Additional criteria must use the same activity type. You can choose if multiple conditions are connected with an AND or an OR operator.

   :::image type="content" source="media/funnel-add-condition.png" alt-text="Funnel editor showing the step configuration with multi-condition steps.":::

1. Select **Add step** until you complete all the steps you want in the report.

1. Select **Save**, name the report, and **Save** again. 

### Example: Fourth Coffee company funnel report

The following scenario demonstrates one way of using a funnel report. An analyst with the Fourth Coffee company wants to understand the influence of a recent promotion on subscription rates. The analyst creates a funnel report to identify customer activity. It starts when customers arrive on the company home page until they use the subscription promotion code. The analyst creates a funnel report with the following steps:

Step 1: Customers who land on the homepage   
Step 2: Customers who make a purchase   
Step 3: Customers who use the promotion code to get a discount on a subscription   
Step 4: Subscription sign-up   

:::image type="content" source="media/funnel-report-example.png" alt-text="funnel report example.":::
  
This funnel lets you see the number of users who used the promotion code after a one-time purchase to sign up for the subscription program.

### Configure advanced settings 

Funnel reports let you define a limit on the time it takes to complete a funnel. For example, you can set the time to complete the funnel to four days. This setting will only count successful subscription sign-ups that occurred within four days of a user visiting the homepage.

1. Go to **Funnels** to open the **Funnels library**.

1. Select a name to open the report. 

1. In the **Funnel Editor** pane, select **Advanced settings**. 

1. Set Limit funnel completion time to **On**.

   :::image type="content" source="media/funnel-limit-time.png" alt-text="Funnel editor showing advanced setting and options to limit time to complete a funnel.":::

1. Choose the time the funnel must have been completed in the **Set limit to** dropdown list.

1. Select **Save** to apply your changes.


## Cross-channel funnel reports 

Engagement insights can also to collect behavioral customer data on your mobile app. Once you have instrumented your mobile app with the engagement insights [Android SDK](get-started-android.md) or [iOS SDK](get-started-ios.md), you can create cross-channel funnel reports. 

### Create a cross-channel funnel report 

1. Follow the steps to [create a funnel report](#create-a-funnel-report).    

1. To track how your customers are interacting with your brand across both your website and mobile app, or multiple websites, use the workspace switcher to create funnel steps with data from other workspaces. In the **Funnel Editor**, under **Steps** select which workspace the data for your funnel step should come from.

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

:::image type="content" source="media/funnel-step-data.png" alt-text="funnel data.":::

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

### Funnel Insights 

Engagement insights now offers Funnel Insights for customers. Use Funnel Insights to gain deeper insight into customer behavior about the steps in your funnel report. 
When you create and save a new funnel report, funnel insights are automatically generated for your report. You will be shown insights from the following categories at both the step--level and overall funnel level: 

   1. Conversion rate 
   2. Transition time 
   3. Completion time 

Use these insights to dig deeper into customer behavior and better understand drop-off points and conversions for your funnel report. 
Insights are recalculated every 24 hours, or when you SAVE your funnel report. 

**In order to view insights for your funnel, you must SAVE your report** 

