---
title: "Select source fields for data unification"
description: "The first step in the unification process is selecting entities, attributes, primary keys, and semantic types to map data to the unified customer profile."
ms.date: 04/08/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: v-wendysmith
ms.author: mukeshpo
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-map
  - ci-match
  - customerInsights
---

# Select source fields for data unification

The first step in customer or account unification is selecting the entities and attributes within your datasets that you want to unify. Select entities that contain customer-related details such as name, address, and email. You can select one or more entities.

## Select entities and fields

1. Go to **Data** > **Unify**.

1. Select **Get started**.

   :::image type="content" source="media/m3_unify_land.png" alt-text="Screenshot of unify landing page with Guide me highlighted.":::

1. On the **Source fields** page, select **Select entities and fields**. The **Select entities and fields** pane displays.

1. Select the **Entities** to combine into a customer or account profile.

1. For each selected entity, identify the columns you want to combine and reconcile. These columns are called *Attributes*. You can select the required attributes individually from an entity or include all attributes from an entity by selecting the checkbox on the entity level. You can search on keywords across all attributes and entities to select the required attributes you want to map.

   :::image type="content" source="media/m3_select_entities.png" alt-text="Screenshot of selected entities and attributes.":::

   In this example, we're adding the **Contacts** and **CustomerLoyalty** entities. By choosing these entities, you can derive insights on which of the online business customers are loyalty program members.

1. Select **Apply** to confirm your selections. The selected entities and attributes display.

## Select primary key and semantic type for attributes

   :::image type="content" source="media/m3_select_primary.png" alt-text="Screenshot of selected entities with primary key not selected.":::

For each entity, perform the following steps.

1. Choose the **Primary key**. The primary key is an attribute unique to the entity. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.

1. To use AI models for smart prediction of semantics, save time and improve accuracy, ensure **Intelligent mapping** is on. Intelligent mapping highlights AI-based semantics recommendation in the **Type** field. You can override the suggested selection by choosing any semantic type from the available list of options.

1. For each attribute, choose a semantic **Type** that best describes that attribute, such as name, city, or email address.

   > [!NOTE]
   > One field should map to the semantic type Person.FullName to populate the customer name in customer card. Otherwise, the customer cards will appear nameless.

   1. To change an attribute type identified by the system, add a custom semantic type. Select the **Type** field for an attribute, and enter your custom semantic type name.

   1. To add an attribute that contains a URL to publicly available profile images or logos, select the entity and field that contains the URL. In the **Type** field, enter the following:
      - For a person: Person.ProfileImage
      - For an organization: Organization.LogoImage

   1. For an organization (preview) attribute, enter "Organization.Name" in the **Type** field.

1. For attributes where a semantic type is automatically identified, review these attributes and types as they'll be used to combine your entities. These attributes are listed under **Review mapped fields**. Ensure the types you chose are consistent across all the selected entities.

1. For attributes that aren't automatically mapped to a semantic type, select a semantic type field, or enter your custom attribute-type name. These attributes are listed under **Define the data in the unmapped fields**.

1. After completing the steps for each entity, select **Next**.

> [!div class="nextstepaction"]
> [Next step: Remove duplicates](remove-duplicates.md)
