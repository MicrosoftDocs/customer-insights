---
title: "Create a unified view of your business contacts"
description: "Go through the data unification process to create a single master dataset of contacts."
recommendations: false
ms.date: 06/02/2022
ms.reviewer: v-wendysmith

ms.subservice: audience-insights
ms.topic: overview
author: mukeshpo
ms.author: mukeshpo
manager: shellyha

searchScope: 
  - ci-map
  - ci-match
  - ci-merge
  - customerInsights
---

# Create a unified business contact profile

After [unifying business accounts](map-entities.md), unify the contacts. The contact unification process maps contact data from your data sources, removes duplicates, matches the data across entities, sets up semantic mapping, creates relationships between contacts and accounts, and then creates a unified contact profile.

The following steps and images reflect the first time you go through the contact unification process. To edit existing contact unification settings, see [Update the unification settings](data-unification-update.md).

The first few steps are identical to the unifying accounts steps.

## Initial contact unification steps

1. Under **Unify contacts**, select **Get started**.

1. [Select the entities and fields](map-entities.md) for your contact data sources, including the primary keys and attribute types.

1. Select **Next**.

1. Optionally, [define deduplication rules](remove-duplicates.md) for your selected entities.

1. Select **Next**.

1. [Define the match order and rules](match-entities.md) for cross-entity matching.

1. Select **Next**.

1. [Combine and exclude contact fields](merge-entities.md).

1. Select **Next**.

## Define the semantic fields for unified contacts

This step in the unification process maps your unified contact fields to semantic types. Semantic mapping lets you map your non-activity data to pre-defined schemas. These schemas help Customer Insights to better understand your data attributes. You can map your [contact activity](activities.md#define-a-contact-activity) data to the schemas.

1. Select the semantic type that maps to each unified field. Select **None** if a semantic type is not available.

   :::image type="content" source="media/semantic_mapping.png" alt-text="Screenshot of Semantic fields page to define the semantic types." lightbox="media/semantic_mapping.png":::

1. After mapping all unified fields, select **Next**.

## Set the relationship between contacts and accounts

This step in the unification process connects your contact data to its corresponding account data.

1. For each entity, enter the following information:

   - **Foreign key from contact entity**: Choose the attribute that connects your contact entity to the account.
   - **To account entity**: Choose the account entity associated with the contact.

   :::image type="content" source="media/contact_relationship.png" alt-text="Screenshot of Relationship page to connect the contact and account entities.":::

1. Select **Next**.

## Review contact unification

This last step in the unification process shows a summary of the steps in the process and provides a chance to make changes before you create the unified contact profile.

:::image type="content" source="media/b2b_review_contacts.png" alt-text="Screenshot of Review and create contact profiles.":::

### Review the contact unification steps

1. Select **Edit** on any of the contact unification steps to review and make any changes.

1. If you are satisfied with your selections, select **Create contact profiles**. The **Unify** page displays while the unified contact profile is being created.
  
   :::image type="content" source="media/b2b_unify_refreshing.png" alt-text="Screenshot of Unify Contacts page with tiles showing Queued or Refreshing.":::

   [!INCLUDE [progress-details-pane-include](includes/progress-details-pane.md)]

The unification algorithm takes some time to complete and you can't change the configuration until it completes.

### Review the results of contact unification

After unification, the **Data** > **Unify** page shows the number of unified contact profiles. The results of each step in the unification process displays on each tile. For example, **Source fields** shows the number of mapped attributes (fields) and **Duplicate records** shows the number of duplicate records found.

> [!TIP]
> The **Matching conditions** tile displays only if multiple entities were selected.

We recommend you review the results, particularly the quality of your [match rules](data-unification-update.md#manage-match-rules) and refine them if necessary.

When needed, [make changes to the contact unification settings](data-unification-update.md) and rerun the unified profile.

### Output entities from data unification

When the unification process completes, the unified contact profile entity, called *ContactProfile*, displays on the **Entities** page in the **Semantic entities** section. The first successful unification run creates the unified *ContactProfile* entity. All subsequent runs expand that entity.

Deduplication and conflation entities are created and display in the **System** section in the **Entities** page. A deduplicated entity for each of the source entities is created with the name **Deduplication_DataSource_Entity**. The **ContactsConflationMatchPairs** entity contains information about cross-entity matches.

A deduplication output entity contains the following information:
- IDs / Keys
  - Primary key and Alternate ID fields. Alternate ID field consists of all the alternate IDs identified for a record.
  - Deduplication_GroupId field shows the group or cluster identified within an entity that groups all the similar records based on the specified deduplication fields. It's used for system processing purposes. If there are no manual deduplication rules specified and system defined deduplication rules apply, you may not find this field in the deduplication output entity.
  - Deduplication_WinnerId: This field contains the winner ID from the identified groups or clusters. If the Deduplication_WinnerId is same as the Primary key value for a record, it means that the record is the winner record.
- Fields used to define the deduplication rules.
- Rule and Score fields to denote which of the deduplication rules got applied and the score returned by the matching algorithm.

A **ContactsCustomer** entity is created and is used for internal processing.

## Next Step

Configure [activities](activities.md), [enrichment](enrichment-hub.md), [relationships](relationships.md), or [measures](measures.md) to gain more insights about your customers.
