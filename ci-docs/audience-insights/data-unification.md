---
title: "Unify data in Dynamics 365 Customer Insights | Microsoft Docs"
description: "Learn how to unify data ingested into Dynamics 365 Customer Insights."
ms.date: 04/16/2020
ms.reviewer: adkuppa
ms.service: dynamics-365-ai
ms.topic: "get-started-article"
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Data unification

<!--rename file-->

After [setting up the data sources](data-sources.md), you can unify the data in Dynamics 365 Customer Insights. Data unification includes three steps: **Map**, **Match**, and **Merge**.

The data unification process lets you unify once-disparate data sources into a single master dataset that provides a unified view of your customers. Unification stages are mandatory, and performed in the following order:

1. [Map](map-entities.md)
2. [Match](match-entities.md)
3. [Merge](merge-entities.md)

After completing the data unification, you can optionally

- [set up relationships between entities](relationships.md) to create sophisticated segments,
- [enrich your data](enrichment-microsoft-graph.md) to get a wider range of insights about your customers,
- or [define activities](activities.md) from some of the ingested attributes.

> [!TIP]
> Check out the following video: [Getting Started: Creating a Unified Customer Profile](https://youtu.be/oBfGEhucAxs).
