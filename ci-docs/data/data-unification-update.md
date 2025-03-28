---
title: "Update customer, account, or contact unification settings"
description: "Update duplicate rules, match rules, or unified fields in the customer or account unification settings."
ms.date: 03/28/2025
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Update unification settings

To review or change any unification settings once a unified profile has been created, perform the following steps.

1. Go to **Data** > **Unify**.

   The **Unify** page displays the number of unified customer profiles and tiles for each of the unification steps.

   :::image type="content" source="media/m3_unified.png" alt-text="Screenshot of the Data Unify page after data is unified." lightbox="media/m3_unified.png":::

1. Choose what you want to update:
   - [Customer data](#edit-customer-data) to add columns or tables or change column types. To remove a column, see [Remove a unified field](#remove-a-unified-field). To remove a table, see [Remove a unified table](#remove-a-unified-table).
   - [Deduplication rules](#manage-deduplication-rules) to manage deduplication rules or merge preferences.
   - [Matching rules](#manage-match-rules) to update matching rules across two or more tables.
   - [Unified data view](#manage-unified-fields) to combine or exclude fields. You can also group related profiles into clusters.

   > [!TIP]
   > The **Matching rules** tile displays only if multiple tables were selected.

1. After making your changes, choose your next option:

   - [Run matching conditions only](#run-matching-conditions) to quickly evaluate the quality of your deduplication and match rules without updating the unified profile. The **Run matching conditions only** option doesn't display for a single table.
   - [Unify customer profiles](#run-updates-to-the-unified-profile) to run deduplication and match rules and update the unified profile table without impacting dependencies (such as enrichments, segments, or measures). Dependent processes aren't run, but will be refreshed as [defined in the refresh schedule](schedule-refresh.md).
   - [Unify customer profiles and dependencies](#run-updates-to-the-unified-profile) to run deduplication and match rules, update the unified profile table, and update all dependencies (such as enrichments, segments, or measures). All processes are rerun automatically.

## Edit customer data

1. Select **Edit** on the **Customer data** tile.

   :::image type="content" source="media/m3_source_edit.png" alt-text="Screenshot of Customer data page showing number of primary keys, mapped and unmapped fields":::

   The number of mapped and unmapped fields display.

1. To add other columns or tables, select **Select tables and columns**.

1. Optionally, you can change the primary key for a table or the column types. For more information, see [Describe customer data](data-unification-map-tables.md).

1. Select **Next** to make changes to deduplication rules, or select **Save and close** and return to [Update unification settings](#update-unification-settings).

### Remove a unified field

To remove a field that has been unified, the field must be removed from any dependencies such as segments, measures, enrichments, or relationships.

1. Once all dependencies for the field have been removed, go to **Data** > **Unify**.

1. Select **Edit** on the **Unified data view** tile.

1. Select all occurrences of the field and then select **Exclude**.

   :::image type="content" source="media/m3_remove_attribute1.png" alt-text="Screenshot of Unified fields page showing selected fields and Exclude button":::

1. Select **Done** to confirm and then select **Save and close**.

   > [!TIP]
   > If you see the message "Couldn't save unify. The specified resource cannot be modified or deleted due to downstream dependencies", then the field is still used in a downstream dependency.

1. If the field is used in a rule for deduplication rules or matching rules, perform the following steps. Otherwise, go to the next step.
   1. Select **Edit** on the **Deduplication rules** tile.
   1. Remove the field from all rules it's used in, if any, and then select **Next**.
   1. On the **Matching rules** page, remove the field from all rules it's used in, if any, and then select **Save and close**.
   1. Select **Unify** > **Unify customer profiles and dependencies**. Wait for unification to complete before going to the next step.

1. Select **Edit** on the **Customer data** tile.

1. Select **Select tables and columns** and clear the checkbox next to each occurrence of the field.

   :::image type="content" source="media/m3_remove_attribute2.png" alt-text="Screenshot of Select tables and columns dialog box showing cleared checkboxes":::

1. Select **Apply**.

1. Select **Save and close**.

1. Select **Unify** > **Unify customer profiles and dependencies** to update the unified profile.

### Remove a unified table

To remove a table that has been unified, the table must be removed from any dependencies such as segments, measures, enrichments, or relationships.

1. Once all dependencies for the table have been removed, go to **Data** > **Unify**.

1. Select **Edit** on the **Unified data view** tile.

1. Expand the columns and select all fields for the table. Then select **Exclude**.

   :::image type="content" source="media/m3_remove_table1.png" alt-text="Screenshot of Unified fields with all fields for a table selected and Exclude button":::

1. Select **Done** to confirm and then select **Save and close**.

   > [!TIP]
   > If you see the message "Couldn't save unify. The specified resource cannot be modified or deleted due to downstream dependencies", then the table is still used in a downstream dependency.

1. Select **Edit** on the **Deduplication rules** tile.

1. Remove all rules from the table, if any, and then select **Next**.

1. On the **Matching rules** page, select the table and then select **Delete**.

   :::image type="content" source="media/m3_remove_table2.png" alt-text="Screenshot of Matching rules with table selected and Delete button":::

1. Select **Save and close**.

1. Select **Edit** on the **Customer data** tile.

1. Select **Select tables and columns** and clear the checkbox next to the table.

   :::image type="content" source="media/m3_remove_table3.png" alt-text="Screenshot of Select tables and columns dialog box with table checkbox cleared":::

1. Select **Apply**.

1. Select **Save and close**.

1. Run unification by selecting **Unify** > **Unify customer profiles and dependencies** to update the unified profile.

## Manage deduplication rules

1. Select **Edit** on the **Deduplication rules** tile.

   :::image type="content" source="media/m3_duplicates_edit.png" alt-text="Screenshot of Deduplication rules page showing number of duplicated records" lightbox="media/m3_duplicates_edit.png":::

   The number of duplicate records found displays under **Duplicates**. The **Records deduplicated** column shows which tables had duplicate records and the percentage of duplicated records.

1. To use an enriched table, select **Use enriched tables**. For more information, see [Enrichment for data sources](data-sources-enrichment.md).

1. To manage deduplication rules, choose any of the following options:
   - **Create a new rule**: Select **Add rule** under the appropriate table. For more information, see [Define deduplication rules](data-unification-duplicates.md#define-deduplication-rules).
   - **Change rule conditions**: Select the rule and then **Edit**. Change fields, add or remove conditions, or add or remove exceptions.
   - **Preview**: Select the rule and then **Preview** to view the last run results for this rule.
   - **Deactivate a rule**: Select the rule and then **Deactivate** to retain a deduplication rule while excluding it from the matching process.
   - **Duplicate a rule**: Select the rule and then **Duplicate** to create a similar rule with modifications.
   - **Delete a rule**: Select the rule and then **Delete**.

1. To change merge preferences, select the table. You can only change the preferences if a rule is created.
   1. Select **Edit merge preferences** and change the **Record to keep** option.
   1. To change merge preferences on individual columns of a table, select **Advanced** and make the necessary changes.

   1. Select **Done**.

1. Select **Next** to make changes to matching conditions, or select **Save and close** and return to [Update unification settings](#update-unification-settings).

## Manage match rules

You can reconfigure and fine-tune most of the match parameters. You can't add or delete tables. Match rules don't apply to a single table.

1. Select **Edit** on the **Matching rules** tile.

   :::image type="content" source="media/m3_match_edit.png" alt-text="Screenshot of the Match rules and conditions page with statistics." lightbox="media/m3_match_edit.png":::

   The page displays the match order and defined rules and the following statistics:
   - **Unique source records** show the number of individual source records that were processed in last match run.
   - **Matched and non-matched records** highlight how many unique records remain after processing the match rules.
   - **Matched records only** show the number of matches across all of your match pairs.

1. To view the results of all rules and their scores, select **View last run**. The results display, including the alternate contact IDs. You can download the results.

1. To view the results and scores of a particular rule, select the rule and then **Preview**. The results display. You can download the results.

1. To view the results of a particular condition on a rule, select the rule and then **Edit**. On the Edit pane, select **Preview** under the condition. You can download the results.

   :::image type="content" source="media/m3_match_condition_preview.png" alt-text="Graphical representation of unmatched and matched records including a list of the data.":::

1. If you added an enriched table, select **Use enriched tables**. For more information, see [Enrichment for data sources](data-sources-enrichment.md).

1. To manage rules, choose any of the following options:
   - **Create a new rule**: Select **Add rule** under the appropriate table. For more information, see [Define rules for match pairs](data-unification-match-tables.md#define-rules-for-match-pairs).
   - **Change the order of your rules** if you defined multiple rules: Drag and drop the rules into the order you want. For more information, see [Specify the match order](data-unification-match-tables.md#specify-the-match-order).
   - **Change rule conditions**: Select the rule and then **Edit**. Change fields, add or remove conditions, or add or remove exceptions.
   - **Deactivate a rule**: Select the rule and then **Deactivate** to retain a match rule while excluding it from the matching process.
   - **Duplicate a rule**: Select the rule and then **Duplicate** to create a similar rule with modifications.
   - **Delete a rule**: Select the rule and then **Delete**.

1. Select **Next** to [make changes to unified fields](#manage-unified-fields), or select **Save and close** and return to [Update unification settings](#update-unification-settings).

## Manage unified fields

1. Select **Edit** on the **Unified data view** tile.

    :::image type="content" source="media/m3_merge_edit.png" alt-text="Screenshot of Unified data view":::

1. Review the combined and excluded fields, and make any changes as needed. Add or edit the CustomerID key or group profiles into clusters. For more information, see [Unify customer fields](data-unification-merge-tables.md).

1. Select **Next** to review and [update the unified profile and dependencies](#run-updates-to-the-unified-profile). Or select **Save and close** and return to [Update unification settings](#update-unification-settings) to make more changes.

## Run matching conditions

Run matching conditions runs deduplication and match rules only and updates the *Deduplication_** and *ConflationMatchPair* tables.

1. From the **Data** > **Unify** page, select **Run matching conditions only**.

   The **Deduplication rules** and **Matching rules** tiles show **Queued** or **Refreshing** status.

   [!INCLUDE [progress-details-pane-include](includes/progress-details-pane.md)]

1. When the matching process completes, select **Edit** on the **Matching rules** tile.

   :::image type="content" source="media/match-KPIs.png" alt-text="Cropped screenshot of the key metrics on the Match page with numbers and details.":::

1. To make changes, see [Manage deduplication rules](#manage-deduplication-rules) or [Manage match rules](#manage-match-rules).

1. Run the match process again or [run updates to the profile](#run-updates-to-the-unified-profile).

## Run updates to the unified profile

- To run matching conditions and update the unified profile table *without* impacting dependencies (such as customer cards, enrichments, segments, or measures), select **Unify customer profiles**. Dependent processes aren't run, but will be refreshed as [defined in the refresh schedule](schedule-refresh.md).
- To run matching conditions, update the unified profile, and run all dependencies, select **Unify customer profiles and dependencies**. All processes are rerun automatically.

All tiles except **Customer data** show **Queued** or **Refreshing**. More data, skewed data, or data with lots of duplicates impact processing time.

[!INCLUDE [progress-details-pane-include](includes/progress-details-pane.md)]

The results of a successful run display on the **Unify** page showing the number of unified profiles.
