---
title: Get started with the web SDK for Dynamics 365 Product Insights
author: ruthaisabokhae
description: Learn how to use the Product Insights SDK to instrument your website.
ms.author: ruthai
ms.date: 08/05/2020
ms.service: product-insights
ms.topic: conceptual
robots: noindex,nofollow
---

# Get started with the web SDK

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

This tutorial guides you through the process of instrumenting your website with a Product Insights SDK. You'll start seeing events in your portal in five minutes or sooner.

## Configuration options

The following configuration options can be passed to the SDK:

- **ingestionKey**: The ingestion key used to send events to your project.
-	**autoCapture**: Specifies the auto capture instructions for the SDK to collect page views and clicks. It has two options:
    - **view**: Set to true if you want the SDK to capture page views automatically. Single page applications need to instrument views manually, and must instrument the trackView() API whenever they route to a new page.
    - **click**: Set to true if you want the SDK to capture page clicks automatically.
-	**userConsent**: Specifies whether the user has consented to let the SDK add data to browser storage (local storage or cookies). Product Insights uses this data to track user behavior. By default, it's assumed to be true.
-	**endpointUrl**: Used to specify the destination URL for your events. Only override this option if you need to send data to a specific endpoint.

## Prerequisites

* The SDK requires the project or webpage to be hosted to send telemetry. Telemetry sent from a local file will not be accepted by the server.
* You have an ingestion key (already embedded in your code snippet).

## Integrate the Product Insights SDK into your webpage

1. From the Product Insights home screen, select your project from the project drop-down list on the left navigation pane. If you don't already have a project, select the **+ New Project** option instead and create one.

2. Go to **Admin** > **Data** > **Code**  and copy the code snippet on this page.

   :::image type="content" source="media/get-code.png" alt-text="Code page with callout on code snippet":::

3. In the code snippet, replace the string "NAME" with a global variable name in the window object where the SDK is instantiated. For example, if you replace "NAME" with "Contoso", then the SDK can be accessed at **window["Contoso"]** or simply **Contoso**. See the following example:

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

4. Ensure your ingestion key is embedded in the code snippet.

5. Add the copied code snippet to your webpage, near the top of the `<head>` tag and before any other script or CSS tags.

## Setting user details for your event

The Product Insights SDK lets you define user information that can be sent with every event. You can specify the user details in a property called `user` (the expected data for this property is the `IUser` object), similar to `src`, `name`, and `cfg` in the code snippet configuration. You can also specify user information by calling the `setUser(user: IUser)` API on the SDK.

Specifying user details in the code snippet means that all telemetry will have this information. However, if specified by the `setUser API`, telemetry sent before the `setUser API` won't contain this information.

The `IUser` interface contains the following string properties:

- **localId**: The user's local ID.
- **authId**: The authenticated user ID.
- **authType**: The authentication type used to get the authenticated user ID.
- **name**: The user's name.
- **email**: The user's email address.
