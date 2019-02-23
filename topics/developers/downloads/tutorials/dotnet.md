---
uid: developers/downloads/dotnet
title: Get started with .NET (C#) 
---
# Getting started with .NET (C#)

This tutorial guides you through the process of using a Product Insights API token and the 1DS .NET Core SDK with your existing app, which will have you sending signals in about five minutes. 
 
## Prerequisites 
* Visual Studio 
* .NET Standard 1.3  
* [API Token](xref:developers/downloads/api-token)

## Integrate the signal sender into your project

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
  
    // Initialize sink with Product Insights configuration 
    var ariaConfig = new TelemetryConfiguration(Constants.OneCollectorTenant); 
    sink.Initialize(ariaConfig); 
  
    // Plug Product Insights sink 
    config.TelemetrySinks.Add(sink); 
    config.TelemetryProcessorChainBuilder.Build(); 
} 
```

5. Track events: 

```csharp
static void SendTelemetry() 
{ 
    EventTelemetry test = new EventTelemetry("TestSink"); 
    test.Properties.Add("CustomName", "CustomValue"); 
    client.TrackEvent(test); 
    client.Flush(); 
    TelemetryConfiguration.Active.TelemetrySinks.First(sink => sink.Name == "AriaSink").TelemetryChannel.Flush();  
    ariaChannel.UploadNow(); 
} 
```

6. Track mixed events:

```csharp
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
```

## Code sample

[Download .NET code sample](https://ariamediahost.blob.core.windows.net/sdk/ProductInsightsSamples/DotNetSample.zip)

### Running the sample

1. Unzip and open the project.
2. Replace the API token in the `Constants` class with your own token. 
3. Run the sample in Visual Studio.
