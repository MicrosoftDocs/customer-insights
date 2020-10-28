---
title: Run a web SDK sample
description: Learn how to personalize and run a web SDK sample
author: pickwick129
ms.reviewer: ruthai
ms.author: v-salash
ms.date: 10/28/2020
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
- You must have the [ingestion key](instrument-website.md).

## Run sample

1. [Download the web SDK sample](https://download.pi.dynamics.com/sdk/EngagementInsightsSamples/ei_websdk_sample.zip).

1. [Install the Live Server extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) in Visual Studio Code.

1. Unzip the compressed file `ei_websdk_sample.zip`.

1. Open the unzipped folder in Visual Studio Code.

1. In the `ei_websdk_sample.html` file, replace the string “INGESTION_KEY” with your ingestion key from the engagement insights capability portal, and the string “NAME” with the global name that you want the SDK to be instantiated in. Ensure you replace all occurrences.

1. Open the `ei_websdk_sample.html` file using Live Server in Visual Studio Code.
