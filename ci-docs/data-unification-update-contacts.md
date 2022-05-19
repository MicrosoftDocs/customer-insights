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
   - [Source fields](data-unification-update.md#edit-source-fields) to add entities or attributes or change attribute types.
   - [Duplicate records](data-unification-update.md#manage-deduplication-rules) to manage deduplication rules or merge preferences.
   - [Matching conditions](data-unification-update.md#manage-match-rules) to update matching rules across two or more entities.
   - [Unified customer fields](data-unification-update.md#manage-unified-fields) to combine or exclude fields.
   - Semantic mapping to add semantic types to unified fields.
   - Relationships to add a relationship for a new entity.

1. After making your changes, choose your next option:

   :::image type="content" source="media/b2b_run_match_merge.png" alt-text="Screenshot of the Data Unify page with the Unify contacts option open.":::

   - To update the unified contact profile (with or without dependencies), see [Run updates to the contact profile](#run-updates-to-the-unified-contact-profile).
   - To evaluate the quality of your matching conditions, see [Run matching conditions](#run-matching-conditions).


## Run matching conditions

1. From the **Data** > **Unify** page, select **Unify contacts** > **Run matching conditions only**.

   The **Duplicate records** and **Matching conditions** tiles show **Queued** or **Refreshing**.

   [!INCLUDE [m3-task-details-include](includes/m3-task-details.md)]

1. When the matching process completes, select **Edit** on the **Matching conditions** tile.

   :::image type="content" source="media/contact_match_KPIs.png" alt-text="Cropped screenshot of the key metrics on the Match page with numbers and details.":::

1. To make changes, see [Manage deduplication rules](data-unification-update.md#manage-deduplication-rules) or [Manage match rules](data-unification-update.md#manage-match-rules).

1. Run the match process again or [run updates to the contact profile](#run-updates-to-the-unified-contact-profile).

## Run updates to the unified contact profile

To update the unified contact profile entity without impacting dependencies (such as enrichments, segments, or measures), select **Unify contacts** > **Unify profiles**. Dependent processes are not run, but will be refreshed as [defined in the refresh schedule](system.md#schedule-tab).

To update the unified profile and all dependencies, select **Unify contacts** > **Unify profiles and dependencies**. All processes are rerun automatically. After all downstream processes have completed, the contact profiles reflect any changes you made.

[!INCLUDE [m3-task-details-include](includes/m3-task-details.md)]
