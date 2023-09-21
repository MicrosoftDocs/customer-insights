---
title: "Select source fields for data unification"
description: "The first step in the unification process is selecting tables, attributes, primary keys, and semantic types to map data to the unified customer profile."
ms.date: 09/21/2023
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
---

# Select source fields for data unification

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

The first step in unification is selecting the tables and fields within your datasets that you want to unify. Select tables that contain customer-related details such as name, address, phone number, and email. You can select one or more tables.

[!INCLUDE [m3-first-run-note](includes/m3-first-run-note.md)]

## Select tables and fields

1. Go to **Data** > **Unify**.

   :::image type="content" source="media/m3_unify_land.png" alt-text="Screenshot of unify landing page for first run experience for individual customers.":::

1. Select **Get started**.

1. On the **Source fields** page, select **Select tables and fields**. The **Select tables and fields** pane displays.

1. Select at least one table.

1. For each selected table, identify the fields you want to use to match customer records and fields to include in the unified profile. These fields are called *Attributes*. You can select the required attributes individually from a table or include all attributes from a table by selecting the checkbox on the table level. You can search on keywords across all attributes and tables to select the required attributes you want to map.

   :::image type="content" source="media/m3_select_tables.png" alt-text="Screenshot of selected tables and attributes.":::

   In this example, we're adding the **eCommerceContacts** and **loyCustomer** tables. By choosing these tables, you can derive insights on which of the online business customers are loyalty program members.

1. Select **Apply** to confirm your selections. The selected tables and attributes display.

## Select primary key

   :::image type="content" source="media/m3_select_primary.png" alt-text="Screenshot of selected tables with primary key not yet selected." lightbox="media/m3_select_primary.png":::

For each table, perform the following steps.

1. Choose the **Primary key**. The primary key value uniquely identifies a row. Primary keys shouldn't have any duplicate, missing, or null values. String, integer, and GUID data type attributes are supported as primary keys.

1. Choose a **Type** that describes each attribute, such as Person.FullName, Location.City, or Identity.Service.Email. Mapping columns to types allows Customer Insights - Data to understand what columns represent and recommend rules, merge redundant data, and configure predictive models.

   > [!NOTE]
   > One field should map to the semantic type *Person.FullName* to populate the customer name in the customer card.

   1. To create a custom type, select the **Type** field for the attribute and enter your custom type name.

   1. To display a profile image on the **Customer** page, select the field that contains the publicly available URL and select *Person.ProfileImage*.

1. Review the recommended types to ensure intelligent mapping correctly identified the type for each field.

1. For attributes that aren't automatically mapped to a type, select a type field, enter a custom type, or leave them unmapped. These attributes are listed under **Define the data in the unmapped fields**. You don't need to map every column. However, columns with key demographic data (such as names and addresses) are important to map. Columns without a clear demographic type don't need to be mapped.

1. After completing the steps for each table, select **Save source fields**.

1. Select **Next**.

> [!div class="nextstepaction"]
> [Next step: Remove duplicates](data-unification-duplicates.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
