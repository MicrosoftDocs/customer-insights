---
title: Create an event registration experience in Customer Insights - Journeys
description: Build a seamless event registration experience using Customer Insights - Journeys. Learn how to create and manage registration forms.
ms.date: 10/16/2025
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

The event registration experience enables new attendees to register for events seamlessly. It's crucial to ensure the registration process is smooth while collecting all necessary information. The registration experience is powered by the [registration form](event-registration-experience.md#event-registration-form), a type of [Customer Insights - Journeys form](real-time-marketing-form-overview.md) or the Event API [Using events API in real-time journeys](developer/using-rtm-events-api.md).

There are various options to build event registration experience depending if you want to build an single registration page or event portal.

**Single registration page:**
- **Registration form hosted as a standalone page**: A single page containing the registration form with all details about the event. The page is hosted on Customer Insights infrastructure and no extra license is needed. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).
- **Registration form embedded into your website**: You can embed the event registration form into your own website. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).

**Event registration portal:**
- **Registration portal on Power Pages**: You can use the event registration template to build a website using Power Pages studio. For more information, see [Build event portal using Power Pages](event-portal-template.md)
- **Registration portal on your own domain build with WebApp**: Use the out-of-box web application to build a registration portal hosted on your own domains. For more information, see [Create an Event Portal on your website using WebApp](developer/rtm-event-portal-webapp.md)
- **Custom solution using the events API**: For more information, see [Using events API in real-time journeys](developer/using-rtm-events-api.md).

:::image type="content" source="media/publishingwebapp.png" alt-text="Select Event portal using WebApp in a dropdown." lightbox="media/publishingwebapp.png":::

## Event registration form

For all of the publishing options mentioned above (aside from Custom solution using the Events API), the registration will be powered by the registration form. The marketing and event registration form types are similar. All features of marketing forms apply to event registration forms, except for audience configuration. Event registration forms can only target a contact audience. Event registration forms have some extra features like dynamic components to render list of sessions, speakers, or details about event. Event registration forms can also create event registration records. Event registration forms also have a different publishing user interface.

The event registration form is different because it can dynamically display the following event-related information:

- Name of the event.
- Description of the event including the date, time, location, and other information.
- List of speakers in the event.
- List of sessions. You can enable session registration or show the read-only list of sessions.
- List of event passes.
  
> [!TIP]
> A single registration form can be used for multiple events. This event-related information is updated dynamically based on the *readableEventId* parameter provided in the page URL.

### Types of registration forms
There are two default event registration forms: 
1. Default registration form
2. Default registration form with sessions

Your newly created form is automatically configured according to the default configuration. To make changes, ask your administrator to update the [default configuration](real-time-marketing-form-global-settings.md) which includes target audience, matching of existing records, and other important settings. Event registration forms can be created or updated using the form editor. For more information, see [Create forms in Dynamics 365 Customer Insights - Journeys](real-time-marketing-form-create.md). 

> [!IMPORTANT]
 > Make sure the domain where you embedded your form is allowed for external form hosting. If the domain isn't allowed for external form hosting, the form won't be rendered on your web page and all form submissions will be rejected. Learn more about [domain authentication](domain-authentication.md).
 > The out-of-box domain for a standalone page is enabled by default. [Learn more](real-time-marketing-form-create.md#publish-your-form)

> [!TIP]
> You can enable the [Form prefill](real-time-marketing-form-prefill.md) feature so that existing users don't have to reenter known information.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
