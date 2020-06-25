---
uid: topics/getting-started-websdk
title: Getting started with the Web SDK
author: ruthaisabokhae
description: Web SDK
ms.author: ruthai
ms.date: 06/25/2020
ms.service: product-insights
ms.topic: conceptual
---

# Getting started with the Product Insights Web SDK

[!INCLUDE [cc-beta-prerelease-disclaimer]( includes/cc-beta-prerelease-disclaimer.md)]

This tutorial will guide you through the process of using a Product Insights ingestion key and the Product Insights SDK for instrumenting your existing website. You'll start seeing signals in your portal in five minutes or sooner.

## Configuration options

The following configuration options can be passed to the SDK:

- **ingestionKey**: This is the key used to send signals to your project.
-	**autoCapture**: This specifies the auto capture instructions for the SDK to collect page views and clicks. It has two options:
    - **view**: Set this to true if you want the SDK to capture page views automatically. Note that single page applications need to instrument views manually, and must instrument the trackView() API whenever they route to a new page.
    - **click**: Set this to true if you want the SDK to capture page clicks automatically.
-	**userConsent**: This specifies whether the user has consented to let the SDK add data to browser storage (localstorage or cookies) that will be used by Product Insights to track user behavior. By default, this is assumed to be true.
-	**endpointUrl**: This can be used to specify the destination URL for your signals. Only override this if you need to send data to a specific endpoint.

## Prerequisites

* The SDK requires the project or webpage to be hosted in order to send telemetry. Telemetry sent from a local file will not be accepted by the server.
* Ingestion key (see below for instructions on how to obtain).

## Get an ingestion key from the Product Insights portal

1. From the Product Insights home screen, select your project from the project dropdown on the left navigation menu. If you don't already have a project, select the **+ New Project** option instead and create one.
2. Once you've selected a project, navigate to **Settings > Basics** in the left panel.
3. Copy your key from the **Ingestion key** field.

## Integrate the Product Insights SDK into your webpage

1. The MSPI Analytics tag should be added near the top of the `<head>` tag and before any other script or CSS tags. Here is the tag to add to your webpage:
    ```javascript
    <script>
	(function(a,t,i){var e="MSPI";var c="Analytics";var u=e+"queue";a[u]=a[u]||[];var n=a[e]||function(r){var t={};t[c]={};function e(e){while(e.length){var n=e.pop();t[c][n]=function(e){return function(){a[u].push([e,r,arguments])}}(n)}}var n="track";var i="set";e([n+"Signal",n+"View",n+"Action",i+"Property",i+"User","initialize","teardown"]);return t}(i.name);var r=i.name;if(!a[e]){a[r]=n[c];a[u].push(["new",r]);setTimeout(function(){var e="script";var n=t.createElement(e);n.async=1;n.src=i.src;var r=t.getElementsByTagName(e)[0];r.parentNode.insertBefore(n,r)},1)}else{a[r]=new n[c]}if(i.user){a[r].setUser(i.user)}a[r].initialize(i.cfg)})
	  (window,document, {
	    src:"SDK_SRC",
	    name:"NAME",
	    cfg:{
	      ingestionKey:"INGESTION_KEY",
	      autoCapture:{
	        view:true,
	        click:true
	      }
	    }
	  });
	</script>
    ```

2. Replace the string "NAME" with a global variable name in the window object where the SDK is instantiated. For example, if you replace "NAME" with "Contoso", then the SDK can be accessed at **window["Contoso"]** or simply **Contoso**.

3. Replace the string "INGESTION_KEY" with your ingestion key from the Product Insights portal.

## Setting user details for your signal

The PI SDK allows you to define user information that can be sent with every signal. This can be done by specifying the user details in a property called `user` (the expected data for this property is the `IUser` object), similar to `src`, `name`, and `cfg` in the code snippet configuration. Alternatively, user information can be specified by calling the `setUser(user: IUser)` API on the SDK.

Specifying user details in the code snippet means that all telemetry will have this information. However, if specified by the `setUser API`, telemetry sent before the `setUser API` will not contain this information.

The `IUser` interface contains the following string properties:

- **localId**: The user's local ID.
- **authId**: The authenticated user ID.
- **authType**: The authentication type used to the get authenticated user ID.
- **name**: The user's name.
- **email**: The user's email address.
