---
title: "Review data unification"
description: "Review the data unification steps, create unified customer profiles, and review the results"
ms.date: 11/27/2024
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Review data unification

Review the summary of changes, create the unified profile, and review the results.

## Review and create customer profiles

This last step in the unification process shows a summary of the steps in the process and provides a chance to make changes before you create the unified profile.

[!INCLUDE [m3-first-run-note](includes/m3-first-run-note.md)]

:::image type="content" source="media/m3_review.png" alt-text="Screenshot of Review and create customer profiles.":::

1. Select **Edit** on any of the data unification steps to review and make any changes.

1. If you're satisfied with your selections, select **Create customer profiles**. The **Unify** page displays while the unified customer profile is being created.

   :::image type="content" source="media/m3_unify_refreshing.png" alt-text="Screenshot of Unify page with tiles showing Queued or Refreshing.":::

   [!INCLUDE [progress-details-pane-include](includes/progress-details-pane.md)]

The unification algorithm takes some time to complete and you can't change the configuration until it completes.

## View the results of data unification

After unification, the **Data** > **Unify** page shows the number of unified customer profiles. The results of each step in the unification process display on each tile. For example, **Customer data** shows the number of mapped columns and **Deduplication rules** shows the number of duplicate records found.

:::image type="content" source="media/m3_unified.png" alt-text="Screenshot of the Data Unify page after data is unified.":::

> [!TIP]
> The **Matching rules** tile displays only if multiple tables were selected.

We recommend you review the results, particularly the quality of your [match rules](data-unification-update.md#manage-match-rules) and refine them if necessary.

When needed, [make changes to the unification settings](data-unification-update.md) and rerun the unified profile.

> [!IMPORTANT]
> If data unification is not behaving as expected, please validate the results using this [troubleshooting guide](/troubleshoot/dynamics-365/customer-insights/data/profile-unification/troubleshoot-unification-results).

## Next steps

Configure [activities](activities.md), [enrichments](enrichment-manage.md), [relationships](relationships.md), or [measures](measures.md) to gain more insights about your customers.

[!INCLUDE[footer-include](includes/footer-banner.md)]
