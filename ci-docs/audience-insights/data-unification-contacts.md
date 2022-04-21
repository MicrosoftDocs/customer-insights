---
title: "Create a unified view of your business contacts"
description: "Go through the data unification process to create a single master dataset of contacts."
ms.date: 04/12/2022
ms.reviewer: v-wendysmith

ms.subservice: audience-insights
ms.topic: overview
author: v-wendysmith
ms.author: mukeshpo
manager: shellyha

searchScope: 
  - ci-map
  - customerInsights
---

# Create a unified view of your business contacts

For business accounts (B-to-B), after [unifying the accounts](map-entities.md), unify the contacts. The contact unification process maps contact data from your data sources, removes duplicates, matches the data across accounts, sets up semantic mapping, creates relationships between contacts and accounts, and then creates a unified contact profile.

## Select source fields for contact unification

1. Under **Unify contacts**, select **Get started**.

1. Select the entities and fields for your contact data sources. See [Select source fields](map-entities.md) for more information.

1. Select **Next**.

## Remove duplicates before unifying contacts

1. Define deduplication rules for your selected entities (optional). See [Remove duplicates](remove-duplicates.md) for more information.

1. Select **Next**.

## Match conditions

1. Define the match order and rules for cross-entity matching. See [Match conditions](match-entities.md) for more information.

1. Select **Next**.

## Unify contact fields

1. Combine and exclude contact fields. See [Unify customer fields](merge-entities.md) for more information.

1. Select **Next**.

## Define the semantic fields for unified contacts

This step in the unification process enables you to map your unified contact fields to semantic types. Semantic mappings let you map your non-activity data to pre-defined schemas. These schemas help Customer Insights to better understand your data attributes.

1. Select the semantic type that maps to the unified field. Select **None** if a semantic type is not available.

   :::image type="content" source="media/semantic_mapping.png" alt-text="Screenshot of Semantic fields page to define the semantic types.":::

1. Select **Next**.

## Set the relationship between contacts and accounts

This step in the unification process connects your contact data to its corresponding account data.

1. Select the contact entity and enter the following information:

   - **To account entity**: Choose the account entity associated with the contact.
   - **Foreign key**: Choose the attribute that connects your contact entity to the account.

   :::image type="content" source="media/contact_relationship.png" alt-text="Screenshot of Relationship page to connect the contact and account entities.":::

1. Select **Next**.

## Review the contact unification steps

This last step in the unification process shows a summary of the steps in the process and provides a chance to make changes before you create the unified contact profile.

1. Select **Edit** on any of the contact unification steps to review and make any changes.

1. If you are satisfied with your selections, select **Create contact profiles**. The **Unify** page displays while the unified contact profile is being created. The unification algorithm takes some time to complete and you can't change the configuration until it completes.

   [!INCLUDE [m3-task-details-include](../includes/m3-task-details.md)]

When the unification process completes, the unified contact profile entity, called **ContactsCustomer**, displays on the **Entities** page in the **Profiles** section. The first successful unification run creates the unified *Contacts* entity. All subsequent runs expand that entity.

To make changes to the unified contact profile entity, see

## Next Step

Configure [activities](activities.md), [enrichment](enrichment-hub.md), or [relationships](relationships.md) to gain more insights about your customers.
