---
title: Run a web SDK sample
description: Learn how to personalize and run a web SDK sample.
author: pickwick129
ms.reviewer: ruthai
ms.author: v-salash
ms.date: 10/30/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---
# Run the web SDK sample for Dynamics 365 Customer Insights engagement insights capability

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

The engagement insights capability web SDK library is a JavaScript library with sample code that you can use on your website.

## Prerequisites

- Install [Visual Studio Code](https://code.visualstudio.com/).
- [Install the Live Server extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) in Visual Studio Code and get familiar with how to run Live Server.
- You must have the [ingestion key](instrument-website.md).

## Run sample

1. [Download the web SDK sample](https://download.pi.dynamics.com/sdk/EngagementInsightsSamples/ei_websdk_sample.zip).

1. Unzip the compressed file `ei_websdk_sample.zip`.

1. Open the unzipped folder in Visual Studio Code.

1. In the `ei_websdk_sample.html` file, replace the string “INGESTION_KEY” with your ingestion key from the engagement insights capability portal, and the string “NAME” with the global name that you want the SDK to be instantiated in. Ensure you replace all occurrences.

1. Open the `ei_websdk_sample.html` file using Live Server in Visual Studio Code by selecting **Go Live** from the status bar.

1. On opening the page, a view event should be automatically sent. Clicking on any of the buttons on the page will send action events. The **Track Events** button will also send custom events. Selecting the **Go to Bing** button will send an action event before navigating to the Bing website.

1. Look at events flowing when you navigate to your workspace. This workspace is associated with the ingestion key entered in Step 4.
