---
title: "Update the unified customer profile"
description: "Update duplicate rules, match rules, or unified fields in the unified customer profile."
ms.date: 03/28/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: v-wendysmith
ms.author: v-wendysmith
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-match
  - ci-merge
  - ci-relationships
  - customerInsights
---

# Update the unified customer profile

1. Go to **Data** > **Unify**.

1. Choose the area you want to update by selecting **Edit** on one of the following:
   - [Source fields](#edit-source-fields)
   - [Duplicate records](#manage-deduplication-rules)
   - [Matching conditions](#manage-match-rules)
   - [Unified customer fields](merge-entities.md)

1. To evaluate the quality of your matching conditions, [run the match process](#run-the-match-process).

1. To merge your changes, [run the merge process](#run-the-merge-process) or **Run all** to run both match and merge processes.

## Edit source fields

You can't remove an attribute or an entity if they've already been unified.

1. Select **Edit entities and fields** to add other attributes or entities. Use the search or scroll to find and select your attributes and entities of interest. Select **Apply**.

1. Change the primary key for an entity, if applicable.

1. Change the attribute type, if applicable.

1. Toggle **Intelligent mapping** on or off, if applicable.

1. Select **Save and close**.

1. Return to [Update the unified customer profile](#update-the-unified-customer-profile) to make additional changes.

## Manage deduplication rules

You can reconfigure and fine-tune most of the deduplication parameters.

1. To change merge preferences, select the entity.
   1. Select **Edit merge preferences** and change the record to keep option.
   1. To change merge preferences on individual attributes of an entity, select **Advanced** and make the necessary changes.
   1. Select **Done**.

1. To manage rules, choose any of the following:

   - **Create a new rule**: Select **Add rule** under the appropriate entity.
   - **Change rule conditions**: Select **Edit** on the rule and choose different fields.
   - **Deactivate a rule**: Select **Deactivate** on the rule to retain a deduplication rule while excluding it from the matching process.
   - **Duplicate a rule**: Select **Duplicate** on the rule to create a similar rule with modifications.
   - **Delete a rule**: Select **Delete** on the rule.

1. Select **Done**.

1. Click **Save and close**.

1. Return to [Update the unified customer profile](#update-the-unified-customer-profile) to make additional changes.

## Manage match rules

You can reconfigure and fine-tune most of the match parameters.

:::image type="content" source="media/match-rules-management.png" alt-text="Screenshot of the dropdown menu with match rule options.":::

- **Change the order of your rules** if you defined multiple rules: Select the **Move Up** and **Move Down** options or drag and drop.
- **Change rule conditions**: Select **Edit** on the rule and choose different fields.
- **Deactivate a rule**: Select **Deactivate** on the rule to retain a match rule while excluding it from the matching process.
- **Duplicate a rule**: Select **Duplicate** on the rule to create a similar rule with modifications..
- **Delete a rule**: Select **Delete** on the rule.

Return to [Update the unified customer profile](#update-the-unified-customer-profile) to make additional changes.

## Run the match process

From the **Data** > **Unify** page, select **Run Match**.

:::image type="content" source="media/m3_run_match_merge.png" alt-text="Cropped screenshot of the Run merge selection.":::

The **Duplicate records** and **Matching conditions** tiles show **Queued** or **Refreshing**.

[!INCLUDE [m3-task-details-include](../includes/m3-task-details.md)]

The **Duplicate records** and **Matching conditions** tiles show the last time a match was run.

### Review and validate your matches

When the matching process completes, select **Edit** on the **Matching conditions** tile.

The tiles on top of the page show key metrics, summarizing the number of matched records and duplicates.

:::image type="content" source="media/match-KPIs.png" alt-text="Cropped screenshot of the key metrics on the Match page with numbers and details.":::

- **Unique source records** shows the number of individual source records that were processed in last match run.
- **Matched and non-matched records** highlights how many unique records remain after processing the match rules.
- **Matched records only** shows the number of matches across all of your match pairs.

You can assess the results of each match pair and its rules under **Records matched**. Compare the number of records that came from a match pair against the percentage of successfully matched records.

To make changes, see [Manage deduplication rules](#manage-deduplication-rules) or [Manage match rules](#manage-match-rules).

Run the match process again or proceed to run your merge.

## Run the merge process

Whether you manually merge attributes or let the system merge them, you can always run your merge from the **Unify** page.

:::image type="content" source="media/m3_run_match_merge.png" alt-text="Cropped screenshot of the Run merge selection.":::

Choose **Run only Merge** if you only want to see the output reflected in the unified customer entity. Downstream processes will be refreshed as [defined in the refresh schedule](system.md#schedule-tab).

Choose **Run Merge and downstream processes** to refresh the system with your changes. All processes, including enrichment, segments, and measures will rerun automatically. After all downstream processes have completed, the customer profiles reflect any changes you made.

[!INCLUDE [m3-task-details-include](../includes/m3-task-details.md)]
