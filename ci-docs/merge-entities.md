---
title: "Unify customer or account fields"
description: "Merge entities to create unified customer profiles."
recommendations: false
ms.date: 04/22/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: v-wendysmith
ms.author: mukeshpo
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-merge
  - ci-match
  - ci-relationships
  - customerInsights
---

# Unify customer fields

In this step of the unification process, choose and exclude attributes to merge within your unified profile entity. You can also create stable and unique Customer IDs.

:::image type="content" source="media/m3_unify.png" alt-text="Merge page in the data unification process showing table with merged fields that define the unified customer profile.":::

## Review and update the customer fields

1. Review the list of fields that will be unified under the **Customer fields** tab of the table. Make any changes if applicable.

   1. For any single fields, you can:
      - [Combine fields](#combine-fields-manually)
      - [Combine a group of fields](#combine-a-group-of-fields)
      - [Rename](#rename-fields)
      - [Exclude](#exclude-fields)
      - [Move up or down](#change-the-order-of-fields)

   1. For any combined fields, you can:
      - [Edit](#edit-a-merged-field)
      - [Rename](#rename-fields)
      - [Separate](#separate-merged-fields)
      - [Exclude](#exclude-fields)
      - [Move up or down](#change-the-order-of-fields)

1. Optionally, [generate the CustomerID configuration](#configure-customer-id-generation).

> [!div class="nextstepaction"]
> [Next step: Review unification](review-unification.md)

### Combine fields manually

Combine separated fields to create a merged attribute.

1. Select **Combine** > **Fields**.

1. Specify the merge winner policy in the **Combine fields by** dropdown.

1. Select **Add field** to combine more fields.

1. Provide a **Name** and an **Output field name**.

1. Select **Done** to apply the changes.

1. Select **Save**.

### Combine a group of fields

Treat a group of fields as a single unit. For example, if our records contain the fields Address1, Address2, City, State, and Zip, we don't want to merge in a different record’s Address2, thinking it would make our data more complete.

1. Select **Combine** > **Group of fields**.

1. Specify the merge winner policy in the **Rank groups by** dropdown.

1. Select **Add** and choose if you want to add more fields or additional groups to the fields.

1. Provide a **Name** and an **Output name** for every combined field.

1. Provide a **Name** for the group of fields.

1. Select **Done** to apply the changes.

1. Select **Save**.

### Rename fields

Change the display name of merged or separate fields. You can't change the name of the output entity.

1. Select the field.
  
1. Select **Show more** and choose **Rename**.

1. Confirm the changed display name.

1. Select **Save**.

### Exclude fields

Exclude a merged or separate field from the unified customer profile. If the field is used in other processes, for example in a segment, remove it from these processes before excluding it from the customer profile.

1. Select a field.
  
1. Select **Show more** and choose **Exclude**.

1. Confirm the exclusion.

1. Select **Save**.

To see the list of all excluded fields, select **Excluded fields**. If necessary, you can re-add the excluded field.

### Change the order of fields

Some entities contain more details than others. If an entity includes the latest data about a field, you can prioritize it over other entities when merging values.

1. Select the field.
  
1. Select **Show more** and choose **Move up/down** to set the order or drag and drop them in the desired position.

1. Select **Done**.

### Edit a merged field

1. Select a merged field.

1. Select **Show more** and choose **Edit**.

1. Specify how to combine or merge the fields from one of three options:
    - **Importance**: Identifies the winner value based on importance rank specified for the participating fields. It's the default merge option. Select **Move up/down** to set the importance ranking.

      :::image type="content" source="media/importance-merge-option.png" alt-text="Importance option in the merge fields dialog.":::

    - **Most recent**: Identifies the winner value based on the most recency. Requires a date or a numeric field for every participating entity in the merge fields scope to define the recency.

      :::image type="content" source="media/recency-merge-option.png" alt-text="Recency option in the merge fields dialog.":::

    - **Least recent**: Identifies the winner value based on the least recency. Requires a date or a numeric field for every participating entity in the merge fields scope to define the recency.

1. You can add more fields to participate in the merge process.

1. You can rename the merged field.

1. Select **Done** to apply your changes.

1. Select **Save**.

### Separate merged fields

To separate merged fields, find the attribute in the table. Separated fields show as individual data points on the unified customer profile.

1. Select the merged field.
  
1. Select **Show more** and choose **Separate fields**.

1. Confirm the separation.

1. Select **Save**.

## Configure Customer ID generation

Define how to generate CustomerId values, the unique customer profile identifiers. The unify fields step in the data unification process generates the unique customer profile identifier. The identifier is the CustomerId in the *Customer* entity that results from the data unification process.

The CustomerId in the Customer entity is based on a hash of the first value of the non-null winner primary keys. These keys come from the entities used in data unification and are influenced by the match order. So the generated CustomerID can change when a primary key value changes in the primary entity of the match order. So the primary key value might not always represent the same customer.

Configuring a stable customer ID enables you to avoid that behavior.

1. Select the **Keys** tab.

1. Hover on the **CustomerId** row and select **Configure**.
   :::image type="content" source="media/customize-stable-id.png" alt-text="Control to customize the ID generation.":::

1. Select up to five fields that will comprise a unique customer ID and are more stable. Records that don’t match your configuration use a system-configured ID instead.  

1. Select **Done**.

> [!div class="nextstepaction"]
> [Next step: Review unification](review-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
