---
title: Set up large-scale events with Teams town halls
description: Learn how to create and host large scale streamed events in Dynamics 365 Customer Insights - Journeys using Microsoft Teams town halls.
ms.date: 12/22/2025
ms.topic: how-to
author: terezakirk
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Use Microsoft Teams town halls to host large-scale online events

Teams town halls is a new feature designed to help organizations host large-scale, interactive virtual events directly within Microsoft Teams. Town halls can host up to 10,000 attendees, or up to 100,000 attendees with Teams Premium. By integrating town halls with Customer Insights - Journeys, you can create personalized event experiences, track engagement, and nurture customer relationships seamlessly. Learn more: [Get started with town hall in Microsoft Teams](https://support.microsoft.com/office/get-started-with-town-hall-in-microsoft-teams-33baf0c6-0283-4c15-9617-3013e8d4804f).

This integration enables:
- **Event orchestration**: Schedule and manage town hall events from your customer journey workflows.
- **Audience targeting**: Use Customer Insights segments to invite the right participants.
- **Engagement tracking**: Capture attendance and interaction data for post-event analysis.

> [!NOTE]
> To use Microsoft Teams as an online event provider, you must have a [Microsoft 365 license](/office365/servicedescriptions/teams-service-description) that grants access to the Teams service. If you don't have the correct license, you won't see the Teams town hall in Customer Insights - Journeys.

## Create a Teams town hall online event

To create a Teams event, select **Event planning** in the Customer Insights - Journeys app area switcher, then select **Events** in the left navigation pane. Select **+New** in the top ribbon. Next, on the General tab, under the "Stream this event online" section, enable the toggle. After you flip the **Do you want to stream this event** toggle to **Yes**, you see four streaming options: Teams webinar, Teams meeting, Teams live event, and **Teams town hall**.

Select **Teams town hall** as your streaming provider. After you save your changes, the meeting URL for Teams town hall is generated. You can then send this URL to your attendees through emails created in Customer Insights - Journeys.

### Town hall settings

The default town hall settings are configured to provide the best attendee and presenter experience. However, you can easily adjust these settings from your Customer Insights - Journeys event. To change the default settings, select **Open settings**. This selection opens a Teams town hall meeting options pop up and allows you to configure the town hall experience. Learn more: [How to set up town hall meeting options](https://support.microsoft.com/office/schedule-a-town-hall-in-microsoft-teams-d493b5cc-9f61-4dac-8027-d837dafb7a4c).

### Town hall roles

| Role name                    | Role function                                                                                   | How to create the role |
|------------------------------|----------------------------------------------------------------------------------------------------|----------------------------|
| Event owner                  | The user who owns the event record in Customer Insights - Journeys. | Set the event owner by using the **Assign** button on the event ribbon. |
| Teams meeting owner (organizer) | The user who creates and *saves* the record after choosing the town hall option in Customer Insights - Journeys. Changing the owner of the event record in Customer Insights - Journeys doesn’t change the owner of the town hall in Teams. Any change to the event record in Customer Insights - Journeys only reflects in Teams when the owner makes the change or when they select **Sync to Teams**. | Sign in as this user in Customer Insights - Journeys and create a new event to change the owner. |
| Presenter                    | In a Teams town hall, a presenter is a person who presents audio, video, or a screen to the live event, or moderates the question and answer portion.| If you want to invite another person to present, add them to the event or session as a speaker in Customer Insights - Journeys. To add a speaker, create a speaker engagement at the event (or session) level. The speaker is added as a “presenter” for the town hall. Ensure that the speaker's email ID is filled in.

Currently, only organizers can publish or cancel the town hall event through Customer Insights - Journeys. When assigned, co-organizers can edit the meeting options.

### Keeping Customer Insights - Journeys and Teams in sync

A user who has access to an event record and permissions to edit the record in Customer Insights - Journeys can make any change to a record. However, because the same user might not have created the corresponding live event or meeting in Teams (and thus might not be the "Teams Meeting owner"), the changes the user makes to an event record in Customer Insights - Journeys aren’t propagated to Teams. This functionality is similar to functionality within Teams, where a user can’t make changes to a live event or meeting created by another user.

In scenarios where event record changes aren’t propagated to Teams, the Customer Insights - Journeys app displays a warning to any user who isn’t the Teams meeting owner. If the Teams meeting owner opens the event record, they see a **Sync with Teams** button in the ribbon. Selecting the **Sync with Teams** button syncs the changes made to the event by any non-owner users.

> [!NOTE]
> The ability to add co-organizers through Customer Insights - Journeys will be introduced in the February 2026 Customer Insights - Journeys release.

## Publishing a town hall

After you set up the event, you can publish the event in Customer Insights - Journeys. After the Customer Insights - Journeys event is live, the town hall event is published and calendar invites are automatically generated for organizers and sent to co-organizers and speakers directly from Teams.

## Inviting registrants to attend the Teams event through email

After creating the event, going live with it, and gathering registrations, you should [send the registrants an email](email-design.md) to provide the attendee URL. In the Customer Insights - Journeys email designer, you’ll find a **Join in Teams** option in the **Link to** menu for the button element. The **Join in Teams** button generates a unique attendee URL for each attendee.

## Attendance report

Users don't need to register for town hall events, so registrations don't include check-ins. You can view the attendance report for attendees who join the event after it ends, but the report doesn't link to event registrations. Teams town hall events track attendance by email, so the check-in table in Customer Insights - Journeys shows attendance data connected to email addresses, not to event registrations.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
