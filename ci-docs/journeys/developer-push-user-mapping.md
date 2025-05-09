---
title: Push notification user mapping for application developers
description: Learn developer settings user mapping for push notifications in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/14/2023
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Push notification user mapping for application developers

To learn more about the overall approach to setting up push notifications in Customer Insights - Journeys, visit the [push notification setup overview](push-setup-overview.md).

To enable push notifications in Customer Insights - Journeys, you need to complete the following steps:

1. [Push notification application configuration](push-notifications-setup.md)
1. [User mapping for push notifications](developer-push-user-mapping.md)
1. [Device registration for push notifications](developer-push-device-registration.md)
1. [Receiving push notifications on devices](developer-notifications.md)
1. [Interaction reporting for push notifications](developer-push-interactions.md)

## Implement user mapping

:::image type="content" source="media/real-time-marketing-push-user-mapping.png" alt-text="Push notifications user mapping diagram." lightbox="media/real-time-marketing-push-user-mapping.png":::

For push notifications from a mobile application to work correctly, you need to configure mapping from Dynamics 365 Customer Insights - Journeys customers to mobile application users. The mapping ensures that the correct person (represented with the correct entity and record ID) receives the expected mobile push notification.

This step isn't related to the mobile application setup (whether on Android or Apple devices), but rather, to the logical connection between the person represented as a Customer Insights - Journeys record and the counterpart record as a mobile application user.

First, to implement user mapping, the correct entity must be selected. This step is crucial because, in Customer Insights - Journeys, it's possible to orchestrate to multiple Microsoft Dataverse entities (such as a contact or lead), or to a Customer Insights - Data profile. Then, the correct record ID should be passed along to the mobile application and the mobile application should identify the user with that ID.

### User mapping example

As an example, if the contact Dataverse entity is used and the email address field is used as the unique key for an end user as a contact, one possibility to retrieve the correct ID is using an OData `GET` call to Dataverse is the following example:

```HTTP
https://<your Customer Insights - Journeys instance>.dynamics.com/api/data/v9.0/contacts?$filter=emailaddress1 eq 'andrew@contosoltd.com'
```

This query to Dataverse returns a single contact that has *andrew@contosoltd.com* as the email address. Once this ID is acquired (in this example, a contact ID), it should be used as the `UserId` parameter in the mobile application.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
