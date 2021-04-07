---
title: Funnel reports (public preview)
description: How to use funnel reports to understand how audience makes decisions.
ms.reviewer: kamacdon
ms.author: v-salash
author: pickwick129
ms.date: 04/02/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# Create and manage funnel reports (public preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A funnel report collects information about the steps that occur during a process. It helps you understand how an audience progresses through a process and identifies drop-off points. For example, you can use a funnel report to monitor the success rate of a purchase when customers land on your website. A funnel report provides data to inform decisions and  identifies areas for optimization and process improvements.

## Prerequisites

Before creating a funnel report, you must create a [workspace](manage-environments-workspaces.md) and use the [engagement insights SDK](instrument-website.md) to instrument your website.

## Create a funnel report

To create the funnel report, specify the steps that you want to include and the activity for each step. An activity is an [event](glossary.md) that represents user behavior. You can also set a time period for the report. The funnel report gathers data from the selected steps. <Kate, is this true?>

1. Go to **Funnels,** and select **+New funnel** to start a funnel report.
1. In the **Funnel Editor**, under **Steps** select **+Add step.** 
:::image type="content" source="media/new-funnel-report.png" alt-text="New custom reports":::

1. Enter a name in  **Step title**.
1. Select an **Activity**. An activity records when a user views a page (**View** activity) or interacts with content (**Action** activity).
1. Use **Step criteria** to specify the activity's dimension. Dimensions are attributes that can describe, filter, or group data.

1. Select **Add step** until you complete all the steps you want in the report.

- Use the **Time Range** setting to change the time period in which your funnel report takes place.

7. Select **Save**, name the report, and **Save** again. 

The following scenario demonstrates one way of using a funnel report. An analyst with the Volcano Coffee Company wants to understand the impact of a recent promotion on subscription rates. The analyst creates a funnel report to follow customer activity from the moment a customer lands on the company home page and uses a subscription promotion code. The analyst creates a funnel report that defines the following steps:

1. Step 1: Customers who land on the homepage
2. Step 2: Customers who make a purchase
3. Step 3: Customers who use the promotion code to get a discount on a subscription
4. Step 4: Subscription

:::image type="content" source="media/funnel-report-example.png" alt-text="New custom reports":::
  
This funnel lets you see the number of users who used the promotion code after a one-time purchase to sign up for the subscription program.

## Manage funnel reports

You can view previously created funnel reports in the **Funnels library** to see how your report changes over time and compare previous funnel reports to future ones. <Kate, How would I compare reports?>

 1. Go to **Funnels** to see the list of existing funnel reports in the **Funnels library**.
 1. Select a name to open a report.

You can also delete and reorder steps.

1. To move a funnel step, select the step that you want to reorder.
1. Select the ellipsis **(...)**, **Move**, and then **Up**, **Down**, **To top**, or **To bottom**, to move the step.

## Edit or delete a funnel report


1. Go to **Funnels** to see the list of existing funnel reports in the **Funnels library**.
1. Select a name to open a report.
1. Select the ellipsis **(...)** to edit or delete a step.
1. Select **Save**  to update your changes.

> [!NOTE]
> Future enhancements to funnel reports include support for scenarios in which users transition from unauthenticated and authenticated (Kate, do you mean a user in Active Directory services?Can we supply a link for more information for users?). At this time, engagement insights funnel reports supports scenarios in which all users are anonymous OR all users in the funnel are authenticated.
