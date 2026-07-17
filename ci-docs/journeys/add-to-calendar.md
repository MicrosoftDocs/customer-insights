---
title: Generate iCalendar files for events and sessions
description: Set up an Add to Calendar email button and customize iCalendar descriptions for events and sessions in Customer Insights - Journeys.
ms.date: 07/16/2026
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Generate iCalendar files for events and sessions

Use this article to set up **Add to calendar** links in Customer Insights - Journeys emails and generate personalized iCalendar (.ics) files for event attendees. Learn how to choose whether the file includes the event, registered sessions, or both, and how to customize calendar descriptions for HTML and plain-text calendar clients.

For streamed events, this article also explains how to use the check-in link wildcard to add or update personalized check-in buttons in the iCalendar description.

## How to create a customized iCalendar file

iCalendar files are generated using the new **Add to Calendar** button option in the email editor.

To create an **Add to Calendar** button:

1. In the email designer, add a button.
1. Go to the button **Properties** tab. Select **Add to Calendar** from the **Link to** dropdown.

    :::image type="content" source="media/add-to-calendar-properties2.png" alt-text="Screenshot of the Add to Calendar option in the button properties." lightbox="media/add-to-calendar-properties2.png":::

1. Choose the information you want to include in the iCalendar file using the **What should be added to calendar** dropdown. The options include:
    - **Only the event**: The iCalendar file will contain only the *event* the contact has registered for.
    - **Only the sessions**: The file will contain only the event *sessions* the contact has registered for.
    - **Both event and associated sessions**: The file will contain information for the *event* and the *sessions* the contact has registered for.
1. Select the event you want to link to.
1. Enter the **Button text** that appears on the button. You can customize button style in the **Style** section.

When you send an email with the **Add to Calendar** button, contacts who registered for the event will receive a personalized link to download their agenda as an iCalendar file.

> [!NOTE]
> If a contact didn't register for the event or session you select for the button, they will not see the **Add to Calendar** button in their email.

## Customize the iCalendar file descriptions

Each event or session in the iCalendar file contains a configurable description. To configure the description content:

1. Go to the **Event planning** work area and choose the event you want to configure.
1. In the event, go to the **Additional information** tab.
1. To edit the iCalendar information, go to the **Calendar content** section. The left content section allows you to edit content for calendars that support HTML descriptions, such as Outlook. The right content section allows you to edit content for calendars that only support text descriptions, such as Gmail and Apple Calendar. Depending on which calendar the iCalendar file is imported into, either the HTML *or* the text only description will be used.

    :::image type="content" source="media/add-to-calendar-content.png" alt-text="Screenshot of the calendar content editing section in Customer Insights - Journeys." lightbox="media/add-to-calendar-content.png":::

## Streamed event check-ins

For streamed events, a check-in button is automatically added to the iCalendar file description if the calendar content is empty. You can remove the check-in button or add a new button with the link set to the following wildcard: `{{msevtmgt_checkin_url}}`. The wildcard is converted to a personalized check-in link for the streamed event when the contact downloads the iCalendar file.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
