---
title: Boost event engagement with journeys
ms.reviewer: alfergus
description: Learn how to use Dynamics 365 Customer Insights - Journeys to automate event engagement. From registration to post-event follow-ups, streamline your process.
ms.date: 10/07/2025
ms.custom: 
  - dyn365-marketing
ms.topic: get-started
author: alfergus
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---


# Boost event engagement with journeys

When you host in-person or online events, success depends on engaging your audience throughout the event lifecycle. The lifecycle can span two to three months and includes setup, promotion, reminders, inspiration, thanking, and post-event engagement. Here are some activities in each step of the event lifecycle:

- **Setup**: *Two to three months before the event*. Sign up forms for attendees, speakers, and sponsors. Text messages with short links to social channels. Enrollment confirmation emails.
- **Promote**: *Four to five weeks before the event*. Invitations through email, text messages, social channels, and direct mail. Featured content and people.
- **Remind**: One to seven days before the event. Deadline reminder. Sign up count and capture interest forms. Send updates on dates, locations, and sessions. Send event tips.
- **Inspire**: *During the event*. Check in attendees. Send schedule updates. Send updates to attendees. Share event stats.
- **Thank**: *One to three days after the event*. Send thank you emails. Send surveys. Update social channels with event wrap-up.
- **Engage**: *One to two weeks after the event*. Send a wrap-up email. Announce upcoming events. Nurture leads from the event. Qualify leads.

This article explains how to use Dynamics 365 Customer Insights - Journeys real-time journeys to facilitate the *remind*, *inspire*, and *thank you* steps of the event lifecycle. You learn how to create a real-time journey that:

- Sends a welcome email when a user registers for an event.
- Sends email reminders seven days and one day before the event.
- Sends a text message or email reminder one hour before the event.
- Sends a thank you email if the journey participant attended the event. If the journey participant didn't attend the event, sends a “we missed you” email.

The complete journey looks like this:

