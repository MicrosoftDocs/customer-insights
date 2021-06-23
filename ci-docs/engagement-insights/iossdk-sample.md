---
title:  Run the iOS SDK sample
description: Sample project to learn about the iOS SDK
author: britl
ms.reviewer: mhart
ms.author: britl
ms.date: 06/23/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---

# Run the iOS SDK sample

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

This sample iOS project helps you understand how the SDK works in an app. You don’t have to write code. Just add your ingestion key and you can see events in your workspace right away.

## Prerequisites

- [Xcode version 9+](https://developer.apple.com/xcode/downloads/)
- [Ingestion key](get-started-ios.md)

## Download the iOS SDK sample

1. [Download the engagement insights iOS SDK sample](https://download.pi.dynamics.com/sdk/EI-SDKs/ei-ios-sample.zip).
1. Unzip the compressed file `ei-ios-sample.zip`.
1. Open the sample app project in Xcode.
1. In the `EIConfig.plist` file, replace the string `“YOUR-INGESTION-KEY”` in the field `ingestionKey` with your workspace ingestion key from engagement insights under **Admin** > **Workspace** > **Installation guide**.
1. Select **Run** to start the sample project.
1. View the events in your workspace.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
