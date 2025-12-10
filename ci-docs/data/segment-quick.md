---
title: "Create simple segments with quick segments"
description: "Create simple segments of customers to group them based on various attributes."
ms.date: 03/20/2023
ms.topic: how-to
author: JimsonChalissery
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Create simple segments with quick segments

Quick segments let you build simple segments with a single operator quickly for faster insights. Quick segments are only supported in environments for **individual customers**.

## Create a new segment with quick segments

1. Go to **Insights** > **Segments**.

1. Select **New** > **Create from**.
   - Select the **Profiles** option to build a segment that is based on the *unified customer* table.
   - Select the **Measures** option to build a segment around measures you have previously created.
   - Select the **Insights** option to build a segment around one of the output tables you generated using either the **Predictions** or **Custom Models** capabilities.

1. In the **New quick segment** dialog box, select an attribute from the **Field** dropdown. Based on your selection, the system provides different values.
   - For categorical fields, the 10 top customer counts display. Choose a **Value** and select **Review**.
   - For a numerical attribute, the system shows what attribute value falls under each customer's percentile. Choose an **Operator** and a **Value**, then select **Review**.

1. The system provides an **Estimated segment size**. Choose whether to generate the segment you've defined, or go back to choose a different field.

   :::image type="content" source="media/quick-segment-name.png" alt-text="Name and estimation for a quick segment.":::

1. Provide a **Name** and **Output table name** for your segment. Optionally, add [tags](work-with-tags-columns.md#manage-tags).

1. Select **Save** to create your segment. The **Segments** page displays.

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

## Next steps

- [Schedule a segment](segments-schedule.md).
- [Export a segment](export-manage.md) and explore the [Customer Card integration](customer-card-add-in.md) to use segments in other applications.

[!INCLUDE [footer-include](includes/footer-banner.md)]
