---
title: Use the events API in real-time journeys
description: Learn how to use the events API to access date from events, sessions, session tracks, and passes in real-time journeys.
ms.date: 10/07/2025
ms.topic: overview
author: alfergus
ms.author: colinbirkett
search.audienceType: 
  - developer
ms.custom: sfi-image-nochange
---

# Use the events API in real-time journeys

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

The events API is a programmatic method to access data from events, sessions, session tracks, passes, speakers, and sponsorships. Additionally, the events API allows you to register for events and sessions.

The API accessed is over HTTPS protocol and is accessed from the API endpoint that you receive while creating a web application token. All data is sent and received as JSON.

## Register for the events API

In the **Settings** section under **Event management** > **Web Applications**, create a new web application. It's important to select the correct origin. For example, if you select https://contoso.com, JavaScript hosted on different domain won't be able to access the event management API.

:::image type="content" source="../media/event-api-settings.png" alt-text="Event API settings screenshot." lightbox="../media/event-api-settings.png":::

After you create a web application, you see a link to the OpenAPI specification in **Endpoint documentation (Preview)**.

:::image type="content" source="../media/event-api-endpoint.png" alt-text="Event API endpoint screenshot." lightbox="../media/event-api-endpoint.png":::

You can select the link and copy and paste the API contract to an OpenAPI editor such as [Swagger Editor](https://editor-next.swagger.io/), which automatically pregenerates a wrapper you can use to discover your API. To access your API, you must be authorized (provide the **Token** column).

:::image type="content" source="../media/event-api-swagger.png" alt-text="Event API Swagger Editor screenshot." lightbox="../media/event-api-swagger.png":::

## Create an event page or event portal  

The events API allows you to create a customized event page and an event portal that lists all available events that are live and published using the “Custom solution using event API” publishing option. The events API allows you to:  

- Retrieve a list of live events that includes their name, description, location, and time.
- For the event page, it allows you to retrieve key information about the event such as:
    - Name
    - Time
    - Location
    - Event QR code
    - Capacity
    - List of sessions
    - List of speakers
    - List of sponsors and their logos

## Create a custom event registration experience  

The events API also allows you to create a registration submission without the need to use real-time marketing forms, while still benefiting from important features such as matching strategy, consent, audience settings, and more.

First, define the key settings for your audience by navigating to **Settings** > **Event management** > **Event registration settings** and define:

1. Default audience
1. Default matching rule
1. Default compliance profile

The default event registration settings are used when processing submissions from the API. Once you set the registration settings, the event API submission endpoint allows you to:  

1. Create a registration submission for an event:

```
{ 
    "attendees": [ 
        { 
            "lastName": "Sample Contact Last Name", 
            "firstName": "Sample Contact First Name", 
            "email": "email@contoso.com", 
            "responses": [ 
                { 
                    "id": "jobtitle", 
                    "value": "Sample Contact Job Title" 
                }, 
                { 
                    "id": "customUnmappedField1", 
                    "value": "Sample Custom Unmapped Field 1" 
                }, 
                { 
                    "id": "customUnmappedField2", 
                    "value": "Sample Custom Unmapped Field 2" 
                } 
            ] 
        } 
    ] 
}
```

2. Create a registration submission for a session:

```
{ 
    "attendees": [ 
        { 
            "lastName": "Sample Contact Last Name", 
            "firstName": "Sample Contact First Name", 
            "email": "email@contoso.com", 
            "responses": [ 
                { 
                    "id": "jobtitle", 
                    "value": "Sample Contact Job Title" 
                } 
            ], 
            "attendeeSessions": [ 
                { 
                    "sessionId": "d5f513c6-989f-f011-bbd3-000d3a5b6385" 
                }, 
                { 
                    "sessionId": "f5d4e4b9-989f-f011-bbd3-000d3a5b6385" 
                } 
            ] 
        } 
    ] 
} 
```

3. Create a waitlist registration:

```
{
    "attendees": [ 
        { 
            "lastName": "Sample Contact Last Name", 
            "firstName": "Sample Contact First Name", 
            "email": "email@contoso.com", 
            "waitlisted": true, 
            "responses": [ 
                { 
                    "id": "jobtitle", 
                    "value": "Sample Contact Job Title" 
                }, 
                { 
                    "id": "customUnmappedField1", 
                    "value": "Sample Custom Unmapped Field 1" 
                }, 
                { 
                    "id": "customUnmappedField2", 
                    "value": "Sample Custom Unmapped Field 2" 
                } 
            ] 
        } 
    ]
}
```

## Backward compatibility with the outbound marketing API

The aim for the real-time journeys events API is to be backward compatible contact-wise. There are, however, a few limitations:

- The real-time journeys events API doesn't support user authentication.
- Operations like CAPTCHA and registration to outbound events are supported only as long as the organization has outbound marketing provisioned.
- If you previously used an Angular client application, you can switch the **apiEndpoint** property from the outbound marketing endpoint that looked like `https://<your org alias>.svc-tip.dynamics.com/EvtMgmt/api/v2.0/` to the endpoint specified in `Endpoint (Preview)`, which looks something like `https://public-<your org geo>.mkt.dynamics.com/api/v1.0/orgs/<your org id>/eventmanagement/`.

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
