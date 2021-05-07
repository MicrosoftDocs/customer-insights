---
title: "Create and manage segments"
description: "Create segments of customers to group them based on various attributes."
ms.date: 05/03/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: mhart
manager: shellyha
---

# Create and manage segments

Define complex filters around the unified customer entity and its related entities. Each segment, after processing, creates a set of customer records that you can export and take action on. Segments are managed on the **Segments** page. 

The following example illustrates the segmentation capability. We've defined a segment for customers who ordered at least $500 of goods in the last 90 days *and* who were involved in a customer service call that got escalated.

:::image type="content" source="media/segmentation-group1-2.png" alt-text="Screenshot of the segment builder UI with two groups that specify a customer segment.":::

## Create a new segment

There are multiple ways to create a new segment. This section describes how to create a *blank segment* from scratch. You can also create a *quick segment* based on existing entities or make use of machine learning models to get *suggested segments*. More information: [Segments overview](segments.md).

While creating a segment, you can save a draft. It will be saved as an inactive segment, and can't be activated it finished with a valid configuration.

1. Go to the **Segments** page.

1. Select **New** > **Blank segment**.

1. In the **New segment** pane, choose a segment type:

   - **Dynamic segments** [refresh](segments.md#refresh-segments) on a recurring schedule.
   - **Static segments** run once when you create it.

1. Provide an **Output entity name** for the segment. Optionally, provide a display name, and a description that helps identifying the segment.

1. Select **Next** to get to the **Segment builder** page where you define a group. A group is a set of customers.

1. Choose the entity that includes the attribute you want to segment by.

1. Choose the attribute to segment by. This attribute can have one of four value types: numerical, string, date, or Boolean.

1. Choose an operator and a value for the selected attribute.

   > [!div class="mx-imgBorder"]
   > ![Custom group filter](media/customer-group-numbers.png "Customer group filter")

   |Number |Definition  |
   |---------|---------|
   |1     |Entity          |
   |2     |Attribute          |
   |3    |Operator         |
   |4    |Value         |

   1. To add more conditions to a group, you can use two logical operators:

      - **AND** operator: Both conditions must be met as part of the segmentation process. This option is most useful when you define conditions across different entities.

      - **OR** operator: Either one of the conditions needs to be met as part of the segmentation process. This option is most useful when you define multiple conditions for the same entity.

      > [!div class="mx-imgBorder"]
      > ![OR operator where either condition needs to be met](media/segmentation-either-condition.png "OR operator where either condition needs to be met")

      It's currently possible to nest an **OR** operator under an **AND** operator, but not the other way around.

   1. Each group matches set of customers. You can combine groups to include the customers required for your business case.    
   Select **Add Group**.

      > [!div class="mx-imgBorder"]
      > ![Customer group add group](media/customer-group-add-group.png "Customer group add group")

   1. Select one of the set operators: **Union**, **Intersect**, or **Except**.

   > [!div class="mx-imgBorder"]
   > ![Customer group add union](media/customer-group-union.png "Customer group add union")

   - **Union** unites the two groups.

   - **Intersect** overlaps the two groups. Only data that *is common* to both groups is retained in the unified group.

   - **Except** combines the two groups. Only data in group A that *is not common* to data in group B is retained.

1. If the entity is connected to the unified customer entity through [relationships](relationships.md), you need to define the relationship path to create a valid segment. Add the entities from the relationship path until you can select the **Customer:CustomerInsights** entity from the dropdown. Then, choose **All records** for each step.

   > [!div class="mx-imgBorder"]
   > ![Relationship path during segment creation](media/segments-multiple-relationships.png "Relationship path during segment creation")

1. By default, segments generate an output entity that contains all attributes of customer profiles which match the defined filters. If a segment is based on other entities than the *Customer* entity, you can add more attributes from these entities to the output entity. Select **Project attributes** to choose the attributes that will be appended to the output entity.  
  
   Example: A segment is based on an entity that contains customer activity data which is related to the *Customer* entity. The segment looks for all customers that called the help desk in the last 60 days. You can choose to append the call duration and the number of calls to all matching customer records in the output entity. This information might be useful to send an email with helpful links to online help articles and FAQs to customers who called frequently.

   > [!NOTE]
   > - Projected attributes only work for entities that have a one-to-many relationship with the customer entity. For example, one customer can have multiple subscriptions.
   > - You can only project attributes from an entity that is used in every group of segment query you are building.
   > - Projected attributes are factored in when using set operators.

1. Select **Save** to save your segment. Your segment will be saved and processed if all requirements are validated. Otherwise, it will be saved as a draft.

1. Select **Back to segments** to go back to the **Segments** page.



## Quick segments

Quick segments let you build simple segments with a single operator quickly for faster insights.

1. On the **Segments** page, select **New** > **Quickly create from**.

   - Select the **Profiles** option to build a segment that is based on the *unified customer* entity.
   - Select the **Measures** option to build a segment around  measures you have previously created.
   - Select the **Intelligence** option to build a segment around one of the output entities you generated using either the **Predictions** or **Custom Models** capabilities.

2. In the **New quick segment** dialog box, select an attribute from the **Field** dropdown.

3. The system will provide some additional insights that help you create better segments of your customers.
   - For categorical fields, we'll show 10 top customer counts. Choose a **Value** and select **Review**.

   - For a numerical attribute, the system will show what attribute value falls under each customer's percentile. Choose an **Operator** and a **Value**, then select **Review**.

4. The system will provide you with an **Estimated segment size**. You can choose whether to generate the segment you've defined, or first revisit it to get a different segment size.

    > [!div class="mx-imgBorder"]
    > ![Name and estimation for a quick segment](media/quick-segment-name.png "Name and estimation for a quick segment")

5. Provide a **Name** for your segment. Optionally, provide a **Display name**.

6. Select **Save** to create your segment.

7. After the segment has finished processing, you can view it like any other segment you've created.

## Next steps

[Export a segment](export-destinations.md) and explore the [Customer Card](customer-card-add-in.md) and [Connectors](export-power-bi.md) to get insights on the customer level.

[!INCLUDE[footer-include](../includes/footer-banner.md)]