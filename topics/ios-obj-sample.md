---
uid: developers/downloads/ios-objc-sample
title: Run iOS/macOS (Objective-C) SDK Sample
author: ruthaisabokhae
description: Run iOS/macOS (Objective-C) SDK Sample
ms.author: ruthai
ms.date: 12/27/2019
ms.service: product-insights
ms.topic: conceptual
---

# Run Product Insights iOS/macOS (Objective-C) SDK Sample

[!INCLUDE [cc-beta-prerelease-disclaimer]( includes/cc-beta-prerelease-disclaimer.md)]

## Prerequisites

- Xcode
- Ingestion key (see [here](ios-objc.md) for instructions on how to obtain)

## Run Sample

1. [Download](https://download.pi.dynamics.com/sdk/ProductInsightsSamples/pi_objc_sample.zip) the **Product Insights iOS/macOS (Objective-C) SDK sample**.
2. Unzip the compressed file `pi_objc_sample.zip`.
3. Open the **pi_objc_sample** folder.
4. Open the `SampleProductInsightsAnalytics.xcworkspace` file with Xcode.
5. Replace *{YOUR_INGESTION_KEY}* with your ingestion key from the Product Insights portal.
6. Select the simulator device of your choice in the active schema navigation menu in the top left.
7. Select **Run**.
8. Within a few minutes, you should start to see signals entering your project on the Product Insights portal.
