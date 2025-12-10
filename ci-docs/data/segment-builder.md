---
title: "Create complex segments with segment builder"
description: "Use segment builder to create complex segments of customers by grouping them based on various attributes."
ms.date: 08/28/2023
ms.topic: how-to
author: JimsonChalissery
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Create complex segments with segment builder

Define complex filters around the unified customer and its related tables. Each segment, after processing, creates a set of customer records that you can export and take action on.

## Create a new segment with segment builder

For an illustration of the key aspects of segment builder, see [Aspects of segment builder](segment-builder-aspects.md). For tips, see [Segment builder tips](segment-builder-aspects.md#segment-builder-tips).

1. Go to **Segments**.

1. Select **New** > **Build your own**. On the segment builder page, you define or compose rules. A rule consists of one or more conditions that define a set of customers.

1. Select **Edit details** next to Untitled segment. Provide a name for your segment and update the suggested **Output table name** for the segment. Optionally, add a description and [tags](work-with-tags-columns.md#manage-tags) to the segment.

1. In the **Rule1** section, choose an attribute of a table you want to filter customers by. There are two ways to choose attributes:
   - Review the list of available tables and attributes in the **Add to Rule** pane and select the **+** icon next to the attribute to add. Choose if you want to add the attribute to an existing rule or use it to create a new rule.
   - Type the name of the attribute in the rule section to see matching suggestions.

1. Choose the operators to specify the matching values of the condition. Attributes can have one of four data types as a value: numerical, string, date, or Boolean. Depending on the data type of the attribute, different operators are available to specify the condition.

1. Select **Add condition** to add more conditions to a rule. To create a rule under the current rule, select **Add sub-rule**.

1. If a rule uses other tables than the *Customer* table, select **Set relationship path** to map the selected table to the unified customer table. If there's only one possible relationship path, the system selects it automatically. Different [relationship paths](relationships.md#relationship-paths) can yield different results. Every rule can have its own relationship path.

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

1. By default, the output table will automatically contain all attributes of customer profiles that match the defined filters. If a segment is based on other tables than the *Customer* table, select **Project attributes** to add more attributes from these tables to the output table.

   For example: A segment is based on a table that contains purchase data, which is related to the *Customer* table. The segment looks for all customers from Spain that purchased goods in the current year. You can choose to append attributes like the price of goods, or the purchase date to all matching customer records in the output table. This information might be useful to analyze seasonal correlations to the total spending.

   :::image type="content" source="media/segments-project-attributes.png" alt-text="Example of projected attributes selected in the side pane to be added to the output table.":::

   > [!NOTE]
   > - **Project attributes** only work for tables that have a one-to-many relationship with the *Customer* table. For example, one customer can have multiple subscriptions.
   > - If the attribute you want to project is more than one hop away from the *Customer* table, as defined by the relationship, that attribute should be used in every rule of the segment query you are building.
   > - If the attribute you want to project is just one hop away from the *Customer*  table, that attribute doesn't need to be present in every rule of the segment query you are building.
   > - **Projected attributes** are factored in when using set operators.

1. To save the configuration, select **Save** and then **Close**. The segment is in draft mode or inactive so you can make changes to the configuration before actually creating the segment.

1. To create the segment, select **Run**.

## Next steps

- [Schedule a segment](segments-schedule.md).
- [Export a segment](export-manage.md) and explore the [Customer Card integration](customer-card-add-in.md) to use segments in other applications.

[!INCLUDE [footer-include](includes/footer-banner.md)]
