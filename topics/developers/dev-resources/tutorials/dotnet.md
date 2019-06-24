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

[Download .NET code sample](https://ariamediahost.blob.core.windows.net/sdk/ProductInsightsSamples/ProductInsightsDotNetSample.zip)
 
### Running the sample
 
1.	Unzip the sample and open the solution.
2. Add a new package manage source pointing to the folder location of the sample.
    1. Select Tools > Nuget Package Manager > Package Manager Settings. 
    2. Select Package Sources and add a package source. For the source field add the folder location of the sample.
3. Select Tools > Nuget Package Manager > Package Manager Console. Select Restore when the app prompts you to restore the missing NuGet package.
4. Open Program.cs and replace `YOUR_INSTRUMENTATION_KEY` with your project's instrumentation key.
5. Start the program.

## Integrate

TBD
