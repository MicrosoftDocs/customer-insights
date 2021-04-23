# Get started with the Android SDK

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

This tutorial guides you through the process of instrumenting your Android application with an engagement insights SDK. You'll start seeing signals in your portal in five minutes or sooner.

## Configuration options
The following configuration options can be passed to the SDK:
- **ingestionKey**: The ingestion key used to send signals to your workspace.

## Prerequisites
* Android Studio
* Minimum Android API Level: 16 (Jelly Bean)
* An ingestion key (see below for instructions on how to obtain)

## Integrate the engagement ensights SDK into your application

1. From the engagement insights home screen, select your workspace from the workspace dropdown on the left navigation pane. If you don't already have a workspace, select the **+ New Workspace** option instead and create one.

2. Once workspace is created, go to **Settings** and then **General**. The ingestion key will be available under **Ingestion Key**. Copy the ingestion key.

3. Download the [engagement insights Android SDK](https://download.pi.dynamics.com/sdk/EI-SDKs/ei-android-sdk.zip), and place the `eiandroidsdk-debug.aar` file in the `libs` folder.

4. Open your project level `build.gradle` file and add the following snippets:
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

5. Set up the engagement insights SDK configuration through your `AndroidManifest.xml` file located under the `manifests` folder. Add the following lines under your `<application>` tag and replace `Your-Ingestion-Key` with the key created from Step 2:

    NOTE: There is *no* need to replace the `${applicationId}` part as it is automatically populated.
    ```xml
    <application
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

6. Enable or disable autocapture of `View` events by setting the above `autoCapture` field to `true` or `false`.

6. (Optional) Other configurations include setting the endpoint collector URL. They can be added under the ingestion key metadata in `AndroidManifest.xml`:
    ```xml
        <meta-data
            android:name="com.microsoft.engagementinsights.endpointUrl"
            android:value="https://some-endpoint-url.com" />
    ```


5. Initialize the engagement insights SDK from your MainActivity:
    
    Java:
    ```java
    Analytics analytics = new Analytics();
    ```

    Kotlin:
    ```kotlin
    var analytics = Analytics()
    ```

6. (optional) Set property for all events:
    
    Java:
    ```java
    analytics.setProperty("year", 2021);
    ```

    Kotlin:
    ```kotlin
    analytics.setProperty("year", 2021)
    ```

    The following types are supported for context event properties:
    * String
    * Date
    * Double
    * Long
    * Boolean
    * UUID

6. Track an event:

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

## Setting user details for your event

The engagement insights SDK lets you define user information that can be sent with every event. You can specify user information by calling `setUser(user: User)` API on the `Analytics` level.

    Java:
    ```java
    User user = new User();
    user.setName("testuser");
    user.setEmail("testuser@mail.com");
    analytics.setUser(user);
    ```

    Kotlin:
    ```kotiln
    var user = User();
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