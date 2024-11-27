---
title: "Data unification overview"
description: "Learn how to unify your data to create a single master dataset of customer profiles."
ms.date: 11/27/2024
ms.reviewer: v-wendysmith
ms.topic: overview
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Data unification overview

After [setting up the data sources](data-sources.md), you can unify the data. Data unification lets you unify once-disparate data sources into a single master dataset that provides a unified view of your customers.

Data can be unified on a single table or multiple tables. Tables were previously called entities.

## Data unification process

The unification process maps customer data from your data sources, removes duplicates, matches the data across tables, and creates a unified profile. Unification is performed in the following order:

1. [Customer data](data-unification-map-tables.md): In the Customer data step, select tables and columns to include in the unification process. Map fields to a common type that describes the purpose of the column.

1. [Deduplication rules](data-unification-duplicates.md): In the Deduplication rules step, optionally define rules to remove duplicate customer records from within each table.

1. [Matching rules](data-unification-match-tables.md): In the matching rules step, define rules that match customer records between tables. When a customer is found in two or more tables, a single consolidated record is created with all columns and data from each table.

1. [Unified data view](data-unification-merge-tables.md): In the unified data view step, determine which customer columns should be included, excluded, or merged into a unified customer profile.  

1. [Review](data-unification-review.md) and create the unified profile.

## Customer ID

When unification runs, a unique **CustomerId** is assigned to each customer profile. This ID doesn't change between unification runs except in the following two cases.

- **Merge profiles**
  When two or more or more unified profiles exist and the source data or rules change such that the source data now matches, then the next unification run creates one customer profile where several previously existed. The new merged customer profile is assigned one of the previous CustomerIds. In rare cases a new CustomerId might be assigned, for example when many changes happen to one or both of the unified profiles being merged. The **PreviousCustomerId** field for the merged customer profile shows the previous CustomerId, or when appropriate, multiple CustomerIds separated by semicolons.

- **Split a profile**
  When one unified customer profile exists and the source data or rules change such that the records no longer match, then the next unification run creates two or more customer profiles where one previously existed. One record retains the previous CustomerId, while the others are assigned a new CustomerID. The **PreviousCustomerId** field for the customer profile with the newly assigned CustomerId shows the CustomerId the profile was split off from.

## See also

- [Set up relationships between tables](relationships.md) to create sophisticated segments.
- [Enrich your data](enrichment-manage.md) to get a wider range of insights about your customers.
- [Define activities](activities.md) from some of the ingested columns.
- [Build measures](measures.md) to better understand customer behaviors and business performance.
- [FastTrack blog: Best practices for data modelling](https://community.dynamics.com/blogs/post/?postid=988fae7a-3f37-ee11-bdf4-6045bdebe084)
- [FastTrack blog: Advanced unification scenario for unrelated sources](https://community.dynamics.com/blogs/post/?postid=cbf1def2-2a94-4a4d-9535-0489e647157c)

[!INCLUDE [footer-include](includes/footer-banner.md)]
