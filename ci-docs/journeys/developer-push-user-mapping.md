---
title: Push notification user mapping for application developers
description: Push notification user mapping connects Customer Insights - Journeys records to mobile app users so notifications reach the correct person.
ms.date: 07/16/2026
ms.topic: how-to
author: alfergus
ms.author: alfergus
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Push notification user mapping for application developers

Push notification user mapping in Customer Insights - Journeys helps you connect the correct record to a mobile app user so push notifications reach the right person. To learn more about the overall approach to setting up push notifications, see the [push notification setup overview](push-setup-overview.md).

To enable push notifications in Customer Insights - Journeys, you need to complete the following steps:

1. [Push notification application configuration](push-notifications-setup.md)
1. [User mapping for push notifications](developer-push-user-mapping.md)
1. [Device registration for push notifications](developer-push-device-registration.md)
1. [Receiving push notifications on devices](developer-notifications.md)
1. [Interaction reporting for push notifications](developer-push-interactions.md)

## User mapping architecture

The device application publishes device and user information to the device token management system. The token management system sends a GET request to the Customer Insights - Journeys contact, lead, or profile API to retrieve the Customer Insights - Journeys user identifier. The token management system then sends a POST request containing the device token, user ID, and app ID to the Customer Insights - Journeys push device registration API.

:::image type="content" source="media/real-time-marketing-push-user-mapping.png" alt-text="Screenshot of push notification user mapping between a device application, token system, and Customer Insights - Journeys APIs." lightbox="media/real-time-marketing-push-user-mapping.png":::

## Implement user mapping

For push notifications from a mobile application to work correctly, you need to configure mapping from Dynamics 365 Customer Insights - Journeys customers to mobile application users. Mapping ensures that the correct person (represented with the correct entity and record ID) receives the expected mobile push notification. This step isn't related to the mobile application setup (whether on Android or Apple devices), but rather, to the logical connection between the person represented as a Customer Insights - Journeys record and the counterpart record as a mobile application user.

To implement user mapping:

1. Select the correct entity to implement user mapping. This step is crucial because, in Customer Insights - Journeys, you can orchestrate to multiple Microsoft Dataverse entities (such as a contact or lead), or to a Customer Insights - Data profile.
1. Pass the correct record ID to the mobile application so it can identify the user with that ID.

## User mapping example

As an example, if you use the contact Dataverse entity and use the email address field as the unique key for an end user as a contact, you can retrieve the correct ID by making an OData `GET` call to Dataverse. The following example shows how to make this call:

```http
https://<your Customer Insights - Journeys instance>.dynamics.com/api/data/v9.0/contacts?$filter=emailaddress1 eq 'andrew@contosoltd.com'
```

This query to Dataverse returns a single contact that has *andrew@contosoltd.com* as the email address. Once this ID is acquired (in this example, a contact ID), it should be used as the `UserId` parameter in the mobile application.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
