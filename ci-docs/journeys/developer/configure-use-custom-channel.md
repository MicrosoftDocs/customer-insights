---
title: Configure and use a custom channel in outbound marketing
description: Provides information on how to install custom channel from AppSource to your outbound marketing instance.
ms.date: 03/17/2022
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
---

# Configure and use a custom channel in outbound marketing

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

This step is typically performed by administrators of your Dynamics 365 Customer Insights - Journeys instance.

To configure a custom channel in your instance of Customer Insights - Journeys, administrators can:

1. Search for the required custom channel on [the Microsoft commercial marketplace](https://appsource.microsoft.com).
2. For a custom channel, select **Get it now** or **Free trial** depending on the pricing of the custom channel.
3. If you're signed into AppSource using your work or school account that you have registered with Microsoft while signing up for Customer Insights - Journeys, you'll be prompted to accept the license agreement for the custom channel. Otherwise, you'll be prompted to sign in using your work or school account. After signing in, you'll be prompted to accept the license agreement for the custom channel. Select **Continue** to accept and proceed.
4. The next page will let you select the instance where you want to add the custom channel. Select the appropriate instance, select the check boxes to accept Microsoft legal terms and privacy notices, and select **Agree** to install.

Installing a custom channel installs a [managed solution](/powerapps/developer/common-data-service/introduction-solutions#managed-and-unmanaged-solutions) for the custom channel in your instance. After the custom channel is installed in your instance, users will see the new custom channel tile in their customer journey designer when they create a customer journey.

> [!div class="mx-imgBorder"]
> ![Custom Content tiles.](../media/marketing-custom-channel-tile2.png "Custom Content tiles")

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
