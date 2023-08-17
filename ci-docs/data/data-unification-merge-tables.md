---
title: "Unify customer fields for data unification"
description: "Merge tables to create unified customer profiles."
ms.date: 09/01/2023
ms.topic: how-to
author: v-wendysmith
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Unify customer fields

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

In this step of the unification process, choose and exclude attributes to merge within your unified profile table. For example, if three tables had email data, you may want to keep all three separate email fields or merge them into a single email field for the unified profile. Dynamics 365 Customer Insights - Data automatically combines some attributes.

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
> [Next step: Review unification](data-unification-review.md)

### Edit a merged field

1. Select a merged field and choose **Edit**. The Combine fields pane displays.

1. Specify how to combine or merge the fields from one of three options:
    - **Importance**: Identifies the winner value based on importance rank specified for the participating fields. It's the default merge option. Select **Move up/down** to set the importance ranking.

      > [!NOTE]
      > The system uses the first non-null value. For example, given tables A, B, and C ranked in that order, if A.Name and B.Name are null, then the value from C.Name is used.

      :::image type="content" source="media/importance-merge-option.png" alt-text="Importance option in the merge fields dialog.":::

    - **Most recent**: Identifies the winner value based on the most recency. Requires a date or a numeric field for every participating table in the merge fields scope to define the recency.

      :::image type="content" source="media/recency-merge-option.png" alt-text="Recency option in the merge fields dialog.":::

    - **Least recent**: Identifies the winner value based on the least recency. Requires a date or a numeric field for every participating table in the merge fields scope to define the recency.

1. You can add more fields to participate in the merge process.

1. You can rename the merged field.

1. Select **Done** to apply your changes.

### Rename fields

Change the display name of merged or separate fields. You can't change the name of the output table.

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

Some tables contain more details than others. If a table includes the latest data about a field, you can prioritize it over other tables when merging values.

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

When you combine a group of fields, Customer Insights - Data treats the group as a single unit, and chooses the winner record based on a merge policy. When merging fields without combining them into a group, the system chooses the winner record for each field based on the table order ranking set up in the **Match conditions** step. If a field has a null value, Customer Insights - Data continues to look at the other data sources until it finds a value. If this mixes information in an unwanted way or you want to set a merge policy, combine the group of fields.

#### Example
Monica Thomson matches across three data sources: Loyalty, Online, and POS. Without combining the mailing address fields for Monica, the winner record for each field is based on the first ranked data source (Loyalty), except **Addr2** which is null. The winner record for **Addr2** is Suite 950 resulting in an incorrect mix of address fields (200 Cedar Springs Road, Suite 950, Dallas, TX 75255). To ensure data  integrity, combine the address fields into a group.

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

1. Specify which group of fields to select as the winner in the **Rank groups by** dropdown. The same merge policy is used for all the fields that make up the group.

   - **Importance**: Identifies the winner group by looking at the groups in order starting with Group 1. If all fields are null, the next group is considered. Importance is the default value.
   - **Most recent**: Identifies the winner group by referencing a field in the group you select to indicate recency. The field can be a date, time, or numeric as long as it can be ranked largest to smallest.
   - **Least recent**: Identifies the winner group by referencing a field in the group you select to indicate recency. The field can be a date, time, or numeric as long as it can be ranked smallest to largest.

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

Define how to generate customer ID values, the unique customer profile identifiers. The unify fields step in the data unification process generates the unique customer profile identifier. The identifier is the *CustomerId* in the *Customer* table that results from the data unification process.

The *CustomerId* is based on a hash of the first value of the non-null winner primary keys. These keys come from the tables used in data unification and are influenced by the match order. So the generated customer ID can change when a primary key value changes in the primary table of the match order. The primary key value might not always represent the same customer.

Configuring a stable customer ID enables you to avoid that behavior.

1. Select the **Keys** tab.

1. Hover on the **CustomerId** row and select **Configure**.
   :::image type="content" source="media/customize-stable-id.png" alt-text="Control to customize the ID generation.":::

1. Select up to five fields that will comprise a unique customer ID and are more stable. Records that don’t match your configuration use a system-configured ID instead.  

1. Select **Done**.

## Group profiles into households or clusters

For individual customers, you can define rules to group related profiles into a cluster. There are currently two types of clusters available – household and custom clusters. The system automatically chooses a household with predefined rules if the *Customer* table contains the semantic fields *Person.LastName* and *Location.Address*. You can also create a cluster with your own rules and conditions, similar to [match rules](data-unification-match-tables.md#define-rules-for-match-pairs).

1. Select **Advanced** > **Create cluster**.

   :::image type="content" source="media/create-cluster.png" alt-text="Control to create a new cluster.":::

1. Choose between a **Household** or a **Custom** cluster. If the semantic fields *Person.LastName* and *Location.Address* exist in the *Customer* table, household is automatically selected.

1. Provide a name for the cluster and select **Done**.

1. Select the **Clusters** tab to find the cluster you created.

1. Specify the rules and conditions to define your cluster.

1. Select **Done**. The cluster is created when the unification process is complete. The cluster identifiers are added as new fields to the *Customer* table.

> [!div class="nextstepaction"]
> [Next step: Review unification](data-unification-review.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
