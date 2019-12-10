---
uid: developers/downloads/android-java
title: Get Started with Android (Java)
author: ruthaisabokhae
description: Get Started with Android (Java)
ms.author: ruthai
ms.date: 09/04/2019
ms.service: product-insights
ms.topic: conceptual
---
# Getting started with the Product Insights SDK for Android (Java)
[!INCLUDE [cc-beta-prerelease-disclaimer]( includes/cc-beta-prerelease-disclaimer.md)]

This tutorial will guide you through the process of using a Product Insights ingestion key and the Product Insights SDK for your existing Android application, which will allow you to see signals in the portal in five minutes or sooner.

The following scenario will be used to construct the Product Insights SDK example: you work at a car manufacturing company, and the company has just released a new car. You want to know how the car is performing, the demographic of users, and their driving habits. Product Insight allows you to achieve these goals by sending real-time signals and generating valuable insights with only a few simple steps.

## Prerequisites
* Android Studio
* Minimum Android API Level: 16 (Jelly Bean)
* Ingestion key (see below for instructions to obtain)

## Get an ingestion key from Product Insights portal
1. From the [pi.dynamics.com](http://pi.dynamics.com) home screen, select your team from the left panel. If you do not already have a team, refer to [Create a team](xref:developers/quick-starts/create-a-team).
2. Add a new project to your team by selecting the **+ New Project** button from the top right corner.
3. Type in a project name in the **Name** field and any other text for **Description**. Select **Create** to commit the update.
4. Once your project is created, select the project.
5. Select **Settings** under your project. Your ingestion key is available under **Ingestion Key**.

> [!NOTE]
> Leave this tab open in your web browser, or copy the key to a clipboard because you will need to use it later.

## Integrate the Product Insights SDK into your Android project
1. Open your Android Studio project. If you don't have one, create a new project with **Empty Activity** in Android Studio.

2. Import the Product Insights Android SDK:
    * [Download](https://download.pi.dynamics.com/sdk/ProductInsightsSenders/pi_android_sdk.zip) the **Product Insights Android Java SDK**.
    * Unzip the compressed file `pi_android_sdk.zip`
    * Copy the Android archive file (extension: `.aar`) into your project's `app/libs` folder.

3. Open the app level `build.gradle` file (`app/build.gradle`), and add the following lines after ```apply plugin``` to first include the AppCenter SDK dependencies for the project:

    ```java
    dependencies {
        def appCenterSdkVersion = '2.2.0'
        implementation "com.microsoft.appcenter:appcenter-analytics:${appCenterSdkVersion}"
    }
    ```
4. Include the Product Insights SDK library as a dependency, and declare the `/libs` folder as a dependency repository:

    ```java
    dependencies {
        ...
        implementation(name: 'pi-android', ext: 'aar')
        ...
    }

    repositories {
        flatDir {
            dirs 'libs'
        }
    }
    ```
5. Gradle sync.

6. Open your app's main activity class and import:

    ```java
    import com.microsoft.appcenter.AppCenter;
    import com.microsoft.appcenter.analytics.Analytics;

    import microsoft.dynamics.productinsights.ProductInsightsAnalytics;
    import microsoft.dynamics.productinsights.Signals;
    ```

7. Start the SDK (only required to start it once):

    ```java
    // The first parameter is the application context, this examples assumes it is called from an Activity.
    AppCenter.start(getApplication(), "target=Your-Ingestion-Key", Analytics.class);
    ```

    If your application already uses the Microsoft AppCenter SDK to track telemetry:
    ```java
    // The first parameter is the application context, this examples assumes it is called from an Activity.
    AppCenter.start(
        getApplication(),
        "app-secret=Your-AppCenter-Secret;target=Your-Ingestion-Key",
        Analytics.class);
    ```

8. Initialize `ProductInsightsAnalytics`:

    ```java
    ProductInsightsAnalytics pia = new ProductInsightsAnalytics("Your-Ingestion-Key");
    ```

9. Track signals:

    ```java
    // Do a simple trackSignal call.
    pia.trackSignal(new Signal("user_information"));

    // Track a signal with custom properties of various types.
    Signal signal = new Signal("car_information");
    signal.setVersion("1.0.0");

    signal.setProperty("engine_start", true);
    signal.setProperty("car_model", "Star Car");
    signal.setProperty("model_year", "2017");
    signal.setProperty("rpm", 3000);
    signal.setProperty("temperature", 74.3);
    pia.trackSignal(signal);
    ```

    The following types are supported for custom signal properties:
    - **String**
    - **Date**
    - **double**
    - **long**
    - **boolean**
