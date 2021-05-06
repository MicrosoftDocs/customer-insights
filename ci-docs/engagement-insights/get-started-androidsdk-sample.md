# Run the Android SDK sample for Product Insights

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

## Prerequisites

- [Android Studio](https://developer.android.com/studio)
- [Ingestion key](get-started-android.md)

## Run Sample

1. [Download the engagement insights Android SDK sample](https://download.pi.dynamics.com/sdk/EI-SDKs/ei-android-sample.zip).
1. Unzip the compressed file `ei-android-sample.zip`.
1. Open the unzipped folder in Android Studio.
1. In the `AndroidManifest.xml` file, replace the string `"Your-Ingestion-Key"` with your workspace ingestion key from the engagement insights portal under Admin -> Workspace -> Installation Guide. There is *no* need to replace the `${applicationId}` part as it is automatically populated.
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
7. Click **Run** to run the sample project.
8. View the events in your workspace.