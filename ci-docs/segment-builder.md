---
title: "Create complex segments with segment builder"
description: "Use segment builder to create complex segments of customers by grouping them based on various attributes."
ms.date: 08/12/2022

ms.subservice: audience-insights
ms.topic: how-to
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-segments
  - ci-segment-builder
  - ci-segment-details
  - customerInsights
---

# Create complex segments with segment builder

Define complex filters around the unified customer or unified contact and its related tables. Each segment, after processing, creates a set of customer or contact records that you can export and take action on.

> [!TIP]
> Segments based on **individual customers** automatically include available contact information for segment members. In **business accounts**, if you [unified](data-unification.md) both accounts and contacts, choose whether the segment is based on accounts or business contacts. To export to a destination expecting contact information, use a segment of contacts. To export to a destination expecting account information, use a segment of accounts.

## Segment builder

The following image illustrates the various aspects of the segment builder. It shows a segment that results in a group of customers. The customers ordered goods in a specific time frame and gathered reward points or spent a certain amount of money.

:::image type="content" source="media/segment-builder-overview.png" alt-text="Elements of the segment builder." lightbox="media/segment-builder-overview.png":::

1. Organize your segment with rules and subrules. Each rule or subrule consists of conditions. Combine the conditions with logical operators.

1. Choose the [relationship path](relationships.md) between tables that applies to a rule. The relationship path determines which attributes can be used in a condition.

1. Manage rules and subrules. Change the position of a rule or delete it.

1. Add conditions and build the right level of nesting using subrules.

1. Apply set operations to connected rules.

1. Use the attribute pane to add available table attributes or create conditions based on attributes. The pane shows the list of tables and attributes, based on the selected relationship path, that are available for the selected rule.

1. Add conditions based on attributes to existing rules and subrules or add it to a new rule.

1. Undo and redo changes while building the segment.

The example above illustrates the segmentation capability. We've defined a segment for customers who bought at least $500 of goods online *and* have an interest in software development.

## Create a new segment with segment builder

1. Go to **Insights** > **Segments**.

