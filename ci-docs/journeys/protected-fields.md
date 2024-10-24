---
title: Add protected fields in segment criteria
description: Learn how to use protected fields and columns to restrict segment access to certain Dataverse columns in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/24/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Add protected fields in segment criteria

Protected fields allow you to restrict segment access to certain Dataverse columns. For example, you could choose to restrict access to the Social Security number column. Restricting access to this column means that regular users looking at the table can't see the Social Security number column. In segmentation, restricting access to the Social Security number column means that, by default, the column isn't available for use as a query condition.

The protected fields setting allows admins flexibility in restriction. An admin can designate a protected field, but still allow users to use the field for querying purposes. This way, the admin could designate, for example, the gender column as restricted while allowing users to still create a segment of male customers, even though they can't see the values in the gender column.

## Enable protected fields

To enable protected fields:

1. Go to **Settings** > **Overview** > **Feature switches**.
1. Enable the **Use protected fields in segments** feature switch under the Segmentation section and select **Save** in the upper right corner.

:::image type="content" source="media/protected-fields-feature-switch.png" alt-text="Screenshot showing the protected fields feature switch.":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]