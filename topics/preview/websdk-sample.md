---
title: Run the web SDK sample for Product Insights
author: ruthaisabokhae
description: How to run the web SDK sample for Dynamics 365 Product Insights
ms.author: ruthai
ms.date: 07/31/2020
ms.service: product-insights
ms.topic: conceptual
robots: noindex,nofollow
---

# Run the web SDK sample for Product Insights

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- You have the [ingestion key](get-started-websdk.md)

## Run Sample

1. [Download the Product Insights web SDK sample](https://download.microsoft.com/download/f/e/c/fec76936-6440-414d-b75a-7be644f82892/pi_websdk_sample.zip).
2. [Install the live server extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) in Visual Studio Code.
3. Unzip the compressed file `pi_websdk_sample.zip`.
4. Open the unzipped folder in Visual Studio Code.
5. In the `pi_websdk_sample.html` file, replace the string “INGESTION_KEY” with your ingestion key from the Product Insights portal, and the string “NAME” with the global name that you want the SDK to be instantiated in. Be sure to replace all occurrences.
6. Open the `pi_websdk_sample.html` file using live server in Visual Studio Code.
