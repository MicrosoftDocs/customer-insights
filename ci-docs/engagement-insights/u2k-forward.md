---
title: Recognize web events from previously authenticated visitors with Unknown to known
description:  The Unknown to known feature allows you to associate events on a website with visitors who authenticated previously. 
ms.reviewer: mhart
ms.author: mkisel
author: mhart
ms.date: 7/12/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: overview
ms.manager: shellyha
---
# Recognize web events from previously authenticated visitors with **Unknown to known**

The **Unknown to known** feature in Engagement insights allows you to associate events for a website with visitors who authenticated previously. If the feature is disabled, visitors who authenticated during an earlier visit and then left are not identified if they don’t authenticate again when coming back. 

For example, John visited a website last week, signed into his user account on the site, and browsed the product catalog. He returned the following week to browse more products without signing into his account. The site owner using the **Unknown to known** feature would know that John had returned and what he had done on the site. This allows for more accurate reporting and analysis of website activities.

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

## How to enable

You need to be a workspace admin to enable this feature. 

1. In Engagement insights, go to **Admin > Workspace**. 
2. In the **Unknown to known** section, set the toggle to **Enabled**.

![Enable U2K forward](media/U2Ktoggle.png "Enable U2K forward")

## Data flow

1. Login via special mapping event `(CookieId and AuthId)`sent to Engagement insights and Azure Storage
2. Web events sent via website to Engagement insights
3. Unauthenticated (unknown) web event sent to Azure Storage 
4. Events combined and enriched with AuthId (now known)
5. Enriched events stored in [Kusto](https://docs.microsoft.com/azure/data-explorer/kusto/concepts) (Time forward)

## Adding JS Code to your site

A website **user authId** needs to be captured via the following Javascript sample in the Engagement insights SDK:

```
},
userMapping: true
},
user:{
authId: getLoggedInUserId()*,
email: getLoggedInUserEmail()*,
authType: "MSA",
name: "John Doe"
}
```

## Learn more
[Advanced web SDK instrumentation](https://docs.microsoft.com/dynamics365/customer-insights/engagement-insights/advanced-sdk-implementation)


[!INCLUDE[footer-include](../includes/footer-banner.md)]
