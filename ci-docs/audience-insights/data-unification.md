---
title: "Create a unified view of your customers"
description: "Go through the data unification process with your data to create a single master dataset of customer profiles."
ms.date: 03/31/2022
ms.reviewer: v-wendysmith

ms.subservice: audience-insights
ms.topic: overview
author: v-wendysmith
ms.author: adkuppa
manager: shellyha

searchScope: 
  - ci-map
  - customerInsights
---

# Data unification overview

After [setting up the data sources](data-sources.md), you can unify the data. Data unification lets you unify once-disparate data sources into a single master dataset that provides a unified view of that data. For individual consumers (B-to-C) where the data is centered around individuals, unification provides a unified view of your customers. For business accounts (B-to-B) where the data is centered around accounts, unification provides a unified view of your accounts.

Data unification is mandatory and performed in the following order:

1. [Select source fields](map-entities.md) which map entities and attributes to include in a unified customer or account profile.
1. [Remove duplicate records](remove-duplicates.md) (optional).
1. Create [match rules and conditions](match-entities.md) for cross-entity matching.
1. Reconcile [unified customer fields](merge-entities.md) to merge the data.
1. [Review](review-unification.md) and create the unified profile.

After completing the data unification, you can optionally:

- [Set up relationships between entities](relationships.md) to create sophisticated segments
- [Enrich your data](enrichment-hub.md) to get a wider range of insights about your customers
- [Define activities](activities.md) from some of the ingested attributes

[!INCLUDE[footer-include](../includes/footer-banner.md)]
