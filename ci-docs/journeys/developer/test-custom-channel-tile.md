---
title: "Step 4: Test your custom channel tile in outbound marketing"
description: Provides information on how you can make the custom channel tile available in the customer journey designer in outbound marketing.
ms.date: 03/17/2022
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
---

# Step 4: Test your custom channel tile in outbound marketing

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](../user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](../transition-overview.md)

To make the custom channel tile available in the customer journey designer:

1. Create a solution. More information: [Create a solution](/powerapps/maker/common-data-service/create-solution).
1. Add the tile XML file as a **Data (XML)** web resource to the solution you created. The file name must end with 'CustomerJourneyDesignerTileConfig.xml’.
1. Save the solution and publish all customizations.
1. Create a customer journey to open the customer journey designer. Go to **Customer Insights - Journeys** > **Marketing Execution** > **Customer Journeys**, and then select **New**. For more information about creating a journey, see [Create a simple customer journey](../../journeys/create-simple-customer-journey.md).
    
    The tile should show up in the **Custom Content** section of the tile library in the customer journey designer.

    > [!div class="mx-imgBorder"]
    > ![Custom Content tiles.](../media/marketing-custom-channel-tile2.png "Custom Content tiles")

> [!div class="nextstepaction"]
> [Publish custom channel on AppSource](publish-custom-channel-appsource.md)

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
