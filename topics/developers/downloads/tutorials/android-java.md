---
uid: developers/downloads/android-java
title: Get Started with Android (mobile)
---
# Getting started with the 1DS SDK for Android (Java) 
 
This tutorial guides you through the process of using an Aria ingestion token and the 1DS SDK for your existing app, which will have you tracking events in about five minutes. 
 
## Prerequisites 
- Android Studio 
- Minimum Android API Level: 16 (Jelly Bean)  
 
## 1. Get an API token from Aria portal 
a. From the **Home** screen in the Portal, click **Explorer** in the navigation pane on the left. The **Projects List** appears.

b. Add a new project by clicking the plus sign at the bottom of the list. The **Instrument Wizard** appears, displaying the **Create a project** page.

c. Enter a name for your project.

d. Leave the default value of Sandbox for **Group**.

e. Select **Create project**. The **What platform are you using?** page appears.

f. Pick a platform from the drop-down list, but don’t click **Next**. Click **Skip this wizard** instead, and the **Project Manager** page appears.

g. Your API token appears on the right side of this page, under **Ingestion Key**. Leave this tab open in your web browser because you will come back to it and copy it to the clipboard for use later. 
 
## 2. Integrate the SDK into your project 
a. Open your project. If you don't have one, create a new project with Empty Activity in Android Studio.

b. Open the app level `build.gradle` file (`app/build.gradle`) and add the following lines after apply plugin to include the dependencies for project:
```
dependencies { 
    def appCenterSdkVersion = '1.11.0' 
    implementation "com.microsoft.appcenter:appcenter-analytics:${appCenterSdkVersion}" 
} 
```
c. Gradle Sync.

d. Open your app's main activity class and import: 
```
import com.microsoft.appcenter.AppCenter; 
import com.microsoft.appcenter.analytics.Analytics; 
```

e. Start the SDK (it's only required to start it once): 
```
// The first parameter is the application context, this examples assumes it is called from an Activity. 
AppCenter.start(getApplication(), "target={Your-API-Token}", Analytics.class); 
```

f. Track events : 
```
// Do a simple trackEvent call. 
Analytics.trackEvent("my_simple_event_name"); 
 
// Track an event with properties of various types. 
EventProperties properties = new EventProperties(); 
properties.set("Name", "Ashley Smith"); 
properties.set("School", "Bellevue High School"); 
properties.set("Grade", 11); 
properties.set("Gpa", 3.82); 
properties.set("Birthday", new Date(800320249)); 
properties.set("Suspended", false); 
Analytics.trackEvent("StudentInformation", properties); 
```

The following types are supported for event properties: 
- String 
- Date 
- double 
- long 
- boolean
