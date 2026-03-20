---
title: Segments overview
description: An overview of segments and segment builder including an example of the various segment builder parts in Dynamics 365 Customer Insights - Data.
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.topic: article
ms.date: 03/11/2026
ms.custom: bap-template
---

# Segments overview

Segments let you group your customers based on demographic, transactional, or behavioral attributes. Use segments to target promotional campaigns, sales activities, and customer support actions to achieve your business goals.

Customer or contact profiles that match the filters of a segment definition are referred to as *members* of a segment. Some [service limits](/dynamics365/customer-insights/service-limits) apply.

## Create segments

Choose how to create a segment based on your target audience.

- Simple segments with one operator: [Quick segment](segment-quick.md)
- Create complex segments using rules and conditions: [Segment builder](#segment-builder-overview)
- AI-powered way to find similar customers: [Similar customers](find-similar-customer-segments.md)
- AI-powered suggestions based on measures or attributes: [Suggested segments based on measures](suggested-segments.md#suggested-segments-based-on-measures-preview)
- Suggestions based on activities: [Suggested segments based on customer activity](suggested-segments.md#suggested-segments-based-on-activity-preview)

## Segment builder overview

Segment builder lets you use logic to create segments. It uses the following components:

- Rule: A rule consists of one or more conditions that define a set of customers. For example, one rule identifies customers who purchased coffee beans or tea bags.

- Subrule: A subrule is nested under another rule. It groups logic within a rule to further refine the set of customers. For example, only include customers who purchased coffee beans or tea bags in the month of March.

- Condition: A single filter statement built from an attribute, an operator, and a value (or values).

- Attributes and tables: Fields from the customer table or related tables that contain the attributes you need to define your rules. For example, to identify customers who purchased coffee beans or tea bags, you need the purchases and customer tables.

- Relationship path: The mapping between a selected table and the unified customer table that controls which attributes can be used in a rule and can change results.

The following image illustrates the various parts of the segment builder. It shows a segment that's a group of customers who ordered goods in a specific time frame and gathered reward points or spent a certain amount of money.

:::image type="content" source="media/segment-builder-overview.png" alt-text="Elements of the segment builder." lightbox="media/segment-builder-overview.png":::

1. Organize your segment with rules and subrules.

1. Choose the [relationship path](relationships.md) to identify the tables that contain the attributes you need to define your rules. For example, to identify customers who purchased coffee beans or tea bags, you need the purchases and customer tables.

1. Manage rules and subrules. Change the position of a rule or delete it. The position of a rule defines a logical grouping and controls how AND/OR logic is applied. Conditions inside the same rule are evaluated together. Nesting a rule changes which conditions are evaluated together first. The position of a rule—including its order and its place in the rule hierarchy—directly affects how the logic is evaluated and therefore who ends up in the segment.

1. Add conditions and build subrules.

1. Apply set operations to connected rules.

1. Use the attribute pane to add available table attributes or create conditions based on attributes. The pane shows the list of tables and attributes based on the selected relationship path that are available for the selected rule.

1. Add conditions based on attributes to existing rules and subrules or add it to a new rule.

1. Undo and redo changes while building the segment.

The example illustrates the segmentation capability. We defined a segment for customers who bought goods online in March, June, or the last 20 days *and* spent $500 or more or earned 100 reward points or more.

## Segment builder tips

When creating a segment using the segment builder, keep in mind the following tips:

- When you select a field to filter on, the system tries to show a list of valid values to choose from, based on the type of column.
  - Dataverse Choice columns display a list of names and values. For example, Shipping Method might show the choices FedEx (1), UPS (2), and USPS (3).
  - String and numeric columns with < 200 distinct values display the distinct values. For performance, the system scans the first 10,000 rows to determine the list of distinct values so it’s possible with large data sets that not all distinct values are displayed. These fields allow you to manually enter other values.
- If you have multiple rules for your segment, the rule you're editing has a vertical blue line next to it.
- You can move rules and conditions to other places in the segment definition. Select the vertical ellipsis (&vellip;) next to a rule or condition and choose how and where to move it.
- The **Undo** and **Redo** controls in the command bar let you roll back changes.
- After you create a segment, some segments allow you to [track the usage of the segment](segments-track-usage.md).

## Known limitations

- Filter value dropdowns in the segment builder don't currently support sorting. Use the search box within the dropdown to find specific values.

## Next steps

- [Create complex segments with segment builder](segment-builder.md)


[!INCLUDE [footer-include](includes/footer-banner.md)]
