---
title: Overview of custom channels in outbound marketing
description: A custom channel contains custom entities, workflow or plug-in containing your custom logic, and couple of web resources that help surface the custom channel as a “tile” in the customer journey designer in outbound marketing.
ms.date: 04/01/2018
ms.topic: overview
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
ms.custom: outbound-marketing
---

# Overview of custom channels in outbound marketing

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](../user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](../transition-overview.md)

A custom channel contains custom entities, workflows or plug-ins containing your custom logic, and a couple of web resources that help surface the custom channel as a “tile” in the customer journey designer. All these components are bundled into a solution that can be imported into a Dynamics 365 Customer Insights - Journeys instance to enable a custom channel.

The following illustration provides a high-level overview of the operation flow for a custom channel:  

![Custom channel flow.](../media/marketing-custom-channel-flow.png) 

1. When a contact record, which has the compliance field set to allow using custom channels, goes through a customer journey, an instance (record) of the **Custom Channel Activity** (**msdyncrm_customerjourneycustomchannelactivity**) entity is automatically created. For example, for a segment of 50 contacts with 40 contacts enabled for custom channel, the customer journey would generate 40 records of the **Custom Channel Activity** entity. For information about the compliance field, see [Define the Tile XML file](configure-tile-custom-channel.md#define-the-tile-xml-file).
2. On creation of the entity instance, the custom business logic present in a partner-developed plug-in or workflow is triggered, and interacts with the external service to execute custom operations. For example, send a message to the external service and receive a response from the external service.
3. Activity execution feedback is processed through a custom action, **CustomChannelActivity CreateInteraction**, and the interactions are sent to the marketing-insights service to enable analytics and triggers on the interactions. For example, one message could generate three interactions: sent, delivered, opened.

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
