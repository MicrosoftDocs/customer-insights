---
title: "Unify data for business accounts"
description: "Learn how to unify your data to create a single master dataset of account profiles."
ms.date: 09/01/2023
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Unify data for business accounts

For business accounts (B2B) where the data is centered around accounts, unification provides a unified view of your accounts. After unifying accounts you can optionally [unify contacts](data-unification-contacts.md) for those accounts and link the unified contacts to the unified accounts.

## Data unification process for B2B

The unification process maps account data from your data sources, removes duplicates, matches the data across tables, and creates a unified profile.

:::image type="content" source="media/b2b_unify_land.png" alt-text="Screenshot of unify landing page for first run experience for business accounts.":::

Unification is performed in the following order:

1. [Customer data](../data-unification-map-tables.md) (previously called Map): In the source fields step, select tables and fields to include in the unify process. Map fields to a common semantic type that describes the purpose of the field.

   > [!NOTE]
   > When choosing semantic **Type**, the account name should map to *Organization.Name*. Otherwise, the customer cards will appear nameless. An organization logo or image maps to *Organization.LogoImage*.

1. [Deduplication rules](../data-unification-duplicates.md) (previously part of Match): In the duplicate records step, optionally define rules to remove duplicate customer records from within each table.

1. [Matching rules](../data-unification-match-tables.md) (previously called Match): In the matching conditions step, define rules that match customer records between tables. When a customer is found in two or more tables, a single consolidated record is created with all columns and data from each table.

1. [Unified data view](../data-unification-merge-tables.md) (previously called Merge): In the unified customer fields step, determine which source fields should be included, excluded, or merged into a unified customer profile.  

   > [!NOTE]
   > Group profiles into households or clusters is not supported.

1. [Review](../data-unification-review.md) and select **Create account profiles** to create the unified profile.

   After unification, the **Data** > **Unify** page shows the number of unified customer (account) profiles. The unified account profile table is called *Customer* and displays in the **Profiles** section of the **Data** > **Tables** > **Output** page.

1. Optionally, [unify contacts](data-unification-contacts.md).

## Review or change unification settings

To review or change any unification settings once a unified profile has been created, perform the following steps. 

1. Go to **Data** > **Unify**.

   The **Unify** page displays the number of unified account profiles and tiles for each of the account unification steps. If contacts were unified, the number of unified contact profiles and tiles for each of the contact unification steps display. Choose the appropriate tile under **Unify Accounts** or **Unify Contacts (preview)** depending on what you want to update.

   :::image type="content" source="media/b2b_unified.png" alt-text="Screenshot of the Data Unify page after account and contact data is unified." lightbox="media/b2b_unified.png":::

1. Make changes. For more information, see [Update unification settings](../data-unification-update.md).

   > [!NOTE]
   > Select **Edit** on the **Relationships** tile to manage the contact and account relationships. If you select **No** for **Add contact to account relationship?**, you remove the relationship between contacts and accounts.

1. After making changes, choose one of the following:

   - To run matching conditions and update the unified profile table without impacting dependencies (such as customer cards, enrichments, segments, or measures), select **Unify accounts** > **Unify profiles** to run accounts. For contacts, select **Unify contacts** > **Unify profiles**. Dependent processes aren't run, but will be refreshed as [defined in the refresh schedule](../schedule-refresh.md).
   - To run matching conditions, update the unified profiles, and run all dependencies, select **Unify accounts** > **Unify profiles and dependencies**. Matching rules are run for both accounts and contacts updating both unified profiles and all other dependencies are run.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
