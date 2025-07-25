---
title: Using the events API in real-time journeys (preview)
description: Learn how to use the events API to access date from events, sessions, session tracks, and passes in real-time journeys.
ms.date: 07/16/2025
ms.topic: overview
author: alfergus
ms.author: colinbirkett
search.audienceType: 
  - developer
ms.custom: sfi-image-nochange
---

# Using the events API in real-time journeys (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

The events API is a programmatic method to access data of events, sessions, session tracks, passes, speakers, and sponsorships. Additionally, it allows you to register for events and sessions.

The API access is over HTTPS protocol and is accessed from the API endpoint that you receive while creating a web application token. All data is sent and received as JSON.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## Register for the events API

In the **Settings** section under **Event management** > **Web Applications** create a new web application. It's important to select the correct origin. For example, if you select https://contoso.com, JavaScript hosted on different domain won't be able to access the event management API.

:::image type="content" source="../media/event-api-settings.png" alt-text="Event API settings screenshot." lightbox="../media/event-api-settings.png":::

After you create a web application, you see a link to the OpenAPI specification in **Endpoint documentation (Preview)**.

:::image type="content" source="../media/event-api-endpoint.png" alt-text="Event API endpoint screenshot." lightbox="../media/event-api-endpoint.png":::

You can select the link and copy and paste the API contract to an OpenAPI editor such as [Swagger Editor](https://editor-next.swagger.io/), which automatically pregenerates a wrapper you can use to discover your API. To access your API, you must be authorized (provide the **Token** column).

:::image type="content" source="../media/event-api-swagger.png" alt-text="Event API Swagger Editor screenshot." lightbox="../media/event-api-swagger.png":::

## Backward compatibility with the outbound marketing API

The aim for the real-time journeys API is to be backward compatible contract-wise. There are, however, a few limitations. The real-time journeys API doesn't support user authentication. Operations like CAPTCHA and registration to outbound events are supported only as long as the organization has outbound marketing provisioned. If you previously used an Angular client application, you can switch the **apiEndpoint** property from the outbound marketing endpoint that looked like `https://<your org alias>.svc-tip.dynamics.com/EvtMgmt/api/v2.0/` to the endpoint specified in `Endpoint (Preview)`, which looks something like `https://public-<your org geo>.mkt.dynamics.com/api/v1.0/orgs/<your org id>/eventmanagement/`

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
