---
title: Get started with the web SDK
description: Learn how to use the engagement insights capability SDK to instrument your website.
author: pickwick129
ms.reviewer: ruthai
ms.author: v-salash
ms.date: 11/12/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Get started with the web SDK

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Once you add code to your website, data starts to appear in your workspace. This tutorial guides you through the process of using the web SDK for engagement insights to instrument your website. You'll start seeing events in your workspace in five minutes or less after implementing the code.

## Prerequisites

* The SDK requires that your webpage or project is hosted to send telemetry. Telemetry sent from a local file will not be accepted by the server.
* You must have an ingestion key (already embedded in your code snippet).

## Configuration options

You can pass the following configuration options to the SDK:

- **ingestionKey**: The ingestion key used to send events to your workspace.
-	**autoCapture**: Specifies the auto capture instructions for the SDK to collect page views and clicks. It has two options:
    - **view**: Set to *true* if you want the SDK to capture page views automatically. Single page applications need to instrument views manually and must instrument the trackView() API whenever they route to a new page.
    - **click**: Set to *true* if you want the SDK to capture page clicks automatically.
-	**userConsent**: Specifies whether the user has consented to let the SDK add data to browser storage (local storage or cookies). We use this data to track user behavior. By default, it's assumed to be true.
-	**endpointUrl**: Used to specify the destination URL for your events. Only override this option if you need to send data to a specific endpoint.

## Integrate the SDK into your webpage

1. In the navigation pane, choose your workspace from the workspace drop-down list. If you don't have a workspace, select **+ New Workspace**  to create one.

2. Go to **Admin** > **Data** > **Code**  and copy the code snippet. By default, your ingestion key is embedded in the code snippet.

   :::image type="content" source="media/copy-code.png" alt-text="Code page screenshot":::


3. Add the copied code snippet to your webpage, near the top of the `<head>` tag and before any other script or CSS tags.

## Considerations for Single Page Applications (SPAs)

For SPAs, the SDK can't autocollect view events. You must ensure that the autoCapture configuration setting view is set to *false* or *removed*.

Instead, manually instrument view events. The SDK has a `trackView(view)` API that can be used to log a page view. The only required field in the view object is the `uri`.

The following example shows a code snippet tracking a view event. The "NAME" here is the value in the `name` key in the snippet configuration. It's also the variable name in the window object where the SDK is loaded.

```

window["NAME"].trackView({
  uri: "https://mywebsite.com/path/"
});

```
