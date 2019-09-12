---
uid: developers/downloads/dotnet
title: Get started with .NET (C#)
author: ruthaisabokhae
description: Get started with .NET (C#)
ms.author: ruthai
ms.date: 09/04/2019
ms.service: product-insights
ms.topic: conceptual
---
# .NET (C#)

# Getting started with the Product Insights SDK for .NET Core

This tutorial will guide you through the process of using a Product Insights ingestion token and the Product Insights SDK for your existing .NET Core Server application, which will allow you to see signals in the portal in five minutes or sooner.

The following scenario will be used to construct the Product Insights SDK example: you work at a car manufacturing company, and the company has just released a new car. You want to know how the car is performing, the demographic of users, and their driving habits. Product Insight allows you to achieve these goals by sending real-time signals and generating valuable insights with only a few simple steps. 


## Prerequisites
* .NET Core
* Visual Studio 2017
* Ingestion key 
	
## Get an ingestion key from Product Insights portal
1. From the home screen, select your team from the left panel. If you do not already have a team, refer to [What is Product Insights?](topics/developers/quick-starts/what-is.md) to create a new team.
2. Add a new project to your team by selecting the **"+ New Project"** button from the top right corner.
3. Type in a project name in the **Name** field and any other text for **Description**. Select **Create** to commit the update.
4. Once your project is created, select the project.
5. Select **Settings** under your project. Your ingestion key is available under **Ingestion Key**. 

> [!NOTE]
> Leave this tab open in your web browser or copy the key to a clipboard because you will need to use it later.
		
## Integrate the Product Insights SDK into your .NET Core Server project
1. The 1DS SDK is available as a NuGet package. In your project's **NuGet Feed Sources**, add **OneSDK** as a source with the feed URL: https://msasg.pkgs.visualstudio.com/_packaging/OneSDK/nuget/v3/index.json
		
2. In Visual Studio, open **Manage NuGet Packages**.
		
3. Select the **AriaSDK** feed from the top right, and select **Browse**.
		
4. Select the version of the SDK you want to install:  
			i. Microsoft.Applications.Events.Server for Core 1.0 Standard 1.1  
			ii. Microsoft.Applications.Events.Server.Core2 for Core 2.0 Standard 2.0  
			
5. Import the Product Insights SDK:  
			i. Unzip the compressed file **pi_csharp_sdk.zip** to a local folder.  
			ii. Go to your project in Visual Studio, and add a new **Nuget Package Source** to the local folder where you put the SDK.  
			iii. Right click on **References**, and select **Manage Nuget Package...**.  
			iv. Install the **ProductInsightsAnalytics** package.
		
		
6. Import the Product Insights SDK by adding the following statement of your app's implementation file:
		
		using Microsoft.Dynamics.ProductInsights;
		using Microsoft.Applications.Events;
		
7. Initialize ProductInsightsAnalytics:
		
		LogManager.Start(new LogConfiguration());
		ProductInsightsAnalytics pia = new ProductInsightsAnalytics(ingestionKey);
		
8. Track signals:
		
		// Do a simple track signals call.
		pia.TrackSignal(new Signal("user_information"));
		
		// Track a signal with custom properties of various types.
		Signal signal = new Signal("car_information");
		signal.Version = "1.0.0";
		
		signal.SetProperty("engine_start", true);
		signal.SetProperty("car_model", "Accord");
		signal.SetProperty("model_year", "2017");
		signal.SetProperty("rpm", 3000);
		signal.SetProperty("temperature", 74.3);
		pia.TrackSignal(signal);
		
		Following types are supported for custom signal properties:
			§ string
			§ DateTime
			§ double
			§ long
			§ Bool
		
9. Teardown the SDK when the application closes to ensure all signals currently in queue are sent:  
		LogManager.UploadNow();    
  LogManager.Teardown();
