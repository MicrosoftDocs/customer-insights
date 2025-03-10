---
title: "Preview: Set up and manage event waitlist"
description: Ability to register interested attendees on a waitlist in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/10/2025
ms.topic: article
author: terezakirk
ms.author: 
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Preview: Preview: Set up and manage event waitlist

> [!IMPORTANT]
> A preview feature is a feature that isn't complete but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.
>
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support will not be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data, or other data that are subject to legal or regulatory compliance requirements.

Ensuring marketing events are filled to capacity is crucial for success and return on investment. To encourage a high turnout for marketing events, you can now enable waitlist registrations, which ensures spots are filled when registered attendees cancel. By setting the capacity for events and sessions, prospective attendees are placed on a waitlist when events and sessions are full. Should a slot open, the system automatically registers the individual next on the waitlist. That individual then automatically receives registration confirmation and personalized event information, ensuring your event is filled to capacity.

## How the waitlist works
You can assign a maximum capacity to each event and/or session when needed. When the number of registrations reaches that capacity, the system won't accept any more active registrations, but you can still allow new registrants to add themselves to a waitlist. The waitlist holds a list of contacts who submitted a registration through the event website after an event or session was fully booked. The waitlist registers the time and day that each contact registered, so when space becomes available, contacts are either automatically registered or offered an invitation to register in the same order that they joined the waitlist. You can choose whether contacts will be automatically registered when space becomes available for them, or whether they should instead be sent an invitation to register manually.

When new space becomes available, the waitlist reacts as follows:

1. The oldest existing waitlist record is identified by checking the registration date/time.
1. One of the following occurs, depending on whether the contact is using automatic registration or not:
- If the identified waitlist record has Automatically register set to Yes, then an event registration record is generated for the contact and the associated waitlist record is deleted.
- If the identified waitlist record has Automatically register set to No, then the waitlist record has its Invited field changed from No to Yes to indicate that space is now available for that contact. You should create a segment that finds these contacts (where (Automatically-register = No) and (Invited = Yes)) and then use a customer journey to send them an email that invites them to visit the event website to accept the slot.
