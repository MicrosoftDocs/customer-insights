---
title: "Update the unified customer profile"
description: "Update duplicate rules, match rules, or unified fields in the unified customer profile."
ms.date: 03/23/2022

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

# Update a unified customer profile

## Edit source fields

You can't remove an attribute or an entity if they've already been unified.

1. Go to **Data** > **Unify**.

1. Select **Edit** on the **Source fields** tile.

1. Optionally, toggle **Intelligent mapping** on or off.

1. Select **Edit fields**.

1. In the **Edit fields** pane, add or remove attributes and entities. Use the search or scroll to find and select your attributes and entities of interest.

1. Select **Apply**.

1. Select **Save and close**.

## Manage deduplication rules

You can reconfigure and fine-tune most of the deduplication parameters.

1. Go to **Data** > **Unify**.

1. Select **Edit** on the **Duplicate records** tile.

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

## Manage match rules

You can reconfigure and fine-tune most of the match parameters.

:::image type="content" source="media/match-rules-management.png" alt-text="Screenshot of the dropdown menu with match rule options.":::

- **Change the order of your rules** if you defined multiple rules. You can reorder the match rules by selecting the **Move Up** and **Move Down** options or by drag and drop.

- **Change rule conditions** by selecting **Edit** and choose different fields.

- **Deactivate a rule** to retain a match rule while excluding it from the matching process.

- **Duplicate your rules** if you've defined a match rule and would like to create a similar rule with modifications, select **Duplicate**.

- **Delete a rule** by selecting the **Delete** symbol.

## Preview and validate your matches

The tiles on top of the page show key metrics, summarizing the number of matched records and duplicates.

:::image type="content" source="media/match-KPIs.png" alt-text="Cropped screenshot of the key metrics on the Match page with numbers and details.":::

- **Unique source records** shows the number of individual source records that were processed in last match run.
- **Matched and non-matched records** highlights how many unique records remain after processing the match rules.
- **Matched records only** shows the number of matches across all of your match pairs.

You can assess the results of each match pair and its rules in the **Matched records details** table. Compare the number of records that came from a match pair against the percentage of successfully matched records.

## Run your merge

Whether you manually merge attributes or let the system merge them, you can always run your merge. Select **Run** on the **Unified fields** page to start the process.

> [!div class="mx-imgBorder"]
> ![Data merge Save and Run.](media/configure-data-merge-save-run.png "Data merge Save and Run")

Choose **Run only Merge** if you only want to see the output reflected in the unified customer entity. Downstream processes will be refreshed as [defined in the refresh schedule](system.md#schedule-tab).

Choose **Run Merge and downstream processes** to refresh the system with your changes. All processes, including enrichment, segments, and measures will rerun automatically. After all downstream processes have completed, the customer profiles reflect any changes you made.

To make more changes and rerun the step, you can cancel an in-progress merge. Select **Refreshing ...** and select **Cancel job**  in the side pane that appears.

[!INCLUDE [progress-details-include](../includes/progress-details-pane.md)]

:::image type="content" source="media/process-detail-path.png" alt-text="Drill-down path to get to process details from the task status link.":::
