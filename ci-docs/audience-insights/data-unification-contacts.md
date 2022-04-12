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

For business accounts (B-to-B), this process maps contact data from your data sources, removes duplicates, matches the data across accounts, sets up semantic mapping, and then creates a unified contact profile.

## Select source fields for contact unification

Select the entities and primary keys for your contact data sources. See [Select source fields](map-entities.md) for more information.

## Remove duplicates before unifying contacts

Define deduplication rules for your selected entities. See [Remove duplicates](remove-duplicates.md).

## Match conditions

Define the match order and rules for cross-entity matching. See [Match conditions](match-entities.md).

## Unify contact fields

Merge your contact fields. See [Unify customer fields](merge-entities.md).

## Connect your contacts to accounts

### Define the semantic fields for unified contacts

This step in the unification process enables you to map your unified contact fields to semantic types. Semantic mappings let you map your non-activity data to pre-defined schemas. These schemas help Customer Insights to better understand your data attributes.

Select the unified field that maps to the semantic type.

### Set the relationship between contacts and accounts

This step in the unification process connects your contact data to its corresponding account data.

Configure the details to connect your contact data to its corresponding account data. This step visualizes the connection between entities.

1. Select **New Relationship**. The Add relationship path pane displays.

   1. Choose the attribute from your source entity that connects your contact entity to another entity.

   1. Choose the account entity.

   1. Provide a **Relationship name**. If a relationship between your entities already exists, the relationship name is read-only. If no relationship exists, a new relationship will be created with the name you provide.

## Review the contact unification steps

Select **Edit** on any of the contact unification steps to review and make any changes before creating the unified contact profile.

If you are satisfied with your selections, select **Create contact profiles**. The **Unify** page displays while the unified contact profile is being created. The unification algorithm takes some time to complete and you can't change the configuration until it completes.

[!INCLUDE [m3-task-details-include](../includes/m3-task-details.md)]

The unified contact profile entity, called **ContactsCustomer**, displays on the **Entities** page in the **Profiles** section. The first successful unification run creates the unified *Contacts* entity. All subsequent runs expand that entity.

## Next Step

Configure [activities](activities.md), [enrichment](enrichment-hub.md), or [relationships](relationships.md) to gain more insights about your customers.
