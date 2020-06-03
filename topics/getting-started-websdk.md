---
uid: topics/getting-started-websdk
title: Getting started with the Web SDK
author: ruthaisabokhae
description: Web SDK
ms.author: ruthai
ms.date: 06/02/2020
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
* Ingestion key (see below for instructions on how to obtain)

## Get an ingestion key from the Product Insights portal

1. From the Product Insights home screen, select your project from the project dropdown on the left navigation menu. If you don't already have a project, select the **+ New Project** option instead and create one.
2. Once you've selected a project, navigate to **Settings > Basics** in the left panel.
3. Copy your key from the **Ingestion key** field.

## Integrate the Product Insights SDK into your webpage

1. Add the following script to your webpage:
    ```javascript
    (function(i,t,a){var e="MSPI";var c="Analytics";var u=e+"queue";i[u]=i[u]||[];var n=i[e]||function(r){var t={};t[c]={};function e(e){while(e.length){var n=e.pop();t[c][n]=function(e){return function(){i[u].push([e,r,arguments])}}(n)}}var n="track";var a="set";e([n+"Signal",n+"View",n+"Action",a+"Property",a+"User","initialize","teardown"]);return t}(a.name);var r=a.name;if(!i[e]){i[r]=n[c];i[u].push(["new",r]);setTimeout(function(){var e="script";var n=t.createElement(e);n.async=1;n.src=a.src;var r=t.getElementsByTagName(e)[0];r.parentNode.insertBefore(n,r)},1)}else{i[r]=new n[c]}i[r].initialize(a.cfg)})  (window,document,{
    src:"https://download.pi.dynamics.com/sdk/web/mspi-0.js",
    name:"NAME",
    cfg:{
      ingestionKey:"INGESTION_KEY",
      autoCapture:{
        view:true,
        click:true
        }
      }
    });
    ```

2. Replace the string "NAME" with a global variable name in the window object where the SDK is instantiated. For example, if you replace "NAME" with "Contoso", then the SDK can be accessed at **window["Contoso"]** or simply **Contoso**.

3. Replace the string "INGESTION_KEY" with your ingestion key from the Product Insights portal.
