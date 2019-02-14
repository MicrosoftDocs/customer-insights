---
uid: developers/downloads/ios-objc
title: iOS (mobile)
---

# Getting started with the 1DS SDK for iOS (ObjC & Swift) 
 
This tutorial guides you through the process of using an Aria ingestion token and the 1DS SDK for your existing app, which will have you tracking events in about five minutes. 
 
Prerequisites:
- Xcode 8.3.3+ 
- macOS 10.12+ 
- iOS 9+ 
 
## 1. Get an API token from Aria portal 
a. From the **Home** screen in the Portal, select **Explorer** in the navigation pane on the left. The **Projects List** appears. 
b. Add a new project by clicking the plus sign at the bottom of the list. The **Instrument Wizard** appears, displaying the **Create a project** page. 
c. Enter a name for your project. 
d. Leave the default value of **Sandbox** as **Group**. 
e. Select **Create project**. The **What platform are you using?** page appears. 
f. Select a platform from the drop-down list, but don’t select **Next**. Click **Skip this wizard** instead, and the **Project Manager** page appears. 
g. Your API token appears on the right side of this page, under **Ingestion Key**. Leave this tab open in your web browser because you will come back to it and copy your token to the clipboard for use later. 

## 2. Integrate the 1DS iOS SDK into your project and instrument your app 
Option 1: Integrate the SDK using CocoaPods 
If you haven't installed CocoaPods, run this command in the terminal to install CocoaPods and create a Podfile.
```
$ sudo gem install cocoapods 
$ pod init 
```

Add the following to your Podfile
```
Target 'SampleApp' do 
pod 'AppCenter' 
pod 'AppCenter/Analytics' 
```

Save the file and run this command in the terminal:
`$ pod install`
 
Option 2: Integrate the SDK manually 
Download the 1DS SDK for iOS. 
The SDK is available as a ZIP file. Click the following link to download it. 
Download the iOS SDK 
Integrate the SDK into your project In this step, you’ll configure your project to link-in the 1DS SDK libraries. 
Make sure that your project has modules enabled. 
Unzip the SDK archive and copy the AppCenter.framework and AppCenterAnalytics.framework  
frameworks from the iOS folder. 
Create a new folder named Frameworks inside your project folder, and paste the frameworks into this. 
Add the SDK frameworks to the project in Xcode: 
Drag and drop all the frameworks into Xcode's Project Navigator. 
A dialog will appear, make sure your app target is checked. Then click Finish. 
Make sure the .frameworks have been added to the project and target correctly. 
Select your project in Xcode's project navigator. 
Select your app target. 
In the General tab, verify that 
None of the .frameworks have been added to Embedded Binaries. 
The section about Linked Frameworks and Libraries contains all .frameworks. Remove duplicates and add missing frameworks if necessary. 
In the Build Phases tab, verify that 
All .framework files have been added to Link Binary With Libraries. 
None of the .frameworks have been added to Embed Frameworks. 
Note that all .frameworks are distributed as statically linked, "fake" frameworks. 
Open your AppDelegate.m file and add the following import statements:

```
// Objective-C 
@import AppCenter; 
@import AppCenterAnalytics;
```
```
// Swift 
import AppCenter 
import AppCenterAnalytics 
```

Add the start method and start tracking events. 
Start the SDK from an app 
Insert the following line to start the SDK in your app's AppDelegate.m class in the didFinishLaunchingWithOptions: method. Use this if you only have a single target configured.

```
// Objective-C 
[MSAppCenter start:@"target={Your API Token}" withServices:@[[MSAnalytics class]]]; 
```
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
 
   b.  
```   
// Swift 
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
 
Use this code to configure multiple projects or telemetry endpoints: 
// Objective-C 
// Create your first transmission target. 
MSAnalyticsTransmissionTarget *appTarget1 = [MSAnalytics transmissionTargetForToken:@"Your API token 1"]; 
 
// Do a simple trackEvent call for your first target. 
[appTarget1 trackEvent:@"eventname"]; 
 
// Track an event with properties on your first target. 
MSEventProperties *properties = [MSEventProperties new]; 
[properties setString:@"Music" forKey:@"Category"]; 
[properties setDouble:3.23 forKey:@"LengthMinutes"]; 
[appTarget1 trackEvent:@"VideoClicked" withTypedProperties:properties]; 
 
// Create you a second transmission target. 
MSAnalyticsTransmissionTarget *appTarget2 = [MSAnalytics transmissionTargetForToken:@"Your API token 2"]; 
 
// Do a simple trackEvent call for your second target. 
[appTarget2 trackEvent:@"eventname"]; 
 
// Track an event with properties on your second target. 
MSEventProperties *properties = [MSEventProperties new]; 
[properties setString:@"Music" forKey:@"Category"]; 
[properties setDouble:3.23 forKey:@"LengthMinutes"]; 
[appTarget2 trackEvent:@"VideoClicked" withTypedProperties:properties]; 
 
```
// Swift 
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
 
You’re done! When you run your app or library, it sends a telemetry event when it launches. 
