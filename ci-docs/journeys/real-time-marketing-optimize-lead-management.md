---
title: Create sales activities from lead signals
description: Learn how to optimize lead management by engaging sellers right away in Dynamics 365 Customer Insights - Journeys.
ms.date: 02/12/2025
ms.topic: get-started
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Create sales activities from lead signals

When using journeys to nurture leads and opportunities, it's important to pay attention to signals that may indicate a sense of urgency or interest from the leads. Signals may include enhanced engagement with your marketing messages or increased activity on your website or social media channels.

With Dynamics 365 Customer Insights - Journeys, you can leverage this information to create customized sales activities, such as tasks and phone calls, directly from the journey. This means that you can reach out to leads with individualized attention when they're most likely to engage and show interest in your product or service. This increases your chances of converting leads into customers and driving revenue for your business.

This feature allows you to seamlessly integrate your marketing and sales efforts, providing a more cohesive and streamlined experience for your leads and customers. With the ability to create sales activities directly from the journey, you can better track and measure the effectiveness of your marketing and sales efforts and make data-driven decisions to optimize your campaigns for maximum impact.

[!NOTE]
> The current implementation of creating a task, phone call, lead, or opportunity has a limited set of values exposed in the journey editor that can be set on each entity type. The ability to set additional fields (including custom) is a known feature ask that doesn't yet have an estimated date. Check the [release plans](/dynamics365/release-plans/) to see when this feature will be prioritized and delivered.

## Scenario 1: Handing off high value leads timely to drive paid conversion rate

To facilitate faster and more effective deal closures, you can create phone call records for your sales team directly from nurturing journeys when a high value action is taken. In this example, after a lead has expressed interest through submitting a form, you can create a phone call record in the journey based on the form name using the below steps:

1. Go to **Customer Insights - Journeys** > **Engagement** > **Journeys** and select **+ New Journey** in the top toolbar.
1. Give the journey a name, select **Trigger-based** as the journey type, and search for the **Marketing form submitted** trigger.
1. Next, select the **+** sign below the "Marketing form submitted" trigger on the journey designer canvas to add another tile to the journey.

    > [!div class="mx-imgBorder"]
    > ![Add a phone call tile to start the journey](media/real-time-marketing-phone-call-tile.png "Add a phone call tile to start the journey")

1. Create a subject for the **Phone call** and assign it to the owner. It can be the record owner itself, its contact/account owner, or any specific user/team in your organization.

    > [!div class="mx-imgBorder"]
    > ![Add a phone call assignee](media/real-time-marketing-phone-call-assignee.png "Add a phone call assignee")

1. You can also add notes for the sales agent so that they have more well-rounded information regarding where the lead came from.

    > [!div class="mx-imgBorder"]
    > ![Add a note regarding the phone call to the assignee](media/real-time-marketing-phone-call-assignee-note.png "Add a note regarding the phone call to the assignee")

1. To further nurture the lead, you can track the status of the phone call being completed (after the seller marks the task as **Completed** in Dynamics 365 Sales), then send a follow up email.

    > [!div class="mx-imgBorder"]
    > ![Track the status of the phone call lead completed](media/real-time-marketing-phone-call-lead-status.png "Track the status of the phone call lead completed")

## Scenario 2: Resolve a hard bounce as a task

You can give a task to your team to look for a customer's email address after a hard bounce, like how a phone call record can be created in customer journeys. Your previously created task templates will automatically be finished on the journey canvas. 

> [!div class="mx-imgBorder"]
> ![Track the email address after a hardbounce](media/real-time-marketing-create-hardbounce-task.png "Track the email address after a hardbounce")

You can also send a "System Down" email after the task has been completed by your team member.

> [!div class="mx-imgBorder"]
> ![Send the email with downtime status after a hardbounce](media/real-time-marketing-email-update-after-hardbounce.png "Send the email with downtime status after a hardbounce")

## Scenario 3: Create a lead for a seller to follow-up on

You can create a lead in Dynamics 365 Sales for a seller to follow-up on and specify a topic, owner, determine what should happen if there's already a lead record for that person, and add any note you'd like the seller to consider when taking action. 

## Scenario 4: Create an opportunity for a seller to follow-up on

You can create an opportunity in Dynamics 365 Sales for a seller to follow-up on and specify a topic, owner, and any notes you want the seller to know when taking action. 

## Scenario 5: Activate a custom trigger to initiate a sales sequence

You can activate a custom trigger anywhere in a journey, including a custom trigger that initiates a sales sequence in Dynamics 365 Sales. This is a powerful tool if there are already sales sequences configured and you want to start them off after a marketing journey. 

## View analytics for your activities  

You can view the status breakdown for the phone call record created after the journey has been running for a while.

> [!div class="mx-imgBorder"]
> ![Check the lead analytics](media/real-time-marketing-phone-call-lead-status-analytics-1.png "Check the lead analytics")
