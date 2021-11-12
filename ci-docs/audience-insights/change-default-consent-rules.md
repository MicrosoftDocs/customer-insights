---
title: "Manage default consent rules on segments"
description: "With the consent management capability, you can disable or change the default consent rules if overrides are enabled."
ms.date: 11/12/2021
ms.service: customer-insights
mms.topic: how-to
author: smithy7
ms.author: smithc
ms.reviewer: mhart
manager: shellyha
---

# Disable or change default consent rules

If your organizations uses the [consent management capability](../consent-management/overview.md) combined with audience insights, [admins can enforce consent rules](activate-consent.md) for segments. 

With enforced consent rules in the segment area, every segment informs about the state of consent check and rules. If overrides are allowed, default consent rules are turned off for specific segments. Every creator of a segment can add more consent rules on top of the default rules to a segment. 

## For administrators

:::image type="content" source="../consent-management/media/consent-rules-segment.png" alt-text="Segment builder with consent rule options.":::

**To deactivate default consent rules:**

1. In the **Consent rules** notification, select **See details**. 

1. Set the **Default consent rules** toggle to **Off**.

**To add more consent rules:**

1. In the **Consent rules** notification, select **See details**. 

1. Select **Add consent rules** and choose a consent rule from the **Select consent data type** dropdown.

1. Select **Save** to apply the new rule to the segment.

## For contributors

To create a segment without enforced consent rules or add your own set of rules, you have to work with your administrator.

It's a three step process: 
1. [Create the segment](segments.md) in audience insights and save it. 

1. Share the segment name with your admin and ask them to [enable overrides for your segment](activate-consent.md). 

1. Open your segments again. In the **Consent rules** notification, select **See details** and add the consent rules you want to apply. Then, **Save** and **Run** your segment.



[!INCLUDE[footer-include](../includes/footer-banner.md)] 
