---
title: "Update the contact unification settings"
description: "Update duplicate rules, match rules, unified fields, semantic mapping, or relationships in the unified contact profile."
recommendations: false
ms.date: 05/06/2022

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

# Update the contact unification settings

To review or change any unification settings once a unified contact profile has been created, perform the following steps.

1. Go to **Data** > **Unify**. Under **Unify contacts**, the contact unification tiles display.

   :::image type="content" source="media/b2b_unified.png" alt-text="Screenshot of the Data Unify page after account and contact data is unified.":::

   > [!TIP]
   > The **Matching conditions** tile displays only if multiple entities were selected.

1. Choose what you want to update:
   - [Source fields](#edit-source-fields) to add entities or attributes or change attribute types.
   - [Duplicate records](#manage-deduplication-rules) to manage deduplication rules or merge preferences.
   - [Matching conditions](#manage-match-rules) to update matching rules across two or more entities.
   - [Unified customer fields](#manage-unified-fields) to combine or exclude fields.
   - [Semantic mapping](#manage-semantic-mappings) to add semantic types to unified fields.
   - [Relationships](#manage-the-contact-and-account-relationship) to add a relationship for a new entity.

1. After making your changes, choose your next option:

   :::image type="content" source="media/m3_run_match_merge.png" alt-text="Screenshot of the Data Unify page with the Unify contacts option open.":::

   - To update the unified contact profile (with or without dependencies), see [Run updates to the contact profile](#run-updates-to-the-unified-contact-profile).
   - To evaluate the quality of your matching conditions, see [Run matching conditions](#run-matching-conditions).

## Edit source fields

You can't remove an attribute or an entity if they've already been unified.

1. Select **Edit** on the **Source fields** tile.

   :::image type="content" source="media/m3_source_edit.png" alt-text="Screenshot of Source fields page showing number of primary keys, mapped and unmapped fields":::

   The number of mapped and unmapped fields display.

1. Select **Select entities and fields** to add other attributes or entities. Use the search or scroll to find and select your attributes and entities of interest. Select **Apply**.

1. Optionally, you can change the primary key for an entity, the attribute types, and toggle **Intelligent mapping** on or off.

1. Select **Next** to manage deduplication rules, or select **Save and close** and return to [Update the contact unification settings](#update-the-contact-unification-settings).

## Manage deduplication rules

1. Select **Edit** on the **Duplicate records** tile.

   :::image type="content" source="media/m3_duplicates_edit.png" alt-text="Screenshot of Duplicate records page showing number of duplicated records":::

   The number of duplicate records found displays. The **Records deduplicated** column shows which entities had duplicate records.

1. To manage rules, choose any of the following:
   - **Create a new rule**: Select **Add rule** under the appropriate entity.
   - **Change rule conditions**: Select **Show more (...)** > **Edit** on the rule and choose different fields.
   - **Match preview**: Select **Show more (...)** > **Edit** on the rule to view the last run results. If no duplicate records were found in the last run, Match preview does not display.
   - **Deactivate a rule**: Select **Show more (...)** > **Deactivate** on the rule to retain a deduplication rule while excluding it from the matching process.
   - **Duplicate a rule**: Select **Show more (...)** > **Duplicate** on the rule to create a similar rule with modifications.
   - **Delete a rule**: Select **Show more (...)** > **Delete** on the rule.

1. To change merge preferences, select the entity. You can only change the preferences if a rule is created.
   1. Select **Edit merge preferences** and change the **Record to keep** option.
   1. To change merge preferences on individual attributes of an entity, select **Advanced** and make the necessary changes.

      :::image type="content" source="media/m3_adv_merge.png" alt-text="Screenshot of advanced merge preferences showing most recent email and most complete address":::

   1. Select **Done**.

1. Select **Next** to manage matching conditions, or select **Save and close** and return to [Update the contact unification settings](#update-the-contact-unification-settings).

## Manage match rules

You can reconfigure and fine-tune most of the match parameters. You cannot add or delete entities.

1. Select **Edit** on the **Matching conditions** tile.

   :::image type="content" source="media/match-rules-management.png" alt-text="Screenshot of the dropdown menu with match rule options.":::

   The page displays the match order and defined rules as well as the following statistics:
   - **Unique source records** shows the number of individual source records that were processed in last match run.
   - **Matched and non-matched records** highlights how many unique records remain after processing the match rules.
   - **Matched records only** shows the number of matches across all of your match pairs.

1. To view the results of all rules, select **View last run** on a rule. You can also download the results.

1. To manage rules, choose any of the following:
   - **Change the order of your rules** if you defined multiple rules: Drag and drop the rules into the order you want.
   - **Match preview**: Select **Show more (...)** > **Edit** on the rule to view the last run results. If no matching records were found in the last run, Match preview does not display.
   - **Change rule conditions**: Select **Show more** > **Edit** on the rule and choose different fields.
   - **Deactivate a rule**: Select **Show more** > **Deactivate** on the rule to retain a match rule while excluding it from the matching process.
   - **Duplicate a rule**: Select **Show more** > **Duplicate** on the rule to create a similar rule with modifications.
   - **Delete a rule**: Select **Show more** > **Delete** on the rule.

1. Select **Next** to manage unified fields, or select **Save and close** and return to [Update the contact unification settings](#update-the-contact-unification-settings).

## Manage unified fields

1. Select **Edit** on the **Unified customer fields** tile.

    :::image type="content" source="media/m3_merge_edit.png" alt-text="Screenshot of Unified customer fields":::

1. Review the combined and excluded fields, and make any changes as needed. Add or edit the CustomerID key or group profiles into clusters. For more information, see [Unify customer fields](merge-entities.md).

1. Select **Next** to manage semantic mappings, or select **Save and close** and return to [Update the contact unification settings](#update-the-contact-unification-settings).

## Manage semantic mappings

1. Select **Edit** on the **Semantic fields** tile.

1. Change the semantic type of a unified field if needed.

1. Select **Next** to manage relationships, or select **Save and close** and return to [Update the contact unification settings](#update-the-contact-unification-settings).

## Manage the contact and account relationship

1. Select **Edit** on the **Relationships** tile.

1. If a new entity has been added, enter the following information:

   - **Foreign key from contact entity**: Choose the attribute that connects your contact entity to the account.
   - **To account entity**: Choose the account entity associated with the contact.

1. Select **Next** to review the unification settings and [update the unified profile and dependencies](#run-updates-to-the-unified-contact-profile), or select **Save and close** and return to [Update the contact unification settings](#update-the-contact-unification-settings) to make more changes.

## Run matching conditions

1. From the **Data** > **Unify** page, select **Unify contacts** > **Run matching conditions only**.

   The **Duplicate records** and **Matching conditions** tiles show **Queued** or **Refreshing**.

   [!INCLUDE [m3-task-details-include](includes/m3-task-details.md)]

1. When the matching process completes, select **Edit** on the **Matching conditions** tile.

   :::image type="content" source="media/match-KPIs.png" alt-text="Cropped screenshot of the key metrics on the Match page with numbers and details.":::

1. To make changes, see [Manage deduplication rules](#manage-deduplication-rules) or [Manage match rules](#manage-match-rules).

1. Run the match process again or [run updates to the contact profile](#run-updates-to-the-unified-contact-profile).

## Run updates to the unified contact profile

To update the unified contact profile entity without impacting dependencies (such as enrichments, segments, or measures), select **Unify contacts** > **Unify profiles**. Dependent processes are not run, but will be refreshed as [defined in the refresh schedule](system.md#schedule-tab).

To update the unified profile and all dependencies, select **Unify contacts** > **Unify profiles and dependencies**. All processes are rerun automatically. After all downstream processes have completed, the contact profiles reflect any changes you made.

[!INCLUDE [m3-task-details-include](includes/m3-task-details.md)]
