---
title: "Create business account or contact segments with segment builder"
description: "Use segment builder to create complex segments of account or contact by grouping them based on various attributes."
ms.date: 09/01/2023
ms.topic: how-to
author: JimsonChalissery
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Create business account or contact segments with segment builder



Define complex filters around the unified customer or unified contact and its related tables. Each segment, after processing, creates a set of customer or contact records that you can export and take action on.

In **business accounts**, if you [unified](../data-unification.md) both accounts and contacts, choose whether the segment is based on accounts or business contacts. To export to a destination expecting contact information, use a segment of contacts. To export to a destination expecting account information, use a segment of accounts.

## Create a new segment with segment builder

For an illustration of the key aspects of segment builder, see [Aspects of segment builder](../segment-builder-aspects.md). For tips, see [Segment builder tips](../segment-builder-aspects.md#segment-builder-tips).

1. Go to **Segments**.

1. Select **New** > **Segment of Accounts** or **Segment of Contacts (preview)** based on the type of segment you want to create. On the segment builder page, you define or compose rules. A rule consists of one or more conditions that define a set of customers.

1. If an [account hierarchy](account-hierarchies.md) has been defined and you want to create rules to filter out data based on child and parent relationship, select **Use hierarchy? (preview)**, select the hierarchy, and then **Apply**.

   :::image type="content" source="media/segment_acct_hierarchy.png" alt-text="Segment select account hierarchy pane.":::

1. Select **Edit details** next to Untitled segment. Provide a name for your segment and update the suggested **Output table name** for the segment. Optionally, add a description and [tags](../work-with-tags-columns.md#manage-tags) to the segment.

1. In the **Rule1** section, choose an attribute of a table you want to filter customers by. There are two ways to choose attributes:
   - Review the list of available tables and attributes in the **Add to Rule** pane and select the **+** icon next to the attribute to add. Choose if you want to add the attribute to an existing rule or use it to create a new rule.
   - Type the name of the attribute in the rule section to see matching suggestions.

1. Choose the operators to specify the matching values of the condition. Attributes can have one of four data types as a value: numerical, string, date, or Boolean. Depending on the data type of the attribute, different operators are available to specify the condition.

1. Select **Add condition** to add more conditions to a rule. To create a rule under the current rule, select **Add sub-rule**.

1. If a rule uses other tables than the *Customer* table or *UnifiedContact* table, select **Set relationship path** to map the selected table to the unified customer table. If there's only one possible relationship path, the system selects it automatically. Different [relationship paths](../relationships.md#relationship-paths) can yield different results. Every rule can have its own relationship path.

1. If you have multiple conditions in a rule, choose which logical operator connects them.  
   - **AND** operator: All conditions must be met to include a record in the segment. Use this option when you define conditions across different tables.
   - **OR** operator: Either one of the conditions must be met to include a record in the segment. Use this option when you define multiple conditions for the same table.

   :::image type="content" source="../media/segmentation-either-condition.png" alt-text="Rule with two AND conditions.":::

   When using the OR operator, all conditions must be based on tables included in the relationship path.

1. To create different sets of customer records, create multiple rules. To include the customers required for your business case, combine groups. Specifically, if you can't include a table in a rule because of the specified relationship path, create a new rule to choose attributes from it.

      :::image type="content" source="../media/segment-rule-grouping.png" alt-text="Add a new rule to a segment and choose the set operator.":::

   1. Select **Add rule**.
   1. Select one of the set operators: **Union**, **Intersect**, or **Except**.

      - **Union** unites the two groups.
      - **Intersect** overlaps the two groups. Only data that *is common* to both groups remains in the unified group.
      - **Except** combines the two groups. Only data in group A that *is not common* to data in group B is kept.

1. By default, the output table will automatically contain all attributes of customer profiles that match the defined filters. When using the *UnifiedContact* table, the Account ID is automatically included. If a segment is based on other tables than the *Customer* table or to include more attributes from the *UnifiedContact*, select **Project attributes** to add more attributes from these tables to the output table.

   A sample output for a segment based on business accounts with projected attributes of contacts could look like this:

   |ID  |Account name  |Revenue  |Contact name  | Contact role|
   |---------|---------|---------|---------|---|
   |10021     | Contoso | 100K | [Abbie Moss, Ruth Soto]  | [CEO, Procurement manager]

   > [!NOTE]
   >
   > - **Project attributes** only work for tables that have a one-to-many relationship with the *Customer* or *UnifiedContact* table. For example, one customer can have multiple subscriptions.
   > - If the attribute you want to project is more than one hop away from the *Customer* or *UnifiedContact* table, as defined by the relationship, that attribute should be used in every rule of the segment query you are building.
   > - If the attribute you want to project is just one hop away from the *Customer* or *UnifiedContact* table, that attribute doesn't need to be present in every rule of the segment query you are building.
   > - **Projected attributes** are factored in when using set operators.

1. To save the configuration, select **Save** and then **Close**. The segment is in draft mode or inactive so you can make changes to the configuration before actually creating the segment.

1. To create the segment, select **Run**.

   > [!TIP]
   > When viewing segments on the **Segments** page, the **Audience Type** column identifies whether a segment is based on accounts or contacts.

[!INCLUDE [footer-include](../includes/footer-banner.md)]
