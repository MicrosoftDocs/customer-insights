---
title: Using the events API in outbound marketing
description: Learn how to use the events API to access date from events, sessions, session tracks, and passes in outbound marketing.
ms.date: 10/18/2022
ms.topic: overview
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
ms.custom: outbound-marketing
---

# Using the events API in outbound marketing

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](transition-overview.md).

The events API is a programmatic method to access data of events, sessions, session tracks, passes, speakers, and sponsorships. Additionally, it allows you to register for events and sessions.

## Schema 

The API access is over HTTPS protocol and is accessed from the API endpoint that you receive while creating a web application token. All data is sent and received as JSON. 

Blank fields are included as `null` instead of being omitted. 

## Endpoint 

Every customer has their own endpoint URL. The Event API endpoint URL consists of two parts:

- The endpoint domain
- The subdirectory  

You will get the root endpoint after creating a web application token. You can find more information on how to create a web application token here: [Register web application](#bkmk_registerwebapp). 

**Example for root endpoint**

```http
https://b7c1ad1ab7fa4a7482b16315d94a26af.svc.dynamics.com 
``` 

The subdirectory always starts with `EvtMgmt/api` followed by the API version (which can be retrieved from the API documentation available here: [Event management API reference docs](https://go.microsoft.com/fwlink/?linkid=2042224). 

**Example for subdirectory**

```http
EvtMgmt/api/v2.0/ 
``` 

**Example for full endpoint URL** 

```http
https://b7c1ad1ab7fa4a7482b16315d94a26af.svc.dynamics.com/EvtMgmt/api/v2.0/ 
```

## Authentication 

To use the events API, you need to provide a `web application token` as a URL parameter in each request. The web application token is used to control API requests that are associated with your organization. See [Register web application](#bkmk_registerwebapp) for more information on how to create and retrieve a web application. 

The `web application token` can be added to the request by adding a URL parameter called `emApplicationtoken`. 

**Example** 

```http
https://b7c1ad1ab7fa4a7482b16315d94a26af.svc.dynamics.com/EvtMgmt/api/v2.0/events/published?emApplicationtoken=B7vdzdhCiLt9c5iT….
```

Additionally, the origin from where the request is sent must be equal to the origin specified when creating the web application token.

If you do not provide a web application token or the Origin Header, the events API will return `HTTP 400 Bad Request`.

If the web application token is invalid, the events API will return `HTTP 401 Unauthorized`.

<a name="bkmk_registerwebapp"></a>

## Register your web application

To use the events API, you need to provide a web application token in each request. The web application token is used to control API requests that are associated with your organization. More information: [Register your web application](host-custom-event-website-on-azure.md#step-2-register-your-web-application)

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
