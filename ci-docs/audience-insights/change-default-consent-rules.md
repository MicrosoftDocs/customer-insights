---
title: "Manage default consent rules on segments"
description: "Learn how to disable or change default consent rules if overrides are enabled."
ms.date: 10/30/2021
ms.service: customer-insights
mms.topic: how-to
author: smithy7
ms.author: smithc
ms.reviewer: mhart
manager: shellyha
---

# Disable or change default consent rules

If your organizations uses the [consent management capability](../consent-management/overview.md) combined with audience insights, [admins can enforce consent](activate-consent.md) for segments. 

With enforced consent rules in the segment area, every segment informs about the state of consent check and rules. If overrides are allowed, administrators can deactivate default consent rules. Every creator of a segment can add more consent rules for a segment. 

To deactivate default consent rules as admin

1. In the **Consent rules** notification, select **See details**. 
1. Set the **Default consent rules** toggle to **Off**.

To add more consent rules

1. In the **Consent rules** notification, select **See details**. 
1. Select **Add additional consent rule** and choose if you want to add **From a subscription** or **From a purpose**.
1. Choose the subscription or purpose and **Select the identifying attribute**.
1. Select **Save** to apply the new rule to the segment.

[!INCLUDE[footer-include](../includes/footer-banner.md)] 
