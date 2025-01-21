---
title: Manage attendee logistics and accommodation availability in outbound marketing
description: How to manage event logistics (including vendors, hotels, room allocations, and reservations) in outbound marketing.
ms.date: 08/21/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing
---

# Manage attendee logistics and accommodation availability in outbound marketing

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Use the entities in the **Logistics** area to provide information that can help attendees from farther away to plan accommodation for their trip. Register local hotels, record their contact information, allocate sets of rooms that will be made available to attendees, and take reservations for the allocated rooms. You can also register various other types of attendee-facing vendors here, such as airlines, car rentals, food caterers, and more.

Logistics features are mostly informational, and they are not exposed directly to attendees through the standard event website. For example, you can enter hotel reservations in Dynamics 365 Customer Insights - Journeys based on communications you've had with attendees, but you'd still need to contact the hotel to let them know about the reservations.

Use the following entities of the [Events work area](open-events.md) to record and provide logistics services for attendees:

- **Events** > **Logistics** > **Event Vendors**: Enter and view event-vendor details here. Each event vendor must be associated with an account (external company) already recorded in your system. You can assign each vendor a type, such as hotel group, airline, car rental, and so on. 
    > NOTE
    > A *hotel group* is typically a company that operates a chain of hotel properties under the same name, such as Marriott. You can associate individual hotels with the hotel group type, as explained below. 
- **Events** > **Logistics** > **Hotels**: Enter and view details about specific hotel properties here. You can associate each hotel record with a contact from your database, so you'll know who to call if you have any questions for the hotel. You can associate the hotel record with a hotel group (event vendor) if the property is part of a group. The hotel group and contact details are shown here, if they are defined. You must always specify the hotel's address as part of its record. You can also view and add room allocations for the current hotel here.
- **Events** > **Logistics** > **Hotel Room Allocations**: Room allocations represent a block of rooms that the hotel has agreed to make available during your event. Each room allocation record specifies the number of rooms allocated and the type of rooms they are (single, double, or suite). Each allocation must be associated with a hotel that is registered in your database. If you have allocated several different room types in the same hotel, you must set up a separate allocation for each type. You can also view and add room reservations associated with the current allocation here.
- **Events** > **Logistics** > **Hotel Room Reservations**: Here you can reserve rooms for attendees from among the rooms you have allocated. More information: [Book hotel rooms for staff, speakers, and guests](invite-register-house-event-attendees.md#book-hotel-rooms-for-staff-speakers-and-guests)

[!INCLUDE [footer-include](./includes/footer-banner.md)]