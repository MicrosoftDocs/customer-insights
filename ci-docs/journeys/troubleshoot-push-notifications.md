---
title: Troubleshoot push notifications setup
description: Learn how to troubleshoot push notifications setup in Dynamics 365 Customer Insights - Journeys.
ms.date: 11/21/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Troubleshooting push notifications setup

This article covers possible problems with push notifications setup in Customer Insights - Journeys and provides some troubleshooting solutions.

## General

### Why am I receiving multiple push notifications?

This is due to one of the following reasons:

1. You're sending push notifications from multiple journeys to same the audience member (for example, the same contact).
1. You have multiple audience members (contacts) with the same device token.

## Device registration problems

The following are possible device registration problems.

### I'm calling the device registration public API and it returns "202," but nothing happens

The device registration public API returns in an asynchronous manner, which is a reason why the response status code is 202 (Accepted) and not 200 (OK). The request starts the registration process, but this doesn't necessarily mean that the operation was successful. There's a separate [device registration status API](developer-push-device-registration.md#device-registration-status) you need to call to see results of the registration. Use the `RegistrationRequestId` that's provided in response to the device registration API execution to request the registration status. If there's no `RegistrationRequestId` returned within the response, then you need to add `x-ms-track-registration` set to `true` within the request headers.

### Device registration doesn't do anything, and the registration status request returns 400

There are two common reasons for this issue:
1. The wrong `ApiToken` or `MobileAppId` field was provided. Make sure these values are taken from the **Developer Information** section of the CRM. 
2. The wrong organization ID was used in the public API URL. Make sure you're using the relevant value from the **Developer Information** tab and call the API for the correct CRM environment.

### Registration status API shows the following failure message: *Provided API token is not valid*

The device registration API request body has an ApiToken field and its value should equal the value in the field shown within the "Access tokens" section of the "Developer Information" tab in the mobile application configuration in the CRM user interface. Make sure the value used in the API is taken from the correct mobile application and the correct mobile application ID is used for the request.

### Registration status API includes the following failure text: *Sending a test invisible notification failed for the given device token*

As a part of the device registration process, Customer Insights sends an invisible test push notification for a given device token. If sending fails, the registration process also fails. The sections below explain the problem, in accordance with platform type (Android or iOS).

## Push notification sending problems for Android

The following are push notification sending problems for Android devices.

### Sending failure includes a "Provided service account JSON is incorrect" message

To send push notifications, Customer Insights needs to have a correct service account JSON file uploaded within the mobile application CRM user interface. A common mistake is to use a `google-service.json` file. This file is used within the source code of mobile app itself and shouldn't be used in the CRM. To see how to fetch the correct service account JSON file, see [Transition Android push notifications to Firebase Cloud Messaging (FCM) tokens for authentication](push-notification-fcm-token-transition.md).

### Sending failure includes a "PROJECT_NOT_PERMITTED" error code

It's likely that the "Firebase In-App Messaging API" service isn't enabled. Navigate to "Google Cloud" from within the Firebase Console user interface, find "Firebase In-App Messaging API," and enable it.

### Customer Insights claims the notification was sent successfully, but no notification appeared on the screen

Customer Insights sends push notifications using a data payload format. This is required to make changes in the mobile application code to receive the push notification payload and render it as a popup. For more instructions, see [Receiving push notifications on mobile devices](developer-notifications.md).

For more information about data payload formats in Firebase, see [Firebase Cloud Messaging message types](https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type).

### Sending failure includes unclear error code or message

Customer Insights sends push notification using Firebase servers directly. The failure response comes directly from the Firebase server if there's a submission failure. Review the [ErrorCode](https://firebase.google.com/docs/reference/fcm/rest/v1/ErrorCode) reference documentation for all possible error codes and their meaning.

## Push notification sending problems for iOS

For notification sending problems for iOS, it's possible to use external third-party websites to help troubleshoot, such as `https://apnspush.com/`>`. These websites allow you to quickly test push notification submission and see if any changes made work.

### Sending failure includes a BadDeviceToken error code

The most common reason for this error is mismatched environments of the device token and the CRM configuration. When the device token is generated by an iOS application, it's also generated for Sandbox or Production mode. Make sure to set the same app mode in the CRM user interface and use the same app mode credentials in the CRM mobile application.

### Sending fails for iOS device tokens wrapped by Firebase

Customer Insights doesn't currently support iOS device tokens working using FCM. Make sure that the device token used for iOS device registration has an original APNS device token in the correct format. This token includes only HEX symbols, for example, `0123456789ABCDEF`. Make sure the token doesn't exceed 64 characters.

### Sending failure includes unclear error code or message

Customer Insights sends push notification using APNS servers directly. Failure responses directly come from the APNS server if there's a submission failure. Review the [local and remote notification programming guide: Communicating with APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html#//apple_ref/doc/uid/TP40008194-CH11-SW17) for all possible error codes and their meaning.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
