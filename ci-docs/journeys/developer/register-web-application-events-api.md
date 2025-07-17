---
title: Register your web application to use the events API in outbound marketing
description: Learn about the events API that lets you access data of events, sessions, session tracks and passes in outbound marketing.
ms.date: 06/12/2019
ms.update-cycle: 1095-days
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
ms.custom: outbound-marketing, evergreen
---

# Register your web application to use the events API in outbound marketing

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](../user-guide.md), which is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](../transition-overview.md).

To use the events API, you need to provide a web application token in each request. The web application token is used to control API requests that are associated with your organization. Follow the steps given below to register your web application:

1. Open your Dynamics 365 Customer Insights - Journeys instance and navigate to **Event Management**.
2. Select the drop-down and select **Settings**
    > [!div class="mx-imgBorder"]
    > ![Settings.](../media/event-management-settings.png "Settings")
    
3. Select **Web applications**.
    > [!div class="mx-imgBorder"]
    > ![Web application token.](../media/create-web-application-token.png "Web application token")
    
4. Select **New** to create a new web application token.
5. Enter details in the **Name** field.
6. For the **Origin** field, enter the  URL from where your application is served in the **Primary endpoint** value that you got while enabling the static website. For example: `https://localhost:4200` or `https://contoso.com`.
   
   > [!NOTE]
   > When you enter the Primary endpoint value, make sure that you don't have a trailing slash (/) at the end of the url.
   
7. Select **Save**. You get the web application token and the API endpoint.

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
