---
title: "Enrich unified customer profiles"
description: "Use capabilities to enrich your customer data."
ms.date: 08/21/2020
ms.reviewer: kishorem
ms.service: dynamics-365-ai
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Enrichment for customer profiles (preview)

Use data from sources like Microsoft and other partners to enrich your customer data.

:::image type="content" source="media/enrichment-hub-page.png" alt-text="Enrichment hub page":::

In audience insights, go to **Data** > **Enrichment** to work with enrichment options.    
You need to have Contributor or Administrator permissions to create or edit enrichments. For more information, see [Permissions](permissions.md).

On the **Discover** tab, you'll find the following enrichments:

- [Brands](enrichment-microsoft-graph.md) provided by Microsoft Graph
- [Interests](enrichment-microsoft-graph.md) provided by Microsoft Graph
- [Company data](enrichment-leadspace.md)  provided by Leadspace
- [Demographics](enrichment-experian.md) provided by Experian

On the **My enrichments** tab, you can see the enrichments you've configured and edit their properties.

## Manage existing enrichments

Go to the **My enrichments** to see all configured enrichments. Each enrichment is represented as a row that includes additional information about the enrichment.

Select an enrichment to see the available options. Alternatively, you can select the ellipsis (...) on a list item to see the options.

<!--- :::image type="content" source="media/enrichment-hub-options-run.png" alt-text="Options to manage enrichments in the list of enrichments"::: --->

- **View** enrichment details with the number of enriched customer profiles.
- **Edit** the enrichment configuration.
- **Run** the enrichment to update customer profiles with the latest data.
- **Deactivate** an existing enrichment to stop it from refreshing automatically with every scheduled refresh. Data from the last successful refresh will continue to be available. **Activate** an inactive enrichment to restart automatic refreshing with every scheduled refresh.

You can run or deactivate multiple enrichments at once by selecting them in the list. View and edit options aren't available as bulk action and only work for one enrichment at a time.
