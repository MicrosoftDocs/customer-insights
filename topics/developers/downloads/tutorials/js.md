---
uid: developers/downloads/js
title: Get started with the 1DS SDK for JavaScript
---
# Getting started with the 1DS SDK for JavaScript

This tutorial guides you through the process of using a Product Insights instrumentation token and the 1DS JavaScript SDK for your existing project, which will have you tracking events in about five minutes. 
 
## Prerequisites

The SDK requires that the project or webpage must be hosted to send telemetry. Sending telemetry from a local file will not be accepted by the server.  
 
## 1. Get an API token from Aria portal

1. On the **Home** screen in the Portal, select **Explorer** in the navigation pane on the left. The **Projects List** appears.

2. Add a new project by clicking the plus sign at the bottom of the list. The **Instrument Wizard** appears, displaying the **Create a project** page.

3. Enter a name for your project.

4. Leave the default value of **Sandbox** for **Group**.

5. Select **Create project**. The **What platform are you using?** page appears.

6. Select a platform from the drop-down list, but don’t select **Next**. Select **Skip this wizard** instead. The **Project Manager** page appears.

7. Your API token appears on the right side of the page, under **Ingestion Key**. Leave the tab open in your web browser because you will come back to it and copy the ingestion key to the clipboard for later use. 
 
## 2. Integrate the SDK into your webpage or project

1. Add the SDK to your page using the `script` tag: 

```javascript
<script type="text/javascript" src="https://1dsjssdk.blob.core.windows.net/scripts/latest/ms.analytics-1-beta.js"> 
</script> 
```

2. Start the SDK (you only need to do this once):

```javascript
var analytics = new oneDS.ApplicationInsights(); 
var config = { 
    instrumentationKey: "Your_Instrumentation_Key" 
}; 
 
Analytics.initialize(config, []); 
```

3. Track events: 

```javascript
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
```

## Types

The following types are supported for event properties: 
* String 
* Double 
* boolean 
