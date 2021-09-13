---
title: "View customer profiles"
description: "Get a combined view of your unified customer data."
ms.date: 09/30/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: Nils-2m
ms.author: nikeller
manager: shellyha
---

# Customer profiles

The **Customers** page shows a combined view of your customers, based on profile data gathered from [all data sources](data-sources.md). Customer profiles are available once you [create the unified Customer entity](data-unification.md). Make sure you complete the data unification process to get richer views of your customers. The page also lets you search for customers.

Customers can be individuals or organizations. Each customer profile is represented by a tile. Use the pagination controls to get more records. The card displays the profile fields defined in the [search & filter index](search-filter-index.md). Select a tile to load more data for that customer profile in a separate view. 

> [!div class="mx-imgBorder"] 
> ![B2C customer profiles.](media/profiles-customers.png "B2C customer profiles")

> [!NOTE]
> If you can't see the tiles when you select **Customers** in navigation, your administrator needs to [define at least one searchable attribute](search-filter-index.md) on the **Search & filter index**.

## Search for customers

Search for customers by entering a name or some other attribute in the search box. The search only works within the Customer Profile entity created during the data unification process. 

As an admin, you can configure the searchable attributes using the **Search & filter index** page. For more information, see [Manage search & filter index](search-filter-index.md).

## Filter customers

You can filter customers by the Customer Profile entity fields. Similar to search, your admin will first need to define the fields as filterable using the **Search & filter index** page.

1. Select **Filter** on the **Customers** page.

2. Check the boxes next to the attributes you want to filter customers by.

   > [!div class="mx-imgBorder"] 
   > ![Customer profiles.](media/profiles-customers3.png "Customer profiles")

3. Remove your filters by selecting **Clear filters** on the **Customers** page.

##  Customer details page

Select any of the customer tiles to open the **Customer details page**. This view contains unified information for the selected customer.

Customer details include:

-	**Customer profile tile**: This tile shows the different values from the unified customer profile entity. If a field has no value set for the in the selected customer profile, it won't show. The tile is structured into sections. The first section shows a predefined set of fields followed by all fields which are part of the search & filter index. If available, the system combines all address-related fields in the address line. The second section is called **additional fields**. It shows remaining fields, except IDs. Fields which are identified by their semantics categorizing them as IDs, are grouped in the third section called **IDs**. Within the third section, fields are grouped by thr entity they belong to.

-	**Activity timeline**: Shows if you have configured activities. The timeline view contains chronologically sorted activities of th selected customer profile, starting with the most recent activity. For more information, see [Customer activities](activities.md).

-	**Measures**: Shows if you configured one or more measures of a specific type: customer attribute measures. They include calculated KPIs around your customers on the individual customer level. For more information, see [Define and manage measures](measures.md).

-	**Potential interests, potential brands**: Shows if you configured a brand or interest affinity enrichment. It represents potential interests and affinities for brands a other customers whose profile is similar to the selected customer profile. For more information, see [Enrich customer profiles with brand and interest affinities](enrichment-microsoft.md).

Select **Back to Customers** to return to the customer search page.

## Next steps

[Add more data sources](data-sources.md), [enrich unified profiles](enrichment-hub.md), or [create segments](segments.md) to work with unified profiles in other applications.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
