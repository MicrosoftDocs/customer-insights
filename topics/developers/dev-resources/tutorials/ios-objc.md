---
uid: developers/downloads/ios-objc
title: iOS (ObjC & Swift)
author: vroha
description: iOS (ObjC & Swift)
ms.author: ruthai
ms.date: 04/12/2019
ms.service: product-insights
ms.topic: conceptual
---

# iOS (ObjC & Swift)
 
## Prerequisites:
- [Xcode 8.3.3+](https://developer.apple.com/xcode/downloads/)
- macOS 10.12+ 
- iOS 9+ 
- `Your-API-Token` (get from [pi.dynamics.com](http://pi.dynamics.com)>team>project>settings – copy the Ingestion Key)

## SDK
[Download the iOS SDK](https://github.com/Microsoft/AppCenter-SDK-Apple/releases/latest)

## Integrate
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
1. [Download the iOS SDK](https://github.com/Microsoft/AppCenter-SDK-Apple/releases/latest).
2. Integrate the SDK into your project. In this step, you’ll configure your project to link the 1DS SDK libraries.
    * Ensure that your project has modules enabled.
    * Unzip the SDK archive and copy the AppCenter.framework and AppCenterAnalytics.framework frameworks from the iOS folder.
    * Create a new folder named Frameworks inside your project folder, and paste the frameworks into it.
    * Add the SDK frameworks to the project in Xcode:
        * Drag and drop all the frameworks into Xcode's Project Navigator.
        * A dialog will appear. Ensure your app target is checked, and then click Finish.
    * Ensure the frameworks have been added to the project and target correctly.
        * Select your project in Xcode's project navigator.
        * Select your app target.
        * In the General tab, verify that
            * None of the .framework files have been added to Embedded Binaries.
            * The section Linked Frameworks and Libraries contains all frameworks. Remove duplicates and add missing frameworks if necessary.
        * In the Build Phases tab, verify that
            * All .framework files have been added to Link Binary With Libraries.
            * None of the .framework files have been added to Embed Frameworks.

Note that all .framework files are distributed as statically linked, "fake" frameworks.

3. Open your AppDelegate.m file and add the following import statements:

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

4. Add the **start method** and **start tracking** events.

* Start the SDK from an app.
* Insert the following code to start the SDK in your app's AppDelegate.m class in the **didFinishLaunchingWithOptions:** method. 
* Replace `Your-API-Token` with your project's instrumentation key.

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

You’re done! When you run your app or library, it will send a telemetry event when it launches.
