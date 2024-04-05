---
title: Set up session-level registration
description: Learn how to set up session-level registration in Dynamics 365 Customer Insights - Journeys.
ms.date: 12/15/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - enduser
---

# Set up session-level registration

Session-level registration allows event organizers to let attendees assemble their own event agenda by choosing from all available sessions. In most ways, events with session-level registration work the same as those with event-level registration, but there are a few key differences, as outlined in the following table. Keep reading this article for more information about these differences.

| Feature                               | Event-level registration                      | Session-level registration                                    |
|---------------------------------------|-----------------------------------------------|---------------------------------------------------------------|
| Session selection during registration | Preconfigured: No specific session selection. | Customized: Registrants choose exactly the sessions they want.|
| Registration list                     | Available on the event record only.           | The event record lists each contact that registered for at least one session for that event; each session record shows registrations for that session. |

## Enable session-based registration

1. Go to **Settings** and select **Feature switches**.
2. Enable the **Enable session level registration in Real-time Journeys** feature toggle in the **Event management** section.

<img width="296" alt="image" src="https://github.com/MicrosoftDocs/customer-insights/assets/123373049/4263424f-015c-4e13-ac37-090e39df67f4">

## Use session-level registration

To use session-based registration, start by [setting up the event](set-up-event.md) as usual, including basic settings and session schedule, but then go to the **Agenda** tab for the event and set **Allow registrants to create their own** agenda to **Yes**.

:::image type="content" source="media/journeys-session-enable.png" alt-text="Enable session-level registration in real-time journeys events.":::

It’s important to note that session level registration requires the registration form to include the sessions. This is done by using the **Sessions** element in the form editor so that attendees can see the sessions and have the option to sign up for the sessions they select. 

![image](https://github.com/MicrosoftDocs/customer-insights/assets/123373049/6ef45802-d08b-4be5-8798-ae28fa40efba)

To access the registration form for the event, select the event, then go to **Website and form** and select the **Registration form**. 

![image](https://github.com/MicrosoftDocs/customer-insights/assets/123373049/a62f2c06-e2fc-48ec-835a-696cdedb53b0)

This opens a special version of the form editor that has extra elements for your event including the **About**, **Sessions**, and **Speakers** elements.

When session-level registration is enabled for an event (allow registrants to create their own agenda), the registration form that has session tiles in it, automatically allows the attendees to select the sessions they're interested in.

**Session Capacity Utilization:** Additionally, session capacity can be allocated to sessions with limited seating, by navigating to Session > Summary > Maximum session capacity:

![image](https://github.com/MicrosoftDocs/customer-insights/assets/123373049/269a71f1-5774-4cf9-9e2f-539c47016b19)

> [!WARNING]
> To ensure successful registration for an event with a custom agenda, at least one session must be published and available for selection (with seats available).

## View and edit event session registrations

The method to view and edit registration details for a session-level event depends on whether you want to view all registrations for the event or view registrations for a specific session:

- To view all registrations for the event (people who registered for at least one session), open the relevant event record, go to the **Registration and attendance** tab, and scroll to the **Event registration** section. You can also add or remove registrations from here.
- To view all registrations for a specific session, open the relevant event record, go to the **Agenda** tab, scroll to the **Sessions** list, and select a session. In the open session record, go to the **Registration and attendance** tab and scroll to the **Sessions registrations** list. You can also add or remove registrations from here.
