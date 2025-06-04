---
title: Manage segment memberships from a contact record
description: How to add or remove a displayed contact to or from a segment in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/21/2023
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing
---

# Manage segment memberships from a contact record

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Instead of working directly with a segment definition, you can add or remove a contact to/from any static segment while viewing their contact record. This enables users such as salespeople, who know their contacts well but don't have access to the segment entity, to manage the segments a contact belongs to while working directly with that contact record.

> [!NOTE]
> You can only use contact records to add or remove contacts to or from *static segments*, not *dynamic segments*. Both live and draft segments are supported.

To add or remove a contact to/from a static segment using their contact record:

1. Go to **Outbound marketing** > **Customers** > **Contacts**.
1. Open or create a contact record.
1. On the command bar, select one of the following:
    - **Add to segment**: To add the current contact to one or more existing static segments.
    - **Remove from segment**: To remove the current contact from one or more existing static segments.
1. A dialog box opens, showing a list of available segments. Select each segment that you'd like to update and then choose **Select** to apply your changes.

    ![Select segments to add the current contact to.](media/select-segment-from-contact.png "Select segments to add the current contact to")

[!INCLUDE [footer-include](./includes/footer-banner.md)]
