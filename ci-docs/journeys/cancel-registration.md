---
title: Set up event registration cancellation
description: Learn how registered attendees can cancel registration in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/03/2025
ms.topic: how-to
author: terezakirk
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Set up event registration cancellation

Event registration cancellation lets event organizers and attendees cancel event registrations in Customer Insights - Journeys. With event registration cancellation, event organizers and attendees can:

- **[Add a cancellation link directly in registration confirmation emails](#add-a-cancel-registration-button-to-event-email)**: Attendees select the link to go to a standalone cancellation page.
- **Enable self-service cancellation**: Users cancel their registration without signing in or contacting support.
- **[Manually cancel their event registrations](#cancel-registration-manually)**: The event organizer cancels a registration.

## Add a cancel registration button to event email

Organizers set up a cancellation flow by adding a cancel registration button to an event registration confirmation email.

To add a cancel registration button to an event registration confirmation email:

1. Add a **Button** element to the email.
1. Select **Edit link**, and link to **Cancel event registration**.
1. Choose whether to link the canceled registration to a specific event or another source.
1. Enter the **link alias**.
1. Select **Insert**.

When the attendee receives the email and selects the cancel registration button, a standalone page opens. If the event registration is linked to sessions, the sessions the attendee signed up for are listed. Attendees can cancel specific session registrations or the entire event registration. 

## Cancel registration manually 

If your attendee can no longer attend an event and informs you through email or a phone call, you can manually cancel event registration by going to the **Registration and attendance** tab. Here, you can select the relevant registrations and select **Cancel registrations** on top of the grid.

[!INCLUDE [footer-include](./includes/footer-banner.md)]