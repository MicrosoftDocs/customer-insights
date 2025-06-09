---
title: "Data unification overview"
description: "Learn how to unify your customer data sources to create a single master dataset of customer profiles in Customer Insights - Data."
ms.date: 06/09/2025
ms.reviewer: v-wendysmith
ms.topic: overview
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Data unification overview

After [setting up the data sources](data-sources.md), you then unify the data. Unification combines your various customer data sources and creates a single customer profile record per customer. Unification eliminates duplicate data and combines all the important fields from your various data sources into a single record, eliminating data silos. Before unification, we recommend that you review your ingested source data and [remove any unwanted rows (preview)](tables-filters.md).

Data can be unified on a single table or multiple tables. Tables were previously called entities.

## Data unification process

The unification process consists of four steps:

1. **[Customer data](data-unification-map-tables.md)**: Select your source data that contains customer profile information like name, phone, and address. Don't include customer activity data such as purchases that have a one-to-many relationship to the customer. Map columns to descriptive types.

1. **[Deduplication](data-unification-duplicates.md)**: Define rules to find multiple rows for a single customer and select the best row to represent the customer. Deduplication rules remove duplicate rows to help ensure the best unification results.

1. **[Matching conditions](data-unification-match-tables.md)**: Define rules that match customer records between tables. Matching rules create a single consolidated record with all columns and data from each table.

1. **[Unified data view](data-unification-merge-tables.md)**: Determine which columns from the source tables should be included, excluded, or merged into a unified customer profile. For example, if you unify six tables and each table has an email column, you can merge them into a single email column.

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
- [FastTrack blog: Best practices for data modeling](https://community.dynamics.com/blogs/post/?postid=988fae7a-3f37-ee11-bdf4-6045bdebe084)
- [FastTrack blog: Advanced unification scenario for unrelated sources](https://community.dynamics.com/blogs/post/?postid=cbf1def2-2a94-4a4d-9535-0489e647157c)
- [FastTrack blog: Understanding Job Execution Flow in Customer Insights - Data Batch Runs](https://community.dynamics.com/blogs/post/?postid=84fbbaaf-262b-f011-8c4e-7c1e5218b899)

[!INCLUDE [footer-include](includes/footer-banner.md)]
