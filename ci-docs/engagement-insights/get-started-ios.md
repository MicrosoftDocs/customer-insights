---
title: Get Started with iOS SDK
description: Getting started with the iOS SDK
author: britl
ms.reviewer: m-hartmann
ms.author: v-salash
ms.date: 04/23/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---
# Get started with the iOS SDK

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

This tutorial guides you through the process of instrumenting your iOS application with an engagement insights SDK. You'll start seeing events in your portal in five minutes or sooner.

## Configuration options
The following configuration options can be passed to the SDK through the provided `EIConfig.plist` file:
- **ingestionKey**: The ingestion key used to send events to your project.
- **autocollectAction**: A boolean value to enable/disable auto instrumentation of the action event.
- **autocollectView**: A boolean value to enable/disable auto instrumentation of the view event.
- **endpointUrl**: The endpoint url where the events will be directed.

## Prerequisites
* Xcode 9+
* iOS 8.2+
* An ingestion key (see below for instructions on how to obtain)

## Integrate the engagement insights SDK into your application

1. From the engagement insights home screen, select your project from the project dropdown on the left navigation pane. If you don't already have a project, select the **+ New Project** option instead and create one.

2. Once a project is created, go to **Data** and then **Code**. The ingestion key will be available under **ingestionkey**. Copy the ingestion key.

3. Download the [engagement insights iOS SDK](https://download.pi.dynamics.com/sdk/EI-SDKs/ei-ios-sdk.zip), and place the `EIObjC.xcframework` file in the `Frameworks` folder.
* If a `Frameworks` folder does not exist already create one in the project folder

### Zero code implementation with auto instrumentation

4. If you would like to enable auto instrumentation without any coding, update and include the provided `EIConfig.plist` file in your project directory folder for the following fields:
    * ingestionKey = `"Your-Ingestion-Key"`
    * autocollectView = YES
    * autocollectAction = YES

5. Then add the `EIConfig.plist` file to your project in Xcode. When the project runs it will automatically track the Action and View events using the configured ingestion key.

### Custom event implementation

4. Open your project in Xcode, and navigate to the 'General' settings. Add the `EIObjC.xcframework` to the project under the 'Frameworks, Libraries, and Embedded Content' section.

5. Import the framework header file in AppDelegate.m with the following snippet:
    ```objectivec
    #import <EIObjC/EIObjC.h>
    ```

6. Initialize the engagement insights SDK from application:didFinishLaunchingWithOptions: and replace `"Your-Ingestion-Key"` with the one created from Step 2:
    ```objectivec
    NSError *error = [NSError new];
    id<EIIAnalytics> analytics = [EIAnalyticsProvider analyticsForIngestionKey:@"Your-Ingestion-Key" error:&error];
    ```

7. Track an event:
    ```objectivec
    EIEvent *event = [EIEvent new];
    event.name = @"video.log";
    [event setLongValue:320 forKey:@"duration"];
    [event setBoolValue:YES forKey:@"ad_shown"];
    [analytics trackEvent:event];
    ```

## Enable/Disable auto instrumentation
Engagement insights iOS SDK supports auto instrumentation and auto collection of `view` and `action` events. If you would like to enable or disable auto instrumentation, update the following fields in the included `EIConfig.plist` file in your project directory folder. 
```objectivec
'autocollectView' = YES (to enable) / NO (to disable)
'autocollectAction' = YES (to enable) / NO (to disable)
```

## Setting user details for your signal

The engagement insights SDK lets you define user information that can be sent with every event. You can specify user information by calling the `setUser:(nonnull EIUser *)user` API on the SDK.

Specifying user details on the `Analytics` level means that all telemetry will have this information. However, if specified on the event level by calling the `setUser:(nonnull EIUser *)user` API on the EIEvent object, only that specific event will contain the information.

The `EIUser` data class contains the following NSString properties:

- **localId**: The user's local ID.
- **authId**: The authenticated user ID.
- **authType**: The authentication type used to the get authenticated user ID.
- **name**: The user's name.
- **email**: The user's email address.
