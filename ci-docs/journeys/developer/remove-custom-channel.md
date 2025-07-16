---
title: Remove a custom channel in outbound marketing
description: Provides information on how to uninstall/remove custom channel from your outbound marketing instance.
ms.date: 04/01/2018
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
ms.custom: outbound-marketing, evergreen
---

# Remove custom channel in outbound marketing

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](../user-guide.md), which is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](../transition-overview.md).

This step is typically performed by administrators of your Dynamics 365 Customer Insights - Journeys instance.

To remove a custom channel app from your Dynamics 365 Customer Insights - Journeys instance, you'll first have to ensure that none of the components of the custom channel app are in use. This implies that before removing a custom channel app, you'll have to remove the custom tile from your customer journeys, or delete the customer journeys containing the custom tile altogether. This includes journeys in any state: draft, live or even past journeys in stopped/expired state. 

This is because the custom channel app is a [managed solution](/powerapps/developer/common-data-service/introduction-solutions#managed-and-unmanaged-solutions), and the solution component [dependency tracking](/powerapps/developer/common-data-service/dependency-tracking-solution-components) feature *prevents* you from deleting a managed solution if any of the managed solution components are used by other components in a customization.

After you have taken care of the dependencies, delete the managed solution to remove the custom channel app from your Dynamics 365 Customer Insights - Journeys instance. More information: [Uninstall or delete a solution](/powerapps/developer/common-data-service/uninstall-delete-solution)

If there are any customer journeys that still use one or more components of the custom channel app solution, you'll receive the following error on deleting the custom channel app solution:

![Cannot delete component error.](../media/error-delete-solution.png "Cannot delete component error")

Review your customer journey records to identify the ones still using the custom tile, remove the custom tile from the customer journey or the customer journey record itself, and then retry deleting the custom channel app solution.

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
