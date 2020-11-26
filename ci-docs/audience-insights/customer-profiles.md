---
title: "Customer profiles"
description: "Get a consolidated view of your unified customer data."
ms.date: 04/16/2020
ms.reviewer: nimagen
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Customer profiles

The **Customers** page presents a consolidated view of your customers, based on profile data gathered from [all data sources](data-sources.md). Customer profiles are available once you [create the unified Customer entity](data-unification.md). Make sure you complete the data unification process to get richer views of your customers. The page also lets you search for customers.

Customers can be individuals or organizations (preview). Each customer or organization profile is represented by a tile. Select a tile to see additional information on that specific customer or organization. Use the pagination controls at the bottom of the page to see additional records.

> [!div class="mx-imgBorder"] 
> ![B2C customer profiles](media/profiles-customers.png "B2C customer profiles")

Organizations (Preview)
> [!div class="mx-imgBorder"] 
> ![B2B customer profiles](media/profile-customers-b2b.png "B2B customer profiles")

> [!NOTE]
> If you can't see the tiles when you select **Customers** in navigation, your administrator needs to [define at least one searchable attribute](search-filter-index.md) on the **Search & filter index**.

## Search for customers

Search for customers by entering a name or some other attribute in the search box. The search only works within the Customer Profile entity created during the data unification process.

As an admin, you can configure the searchable attributes using the **Search & filter index** page. For more information, see [Manage search & filter index](search-filter-index.md).

## Filter customers

You can filter customers by the Customer Profile entity fields. Similar to search, your admin will first need to define the fields as filterable using the **Search & filter index** page.

1. Select **Filter** on the top right corner of the **Customers** page.

2. Check the boxes next to the attributes you want to filter customers by.

   > [!div class="mx-imgBorder"] 
   > ![Customer profiles](media/profiles-customers3.png "Customer profiles")

3. Remove your filters by selecting **Clear filters** on the top right corner of the **Customers** screen.

##  The Customer details page
Clicking on any of the customers’ tiles will take you to the **Customer details page** whare you can view unified information for that specific customer.

The Customer details page includes the following components: 
-	**Customer profile tile:** Located at the left side, this tile shows the different values that were pulled from the unified customer profile entity. These details might include email address, name, city, etc. 
-	**Potential interests, potential brands:** These tiles only show up if you have successfully ran a first-party enrichment. It represents potential interests and affinities for brands a customer with a profile similar to this customer might have. [Learn more about our data enrichments](enrichment-microsoft-graph.md).
-	**Measures:** These tiles will show up if you have successfully ran one or more measures of a specific type called customer attribute measures. They include calculated KPIs around your customers on the individual customer level. [Learn more about measures](measures.md).
-	**Activity timeline:** This component will show up if you have configured activities. The component shows the consolidated activities of this customer sorted by time starting with the most recent activity. [Learn more about activities](activities.md).

To get back to the customer search page, click the button "Back to Customers" on the top of this page.

## Next steps

[Add more data sources](data-sources.md) or [create customer segments](segments.md).
