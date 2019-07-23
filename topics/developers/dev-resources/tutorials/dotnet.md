---
uid: developers/downloads/dotnet
title: Get started with .NET (C#)
author: vroha
description: Get started with .NET (C#)
ms.author: hakrou
ms.date: 04/12/2019
ms.service: product-insights
ms.topic: conceptual
---
# .NET (C#)

## Prerequisites

* Visual Studio 
* .NET Standard 1.3  
* Instrumentation Key (get from [pi.dynamics.com](http://pi.dynamics.com)>team>project>settings – copy the Ingestion Key)

## Code sample

[Download .NET code sample](https://ariamediahost.blob.core.windows.net/sdk/ProductInsightsSenders/microsoft.applications.events.server.zip)
 
### Running the sample
 
1.	Unzip the sample and open the solution.
2. Add a `New Package Manage Source` pointing to the folder location of the sample. Here's how:
    1. Select Tools > Nuget Package Manager > Package Manager Settings. 
    2. Select Package Sources and add a Package Source. For the Source Field, add the folder location of the sample.
3. Select Tools > Nuget Package Manager > Package Manager Console. Select Restore when the app prompts you to restore the missing NuGet package.
4. Open Program.cs and replace `YOUR_INSTRUMENTATION_KEY` with your project's instrumentation key.
5. Start the program.

## Integrate

1. Open your project. If you don't have one, create a new project in Visual Studio.
2. Download the SDK.
3. Add a `New Package Manage Source` pointing to the folder location which has the downloaded SDK. Here's how:  
   1. Select Tools > Nuget Package Manager > Package Manager Settings.  
   2. Select Package Sources and add a Package Source. For the Source Field, add the folder location which has the downloaded SDK.
4. Add the SDK Nuget package "Microsoft.Applications.Events.Server" to your project.
5. Initialize logger and replace `Your-API-Token` with your project's instrumentation key
```
// Initialize logger
var logConfiguration = new LogConfiguration();
LogManager.Start(configuration);
var logger = LogManager.GetLogger("Your-API-Token", out EVTStatus value);
```
6. Create a signal:
```
// Track an event with properties of various types.
EventProperties properties = new EventProperties { Name = "TestName"};
properties.SetProperty("Name", "Ashley Smith");
properties.SetProperty("School", "Bellevue High School");
properties.SetProperty("Grade", 11);
properties.SetProperty("Gpa", 3.82);
properties.SetProperty("Birthday", new Date(800320249));
properties.SetProperty("Suspended", false);
logger.trackEvent("StudentInformation", properties);
```
7. We recommend that you upload all events in the queue and teardown the SDK before your application closes.
```
LogManager.UploadNow();
LogManager.Teardown();
```

The following types are supported for event properties:

- String
- Date
- Double
- Long
- Boolean
