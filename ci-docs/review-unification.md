---
title: "Review data unification"
description: "Review the data unification steps, create unified customer profiles, and review the results"
ms.date: 11/15/2022

ms.topic: tutorial
author: v-wendysmith
ms.author: adkuppa
ms.reviewer: v-wendysmith
searchScope: 
  - ci-match
  - ci-merge
  - ci-relationships
  - customerInsights
---

# Review data unification

Review the summary of changes, create the unified profile, and review the results.

## Review and create customer profiles

This last step in the unification process shows a summary of the steps in the process and provides a chance to make changes before you create the unified profile.

[!INCLUDE [m3-first-run-note](includes/m3-first-run-note.md)]

:::image type="content" source="media/m3_review.png" alt-text="Screenshot of Review and create customer profiles.":::

1. Select **Edit** on any of the data unification steps to review and make any changes.

1. If you are satisfied with your selections, select **Create customer profiles** (or **Create account profiles** for B-to-B). The **Unify** page displays while the unified customer profile is being created.

   :::image type="content" source="media/m3_unify_refreshing.png" alt-text="Screenshot of Unify page with tiles showing Queued or Refreshing.":::

   [!INCLUDE [progress-details-pane-include](includes/progress-details-pane.md)]

The unification algorithm takes some time to complete and you can't change the configuration until it completes.

## View the results of data unification

After unification, the **Data** > **Unify** page shows the number of unified customer profiles (or account profiles for B-to-B). The results of each step in the unification process display on each tile. For example, **Source fields** shows the number of mapped attributes (fields) and **Duplicate records** shows the number of duplicate records found.

:::image type="content" source="media/m3_unified.png" alt-text="Screenshot of the Data Unify page after data is unified.":::

> [!TIP]
> The **Matching conditions** tile displays only if multiple tables were selected.

We recommend you review the results, particularly the quality of your [match rules](data-unification-update.md#manage-match-rules) and refine them if necessary.

When needed, [make changes to the unification settings](data-unification-update.md) and rerun the unified profile.

### Verify output tables from data unification

Go to **Data** > **Tables** to verify the output tables.

The unified customer profile table, called *Customer*, displays in the **Profiles** section. The first successful unification run creates the unified *Customer* table. All subsequent runs expand that table.

Deduplication and conflation tables are created and display in the **System** section. A deduplicated table for each of the source tables is created with the name **Deduplication_DataSource_Table**. The **ConflationMatchPairs** table contains information about cross-table matches.

A deduplication output table contains the following information:
- IDs / Keys
  - Primary key and Alternate ID fields. Alternate ID field consists of all the alternate IDs identified for a record.
  - Deduplication_GroupId field shows the group or cluster identified within a table that groups all the similar records based on the specified deduplication fields. It's used for system processing purposes. If there are no manual deduplication rules specified and system defined deduplication rules apply, you may not find this field in the deduplication output table.
  - Deduplication_WinnerId: This field contains the winner ID from the identified groups or clusters. If the Deduplication_WinnerId is same as the Primary key value for a record, it means that the record is the winner record.
- Fields used to define the deduplication rules.
- Rule and Score fields to denote which of the deduplication rules got applied and the score returned by the matching algorithm.

## Next Step

- For B-to-B, optionally perform [contact unification](data-unification-contacts.md).

- For B-to-C, configure [activities](activities.md), [enrichments](enrichment-hub.md), [relationships](relationships.md), or [measures](measures.md) to gain more insights about your customers.

[!INCLUDE[footer-include](includes/footer-banner.md)]
