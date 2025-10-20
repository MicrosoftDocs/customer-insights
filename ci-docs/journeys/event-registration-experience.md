---
title: Create an event registration experience in Customer Insights - Journeys
description: Build a seamless event registration experience using Customer Insights - Journeys. Learn how to create and manage registration forms.
ms.date: 10/20/2025
ms.topic: article
author: petrjantac
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:01/23/2025
---

# Create a comprehensive event registration experience

The event registration experience enables new attendees to register for events seamlessly. It's crucial to ensure the registration process is smooth while collecting all necessary information. The registration experience is powered by the [registration form](event-registration-experience.md#event-registration-form), a type of [Customer Insights - Journeys form](real-time-marketing-form-overview.md), or by the events API. For more information, see [Using the events API in real-time journeys](developer/using-rtm-events-api.md).

## Building a single registration page versus an event portal

You can build an event registration experience as a single registration page or as an event portal.

### Single registration page

- **Registration form hosted as a standalone page**: A single page has the registration form and all event details. The page is hosted on Customer Insights infrastructure and doesn't require an extra license. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).
- **Registration form embedded into your website**: You can embed the event registration form into your own website. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).

### Event registration portal

- **Registration portal on Power Pages**: You can use the event registration template to build a website using Power Pages studio. For more information, see [Build an event portal using Power Pages](event-portal-template.md).
- **Registration portal on your own domain built with the web application**: Use the out-of-box web application to build a registration portal hosted on your own domain. For more information, see [Create an event portal on your website using the web application](developer/rtm-event-portal-webapp.md).
- **Custom solution using the events API**: For more information, see [Using the events API in real-time journeys](developer/using-rtm-events-api.md).

:::image type="content" source="media/publishing-web-application.png" alt-text="Screenshot of selecting an event portal using the web application in a dropdown." lightbox="media/publishing-web-application.png":::

## Event registration form

For all publishing options mentioned above, except for a custom solution using the events API, registration uses the registration form. Marketing and event registration form types are similar. All features of marketing forms apply to event registration forms, except for audience configuration. Event registration forms only target a contact audience. Event registration forms have extra features like dynamic components that show a list of sessions, speakers, or event details. Event registration forms also create event registration records and use a different publishing user interface.

Event registration forms dynamically display the following event-related information:

- Name of the event.
- Description of the event including the date, time, location, and other information.
- List of speakers in the event.
- List of sessions. You can enable session registration or show the read-only list of sessions.
- List of event passes.
  
> [!TIP]
> You can use a single registration form for multiple events. The event-related information updates dynamically based on the `readableEventId` parameter in the page URL.

### Types of registration forms

There are two default event registration forms:

1. Default registration form
1. Default registration form with sessions

Your newly created form is automatically configured according to the default configuration. To make changes, ask your administrator to update the [default configuration](real-time-marketing-form-global-settings.md), which includes target audience, matching of existing records, and other important settings. Event registration forms can be created or updated using the form editor. For more information, see [Create forms in Dynamics 365 Customer Insights - Journeys](real-time-marketing-form-create.md).

> [!IMPORTANT]
> Make sure the domain where you embedded your form is allowed for external form hosting. If the domain isn't allowed for external form hosting, the form isn't rendered on your web page and all form submissions are rejected. For more information, see [Authenticate your domains](domain-authentication.md).
>
> The out-of-the-box domain for a standalone page is enabled by default. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).

> [!TIP]
> Enable the [form prefill](real-time-marketing-form-prefill.md) feature so existing users don't have to reenter known information.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
