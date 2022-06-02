---
title: "Update the unification settings"
description: "Update duplicate rules, match rules, or unified fields in the unification settings."
ms.date: 06/01/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: v-wendysmith
ms.author: mukeshpo
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-match
  - ci-merge
  - ci-relationships
  - customerInsights
---

# Update the unification settings

[!INCLUDE [m3-prod-trial-note](includes/m3-prod-trial-note.md)]

To review or change any unification settings once a unified profile has been created, perform the following steps.

1. Go to **Data** > **Unify**.

   :::image type="content" source="media/m3_unified.png" alt-text="Screenshot of the Data Unify page after data is unified.":::

   > [!TIP]
   > The **Matching conditions** tile displays only if multiple entities were selected.

1. Choose what you want to update:
   - [Source fields](#edit-source-fields) to add entities or attributes or change attribute types.
   - [Duplicate records](#manage-deduplication-rules) to manage deduplication rules or merge preferences.
   - [Matching conditions](#manage-match-rules) to update matching rules across two or more entities.
   - [Unified customer fields](#manage-unified-fields) to combine or exclude fields. You can also group related profiles into clusters.

1. After making your changes, choose your next option:

   :::image type="content" source="media/m3_run_match_merge.png" alt-text="Screenshot of the Data Unify page with the Unify options highlighted.":::

   - To evaluate the quality of your matching conditions (deduplication and match rules) without updating the unified profile, see [Run matching conditions](#run-matching-conditions). The **Run matching conditions only** option doesn't display for single entity.
   - To update the unified customer profile (with or without dependencies), see [Run updates to the customer profile](#run-updates-to-the-unified-customer-profile).

## Edit source fields

You can't remove an attribute or an entity if they've already been unified.

1. Select **Edit** on the **Source fields** tile.

   :::image type="content" source="media/m3_source_edit.png" alt-text="Screenshot of Source fields page showing number of primary keys, mapped and unmapped fields":::

   The number of mapped and unmapped fields display.

1. Select **Select entities and fields** to add other attributes or entities. Use the search or scroll to find and select your attributes and entities of interest. Select **Apply**.

1. Optionally, you can change the primary key for an entity, the attribute types, and toggle **Intelligent mapping** on or off. For more information, see [Select primary key and semantic type for attributes](map-entities.md#select-primary-key-and-semantic-type-for-attributes).

1. Select **Next** to make changes to deduplication rules, or select **Save and close** and return to [Update the unification settings](#update-the-unification-settings).

## Manage deduplication rules

1. Select **Edit** on the **Duplicate records** tile.

   :::image type="content" source="media/m3_duplicates_edit.png" alt-text="Screenshot of Duplicate records page showing number of duplicated records" lightbox="media/m3_duplicates_edit.png":::

   The number of duplicate records found displays under **Duplicates**. The **Records deduplicated** column shows which entities had duplicate records and the percentage of duplicated records.

1. If you added an enriched entity, select **Use enriched entities**. For more information, see [Enrichment for data sources](data-sources-enrichment.md).

1. To manage deduplication rules, choose any of the following options:
   - **Create a new rule**: Select **Add rule** under the appropriate entity. For more information, see [Define deduplication rules](remove-duplicates.md#define-deduplication-rules).
   - **Change rule conditions**: Select the rule and then **Edit**. Change fields, add or remove conditions, or add or remove exceptions.
   - **Preview**: Select the rule and then **Preview** to view the last run results for this rule.
   - **Deactivate a rule**: Select the rule and then **Deactivate** to retain a deduplication rule while excluding it from the matching process.
   - **Duplicate a rule**: Select the rule and then **Duplicate** to create a similar rule with modifications.
   - **Delete a rule**: Select the rule and then **Delete**.

1. To change merge preferences, select the entity. You can only change the preferences if a rule is created.
   1. Select **Edit merge preferences** and change the **Record to keep** option.
   1. To change merge preferences on individual attributes of an entity, select **Advanced** and make the necessary changes.

      :::image type="content" source="media/m3_adv_merge.png" alt-text="Screenshot of advanced merge preferences showing most recent email and most complete address":::

   1. Select **Done**.

1. Select **Next** to make changes to matching conditions, or select **Save and close** and return to [Update the unification settings](#update-the-unification-settings).

## Manage match rules

You can reconfigure and fine-tune most of the match parameters. You can't add or delete entities. Match rules don't apply to a single entity.

1. Select **Edit** on the **Matching conditions** tile.

   :::image type="content" source="media/m3_match_edit.png" alt-text="Screenshot of the Match rules and conditions page with statistics." lightbox="media/m3_match_edit.png":::

   The page displays the match order and defined rules and the following statistics:
   - **Unique source records** shows the number of individual source records that were processed in last match run.
   - **Matched and non-matched records** highlights how many unique records remain after processing the match rules.
   - **Matched records only** shows the number of matches across all of your match pairs.

1. To view the results of all rules and their scores, select **View last run**. The results displays, including the alternate contact IDs. You can download the results.

1. To view the results and scores of a particular rule, select the rule and then **Preview**. The results displays. You can download the results.

1. To view the results of a particular condition on a rule, select the rule and then **Edit**. On the Edit pane, select **Preview** under the condition. You can download the results.

   :::image type="content" source="media/m3_match_condition_preview.png" alt-text="Graphical representation of unmatched and matched records including a list of the data.":::

1. If you added an enriched entity, select **Use enriched entities**. For more information, see [Enrichment for data sources](data-sources-enrichment.md).

1. To manage rules, choose any of the following options:
   - **Create a new rule**: Select **Add rule** under the appropriate entity. For more information, see [Define rules for match pairs](match-entities.md#define-rules-for-match-pairs).
   - **Change the order of your rules** if you defined multiple rules: Drag and drop the rules into the order you want. For more information, see [Specify the match order](match-entities.md#specify-the-match-order).
   - **Change rule conditions**: Select the rule and then **Edit**. Change fields, add or remove conditions, or add or remove exceptions.
   - **Deactivate a rule**: Select the rule and then **Deactivate** to retain a match rule while excluding it from the matching process.
   - **Duplicate a rule**: Select the rule and then **Duplicate** to create a similar rule with modifications.
   - **Delete a rule**: Select the rule and then **Delete**.

1. Select **Next** to make changes to unified fields, or select **Save and close** and return to [Update the unification settings](#update-the-unification-settings).

## Manage unified fields

1. Select **Edit** on the **Unified customer fields** tile.

    :::image type="content" source="media/m3_merge_edit.png" alt-text="Screenshot of Unified customer fields":::

1. Review the combined and excluded fields, and make any changes as needed. Add or edit the CustomerID key or group profiles into clusters. For more information, see [Unify customer fields](merge-entities.md).

1. Select **Next** to review the unification settings and [update the unified profile and dependencies](#run-updates-to-the-unified-customer-profile), or select **Save and close** and return to [Update the unification settings](#update-the-unification-settings) to make more changes.

## Run matching conditions

Run matching conditions runs deduplication and match rules only and updates the Deduplication and ConflationMatchPair entities.

1. From the **Data** > **Unify** page, select **Run matching conditions only**.

   The **Duplicate records** and **Matching conditions** tiles show **Queued** or **Refreshing**.

   [!INCLUDE [m3-task-details-include](includes/m3-task-details.md)]

1. When the matching process completes, select **Edit** on the **Matching conditions** tile.

   :::image type="content" source="media/match-KPIs.png" alt-text="Cropped screenshot of the key metrics on the Match page with numbers and details.":::

1. To make changes, see [Manage deduplication rules](#manage-deduplication-rules) or [Manage match rules](#manage-match-rules).

1. Run the match process again or [run updates to the customer profile](#run-updates-to-the-unified-customer-profile).

## Run updates to the unified customer profile

1. From the **Data** > **Unify** page, select:

   - **Unify customer profiles**: Runs matching conditions and updates the unified customer profile entity without impacting dependencies (such as enrichments, segments, or measures). Dependent processes aren't run, but will be refreshed as [defined in the refresh schedule](system.md#schedule-tab).

   - **Unify customer profiles and dependencies**: Runs matching conditions and updates the unified profile and all dependencies. All processes are rerun automatically. After all downstream processes have completed, the customer profile reflects the updated data.

   The **Duplicate records**, **Matching conditions**, and **Unified customer fields** tiles show **Queued** or **Refreshing**.

   [!INCLUDE [m3-task-details-include](includes/m3-task-details.md)]
