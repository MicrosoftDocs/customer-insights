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

Dataverse offers protection for your data, allowing only authorized users to access attributes like Social Security number or bank balance. By default, such columns aren't available for use as a query condition in segmentation.

The protected fields setting in Customer Insights - Journeys allows admins to override the use of such restricted columns as query conditions, by regular users. For instance, a user can now create a segment of customers with varying ranges of bank balances, without revealing the actual bank balance of each individual.

## Enable protected fields in query conditions

> [!WARNING]
> Enabling this will allow all marketing contributors to have access to protected fields for querying. This can allow marketing contributors to infer the values of the protected field. For example, if "Gender" is a protected field, with this override, a marketing contributor can create a segment of all "male" customers. While they won't be able to see the "Gender" column in the result, they can infer that anyone included in the segment is a male. **Administrators have the responsibility to ensure that overriding this setting won't lead to leaking of protected data.**

To enable access to protected fields in query conditions:

1. Go to **Settings** > **Overview** > **Feature switches**.
1. Enable the **Use protected fields in segments** feature switch under the Segmentation section and select **Save** in the upper right corner.

:::image type="content" source="media/protected-fields-feature-switch.png" alt-text="Screenshot showing the protected fields feature switch.":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]