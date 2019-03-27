---
uid: developers/downloads/dotnet
title: Get started with .NET (C#)
author: vroha
description: Get started with .NET (C#)
ms.author: v-roha
ms.date: 03/29/2019
ms.service: product-insights
ms.topic: conceptual
---
# Getting started with .NET (C#)

This tutorial guides you through the process of using a Product Insights API token with C#, and will have you sending signals in about five minutes. The sample project is a C# console app that will send a signal to Product Insights every second until the user presses a key to stop it. Each signal is a student record containing the name of an imaginary student, their grade, GPA, school, and whether they're currently suspended.

## Prerequisites

* Visual Studio 
* .NET Standard 1.3  
* [API Token](xref:developers/downloads/api-token)

## Code sample

[Download .NET code sample](https://ariamediahost.blob.core.windows.net/sdk/ProductInsightsSamples/ProductInsightsDotNetSample.zip)
 
## Steps to run the project
 
1.	Unzip the sample and open the solution.
2.	Select **Tools > Nuget Package Manager > Package Manager Console**. Select **Restore** when the app prompts you to restore the missing NuGet package.
3.	Open `Program.cs` and replace `YOUR_INSTRUMENTATION_KEY` with your project's instrumentation key.
4.	Start the program.
