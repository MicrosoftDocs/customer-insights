---
title: Advanced web SDK instrumentation scenarios
author: ruthaisabokhae
description: Advanced scenarios to consider when instrumenting your website with an SDK
ms.author: ruthai
ms.date: 10/16/2020
ms.service: product-insights
ms.topic: conceptual
robots: noindex,nofollow
---

# Introduction

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

This page guides you through advanced scenarios to consider when instrumenting your website with a Dynamics 365 Customer Insight engagement insights capability SDK.

## Setting user details for your event

The engagement insights capability SDK lets you define user information that can be sent with every event. You can specify the user details in a property called `user` (the expected data for this property is the `IUser` object), similar to `src`, `name`, and `cfg` in the code snippet configuration.

The `IUser` object contains the following string properties:

- **localId**: The user's local ID.
- **authId**: The authenticated user ID.
- **authType**: The authentication type used to get the authenticated user ID.
- **name**: The user's name.
- **email**: The user's email address.
    
The following example shows a code snippet sending user information. Where you see Functions denoted by *, replace it with your implementation of calling those values:  

```
[…]
window, document 
{
    src:"https://download.pi.dynamics.com/sdk/web/mspi-0.min.js", 
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

You can also specify user information by calling the `setUser(user: IUser)` API on the SDK. Telemetry sent after calling the `setUser API` will contain the user information.

## Adding custom properties for each event

The SDK lets you specify custom properties that can be sent with every event. You can specify the custom properties as an object containing key-value pairs (the value can be of type `string | number | boolean`). The object can be added in a property called `props`, similar to `src`, `name`, and `cfg` in the code snippet configuration. 

The following example shows a code snippet sending custom properties:

```
[…]
window, document 
{
    src:"https://download.pi.dynamics.com/sdk/web/mspi-0.min.js", 
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

You can also specify custom properties one by one by calling the `setProperty(name: string, value: string | number | boolean)` API on the SDK.

## Sending custom events

The SDK can be used to send custom events. Customer must specify a name for the event and properties to be sent with the event.

The following example shows a code snipped tracking a custom event. The "NAME" is the value in the `name` key in the snippet configuration. This is the variable name in the window object where the SDK is loaded.

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
