---
title: Troubleshoot customer journey customization errors
description: Use the recovery items tab to troubleshoot customer journey custom workflows in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/18/2023
ms.topic: reference
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing
---

# Troubleshoot customer journey customization errors

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

The Recovery items tab allows system administrators to track customization errors, improving the customer journey workflow creation process. If there are items in the Recovery items tab, non-system admin users receive a notification that says, "There are work items to recover. Check the recovery items tab."

> [!div class="mx-imgBorder"]
> ![Customer journey recovery items notification.](media/customer-journey-recovery-items-error.png)

The Recovery items tab contains a grid with customization errors and gives administrators options to handle them. For customer journeys, typical errors occur when a CRM workflow is used in a customer journey but isn't marked as **On Demand** in the workflow properties.

> [!div class="mx-imgBorder"]
> ![List of customer journey recovery items.](media/customer-journey-recovery-items-grid.png)

After selecting rows in the Recovery items tab, you can delete the items (which will delete them from blob storage), or you can fix the issue and "recover" any item, which will replay the previously failed functionality. 

[!INCLUDE [footer-include](./includes/footer-banner.md)]
