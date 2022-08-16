---
title: "Select source fields for data unification"
description: "The first step in the unification process is selecting entities, attributes, primary keys, and semantic types to map data to the unified customer profile."
recommendations: false
ms.date: 08/12/2022

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

The first step in unification is selecting the entities and fields within your datasets that you want to unify. Select entities that contain customer-related details such as name, address, phone number, and email. You can select one or more entities.

[!INCLUDE [m3-first-run-note](includes/m3-first-run-note.md)]

## Select entities and fields

1. Go to **Data** > **Unify**.

   For individual customers (B-to-C), the **Unify** landing page displays showing **Get started** on the first step, **Source fields**.

   :::image type="content" source="media/m3_unify_land.png" alt-text="Screenshot of unify landing page for first run experience for individual customers.":::

   For business accounts (B-to-B), the **Unify** landing page displays **Unify accounts** showing **Get started** on the first step, **Source fields**. The **Unify contacts (preview)** steps are optional and pending completion of account unification.

   :::image type="content" source="media/b2b_unify_land.png" alt-text="Screenshot of unify landing page for first run experience for business accounts.":::

1. Select **Get started**.

1. On the **Source fields** page, select **Select entities and fields**. The **Select entities and fields** pane displays.

1. Select at least one entity.

1. For each selected entity, identify the fields you want to use to match customer records and fields to include in the unified profile. These fields are called *Attributes*. You can select the required attributes individually from an entity or include all attributes from an entity by selecting the checkbox on the entity level. You can search on keywords across all attributes and entities to select the required attributes you want to map.

   :::image type="content" source="media/m3_select_entities.png" alt-text="Screenshot of selected entities and attributes.":::

   In this example, we're adding the **eCommerceContacts** and **loyCustomer** entities. By choosing these entities, you can derive insights on which of the online business customers are loyalty program members.

1. Select **Apply** to confirm your selections. The selected entities and attributes display.

## Select primary key and semantic type for attributes

   :::image type="content" source="media/m3_select_primary.png" alt-text="Screenshot of selected entities with primary key not yet selected." lightbox="media/m3_select_primary.png":::

For each entity, perform the following steps.

1. Choose the **Primary key**. The primary key is an attribute unique to the entity. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.

1. To use AI models for smart prediction of semantics which saves time and improves accuracy, ensure **Intelligent mapping** is on. Intelligent mapping provides AI-based semantic recommendations in the **Type** field.

1. For each attribute, choose a semantic **Type** that best describes that attribute, such as name, city, or email address.

   > [!NOTE]
   > In B-to-C, one field should map to the semantic type *Person.FullName* to populate the customer name in the customer card. In B-to-B, the account name should map to *Organization.Name*. Otherwise, the customer cards will appear nameless.

   1. To override an attribute type identified by the system, select another option. If the type doesn't exist, create a custom semantic type by selecting the **Type** field for the attribute and entering your custom semantic type name.

   1. To add an attribute that contains a URL to publicly available profile images or logos, select the entity and field that contains the URL. In the **Type** field, enter the following:
      - For a person: Person.ProfileImage
      - For an organization: Organization.LogoImage

1. Review the attributes where a semantic type is automatically identified. These attributes are listed under **Review mapped fields**. Only attributes with the same type can be combined in the **Unify customer fields** step. Semantic types are used to automatically suggest insights. Ensure the types you chose are consistent across all the selected entities.

1. For attributes that aren't automatically mapped to a semantic type, select a semantic type field, enter your custom attribute type name, or leave them unmapped. These attributes are listed under **Define the data in the unmapped fields**.

1. After completing the steps for each entity, select **Save source fields**.

1. Select **Next**.

> [!div class="nextstepaction"]
> [Next step: Remove duplicates](remove-duplicates.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
