---
uid: developers/downloads/android-java-sample
title: Run Android (Java) SDK Sample
author: ruthaisabokhae
description: Run Android (Java) SDK Sample
ms.author: ruthai
ms.date: 09/27/2019
ms.service: product-insights
ms.topic: conceptual
---

# Run Product Insights Android (Java) SDK Sample
## Prerequisites
- Android Studio
- Ingestion Key (See [here](android-java.md) for instructions on how to obtain)

## Run Sample
1. [Download](https://download.pi.dynamics.com/sdk/ProductInsightsSamples/pi_android_sample.zip) the **Product Insights Android (Java) SDK sample**.
2. Unzip the compressed file `pi_android_sample.zip`.
3. Open Android Studio.
4. Select **File > Open...**.
5. Choose the decompressed **pi-android-sample** project.
6. Gradle sync should happen automatically. If not, select **File > Sync Project with Gradle Files**.
7. Wait until Gradle successfully finishes building.
8. Go to **app/java/microsoft.dynamics.productinsights.androidsample/MainActivity**.
9. Replace *YOUR_INGESTION_KEY* with the ingestion key you have created on Product Insights portal.
10. Select **Run > Run 'app'**.
11. Wait a few minutes and you should be able to see signals under your project on the Product Insights portal.