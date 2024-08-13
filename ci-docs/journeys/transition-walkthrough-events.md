---
title: Transition event management
description: Learn how to transition event management capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/08/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition event management

> [!IMPORTANT]
> **[Outbound marketing](user-guide.md) will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Event management comprises three areas:
- Event setup (including tracks and sessions, speakers, registrants, etc.)
- Communication about events
- Publishing of information about events

More granularly, the event management areas can be broken down as follows:

| Event setup                                                       | Event communication                  | Event publishing          |
|-------------------------------------------------------------------|--------------------------------------|---------------------------|
| Events, speakers, tracks, sessions, registrants | Segments, emails, journeys | Forms, portal pages |

Creation and setup of events, tracks and sessions, speakers, and registrants is unaffected by the change to real-time journeys.

Communication about events is also largely unaffected by the transition to real-time journeys. New emails and journeys are required, but the process of inviting and registering attendees remains consistent. However, there are enhancements associated with the addition of triggers that should be considered when creating event invitation and registration real-time journeys.

Event-based communications in real-time journeys allow for more timely communication with attendees. This is illustrated below:

> [!div class="mx-imgBorder"]
> ![Transition event planning diagram.](media/transition-event-planning.png "Transition event planning diagram")

The one thing that changes with real-time journeys events is the publishing of event information now that the dependency on Power Pages is removed. With outbound marketing, Power Pages were used as a platform to present event data (sessions, speakers, etc.) and handle registrations.

With real-time journeys events, the Power Pages dependency changes and only the registration form is provided. Registration forms can be either self-hosted or embedded into a website. This allows you to create the online presence you require for events using your technology of choice while capturing event registrations into Customer Insights - Journeys. Your technology of choice can include Power Pages (as it did with outbound marketing) if so desired, but you need to create the necessary pages for the event.

> [!TIP]
> If you have questions or comments, visit the [Outbound to real-time transition community forum](https://community.dynamics.com/forums/thread/?partialUrl=Outbound-to-Real-Time-Transition)

## When to use real-time journeys and when to use outbound marketing for event management

Real-time journeys contains a subset of outbound event management features plus several improvements. The following table compares the real-time journeys and outbound marketing event management features.

|     Feature     |     Outbound marketing    |    Real-time journeys    |
|---|---|---|
|     Single session event    |     [Yes](set-up-event-outbound.md)    |     [Yes](set-up-event.md)    |
|     Multi-session event          |     [Yes](set-up-event-outbound.md#manage-event-sessions-and-speakers)    |     [Yes](set-up-event.md)    |
|     Session-level registration          |     [Yes](set-up-event-outbound.md#manage-event-sessions-and-speakers)    |     [Yes](real-time-journeys-event-session.md)    |
|     Recurring event    |     [Yes](event-recurring-outbound.md)    |     Planned    |
|     Event level templates    |     [Yes](event-templates-outbound.md)    |     Planned    |
|     Sessions, session tracks, speaker management    |     [Yes](set-up-event-outbound.md)    |     [Yes](set-up-event.md)    |
|     Venue management    |     [Yes](set-up-event-outbound.md#set-up-the-event-venue)    |     [Yes](set-up-event.md#set-up-the-event-venue)    |
|     Tracking sponsors    |     [Yes](manage-event-sponsorships-outbound.md)    |     [Yes](manage-event-sponsorships.md)    |
|     Creating Teams meetings/live events/webinars    |     [Yes](teams-webinar-outbound.md)    |     [Yes](teams-webinar.md)    |
|     Support for On24 and other generic webinar providers      |     [Yes](set-up-webinar-outbound.md)    |     Planned    |
|     Using marketing forms for registrations    |     [Yes](event-forms-outbound.md)    |     [Yes](real-time-marketing-form-create.md)   |
|     Event portal landing page    |    [Yes](set-up-event-portal-outbound.md)    |    Planned    |                     
|     Waitlist    |     [Yes](event-waitlist-outbound.md)    |     Planned    |
|     Payments    |     [Yes](event-payment-gateway-outbound.md)    |     Planned    |
|     Lead entity registration    |     [Yes](set-up-event-outbound.md#the-website-and-form-tab)    |     Planned    |
|     Custom registration fields    |     [Yes](custom-registration-fields-outbound.md)    |     Planned    |
|     Set registrations end date    |    Yes   |    Planned    |

[!INCLUDE [footer-include](./includes/footer-banner.md)]