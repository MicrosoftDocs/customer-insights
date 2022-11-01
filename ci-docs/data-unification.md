---
title: "Create a unified view of your customers"
description: "Go through the data unification process with your data to create a single master dataset of account or customer profiles."
ms.date: 08/12/2022
ms.reviewer: v-wendysmith

ms.subservice: audience-insights
ms.topic: overview
author: Scott-Stabbert
ms.author: sstabbert
manager: shellyha

searchScope: 
  - ci-map
  - customerInsights
---

# Data unification overview

After [setting up the data sources](data-sources.md), you can unify the data. Data unification lets you unify once-disparate data sources into a single master dataset that provides a unified view of that data.

For individual consumers (B-to-C) where the data is centered around individuals, unification provides a unified view of your customers. For business accounts (B-to-B) where the data is centered around accounts, unification provides a unified view of your accounts. [Contact unification (preview)](data-unification-contacts.md) allows contacts for those accounts to be separately unified and associated with the accounts.

Data can be unified on a single table or multiple tables.

# [Individual consumers (B-to-C)](#tab/b2c)

The unification process maps customer data from your data sources, removes duplicates, matches the data across tables, and creates a unified profile. Unification is performed in the following order:

1. [Source fields](map-entities.md) (previously called Map): In the source fields step, select tables and fields to include in the unify process. Map fields to a common semantic type that describes the purpose of the field.

1. [Duplicate records](remove-duplicates.md) (previously part of Match): In the duplicate records step, optionally define rules to remove duplicate customer records from within each table.

1. [Matching conditions](match-entities.md) (previously called Match): In the matching conditions step, define rules that match customer records between tables. When a customer is found in two or more tables, a single consolidated record is created with all columns and data from each table.

1. [Unified customer fields](merge-entities.md) (previously called Merge): In the unified customer fields step, determine which source fields should be included, excluded, or merged into a unified customer profile.  

1. [Review](review-unification.md) and create the unified profile.

# [Business accounts (B-to-B)](#tab/b2b)

The unification process maps account data from your data sources, removes duplicates, matches the data across tables, and creates a unified profile. Unification is performed in the following order:

1. [Source fields](map-entities.md) (previously called Map): In the source fields step, select tables and fields to include in the unify account process. Map fields to a common semantic type that describes the purpose of the field.

1. [Duplicate records](remove-duplicates.md) (previously part of Match): In the duplicate records step, optionally define rules to remove duplicate account records from within each table.

1. [Matching conditions](match-entities.md) (previously called Match): In the matching conditions step, define rules that match account records between tables. When an account is found in two or more tables, a single consolidated record is created with all columns and data from each table.

1. [Unified customer fields](merge-entities.md) (previously called Merge): In the unified customer fields step, determine which source fields should be included, excluded, or merged into a unified customer profile.  

1. [Review](review-unification.md) and create the unified profile.

After unifying accounts, you can optionally [unify contacts (preview)](data-unification-contacts.md) for those accounts and link the unified contacts to the unified accounts.

---

After completing data unification, you can optionally:

- [Set up relationships between tables](relationships.md) to create sophisticated segments.
- [Enrich your data](enrichment-hub.md) to get a wider range of insights about your customers.
- [Define activities](activities.md) from some of the ingested attributes.
- [Build measures](measures.md) to better understand customer behaviors and business performance.

[!INCLUDE [footer-include](includes/footer-banner.md)]
