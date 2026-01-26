---
title: Set up event passes
description: Discover how to create and manage event passes for paid events in Dynamics 365, including pricing, allocation, and session-level access control.
ms.date: 01/26/2026
ms.topic: article
author: terezakirk
ms.author: terezakirk
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - enduser
---

# Set up event passes

Event passes act as tickets that grant attendees access to your event and its sessions or tracks. Passes are optional, but they're essential if you want to manage paid access, session-level permissions, or special categories of registrations (for example, VIP or sponsors).

To enable event passes, go to **Settings** > **Feature switches**, and under **Event management**, turn on the **Enable payments in real-time journeys** toggle.

## What are event passes?

Passes enable you to control who can attend your event and its sessions. They help you manage capacity and generate revenue from your events. Passes work with registrations through all available publishing options for your event, regardless of whether your attendees register through a form, a custom registration experience [built using the API](developer/using-rtm-events-api.md), or another method. For more information, see [Create a comprehensive event registration experience](event-registration-experience.md).

Each pass type can:
- Apply to a specific event.
- Include a name, pricing, description, and allocation limits.
- Control who can attend specific sessions.

For each assigned pass, Customer Insights – Journeys creates an attendee pass with a unique ID and QR code for check-in and attendance tracking.

## Set up event passes

Go to the **Event record** > **Passes** tab. Select **+New Pass** to create a new pass by using the quick create form. Define the following fields:
- **Name**: Pass name. This name shows to attendees in the registration form.
- **Number of passes allocated**: Number of passes available for attendees to select and buy. Set **Passes allocated** to a positive number to make it visible on the event website. If the allocation is zero, the pass stays hidden (useful for VIP or draft passes).
- **Pass price**: Pass price in the currency set in your organization settings and on the **Additional information** tab for your event.
- **Description**: Optional field that helps attendees learn what's included in the pass price.

After you create the pass, open the pass record and assign eligible sessions (if needed). The pass and session relationship helps event planners and attendees learn which pass lets them join which session.

## Add passes to a registration form

When you use a real-time journeys registration form to register attendees for your event, you see an element in the form editor called **Passes**. To add the passes element to your existing form, go to your event, select the **Form** tab, then select **Edit**. In the toolbox on the right-hand side, you see a section called **Events** and a new tile called **Passes**. 

:::image type="content" source="media/form-with-passes.png" alt-text="Screenshot of form editor and passes element." lightbox="media/form-with-passes.png":::

You can drag and drop the **Passes** element anywhere on the form. Once added, you can edit the properties of the element. In the panel on the right-hand side, you can change the order in which the passes are displayed, select which attribute you want to show to your attendees, and change the display style for the element. You can choose from a traditional dropdown or select a card style for a more modern look and feel.

:::image type="content" source="media/passes-settings.png" alt-text="Screenshot of passes element settings." lightbox="media/passes-settings.png":::

## Set up a payment gateway

To allow attendees to pay for selected passes through an online payment gateway, your organization admin needs to set up the payment provider in **Settings** > **Event management** > **Payment providers**. This setup requires some developer help. For more information, see [Set up payment gateway integration](developer/payment-gateway-integration.md).

After your admin sets up the payment gateway, enable it in the **Passes** tab of the event. Set the toggle to **Yes**, and select your payment provider. When attendees select a pass, they're redirected to your payment gateway to finish the purchase.

## How payment processing works

When you submit a registration with a selected pass, the system creates a reservation to allocate event and pass capacity while it processes payment. The admin sets how long the payment link is valid. If payment is successful before the time expires, the registration is confirmed and the attendee pass is allocated.

If payment isn't successful before the time expires, the reservation is canceled, the registration isn't successful, and the event and pass capacity increase.

## View sold passes

To check how many passes are allocated, go to the **Passes** tab. In the "No. of passes sold" column, you see the number of sold passes. If you go to the **Registration and Attendance** tab, a new column, "Pass," shows the name and price of the pass the attendee bought.

To view the attendee pass for an individual registration, select the event registration. On the **General** tab, check the "Attendee passes" section for the unique ID linked to the attendee pass for the registration.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
