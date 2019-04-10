---
uid: developers/downloads/ios-objc
title: iOS (mobile)
author: vroha
description: iOS (mobile)
ms.author: v-roha
ms.date: 03/29/2019
ms.service: dynamics-365-crossapp
ms.topic: conceptual
---

# Getting started with iOS (ObjC & Swift) 
 
This tutorial guides you through the process of using an Product Insights ingestion token and the 1DS SDK for your existing app, which will have you tracking events in about five minutes. 
 
Prerequisites:
- [Xcode 8.3.3+](https://developer.apple.com/xcode/downloads/) 
- macOS 10.12+ 
- iOS 9+ 
- [API token](xref:developers/downloads/api-token)

## Integrate the 1DS iOS SDK into your project and instrument your app

### Option 1: Integrate the SDK using CocoaPods

1. If you haven't installed CocoaPods, run the following command in the terminal to install CocoaPods and create a Podfile:

```Terminal
$ sudo gem install cocoapods 
$ pod init 
```

2. Add the following code snippet to your Podfile:

```Podfile
Target 'SampleApp' do 
pod 'AppCenter' 
pod 'AppCenter/Analytics' 
```

3. Save the file and run the following command in the terminal:

```Terminal
$ pod install
```
 
### Option 2: Integrate the SDK manually

1. Download the 1DS SDK for iOS. 

2. The SDK is available as a ZIP file. [Download the iOS SDK.](https://github.com/Microsoft/AppCenter-SDK-Apple/releases/latest) 

3. Integrate the SDK into your project. In this step, you’ll configure your project to link the 1DS SDK libraries. 
- Ensure that your project has modules enabled. 
- Unzip the SDK archive and copy the `AppCenter.framework` and `AppCenterAnalytics.framework` frameworks from the iOS folder. 
- Create a new folder named `Frameworks` inside your project folder, and paste the frameworks into it.
- Add the SDK frameworks to the project in Xcode: 
    * Drag and drop all the frameworks into Xcode's Project Navigator. 
    * A dialog will appear. Ensure your app target is checked, and then click **Finish**. 
- Ensure the frameworks have been added to the project and target correctly. 
    * Select your project in Xcode's project navigator. 
    * Select your app target. 
    * In the **General** tab, verify that 
        - None of the `.framework` files have been added to **Embedded Binaries**. 
        - The section **Linked Frameworks and Libraries** contains all frameworks. Remove duplicates and add missing frameworks if necessary.
    * In the **Build Phases** tab, verify that 
        - All `.framework` files have been added to **Link Binary With Libraries**. 
        - None of the `.framework` files have been added to **Embed Frameworks**. 
    > Note that all `.framework` files are distributed as statically linked, "fake" frameworks.

4. Open your `AppDelegate.m` file and add the following import statements:

**Objective-C:**

```obj-c
@import AppCenter; 
@import AppCenterAnalytics;
```

**Swift:**
```swift
import AppCenter 
import AppCenterAnalytics 
```

5. Add the **start method** and **start tracking** events. 
 - Start the SDK from an app. 
 - Insert the following code to start the SDK in your app's `AppDelegate.m` class in the `didFinishLaunchingWithOptions:` method. Use this if you only have a single target configured.

**Objective-C:**

```obj-c
[MSAppCenter start:@"target={Your API Token}" withServices:@[[MSAnalytics class]]]; 

// Do a simple trackEvent call 
[MSAnalytics trackEvent:@"eventName"]; 
 
// Track an event with various property types 
MSEventProperties *properties = [MSEventProperties new]; 
[properties setString:@"Music" forKey:@"Category"]; 
[properties setDouble:3.23 forKey:@"LengthMinutes"]; 
[properties setInt64:193800 forKey:@"LenthMs"]; 
[properties setBool:YES forKey:@"InLibrary"]; 
[properties setDate:[NSDate new] forKey:@"DateAdded"]; 
[MSAnalytics trackEvent:@"VideoClicked" withTypedProperties:properties]; 
```

**Swift:**
```swift   
MSAppCenter.start("target={Your API token}", withServices:[MSAnalytics.self]) 
 
// Do a simple trackEvent call. 
MSAnalytics.trackEvent("eventname") 
 
// Track an event with properties. 
let properties = MSEventProperties() 
properties.setEventProperty("Music", forKey:"Category") 
properties.setEventProperty(3.23, forKey:"LengthMinutes") 
properties.setEventProperty(193800, forKey:"LengthMs") 
properties.setEventProperty(true, forKey:"InLibrary") 
properties.setEventProperty(Date(), forKey:"DateAdded") 
MSAnalytics.trackEvent("VideoClicked", withProperties:properties) 
```
 
 - Use this code to configure multiple projects or telemetry endpoints:

**Objective-C:**

```obj-c
// Create your first transmission target. 
MSAnalyticsTransmissionTarget *appTarget1 = [MSAnalytics transmissionTargetForToken:@"Your API token 1"]; 
 
// Do a simple trackEvent call for your first target. 
[appTarget1 trackEvent:@"eventname"]; 
 
// Track an event with properties on your first target. 
MSEventProperties *properties = [MSEventProperties new]; 
[properties setString:@"Music" forKey:@"Category"]; 
[properties setDouble:3.23 forKey:@"LengthMinutes"]; 
[appTarget1 trackEvent:@"VideoClicked" withTypedProperties:properties]; 
 
// Create your second transmission target. 
MSAnalyticsTransmissionTarget *appTarget2 = [MSAnalytics transmissionTargetForToken:@"Your API token 2"]; 
 
// Do a simple trackEvent call for your second target. 
[appTarget2 trackEvent:@"eventname"]; 
 
// Track an event with properties on your second target. 
MSEventProperties *properties = [MSEventProperties new]; 
[properties setString:@"Music" forKey:@"Category"]; 
[properties setDouble:3.23 forKey:@"LengthMinutes"]; 
[appTarget2 trackEvent:@"VideoClicked" withTypedProperties:properties]; 
```

**Swift:**

```swift
// Create your first transmission target. 
let appTarget1 = MSAnalytics.transmissionTarget(forToken:"our API token 1") 
 
// Do a simple trackEvent call for your first target. 
appTarget1.trackEvent("eventname"); 
 
// Track an event with properties in your first target. 
let properties = MSEventProperties() 
properties.setEventProperty("Music", forKey:"Category") 
properties.setEventProperty(3.23, forKey:"LengthMinutes") 
appTarget1.trackEvent("eventName", withProperties:properties) 
 
// Create your second transmission target. 
let appTarget2 = MSAnalytics.transmissionTarget(forToken: "our API token 2") 
 
// Do a simple trackEvent call for your second target. 
appTarget2.trackEvent("eventname"); 
 
// Track an event with properties on your second target. 
let properties = MSEventProperties() 
properties.setEventProperty("Music", forKey:"Category") 
properties.setEventProperty(3.23, forKey:"LengthMinutes") 
appTarget2.trackEvent("eventName", withProperties:properties) 
```
 
You’re done! When you run your app or library, it will send a telemetry event when it launches. 
