---
title: Set up large-scale events with Teams Town Hall 
description: Learn how to create and host large scale streamed events in Dynamics 365 Customer Insights - Journeys using Microsoft Teams Town Hall.
ms.date: 11/05/2025
ms.topic: how-to
author: terezakirk
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Use Microsoft Teams Town Hall to Host large-scale online events
Teams Town Hall is a new feature designed to help organizations host large-scale, interactive virtual events directly within Microsoft Teams. Town halls can host up to 10k attendees, or up to 100k attendees with Teams Premium.  By integrating Town Hall with Customer Insights Journeys, you can create personalized event experiences, track engagement, and nurture customer relationships seamlessly. Read more [Get started with Town Hall in Microsoft Teams](/https://support.microsoft.com/en-us/office/get-started-with-town-hall-in-microsoft-teams-33baf0c6-0283-4c15-9617-3013e8d4804f)

This integration enables:
- Event orchestration: Schedule and manage Town Hall events from your customer journey workflows.
- Audience targeting: Use Customer Insights segments to invite the right participants.
- Engagement tracking: Capture attendance and interaction data for post-event analysis.

> [!NOTE]
> To use Microsoft Teams as an online event provider, you must have a [Microsoft 365 license](/office365/servicedescriptions/teams-service-description) that allows you access to the Teams service. If you do not have the correct license, you will not see the Teams Town Hall in Customer Insights - Journeys.

## Create a Teams Town Hall online event

To create a Teams event, select **Event planning** in the Customer Insights - Journeys app area switcher, then select **Events** in the left navigation pane. Select **+New** in the top ribbon. Next, on the General tab, under "Stream this event online" section, enable the toggle. After you flip the **Do you want to stream this event** toggle to **Yes**, you’ll have four streaming options: Teams webinar, Teams meeting, Teams live event and 
**Teams Town Hall**. 

Select Teams Town hall as your streaming provider. Once you save your changes the meeting URL for Teams Town Hall will get generated. This URL can then be used to send to your attendees through emails created in Customer Insights-Journeys.

### Town Hall settings

The default Town Hall settings are configured to provide the best attendee and presenter experience. However, you can easily tweak these settings from your Customer Insights - Journeys event. To change the default settings, click on **Open settings**. This will open a Teams Town Hall meeting options pop up and it will allow you to configure the Town Hall experience. 
Read more: [How to set up Town Hall meeting options](/https://support.microsoft.com/en-us/office/schedule-a-town-hall-in-microsoft-teams-d493b5cc-9f61-4dac-8027-d837dafb7a4c) 

### Town Hall roles

| Role name                    | What do they do?                                                                                   | How to create them? |
|------------------------------|----------------------------------------------------------------------------------------------------|----------------------------|
| Event owner                  | The user who owns the event record in Customer Insights - Journeys. | Set the event owner using the **Assign** button on the event ribbon. |
| Teams meeting owner (organizer) | The user who created and *saved* the record after choosing the Town Hall option in Customer Insights - Journeys. Changing the owner of the event record in Customer Insights - Journeys doesn’t change the owner of the Town Hall in Teams. Any change to the event record in Customer Insights - Journeys will only reflect in Teams when done by the owner or when they select **Sync to Teams**. | Sign in as this user in Customer Insights - Journeys and create a new event to change the owner. |
| Presenter                    | In a Teams Town Hall, a presenter is a person who presents audio, video, or a screen to the live event, or moderates the Q&A.| If you want to invite another person to present, add them to the event or session as a speaker in CIJ. To add a speaker, create a speaker engagement at the event (or session) level. The speaker is added as a “presenter” for the Town Hall. Ensure that the speaker's email ID is filled in.

Only organizers can publish the Town Hall Event through Customer Insights-Journeys and cancel the event at present. Co-organizers, when assigned, are able to edit the meeting options. 

### Keeping Customer Insights - Journeys and Teams in sync

A user who has access to an event record and permissions to edit the record in Customer Insights - Journeys can make any change to a record. However, since the same user may not have created the corresponding live event or meeting in Teams (and thus may not be the "Teams Meeting owner"), the changes the user makes to an event record in Customer Insights - Journeys aren’t propagated to Teams. This functionality is similar to functionality within Teams, where a user can’t make changes to a live event or meeting created by another user.

In scenarios where event record changes aren’t propagated to Teams, the Customer Insights - Journeys app displays a warning to any user who isn’t the Teams meeting owner. If Teams meeting owner opens the event record, they’ll see a **Sync with Teams** button in the ribbon. Selecting the **Sync with Teams** button syncs the changes made to the event by any non-owner users.

> [!NOTE]
> The ability to add co-organizers through Customer Insights - Journeys will be introduced with December release.

## Publishing a Town Hall 
When the event is set up, you can go ahead and publish the event in Customer Insights - Journeys. Once the event is live, the Town Hall Event will be published and calendar invites will be automatically generated for organizers and sent to co-organizers and speakers directly from Teams. 

## Inviting registrants to attend the Teams event through email

After creating the event, going live with it, and gathering registrations, you should [send the registrants an email](email-design.md) to provide the attendee URL. In the Customer Insights - Journeys email designer, you’ll find a **Join in Teams** option in the **Link to** menu for the button element. The **Join in Teams** button generates a unique attendee URL for each attendee. 

## Attandance report
Town Hall events do not require users to register for the event so no check-ins are being associated with registrations. The attandance report of attendees who joined the event will be available after the event is over, but it won't be associated with event registrations. The way Teams Town Hall map attandance is via email, therefore you will see the check-in table populated in Customer Insights - Journeys with attandance data associated with the email address, but not with event registration. 
