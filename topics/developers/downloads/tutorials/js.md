---
uid: developers/downloads/js
title: Get started with the 1DS SDK for JavaScript
---
# Getting started with the 1DS SDK for JavaScript

This tutorial guides you through the process of using a Product Insights instrumentation token and the 1DS JavaScript SDK for your existing project, which will have you tracking events in about five minutes. 
 
## Prerequisites

The SDK requires that the project or webpage must be hosted to send telemetry. Sending telemetry from a local file will not be accepted by the server.  
 
## Get an API token from Aria portal

From the Home screen in the Portal, click Explorer in the navigation pane on the left. The Projects List flies-out.

Add a new project by clicking the plus sign at the bottom of the list. The Instrument Wizard appears, displaying the Create a project page.

Enter a name for your project.

Leave the default value of Sandbox for Group.

Click Create project. The What platform are you using? page appears.

Pick a platform from the drop-down list, but don’t click Next! Click Skip this wizard instead, and the Project Manager page appears.

Your API token appears on the right side of this page, under Ingestion Key. Leave this tab open in your web browser because you will come back to it and copy it to the clipboard for use later. 
 
## Integrate the SDK into your webpage or project

Add the SDK to your page using the script tag like so: 
 
<script type="text/javascript"  
src="https://1dsjssdk.blob.core.windows.net/scripts/latest/ms.analytics-1-beta.js"> 
</script> 
 
Start the SDK (Only required to start it once): 
 
var analytics = new oneDS.ApplicationInsights(); 
var config = { 
instrumentationKey: "Your_Instrumentation_Key" 
}; 
 
Analytics.initialize(config, []); 
 
Track events : 
 
// Do a simple track call. 
Analytics.track({ 
name: "my_simple_event_name", 
data: { 
"Name": "Ashley Smith", 
"School": "Bellevue High School", 
"Grade": 11, 
"Gpa": 3.82, 
"Suspended": false 
} 
}); 
 
Following types are supported for event properties: 
String 
Double 
boolean 
