---
title: Migrate event registration and marketing pages to real-time journeys
description: Learn how to set up event registration and marketing pages in Dynamics 365 Customer Insights - Journeys.
ms.date: 02/06/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - enduser
---

# Migrate event registration and marketing pages to real-time journeys

After the outbound marketing module is removed from Customer Insights - Journeys, it will be no longer possible to create outbound marketing events or to register for outbound marketing events. You can start building events in real-time journeys, but this new type of event requires a different registration process.

There were multiple options on how to build event registration experience in outbound marketing. Each of these has a slightly different migration path:

1. Event portal hosted on Power Portals
1. Event portal *not* hosted on Power Portals
1. Outbound marketing form for event registration published in an outbound marketing marketing page
1. Custom solution using the outbound marketing event management API, not using an Angular application

The next sections detail each outbound marketing event registration experience and how to transition them to real-time journeys events.

## Event portal hosted on Power Portals



## Event portal *not* hosted on Power Portals



## Outbound marketing event registration marketing form



## Custom solution using the outbound marketing event management API



## Can I keep using the Angular app after outbound marketing is removed?



## Marketing pages

After outbound marketing is removed, marketing pages hosted on Power Portals will still be online, but the following parts of the marketing pages will not work:

- Outbound marketing forms
- Outbound marketing web tracking and all page visit insights
- Marketing page lifecycle
- Marketing page editor

The underlying Power Pages data model used to host the Marketing pages will be deprecated and it will be required to migrate the whole portal to a new data model.
Given all the limitations, we strongly recommend rebuilding the OBM Marketing Pages as a native Power Pages Website. You can embed RTM marketing form into Power Pages website.
For a simple landing page with form, you can also build an RTM form and host it as a standalone page.

[!INCLUDE [footer-include](./includes/footer-banner.md)]