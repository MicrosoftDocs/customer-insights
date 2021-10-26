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

The **Customers** page shows a combined view of your unified customer profiles. The customer profiles are available once you [created the unified Customer entity](data-unification.md). The page lets you search for customers and define the index for that search.

Customers can be individuals or organizations. Each customer profile is represented by a tile. Use the pagination controls to get more records. The card displays fields from the *Customer* entity as defined in the **Search & filter index**. Select a tile to see data for the selected customer in a dedicated page called [Customer details page](customer-profiles.md#customer-details-page).

> [!div class="mx-imgBorder"] 
> ![Customers page showing result tiles](media/customers-page-result-tiles-B2C.png "Customers page showing result tiles")

> [!NOTE]
> If you can't see the tiles when you select **Customers** in navigation, your administrator needs to [define at least one searchable attribute](search-filter-index.md) in the **Search & filter index**.

## Search for customers

Search for customers by entering a name or some other attribute in the search box. The search only works within the _Customer_ entity created during the data unification process.

As an admin, you can configure the searchable attributes using the **Search & filter index** page. For more information, go to [Manage search & filter index](search-filter-index.md).

## Filter customers

You can filter customers by the _Customer_ entity fields. Similar to search, your admin will first need to define the fields as filterable using the **Search & filter index** page.

1. Select **Show filters** on the **Customers** page.

1. Check the boxes next to the attributes you want to filter customers by.

1. Remove your filters by selecting **Clear filters** on the **Customers** page.

## Customer details page

Select any of the customer tiles to open the **Customer details page**. This view contains unified information for the selected customer. Customer details include the following content:

**Customer profile tile**: This tile shows the different values from the unified _Customer_ entity. If a field has no value for the selected customer profile, it won't show. The tile is structured into sections:  
  - The first section shows a predefined set of fields followed by all fields that are part of the search & filter index. All address-related fields are combined into a single line if the profile contains such fields. 
  - **Contacts for this customer**: In environments for business accounts, you'll see all related contacts for this customer as the second section. Each contact is shown with their fields. Empty fields are hidden.
  - **Additional fields**: Shows the remaining fields of the selected customer, except IDs. 
  - **IDs**: Lists all IDs under their corresponding entity name. Fields are identified as IDs by their semantics, which categorize them as such.

**Activity timeline**: Shows data if you have configured activities. The timeline view contains chronologically sorted activities of the selected customer, starting with the most recent activity. For more information, go to [Customer activities](activities.md).

**Insights**:  
  - **Measures**: Shows if you configured one or more measures customer attribute measures. They include calculated KPIs around your customers on the individual customer level. For more information, go to [Define and manage measures](measures.md).

  -	**Potential interests, potential brands**: Shows if you configured a brand or interest affinity enrichment. It represents potential interests and affinities for brands based on other customers whose profile is similar to the selected customer profile. For more information, go to [Enrich customer profiles with brand and interest affinities](enrichment-microsoft.md).

To return to the customer search page, select **Back to Customers**.

## Next steps

[Add more data sources](data-sources.md), [enrich unified profiles](enrichment-hub.md), or [create segments](segments.md) to work with unified customer profiles in other applications.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
