---
title: "Review data unification"
description: "Review the data unification steps, create unified customer profiles, and review the results"
ms.date: 05/04/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: v-wendysmith
ms.author: adkuppa
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-match
  - ci-merge
  - ci-relationships
  - customerInsights
---

# Review data unification

This last step in the unification process shows a summary of the steps in the process and provides a chance to make changes before you create the unified profile.

:::image type="content" source="media/m3_review.png" alt-text="Screenshot of Review and create customer profiles.":::

## Review the data unification steps

1. Select **Edit** on any of the data unification steps to review and make any changes.

1. If you are satisfied with your selections, select **Create customer profiles** (or **Create account profiles** for B-to-B). The **Unify** page displays while the unified customer profile is being created. The unification algorithm takes some time to complete and you can't change the configuration until it completes.

   [!INCLUDE [m3-task-details-include](includes/m3-task-details.md)]

When the unification process completes, the unified customer profile entity, called *Customers*, displays on the **Entities** page in the **Profiles** section. The first successful unification run creates the unified *Customer* entity. All subsequent runs expand that entity.

## Review the results of data unification

After unification, the **Data** > **Unify** page shows the number of unified customer profiles. The results of each step in the unification process displays on each tile. For example, **Source fields** shows the number of mapped attributes (fields) and **Duplicate records** shows the number of duplicate records found.

:::image type="content" source="media/m3_unified.png" alt-text="Screenshot of the Data Unify page after data is unified.":::

> [!TIP]
> The **Matching conditions** tile displays only if multiple entities were selected.

We recommend you review the results, particularly the quality of your [match rules](data-unification-update.md#manage-match-rules) and refine them if necessary.

When needed, [make changes to the unification settings](data-unification-update.md) and rerun the unified profile.

## Next Step

For B-to-B, perform [contact unification](data-unification-contacts.md).

For B-to-C, configure [activities](activities.md), [enrichment](enrichment-hub.md), or [relationships](relationships.md) to gain more insights about your customers.

[!INCLUDE[footer-include](includes/footer-banner.md)]
