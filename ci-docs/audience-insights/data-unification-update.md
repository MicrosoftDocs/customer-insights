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
