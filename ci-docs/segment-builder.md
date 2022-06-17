---
title: "Create complex segments with segment builder"
description: "Create segments of customers to group them based on various attributes."
ms.date: 03/25/2022

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

Define complex filters around the unified customer entity and its related entities. Each segment, after processing, creates a set of customer records that you can export and take action on.

> [!TIP]
> Segments based on **individual customers** automatically include available contact information for segment members. In environments for **business accounts**, segments are based on accounts (companies or subsidiaries). To include contact information in a segment, use the **Project attributes** functionality in the segment builder. Ensure that the contact data sources are [semantically mapped to the ContactProfile](semantic-mappings.md#define-a-contactprofile-semantic-entity-mapping) entity.

## Segment builder

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

## Create a new segment with segment builder

1. Go to the **Segments** page.

1. Select **New** > **Build your own**.

1. On the segment builder page, you define or compose rules. A rule consists of one or more conditions that define a set of customers.

1. In the **Rule1** section, choose an attribute of an entity you want to filter customers by. There are two ways to choose attributes:
   - Review the list of available entities and attributes in the **Add to Rule** pane and select the **+** icon next to the attribute to add. Choose if you want to add the attribute to an existing rule or use it to create a new rule.
   - Type the name of the attribute in the rule section to see matching suggestions.

1. Choose the operators to specify the matching values of the condition. Attribute can have one of four data types as value: numerical, string, date, or Boolean. Depending on the data type of the attribute, different operators are available to specify the condition. For segments with business accounts, two special operators are available to include potential hierarchies between the ingested accounts. Use the *child of* and *parent of* operators to include related accounts.

1. Select **Add condition** to add more conditions to a rule. To create a rule under the current rule, select **Add sub-rule**.

1. If a rule uses other entities than the *Customer* entity, select **Set relationship path** to map the selected entity to the unified customer entity. If there's only one possible relationship path, the system selects it automatically. Different [relationship paths](relationships.md#relationship-paths) can yield different results. Every rule can have its own relationship path.

   :::image type="content" source="media/relationship-path.png" alt-text="Potential relationship path when creating a rule based on an entity mapped to the unified customer entity.":::

1. If you have multiple conditions in a rule, choose which logical operator connects them.  
   - **AND** operator: All conditions must be met to include a record in the segment. This option is most useful when you define conditions across different entities.
   - **OR** operator: Either one of the conditions must be met to include a record in the segment. This option is most useful when you define multiple conditions for the same entity.

   :::image type="content" source="media/segmentation-either-condition.png" alt-text="Rule with two AND conditions.":::

   When using the OR operator, all conditions must be based on entities included in the relationship path.

   - To create different sets of customer records, create multiple rules. To include the customers required for your business case, combine groups. To create a new rule, select **Add rule**. Specifically, if you can't include an entity in a rule because of the specified relationship path, create a new rule to choose attributes from it.

      :::image type="content" source="media/segment-rule-grouping.png" alt-text="Add a new rule to a segment and choose the set operator.":::

   - Select one of the set operators: **Union**, **Intersect**, or **Except**.

      - **Union** unites the two groups.
      - **Intersect** overlaps the two groups. Only data that *is common* to both groups remains in the unified group.
      - **Except** combines the two groups. Only data in group A that *is not common* to data in group B is kept.

1. By default, segments generate the output entity containing all attributes of customer profiles that match the defined filters. If a segment is based on other entities than the *Customer* entity, you can add more attributes from these entities to the output entity. Select **Project attributes** to choose the attributes that will be appended to the output entity.

   > [!IMPORTANT]
   > For segments based on business accounts, details of one or more contacts of each account from the *ContactProfile* entity must be included in the segment to allow that segment to be activated or exported to destinations that require contact information. For more information about the *ContactProfile* entity, see [Semantic mappings](semantic-mappings.md).
   > A sample output for a segment based on business accounts with projected attributes of contacts could look like this:
   >
   > |ID  |Account name  |Revenue  |Contact name  | Contact role|
   > |---------|---------|---------|---------|---|
   > |10021     | Contoso | 100K | [Abbie Moss, Ruth Soto]  | [CEO, Procurement manager]

   :::image type="content" source="media/segments-project-attributes.png" alt-text="Example of projected attributes selected in the side pane to be added to the output entity.":::
  
   For example: A segment is based on an entity that contains purchase data, which is related to the *Customer* entity. The segment looks for all customers from Spain that purchased goods in the current year. You can choose to append attributes like the price of goods, or the purchase date to all matching customer records in the output entity. This information might be useful to analyze seasonal correlations to the total spending.

   > [!NOTE]
   > - **Project attributes** only works for entities that have a one-to-many relationship with the customer entity. For example, one customer can have multiple subscriptions.
   > - If the attribute you want to project is more than one hop away from the *Customer* entity, as defined by the relationship, that attribute should be used in every rule of the segment query you are building.
   > - If the attribute you want to project is just one hop away from the *Customer* entity, that attribute doesn't need to be present in every rule of the segment query you are building.
   > - **Projected attributes** are factored in when using set operators.

1. Select **Edit details** next to Untitled segment. Provide a name for your segment and update the suggested **Output entity name** for the segment. Optionally, add a description and [tags](work-with-tags-columns.md#manage-tags) to the segment.

   :::image type="content" source="media/segments_edit_details.png" alt-text="Edit details dialog box.":::

1. Select **Run** to save the segment, activate it, and begin processing your segment based on all the rules and conditions. The **Segments** page displays the new segment.

   > [!TIP]
   > Save a segment configuration as a draft and complete it later. As a draft, the segment is considered inactive. When ready, select **Run** or **Activate** to activate the segment.

## Segment builder tips

When creating a segment using the segment builder, keep in mind the following tips:

- The segment builder won't suggest valid values from entities when setting the operators for the conditions. You can go to **Data** > **Entities** and download the entity data to see which values are available.
- Conditions based on dates let you switch between fixed dates and a floating date range.
- If you have multiple rules for your segment, the rule you're editing has a vertical blue line next to it.
- You can move rules and conditions to other places in the segment definition. Select the vertical ellipsis (&vellip;) next to a rule or condition and choose how and where to move it.
- The **Undo** and **Redo** controls in the command bar let you roll back changes.
- After creating a segment, some segments allow you to [track the usage of the segment](segments.md#track-usage-of-a-segment).

## Next steps

[Export a segment](export-destinations.md) and explore the [Customer Card integration](customer-card-add-in.md) to use segments in other applications.

[!INCLUDE [footer-include](includes/footer-banner.md)]
