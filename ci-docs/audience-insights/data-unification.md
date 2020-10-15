---
title: "Data unification"
description: "Learn how to unify ingested data."
ms.date: 04/16/2020
ms.reviewer: adkuppa
ms.service: customer-insights
ms.subservice:
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Data unification

After [setting up the data sources](data-sources.md), you can unify the data. Data unification includes three steps: **Map**, **Match**, and **Merge**.

The data unification process lets you unify once-disparate data sources into a single master dataset that provides a unified view of your customers. Unification stages are mandatory, and performed in the following order:

1. [Map](map-entities.md)
2. [Match](match-entities.md)
3. [Merge](merge-entities.md)

After completing the data unification, you can optionally

- [set up relationships between entities](relationships.md) to create sophisticated segments
- [enrich your data](enrichment-hub.md) to get a wider range of insights about your customers
- [define activities](activities.md) from some of the ingested attributes
