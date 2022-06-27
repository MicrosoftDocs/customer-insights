---
title: "Unify customer fields for data unification"
description: "Merge entities to create unified customer profiles."
recommendations: false
ms.date: 05/04/2022

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

# Unify customer fields for data unification

[!INCLUDE [m3-prod-trial-note](includes/m3-prod-trial-note.md)]

In this step of the unification process, choose and exclude attributes to merge within your unified profile entity. For example, if three entities had email data, you may want to keep all three separate email fields or merge them into a single email field for the unified profile. Some attributes are automatically combined by the system. You can create stable and unique customer IDs and group related profiles into a cluster.

:::image type="content" source="media/m3_unify.png" alt-text="Merge page in the data unification process showing table with merged fields that define the unified customer profile.":::

## Review and update the customer fields

1. Review the list of fields that will be unified under the **Customer fields** tab of the table. Make any changes if applicable.

   1. For any combined fields, you can:
      - [Edit](#edit-a-merged-field)
      - [Rename](#rename-fields)
      - [Separate](#separate-merged-fields)
      - [Exclude](#exclude-fields)
      - [Move up or down](#change-the-order-of-fields)

   1. For any single fields, you can:
      - [Combine fields](#combine-fields-manually)
      - [Combine a group of fields](#combine-a-group-of-fields)
      - [Rename](#rename-fields)
      - [Exclude](#exclude-fields)
      - [Move up or down](#change-the-order-of-fields)

1. Optionally, [generate the customer ID configuration](#configure-customer-id-generation).

1. Optionally, [group profiles into households or clusters](#group-profiles-into-households-or-clusters).

> [!div class="nextstepaction"]
> [Next step: Review unification](review-unification.md)

### Edit a merged field

1. Select a merged field and choose **Edit**. The Combine fields pane displays.

1. Specify how to combine or merge the fields from one of three options:
    - **Importance**: Identifies the winner value based on importance rank specified for the participating fields. It's the default merge option. Select **Move up/down** to set the importance ranking.

      :::image type="content" source="media/importance-merge-option.png" alt-text="Importance option in the merge fields dialog.":::

    - **Most recent**: Identifies the winner value based on the most recency. Requires a date or a numeric field for every participating entity in the merge fields scope to define the recency.

      :::image type="content" source="media/recency-merge-option.png" alt-text="Recency option in the merge fields dialog.":::

    - **Least recent**: Identifies the winner value based on the least recency. Requires a date or a numeric field for every participating entity in the merge fields scope to define the recency.

1. You can add more fields to participate in the merge process.

1. You can rename the merged field.

1. Select **Done** to apply your changes.

### Rename fields

Change the display name of merged or separate fields. You can't change the name of the output entity.

1. Select the field and choose **Rename**.

1. Enter the new display name.

1. Select **Done**.

### Separate merged fields

To separate merged fields, find the attribute in the table. Separated fields show as individual data points on the unified customer profile.

1. Select the merged field and choose **Separate fields**.

1. Confirm the separation.

### Exclude fields

Exclude a merged or separate field from the unified customer profile. If the field is used in other processes, for example in a segment, remove it from these processes before excluding it from the customer profile.

1. Select a field and choose **Exclude**.

1. Confirm the exclusion.

To see the list of all excluded fields, select **Excluded fields**. If necessary, you can readd the excluded field.

### Change the order of fields

Some entities contain more details than others. If an entity includes the latest data about a field, you can prioritize it over other entities when merging values.

1. Select the field.
  
1. Choose **Move up/down** to set the order or drag and drop them in the desired position.

### Combine fields manually

Combine separated fields to create a merged attribute.

1. Select **Combine** > **Fields**. The Combine fields pane displays.

1. Specify the merge winner policy in the **Combine fields by** dropdown.

1. Select **Add field** to combine more fields.

1. Provide a **Name** and an **Output field name**.

1. Select **Done** to apply the changes.

### Combine a group of fields

Treat a group of fields as a single unit. For example, if our records contain the fields Address1, Address2, City, State, and Zip, we don't want to merge in a different record’s Address2, thinking it would make our data more complete.

1. Select **Combine** > **Group of fields**.

1. Specify the merge winner policy in the **Rank groups by** dropdown.

1. Select **Add** and choose if you want to add more fields or groups to the fields.

1. Provide a **Name** and an **Output name** for every combined field.

1. Provide a **Name** for the group of fields.

1. Select **Done** to apply the changes.

## Configure customer ID generation

Define how to generate customer ID values, the unique customer profile identifiers. The unify fields step in the data unification process generates the unique customer profile identifier. The identifier is the *CustomerId* in the *Customer* entity that results from the data unification process.

The *CustomerId* is based on a hash of the first value of the non-null winner primary keys. These keys come from the entities used in data unification and are influenced by the match order. So the generated customer ID can change when a primary key value changes in the primary entity of the match order. The primary key value might not always represent the same customer.

Configuring a stable customer ID enables you to avoid that behavior.

1. Select the **Keys** tab.

1. Hover on the **CustomerId** row and select **Configure**.
   :::image type="content" source="media/customize-stable-id.png" alt-text="Control to customize the ID generation.":::

1. Select up to five fields that will comprise a unique customer ID and are more stable. Records that don’t match your configuration use a system-configured ID instead.  

1. Select **Done**.

## Group profiles into households or clusters

You can define rules to group related profiles into a cluster. There are currently two types of clusters available – household and custom clusters. The system automatically chooses a household with predefined rules if the *Customer* entity contains the semantic fields *Person.LastName* and *Location.Address*. You can also create a cluster with your own rules and conditions, similar to [match rules](match-entities.md#define-rules-for-match-pairs).

1. Select **Advanced** > **Create cluster**.

   :::image type="content" source="media/create-cluster.png" alt-text="Control to create a new cluster.":::

1. Choose between a **Household** or a **Custom** cluster. If the semantic fields *Person.LastName* and *Location.Address* exist in the *Customer* entity, household is automatically selected.

1. Provide a name for the cluster and select **Done**.

1. Select the **Clusters** tab to find the cluster you created.

1. Specify the rules and conditions to define your cluster.

1. Select **Done**. The cluster is created when the unification process is complete. The cluster identifiers are added as new fields to the *Customer* entity.

> [!div class="nextstepaction"]
> [Next step: Review unification](review-unification.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
