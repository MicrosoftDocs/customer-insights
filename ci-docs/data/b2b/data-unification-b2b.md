---
title: Unify data for business accounts
description: Unify data for business accounts (B2B) to create a single master dataset of account profiles. Learn how to map, deduplicate, match, and merge your data.
ms.date: 07/10/2026
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.update-cycle: 1095-days
ms.custom:
  - bap-template
  - sfi-image-nochange
---

# Unify data for business accounts

For business accounts (B2B) where the data is centered around accounts, unification provides a unified view of your accounts. After unifying accounts, you can optionally [unify contacts](data-unification-contacts.md) for those accounts and link the unified contacts to the unified accounts.

[!INCLUDE [b2b-note](../includes/b2b-note.md)]

## Data unification process for B2B

The unification process maps account data from your data sources, removes duplicates, matches the data across tables, and creates a unified profile.

:::image type="content" source="media/b2b_unify_land.png" alt-text="Screenshot of unify landing page for first run experience for business accounts.":::

Unification is performed in the following order:

1. [Customer data](../data-unification-map-tables.md) (previously called Map): In the source fields step, select tables and fields to include in the unify process. Map fields to a common semantic type that describes the purpose of the field.

   > [!NOTE]
   > When you choose the semantic **Type**, the account name maps to *Organization.Name*. Otherwise, the customer cards appear nameless. An organization logo or image maps to *Organization.LogoImage*.

1. [Deduplication rules](../data-unification-duplicates.md) (previously part of Match): In the duplicate records step, optionally define rules to remove duplicate customer records from within each table.

1. [Matching rules](../data-unification-match-tables.md) (previously called Match): In the matching conditions step, define rules that match customer records between tables. When the system finds a customer in two or more tables, the process creates a single consolidated record with all columns and data from each table.

1. [Unified data view](../data-unification-merge-tables.md) (previously called Merge): In the unified customer fields step, determine which source fields to include, exclude, or merge into a unified customer profile.  

   > [!NOTE]
   > Group profiles into households or clusters isn't supported.

1. [Review](../data-unification-review.md) and select **Create account profiles** to create the unified profile.

   After unification, the **Data** > **Unify** page shows the number of unified customer (account) profiles. The unified account profile table is called *Customer* and displays in the **Profiles** section of the **Data** > **Tables** > **Output** page.

1. Optionally, [unify contacts](data-unification-contacts.md).

## Review or change unification settings

To review or change unification settings after you create a unified profile, complete the following steps: 

1. Go to **Data** > **Unify**.

   The **Unify** page shows the number of unified account profiles and tiles for each of the account unification steps. If you unify contacts, the number of unified contact profiles and tiles for each of the contact unification steps appear. Select the appropriate tile under **Unify Accounts** or **Unify Contacts (preview)** depending on what you want to update.

   :::image type="content" source="media/b2b_unified.png" alt-text="Screenshot of the Data Unify page after account and contact data is unified." lightbox="media/b2b_unified.png":::

1. Make changes. For more information, see [Update unification settings](../data-unification-update.md).

   > [!NOTE]
   > Select **Edit** on the **Relationships** tile to manage the contact and account relationships. If you select **No** for **Add contact to account relationship?**, you remove the relationship between contacts and accounts.

1. After making changes, choose one of the following options:

   - To run matching conditions and update the unified profile table without affecting dependencies (such as customer cards, enrichments, segments, or measures), select **Unify accounts** > **Unify profiles** to run accounts. For contacts, select **Unify contacts** > **Unify profiles**. The process doesn't run dependent processes, but it refreshes them as [defined in the refresh schedule](../schedule-refresh.md).
   - To run matching conditions, update the unified profiles, and run all dependencies, select **Unify accounts** > **Unify profiles and dependencies**. Matching rules run for both accounts and contacts, updating both unified profiles. The process runs all other dependencies.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
