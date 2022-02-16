---
title: "Data source enrichment"
description: "Enrich data sources before going through the data unification process."
ms.date: 02/10/2022
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: v-wendysmith
ms.author: v-wendysmith
ms.reviewer: mhart
manager: shellyha

---

# Enrichment for data sources (preview)

Use data from sources like Microsoft and other partners to enrich your customer data before data unification. Pre-unification of customer data can produce higher quality unified customer profiles. For example, using a normalized and standardized format for addresses can increase the quality of the match results.

Supported data source enrichment options include **Enhanced addresses** provided by Microsoft.

## Enrich a data source

You must have Contributor or Administrator permissions to create or edit enrichments. For more information, see [Permissions](permissions.md).  

1. In audience insights, go to **Data** > **Unify**. Select the entity you want to enrich and select one attribute as a primary key for the entity. For more information, see [Select primary key](map-entities.md).

1. Go to **Data** > **Data sources**.
 
1. Select the vertical ellipsis next to the data source you want to enrich and select **Enrich**.

   :::image type="content" source="media/data_sources_enrich_discover.png" alt-text="Data sources enrichment page.":::

   The **Discover** tab displays the [supported data source enrichment options](#supported-data-source-enrichments).

1. Select **Enrich my data** to configure a data source enrichment. The output entity name is automatically populated.

## Supported data source enrichments

The following enrichments are currently available for data sources. Review the detailed steps for the enrichment to learn how to configure it.

- [Enhanced addresses](enrichment-enhanced-addresses.md)

## Manage existing data source enrichments

Go to the **My enrichments** tab to see all configured enrichments.

Select the enrichment to see the available options. You can also select the ellipsis (...) on a list item to see the options. If you configured several enrichments, you can use the search box to find it quickly.

You can view, edit, run, or delete a data source enrichment. For more information, see [Manage existing enrichments](enrichment-hub.md).
