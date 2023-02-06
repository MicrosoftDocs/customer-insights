---
title: "View customer profiles"
description: "View your unified customer data including using search and filter"
ms.date: 06/08/2022
ms.reviewer: mhart

ms.topic: conceptual
author: Nils-2m
ms.author: nikeller
searchScope: 
  - ci-customers-page
  - ci-customer-card
  - ci-activities
  - ci-activities-wizard
  - customerInsights
---

# View customer profiles

Customer profiles are available once you [create the unified *Customer* entity](data-unification.md). The combined view of your unified customer profiles display on the **Customers** page. Customers can be individuals or organizations.

Go to the **Customers** page to view your customers and their profiles. Each customer profile is represented by a tile. Use the pagination controls to get more records. The card displays fields from the *Customer* entity as defined in the **Search & filter index**. The order of the fields within each card is picked by the system.

> [!NOTE]
> If you can't see the tiles when you select **Customers**, your administrator needs to [define at least one searchable attribute](search-filter-index.md) in the **Search & filter index**.

:::image type="content" source="media/customers-page-result-tiles-B2C.png" alt-text="Customers page showing result tiles.":::

Select any of the following actions:
- [View customer details](#view-customer-details)
- [Manage the search & filter index](search-filter-index.md) (admins only)
- [Filter customers](#filter-customers)
- **Expand cards** or **Collapse cards** to expand or collapse the information displayed on the customer tile
- **Sort by** a particular attribute
- [Search for customers](#search-for-customers)

  > [!NOTE]
  > To use search and filter, an admin must configure the searchable attributes and define the filterable fields using the search & filter index.

## Search for customers

Search for customers by entering a name or some other attribute in **Search customers**. The searchable attributes are defined by the admin and come from the unified *Customer* entity.

> [!NOTE]
> **String** is the only data type that is included in search. Use it in the **Search customers** field on the Customers page to search for customers.

## Filter customers

Filter customers by the *Customer* entity fields. Filterable fields are defined by the admin.

1. On the **Customers** page, select **Show filters**. The Filter pane displays.

1. Check the boxes next to the attributes you want to filter customers by.

1. Remove all filters by selecting **Clear filters** or clear a checkbox next to a selected attribute.

1. Select **Hide filters** to close the filter pane.

1. To save the filter results as a [segment](segments.md), select **Save filters as segment**.
   1. Enter a name for the segment.
   1. Select **Save** to save the segment.
   1. Choose whether to run the segment now by selecting **Activate** or run it **Later**.

## View customer details

On the **Customers** page, select a customer tile to view details for the selected customer.

:::image type="content" source="media/customers-details-B2C.png" alt-text="Customer details page.":::

Customer details include:

**Customer profile tile** shows the different values from the unified *Customer* entity. If a field has no value for the selected customer profile, it won't show except for the address field. The tile is structured into sections:

- The first section shows a predefined set of fields followed by all fields that are part of the search & filter index. All address-related fields are combined into a single line, which shows even if the profile contains no address information.
- **Contacts for this customer** display in environments for business accounts (B-to-B). Each contact is shown with their fields. Empty fields are hidden.
- **Additional fields** shows the remaining fields of the selected customer, except IDs.
- **IDs** lists all IDs under their corresponding entity name. Fields are identified as IDs by their semantics.

**Activity timeline** shows data if you have configured [activities](activities.md). The timeline view contains chronologically sorted activities of the selected customer, starting with the most recent activity.

**Insights**:

- **Measures** show if you have configured [customer attribute measures](measures.md). They include calculated KPIs around your customers on the individual customer level.

- **Potential interests, potential brands** show if you configured a [brand or interest affinity enrichment](enrichment-microsoft.md). It represents potential interests and affinities for brands based on other customers whose profile is similar to the selected customer profile.

To return to the **Customers** page, select **Back to Customers**.

## Next steps

[Add more data sources](data-sources.md), [enrich unified profiles](enrichment-hub.md), or [create segments](segments.md) to work with unified customer profiles in other applications.

[!INCLUDE [footer-include](includes/footer-banner.md)]
