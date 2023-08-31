---
title: Uninstall Dynamics 365 Customer Insights - Journeys
description: How to remove Dynamics 365 Customer Insights - Journeys.
ms.date: 08/23/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Uninstall Dynamics 365 Customer Insights - Journeys

[!INCLUDE[consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

You can remove the Customer Insights - Journeys application from any Dynamics 365 instance where it's installed. After removing it, you'll end up with a Customer Insights - Journeys license that you can use on another Dynamics 365 instance, if desired.

> [!IMPORTANT]
> The uninstall process detailed below *does not* remove all Customer Insights - Journeys-related solutions from your instance. To remove all Customer Insights - Journeys-related solutions, you must follow the process below then manually delete the solutions in the order listed in [Solution uninstall order for removing Dynamics 365 Customer Insights - Journeys](solution-uninstall-order.md).

## Uninstall Customer Insights - Journeys services

The Customer Insights - Journeys uninstall wizard handles most of the uninstall process. The uninstall wizard:

- Removes all services for Customer Insights - Journeys, event management, and Dynamics 365 Connector for LinkedIn Lead Gen Forms 
- Removes the marketing insights service and its data
- Turns off user syncing from Microsoft 365 for Customer Insights - Journeys users
- Frees your Customer Insights - Journeys license for use with another Dynamics 365 instance

> [!NOTE]
> If you want to release your Customer Insights - Journeys entitlement to use on a different instance, you do not need to uninstall any of the Customer Insights - Journeys solutions.

To run the uninstall wizard:

1. If you have sample data installed, remove it. More information: [Add or remove sample data](/power-platform/admin/add-remove-sample-data).

1. [Run the Customer Insights - Journeys setup wizard](re-run-setup.md) for the instance where you want to uninstall the Customer Insights - Journeys application. Make sure the correct instance is listed.

    > [!div class="mx-imgBorder"]
    > ![Setup wizard for an existing instance with portal integration.](media/fre-re-run3.png)

1. From the **Other actions** panel, choose **Uninstall Customer Insights - Journeys from this org**.

1. Follow the on-screen instructions to confirm and complete the uninstall.

<a name="reset-portal"></a>

## Reset any Power Apps portals connected to the uninstalled Customer Insights - Journeys app

If the Customer Insights - Journeys instance that you are uninstalling was connected to a Power Apps portal (for example to run marketing pages or the events website), then you need to reset the portal to release its license. After the reset, the portal still shows as configured in the Power Platform admin center, but you'll be able to select it when you run the Customer Insights - Journeys setup wizard to set up a new, copied, or restored instance.

Portals are optional, so you might not have one connected to your Customer Insights - Journeys instance. More information: [Integrate Customer Insights - Journeys with a CMS system or Power Apps portal](portal-optional.md)

To reset a portal:

1. Follow the instructions provided in [Reset a portal](/powerapps/maker/portals/admin/reset-portal).
1. Portal reset leaves behind its website bindings, which may prevent you from reusing your portal name. Therefore, you should always delete all website bindings that are related to the portals used by your uninstalled Customer Insights - Journeys instance. More information: [Create and manage website bindings](/powerapps/maker/portals/configure/website-bindings)

[!INCLUDE[footer-include](./includes/footer-banner.md)]
