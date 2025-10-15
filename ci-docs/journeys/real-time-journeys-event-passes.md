---
title: Set up event passes (preview)
description: Discover how to create and manage event passes for paid events in Dynamics 365, including pricing, allocation, and session-level access control.
ms.date: 10/15/2025
ms.topic: article
author: terezakirk
ms.author: terezakirk
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - enduser
---

# Set up event passes (preview)

[!INCLUDE [Preview banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Event passes act as tickets that grant attendees access to your event and its sessions or tracks. Passes are optional, but they’re essential if you want to manage paid access, session-level permissions, or special categories of registrations (for example, VIP or sponsors).

To enable event passes, go to **Settings** > **Feature switches**, and under **Event management**, turn on the **Enable payments in real-time journeys** toggle.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

> [!IMPORTANT]
> In the October 2025 release, payment gateway support is only in registration experiences built using the [events API](developer/using-rtm-events-api.mdusing-rtm-events-api.md). In the November 2025 release, support for event passes is in real-time journeys registration forms.

## What are event passes?

Passes let you control who can attend your event and its sessions, and help you manage capacity. Each pass type can:
- Apply to a specific event.
- Include a name, pricing, description, and allocation limits.
- Control who can attend specific sessions.

For each assigned pass, Customer Insights – Journeys creates an attendee pass with a unique ID and QR code for check-in and attendance tracking.

## Set up event passes

Go to the **Event record** > **Passes** tab. Select **+New Pass** to create a new pass using the quick create form. Define the following fields:
- **Name**: Pass name. This is how the pass shows to attendees in the registration form.
- **Number of passes allocated**: Number of passes available for attendees to select and buy. Set **Passes allocated** to a positive number to make it visible on the event website. If the allocation is zero, the pass stays hidden (useful for VIP or draft passes).
- **Pass price**: Pass price in the currency set in your organization settings and on the **Additional information** tab for your event.
- **Description**: Optional field that helps attendees learn what's included in the pass price.

After you create the pass, open the pass record and assign eligible sessions (if needed). The pass and session relationship helps event planners and attendees learn which pass lets them join which session.

## Set up a payment gateway

To let attendees pay for selected passes through an online gateway, your organization admin sets up the payment provider in **Settings** > **Event management** > **Payment providers**. This setup needs some developer help. For more information, see [Set up payment gateway integration](developer/payment-gateway-integration.md).

After your admin sets up the payment gateway, enable it in the **Passes** tab. Set the toggle to **Yes**, and select your payment provider. When attendees select a pass, they're redirected to your payment gateway to finish the purchase.

## How payment processing works

When you submit a registration with a selected pass, the system creates a reservation to allocate event and pass capacity while payment is processed. The admin sets how long the payment link is valid. If payment is successful before the time expires, the registration is confirmed and the attendee pass is allocated.

If payment isn't successful before the time expires, the reservation is canceled, the registration isn't successful, and the event and pass capacity increase.

## View sold passes

To check how many passes are allocated, go to the **Passes** tab. In the "No. of passes sold" column, you see the number of sold passes. Also, if you go to the **Registration and Attendance** tab, a new column, "Pass," shows the name and price of the pass the attendee bought.

To view the attendee pass for an individual registration, select the event registration. On the **General** tab, check the "Attendee passes" section for the unique ID linked to the attendee pass for the registration.

[!INCLUDE [footer-include](./includes/footer-banner.md)]