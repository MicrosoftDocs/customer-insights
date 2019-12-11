---
uid: developers/downloads/ios-objc
title: iOS (ObjC & Swift)
author: ruthaisabokhae
description: iOS (ObjC & Swift)
ms.author: ruthai
ms.date: 04/12/2019
ms.service: product-insights
ms.topic: conceptual
---

# Getting started with the Product Insights SDK for Objective-C
[!INCLUDE [cc-beta-prerelease-disclaimer]( includes/cc-beta-prerelease-disclaimer.md)]

This tutorial will guide you through the process of using a Product Insights ingestion key and the Product Insights SDK for your existing Objective-C application, which will allow you to see signals in the portal in five minutes or sooner.

The following scenario will be used to construct the Product Insights SDK example: you work at a car manufacturing company, and the company has just released a new car. You want to know how the car is performing, the demographics of users, and their driving habits. Product Insight allows you to achieve these goals by sending real time signals and generating valuable insights with only a few simple steps.


## Prerequisites
* Xcode 10+
* iOS 9+
* MacOS 10.12+
* Ingestion key (see below for instructions to obtain)

## Get an ingestion key from Product Insights portal
1. From the [pi.dynamics.com](http://pi.dynamics.com) home screen, select your team from the left panel. If you do not already have a team, refer to [Create a team](xref:developers/quick-starts/create-a-team).
2. Add a new project to your team by selecting the **+ New Project** button from the top right corner.
3. Type in a project name in the **Name** field and any other text for **Description**. Select **Create** to commit the update.
4. Once your project is created, select the project.
5. Select **Settings** under your project. Your ingestion key is available under **Ingestion Key**.

> [!NOTE]
> Leave this tab open in your web browser, or copy the key to a clipboard because you will need to use it later.

## Integrate the Product Insights SDK into your Objective-C project

### Integrate the AppCenter SDK using CocoaPods
1. If you haven't installed CocoaPods, run this command in the terminal to install CocoaPods and create a Podfile:
    ```bash
    $ sudo gem install cocoapods
    $ pod init
    ```
2. Add the following to your Podfile:
    ```bash
    target 'SampleApp' do
        pod 'AppCenter/Analytics'
    ```
3. Save the file and run this command in the terminal:
    ```bash
    $ pod install
    ```

### Integrate the Product Insights Analytics SDK Manually
1. [Download](https://download.pi.dynamics.com/sdk/ProductInsightsSenders/pi_objc_sdk.zip) the **Product Insights Analytics Objective-C SDK** for iOS and macOS.
2. Unzip the SDK archive and copy the corresponding framework:
    * For iOS, navigate to the *iOS* folder
        * For debug version, navigate to the *Debug* folder
            * For simulator, navigate to the *Simulator* folder
                * Copy the **ProductInsightsAnalytics.framework**
            * For device, navigate to the *Device* folder
                * Copy the **ProductInsightsAnalytics.framework**
        * For release version, navigate to the *Device* folder
            * For simulator, navigate to the *Simulator* folder
                * Copy the **ProductInsightsAnalytics.framework**
            * For device, navigate to the *Device* folder
                * Copy the **ProductInsightsAnalytics.framework**
    * For macOS, navigate to the *macOS* folder
        * For debug version, navigate to the *Debug* folder
            * Copy the **ProductInsightsAnalyticsMacOS.framework**
        * For release version, navigate to the *Release* folder
            * Copy the **ProductInsightsAnalyticsMacOS.framework**
2. Integrate the SDK into your project
    1. Copy the corresponding framework from the step above.
    2. Create a new folder named **Frameworks** inside your project folder, and paste the framework into this.
    3. Select your project in Xcode's project navigator.
    4. Select your app target.
    5. In the **General** tab add the `ProductInsightsAnalytics.framework` (for iOS) or `ProductInsightsAnalyticsMacOS.framework` (for macOS) to **Embedded Binaries**.

### Import Product Insights Analytics and AppCenter into your project
1. Open your `AppDelegate.m` file, and add the following import statements:
    ```objc
    @import AppCenter;
    @import AppCenterAnalytics;

    // if iOS use:
    #import <ProductInsightsAnalytics/ProductInsightsAnalytics.h>

    // if macOS use:
    #import <ProductInsightsAnalyticsMacOS/ProductInsightsAnalyticsMacOS.h>
    ```


### Add the start method and start tracking events.
1. Start the SDK from an app (only required once). Follow these steps:
    * Insert the following lines to start the SDK in your app's `AppDelegate.m` class in the `didFinishLaunchingWithOptions:` method:
        ```objc
        [MSAppCenter start:@"target=Your_Ingestion_Key" withServices:@[[MSAnalytics class]]];
        ```
    * If your application already uses the Microsoft AppCenter SDK to track telemetry:
        ```objc
        [MSAppCenter start:@"app-secret=Your_App_Secret; target=Your_Ingestion_Key" withServices:@[[MSAnalytics class]]];
        ```

2. Insert the following line to initiate Product Insights Analytics:
    ```objc
    PIAnalytics *piAnalytics = [[PIAnalytics new] initWithIngestionKey:Your_Ingestion_Key];
    ```

3. Insert the following lines to track signals:
    ```objc
    // Signal with name only
    PISignal *signal = [[PISignal new] initWithName:@"user_information"];
    [piAnalytics trackSignal:signal];

    // Signal with custom properties of various types
    PISignal *sampleSignal = [[PISignal new] initWithName:@"car_information"];
    sampleSignal.version = @"1.0.0";

    [sampleSignal setStringValue:@"Star Car" forProperty:@"car_model"];
    [sampleSignal setDoubleValue:76.5 forProperty:@"temperature"];
    [sampleSignal setInt64Value:3000 forProperty:@"rpm"];
    [sampleSignal setBoolValue:YES forProperty:@"engine_start"];

    [piAnalytics trackSignal:sampleSignal];
    ```

    The following types are supported for custom signal properties:
    - **NSString**
    - **NSDate**
    - **double**
    - **int64_t**
    - **BOOL**
