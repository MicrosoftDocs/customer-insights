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

This tutorial will guide you through the process of using a Product Insights ingestion key and the Product Insights SDK for your existing Objective-C application, which will allow you to see signals in the portal in five minutes or sooner.

The following scenario will be used to construct the Product Insights SDK example: you work at a car manufacturing company, and the company has just released a new car. You want to know how the car is performing, the demographics of users, and their driving habits. Product Insight allows you to achieve these goals by sending real time signals and generating valuable insights with only a few simple steps.


## Prerequisites
* Xcode 10+
* iOS 9+
* MacOS 10.12+
* Ingestion key 

## Get an ingestion key from Product Insights portal
1. From the [pi.dynamics.com](http://pi.dynamics.com) home screen, select your team from the left panel. If you do not already have a team, refer to [What is Product Insights?](topics/developers/quick-starts/what-is.md) to create a new team.
2. Add a new project to your team by selecting the **"+ New Project"** button from the top right corner.
3. Type in a project name in the **Name** field and any other text for **Description**. Select **Create** to commit the update.
4. Once your project is created, select the project.
5. Select **Settings** under your project. Your ingestion key is available under **Ingestion Key**. 

> [!NOTE]
> Leave this tab open in your web browser, or copy the key to a clipboard because you will need to use it later.

## Integrate the Product Insights SDK into your Objective-C project

### Option 1: Integrate the AppCenter SDK using CocoaPods
1. If you haven't installed CocoaPods, run this command in the terminal to install CocoaPods and create a Podfile:
	```
	$ sudo gem install cocoapods
	$ pod init
	```
2. Add the following to your Podfile:
	```
	target 'SampleApp' do
		pod 'AppCenter/Analytics'
	```
3. Save the file and run this command in the terminal:
	```
	$ pod install
	```

### Option 2: Integrate the AppCenter SDK manually
1. Download the **1DS SDK** for iOS and macOS.
	* The SDK is available as a ZIP file.
2. Integrate the SDK into your project
	* In this step, you'll configure your project to link-in the 1DS SDK libraries.
	* Make sure that your project has modules enabled.
	* Unzip the SDK archive
		* For iOS: Copy the AppCenter.framework and AppCenterAnalytics.framework frameworks from the iOS folder.
		* For macOS: Copy the AppCenter.framework and AppCenterAnalytics.framework frameworks from the macOS folder.
3. Create a new folder named Frameworks inside your project folder, and paste the frameworks into this.
4. Add the SDK frameworks to the project in Xcode:
	* Drag and drop all the frameworks into Xcode's Project Navigator.
	* A dialog will appear, make sure your app target is checked. Then click Finish.
5. Make sure the .frameworks have been added to the project and target correctly. Follow these steps:
	* Select your project in Xcode's project navigator.
	* Select your app target.
	* In the General tab, verify that
		* None of the .frameworks have been added to Embedded Binaries.
		* The section about Linked Frameworks and Libraries contains all .frameworks. Remove duplicates and add missing frameworks if necessary.
	* In the Build Phases tab, verify that
		* All .framework files have been added to Link Binary With Libraries.
		 None of the .frameworks have been added to Embed Frameworks.
6. Note that all .frameworks are distributed as statically linked, "fake" frameworks.

### Integrate the Product Insights Analytics SDK Manually
1. Download the **Product Insights Analytics Objective-C SDK** for iOS or macOS.
2. Integrate the SDK into your project
	* In this step, you'll configure your project to link-in the Product Insights Analytics Objective-C SDK framework.
	* Unzip the SDK archive.
		Copy the `ProductInsightsAnalytics.framework` (for iOS) or `ProductInsightsAnalyticsMacOS.framework` (for macOS).
	* Create a new folder named **Frameworks** inside your project folder, and paste the framework into this.
		> [!NOTE]
		> Skip this step if you have already created the folder named **Frameworks** in a previous step.
	* Select your project in Xcode's project navigator.
	* Select your app target.
	* In the **General** tab add the `ProductInsightsAnalytics.framework` (for iOS) or `ProductInsightsAnalyticsMacOS.framework` (for macOS) to **Embedded Binaries**.

### Import Product Insights Analytics and AppCenter into your project
1. Open your `AppDelegate.m* file`, and add the following import statements:
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
	* Insert the following lines to start the SDK in your app's `AppDelegate.m` class in the `didFinishLaunchingWithOptions:` method.
		```objc
		[MSAppCenter start:@"target={Your Ingestion Key}" withServices:@[[MSAnalytics class]]];
		```
		* If your application already uses the Microsoft AppCenter SDK to track telemetry:
		```objc
		[MSAppCenter start:@"app-secret={Your App Secret}; target={Your Ingestion Key}" withServices:@[[MSAnalytics class]]];
		```

2. Insert the following line to initiate Product Insights Analytics.
	```objc
	PIAnalytics *piAnalytics = [[PIAnalytics new] initWithIngestionKey:{Your Ingestion Key}];
	```

3. Insert the following lines to track signals.
	```objc
	// Signal with name only
	PISignal *sampleSignal = [[PISignal new] initWithName:@"sampleSignal"];
	[piAnalytics trackSignal:sampleSignal];

	// Signal with custom properties of various types
	PISignal *sampleSignal = [[PISignal new] initWithName:@"sampleSignal"];
	SampleSignal.version = @"1.0.0";

	[sampleSignal setStringValue:@"sampleStringValue" forProperty:@"stringProperty"];
	[sampleSignal setDoubleValue:36.5 forProperty:@"doubleProperty"];
	[sampleSignal setInt64Value:3000 forProperty:@"int64Property"];
	[sampleSignal setDateValue:[NSDate new] forProperty:@"dateProperty"];
	[sampleSignal setBoolValue:YES forProperty:@"boolProperty"];

	[piAnalytics trackSignal:sampleSignal];
	```

	The following types are supported for custom signal properties:
	- **NSString**
	- **NSDate**
	- **double**
	- **int64_t**
	- **BOOL**
