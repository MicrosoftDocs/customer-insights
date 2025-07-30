---
title: Push notification overview for application developers
description: Learn how push notifications work in Dynamics 365 Customer Insights - Journeys.
ms.date: 03/14/2024
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: sfi-image-nochange
---

# Push notification overview for application developers

Setting up push notifications requires a few distinct steps for application developers and administrators. This document provides a high-level overview of the architecture and links to detailed documents for each component.

For detailed information about each step, visit the following documents:

1. [Push notification application configuration](push-notifications-setup.md)
1. [User mapping for push notifications](developer-push-user-mapping.md)
1. [Device registration for push notifications](developer-push-device-registration.md)
1. [Receiving push notifications on devices](developer-notifications.md)
1. [Interaction reporting for push notifications](developer-push-interactions.md)

## Register a push notification application with Customer Insights - Journeys

Once you have an application developed, the first step is to register that application with Customer Insights - Journeys. Learn more: [Set up push notification applications](push-notifications-setup.md)

## Architecture diagram

The following diagrams provide an overview of the entities and relationships necessary to send push notifications from Customer Insights - Journeys.

:::image type="content" source="media/real-time-marketing-push-notification-overview.png" alt-text="Push notifications overview diagram." lightbox="media/real-time-marketing-push-notification-overview.png":::

## New application downloaded to mobile device

A mobile app has a device token and user information. The token and user information needs to be stored somewhere, generally in a cloud device management application, in order to provide this information to Customer Insights - Journeys.

User information and a device token need to be stored when someone downloads a new mobile application, generally in a cloud server device token management system. Approaches to storing this information can vary. The user and device information is needed to ensure the right message is delivered to the right device and to support personalization.

It's important to note that the device token can change over time. It's also not predictable what will cause the token to change. For instance, if someone removes and reinstalls the application, it's likely that the device token changes. It's important to update Customer Insights - Journeys if the device token changes to continue to send messages to that device.

## Device and user registration with Customer Insights - Journeys

You need to map the stored user to a known user in Customer Insights - Journeys because the user identifier from the device is different from the user identifier in Dataverse, where the contacts, leads, and Customer Insights - Data profiles are stored.

To perform this mapping, you can use the public API for Customer Insights - Journeys to get the Dataverse identifier. Typically, you query the API with an email address or phone number to get the contact, lead, or Customer Insights - Data profile identifier. This mapping between the mobile application user ID, device token ID, and Dataverse user identifer should be stored in the application's token management system. Because Customer Insights - Journeys supports multiple mobile applications, you need to specify the application ID when sending this data.

When the mapping is complete and stored, you can use the public API to `POST` the Dataverse user identifier, device token, and mobile application identifier in the device registration request to Customer Insights - Journeys.

View full details about registering devices and users in [push notification device registration](developer-push-device-registration.md) and [user registration](developer-push-user-mapping.md).

## Journey execution

When a journey runs and tries to send a push notification to a user, Customer Insights - Journeys attempts to send the message to all device tokens to the specified user for the specified mobile application. Messages only send to currently valid device tokens. If a user has the application installed on multiple devices registered with Customer Insights - Journeys (for instance, a phone and a tablet), they receive messages on both devices.

## Send and interaction reporting

To report on sending and interaction metrics for push notifications within Customer Insights - Journeys, you need to configure the application to send this information back to the Customer Insights - Journeys API.

View full details about send and interaction reporting in [Push notification send and interaction reporting](developer-notifications.md).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
