---
title: Monitor system performance - Dynamics 365 Customer Insights
description: "Monitor system performance with the Performance dashboard to track refresh health, duration trends, and per-stage breakdowns. Optimize your Customer Insights - Data environment."
ms.date: 04/23/2026
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: alfergus
ms.service: customer-insights
ms.subservice: customer-insights-data
ms.custom: bap-template
---

# Monitor system performance

Monitor system performance using the **Performance** page, which provides a centralized view of your Customer Insights - Data environment's refresh health. Use it to quickly assess the overall system status, identify slow or failing pipeline stages, and review refresh history over time.

To open the Performance page, select **Performance** in the left navigation pane.

The page header shows the time, outcome, and total duration of the most recent refresh.
For example: *Last refresh: 4/23, 02:15 AM — Successful (44m 40s)*.

## Overall health summary

The **Overall health** indicator at the top of the page summarizes the outcome of all tasks in the most recent refresh. It shows counts for each status category.

For definitions of each status value, see [Status definitions](system.md#status-definitions).

## Stage pills

Below the health summary, a row of stage pills shows the task count and cumulative duration for each pipeline stage in the most recent refresh:

- Data sources
- Unification
- Enrichments
- Segments
- Measures
- Models
- Sync to Dataverse
- Export destinations

Select a stage pill to filter the task list on the **Overview** tab to that stage only.

## Overview tab

The **Overview** tab is the default view and contains two panels.

:::image type="content" source="media/performance-overview.png" alt-text="Screenshot of the Performance page Overview tab showing overall health, stage pills, stage summary cards, and the task list.":::

### Stage summary cards

Each pipeline stage has a card that shows:

- Stage name and overall status
- Count of tasks broken down by status (for example, *2 Successful, 1 Completed with warnings*)
- A proportional progress bar
- Total duration for the stage

Select a card to open the detail view for that stage.

### Task list

The task list shows all tasks across all stages for the most recent refresh.

**To filter the task list:**

- Select a status filter button (Successful, Skipped, Completed with warnings, Refreshing, Queued, Completed with errors, or Failed) to show only tasks with that status.
- Type in the **Task** search box to filter by task name.

The list includes the following columns:

| Column | Description |
|---|---|
| **Task** | Task name and pipeline stage in parentheses |
| **Status** | Outcome of the most recent run. See [Status definitions](system.md#status-definitions). |
| **Duration** | How long the task took to complete |
| **Last updated** | Date and time the task last ran |

Select a task row to view its detail, including logs and error information.

## Timeline tab

The **Timeline** tab shows a **Refresh duration trend** - a historical log of completed
system refreshes.

:::image type="content" source="media/performance-timeline.png" alt-text="Screenshot of the Performance page Timeline tab showing the refresh history table and an expanded Gantt-style timeline for the most recent refresh.":::

**To change the time window**, select **3 days**, **7 days**, or **30 days**.

Each row represents one full system refresh and includes:

| Column | Description |
|---|---|
| **Time range** | Start and end time of the refresh |
| **Status** | Overall outcome (for example, Successful, Canceled) |
| **Duration** | Total elapsed time |
| **Scope** | The deepest pipeline stage that ran (for example, Merge, Match, Data sources) |
| **Mode** | Incremental or Full |
| **Change** | Percentage change in duration compared to the previous refresh of the same scope |
| **Changes** | Details of tasks that were added or removed from this refresh |

Rows marked with a diamond icon indicate a **configuration change** - one or more tasks were added or removed in that refresh.

**To view a per-stage Gantt timeline for a specific refresh:**
Select a row to expand an inline timeline that shows each pipeline stage running in parallel, with the individual task results within each stage.

## Breakdown by stage tab

The **Breakdown by stage** tab shows the same historical refresh list as the **Timeline** tab, and adds a proportional time breakdown chart for each refresh.

:::image type="content" source="media/performance-breakdown-by-stage.png" alt-text="Screenshot of the Performance page Breakdown by stage tab showing the stage filter pills, the refresh history table, and an expanded time breakdown bar chart for the most recent refresh.":::

**To filter by pipeline stage**, select one of the stage pills at the top of the tab: Data sources, Unification, Segments, Measures, or Sync to Dataverse.

Each expanded refresh row shows a bar chart of how the total duration was distributed across stages (for example, *unification: 29m 7s, dataverseHydration: 10s*). Use this view to identify which stage is the bottleneck in a given refresh.

## Actions you can take from the Performance page

| Action | How |
|---|---|
| View task detail and logs | Select a task row on the **Overview** tab |
| Filter tasks by status | Select a status filter button on the **Overview** tab |
| Filter tasks by stage | Select a stage pill in the stage pill row |
| Search for a specific task | Type in the **Task** search box on the **Overview** tab |
| View refresh history | Select the **Timeline** or **Breakdown by stage** tab |
| Change the history time window | Select **3 days**, **7 days**, or **30 days** on the Timeline or Breakdown by stage tab |
| View per-refresh stage breakdown | Select a row on the **Timeline** or **Breakdown by stage** tab |
| Cancel a running refresh | Select the **Refreshing** status on a task, then select **Cancel job** |

## Related information

- [View system configuration](system.md) — includes status definitions and the refresh process dependency table
- [Schedule system refresh](schedule-refresh.md)
- [Manage data sources](data-sources-manage.md)
- [Data unification overview](data-unification.md)
- [Work with segments](segments.md)
- [Create and manage measures](measures.md)
- [Export destinations overview](export-destinations.md)