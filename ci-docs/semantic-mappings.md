---
title: "Semantic mappings (preview)"
description: "Overview of semantic mappings and how to use them." 
ms.date: 08/12/2022

ms.reviewer: v-wendysmith
ms.topic: conceptual
author: CadeSanthaMSFT
ms.author: cadesantha
searchScope: 
  - ci-semantic-mapping
  - customerInsights
---

# Semantic mappings (preview)

> [!NOTE]
> The **Semantic mappings** page is available only for business environments (B-to-B) where contact profiles have already been created using this page. You can continue to create and manage the individual contact profiles using the **Semantic mappings** page. Or, [unify your contact data](data-unification-contacts.md) to remove duplicates, identify matches across entities, and create one unified contact profile. You can then use the unified contact profile to create contact-level activities.

Semantic mappings let you map your non-activity data to pre-defined schemas. These schemas help Customer Insights to better understand your data attributes. Semantic mapping and the provided data enable new insights and features in Customer Insights. To map your activity data to the schemas, review the [activities](activities.md) documentation.

## Define a ContactProfile semantic entity mapping

1. Go to **Data** > **Semantic mappings (preview)**.

1. Select **Add semantic mapping** to start the guided experience.

1. In the **Entity data** step, set the values for the following fields:

   - **Semantic entity mapping name**: Name for your semantic entity mapping.
   - **Source Entity**: Entity that includes contact data.
   - **Primary key**: Field that uniquely identifies a contact record. It shouldn't contain any duplicate values, empty values, or missing values.

   :::image type="content" source="media/Semantic_Mapping_Wizard1.png" alt-text="Set up the semantic entity mapping with name, source entity, and primary key.":::

1. Select **Next**.

1. In the **Relationships** step, configure the details to connect your contact data to its corresponding account data. This step visualizes the connection between entities.  

   There are two types of relationship paths that can be implemented: **Direct relationships** and **Indirect relationships**. For more information, go to [direct and indirect relationship paths](relationships.md#relationship-paths).

   1. Select **Add Relationship** to configure the relationship.
   1. Choose the attribute from your source entity that connects your contact entity to another entity.
   1. Choose the entity to connect your contact entity to. Choose an entity from the **Account entities** or the **Intermediate entity** section. If you select an intermediate entity, define a second relationship to connect to your target account entity.

      :::image type="content" source="media/Semantic_Mapping_Wizard2.png" alt-text="Select either an Account entity or an Intermediate entity.":::

   1. Provide a **Relationship name**. If a relationship between your entities already exists, the relationship name is read-only. If no relationship exists, a new relationship will be created with the name you provide.
   1. Select **Apply** to finish the relationship configuration.

   > [!NOTE]
   > You can configure more relationships between the contact entity and other account entities with intermediate entities.
   
     :::image type="content" source="media/Semantic_Mapping_Wizard4.png" alt-text="Visualization of various relationships connect contact entities to account entities.":::

1. Select **Next**.

1. In the **Set the semantic type** step, choose a **Semantic type**. Currently, there's one **Semantic Type** called *ContactProfile*.

1. Map your contact id to the *ContactProfile* semantic type **Contact ID**. Optionally, map other fields such as first name, last name, gender, or email.

   :::image type="content" source="media/Semantic_Mapping_Wizard5.png" alt-text="Map your contact data attributes to the provided required and optional fields.":::

1. Select **Next**.

1. In the **Review** step, review the configuration of the semantic mapping. To make changes, select **Edit** for the corresponding section.

1. Select **Save**.

1. To process the semantic mapping, select **Run**. Or select **Close** to save your semantic mapping without processing it. To run it later, select the semantic mapping and select **Refresh**.

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

## Manage existing semantic mappings

Go to **Data** > **Semantic mappings (preview)** to view your saved semantic mappings, their source entity, semantic type, mapping type, and status.

:::image type="content" source="media/semantic-mapping-options.png" alt-text="Options to manage semantic mappings.":::

Select the semantic mapping to view available actions.
- **Edit** the current configuration. Select **Save** and **Run** to process the changes.
- **Refresh** the semantic mapping to include the latest data. Refreshing any given semantic mapping will refresh all semantic mappings of the same type.
- **Rename** the semantic mapping. Select **Save**.
- **Delete** the semantic mapping. To delete more than one semantic mapping at once, select the semantic mappings and the delete icon. Select **Delete** to confirm the deletion.

[!INCLUDE [footer-include](includes/footer-banner.md)]
