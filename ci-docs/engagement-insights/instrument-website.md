---
title: Add code to your website
description: How to add a code snippet to capture events on your website.
author: pickwick129
ms.reviewer: m-hartmann
ms.author: v-salash
ms.date: 04/15/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha
---

# Install the code snippet on a website

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

This article describes the steps that an administrator takes to add a code snippet to a website. You'll start seeing events in your workspace in five minutes or less after adding the script to your website.

## Prerequisite

* You have administator permissions for the workspace to store the data.
* Your website or project must be hosted online to send activity data. Data sent from a local file will not be accepted by the server.

## Add code to your website

1. Go to **Admin** > **Workspace** > **Installation guide**.

1. Select **Copy code** to copy the code snippet. By default, the ingestion key for your workspace is embedded in the code snippet.

   :::image type="content" source="media/copy-code.png" alt-text="Screenshot of the code snippet page":::

1. Add the copied code snippet to your website, near the the `<head>` tag and before any other script or CSS tags.

1. Publish your updated website and wait a few minutes to capture the incoming web traffic.

1. To see your data, select your workspace from the workspace drop-down list in the navigation pane and go to one of the reports in the **Discover** section.

## Configuration options

You can change the following configuration options in the code snippet:

- **ingestionKey**: The ingestion key used to send events to your workspace. You can change the ingestion key to send events to a differnt
- **autoCapture**: Specifies the auto capture instructions to collect page views and clicks. It has two options:
    - **view**: Set to *true* to capture page views. Page views are captured as *View* [events](glossary.md#event), a type of [base event](glossary.md#base-event). [Single page applications](#considerations-for-single-page-applications-spas) need to instrument views manually and must instrument the trackView() API whenever they route to a new page.
    - **click**: Set to *true* to capture visitor interactions on the website. Clicks are captured as *Action* [events](glossary.md#event), a type of [base event](glossary.md#base-event).

## Considerations for Single Page Applications (SPAs)

The script can't automatically collect view events for SPAs. You must set `autoCapture` to *false* or remove the autoCapture option from the code snippet. You can manually instrument view events instead with the `trackView(view)` API that can be used to log a page view. The only required field in the *view* object is the `uri`.

The following example shows a code snippet tracking a view event. The "NAME" is the value in the `name` key in the code snippet configuration. It's also the variable name in the window object where the SDK is loaded.

```

window["NAME"].trackView({
  uri: "https://mywebsite.com/path/"
});

```


[!INCLUDE[footer-include](../includes/footer-banner.md)]