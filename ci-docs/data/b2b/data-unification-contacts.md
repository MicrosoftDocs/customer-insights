---
title: "Create a unified business contact profile"
description: "Learn how to use the data unification process to create a profile of your business contacts that combines data from multiple sources."
ms.date: 11/28/2023
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Create a unified business contact profile



Contact unification allows contacts for unified accounts to be separately unified and associated with the accounts. Contact unification also allows contacts without an account to be included in the unified contact profile.

The contact unification process maps contact data from multiple sources, removes duplicates, matches the data across tables, creates relationships between contacts and accounts, and then creates a unified contact profile. The system supports a one-to-many account to contact relationship. The account relationship for contacts is optional, allowing you to work with commercial contacts where the account is unknown.

[!INCLUDE [m3-first-run-note](../includes/m3-first-run-note.md)]

The first few steps to unify contacts are the same as the steps to [unify accounts](data-unification-b2b.md).

> [!TIP]
> The terms *field* and *column* are used interchangeably in this article to refer to data in a table row, or record.

## Prerequisites

- Accounts with contacts must have a unique key (called a foreign key) that connects them. For example, an account ID that exists in the account record and contact record that ties the account and contact together. Contacts without accounts have a null value for the foreign key.
- At least one contact table must have a relationship defined to an account table. If none of your contact tables have a relationship to an account, add a blank column in one of the contact tables and map it to an account table.

## Describe customer data

1. Sign in to Dynamics 365 Customer Insights - Data.

1. In the left side panel under **Data**, select **Unify**.

1. Under **Unify contacts**, select **Get started**.

1. [Select the tables and columns](../data-unification-map-tables.md) for your contact data sources, including the primary keys and attribute types.

1. Select **Next**.

## Remove duplicate records

1. Optionally, [define deduplication rules](../data-unification-duplicates.md) for your selected tables.

1. Select **Next**.

## Match conditions

1. [Define the match order and rules](../data-unification-match-tables.md) for cross-table matching.

1. Select **Next**.

## Set the relationship between contacts and accounts

This step in the unification process connects your contact data to its corresponding account data. At least one contact table must have a relationship to an account table.

1. For each table, select **Yes** or **No** for **Add contact to account relationship?**.

   - If the table contains one or more contacts with known accounts, select **Yes**.

   - If the table doesn't contain any contact to account relationships, meaning all the contacts are orphans, select **No**. Select **Next** and go to [Unify contact fields](#unify-contact-fields).

1. If you selected **Yes** to **Add contact to account relationship?**, enter the following information:

   - **Foreign key from contact table**: Choose the attribute that connects your contact table to the account.
   - **To account table**: Choose the account table that's associated with the contact.

   :::image type="content" source="media/b2b-contact-relationship.svg" alt-text="Screenshot of Relationship page to connect the contact and account tables.":::

1. Select **Next**.

## Unify contact fields

1. [Combine and exclude contact columns](../data-unification-merge-tables.md).

1. Select **Next**.

## Review contact unification

Review the summary of changes, create the unified profile, and review the results.

### Review and create contact profiles

This last step in the unification process shows a summary of the steps in the process and provides a chance to make changes before you create the unified contact profile.

:::image type="content" source="media/b2b_review_contacts.svg" alt-text="Screenshot of Review and create contact profiles.":::

1. Select **Edit** on any of the contact unification steps to review and make any changes.

1. If you are satisfied with your selections, select **Create contact profiles**. The **Unify** page displays while the unified contact profile is being created. If the message "Object reference not set to an instance of an object" appears, there are references to columns that were deleted or renamed before saving the conflation plans. Update the tables and rerun contact unification.
  
   :::image type="content" source="media/b2b_unify_refreshing.svg" alt-text="Screenshot of Unify Contacts page with tiles showing Queued or Refreshing.":::

   [!INCLUDE [progress-details-pane-include](../includes/progress-details-pane.md)]

The unification algorithm takes some time to complete and you can't change the configuration until it completes.

### View the results of contact unification

After unification completes, the **Data** > **Unify** page shows the number of unified contact profiles. The result of each step in the unification process displays on each tile. For example, **Customer data** shows the number of mapped attributes, or columns, and **Deduplication rules** shows the number of duplicate records that were found. The **Matching rules** tile displays only if multiple tables were selected.

:::image type="content" source="media/b2b-unified-contacts.svg" alt-text="Screenshot of the Data Unify page after contacts are unified.":::

We recommend that you review the results, particularly the quality of your [match rules](../data-unification-update.md#manage-match-rules) and refine them if necessary. If needed, [make changes to the contact unification settings](../data-unification-update.md) and rerun the unified profile.

### Verify output tables from data unification

Go to **Data** > **Tables** to verify the output tables.

The unified contact profile table, called *UnifiedContact*, appears in the **Profiles** section. The first successful unification run creates the table. All subsequent runs expand it.

Key columns in the *UnifiedContact* table include:

- **UnifiedContactId**: Uniquely identifies the unified profile. Assigned by the system.

- **FK_ContactToAccountId**: The primary key from a data source, this value is used to look up he unified account’s unique CustomerID. It's the winner value that results from merging the account foreign keys for the contact.

- **FK_CustomerId**: Uniquely identifies the contact’s unified accounts. This value is a foreign key reference to the 'Customer' table’s 'CustomerID' column. If it's null, the contact doesn't have an account.

- **{ContactSourceTable1}{PrimaryKeyColumn}**: This value is the primary key of the winner source record from the named table that's involved in the unification of the profile.

- **{ContactSourceTable1}{PrimaryKeyColumn}_Alternate**: This value is a semicolon-separated list of all source records from the named table involved in unification of the profile.

Deduplication and conflation tables are created and appear in the **System** section. A deduplicated table for each of the source tables is created with the name **Deduplication_DataSource_Tablename**. The **ContactsConflationMatchPairs** table contains information about cross-table matches.

A deduplication output table contains the following information:
- IDs / Keys

  - Primary key and Alternate ID columns, which consist of all the alternate IDs identified for a record.

  - Deduplication_GroupId column shows the group or cluster that's identified in a table and groups similar records based on the specified deduplication columns. It's used for system processing purposes. If there are no manual deduplication rules specified and system defined deduplication rules apply, you may not find this field in the deduplication output table.

  - Deduplication_WinnerId column contains the winner ID from the identified groups or clusters. If the Deduplication_WinnerId is same as the primary key value for a record, it means that the record is the winner record.

- Columns that are used to define the deduplication rules.

- Rule and Score columns that denote which of the deduplication rules got applied and the score that's returned by the matching algorithm.

## Next step

Configure [activities](activities-contacts.md), [enrichment](supported-features-b2b.md#enrichments), and [relationships](../relationships.md) to gain more insights about your contacts.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
