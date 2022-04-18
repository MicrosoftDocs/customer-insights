---
title: "Update the unified customer profile"
description: "Update duplicate rules, match rules, or unified fields in the unified customer profile."
ms.date: 04/18/2022

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

# Update the unified customer profile

1. Go to **Data** > **Unify**. Each tile shows the number of fields or records found during the last unification run. For example, **Source fields** shows the number of entity attributes (fields) defined and **Duplicate records** shows the number of duplicate records found.

   :::image type="content" source="media/m3_unified.png" alt-text="Screenshot of the Data Unify page after data is unified.":::

1. Choose what you want to update:
   - [Source fields](#edit-source-fields) to add entities or attributes or change attribute types.
   - [Duplicate records](#manage-deduplication-rules) to manage deduplication rules or merge preferences.
   - [Matching conditions](#manage-match-rules) to update matching rules.
   - [Unified customer fields](#manage-unified-fields) to combine or exclude fields.

1. After making your changes, choose your next option:

   :::image type="content" source="media/m3_run_match_merge.png" alt-text="Screenshot of the Data Unify page with the Unify options highlighted.":::

   - To unify the customer profile (with or without dependencies), see [Unify the customer profile](#unify-the-customer-profile).
   - To evaluate the quality of your matching conditions, see [Run matching conditions](#run-matching-conditions).

## Edit source fields

You can't remove an attribute or an entity if they've already been unified.

1. Select **Edit** on the **Source fields** tile.

   :::image type="content" source="media/m3_source_edit.png" alt-text="Screenshot of Source fields page showing number of primary keys, mapped and unmapped fields":::

   The number of primary keys and mapped and unmapped fields display on the top right of the page.

1. Select **Edit entities and fields** to add other attributes or entities. Use the search or scroll to find and select your attributes and entities of interest. Select **Apply**.

1. Optionally, you can change the primary key for an entity, the attribute types, and toggle **Intelligent mapping** on or off.

1. Select **Save and close**.

1. Return to [Update the unified customer profile](#update-the-unified-customer-profile) to make additional changes.

## Manage deduplication rules

1. Select **Edit** on the **Duplicate records** tile.

   :::image type="content" source="media/m3_duplicates_edit.png" alt-text="Screenshot of Duplicate records page showing number of duplicated records":::

   The number of duplicate records found displays in the top right of the page. The **Records deduplicated** column shows which entities had duplicate records.

1. To change merge preferences, select the entity.
   1. Select **Edit merge preferences** and change the **Record to keep** option.
   1. To change merge preferences on individual attributes of an entity, select **Advanced** and make the necessary changes.

      :::image type="content" source="media/m3_adv_merge.png" alt-text="Screenshot of advanced merge preferences showing most recent email and most complete address":::

   1. Select **Done**.

1. To manage rules, choose any of the following:
   - **Create a new rule**: Select **Add rule** under the appropriate entity.
   - **Change rule conditions**: Select **Show more (...)** > **Edit** on the rule and choose different fields.
   - **Deactivate a rule**: Select **Show more (...)** > **Deactivate** on the rule to retain a deduplication rule while excluding it from the matching process.
   - **Duplicate a rule**: Select **Show more (...)** > **Duplicate** on the rule to create a similar rule with modifications.
   - **Delete a rule**: Select **Show more (...)** > **Delete** on the rule.

1. To view the last run results, select **Show more (...)** > **Match Preview**. If no duplicate records were found in the last run, Match preview does not display.

1. Click **Save and close**.

1. Return to [Update the unified customer profile](#update-the-unified-customer-profile) to make additional changes.

## Manage match rules

You can reconfigure and fine-tune most of the match parameters. You cannot add or delete entities.

1. Select **Edit** on the **Matching conditions** tile.

   :::image type="content" source="media/match-rules-management.png" alt-text="Screenshot of the dropdown menu with match rule options.":::

   The page displays the match order and defined rules as well as the following statistics:
   - **Unique source records** shows the number of individual source records that were processed in last match run.
   - **Matched and non-matched records** highlights how many unique records remain after processing the match rules.
   - **Matched records only** shows the number of matches across all of your match pairs.

1. To review the results of the match rule pairs, select **Show more** > **Match preview** on a rule. The results displays. You can also download the results.

1. To manage rules, choose any of the following:
   - **Change the order of your rules** if you defined multiple rules: Drag and drop the rules into the order you want.
   - **Change rule conditions**: Select **Show more** > **Edit** on the rule and choose different fields.
   - **Deactivate a rule**: Select **Show more** > **Deactivate** on the rule to retain a match rule while excluding it from the matching process.
   - **Duplicate a rule**: Select **Show more** > **Duplicate** on the rule to create a similar rule with modifications.
   - **Delete a rule**: Select **Show more** > **Delete** on the rule.

1. Return to [Update the unified customer profile](#update-the-unified-customer-profile) to make additional changes.

## Manage unified fields

1. Select **Edit** on the **Unified customer fields** tile.

1. Review the combined and excluded fields. Make any changes as needed. See [Unify customer fields](merge-entities.md) for more information.

1. Click **Save and close**.

1. Return to [Update the unified customer profile](#update-the-unified-customer-profile) to make additional changes.

## Run matching conditions

1. From the **Data** > **Unify** page, select **Run matching conditions only**.

   The **Duplicate records** and **Matching conditions** tiles show **Queued** or **Refreshing**.

   [!INCLUDE [m3-task-details-include](../includes/m3-task-details.md)]

1. When the matching process completes, select **Edit** on the **Matching conditions** tile.

   :::image type="content" source="media/match-KPIs.png" alt-text="Cropped screenshot of the key metrics on the Match page with numbers and details.":::

1. To make changes, see [Manage deduplication rules](#manage-deduplication-rules) or [Manage match rules](#manage-match-rules).

1. Run the match process again or [update the customer profile](#update-the-customer-profile).

## Update the customer profile

To update the unified customer profile entity without impacting dependencies (such as enrichments, segments, or measures), select **Unify customer profiles**. Dependent processes are not run, but will be refreshed as [defined in the refresh schedule](system.md#schedule-tab).

To update the unified profile and all dependencies, select **Unify customer profiles and dependencies**. All processes are rerun automatically. After all downstream processes have completed, the customer profiles reflect any changes you made.

[!INCLUDE [m3-task-details-include](../includes/m3-task-details.md)]
