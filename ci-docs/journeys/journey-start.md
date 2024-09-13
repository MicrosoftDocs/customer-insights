---
title: Journey start
description: An overview of the Journey start configuration in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/12/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Journey start

The journey start configuration lets you define how customers can start the journey.

## Trigger-based journey

- **Trigger to start the journey**: Customers start the journey as soon as the selected trigger occurs.  
- **Repeating the journey**: Lets you configure how soon customers can repeat the journey if the trigger to start the journey occurs again. You can allow customers to repeat the journey immediately, or only allow them to repeat the journey after a delay interval.
- **Exclude this segment**: Members of this segment won't be allowed to start the journey. This is an easy way to filter out certain segments of customers from starting the journey, even if they performed the trigger to start the journey.  
- **Journey Timing**: Lets you specify the time window in which customers can start the journey. Customers must perform the journey start trigger after the start time to enter the journey. No new customers will be allowed to start the journey after the end time. The end time only affects when customers can start the journey. If a customer is already in the journey, they'll be allowed to continue the journey even after the end time.
- **Handling unresolved profile**: This option is only available for trigger-based journeys that target Customer Insights - Data profiles. It takes time to create a full Customer Insights - Data profile. If the full profile isn’t available at the time the person triggers the journey, they can either start the journey immediately using defaults for any missing profile data or wait for the full profile to be available before starting the journey. To successfully communicate with someone without a profile, the trigger must specify email (contactpoint_email) or phone (contactpoint_phone) attributes. See [Create a custom trigger](real-time-marketing-custom-triggers.md). <br>
For journeys such as sending purchase order confirmations, both new customers and existing customers can trigger the journey. A new customer may not have a full profile when they make the purchase. By selecting the option to start the journey immediately even if the full profile isn't available, you can ensure new users get the order confirmation immediately without having to wait. All profile attributes for these new users will be treated as empty, so it's important to always include default fallbacks in personalized content as well as attribute branches.

## Segment-based journey

- **Audience**: The audience property lets you specify the segment of people that start the journey. Segment-based journeys [support segments from outbound marketing as well as segments created in Dynamics 365 Customer Insights - Data](real-time-marketing-segments.md). The journey uses audience data based upon the segment selected. For example, if the journey is started with an outbound marketing segment that contains a segment of **Contacts**, the journey uses Contacts as its Audience data. Similarly, if the journey is started using a Customer Insights - Data segment that is a segment of **Customer Profiles**, the journey uses Customer Profile as its Audience data. Once an audience segment has been selected, all other segments used in the journey must be of the same type (segment from outbound marketing or Customer Insights - Data segment).
- **Exclude this segment**: Members of this segment won't be allowed to start the journey. Specifying an exclusion segment lets you remove anyone from the Audience that starts the journey.
- **Frequency**: Lets you specify whether the journey should repeat.
  - *One time*: One time journeys run only once with a static audience segment. This is useful for scenarios like one-time email blasts that are sent on a specific date to a fixed set of customers.
  - *Ongoing*: Ongoing journeys run only once with a dynamic audience segment. This is useful for scenarios like nurture campaigns where anyone who gets added to the audience segment can start the journey as soon as they're added to the segment.
  - *Repeating*: These journeys repeat based on the time interval specified. Every time the journey repeats, all the members of the audience segment go through the journey. If any new members get added to the segment between the repeat interval, those new members will only go through the journey the next time the journey repeats. This type of journey is useful for scenarios like renewal reminders, where you might want to send people through the journey every time they're up for a renewal.

[!INCLUDE [footer-include](./includes/footer-banner.md)]