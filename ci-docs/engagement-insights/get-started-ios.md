---
title: Get started with iOS SDK
description: Learn how to personalize and run the iOS SDK
author: britl
ms.reviewer: m-hartmann
ms.author: v-salash
ms.date: 05/07/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: conceptual
ms.manager: shellyha
---


<!-- Just checking ... There's a level## step 1 and step 2. Should the other level## headings also be steps? -->



# Get started with the iOS SDK

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

This tutorial guides you through instrumenting your iOS application with a Dynamics 365 Customer Insights engagement insights SDK. You'll start seeing events in your portal in five minutes or sooner.

## Configuration options

The following configuration options can be passed to the SDK through the provided `EIConfig.plist` file:

- **ingestionKey**: The ingestion key used to send events to your project.
- **autocollectAction**: A Boolean value to enable or disable auto-instrumentation of the action event.
- **autocollectView**: A Boolean value to enable or disable auto-instrumentation of the view event.
- **endpointUrl**: The endpoint URL where the events will be directed.

## Prerequisites

- Xcode version 9+
- iOS version 8.2+
- An ingestion key (see the instructions below to obtain)

## Step 1. Integrate the SDK into your application

Begin the process by selecting a workspace to work in, selecting the iOS mobile platform, and downloading the SDK.

- Use the workspace switcher in the left navigation pane to select your workspace.

- If you don't have an existing workspace, select  **New Workspace** and follow the steps to create a [new workspace](create-workspace.md).

## Step 2. Configure the SDK

Once you download the SDK, you can work with it in Xcode to enable and define events.

1. After you create a workspace, go to **Admin** > **Workspace** and then select **Installation guide**.


1. Download the [engagement insights iOS SDK](https://download.pi.dynamics.com/sdk/EI-SDKs/ei-ios-sdk.zip), and place the `EIObjC.xcframework` file in the `Frameworks` folder.

1. If a `Frameworks` folder doesn't exist, create one in the project folder.

## Enable auto-instrumentation
 
You can easily enable auto-instrumentation without coding. When the project runs, it will automatically track the `view` and `action` events using the configured ingestion key. 

1. Update and include the provided `EIConfig.plist` file in your project directory folder for the following fields:
    - ingestionKey = `"Your-Ingestion-Key"`
    - autocollectView = YES
    - autocollectAction = YES

2. Then add the `EIConfig.plist` file to your project in Xcode. 



To disable auto-instrumentation, update the following fields in the included `EIConfig.plist` file in your project directory folder. 

```objectivec
'autocollectView' = NO (to disable)
'autocollectAction' = NO (to disable)
```


## Implement custom events

1. Open your project in Xcode, and navigate to **General** settings. 
1. Add the `EIObjC.xcframework` to the project under the 'Frameworks, Libraries, and Embedded Content' section.

1. Import the framework header file in AppDelegate.m with the following snippet:

    ```objectivec
    #import <EIObjC/EIObjC.h>
    ```

1. Initialize the engagement insights SDK from the application: didFinishLaunchingWithOptions.
1. Copy the XML snippet from the **Installation guide**.

    ```objectivec
    NSError *error = [NSError new];
    id<EIIAnalytics> analytics = [EIAnalyticsProvider analyticsForIngestionKey:nil error:&error];
    ```

1. Track an event:

    ```objectivec
    EIEvent *event = [EIEvent new];
    event.name = @"video.log";
    [event setLongValue:320 forKey:@"duration"];
    [event setBoolValue:YES forKey:@"ad_shown"];
    [analytics trackEvent:event];
    ```

## Set user details for your event

The SDK lets you define user information that can be sent with every event. You can specify user information by calling the `setUser:(nonnull EIUser *)user` API on the SDK.

Specifying user details on the `Analytics` level means that all telemetries will have this information. However, if you specify on the event level by calling the `setUser:(nonnull EIUser *)user` API on the EIEvent object, only that specific event will contain the information.

The `EIUser` data class contains the following NSString properties:

- **localId**: The user's local ID.
- **authId**: The authenticated user ID.
- **authType**: The authentication type used to get the authenticated user ID.
- **name**: The user's name.
- **email**: The user's email address.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
