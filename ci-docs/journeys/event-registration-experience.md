---
title: Create event registration experience in Customer Insights - Journeys
description: Build event registration experience using registration forms in Customer Insights - Journeys Event Management.
ms.date: 1/13/2025
ms.topic: article
author: petrjantac
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Create a comprehensive event registration experience

The event registration experience enables new attendees to register for events seamlessly. It's crucial to ensure the registration process is smooth while collecting all necessary information. The registration experience is powered by the [registration form](event-registration-experience.md#event-registration-form), a type of [Customer Insights - Journeys form](real-time-marketing-form-overview.md).

There are various options how to build event registration experience:

- Registration form hosted as a standalone page—a single page containing the registration form with all details about the event. The page is hosted on Customer Insights infrastructure and no extra license is needed. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).
- Registration form embedded into your website—you can embed the event registration form into your own website. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).
- Registration portal on Power Pages—you can use the event registration template to build a website using Power Pages Studio.
  > [!NOTE]
  > As of January 2025, this feature is not available. General availability is scheduled soon. 
- Custom solution using events API. For more information, see [Using events API in real-time journeys](developer/using-rtm-events-api.md).

## Event registration form

The event registration form can dynamically display the following event-related information:

- Name of the event.
- Description of event including the date, time, location, and other information.
- List of speakers in the event.
- List of sessions—you can enable session registration or show the read-only list of sessions.

> [!TIP]
> A single registration form can be used for multiple events. This event-related information is dynamically updated based on the *readableEventId* parameter provided in the page URL.

The event registration forms can be created or updated using the form editor. For more information, see [Create forms in Dynamics 365 Customer Insights - Journeys](real-time-marketing-form-create.md).

> [!TIP]
> You can enable the [Form prefill](real-time-marketing-form-prefill.md) feature so that existing users don't have to reenter known information.
