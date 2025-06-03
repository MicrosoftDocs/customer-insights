---
title: "Set up event registration cancellation"
description: Learn how registered attendees can cancel registation in Dynamics 365 Customer Insights - Journeys.
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

With this feature, organizers can now:

- Add a cancellation link directly in registration confirmation emails: Attendees can click the link to access a standalone cancellation page.
- Enable self-service cancellation: The page allows users to cancel their registration without needing to log in or contact support.
- Alternatively use manual cancellation of event registrations.

## Add a cancel registration button to event email

Set up cancellation flow by adding cancel registration button to event registration confirmation email.  
- Add a button element to the email
- Link to "Cancel event registration"
- Define if you want this to be linked to a specific event or automatically set for all events

Once the attendee received this email and clicks on the cancel registration button, a standalone page will open up. If this event registration is linked to sessions as well, there will be a list of sessions the attendee signed up for, listed. Attendee can cancel specific session registrations or if the entire event registration should be cancelled. 

## Cancel registration manually 

If your attendee can no longer attend and lets you know via email or a phone, you can also cancel event registration manually by going to the **Registration and Attendees** tab, where you can select the relevant registrations and click on "Cancel registration" on top of the grid.