> [!div class="mx-imgBorder"]
> [ ![Diagram that shows the complete event engagement journey.](media/event-engagement-complete-journey-small.png) ](media/event-engagement-complete-journey.png#lightbox)

To create this journey, make sure you have the prerequisites ready.

## Prerequisites for a remind, inspire, and thank you journey

To start the event registration process, you need these assets:

1. **Event**: Use the Customer Insights - Journeys app to create an in-person or online event. For details about creating an event, see [Set up an event](set-up-event.md).
1. **Triggers**: Triggers let you respond to customer activities in real time. Use three triggers included with the Customer Insights - Journeys app: Event Registration Created, Event Check-in, and Event Registration Canceled. For more information, see [Customer Insights - Journeys triggers](real-time-marketing-triggers.md).
1. **Email**: Before you create your journey, create emails to welcome attendees, remind attendees about the event, thank attendees, and let people who didn't attend know you missed them. For more information, see [Create a new email and design its content](email-design.md).
1. **Text message**: Create one text message for the last hour reminder before the event. For more information, see [Create outbound text messages](real-time-marketing-outbound-text-messaging.md).

## Step 1: Send a welcome email when a user registers for the event

The first thing you need to create for your event is a journey that sends a welcome email whenever someone registers for the event. To create the journey:

1. Go to **Customer Insights - Journeys** > **Journeys** and select **+ New Journey** in the top toolbar.
1. Give the journey a name, select **Trigger-based** as the journey type, and search for the **Event Registration Created** trigger. This trigger starts an action each time a new attendee register for an event. 
1. Select the **Create** button.

    > [!div class="mx-imgBorder"]
    > ![create a journey](media/event-engagement-create-journey.png "create a journey")

1. On the journey designer canvas, add an action to the journey by selecting the **+** sign below the event registration trigger. Select the **Send an email** action.
1. In the **Send an email** action properties pane, search for the welcome email you want to send. It’s easiest to fine-tune your email and mark it ready to send before creating your journey, but you can also select **+ New Email** to open the email designer as a modal window within the journey designer.

    > [!div class="mx-imgBorder"]
    > ![add email](media/event-engagement-add-email.png "add email")

1. The journey starts each time someone registers for an event. To tie the journey to your specific event, select the trigger, select **Edit** in the right pane, then select **+ Add condition**. In the **Choose an attribute** dropdown, go to **Event Registration Reference** and select **Event**. Then, you can use the **Look for Event** lookup field to find your event.

    > [!div class="mx-imgBorder"]
    > ![add attribute](media/event-engagement-event-attribute.png "add attribute")

Now, each time someone registers for your event, they receive your welcome email. Next, you create reminder emails that are automatically sent to attendees seven days and one day before the event.

## Step 2: Send email reminders seven days and one day before the event

When sending timed reminders, the first instinct of many Customer Insights - Journeys users is to add a "Wait" element to their journey. In this scenario, a wait element won't work. Although the wait element can trigger an action at a specific date and time, we want to trigger an action relative to the date of the event. To trigger a relative-date-based action, you need to create a branch in your journey that activates based on a specific condition.

1. To add a branch based on a condition, select the **+** sign below the Send an email action, then select **Branch based on a specific value**. Name the attribute *Check event start*.
1. Select **Branch 1** in the journey designer. Here, you add a trigger to check the event start date. In the right pane, name the branch *Event start date > 7 days from now*. Then, select the **Condition** button and select the **Choose an attribute** dropdown. You want to create a condition based on the main trigger for the journey. To create the condition, go to **Trigger** > **Event registration created** > **Event Reference**, then search for and select the **Event start date** attribute.

    > [!div class="mx-imgBorder"]
    > ![event start](media/event-engagement-event-start.png "event start")

1. Next, set a relative date for the journey to monitor. To set a relative date, select the **Is** dropdown and change it to **Is after**. Then, select the **Actual date** dropdown and change it to **Relative date**. Finally, change the date dropdown to **7 days from today**. Now, the branch references whether the event start date is seven days after the execution time of the attribute tile.
1. Now, add a **Wait** element to the relative date branch. The Wait element ties to the event and waits until the date is seven days before the event to trigger an action. To add the Wait element, select the **+** below the **Event start date > 7 days from now** condition. Add a **Hold an action for a specific time** element. In the right pane, under **People will wait**, select **Until a time specified by a trigger**. Then, under **Choose a specific trigger attribute**, go to **Event registration created** > **Event Reference**, then search for and select the **Event start date** attribute. Set the **Timing** to **7 days before the specified time**.
1. You’re now ready to trigger an action seven days before the event’s start date. To send a reminder email, select the **+** below the Wait element and select a **Send an email** action. In the right pane, select the reminder email you’d like to send.

    > [!div class="mx-imgBorder"]
    > ![event reminder](media/event-engagement-event-reminder.png "event reminder")

1. To send a second reminder one day before the event, add a new attribute branch that follows the same steps, only with a relative date condition and a Wait element set one day before the event. To add the reminder, select the **+** above the journey exit and select a **Branch based on a specific value** element. Name the attribute **Check event start**.
1. Next, select **Branch 1**, name it **Event start date** > **1 day from now**, set **Event start date** as the attribute, and set the timing to **Is before**, **Relative date**, and **Tomorrow**.
1. Add a **Wait** element after the branch condition, set the **People will wait** value to **Until specified by a trigger**, choose the **Event start date** attribute, and set the **Timing** to **Before the specified time 1 day**.
1. Then, to send the second reminder after the Wait element expires, select the **+** after the Wait element, add a **Send an email** element, and select the second reminder email.

    > [!div class="mx-imgBorder"]
    > ![event reminder2](media/event-engagement-event-reminder2.png "event reminder2")

## Step 3: Send a text message or email reminder one hour before the event

Now you need to set up a text message reminder to be sent one hour before the event. For this, Customer Insights - Journeys has a feature that allows you to select time funnels not only for weeks, days, and hours but even for minutes. Here, you can use a **Wait** element because you already filtered relative dates for seven days and one day before the event. At this point, chances are your non-relative date Wait element is valid.

1. Select the **+** above the journey exit, then add a **Hold an action for a specific time** element. Set **People will wait** to **Until specified by a trigger**, choose the **Event start date** attribute, and set **Timing** to **Before the specified time 1 hour**.
1. Next, you let Customer Insights - Journeys use the power of AI to decide which channel is the best to send your one-hour reminder on. To let Customer Insights - Journeys decide, select the **+** above the journey exit and select a **Send messages through the right channel** element. Choose **Email** and **Text message** as your channels and select the **Optimize** button.
1. In the **Channel optimization** pane, set **Display name** to **One-hour reminder optimization**.
1. Select the **Email** action below the **Channel optimization** element, then select your one-hour reminder email. Likewise, select the **Text message** action, then select your one-hour reminder text message.

    > [!div class="mx-imgBorder"]
    > ![Screenshot of event optimization pane showing channel selection and optimization options.](media/event-engagement-event-optimization.png "event optimization")

1. Notice that the **Channel optimization** element shows a red warning sign because a **Goal** isn't set. In this journey, the goal is to get attendees to check in to the event. To optimize for the goal, select the Channel optimization element. For **Journey goal**, select **Custom goal** for **The goal of this journey is**. Under the **Title** dropdown, enter **Drive event check-in attendance** as the name of your custom goal, then select the **+** sign. For **This goal is met when**, search for and select the **Event Check-in** trigger. Enter **50%** for **The number of people needed is**. This percentage means the Customer Insights - Journeys app considers the goal met when 50 percent of people who registered for the event check-in.
1. Define the control group for channel optimization. Select the **Channel optimization** element, then under **Default channel**, select **Text message**. This step sends 10 percent of the audience a one-hour reminder through the text message channel, giving the Channel optimization element a non-AI-driven control group to measure results against.

## Step 4: Send a thank you or we missed you email

The final step in the journey is to send a response based on whether the recipient checked into the event. If they checked in, the journey sends a “thank you for attending” email. If they didn't check in, the journey sends a “sorry we missed you” email. To tailor your responses, add a **Respond to an action** element to your journey.

1. Select the **+** above the journey exit and add a **Respond to an action** element. Specify a condition that, if met, sends journey participants down the **Yes** branch. If the condition isn't met, participants go down the **No** branch.
1. Select the **If/then branch** element. Set **Choose a branch condition type** to **A trigger is activated**. In the trigger lookup, search for **Event Check-in**. Provide a time frame so that, if the condition is met, participants go down the **Yes** branch. For this event, set the time frame to cover the time after the event starts. Set the time limit to **two hours**.

    > [!div class="mx-imgBorder"]
    > ![event check-in](media/event-engagement-event-if-then.png "event check-in")

1. In the **Yes** branch of the if/then check-in element, you want to send an email you created thanking the recipient for attending, but you don't want to send it right away. Instead, you want to send it an hour after the event ends. To set the email delay time, select the **+** in the Yes branch and add a **Hold an action for a specific time** element. Set **People will wait** to **Until a time specified by a trigger**. For the **trigger attribute**, go to **Event registration created** > **Event Reference**, then search for **Event end date**. Set **Timing** to **1 hour**.
1. Below the Wait element, select the **+** and add a **Send an email** action. Select the “thank you for attending” email.
1. Next, set an email to send to journey participants who didn't check into the event. In the **No** branch of the if/then check-in element, select the **+** and add a **Send an email** action. Select the “sorry we missed you” email.

    > [!div class="mx-imgBorder"]
    > ![thank you email](media/event-engagement-thank-you.png "thank you email")

## Event engagement journey wrap-up

You have now built a journey that thanks event attendees for registering, sends timely event reminders, and sends tailored email responses depending on whether a journey participant checked into the event. What’s so powerful about this journey—and Customer Insights - Journeys generally—is that you can use the journey for any event you host! If you tried to achieve a similar outcome using a segment-based journey, you’d need to painstakingly create specialized segments and separate journeys for each event. Real-time journeys truly are the future of customer engagement.

## Bonus tip

Customer Insights - Journeys triggers give you a simple way to remove a journey participant who cancels their event registration during the journey. To remove the canceled participant from the journey, select the **Event Registration Created** trigger at the top of the journey. In the right pane, select the **Edit** link to the right of **End**. Under **Exit when a trigger occurs**, search for **Event Registration Canceled**. When a participant cancels their registration, they're removed from the journey and don't get further notifications.

> [!div class="mx-imgBorder"]
> ![Screenshot of the Event Registration Canceled trigger selected in Customer Insights - Journeys.](media/event-engagement-create-canceled.png "Screenshot of the Event Registration Canceled trigger selected in Customer Insights - Journeys.")

[!INCLUDE [footer-include](./includes/footer-banner.md)]

## Bonus Tip 2 - New Attributes for Event Timing in UTC
When building journeys for event registration in Real-Time Marketing, especially for journeys that are used for events that span multiple time zones, accurate timing is critical. Journeys for the multi-event scenario typically operate in UTC, which can lead to discrepancies if local time zone values are used in triggers. To address this, two new attributes have been introduced:

- Event start date UTC
- Event end date UTC

If you use the “**Wait until a time specified by a trigger**” condition in your journey, these attributes ensure the correct UTC-based values are applied for event start and end dates. This prevents timing errors and guarantees that your automation aligns with the actual event schedule, regardless of participant time zones.

