---
title:  Android SDK Sample
description: Sample project to learn about the Android SDK
author: britl
ms.reviewer: m-hartmann
ms.author: v-salash
ms.date: 05/07/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---


# Run the Android SDK sample

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

This sample Android project helps you understand how the SDK works in an app. You don’t have to write code. Just add your ingestion key and you can see events in your workspace right away.

## Prerequisites

- [Android Studio](https://developer.android.com/studio)
- [Ingestion key](get-started-android.md)

## Download the Android SDK sample

1. [Download the engagement insights Android SDK sample](https://download.pi.dynamics.com/sdk/EI-SDKs/ei-android-sample.zip).
1. Unzip the compressed file `ei-android-sample.zip`.
1. Open the unzipped folder in Android Studio.
1. In the `AndroidManifest.xml` file, replace the string `"Your-Ingestion-Key"` with your workspace ingestion key from engagement insights under **Admin** > **Workspace** > **Installation guide**. 

 > [!NOTE]
   > You don't need to replace the  `${applicationId}` section. It is automatically populated.

```xml
<provider
    android:authorities="${applicationId}.microsoft.dynamics.engagementinsights.eiandroidsdk.AnalyticsContentProvider"
    android:name="microsoft.dynamics.engagementinsights.eiandroidsdk.AnalyticsContentProvider" />
<meta-data
    android:name="microsoft.dynamics.engagementinsights.ingestionKey"
    android:value="Your-Ingestion-Key" />
<meta-data
    android:name="microsoft.dynamics.engagementinsights.autoCapture"
    android:value="true" />
```

5. Select **Run** to start the sample project.
1. View the events in your workspace.



[!INCLUDE[footer-include](../includes/footer-banner.md)]