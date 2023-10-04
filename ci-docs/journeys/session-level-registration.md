---
title: Set up session-level registration
description: Describes how to set up session-level registration and how it differs from event-level registration in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/22/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Set up session-level registration

[!INCLUDE [consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> To use event management in the real-time journeys area of Customer Insights - Journeys, you must enable the feature switch. To enable the feature switch:
>
> 1. Go to **Settings** > **Overview** > **Feature switches**.
> 1. Enable the **Enable events creation in real-time journeys** feature switch toggle.

Session-level registration enables event organizers to give attendees the ability to assemble their own events from among all available sessions. In most ways, events with session-level registration work the same as those with event-level registration, but there are a few key differences, as outlined in the following table. Keep reading this topic for more information about these differences.

|   | **Event-level registration** | **Session-level registration** |
| --- | --- | --- |
| **Session&nbsp;selection&nbsp;during registration** | Preconfigured: Events can offer multiple passes, each of which provides access to a preselected collection of sessions. | Customized: Registrants choose exactly the sessions they want. |
| **Maximum capacity**<br/>(On-site only, not for webinar or hybrid events) | Set at the event level | Set at the session level |
| **Waitlists**<br/>(On-site only, not for webinar or hybrid events) | One waitlist per event | Individual waitlist per session |
| **Event passes** | Optional (required for online payment) | Not supported |
| **Online payment** | Optional, per pass | Not supported |
| **Registration list** | Available on the event record only | The event record lists each contact that registered for at least one session for that event; each session record shows registrations for that session. |

## Enable session-based registration

To enable session-based registration, start by [setting up the event](set-up-event.md) as usual, including basic settings and session schedule, but then go to the **Agenda** tab for the event and set **Allow registrants to create their own agenda** to **Yes**.

> [!NOTE]
> As mentioned in the introduction to this topic, session-based registration isn't supported for events that have passes defined. If you don't see the **Allow registrants to create their own agenda** setting, then it might be because you have one or more passes defined (you can see these on the **Registration and attendance** tab). If you define a pass after enabling session-based registration, then session-based registration will be disabled automatically.

## Set the maximum capacity for each session

With session-based registration, the system tracks registrations for each session rather than for the event as a whole. When session-based registration is enabled, the session capacity is a required field and is also requested by the quick-create form for sessions. However, if you enable session-based registration after creating the session, you may need to go back and set the capacity for each session.

When the system has received enough registrations to fill the capacity of the session, it will mark that session as sold out. If you enabled the waitlist, then registrants can choose to join the waitlist, but if you haven't then they won't be able to self-register for any sold out sessions using the event website. (Users of Customer Insights - Journeys, however, can overrule the capacity limit by [adding new registrations directly](invite-register-house-event-attendees.md) into the system.)

To set or change the maximum capacity of a session:

1. Open the event record that that session belongs to.
2. Go to the **Agenda** tab.
3. Find the **Sessions** section of the **Agenda** tab and select a session.
4. In the **Venue** constraints area, enter a value for the **Maximum session capacity**.

**Note** : If you fill out any of the fields in the **Location area** ( **Building** , **Room** , and/or **Layout** ), then the initial value for the **Maximum session capacity** is automatically taken maximum capacity set for the most specific location (if available).

## View and edit event and session registrations

To view and edit registration details for a session-level event:

- To view all registrations for the event (people who registered for at least one session), open the relevant event record, go to the **Registration and attendance** tab and scroll to the **Event registration** section. You can also add or remove registrations from here.
- To view all registrations for a specific session), open the relevant event record, go to the **Agenda** tab, scroll to the **Sessions** list and select a session. In the open  session record, go to the Registration and attendance tab and scroll to the **Sessions registrations** list. You can also add or remove registrations from here.

## Session-level waitlists

Waitlists are not supported in Customer Insights - Journeys event management.

[!INCLUDE [footer-include](./includes/footer-banner.md)]