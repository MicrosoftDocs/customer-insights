---
title: Funnel reports (public preview)
description: How to use funnel reports to understand how audience makes decisions.
ms.reviewer: kamacdon
ms.author: v-salash
author: pickwick129
ms.date: 04/08/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# Create and manage funnel reports (public preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A funnel report collects information about the steps that occur during a customer journey through your website. It helps you understand how an audience progresses through a process and identifies drop-off points. For example, you can use a funnel report to monitor the success rate of a purchase when customers land on your website. A funnel report provides data to inform decisions and  identifies areas for optimization and process improvements.

## Create a funnel report

To create the funnel report, specify the steps that you want to include and the activity for each step. An activity is an [event](glossary.md) that represents user behavior. You can also set a time period for the report. The funnel report displays the number of users who completed each defined step. 

1. Go to **Funnels** and select **+New funnel** to start a funnel report.
1. In the **Funnel Editor**, under **Steps** select **+Add step.** 
1. Enter a name in  **Step title**.
:::image type="content" source="media/new-funnel-report.png" alt-text="New custom reports":::


1. Select an **Activity**. An activity records when a user views a page (**View** activity) or interacts with content (**Action** activity).
1. Use **Step criteria** to specify the activity's dimension. Dimensions are attributes that can describe, filter, or group data.

1. Select **Add step** until you complete all the steps you want in the report.

- Use the **Time Range** setting to specify the time period in which your funnel report takes place.

7. Select **Save**, name the report, and **Save** again. 

### The Fourth Coffee Company funnel report

The following scenario demonstrates one way of using a funnel report. An analyst with the Fourth Coffee Company wants to understand the impact of a recent promotion on subscription rates. She creates a funnel report to follow customer activity from the moment customers lands on the company home page and uses a subscription promotion code. The analyst creates a funnel report that defines the following steps:

Step 1: Customers who land on the homepage   
Step 2: Customers who make a purchase   
Step 3: Customers who use the promotion code to get a discount on a subscription   
Step 4: Subscription sign-up   

:::image type="content" source="media/funnel-report-example.png" alt-text="New custom reports":::
  
This funnel lets you see the number of users who used the promotion code after a one-time purchase to sign up for the subscription program.

## View and edit funnel reports
You can view funnel reports, change their names, and delete them in the **Funnels library**. 

To see a list of existing funnel reports
- Go to **Funnels** to open the **Funnels library**.   

To rename or delete a funnel report

- Select the ellipsis **(...)**  next to the report you want to change and then select **Edit name** or **Delete**.

## Work with funnel reports
 You can review reports to see how they change over time. <Kate, does changing the time range after the report is created change the report?>   

To view a report
- Select a name to open the report.   

To see the data collected for a report

- Move through each step in the report.
:::image type="content" source="media/funnel-step-data.png" alt-text="New custom reports":::

## View and edit funnel steps
You can also update, reorder, or delete steps in a funnel.   

To edit a funnel step   

1. Select the ellipsis **(...)** on the step that you want to reorder.
1. Select **Edit**.
1. In the **Funnel Editor**, update the information you want to change.  
1. Select **Save**.

To reorder a funnel step
1. Select the ellipsis **(...)** on the step that you want to reorder.
1. Select **Move**, and then **Up**, **Down**, **To top**, or **To bottom**, to move the step.

To delete a funnel step
1. Select the ellipsis **(...)** on the step that you want to remove and select **Delete**.

> [!NOTE]
> At this time, engagement insights funnel reports supports scenarios in which all users are anonymous *or* all users in the funnel are authenticated.
