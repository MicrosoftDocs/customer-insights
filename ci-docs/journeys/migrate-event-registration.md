---
title: Migrate outbound marketing event registration to real-time journeys
description: Learn how to migrate outbound marketing event registration to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 02/06/2025
ms.topic: upgrade-and-migration-article
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:02/06/2025
---

# Migrate outbound marketing event registration to real-time journeys

After the outbound marketing module is removed from Customer Insights - Journeys, it will be no longer possible to create outbound marketing events or to register for outbound marketing events. You can start building events in real-time journeys, but this new type of event requires a different registration process.

There were multiple options on how to build event registration experience in outbound marketing. Each of these has a slightly different migration path:

1. Event portal hosted on Power Portals.
1. Event portal *not* hosted on Power Portals.
1. Outbound marketing form for event registration published in an outbound marketing page.
1. Custom solution using the outbound marketing event management API, not using an Angular app.

The next sections detail each outbound marketing event registration experience and how to transition them to real-time journeys events.

## Event portal hosted on Power Portals

The event portal is built on an Angular app, which will be deprecated along with outbound marketing. The infrastructure on Power Portals used for the Angular app hosting will also be deprecated with outbound marketing.

The recommended migration path is to build a new event registration website using Power Pages. There's a new event registration website available for Power Pages studio, which lets you build a registration experience that aligns with your brand identity. The new event registration website has many advantages compared to the outbound event portal, including:

- Edit the website design and layout using the visual editor in Power Pages studio.
- Build multiple event registration websites.

## Event portal *not* hosted on Power Portals

If you're currently hosting the Angular app event portal on your own infrastructure (not using Power Portals), you can keep using it but you need to maintain the app on your own. There will be no support for the Angular app.

The recommended migration path is to build a new event registration experience using the new code snippet listing all your events and the real-time journeys event registration form. The code snippet listing your events can be used on the main page where you showcase all your events. The real-time journeys event registration form is reusable for multiple events and can list all sessions, speakers, and information associated with the selected event. You can create one registration page where you embed the real-time journeys event registration form. The registration form reads the `readableEventId` parameter from the URL to dynamically render details about the selected event.

An alternative is to build a new event registration website using Power Pages studio or use the provided Power Pages template, as described in the [previous section](migrate-event-registration.md#event-portal-hosted-on-power-portals).

## Outbound marketing event registration marketing form

Outbound marketing forms are being deprecated along with the outbound marketing module.

The recommended migration path for event registration marketing forms is to replace them with real-time journeys event registration forms. Real-time journeys event registration forms can be embedded into your website, embedded within Power Pages, or hosted as standalone pages. Learn more: [Open the event management work area](open-events.md).

## Custom solution using the outbound marketing event management API

The outbound marketing event management API is being deprecated along with the outbound marketing module.

The new event management API in real-time journeys is backward compatible. It lets you list all events (outbound marketing and real-time journeys) and enables registration for both types of events. You can either adjust your user interface to use the real-time journeys event registration endpoints or embed an event registration form into your website to enable registration for real-time journeys events. Learn more: [Using the events API in real-time journeys](./developer/using-rtm-events-api.md).

> [!NOTE]
> The outbound marketing-related flow in the new real-time journeys event API is being deprecated along with the outbound marketing module.

## Can I keep using the Angular app after outbound marketing is removed?

Out of the box, the outbound Angular portal doesn't work with real-time journeys. You can make it work with some modifications, but we don't recommend continuing to use the outbound Angular portal. After the outbound module is deprecated, the Angular app will no longer be supported and there will be no future security updates. If your Angular app is hosted on Power Portals, you'll also need to migrate the portal to a new data model, as the old data model will be deprecated.

If you still want to use the Angular portal despite the risks and limitations above, you can rebuild the Angular app to use the new real-time journeys event management API for the “list of events” functionality. Learn more: [Using the events API in real-time journeys](./developer/using-rtm-events-api.md).

For the event registration functionality, there are two options:

1. Embed a real-time journeys event registration form into your app. This is an easier option and you'll automatically benefit from all the new registration form features like wait list and custom fields.
1. Keep the existing registration experience and route it to the new API endpoints. This requires significant effort and testing. You'll also need to change your app to account for new features.

## Marketing pages

After outbound marketing is removed, marketing pages hosted on Power Portals will still be online, but the following parts of the marketing pages won't work:

- Outbound marketing forms
- Outbound marketing web tracking and all page visit insights
- Marketing page lifecycle
- Marketing page editor

The underlying Power Pages data model used to host the marketing pages will be deprecated, which means that you'll need to migrate the whole portal to a new data model. Given the limitations, we strongly recommend rebuilding outbound marketing pages as a native Power Pages website. You can embed a real-time journeys marketing form into the Power Pages website. For a simple landing page with a form, you can also build a real-time journeys form and host it as a standalone page.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
