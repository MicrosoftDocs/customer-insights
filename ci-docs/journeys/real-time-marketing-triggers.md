---
title: Customer Insights - Journeys triggers 
description: Learn about triggers in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/04/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Customer Insights - Journeys triggers

> [!Note]
> “Event triggers” are now called “triggers” in the app and documentation. This change avoids confusion when you reference event management functionality or trigger Customer Insights - Journeys.

Triggers control the flow of [trigger-based journeys](real-time-marketing-trigger-based-journey.md). They represent customer actions like downloading a whitepaper, submitting a form, or signing up for Wi-Fi. Triggers can also represent important business events, like shipping a purchase or finishing an enrollment process.

You can use triggers to start, continue, or stop a journey. For example:

- A **Contact created** trigger starts a journey to welcome a new user.
- An **Email opened** trigger sends a follow-up response in a journey that engages users by sending a promotional email.
- An **Order placed** trigger ends a journey designed to remind a customer to finish a purchase order.

## Trigger types

Customer Insights - Journeys has three types of triggers in the triggers catalog: custom triggers, interaction triggers, and business triggers.

### Custom triggers

Customer Insights - Journeys users define custom triggers. Custom triggers let you capture any customer action or significant business event.

Learn more, including important security notes for custom triggers, in [Custom triggers in Customer Insights - Journeys](real-time-marketing-custom-triggers.md).

### Interaction triggers

Interaction triggers represent customer interactions with journey elements like email, text message, and push channels. Use interaction triggers to start journeys, use them within the journey, or as a logical continuation of a previous step. For example, when a journey sends an email, triggers like *Email Link Clicked* or *Email Opened* are available to journey authors, so they can decide the next steps.

You can use all interaction triggers across different channels, like email, SMS, and push, to start a journey or branch within a journey.

### Business triggers

Business triggers represent changes in Dynamics 365 applications like Sales or Service. These changes can be the creation of a new record or an update to an existing one. The following business triggers are available by default:

- *Contact created*
- *Contact email address updated*
- *Contact address updated*
- *Contact phone number updated*
- *Lead created*
- *Incident created*
- *Opportunity created*
- *Marketing event check-in created*
- *Marketing event registration created*
- *Marketing event registration canceled*
- *Marketing form submitted*

You can also create your own triggers based on any Dataverse record change. Learn more: [Trigger a journey based on a Dataverse record change](real-time-marketing-dataverse-trigger.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
