---
uid: developers/downloads/dotnet
title: Get started with the 1DS SDK for .NET (C#) 
---
# Getting started with the 1DS SDK for .NET (C#)

This tutorial guides you through the process of using a Product Insights ingestion token and the 1DS .NET Core SDK for your existing app, which will have you tracking events in about five minutes. 
 
## Prerequisites 
* Visual Studio 
* .NET Standard 1.3  

## 1. Get an API token from the Product Insights portal

1. On the **Home** screen in the Portal, select **Explorer** in the navigation pane on the left. The **Projects List** appears.

2. Add a new project by clicking the plus sign at the bottom of the list. The **Instrument Wizard** appears, displaying the **Create a project** page.

3. Enter a name for your project.

4. Leave the default value of **Sandbox** for **Group**.

5. Select **Create project**. The **What platform are you using?** page appears.

6. Select a platform from the drop-down list, but don’t select **Next**. Select **Skip this wizard** instead. The **Project Manager** page appears.

7. Your API token appears on the right side of the page, under **Ingestion Key**. Leave the tab open in your web browser because you will come back to it and copy the ingestion key to the clipboard for later use. 

## 2. Integrate the SDK into your project

1. Open your project. If you don't have one, create a new project with Empty Activity in Visual Studio. 
 
2. Install the Nuget package of 1DS Hub SDK and 1DS One Collector Channel SDK: 
* [Download](https://www.nuget.org/packages/Microsoft.ApplicationInsights/) the latest version of `Microsoft.ApplicationInsights` (the Hub SDK).
* [Download](https://msasg.pkgs.visualstudio.com/_packaging/1DSOneCollectorChannel/nuget/v3/index.json) the latest version of `OneCollectorChannel` (the One Collector Channel SDK).
* [Download](https://msasg.pkgs.visualstudio.com/_packaging/OneSDK/nuget/v3/index.json) the latest version of `Microsoft.Applications.Events.Server`.

3. Open the code for the app and import: 

```csharp
using Microsoft.ApplicationInsights; 
using Microsoft.ApplicationInsights.Channel.OneCollector; 
using Microsoft.ApplicationInsights.DataContracts; 
using Microsoft.ApplicationInsights.Extensibility; 
using Microsoft.Applications.Events; 
```

4. Start the SDK (you only need to do this once):

```csharp
static void SetUpTelemetrySinks() 
{ 
    var config = TelemetryConfiguration.Active; 
    Var ariaChannel = new OneCollectorChannel(); 
    TelemetrySink sink = new TelemetrySink(config, ariaChannel) { Name = "AriaSink" }; 
  
    // Initialize sink with Aria configuration 
    var ariaConfig = new TelemetryConfiguration(Constants.OneCollectorTenant); 
    sink.Initialize(ariaConfig); 
  
    // Plug Aria sink 
    config.TelemetrySinks.Add(sink); 
    config.TelemetryProcessorChainBuilder.Build(); 
} 
```

Track events : 
 
static void SendTelemetry() 
{ 
    EventTelemetry test = new EventTelemetry("TestSink"); 
    test.Properties.Add("CustomName", "CustomValue"); 
    client.TrackEvent(test); 
    client.Flush(); 
    TelemetryConfiguration.Active.TelemetrySinks.First(sink => sink.Name == "AriaSink").TelemetryChannel.Flush();  
    ariaChannel.UploadNow(); 
} 
 
Track mixed events: 
private static void TestMixedEvents() 
{ 
    var telemetryClient = new TelemetryClient(); 
             
    // sending one event for each type 
    telemetryClient.TrackDependency("MyDependency", "MyCommand", DateTimeOffset.Now, TimeSpan.FromMilliseconds(1), success: true); 
    telemetryClient.TrackAvailability(new AvailabilityTelemetry("availabilityName", DateTime.Now, new TimeSpan(1021), "localhost", true, "this is a message")); 
    telemetryClient.TrackPageView(new PageViewTelemetry("IndexPage")); 
   telemetryClient.TrackRequest(new RequestTelemetry("www.google.com", DateTime.Now, new TimeSpan(12312), "200", true)); 
    telemetryClient.TrackEvent("GetContact"); 
    telemetryClient.TrackMetric("ContactFile", 1); 
    telemetryClient.TrackTrace("Fetched contact details.", SeverityLevel.Information); 
    TelemetryConfiguration.Active.TelemetrySinks.First(sink => sink.Name == "AriaSink").TelemetryChannel.Flush(); 
} 
