---
uid: developers/downloads/js
title: Web/React (JavaScript)
author: ruthaisabokhae
description: Web/React (JavaScript)
ms.author: ruthai
ms.date: 09/05/2019
ms.service: product-insights
ms.topic: conceptual
---

# Web/React (JavaScript)
 
# Getting started with the Product Insights SDK for JavaScript

This tutorial will guide you through the process of using a Product Insights ingestion key and the Product Insights SDK for your existing JavaScript project, which will allow you to see signals in the portal in five minutes or sooner.

The following scenario will be used to construct the Product Insights SDK example: you work at a car manufacturing company, and the company has just released a new car. You want to know how the car is performing, the demographics of users, and their driving habits. Product Insight allows you to achieve these goals by sending real time signals and generating valuable insights with only a few simple steps. 


## Prerequisites
* The SDK requires that the project or webpage must be hosted to send telemetry. Sending telemetry from a local file will not be accepted by the server.
* Ingestion key 

## Get an ingestion key from Product Insights portal
1. From the home screen, select your team from the left panel. If you do not already have a team, refer to [What is Product Insights?](topics/developers/quick-starts/what-is.md) to create a new team.
2. Add a new project to your team by selecting the **"+ New Project"** button from the top right corner.
3. Type in a project name in the **Name** field and any other text for **Description**. Select **Create** to commit the update.
4. Once your project is created, select the project.
5. Select **Settings** under your project. Your ingestion key is available under **Ingestion Key**. 

> [!NOTE]
> Leave this tab open in your web browser, or copy the key to a clipboard because you will need to use it later.
		
## Integrate the Product Insights SDK into your webpage or project
1. Add the Product Insights SDK to your page:    
a. [Download](https://download.pi.dynamics.com/sdk/ProductInsightsSenders/pi_js_sdk.zip) the SDK.    
b. Add the SDK file to your project, and add it to your page using a script tag:  
			
	```<script type="text/javascript" src="pi_js_sdk-1.0.0.min.js">  
		</script>
	```
			
2. Add the 1DS SDK to your page using the script tag, as shown:    
   
   ```<script type="text/javascript" 
		src="https://az416426.vo.msecnd.net/scripts/c/ms.analytics-2.min.js">
		</script>
	```
		
3. Start the SDKs (only required once):  
	```var analytics = new oneDS.ApplicationInsights();
		var config = {
			instrumentationKey: "Your_Ingestion_Key"
		};
		
		analytics.initialize(config, []);
		var pia = new PI.ProductInsightsAnalytics(analytics, "Your_Ingestion_Key");
	```	
		
4. Track signals:
	```	
		// Do a simple track signals call.
		pia.trackSignal({ name: "user_information"});
		
		// Track a signal with custom properties of various types.
		pia.trackSignal({ 
			name: "car_information",
			properties: {
				"engine_start": true,
				"car_model": "Accord",
				"model_year": "2018",
				"rpm": 3000,
				"temperature": 74.3
			}
		});
		
	```	
		The following types are supported for event properties:
			§ String
			§ Double
			§ Boolean
		
5. Teardown the SDK when application closes to ensure all signals currently in queue are sent:   
	```	
	analytics.getPostChannel().teardown();
	```
