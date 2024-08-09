---
title: "Step 3: Create a workflow or plug-in to implement your custom logic in outbound marketing"
description: Partners can create a workflow or plug-in to implement their custom logic for a custom channel in outbound marketing.
ms.date: 04/01/2018
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
---

# Step 3: Create a workflow or plug-in to implement your custom logic in outbound marketing

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Partners can create a workflow or plug-in to implement their custom logic. For information about creating a workflow or plug-in, see:

- [Workflows overview](/dynamics365/customerengagement/on-premises/customize/workflow-processes) and [Automate your business processes](/dynamics365/customerengagement/on-premises/developer/automate-business-processes-customer-engagement)
- [Write plug-ins to extend business processes](/powerapps/developer/common-data-service/plug-ins)

The workflow or the plug-in should be configured to:

1. Execute on the creation of an instance of the **Custom Channel Activity** (**msdyncrm_customerjourneycustomchannelactivity**) entity. An instance of this entity is created whenever a contact, which has the compliance field set to allow use of custom channels, goes through the customer journey. For information about the compliance field, see [Define the Tile XML file](configure-tile-custom-channel.md#define-the-tile-xml-file).
2. Interact with the external service to perform the required operations. For example, in case of a Special custom channel, your custom code should be able to send messages using the external service provider and receive responses or feedback, if any.
3. Call the [Custom Channel Activity Create Interaction](create-custom-channel-activity-interaction.md) action to send the customer journey feedback to the marketing-insights service for further processing.
 
> [!div class="nextstepaction"]
> [Step 4: Test your custom channel tile](test-custom-channel-tile.md)  


[!INCLUDE [footer-include](.././includes/footer-banner.md)]
