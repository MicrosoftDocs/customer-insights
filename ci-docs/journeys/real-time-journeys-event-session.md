---
title: Set up session-level registration
description: Learn how to set up session-level registration in Dynamics 365 Customer Insights - Journeys.
ms.date: 04/05/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - enduser
---

# Set up sessions

The core attractions of your event offering will typically be its sessions and speakers. A simple event might have just one session, whereas a conference will typically have several sessions spread over several days.

To set up sessions, start by [setting up the event](set-up-event.md) as usual, including basic settings, but then go to the **Agenda** tab for the event. In the Agenda tab, you can use calendar or standard grid view to add new sessions. Each session will have its own set of settings that include information about the session, speakers, sponsors, type of the session and also capacity of the session.

**Session Capacity Utilization**: Session capacity can be allocated to sessions with limited seating by navigating to **Session** > **Capacity** > **Session maximum capacity**.

Important: In Dec 2024, a change was introduced to how the capacity of event and sessions work. In the past, you could only use either session or event capacity, but thw two could not be used in conjunction. With the latest update, you can set an event capacity as well as session capacity for your events. Event capacity needs to always be equal or higher than a session capacity.

## Use session-level registration

After setting up the agenda, event organizers can let attendees assemble their own event schedule by choosing from all available sessions. Session-level registration can be enabled in **Website and Form** tab. Under Registration settings, enable "Allow attendees to register for sessions". When session-level registration is enabled for an event (Important: This setting used to be called allow registrants to create their own agenda and was placed in the Agenda tab), the registration form that has the session tiles in it automatically allows the attendees to select the sessions they're interested in.

Additional settings include: 
- Allow single session registration only - this will change multi select field to a single select field on the form and allow attendees to register for one session only
- Make the session registration required - this will make the session selection mandatory

It’s important to note that session-level registration requires the registration form to include the sessions. This is done by using the **Sessions** element in the form editor so that attendees can see the sessions and have the option to sign up for the sessions they select.

:::image type="content" source="media/sessions-form-element.png" alt-text="Screenshot of the sessions form element.":::

To access the registration form for the event, select the event, then go to **Website and form** and select the **Registration form**.

:::image type="content" source="media/select-registration-form.png" alt-text="Screenshot of selecting the registration form.":::

This opens a special version of the form editor that has extra elements for your event including the **About**, **Sessions**, and **Speakers** elements.

> [!WARNING]
> To ensure successful registration for an event with a custom agenda, at least one session must be published and available for selection (with seats available).

## Style your default registration forms with sessions using Theme
The theme feature is a user-friendly interface for editing CSS class definitions in the form HTML and styling your form experience. The Theme section can be opened when navigating to the registration form of your choice and by selecting the brush icon in the right pane. Theme controls the style of all types of fields, buttons, and text. Once you set the theme of a field, it affects all fields of the same type in your form.

> [!NOTE]
> The form styles are constantly being improved. Forms created in an older version of real-time journeys form editor have limited options to change the form styling using the theme feature. You can enable more style options by selecting the Enable button in the theme section. This updates your form styles to the latest version compatible with the theme feature, which is now relevant for the latest release of session-level registration improvements.

## View and edit event session registrations

The method to view and edit registration details for a session-level event depends on whether you want to view all registrations for the event or view registrations for a specific session:

- To view all registrations for the event (people who registered for at least one session), open the relevant event record, go to the **Registration and attendance** tab, and scroll to the **Event registration** section. You can also add or remove registrations from here.
- To view all registrations for a specific session, open the relevant event record, go to the **Agenda** tab, scroll to the **Sessions** list, and select a session. In the open session record, go to the **Registration and attendance** tab and scroll to the **Sessions registrations** list. You can also add or remove registrations from here.
