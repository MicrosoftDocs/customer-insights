---
title: Self-hosted custom event website in outbound marketing
description: Learn how you can extend event management web application functionality for self-hosted custom event websites in outbound marketing.
ms.date: 09/16/2020
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
---

# Self-hosted custom event website in outbound marketing

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

[!INCLUDE [azure-ad-to-microsoft-entra-id](../includes/azure-ad-to-microsoft-entra-id.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Before you start hosting the self-hosted custom event website, complete the actions mentioned in [Prerequisites](event-management-web-application.md) topic.

The frontend can be fully customized and hosted by yourself. Additionally, you can choose to use our backend service, or you can develop your backend. To interact with the backend service, see [Public API documentation](https://go.microsoft.com/fwlink/?linkid=2042224).

If you choose to develop your backend service, you need to take care of the Dynamics 365 Customer Insights - Journeys authentication and the web services by yourself. If you want the event registration linked to the appropriate user who created it, make sure that you create the Dynamics 365 Customer Insights - Journeys contact record for every new website user.  

![Self-hosted instance (same domain) diagram.](../media/self-hosted.png "Self-hosted instance (same domain) diagram")

To give users full control of the event website, you can host the frontend by yourself.

## Register your web application

To use event management public API, you need a web application token. The web application token is used to control API requests that are associated with your organization. More information: [Register your web application](register-web-application-events-api.md).

## Web application environment configuration

1. Duplicate the `environment.selfhosted.ts` configuration file located in the **\src\environments** folder and name it as **environment.ts**.
2. Open the `environment.ts` configuration file in the developer environment of your choice.
3. Change the value of the `apiEndpoint` variable to  `{web-application-endpoint}/EvtMgmt/api/v2.0/` where `{web-application-endpoint}` needs to be replaced with the value from the **Endpoint** field in the newly created web application record in your instance.
4. Make sure that the `useRestStack` variable is set to true.
5. Update the URL for `imagesEndpoint`. If you want to serve the images from the same server, the URL should look like this: `https://HOST/assets/images/` (HOST needs to be replaced with your domain name). 
6. Change the `emApplicationtoken` variable to point to the URL from the **Token** field in the newly created in the web application record. 
7. If you want to use [Microsoft Entra ID](/azure/active-directory/fundamentals/whatis), you need to set the `useAadB2C` variable to `true` and modify the `aadB2CConfig`. More information [Microsoft Entra ID](#configuration-for-microsoft-entra-id).

## Configuration for Microsoft Entra ID

To learn how to set up a Microsoft Entra ID tenant and configure the event management to work with Microsoft Entra ID, see [Setting up event management to work with Microsoft Entra ID](event-management-aad-b2c-setup.md)

## Development

Open Command Prompt or Windows PowerShell and run the command from the root directory to build and locally serve the website. Additionally, this command prints the URL and port where you can reach the application (The default location is `localhost:4200`).

```CLI
ng serve
```

### Specifying environment directly

Starting with June Release 2019, it is possible to specify the environment directly in the `ng serve` command.

With the following command, you can automatically use the configuration from the `environment.selfhosted.ts` file.

```CLI
ng serve --configuration=self-hosted
```

## Building

Open Command Prompt or Windows PowerShell and run the command from the root directory to build the website for production.

```CLI
ng build --prod
```

You can find the built website in the **dist** folder of the root directory.

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
