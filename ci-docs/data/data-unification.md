---
title: "Data unification overview"
description: "Learn how to unify your data to create a single master dataset of customer profiles."
ms.date: 11/15/2023
ms.reviewer: v-wendysmith
ms.topic: overview
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Data unification overview

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

After [setting up the data sources](data-sources.md), you can unify the data. Data unification lets you unify once-disparate data sources into a single master dataset that provides a unified view of your customers.

Data can be unified on a single table or multiple tables. Tables were previously called entities.

## Data unification process

The unification process maps customer data from your data sources, removes duplicates, matches the data across tables, and creates a unified profile. Unification is performed in the following order:

1. [Customer data](data-unification-map-tables.md): In the Customer data step, select tables and columns to include in the unification process. Map fields to a common type that describes the purpose of the field.

1. [Deduplication rules](data-unification-duplicates.md): In the Deduplication rules step, optionally define rules to remove duplicate customer records from within each table.

1. [Matching rules](data-unification-match-tables.md): In the matching rules step, define rules that match customer records between tables. When a customer is found in two or more tables, a single consolidated record is created with all columns and data from each table.

1. [Unified data view](data-unification-merge-tables.md): In the unified data view step, determine which customer columns should be included, excluded, or merged into a unified customer profile.  

1. [Review](data-unification-review.md) and create the unified profile.

## Next steps

After completing data unification, you can optionally:

- [Set up relationships between tables](relationships.md) to create sophisticated segments.
- [Enrich your data](enrichment-manage.md) to get a wider range of insights about your customers.
- [Define activities](activities.md) from some of the ingested attributes.
- [Build measures](measures.md) to better understand customer behaviors and business performance.

[!INCLUDE [footer-include](includes/footer-banner.md)]
