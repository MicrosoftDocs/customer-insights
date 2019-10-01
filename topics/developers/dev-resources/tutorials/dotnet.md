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
# Getting started with the Product Insights SDK for .NET

This tutorial will guide you through the process of using a Product Insights ingestion token and the Product Insights SDK for your existing .NET application, which will allow you to see signals in the portal in five minutes or sooner.

The following scenario will be used to construct the Product Insights SDK example: you work at a car manufacturing company, and the company has just released a new car. You want to know how the car is performing, the demographic of users, and their driving habits. Product Insight allows you to achieve these goals by sending real-time signals and generating valuable insights with only a few simple steps.


## Prerequisites
* .NET Core 1.0 and above
    * *Or* .NET Framework 4.6 and above
* Visual Studio 2017
* Ingestion key (see below for instructions to obtain)

## Get an ingestion key from Product Insights portal
1. From the [pi.dynamics.com](http://pi.dynamics.com) home screen, select your team from the left panel. If you do not already have a team, refer to [Create a team](xref:developers/quick-starts/create-a-team).
2. Add a new project to your team by selecting the **+ New Project** button from the top right corner.
3. Type in a project name in the **Name** field and any other text for **Description**. Select **Create** to commit the update.
4. Once your project is created, select the project.
5. Select **Settings** under your project. Your ingestion key is available under **Ingestion Key**.

> [!NOTE]
> Leave this tab open in your web browser, or copy the key to a clipboard because you will need to use it later.

## Integrate the Product Insights SDK into your .NET project
> [!NOTE]
> The Product Insights .NET SDK works for all languages supported by .NET framework. For convenience, we will use C# standard syntax in the code samples below.

1. Import the Product Insights SDK:
    1. [Download](https://download.pi.dynamics.com/sdk/ProductInsightsSenders/pi_csharp_sdk.zip) the **Product Insights .NET SDK**
    2. Unzip the compressed file **pi_csharp_sdk.zip** to a local folder.
    3. Go to your project in Visual Studio, and add a new **Nuget Package Source** to the local folder where you put the SDK.
        1. On the **Tools** menu, select **Options**.
        2. Expand **NuGet Package Manager** and select **Package Sources**.
        3. Select the green plus in the upper right corner.
        4. At the bottom of the dialog box, enter the feed's name and the local folder path where you put the .NET SDK package.
        5. Select **Update**.
        6. Select **OK**.

        ![Add Local NuGet Feed](add_local_nuget_feed.png "Add Local NuGet Feed")
2. Import the Product Insights SDK by adding the following statement of your app's implementation file:
    ```csharp
    using Microsoft.Dynamics.ProductInsights;
    using Microsoft.Applications.Events;
    ```
3. Initialize ProductInsightsAnalytics:
    ```csharp
    LogManager.Start(new LogConfiguration());
    ProductInsightsAnalytics pia = new ProductInsightsAnalytics("Your-Ingestion-Key");
    ```
4. Track signals:
    ```csharp
    // Do a simple track signals call.
    pia.TrackSignal(new Signal("user_information"));

    // Track a signal with custom properties of various types.
    Signal signal = new Signal("car_information");
    signal.Version = "1.0.0";

    signal.SetProperty("engine_start", true);
    signal.SetProperty("car_model", "Star Car");
    signal.SetProperty("model_year", "2017");
    signal.SetProperty("rpm", 3000);
    signal.SetProperty("temperature", 74.3);
    pia.TrackSignal(signal);
    ```

    Following types are supported for custom signal properties:
    - **string**
    - **DateTime**
    - **double**
    - **long**
    - **Bool**

5. Teardown the SDK when the application closes to ensure all signals currently in queue are sent:
    ```csharp
    LogManager.UploadNow();
    LogManager.Teardown();
    ```