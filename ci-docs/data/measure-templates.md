---
title: Create measures from templates (preview)
description: Build measures faster with templates for average transaction value, loyalty points balance, and more. Discover how to map activity data and calculate results.
ms.date: 07/29/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
---

# Create measures from templates (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Create commonly used [measures](measures.md) quickly by using predefined templates. These templates calculate metrics such as average transaction value, loyalty points balance, and customer lifespan by using mapped data from the *Unified Activity* table.

Available measure templates include:

- Average transaction value (ATV)
- Total transaction value
- Average daily revenue
- Average monthly revenue
- Average yearly revenue
- Transaction count
- Loyalty points earned
- Loyalty points redeemed
- Loyalty points balance
- Active customer lifespan
- Loyalty membership duration
- Time since last purchase

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Prerequisites

Configure [customer activities](activities.md).

## Build a new measure using a template

1. Go to **Insights** > **Measures**.

1. Select **New** and select **Choose a template**.

1. Find the template that fits your need and select **Choose template**.

1. Review the required data and select **Get started** if you have all the data in place.

1. Select **Edit details** next to Measure name. Provide a name for the measure. Optionally, add [tags](work-with-tags-columns.md#manage-tags) to the measure.

   :::image type="content" source="media/measures_edit_details.png" alt-text="Screenshot of the Edit details dialog box.":::

1. Select **Done**.

1. In the **Set time period** section, define the time frame of the data. Choose if you want the new measure to cover the entire dataset by selecting **All time**, or if you want the measure to focus on a **Specific time period**.

   :::image type="content" source="media/measure-set-time-period.png" alt-text="Screenshot of the time period section when configuring a measure from a template.":::

1. In the next section, select **Add data** to choose the activities and map the corresponding data from your *Unified Activity* table.

    1. Step 1 of 2: Under **Activity type**, choose the table type you want to use. For **Activities**, select the tables you want to map, and then select **Next**.
    1. Step 2 of 2: Choose the attribute from the *Unified Activity* table for the component required by the formula. For example, for Average transaction value, it's the attribute representing the Transaction value. For **Activity timestamp**, choose the attribute from the *Unified Activity* table that represents the date and time of the activity.
    1. Select **Save**.

    When the data mapping is successful, the status shows **Complete** and the name of the mapped activities and attributes display.

1. Select **Run** to calculate the results of the measure. Select **Save draft** if you want to keep the current configuration and run the measure later. The **Measures** page displays.

## Next steps

- [Schedule a measure](measures-schedule.md).
- Use existing measures to create [a customer segment](segments.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
