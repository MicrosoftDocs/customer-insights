---
title: Run the web SDK sample for Dynamics 365 Customer Insights engagment insights capability
author: ruthaisabokhae
description: How to run the web SDK sample for Dynamics 365 Customer Insights engagment insights capability
ms.author: ruthai
ms.date: 07/31/2020
ms.service: product-insights
ms.topic: conceptual
robots: noindex,nofollow
---

# Run the web SDK sample for Dynamics 365 Customer Insights engagment insights capability

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- You have the [ingestion key](get-started-websdk.md)

## Run sample

1. [Download the Dynamics 365 Customer Insights engagment insights capability web SDK sample](https://download.pi.dynamics.com/sdk/EngagementInsightsSamples/ei_websdk_sample.zip).
2. [Install the Live Server extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) in Visual Studio Code.
3. Unzip the compressed file `ei_websdk_sample.zip`.
4. Open the unzipped folder in Visual Studio Code.
5. In the `ei_websdk_sample.html` file, replace the string “INGESTION_KEY” with your ingestion key from the engagment insights capability portal, and the string “NAME” with the global name that you want the SDK to be instantiated in. Be sure to replace all occurrences.
6. Open the `ei_websdk_sample.html` file using Live Server in Visual Studio Code.
