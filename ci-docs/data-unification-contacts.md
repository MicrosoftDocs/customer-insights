---
title: "Create a B-to-B unified contact profile (preview)"
description: "Go through the data unification process to create a single master dataset of business contacts."
ms.date: 04/28/2023
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template

searchScope: 
  - ci-map
  - ci-match
  - ci-merge
  - customerInsights
---

# Create a unified B-to-B contact profile (preview)

After [unifying business accounts](data-unification-map-tables.md), you can optionally unify business contacts for those accounts and link the unified contacts to the unified accounts. The contact unification process maps contact data from multiple data sources, removes duplicates, matches the data across tables, creates relationships between contacts and accounts, and then creates a unified contact profile.
An account can have multiple contacts, but a contact is linked to a single account. Contacts without accounts are also included in the contact profile.

[!INCLUDE [m3-first-run-note](includes/m3-first-run-note.md)]

The first few steps are identical to the unifying accounts steps.

## Prerequisites

- Accounts with contacts must have a unique key (called a foreign key) that connects them. For example, an account ID that exists in the account record and contact record that ties the account and contact together. Contacts without accounts have a null value for the foreign key.
- At least one contact table must have a relationship defined to an account table. If none of your contact tables have a relationship to an account, add a blank column in one of the contact tables and map it to an account table.

## Select source fields

1. Under **Unify contacts (preview)**, select **Get started**.

1. [Select the tables and fields](data-unification-map-tables.md) for your contact data sources, including the primary keys and attribute types.

1. Select **Next**.

## Remove duplicate records

1. Optionally, [define deduplication rules](data-unification-duplicates.md) for your selected tables.

1. Select **Next**.

## Match conditions

1. [Define the match order and rules](data-unification-match-tables.md) for cross-table matching.

1. Select **Next**.

## Set the relationship between contacts and accounts

This step in the unification process connects your contact data to its corresponding account data.

1. For each table, enter the following information:

   - **Foreign key from contact table**: Choose the attribute that connects your contact table to the account.
   - **To account table**: Choose the account table associated with the contact.

   :::image type="content" source="media/contact_relationship.svg" alt-text="Screenshot of Relationship page to connect the contact and account tables.":::

1. Select **Next**.

## Unify contact fields

1. [Combine and exclude contact fields](data-unification-merge-tables.md).

1. Select **Next**.

## Review contact unification

Review the summary of changes, create the unified profile, and review the results.

### Review and create contact profiles

This last step in the unification process shows a summary of the steps in the process and provides a chance to make changes before you create the unified contact profile.

:::image type="content" source="media/b2b_review_contacts.svg" alt-text="Screenshot of Review and create contact profiles.":::

1. Select **Edit** on any of the contact unification steps to review and make any changes.

1. If you are satisfied with your selections, select **Create contact profiles**. The **Unify** page displays while the unified contact profile is being created.
  
   :::image type="content" source="media/b2b_unify_refreshing.svg" alt-text="Screenshot of Unify Contacts page with tiles showing Queued or Refreshing.":::

   [!INCLUDE [progress-details-pane-include](includes/progress-details-pane.md)]

The unification algorithm takes some time to complete and you can't change the configuration until it completes.

### View the results of contact unification

After unification completes, the **Data** > **Unify** page shows the number of unified contact profiles. The results of each step in the unification process displays on each tile. For example, **Source fields** shows the number of mapped attributes (fields) and **Duplicate records** shows the number of duplicate records found.

:::image type="content" source="media/unified_contacts.svg" alt-text="Screenshot of the Data Unify page after contacts are unified.":::

> [!TIP]
> The **Matching conditions** tile displays only if multiple tables were selected.

We recommend you review the results, particularly the quality of your [match rules](data-unification-update.md#manage-match-rules) and refine them if necessary.

When needed, [make changes to the contact unification settings](data-unification-update.md) and rerun the unified profile.

### Verify output tables from data unification

Go to **Data** > **Tables** to verify the output tables.

The unified contact profile table, called *UnifiedContact*, displays in the **Profiles** section. The first successful unification run creates the unified *UnifiedContact* table. All subsequent runs expand that table.

Deduplication and conflation tables are created and display in the **System** section. A deduplicated table for each of the source tables is created with the name **Deduplication_DataSource_Tablename**. The **ContactsConflationMatchPairs** table contains information about cross-table matches.

A deduplication output table contains the following information:
- IDs / Keys
  - Primary key and Alternate ID fields. Alternate ID field consists of all the alternate IDs identified for a record.
  - Deduplication_GroupId field shows the group or cluster identified within a table that groups all the similar records based on the specified deduplication fields. It's used for system processing purposes. If there are no manual deduplication rules specified and system defined deduplication rules apply, you may not find this field in the deduplication output table.
  - Deduplication_WinnerId: This field contains the winner ID from the identified groups or clusters. If the Deduplication_WinnerId is same as the Primary key value for a record, it means that the record is the winner record.
- Fields used to define the deduplication rules.
- Rule and Score fields to denote which of the deduplication rules got applied and the score returned by the matching algorithm.

## Next Step

Configure [activities](activities.md), [enrichment](enrichment-hub.md), or [relationships](relationships.md) to gain more insights about your contacts.
