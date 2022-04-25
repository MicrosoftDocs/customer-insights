---
title: "Review data unification"
description: "Review and finalize the data unification steps and create unified customer profiles."
ms.date: 04/22/2022

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

This last step in the unification process shows a summary of the steps in the process and provides a chance to make changes before you create the unified profile.


# [Individual consumers (B-to-C)](#tab/b2c)

:::image type="content" source="media/m3_review.png" alt-text="Screenshot of Review and create customer profiles.":::

1. Select **Edit** on any of the data unification steps to review and make any changes.

1. If you are satisfied with your selections, select **Create customer profiles**. The **Unify** page displays while the unified customer profile is being created. The unification algorithm takes some time to complete and you can't change the configuration until it completes.

   [!INCLUDE [m3-task-details-include](../includes/m3-task-details.md)]

When the unification process completes, the unified customer profile entity, called **Customers**, displays on the **Entities** page in the **Profiles** section. The first successful unification run creates the unified *Customer* entity. All subsequent runs expand that entity.

When needed, [make changes to the unification settings](data-unification-update.md) and rerun the unified profile.

## Next step

Configure [activities](activities.md), [enrichment](enrichment-hub.md), or [relationships](relationships.md) to gain more insights about your customers.
For B-to-B: [Unify contacts](data-unification-contacts.md)

# [Business accounts (B-to-B)](#tab/b2b)

**For accounts**:
   1. Select **Edit** on any of the data unification steps to review and make any changes.

   1. If you are satisfied with your selections, select **Create account profiles**. The **Unify** page displays while the unified customer profile is being created. The unification algorithm takes some time to complete and you can't change the configuration until it completes.

   [!INCLUDE [m3-task-details-include](../includes/m3-task-details.md)]

   When the unification process completes, the unified customer profile entity, called **Customers**, displays on the **Entities** page in the **Profiles** section. The first successful unification run creates the unified *Customer* entity. All subsequent runs expand that entity.

   To make changes to the unified customer profile entity, see [Update the unified customer profile](data-unification-update.md).

**For contacts**:
   1. Select **Edit** on any of the data unification steps to review and make any changes.

   1. If you are satisfied with your selections, select **Create contact profiles**. The **Unify** page displays while the unified contact profile is being created. The unification algorithm takes some time to complete and you can't change the configuration until it completes.

   [!INCLUDE [m3-task-details-include](../includes/m3-task-details.md)]

   When the unification process completes, the unified contact profile entity, called **ContactsCustomer**, displays on the **Entities** page in the **Profiles** section. The first successful unification run creates the unified *ContactsCustomer* entity. All subsequent runs expand that entity.

