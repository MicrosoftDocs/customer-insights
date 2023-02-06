---
title: "Work with business accounts"
description: "Learn about business accounts as primary target audience in Dynamics 365 Customer Insights."
ms.date: 10/19/2021

ms.topic: conceptual
author: v-wendysmith
ms.custom: intro-internal
ms.author: wimohabb
ms.reviewer: v-wendysmith
searchScope: 
  - ci-semantic-mapping
  - ci-connections
  - customerInsights
---

# Work with business accounts

The Dynamics 365 Customer Insights lets you configure your environment for different primary target audiences: individual consumers (B-to-C) and business accounts (B-to-B). In B-to-C scenarios, the data is centered around individuals. For B-to-B, the primary target audiences are accounts - organizations or companies - and contacts. This article helps you to get started with an environment for business accounts. It lists the differences for the feature areas in Customer Insights, depending on your environment focus. For more information about differences, review the docs of the feature areas. 

## Create an environment for business accounts

Administrators can [create an environment in an existing organization](create-environment.md). A step in the process of creating a new environment asks administrators for the primary target audience of the environment. In case it's the initial set-up after purchasing a license, a guided experience helps with the creation of the first environment.

You can then [ingest data](data-sources.md) for business accounts and related contacts as data sources from all supported sources.

 [Unify](data-unification.md) your account data followed by your contact data to connect contact and account entities.

## Switch between primary target audience

If your organization maintains environments for individual customers and business accounts, you can use the switcher in the left pane to choose the primary target audience.

:::image type="content" source="media/switch-primary-target-audience.png" alt-text="Switcher to change the primary target audience between individual customers and business accounts.":::

## Supported feature areas

- [Activities](activities.md): Support for accounts and related contacts to create activities and show them in a timeline.
- [Relationships](relationships.md): The activity wizard helps creating relationships between the entities so the account view can show all activities from contacts. Contacts can drill up to see contact view and hierarchies can be used for account activity aggregations.
- [Measures](measures.md): Supports measures created from the measure builder with one calculation. An optional setting allows the roll-up for sub accounts when creating measures.
- [Segments](segments.md): Supports segments that are created from scratch with the segment builder. Segments can be based on accounts or contacts.
- [Data ingestion](data-sources.md): All features in this area are the same for business accounts and individual customers.
- B-to-B data unification is very similar to B-to-C data unification but has an additional step to unify contacts after account unification. See [Business accounts (B-to-B)](data-unification.md).
- [Enrichment](enrichment-hub.md): Some enrichment types are available only for individual customer scenarios while others are exclusively available for business accounts.
- [Predictions and out-of-box models](predictions-overview.md): Transactional churn prediction contains additional steps for business accounts. Other predictions are only available for individual customers.
- [Activation and export](export-destinations.md): Exports are available for business accounts and individual customers. Some exports require extra configuration and contact information projected in the underlying segments to be valid for business accounts.
- [System settings](system.md) and [user management](permissions.md): All features in this area are the same for business accounts and individual customers.

[!INCLUDE [footer-include](includes/footer-banner.md)]
