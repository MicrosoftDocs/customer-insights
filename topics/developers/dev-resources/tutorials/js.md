---
uid: developers/downloads/js
title: Web/React (JavaScript)
author: vroha
description: Web/React (JavaScript)
ms.author: hakrou
ms.date: 04/12/2019
ms.service: product-insights
ms.topic: conceptual
---

# Web/React (JavaScript)
 
## Prerequisites

* [API token](https://review.docs.microsoft.com/en-us/dynamics365/product-insights/developers/dev-resources/tutorials/api-token)
* Hosted project or webpage to send telemetry. Telemetry from a local file will not be accepted by the server.

## Code sample

[Download JavaScript code sample](https://ariamediahost.blob.core.windows.net/sdk/ProductInsightsSamples/ProductInsightsJavascriptSample.zip)

### Running the sample

1. Open the file in Visual Studio Code and add the instrumentation key.
2. [Install Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer).
3. Select Alt+L, Alt+O to launch the HTML page in a local server and Alt+L, Alt+C to stop the server. (Under Mac OS select Cmd+L, Cmd+O and Cmd+L, Cmd+C.)

## Integrate

1. Add the SDK to your page using the script tag: TBD:

```
<script type="text/javascript" src="https://1dsjssdk.blob.core.windows.net/scripts/latest/ms.analytics-1-beta.js"> 
</script> 
```

2. Start the SDK (you only need to do this once)
3. Replace `Your-API-Token` with your project's instrumentation key.

```javascript
Var analytics = new ApplicationInsights(); 
var config = { 
    instrumentationKey: "Your-API-Token" 
};

analytics.initialize(config, []); 
```

4. Track events:

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

Before your program exits, call **analytics**.

(TBD)

## Types

The following types are supported for event properties:

* **String**
* **Double**
* **boolean**
