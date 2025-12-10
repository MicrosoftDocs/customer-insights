---
title: Generate and manage suggested segments based on measures (preview)
description: Use AI to suggest segments based on measures or customer attributes 
author: JimsonChalissery
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.service: customer-insights
ms.topic: how-to
ms.date: 03/20/2023
ms.custom: bap-template
---

# Generate and manage suggested segments based on measures (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Find suggested segments based on measures or customer attributes. For more information, see [Suggested segments based on measures](suggested-segments.md).

## Generate suggested segments based on measures

1. Go to **Segments** and select the **Suggestions (preview)** tab.

1. Select **Find new suggestions** and choose **Improve a measure/metric**. Select **Start**.

   :::image type="content" source="media/suggested-segments-measure.png" alt-text="Choosing improve measure on the suggested segments.":::

1. Choose a customer attribute or measure as the primary attribute and select **Next**.

1. Select the influencing attributes and select **Run**.

   > [!TIP]
   > Selecting multiple influencing attributes improves the chances of evaluating how they influence the primary attribute. Don't include attributes that have no influence on the primary attribute. For example, if all your customers are from a specific country, don't include the *country* attribute because it won't have any impact on the output.

Depending on the number of customer profiles and selected attributes, it can take a few minutes to process the selected attributes.

## Manage suggested segments based on measures

Go to **Segments** and select the **Suggestions (preview)** tab. In the **Attribute-based segment suggestions** section, select a suggested segment to view available actions.

- **View** the suggested segment details and the attribute values or rules that the AI model learned.
- **Save as segment** the suggestion as a segment. It displays on the **All segments** tab and can be [refreshed, edited, or deleted](segments.md).
- **Edit attributes** and modify the configured attributes which will replace the current suggestions.
- **Refresh suggestions** to refresh the suggestions while keeping configured attributes.

## Limitations

1. Estimated segment size mismatch: If you choose a primary attribute that contains empty values, it can affect the estimated segment size in the segment suggestions. When saving such segment, the actual segment size can be different to the original estimation.

2. Boolean type primary attributes don't work: Currently, we only support string and numeric types of data as the primary attribute.

3. Suggested segments aren't distinct enough: Keep in mind that the selected attributes and the distribution of values of those attributes influences the results. You can change your influencing attributes or even your primary attribute to get different results.

[!INCLUDE [footer-include](includes/footer-banner.md)]
