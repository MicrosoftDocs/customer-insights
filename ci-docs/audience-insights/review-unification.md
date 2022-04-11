---
title: "Review data unification"
description: "Review and finalize the data unification steps and create unified customer profiles."
ms.date: 04/11/2022

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

# Review the data unification steps

:::image type="content" source="media/m3_review.png" alt-text="Screenshot of Review and create customer profiles.":::

Select **Edit** on any of the data unification steps to review and make any changes before creating the unified customer or account profile.

If you are satisfied with your selections, select **Create customer profiles**. The **Unify** page displays while the unified customer profile is being created. The unification algorithm takes some time to complete and you can't change the configuration until it completes.

[!INCLUDE [m3-task-details-include](../includes/m3-task-details.md)]

The unified customer profile entity, called **Customers**, displays on the **Entities** page in the **Profiles** section. The first successful unification run creates the unified *Customer* entity. All subsequent runs expand that entity.

To make changes to the unified customer profile entity, see [Update the unified customer profile](data-unification-update.md).

## Next Step

Configure [activities](activities.md), [enrichment](enrichment-hub.md), or [relationships](relationships.md) to gain more insights about your customers.
