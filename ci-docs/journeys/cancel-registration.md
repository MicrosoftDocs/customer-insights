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

Set up event registration cancellation allows event organizers and attendees to cancel event registrations in Customer Insights - Journeys. Using set up event registration cancellation, event organizers and attendees can:

- **[Add a cancellation link directly in registration confirmation emails](#add-a-cancel-registration-button-to-event-email)**: Attendees can click the link to access a standalone cancellation page.
- **Enable self-service cancellation**: Event registration cancellation allows users to cancel their registration without needing to sign in or contact support.
- [Manually cancel event registrations](#cancel-registration-manuallycancel-registration-manually).

## Add a cancel registration button to event email

Organizers can set up a cancellation flow by adding a cancel registration button to an event registration confirmation email. 

To add a cancel registration button to an event registration confirmation email:

1. Add a button element to the email.
1. Link to "Cancel event registration."
1. Define if you want the cancel registration linked to a specific event or automatically set for all events.

Once the attendee receives the email and clicks the cancel registration button, a standalone page opens. If this event registration is also linked to sessions, the sessions the attendee signed up for are also listed. Attendees can cancel specific session registrations or the entire event registration. 

## Cancel registration manually 

If your attendee can no longer attend an event and lets you know via email or phone, you can also manually cancel event registration by going to the **Registration and Attendees** tab. Here you can select the relevant registrations and select "Cancel registration" on top of the grid.

[!INCLUDE [footer-include](./includes/footer-banner.md)]