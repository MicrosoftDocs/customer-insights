---
uid: developers/downloads/js
title: Get started with the 1DS SDK for JavaScript
author: vroha
description: Get started with the 1DS SDK for JavaScript
ms.author: hakrou
ms.date: 04/12/2019
ms.service: crm-online
ms.topic: conceptual
---
# Getting started with the 1DS SDK for JavaScript

This tutorial guides you through the process of using a Product Insights instrumentation token and the 1DS JavaScript SDK for your existing project, which will have you tracking events in about five minutes. 
 
## Prerequisites

- [API token](xref:developers/downloads/api-token)
- The SDK requires that the project or webpage must be hosted to send telemetry. Sending telemetry from a local file will not be accepted by the server.  
 
## Integrate the SDK into your webpage or project

1. Add the SDK to your page using the `script` tag: 

```javascript
<script type="text/javascript" src="https://1dsjssdk.blob.core.windows.net/scripts/latest/ms.analytics-1-beta.js"> 
</script> 
```

2. Start the SDK (you only need to do this once):

```javascript 
var analytics = new ApplicationInsights(); 
var config = { 
    instrumentationKey: "Your_Instrumentation_Key" 
}; 
 
analytics.initialize(config, []); 
```

3. Track events: 

```javascript
// Do a simple track call. 
analytics.track({ 
    name: "my_simple_event_name", 
    data: { 
        "Name": "Ashley Smith", 
        "School": "Bellevue High School", 
        "Grade": 11, 
        "Gpa": 3.82, 
        "Suspended": false 
    } 
}); 
```

## Types

The following types are supported for event properties: 
* `String` 
* `Double` 
* `boolean` 

## Code sample

[Download JavaScript code sample](https://ariamediahost.blob.core.windows.net/sdk/ProductInsightsSamples/JavascriptSample.zip)

### Running the sample
 
1. Open the file in Visual Studio Code and add the instrumentation key. 
2. [Install Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer).
3. Select Alt+L, Alt+O to launch the HTML page in a local server and Alt+L, Alt+C to stop the server. (Under Mac OS select Cmd+L, Cmd+O and Cmd+L, Cmd+C.)
