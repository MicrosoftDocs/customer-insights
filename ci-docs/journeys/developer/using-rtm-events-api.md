---
title: Using the events API in outbound marketing
description: Learn how to use the events API to access date from events, sessions, session tracks, and passes in outbound marketing.
ms.date: 10/18/2022
ms.topic: overview
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
---

# Using the events API

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> This is a private preview feature.

The events API is a programmatic method to access data of events, sessions, session tracks, passes, speakers, and sponsorships. Additionally, it allows you to register for events and sessions.
The API access is over HTTPS protocol and is accessed from the API endpoint that you receive while creating a web application token. All data is sent and received as JSON.

# Registering for event API
In Settings section under Event management and Web Applications create a new Web Application. It is important to correctly select origin - for example if you select https://contoso.com javascript hosted on different domain won't be able to access the event management api.
![image](https://github.com/MicrosoftDocs/customer-insights/assets/5519592/80e859d3-201e-4ef4-b4f1-4c60ed077d4b)

After you create a webapplication you'll see a link to the OpenAPI specification in `Endpoint documentation (Preview)`

![image](https://github.com/svejdo1/customer-insights/assets/5519592/5a0163c8-dfd9-41d1-a310-8f5efe09425b)

You can click on the link, and copy & paster the api contract to open api editor - such as [https://editor-next.swagger.io/](https://editor-next.swagger.io/) - which will automatically pregenerate wrapper you can use to discover your api. You have to be authorized - e.g. provide the `Token` column.

![image](https://github.com/svejdo1/customer-insights/assets/5519592/4b5c0aa7-d41e-4c5e-bd01-f85ee5501b3e)

## Backward compatibility with outbound marketing API 
The aim for RTM api is to be backward-compatible contract-wise. There are however few limitations - RTM api doesn't support user authentication, and operations like captcha and registration to outbound event is supported only as long as organization has outbound marketing provisioned. If you were previously using angular client application you can switch the 'apiEndpoint' property from outbound marketing endpoint that looked like `https://<your org alias>.svc-tip.dynamics.com/EvtMgmt/api/v2.0/` to endpoint specified in `Endpoint (Preview)` - e.g. something like `https://public-<your org geo>.mkt.dynamics.com/api/v1.0/orgs/<your org id>/eventmanagement/`


[!INCLUDE [footer-include](.././includes/footer-banner.md)]
