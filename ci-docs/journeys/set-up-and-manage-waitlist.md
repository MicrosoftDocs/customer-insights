---
title: "Preview: Set up and manage event waitlist"
description: Ability to register interested attendees on a waitlist in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/11/2025
ms.topic: article
author: terezakirk
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Preview: Set up and manage event waitlist

> [!NOTE]
> Due to release rollout delays, this feature will be available in the last week of March. You will be able to see "Waitlist in Real-time journeys" in Feature switches in the Settings section, once the feature is available in your region.

> [!IMPORTANT]
> A preview feature is a feature that is not complete but is made available before it’s officially released so customers can get early access and provide feedback. Preview features aren’t meant for full use and may have limited or restricted functionality.
>
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support will not be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data, or other data that are subject to legal or regulatory compliance requirements.

Ensuring marketing events are filled to capacity is crucial for success and return on investment. To encourage a high turnout for marketing events, you can now enable waitlist registrations, which ensures spots are filled when registered attendees cancel. By setting the capacity for events and sessions, prospective attendees are placed on a waitlist when events and sessions are full. Should a slot open, the system automatically registers the individual next on the waitlist. That individual then automatically receives registration confirmation and personalized event information, ensuring your event is filled to capacity.

## How the waitlist works

You can assign a maximum capacity to each event and/or session when needed. When the number of registrations reaches that capacity, the system won't accept any more active registrations, but you can still allow new registrants to add themselves to a waitlist. The waitlist holds a list of contacts who submitted a registration through the event website after an event or session was fully booked. The waitlist registers the time and day that each contact registered, so when space becomes available, contacts are either automatically registered or offered an invitation to register in the same order that they joined the waitlist. 

**When new space becomes available, the waitlist reacts as follows:**

1. The oldest existing waitlist record is identified by checking the registration date/time.
1. One of the following occurs, depending on whether the contact is using automatic registration or not:
    - If the identified waitlist record has **Automatically register** set to **Yes**, then an event registration record is generated for the contact and the associated.
    - If the identified waitlist record has **Automatically register** set to **No**, then these contacts should be invited to sign up/confirm their interest in the event. To automate the workflow, you should create a segment that finds these contacts (where (Automatically-register = No) and (Invited = Yes)) and then use a customer journey to send them an email that invites them to visit the event website to accept the slot.
1. All registrations that are placed on the waitlist will have a status reason "Waitlisted" and once the spot becomes available, the status reason will either automatically or manually change to "Registered".

## Enable a waitlist 

### Enable a waitlist for an event

To enable or disable the waitlist for any event:
1. Open the Events work area, go to the events list (Events > Event > Events), and then open or create an event.
1. Open the General tab and find the Capacity area.
   :::image type="content" source="media/waitlist settings.png" alt-text="Event general tab settings screen" lightbox="media/waitlist settings.png":::

1. Make the following settings:
  - **Maximum event capacity** (event-level registration only): Enter the maximum number of people who can attend your event. The waitlist will only take effect after this number of contacts have registered. If you are using session-level registrations, you can also set up a waitlist for each session, see the section below.
    - **Waitlist this event:** Set to **Yes** to enable the waitlist feature for an event.
    - **Auto-register waitlisted contacts**: set this to **Yes** to automatically register the next contact in line when space becomes available. When this is set to **No**, then you will have to manually invite waitlisted contacts to confirm their interest and once they do, you can change the status reason of their registration from "Waitlisted" to "Registered"
   :::image type="content" source="media/media/waitlistedmanualupdate.png" alt-text="Event general tab settings screen" lightbox="media/waitlistedmanualupdate.png":::

### Enable a waitlist for a session

If you are using [session-level registration]([url](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/real-time-journeys-event-session)), you can also use waitlisting for sessions. Waitlist for sessions can be used together with event waitlist or just for individual sessions. 

To enable or disable the waitlist for a session:
1. Open the Events work area, go to the events list (Events > Event > Events), and then open or create an event. Next create a Session under Agenda tab.
1. Open the Summary tab and find the Capacity area.
1. Make the following settings:
    - **Maximum session capacity**: Enter the maximum number of people who can attend your session. The waitlist will only take effect after this number of contacts have registered.
    - **Waitlist this session:** Set to **Yes** to enable the waitlist feature for this session.
    - **Auto-register waitlisted contacts**: set this to Yes to automatically register the next contact in line when space becomes available. When this is set to No, then you will have to manually invite waitlisted contacts to confirm their interest and once they do, you can change the status reason of their registration from "Waitlisted" to "Registered"

> [!TIP]
> If you have used Waitlist in Outbound marketing in the past, it was not possible to use event and session capacity & waitlisting together. This has now changed in Real-time marketing so you can benefit from greater flexibility when setting up multi-session events.

### How does event & session waitlisting work together

Based on the set up you choose, event might have a larger capacity then individual sessions. In other scenarios, the capacity might be equal and each time, the waitlisting will behave slightly differently. Below are some common scenarios worth noting: 

1. **Event still has capacity but sessions do not**: i.e. Event has capacity a higher capacity and attendees can attend talks and networking opportunities, there is also a number of sessions with limited capacity such as roundtables and workshops, registration to sessions is optional.
    - Sessions might run out of capacity first and in this case registrants will see a "Join a waitlist" notification for the session that is out of capacity
    - Event still has capacity and will allow them to register
    - Upon registering, the attendees will see a summary confirming their event registration and waitlist registration for the sessions they were interested in
1. **Event is full but some sessions still have capacity**: i.e. Event and sessions' capacity is equal and not all session capacity was used when people registered for their events.
    - Registrants will be able to register for an event waitlist
    - When registering for waitlist, they will be able to pick the sessions they are interested
    - For sessions, that have capacity the session registration status will be "**On hold**" as **no attendee can be registered for a session without having secured spot in an event**
    - Once a spot opens up in an event, the attendee will be registered to an event and all of the respective sessions that were "On hold" for them
1. **Event is full and sessions are too**: i.e. Event and session capacity is equal, session registration is required.
    - Registrants will be able to register for an event and session waitlist
    - Given that neither event nor session capacity is available, both registrations will have a status "**Waitlisted**"
    - Registrants will only get registered once a spot opens up in the event. 

## View the waitlist

To see who is currently on the waitlist for any event or session:

1. Open the Events work area, go to the events list (Events > Event > Events), and then open the event.
1. If you are using session-level registration, then go to the the Agenda tab for the event and open the session you want to view.
1. Open the Registration and attendance tab for your selected event or session.
1. In the default system view called "Registration and attendance of Realtime events" you will be able to see a "**Status reason** column where you can see if the attendee is registered, waitlisted or if the registration was canceled. Event check-ins will continue to be recorded in its own table for now. 