1. Select **New** > **Build your own**. On the segment builder page, you define or compose rules. A rule consists of one or more conditions that define a set of customers.

   > [!NOTE]
   > For environments based on business accounts, select **New** > **Segment of Accounts** or **Segment of Contacts (preview)** based on the type of segment you want to create. If an [account hierarchy](relationships.md#set-up-account-hierarchies) has been defined and you want to create rules to filter out data based on child and parent relationship, select **Use hierarchy? (preview)**, select the hierarchy, and then **Apply**.
   >
   > :::image type="content" source="media/segment_acct_hierarchy.png" alt-text="Segment select account hierarchy pane.":::

1. Select **Edit details** next to Untitled segment. Provide a name for your segment and update the suggested **Output table name** for the segment. Optionally, add a description and [tags](work-with-tags-columns.md#manage-tags) to the segment.

   :::image type="content" source="media/segments_edit_details.png" alt-text="Edit details dialog box.":::

1. In the **Rule1** section, choose an attribute of a table you want to filter customers by. There are two ways to choose attributes:
   - Review the list of available tables and attributes in the **Add to Rule** pane and select the **+** icon next to the attribute to add. Choose if you want to add the attribute to an existing rule or use it to create a new rule.
   - Type the name of the attribute in the rule section to see matching suggestions.

1. Choose the operators to specify the matching values of the condition. Attribute can have one of four data types as value: numerical, string, date, or Boolean. Depending on the data type of the attribute, different operators are available to specify the condition.

1. Select **Add condition** to add more conditions to a rule. To create a rule under the current rule, select **Add sub-rule**.

1. If a rule uses other tables than the *Customer* table (or *ContactProfile* table for B-to-B), select **Set relationship path** to map the selected table to the unified customer table. If there's only one possible relationship path, the system selects it automatically. Different [relationship paths](relationships.md#relationship-paths) can yield different results. Every rule can have its own relationship path.

   :::image type="content" source="media/relationship-path.png" alt-text="Potential relationship path when creating a rule based on a table mapped to the unified customer table.":::

1. If you have multiple conditions in a rule, choose which logical operator connects them.  
   - **AND** operator: All conditions must be met to include a record in the segment. Use this option when you define conditions across different tables.
   - **OR** operator: Either one of the conditions must be met to include a record in the segment. Use this option when you define multiple conditions for the same table.

   :::image type="content" source="media/segmentation-either-condition.png" alt-text="Rule with two AND conditions.":::

   When using the OR operator, all conditions must be based on tables included in the relationship path.

1. To create different sets of customer records, create multiple rules. To include the customers required for your business case, combine groups. Specifically, if you can't include a table in a rule because of the specified relationship path, create a new rule to choose attributes from it.

      :::image type="content" source="media/segment-rule-grouping.png" alt-text="Add a new rule to a segment and choose the set operator.":::

   1. Select **Add rule**.
   1. Select one of the set operators: **Union**, **Intersect**, or **Except**.

      - **Union** unites the two groups.
      - **Intersect** overlaps the two groups. Only data that *is common* to both groups remains in the unified group.
      - **Except** combines the two groups. Only data in group A that *is not common* to data in group B is kept.

1. By default, the output table will automatically contain all attributes of customer profiles that match the defined filters. In B-to-B when using the *ContactProfile* table, the Account ID is automatically included. If a segment is based on other tables than the *Customer* table or to include more attributes from the *ContactProfile*, select **Project attributes** to add more attributes from these tables to the output table.
 
   For example: A segment is based on a table that contains purchase data, which is related to the *Customer* table. The segment looks for all customers from Spain that purchased goods in the current year. You can choose to append attributes like the price of goods, or the purchase date to all matching customer records in the output table. This information might be useful to analyze seasonal correlations to the total spending.

   :::image type="content" source="media/segments-project-attributes.png" alt-text="Example of projected attributes selected in the side pane to be added to the output table.":::
 
   A sample output for a segment based on business accounts with projected attributes of contacts could look like this:

   |ID  |Account name  |Revenue  |Contact name  | Contact role|
   |---------|---------|---------|---------|---|
   |10021     | Contoso | 100K | [Abbie Moss, Ruth Soto]  | [CEO, Procurement manager]

   > [!NOTE]
   > - **Project attributes** only work for tables that have a one-to-many relationship with the *Customer* or *ContactProfile* table. For example, one customer can have multiple subscriptions.
   > - If the attribute you want to project is more than one hop away from the *Customer* or *ContactProfile* table, as defined by the relationship, that attribute should be used in every rule of the segment query you are building.
   > - If the attribute you want to project is just one hop away from the *Customer* or *ContactProfile* table, that attribute doesn't need to be present in every rule of the segment query you are building.
   > - **Projected attributes** are factored in when using set operators.

1. Select **Run** to create the segment. Select **Save** if you want to keep the current configuration and run the segment later. The **Segments** page displays.

### Segment builder tips

When creating a segment using the segment builder, keep in mind the following tips:

- The segment builder won't suggest valid values from tables when setting the operators for the conditions. You can go to **Data** > **Tables** and download the table data to see which values are available.
- Conditions based on dates let you switch between fixed dates and a floating date range.
- If you have multiple rules for your segment, the rule you're editing has a vertical blue line next to it.
- You can move rules and conditions to other places in the segment definition. Select the vertical ellipsis (&vellip;) next to a rule or condition and choose how and where to move it.
- The **Undo** and **Redo** controls in the command bar let you roll back changes.
- After creating a segment, some segments allow you to [track the usage of the segment](segments.md#track-usage-of-a-segment).

## Next steps

[Export a segment](export-destinations.md) and explore the [Customer Card integration](customer-card-add-in.md) to use segments in other applications.

[!INCLUDE [footer-include](includes/footer-banner.md)]
