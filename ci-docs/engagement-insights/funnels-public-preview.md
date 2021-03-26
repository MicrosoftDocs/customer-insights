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

Use funnel reports to understand how an audience progresses through the steps of a process and help you identify drop-off points. For example, you can create a funnel report to  monitor view the success rate of a purchase when customers land on your website.  <Kate, just to confirm. Is it funnels or funnel reports?>

You can use the data from a funnel report to inform decisions and identify areas of potential optimization and process improvements.

## Prerequisites

<Kate, Before you create funnel report, what are the pre-reqs, if any?  For example, should they have a workspace set up? >

## Create a funnel report

<Kate, this should be two sections: create a funnel and then edit a funnel report. For this section, I added a screenshot to show users the UI that they will see when creating a report.  I think it's a good idea to use a scenario as an example. Can you supply an example, perhaps based on some of the reports that you already built? That would make it easier to explain the step criteria. Additionally, please describe the purpose of the Activity and Step criteria to help the users.>  

1. Go to **Funnels** >**New funnel** to start the funnel report.
1. In the **Funnel Editor** pane, under **Step 1,** select **Add a step.**
:::image type="content" source="media/new-funnel-report.png" alt-text="New custom reports":::

1. For each step in the process, enter the following information:

- Enter the name in  **Step title**
- Select an **Activity** from the drop-down list.  
- Select the **Dimension criteria** ...

4. Specify the **Action name** and **Select values** in **Step criteria**.
1. To inquire about a certain point in time, use the **Time Range** setting to change the time period in which your funnel report takes place
1. Select **Add step**.
The funnel will update displaying the number of users who completed that step 


<Kate, This is where a scenario would be helpful. I only saw a blue line after this step, probably because I don't have that much data This is a screenshot of the giftcard report. Can you explain the information displayed? >

:::image type="content" source="media/giftcard-example.png" alt-text="New custom reports":::

6. Continue to add steps in the **Funnel Editor** until you've created all the steps you want in the report. 
1. The select **Save**, give the report a name.

<Kate, it looks as though the user selects Save twice to save a report? Is this going to change? >

:::image type="content" source="media/save-funnel-report.png" alt-text="New custom reports":::

## Edit a funnel report

From the funnels resource list, you can view, edit and load previously created funnel reports. <Kate, what are some of the reasons to update a report?>

1. Go to **Funnels** to see the list of existing funnel reports in the **Funnels library**.
1.  Select a name to open a report.
1.  Select the ellipsis **(...)** to edit or delete a step. 
1. Select **Save**  to update your changes. 

<Kate, this note is incomplete. The last sentence is missing information.>
> [!NOTE]
> Future enhancements to funnel reports include support for scenarios in which users transition from unauthenticated and authenticated. At this time, Engagement insights funnel reports only ???