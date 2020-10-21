---
title: Get started with the web SDK
author: ruthaisabokhae
description: Learn how to use the engagement insights capability SDK to instrument your website.
ms.author: ruthai
ms.date: 10/19/2020
ms.service: customer-insights
ms.subservice:
ms.topic: conceptual
---

# Get started with the web SDK

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

This tutorial guides you through the process of instrumenting your website with a Dynamics 365 Customer Insights engagement insights capability SDK. You start seeing events in your portal in five minutes or sooner.

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

## Integrate the engagement insights capability SDK into your webpage

1. From the engagement insights capability home screen, select your workspace from the workspace drop-down list on the left navigation pane. If you don't have a workspace, select **+ New Workspace** option to create one.

2. Go to **Admin** > **Data** > **Code**  and copy the code snippet. By default, your ingestion key is embedded in the code snippet.

   :::image type="content" source="media/copycode.png" alt-text="Code page with callout on code snippet":::


3. Add the copied code snippet to your webpage, near the top of the `<head>` tag and before any other script or CSS tags.

## Considerations for Single Page Applications (SPAs)

For SPAs, the SDK can't autocollect view events. Customers must ensure that the autoCapture configuration setting has view set to *false* or *removed*.

Customers should instead manually instrument view events. The SDK has a `trackView(view)` API which can be used to log a page view. The only required field in the view object is the `uri`.

The following example shows a code snippet tracking a view event. The "NAME" here would be the value in the `name` key in the snippet configuration. This is the variable name in the window object where the SDK is loaded.

```

window["NAME"].trackView({
  uri: "https://mywebsite.com/path/"
});

```
