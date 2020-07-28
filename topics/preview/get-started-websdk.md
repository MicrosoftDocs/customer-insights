---
title: Get started with the web SDK for Dynamics 365 Product Insights
author: ruthaisabokhae
description: Learn how to use an ingestion key and tools in the Dynamics 365 Product Insights SDK to instrument your website.
ms.author: ruthai
ms.date: 07/31/2020
ms.service: product-insights
ms.topic: conceptual
robots: noindex,nofollow
---

# Get started with the web SDK

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

This tutorial will guide you through the process of using a Product Insights ingestion key and the Product Insights SDK for instrumenting your existing website. You'll start seeing signals in your portal in five minutes or sooner.

## Configuration options

The following configuration options can be passed to the SDK:

- **ingestionKey**: This is the key used to send signals to your project.
-	**autoCapture**: This specifies the auto capture instructions for the SDK to collect page views and clicks. It has two options:
    - **view**: Set this to true if you want the SDK to capture page views automatically. Note that single page applications need to instrument views manually, and must instrument the trackView() API whenever they route to a new page.
    - **click**: Set this to true if you want the SDK to capture page clicks automatically.
-	**userConsent**: This specifies whether the user has consented to let the SDK add data to browser storage (localstorage or cookies) that will be used by Product Insights to track user behavior. By default, this is assumed to be true.
-	**endpointUrl**: This can be used to specify the destination URL for your signals. Only override this if you need to send data to a specific endpoint.

## Prerequisites

* The SDK requires the project or webpage to be hosted in order to send telemetry. Telemetry sent from a local file will not be accepted by the server.
* You have an ingestion key.

## Get an ingestion key from the Product Insights portal

1. From the Product Insights home screen, select your project from the project dropdown on the left navigation menu. If you don't already have a project, select the **+ New Project** option instead and create one.
2. Once you've selected a project, navigate to **Admin > Settings > General** in the left panel.
3. Copy your key from the **Ingestion key** field.

## Integrate the Product Insights SDK into your webpage

1. In Product Insights, navigate to **Admin > Data > Code** in the left panel. Copy the code snippet on this page.

2. In the code snippet, replace the string "NAME" with a global variable name in the window object where the SDK is instantiated. For example, if you replace "NAME" with "Contoso", then the SDK can be accessed at **window["Contoso"]** or simply **Contoso**. For example:

```
window["Contoso"].trackSignal({
    name: "video_log",
    properties: {
        "duration": 320,
        "name": "getting_started",
        "ad_shown": true
    }
});
```

3. In the code snippet, ensure the [ingestion key](#get-an-ingestion-key-from-the-product-insights-portal) is added to your code.

4. Add the modified code snippet to your webpage, near the top of the `<head>` tag and before any other script or CSS tags.

## Setting user details for your signal

The Product Insights SDK allows you to define user information that can be sent with every signal. You can do this by specifying the user details in a property called `user` (the expected data for this property is the `IUser` object), similar to `src`, `name`, and `cfg` in the code snippet configuration. Alternatively, user information can be specified by calling the `setUser(user: IUser)` API on the SDK.

Specifying user details in the code snippet means that all telemetry will have this information. However, if specified by the `setUser API`, telemetry sent before the `setUser API` will not contain this information.

The `IUser` interface contains the following string properties:

- **localId**: The user's local ID.
- **authId**: The authenticated user ID.
- **authType**: The authentication type used to the get authenticated user ID.
- **name**: The user's name.
- **email**: The user's email address.
