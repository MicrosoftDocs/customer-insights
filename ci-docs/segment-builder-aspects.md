---
title: Aspects of segment builder
description: An example of the various aspects of segment builder in Customer Insights
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: v-wendysmith
manager: shellyha

ms.service: customer-insights
ms.topic: conceptual
ms.date: 01/05/2023
ms.custom: bap-template
---

# Aspects of segment builder

The following image illustrates the various aspects of the segment builder. It shows a segment that results in a group of customers. The customers ordered goods in a specific time frame and gathered reward points or spent a certain amount of money.

:::image type="content" source="media/segment-builder-overview.png" alt-text="Elements of the segment builder." lightbox="media/segment-builder-overview.png":::

1. Organize your segment with rules and subrules. Each rule or subrule consists of conditions. Combine the conditions with logical operators.

1. Choose the [relationship path](relationships.md) between entities that applies to a rule. The relationship path determines which attributes can be used in a condition.

1. Manage rules and subrules. Change the position of a rule or delete it.

1. Add conditions and build the right level of nesting using subrules.

1. Apply set operations to connected rules.

1. Use the attribute pane to add available entity attributes or create conditions based on attributes. The pane shows the list of entities and attributes, based on the selected relationship path, that are available for the selected rule.

1. Add conditions based on attributes to existing rules and subrules or add it to a new rule.

1. Undo and redo changes while building the segment.

The example above illustrates the segmentation capability. We've defined a segment for customers who bought at least $500 of goods online *and* have an interest in software development.

## Next steps

- [Create complex segments with segment builder](segment-builder.md)


[!INCLUDE [footer-include](includes/footer-banner.md)]
