---
title: Set up event passes
description: Learn how to set up event passes for paid events in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/06/2025
ms.topic: article
author: terezakirk
ms.author: terezakirk
search.audienceType: 
  - admin
  - enduser
---

# Set up event passes 
Event passes act as tickets that grant attendees access to your event and its sessions or tracks. Passes are optional, but they’re essential if you want to manage paid access, session-level permissions, or special categories of registrations (e.g., VIP, sponsors). This feature is in public preview. To enable the feature please navigate to Settings > feature switches and under Event management section, enable the toggle "Enable payments in Real-time Journeys".
[!INCLUDE preview-note]
[!IMPORTANT] Please note that with October release, the payment gateway support was only released for registration experiences built using the Event API. With November release, the support for selection of event passes will be added to Real-time marketing Registration forms.

## What are event passes?

Passes can be sold or given away to control access and capacity limits to your event and its sessions. Each pass type can:
- Apply to a specific event.
- Include name, pricing, description and allocation limits.
- Control access to specific sessions.

For each assigned pass, Customer Insights – Journeys generates an attendee pass with unique ID and a unique QR code for check-in and attendance tracking. 

## How to set up event passes
Go to the event record → Passes tab. Click on + New Pass to create a new pass through quick create form, where you will define:
- Name - Pass name, this is how the pass will be displayed to your attendees through registration form
- Number of passes allocated - Number of passes that are available for attendees to select and purchase. Set Passes Allocated to a positive number to make it visible on the event website.
If allocation = 0, the pass remains hidden (useful for VIP or draft passes).
- Pass price - pass price in a currency defined in your organisation settings and on Additional information tab for your event
- Description - optional field that can help attendee understand what is included in the pass price

Once the pass is created you can add eligible sessions to each pass by opening the pass record and assigning available sessions (if applicable). The pass - session relationship helps event planners and attendees alike understand, which pass grants access to which session.

## How to set up payment gateway 
If you want your attendees to pay for the selected passes through an online gateway, your organization admin will be able to set up the payment provider in Settings > Event Management > Payment providers. This set up does require some developer assistance. for more information, visit: [Set up payment gateway integration](payment-gateway-integration.md)
Once the payment gateway is set up by your admin, you can enable the Payment gateway in the Passes tab. Set the toggle to "Yes" and select the Payment provider of your choice. This will ensure that once your attendees select their pass, they will be redirected to a payment gateway of your choice to complete the purchase.

## How the payment processing works
Once the registration with selected pass is submitted, the system creates a reservation which ensures that the capacity of the event and capacity of the pass is alocated to this registration while the payment is being processed. The admin will define a specific amount of time before the payment links expire, if the payment is successful before this time, the registration is confirmed and the attendee pass is allocated. 

If the payment is not successful before the time out period is reached, the reservation is cancelled, the registration is not successful and the capacity of the event and of the pass is increased by +1. 

## Viewing sold passes 
To see how many passes are already allocated, you can navigate to the Passes tab and in the column "No. of passes sold" you will see the exact number of sold passes. Additionally, if you navigate to the Registration and Attendance tab, you can see a new column "Pass" added where you can see the name and price of the pass the attendee purchased. 

Finally, to view the Attendee pass for each individual registration, click to the event registration and on the General tab, you can see "Attendee passes" section with unique ID for the attendee pass associated with this registration. 




