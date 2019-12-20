---
uid: developers/tutorials/embed
title: Embed in secure applications
author: ruthaisabokhae
description: Embed chart or dashboard
ms.author: ruthai
ms.date: 09/27/2019
ms.service: product-insights
ms.topic: conceptual
---

# Embed in secure applications

[!INCLUDE [cc-beta-prerelease-disclaimer]( includes/cc-beta-prerelease-disclaimer.md)]
Product Insights visuals from dashboards can be embedded into your business applications that are secure such as Dynamics 365, Teams, SharePoint, and more using iframes. Product insights will load the embedded visuals seamlessly using the current logged in user's permissions and scopes. Anonymous sharing of product insights visuals is not yet available.

Below are the two ways visuals are embedded using Product insights.

## How to embed a chart

Charts that are published to dashboards can be embedded with the following steps:

1. Login to Product Insights.
2. Go to a dashboard that which contains the chart you would like to embed.
3. Click on the **(…)** on the title of the chart and select the **Embed chart** option.
4. Copy the URL from the dialog box. This will be the source URL for your iframe.

## How to embed a dashboard page

A full page (collection of visuals/charts) from a dashboard can also be embedded following these steps:

1. Login to Product Insights.
2. Go to a dashboard that which contains the page you would like to embed.
3. Click on **Embed Page(</>)** and copy the URL from the dialog. This will be the source URL for your iframe.
