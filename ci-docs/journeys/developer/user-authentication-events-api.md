---
title: User authentication using the events API in outbound marketing
description: Learn how to use the events API to authenticate users in outbound marketing.
ms.date: 06/11/2019
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
ms.custom: outbound-marketing, evergreen
---

# User authentication using events API in outbound marketing

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

[!INCLUDE [azure-ad-to-microsoft-entra-id](../includes/azure-ad-to-microsoft-entra-id.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](../user-guide.md), which is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](../transition-overview.md).

The events API supports user authentication with Microsoft Entra ID. To link the events API to your Microsoft Entra ID, you need to add your `Microsoft Entra ID Client ID` and `Microsoft Entra ID Metadata Endpoint` to your `web application setting`.  More information: [Creating a Microsoft Entra ID tenant and adding a web application to the tenant](event-management-aad-b2c-setup.md#creating-a-microsoft-entra-id-tenant-and-adding-a-web-application-to-the-tenant)

To authenticate the user against the API, you need to add the `Authorization` header containing the `token_id` bearer to each API request. 

This `token_id` can be retrieved by authenticating the user against Microsoft Entra ID. 

**Request** 

```http
curl -X GET \ 
  'https:// b7c1ad1ab7fa4a7482b16315d94a26af.svc-tip.dynamics.com/EvtMgmt/api/v2.0/events/published?emApplicationtoken=VZsLZhx251OM9uJa..' \ 
  -H 'Authorization: Bearer eyJ0eXAiOiJK…\ 
  -H 'Origin: https://localhost:4200' 
``` 

## Contact matching strategy

The events API will automatically try to link contacts from Microsoft Entra ID to the contacts in Dynamics 365 Customer Insights - Journeys.  

To do so, it uses a contact matching strategy that can be configured in the event administration settings. By default, first name, last name, and email are used as the contact matching strategy. More information: [Event administration](../events-settings.md#event-administration)

In case no matching contact is found, a new contact is created automatically.

> [!NOTE]
> Linked contact entities contain an attribute called `msevtmgt_aadobjectid` that stores the object ID of the user in Microsoft Entra ID.

### Retrieving information of authenticated user 

The events API provides an endpoint that returns the information and contact ID of the authenticated user. 

**Request** 

```http
curl -X GET \
  'https:// b7c1ad1ab7fa4a7482b16315d94a26af.svc-tip.dynamics.com/EvtMgmt/api/v2.0/users/authenticated?emApplicationtoken=VZsLZhx251OM9uJa..' \
  -H 'Authorization: Bearer eyJ0eXAiOiJK…\ 
  -H 'Origin: https://localhost:4200'
```

**Response** 

```json
{
   "id":"05ef77de-b882-e911-a970-000d3a4e9aa0",
   "firstName":"John",
   "lastName":"Doe",
   "email":"joe.doe@contoso.com",
   "isAnonymous":false
} 
```

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
