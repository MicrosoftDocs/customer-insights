---
uid: developers/downloads/android-java
title: Get Started with Android (Java)
author: ruthaisabokhae
description: Get Started with Android (Java)
ms.author: ruthai
ms.date: 04/12/2019
ms.service: product-insights
ms.topic: conceptual
---
# Getting started with Android (Java) 
 
## Prerequisites 
Prerequisites
* Android Studio
* Minimum Android API Level: 16 (Jelly Bean)
* Instrumentation Key (get from [pi.dynamics.com](http://pi.dynamics.com)>team>project>settings – copy the Ingestion Key)

## Integrate
1. Open your project. If you don't have one, create a new project with Empty activity in Android Studio.
2. Open the app level `build.gradle` file (`app/build.gradle`) and add the following lines after "Apply plugin" to include the dependencies for the project:

```java
dependencies { 
    def appCenterSdkVersion = '1.11.0' 
    implementation "com.microsoft.appcenter:appcenter-analytics:${appCenterSdkVersion}" 
}
```

3. Gradle sync.
4. Open your app's main activity class and import:

```java
import com.microsoft.appcenter.AppCenter; 
import com.microsoft.appcenter.analytics.Analytics; 
```

5. Start the sender (it's only required to start it once): 
6. Replace `Your-API-Token` with your project's instrumentation key.

```java
// The first parameter is the application context, this examples assumes it is called from an Activity. 
AppCenter.start(getApplication(), "target={Your-API-Token}", Analytics.class); 
```
7. Create a signal : 

```java
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
- **String** 
- **Date** 
- **double** 
- **long** 
- **boolean**
