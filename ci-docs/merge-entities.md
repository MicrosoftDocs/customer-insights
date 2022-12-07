---
title: "Unify customer fields for data unification"
description: "Merge entities to create unified customer profiles."
recommendations: false
ms.date: 12/6/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: v-wendysmith
ms.author: sstabbert
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-merge
  - ci-match
  - ci-relationships
  - customerInsights
---

# Unify customer fields

In this step of the unification process, choose and exclude attributes to merge within your unified profile entity. For example, if three entities had email data, you may want to keep all three separate email fields or merge them into a single email field for the unified profile. Some attributes are automatically combined by the system.

In this step, you can create stable and unique customer IDs and for individual customers, group related profiles into a cluster.

:::image type="content" source="media/m3_unify.png" alt-text="Unify customer fields page in the data unification process showing table with merged fields that define the unified customer profile.":::

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

1. Optionally for B-to-C, [group profiles into households or clusters](#group-profiles-into-households-or-clusters).

> [!div class="nextstepaction"]
> [Next step: Review unification](review-unification.md)

### Edit a merged field

1. Select a merged field and choose **Edit**. The Combine fields pane displays.

1. Specify how to combine or merge the fields from one of three options:
    - **Importance**: Identifies the winner value based on importance rank specified for the participating fields. It's the default merge option. Select **Move up/down** to set the importance ranking.

      > [!NOTE]
      > Customer Insights uses the first non-null value. For example, given entities A, B, and C ranked in that order, if A.Name and B.Name are null, then the value from C.Name is used.

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

Exclude a merged or separate field from the unified customer profile. If the field is used in other processes, such as a segment, remove it from these processes. Then, exclude it from the customer profile.

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

When you combine a group of fields, Customer Insights treats the group as a single unit, and chooses the winner record based on a merge policy. When merging fields without combining them into a group, Customer Insights chooses the winner record for each field based on the entity order ranking set up in the **Match conditions** step. If a field has a null value, Customer Insights continues to look at the other data sources until it finds a value. If this mixes information in an unwanted way or you want to set a merge policy, combine the group of fields.

#### Example
Monica Thomson matches across three data sources: Loyalty, Online, and POS. Without combining the mailing address fields for Monica, the winner record for each field is based on the first ranked data source (Loyalty), except **Addr2** which is null. The winner record for **Addr2** is Suite 950 resulting in a less than ideal mailing address (200 Cedar Springs Road, Suite 950 Dallas, TX 75255). To treat the address fields as a whole, combine the address fields into a group. The result is a current mailing address.

**Table1 - Loyalty**

| Full_Name      | Addr1                  | Addr2     | City    | State | Zip   |
|----------------|------------------------|-----------|---------|-------|-------|
| Monica Thomson | 200 Cedar Springs Road |           | Dallas | TX    | 75255 |

**Table2 - Online**

| Name           | Addr1                | Addr2     | City    | State | Zip   |
|----------------|----------------------|-----------|---------|-------|-------|
| Monica Thomson | 5000 15th Street     | Suite 950 | Redmond | WA    | 98052 |

**Table3 - POS**

| Full_Name      | Add1                 | Add2      | City    | State | Zip   |
|----------------|----------------------|-----------|---------|-------|-------|
| Monica Thomson | 100 Main Street      | Suite 100 | Seattle | WA    | 98121 |

#### Create a group of fields

1. Select **Combine** > **Group of fields**.

   :::image type="content" source="media/merge-combine-group.png" alt-text="Combine group of fields screen.":::

1. Specify the merge winner policy in the **Rank groups by** dropdown. The same merge policy is used for all the fields that make up the group.

   - **Importance**: Identifies the winner record as the group of fields with the highest ranking. The highest ranking is the data source you select for Group 1. Importance is the default value.
   - **Most recent**: Identifies the winner record as the group of fields with the most recency. Requires a date to define the recency.
   - **Least recent**: Identifies the winner record as the group of fields with the least recency. Requires a date to define the recency.

1. To add more than two fields for your combined group, select **Add** > **Field**. Add as many as 10 fields.

1. To add more than two data sources for your combined group, select **Add** > **Group**. Add as many as 15 data sources.

1. Enter the following information for each field you're combining:

   - **Name**: Unique name of the field you want in the grouping. You can’t use a name from your data sources.
   - **Output name**: Automatically filled in and displays in the Customer profile.
   - **Group 1**: The field from the first data source that corresponds to the **Name**. The ranking of your data sources indicates the order in which the system identifies and merges the records by **Importance**.
     > [!NOTE]
     > In the drop-down for a group, the list of fields is categorized by data source.
     > :::image type="content" source="media/merge-combine-datasource.png" alt-text="Combine group of fields screen with Group drop-down and data source highlighted.":::
   - **Group2**: The field in the next data source that corresponds to the **Name**. Repeat for each data source you include.

1. Provide a **Name** for the combined group of fields, such as mailing address. This name displays on the Unify step but doesn't appear in the Customer profile.

   :::image type="content" source="media/merge-combine-group-example.png" alt-text="Combine group of fields example.":::

1. Select **Done** to apply the changes. The name for the combined group displays on the **Unified customer fields** page, but not in the Customer profile. 

   :::image type="content" source="media/unify-combine-group-example.png" alt-text="Unified customer fields page highlighting the combine group name.":::

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

For individual customers, you can define rules to group related profiles into a cluster. There are currently two types of clusters available – household and custom clusters. The system automatically chooses a household with predefined rules if the *Customer* entity contains the semantic fields *Person.LastName* and *Location.Address*. You can also create a cluster with your own rules and conditions, similar to [match rules](match-entities.md#define-rules-for-match-pairs).

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
