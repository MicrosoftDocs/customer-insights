---
title: Advanced web SDK scenarios
description: Advanced scenarios to consider when instrumenting your website with an SDK.
author: britl
ms.reviewer: mhart
ms.author: britl
ms.date: 11/12/2020
ms.service: customer-insights
ms.subservice: engagement-insights
ms.topic: conceptual
ms.manager: shellyha
---

# Advanced web SDK instrumentation

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

This article guides you through advanced scenarios to consider when [instrumenting your website](instrument-website.md) with a Dynamics 365 Customer Insights engagement insights capability SDK.

## Setting user details for your event

The SDK lets you define user information that can be sent with every event. You can specify the user details in a property called `user` (the expected data for this property is the `IUser` object), similar to `src`, `name`, and `cfg` in the code snippet configuration.

The `IUser` object contains the following string properties:

- **localId**: The user's local ID.
- **authId**: The authenticated user ID.
- **authType**: The authentication type used to get the authenticated user ID.
- **name**: The user's name.
- **email**: The user's email address.

The following example shows a code snippet sending user information. Where you see functions preceeded by an asterisk * symbol, replace the function with your custom implementation:

```
[…]
window, document
{
    src:"https://download.pi.dynamics.com/sdk/web/msei-1.min.js",
    name:"myproject",
    cfg:{
      ingestionKey:<paste your ingestion key>",
      autoCapture:{
        view:true,
        click:true
      }
    },
    user:{
      authId: getLoggedInUserId()*,
      email: getLoggedInUserEmail()*,
      authType: "MSA",
      name: "John Doe"
    }
[…]
```

You can also specify user information by calling the `setUser(user: IUser)` API. Telemetry sent after calling the `setUser` API will contain the user information.

## Adding custom properties for each event

The SDK lets you specify custom properties that can be sent with every event. You can specify the custom properties as an object containing key-value pairs (the value can be of type `string | number | boolean`). You can add the object in a property called `props`, similar to `src`, `name`, and `cfg` in the code snippet configuration.

The following example shows a code snippet sending custom properties:

```
[…]
window, document
{
    src:"https://download.pi.dynamics.com/sdk/web/msei-1.min.js",
    name:"myproject",
    cfg:{
      ingestionKey:<paste your ingestion key>",
      autoCapture:{
        view:true,
        click:true
      }
    },
    props:{
      "key_name_string": "value",
      "key_name_number": 10,
      "key_name_bool": true
    }
[…]
```

You can also specify custom properties individually by calling the `setProperty(name: string, value: string | number | boolean)` API.

## Sending custom events

You can use the SDK to send custom events. You must specify a name for the event and properties to be sent with the event.

The following example shows a code snippet tracking a custom event. The "NAME" is the value in the `name` key in the snippet configuration. It's also the variable name in the window object where the SDK is loaded.

```
window["NAME"].trackEvent({
    name: "event_name",
    properties: {
        "duration": 320,
        "name": "getting_started",
        "ad_shown": true
    }
});
```


[!INCLUDE[footer-include](../includes/footer-banner.md)]
