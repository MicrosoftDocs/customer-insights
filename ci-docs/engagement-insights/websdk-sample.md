---
title: Run a web SDK sample
description: How to run a web SDK sample
author: pickwick129
ms.reviewer: ruthai
ms.author: v-salash
ms.date: 10/14/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---
# Run the web SDK sample for Dynamics 365 Customer Insights engagement insights capability

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

The engagement insights capability web SDK library is a JavaScript library with sample code that you can use on your website.
## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- You must have the [ingestion key](instrument-website.md).

## Run sample

1. [Download the web SDK sample](https://download.microsoft.com/download/f/e/c/fec76936-6440-414d-b75a-7be644f82892/pi_websdk_sample.zip).
2. [Install the Live Server extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) in Visual Studio Code.
3. Unzip the compressed file `ei_websdk_sample.zip`.
4. Open the unzipped folder in Visual Studio Code.
5. In the `ei_websdk_sample.html` file, replace the string “INGESTION_KEY” with your ingestion key from the engagement insights capability portal, and the string “NAME” with the global name that you want the SDK to be instantiated in. Be sure to replace all occurrences.
6. Open the `ei_websdk_sample.html` file using Live Server in Visual Studio Code.
