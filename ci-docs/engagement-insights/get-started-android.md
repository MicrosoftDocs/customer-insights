---
title: Get started with Android SDK
description: Learn how to personalize and run the Android SDK
author: britl
ms.reviewer: mhart
ms.author: britl
ms.date: 10/19/2021
ms.service: customer-insights
ms.subservice: engagement-insights
ms.topic: conceptual
ms.manager: shellyha
---

# Get started with the Android SDK

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

This tutorial guides you through the process of instrumenting your Android application with a Dynamics 365 Customer Insights engagement insights SDK. You'll start seeing events in your portal in five minutes or sooner.

## Configuration options
The following configuration options can be passed to the SDK:

- **ingestionKey**: The ingestion key is used to send events to your workspace.

## Prerequisites

- Android Studio

- Minimum Android API Level: 16 (Jelly Bean)

- An ingestion key (see below for instructions on how to obtain)

## Integrate the SDK into your application
Begin the process by selecting a workspace, selecting the Android mobile platform, and downloading the Android SDK.

- Use the workspace switcher in the left navigation pane to select your workspace.

- If you don't have an existing workspace, select  **New Workspace** and follow the steps to create a [new workspace](create-workspace.md).

- After you create a workspace, go to **Admin** > **Workspace** and then select  **Installation guide**.

## Configure the SDK

Once you download the SDK, you can work with it in Android Studio to enable and define events. There are two ways to do so:
### Option 1: Use JitPack (recommended)
1. Add the JitPack repository to your root `build.gradle`:
    ```gradle
    allprojects {
        repositories {
            ...
		    maven { url 'https://jitpack.io' }
	    }
    }
    ```

1. Add the dependency:
    ```gradle
    dependencies {
        implementation 'com.github.microsoft:engagementinsights-sdk-android:v1.0.0'
        api 'com.google.code.gson:gson:2.8.1'
    }
    ```

### Option 2: Use download link
1. Download the [engagement insights Android SDK](https://download.pi.dynamics.com/sdk/EI-SDKs/ei-android-sdk.zip), and place the `eiandroidsdk-debug.aar` file in the `libs` folder.

1. Open your project level `build.gradle` file and add the following snippets:
    ```gradle
    dependencies {
        implementation(name: 'eiandroidsdk-debug', ext: 'aar')
        api 'com.google.code.gson:gson:2.8.1'
    }

    repositories {
        flatDir {
            dirs 'libs'
        }
    }
    ```

## Enable auto-instrumentation

1. Add permission for network and internet in your `AndroidManifest.xml` file located under the `manifests` folder.
    ```xml
    <manifest>
        ...
        <uses-permission android:name="android.permission.INTERNET" />
        <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    ```

1. Set up the engagement insights SDK configuration through your `AndroidManifest.xml` file.

1. Copy the XML snippet from the **Installation guide**. `Your-Ingestion-Key` should be automatically populated.

   > [!NOTE]
   > You don't need to replace the `${applicationId}` section. It is automatically populated.


   ```xml
   <application>
   ...
       <provider
           android:authorities="${applicationId}.com.microsoft.engagementinsights.AnalyticsContentProvider"
           android:name="com.microsoft.engagementinsights.AnalyticsContentProvider" />
       <meta-data
           android:name="com.microsoft.engagementinsights.ingestionKey"
           android:value="Your-Ingestion-Key" />
       <meta-data
           android:name="com.microsoft.engagementinsights.autoCapture"
           android:value="true" />
   ...
   </application>
   ```

1. Enable or disable autocapture of `View` events by setting the above `autoCapture` field to `true` or `false`. 

   >[!NOTE]
   >`Action` events need to be added manually.

1. (Optional) Other configurations include setting the endpoint collector URL. They can be added under the ingestion key metadata in `AndroidManifest.xml`.

   ```xml
        <meta-data
            android:name="com.microsoft.engagementinsights.endpointUrl"
            android:value="https://some-endpoint-url.com" />
   ```

## Implement custom events

After you initialize the SDK, you can work with events and their properties in the `MainActivity` environment.


Java:
```java
Analytics analytics = new Analytics();
```

Kotlin:
```kotlin
var analytics = Analytics()
```

### Set property for all events (optional)

Java:
```java
analytics.setProperty("year", 2021);
```

Kotlin:
```kotlin
analytics.setProperty("year", 2021)
```

The following types are supported for context event properties:
- String
- Date
- Double
- Long
- Boolean
- UUID

### Track an event

Java:
```java
Event event = new Event("video");
event.setProperty("duration", 320);
event.setProperty("ad_shown", true);
analytics.trackEvent(event);
```

Kotlin:
```kotlin
var event = Event("video")
event.setProperty("duration", 320)
event.setProperty("ad_shown", true)
analytics.trackEvent(event)
```

## Set user details for your event (optional)

The SDK lets you define user information that can be sent with every event. You can specify user information by calling `setUser(user: User)` API on the `Analytics` level.

Java:
```java
User user = new User();
user.setName("testuser");
user.setEmail("abc@xyz.com");
analytics.setUser(user);
```

Kotlin:
```kotlin
var user = User()
user.name = "testuser"
user.email = "abc@xyz.com"
analytics.setUser(user)
```

The `User` data class contains the following string properties:

- **localId**: The user's local ID.
- **authId**: The authenticated user ID.
- **authType**: The authentication type used to the get authenticated user ID.
- **name**: The user's name.
- **email**: The user's email address.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
