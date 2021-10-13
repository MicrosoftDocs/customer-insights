---
title: "Get started with business accounts as primary target audience"
description: "Learn about business accounts as primary target audience Dynamics 365 Customer Insights."
ms.date: 09/30/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: wimohabb
ms.reviewer: mhart
manager: shellyha
---

# Work with business accounts in audience insights

The audience insights capability in Dynamics 365 Customer Insights lets you configure your environment for different primary target audiences: individual customers (B2C) and business accounts (B2B). In B2C scenarios, the data is centered around individuals. For B2B, the primary target audiences are accounts - organizations or companies - and contacts. This article helps you to get started with an environment for business accounts. It lists the differences for the feature areas in audience insights, depending on your environment focus. For more information about differences, review the docs of the feature areas. 

## Create an environment for business accounts

Administrators can [create an environment in an existing organization](get-started-paid.md). A step in the process of creating a new environment asks administrators for the primary target audience of the environment. In case it's the initial set-up of audience insights after purchasing a license, a guided experience helps with the creation of the first environment.

You can then [ingest data](data-sources.md) for business accounts and related contacts as data sources from all supported sources.

After unifying the data, [specify account hierarchies](relationships.md#set-up-account-hierarchies) as part of the relationship configuration. You can also [configure semantic mappings](semantic-mappings.md) to connect contact and account entities. 

## Switch between primary target audience

If your organization maintains environments for individual customers and business accounts, you can use the switcher in the left pane to choose the primary target audience.

:::image type="content" source="media/switch-primary-target-audience.PNG" alt-text="Switcher to change the primary target audience between individual customers and business accounts.":::

## Supported feature areas

- [Activities](activities.md): Support for accounts and related contacts to create activities and show them in a timeline.
- [Relationships](relationships.md): The activity wizard helps creating relationships between the entities so the account view can show all activities from contacts. Contacts can drill up to see contact view and hierarchies can be used for account activity aggregations.
- [Measures](measures.md): Supports measures created from the measure builder with one calculation. An optional setting allows the roll-up for sub accounts when creating measures.
- [Segments](segments.md): Supports segments that are created from scratch with the segment builder. New operators allow incorporating account hierarchy when building segments.
- [Data ingestion](data-sources.md): All features in this area are the same for business accounts and individual customers.
- [Data unification](data-unification.md): All features in this area are the same for business accounts and individual customers.
- [Enrichment](enrichment-hub.md): Some enrichment types are available only for individual customer scenarios while others are exclusively available for business accounts.
- [Predictions and out-of-box models](predictions-overview.md): Transactional churn prediction contains additional steps for business accounts. Other predictions are only available for individual customers.
- [Activation and export](export-destinations.md): Exports are available for business accounts and individual customers. Some exports require extra configuration and contact information projected in the underlying segments to be valid for business accounts.
- [System settings](system.md) and [user management](permissions.md): All features in this area are the same for business accounts and individual customers.

