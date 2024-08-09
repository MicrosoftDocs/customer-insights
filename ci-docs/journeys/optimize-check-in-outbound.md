---
title: Make the most of your event check-in flow in outbound marketing
description: Learn how to optimize your event check-in flow in outbound marketing.
ms.date: 08/21/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Make the most of your event check-in flow in outbound marketing

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Dynamics 365 check-in entities are created for every type of event including meetings, webinars, and live events. After the event, you can see who attended by going to the **Event planning** area, selecting your event, and then going to **Registration and Attendance** > **Event Check-ins**.

## Make the most of your check-in monitoring *before* an event

To ensure that your attendees can check in before an event, implement the following best practices:

- Test your event invite email to ensure that it populates the correct personalized meeting link for each contact.
- Each contact must already be registered for the event when they receive the "Join" email, thus, the timing of your invite emails is important! Send the "Join" email only after the contact is registered for the event or session. Use segments to trigger the email sending action at the right time.

## Make the most of your check-in monitoring *after* an event

In Dynamics 365 Customer Insights - Journeys, you can monitor your event attendance and join and leave times from the check-ins created after the meeting is over. These are some best practices to follow when reviewing check-ins:

- If check-ins are missing, ensure that the event invite and join emails were sent in the correct order [as mentioned above](optimize-check-in-outbound.md#make-the-most-of-your-check-in-monitoring-before-an-event).
- Pay attention to changes to daylight savings, if any, for the time zone selected for your event or session start time. Some "Join" button clicks may fail the 120-minute criteria if there was a change in daylight savings between the event or session creation time and the event or session start time. Learn more about the 120-minute criteria: [Inviting registrants to attend the Teams event through email](teams-webinar.md#inviting-registrants-to-attend-the-teams-event-through-email).
- If you're hosting a Teams webinar, select the **Sync with Teams** button on the event page. The button pulls Teams attendance data to create check-ins in Customer Insights - Journeys.
- Look at the Teams Attendance Report to see the join information. The report will only list a contact if they have certain Teams policies enabled. Learn more: [View webinar engagement data](teams-webinar.md#view-webinar-engagement-data).

- Review the [email](insights.md#email-insights) and [contact](insights.md#contact-insights) insights for your event invite and event attendees. This data will only be collected if the email was sent from the Marketing app and contained the tracking link. Learn more: [How marketing email works in Dynamics 365 Marketing](prepare-marketing-emails.md#how-marketing-email-works-in-customer-insights---journeys).

> [!WARNING]
> Check-ins are created only by selecting the [Join in Teams button](teams-webinar.md#view-webinar-engagement-data) in the email or the [Add to Calendar Join button](add-to-calendar.md#customize-the-icalendar-file-descriptions).
>
> If an attendee selects the **Join in Teams** button *more than 120 minutes* before the event starts, the check-in *won't* be created. This cannot be controlled or changed by the meeting organizer. This is a hard-coded feature to prevent accidental check-ins when a recipient tests the link after they receive the email.
>
> Contacts must use their personalized meeting link for a check-in to be created (forwarded emails won't work). To prevent privacy issues, the Customer Insights - Journeys app does not track attendee actions unless they use the personalized link.
>
> Expect up to a four-hour delay after an event ends until check-ins appear in the Customer Insights - Journeys app. Check-in creation is counted as a post-processing step after the event and takes several hours to fully reflect in the Customer Insights - Journeys app.

[!INCLUDE [footer-include](./includes/footer-banner.md)]