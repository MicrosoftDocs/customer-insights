---
title: "Update customer, account, or contact unification settings"
description: "Update duplicate rules, match rules, or unified fields in the customer or account unification settings."
ms.date: 05/23/2022

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

# Update unification settings

To review or change any unification settings once a unified profile has been created, perform the following steps.

1. Go to **Data** > **Unify**.

   For individual customers (B-to-C), the following image displays.

   :::image type="content" source="media/m3_unified.png" alt-text="Screenshot of the Data Unify page after data is unified." lightbox="media/m3_unified.png":::

   > [!TIP]
   > The **Matching conditions** tile displays only if multiple entities were selected.

   For business accounts (B-to-B), the Unify page displays unified accounts and unified contacts. Choose the appropriate tile under **Unify Accounts** or **Unify Contacts** depending on what you want to update.

   :::image type="content" source="media/b2b_unified.png" alt-text="Screenshot of the Data Unify page after account and contact data is unified." lightbox="media/b2b_unified.png":::

1. Choose what you want to update:
   - [Source fields](#edit-source-fields) to add entities or attributes or change attribute types.
   - [Duplicate records](#manage-deduplication-rules) to manage deduplication rules or merge preferences.
   - [Matching conditions](#manage-match-rules) to update matching rules across two or more entities.
   - [Unified customer fields](#manage-unified-fields) to combine or exclude fields. You can also group related profiles into clusters.
   - [Semantic fields](#manage-semantic-fields-for-unified-contacts) to manage semantic types for unified contact fields.
   - [Relationships](#manage-contact-and-account-relationships) to manage the contact to account relationship.

1. After making your changes, choose your next option:

   - To evaluate the quality of your unification rules (deduplication and matching rules) without updating the unified profile, see [Run matching conditions](#run-matching-conditions). The **Run matching conditions only** option doesn't display for single entity.
   - To update the unified profile (with or without dependencies), see [Run updates to the unified profile](#run-updates-to-the-unified-profile).

## Edit source fields

You can't remove an attribute or an entity if they've already been unified.

1. Select **Edit** on the **Source fields** tile.

   :::image type="content" source="media/m3_source_edit.png" alt-text="Screenshot of Source fields page showing number of primary keys, mapped and unmapped fields":::

   The number of mapped and unmapped fields display.

1. To add other attributes or entities, select **Select entities and fields**.

1. Optionally, you can change the primary key for an entity, the attribute types, and toggle **Intelligent mapping** on or off. For more information, see [Select source fields](map-entities.md).

1. Select **Next** to make changes to deduplication rules, or select **Save and close** and return to [Update unification settings](#update-unification-settings).

## Manage deduplication rules

1. Select **Edit** on the **Duplicate records** tile.

   :::image type="content" source="media/m3_duplicates_edit.png" alt-text="Screenshot of Duplicate records page showing number of duplicated records" lightbox="media/m3_duplicates_edit.png":::

   The number of duplicate records found displays under **Duplicates**. The **Records deduplicated** column shows which entities had duplicate records and the percentage of duplicated records.

1. To use an enriched entity, select **Use enriched entities**. For more information, see [Enrichment for data sources](data-sources-enrichment.md).

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

   1. Select **Done**.

1. Select **Next** to make changes to matching conditions, or select **Save and close** and return to [Update unification settings](#update-unification-settings).

## Manage match rules

You can reconfigure and fine-tune most of the match parameters. You can't add or delete entities. Match rules don't apply to a single entity.

1. Select **Edit** on the **Matching conditions** tile.

   :::image type="content" source="media/m3_match_edit.png" alt-text="Screenshot of the Match rules and conditions page with statistics." lightbox="media/m3_match_edit.png":::

   The page displays the match order and defined rules and the following statistics:
   - **Unique source records** show the number of individual source records that were processed in last match run.
   - **Matched and non-matched records** highlight how many unique records remain after processing the match rules.
   - **Matched records only** show the number of matches across all of your match pairs.

1. To view the results of all rules and their scores, select **View last run**. The results display, including the alternate contact IDs. You can download the results.

1. To view the results and scores of a particular rule, select the rule and then **Preview**. The results display. You can download the results.

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

1. Select **Next** to make changes to unified fields, or select **Save and close** and return to [Update unification settings](#update-unification-settings).

## Manage unified fields

1. Select **Edit** on the **Unified customer fields** tile.

    :::image type="content" source="media/m3_merge_edit.png" alt-text="Screenshot of Unified customer fields":::

1. Review the combined and excluded fields, and make any changes as needed. Add or edit the CustomerID key or group profiles into clusters. For more information, see [Unify customer fields](merge-entities.md).

1. For customers or accounts, select **Next** to review and [update the unified profile and dependencies](#run-updates-to-the-unified-profile). Or select **Save and close** and return to [Update unification settings](#update-unification-settings) to make more changes.
 
   For contacts, select **Next** to manage semantic fields. Or select **Save and close** and return to [Update unification settings](#update-unification-settings) to make more changes.

## Manage semantic fields for unified contacts

1. Select **Edit** on the **Semantic fields** tile.

1. To change the semantic type for a unified field, select a new type. For more information, see [Define the semantic fields for unified contacts](data-unification-contacts.md#define-the-semantic-fields-for-unified-contacts).

1. Select **Next** to manage the account and contact relationship, or select **Save and close** and return to [Update unification settings](#update-unification-settings) to make more changes.

## Manage contact and account relationships

1. Select **Edit** on the **Relationships** tile.

1. To change the contact and account relationship, change any of the following information:

   - **Foreign key from contact entity**: Choose the attribute that connects your contact entity to the account.
   - **To account entity**: Choose the account entity associated with the contact.

1. Select **Next** to review the unification settings and [update the unified profile and dependencies](#run-updates-to-the-unified-profile), or select **Save and close** and return to [Update unification settings](#update-unification-settings) to make more changes.

## Run matching conditions

Run matching conditions to test unification rules without updating the unified profile entity.

1. From the **Data** > **Unify** page, select **Run matching conditions only**. For accounts, select **Unify accounts** > **Run matching conditions only**. For contacts, select **Unify contacts** > **Run matching conditions only**.

   The **Duplicate records** and **Matching conditions** tiles show **Queued** or **Refreshing**.

   [!INCLUDE [m3-task-details-include](includes/m3-task-details.md)]

1. When the matching process completes, select **Edit** on the **Matching conditions** tile.

   :::image type="content" source="media/match-KPIs.png" alt-text="Cropped screenshot of the key metrics on the Match page with numbers and details.":::

1. To make changes, see [Manage deduplication rules](#manage-deduplication-rules) or [Manage match rules](#manage-match-rules).

1. Run the match process again or [run updates to the profile](#run-updates-to-the-unified-profile).

## Run updates to the unified profile

To run matching conditions and update the unified profile entity without impacting dependencies (such as customer cards, enrichments, segments, or measures), select **Unify customer profiles**. For accounts, select **Unify accounts** > **Unify profiles**. For contacts, select **Unify contacts** > **Unify profiles**.Dependent processes aren't run, but will be refreshed as [defined in the refresh schedule](system.md#schedule-tab).

To run matching conditions, update the unified profile, and run all dependencies, select **Unify customer profiles and dependencies**. All processes are rerun automatically.

> [!TIP]
> For accounts, select **Unify accounts** > **Unify profiles and dependencies**. For contacts, select **Unify contacts** > **Unify profiles and dependencies**. When unifying accounts, contact unification will run if contact data or configuration changes have been saved but not yet run. The same is true when unifying contacts, account unification will run if account data or configuration changed have been saved but not yet run.

All tiles except **Source fields** show **Queued** or **Refreshing**.

[!INCLUDE [m3-task-details-include](includes/m3-task-details.md)]
