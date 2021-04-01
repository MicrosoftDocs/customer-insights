---
title: Funnel reports (public preview)
description: How to use funnel reports to understand how audience make decisions.
ms.reviewer: kamacdon
ms.author: v-salash
author: pickwick129
ms.date: 03/25/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# About funnel reports (public preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Use funnel reports to understand how an audience progresses through the steps of a process and help you identify drop-off points. For example, you can create a funnel report to  monitor view the success rate of a purchase when customers land on your website.  <Kate, just to confirm. Is it funnels or funnel reports? Funnel reports!>

You can use the data from a funnel report to inform decisions and identify areas of potential optimization and process improvements.

## Prerequisites

Before creating a funnel report, you must have created a workspace and instrumented your website with the Engagement Insights SDK. This can be done under the Admin section in the navigation. 

## Create a funnel report

<Kate, this should be two sections: create a funnel and then edit a funnel report. For this section, I added a screenshot to show users the UI that they will see when creating a report.  I think it's a good idea to use a scenario as an example. Can you supply an example, perhaps based on some of the reports that you already built? That would make it easier to explain the step criteria. Additionally, please describe the purpose of the Activity and Step criteria to help the users.>  

1. Go to **Funnels** >**New funnel** to start the funnel report.
1. In the **Funnel Editor** pane, under **Step 1,** select **Add a step.**
:::image type="content" source="media/new-funnel-report.png" alt-text="New custom reports":::

1. For each step in the process, enter the following information:

- Enter the name in  **Step title**
- Select an **Activity** from the drop-down list.  
    - Activity can be defined as an event that represents user behavior. An activity records when a user views a page (view activity) or interacts with content (action activity). 
- Select the **Dimension** ...

4. Specify the Dimension name for your step criteria. I.e. "Page name is Homepage". 
1. To inquire about a certain point in time, use the **Time Range** setting to change the time period in which your funnel report takes place
1. Select **Add step**.
The funnel will update displaying the number of users who completed that step 


<Kate, This is where a scenario would be helpful. I only saw a blue line after this step, probably because I don't have that much data This is a screenshot of the giftcard report. Can you explain the information displayed? >

For example: 
An analyst with the Volcano Coffee Company wants to understand the impact their recent promo has had on subscription rates. 
The analyst creates a funnel report and defines the following steps: 
1. Step 1: Customers who land on the homepage
  - Step title = Homepage 
  - Activity = View
  - Dimension = pageName is Homepage 
2. Step 2: Customers who make a purchase
  - Step title = Purchase 
  - Activity = Action
  - Dimension = linkName is Purchase 
3. Step 3: Customers who use the promo code to get a discount on a subscription 
  - Step title = Promo 
  - Activity = View 
  - Dimension = trackingCode is WinterPromo 
4. Step 4: Subscription 
  - Step title = Subscription 
  - Activity = Action
  - Dimension = linkName is Subscribe 

You also have the ability to delete and reorder funnel steps by clicking on the ellipses for each step. From this funnel, I can see the number of users who used the promo code after a one-time purchase to sign up for my subscription program.  

:::image type="content" source="media/giftcard-example.png" alt-text="New custom reports":::

6. Continue to add steps in the **Funnel Editor** until you've created all the steps you want in the report. 
1. The select **Save**, give the report a name.

<Kate, it looks as though the user selects Save twice to save a report? Is this going to change? The user saves a step -- and the report separately>

:::image type="content" source="media/save-funnel-report.png" alt-text="New custom reports":::

## Edit a funnel report

From the funnels resource list, you can view, edit and load previously created funnel reports. <Kate, what are some of the reasons to update a report?>

1. Go to **Funnels** to see the list of existing funnel reports in the **Funnels library**.
1.  Select a name to open a report.
1.  Select the ellipsis **(...)** to edit or delete a step. 
1. Select **Save**  to update your changes. 

<Kate, this note is incomplete. The last sentence is missing information.>
> [!NOTE]
> Future enhancements to funnel reports include support for scenarios in which users transition from unauthenticated and authenticated. At this time, Engagement insights funnel reports supports scenarios in which all users are anonymous OR all users in the funnel are authenticated. 
