---
title: Aspects of segment builder
description: An example of the various aspects of segment builder in Dynamics 365 Customer Insights - Data.
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: v-wendysmith
ms.topic: conceptual
ms.date: 07/05/2023
ms.custom: bap-template
---

# Aspects of segment builder

The following image illustrates the various aspects of the segment builder. It shows a segment that results in a group of customers. The customers ordered goods in a specific time frame and gathered reward points or spent a certain amount of money.

:::image type="content" source="media/segment-builder-overview.png" alt-text="Elements of the segment builder." lightbox="media/segment-builder-overview.png":::

1. Organize your segment with rules and subrules. Each rule or subrule consists of conditions. Combine the conditions with logical operators.

1. Choose the [relationship path](relationships.md) between tables that applies to a rule. The relationship path determines which attributes can be used in a condition.

1. Manage rules and subrules. Change the position of a rule or delete it.

1. Add conditions and build the right level of nesting using subrules.

1. Apply set operations to connected rules.

1. Use the attribute pane to add available table attributes or create conditions based on attributes. The pane shows the list of tables and attributes based on the selected relationship path that are available for the selected rule.

1. Add conditions based on attributes to existing rules and subrules or add it to a new rule.

1. Undo and redo changes while building the segment.

The example illustrates the segmentation capability. We've defined a segment for customers who bought goods online in March, June, or the last 20 days *and* spent $500 or more or earned 100 reward points or more.

## Segment builder tips

When creating a segment using the segment builder, keep in mind the following tips:

- The segment builder doesn't suggest valid values from tables when setting the operators for the conditions. You can go to **Data** > **Tables** and download the table data to see which values are available.
 Conditions based on dates let you switch between fixed dates and a floating date range.
- If you have multiple rules for your segment, the rule you're editing has a vertical blue line next to it.
- You can move rules and conditions to other places in the segment definition. Select the vertical ellipsis (&vellip;) next to a rule or condition and choose how and where to move it.
- The **Undo** and **Redo** controls in the command bar let you roll back changes.
- After creating a segment, some segments allow you to [track the usage of the segment](segments-track-usage.md).

## Next steps

- [Create complex segments with segment builder](segment-builder.md)


[!INCLUDE [footer-include](includes/footer-banner.md)]
