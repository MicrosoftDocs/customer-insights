---
title: "View customer profiles"
description: "View your unified customer data including using search and filter in Dynamics 365 Customer Insights"
ms.date: 12/17/2025
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom:
  - bap-template
  - sfi-image-nochange
---

# View customer profiles

You can view customer profiles after you [create the unified *Customer* table](data-unification.md). The **Customers** page displays the combined view of your unified customer profiles. Customers can be individuals or organizations.

Go to the **Customers** page to view your customers and their profiles. A tile represents each customer profile. Use the pagination controls to get more records. The card displays fields from the *Customer* table as defined in the **Search & filter index**. The system picks the order of the fields within each card.

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
  > To use search and filter, an admin must configure the searchable attributes and define the filterable fields by using the search & filter index.

## Known and unknown customers

Customer Insights - Data supports two types of profile types:

- Known customers: Profiles that have a known identifier, such as emailId, phone number, or loyaltyId, and are created through the [data unification process](data-unification.md).

- Unknown customers: Profiles that don't have a known identifier, but are identified through an unknown identifier such as cookieId. The [web tracking script](real-time-web-personalization.md) automatically creates these profiles when an unauthenticated customer visits your website. Unlike known profiles, unknown profiles expire after seven days of inactivity unless [converted to a known profile](real-time-web-personalization.md). Unknown profiles are free so that they don't count against your profiles used for billing.

## Customer count

Customer Insights displays a customer count in several locations. This number is a count of unified customer profiles and unknown profiles if [real-time web personalization is enabled](real-time-web-personalization.md). The counts shown can differ slightly.

- The count on the **Home** page and the **Unify** page is only calculated when unification runs.
- The count on the **Customers** page is updated in real time and can vary as unknown profiles are added in real time, and age out after 7 days.

## Search for customers

To search for customers, enter terms or phrases in the search box **Search customers**. The admin defines the searchable columns and comes from the unified *Customer* table. Search uses Azure cognitive search (ACS), which looks for matches in columns. However, only columns of data type string are included in search.

If the search has spaces or a hyphen (-), the search phrase is broken into individual terms. For example, searching on "Nancy-Smith" shows customers with "Nancy" and "Smith." Searching on "879 Steve Squares Apt. 093, Surprise, Arizona 80296 USA" shows customers that have some or all of the individual terms.

The best searches use a unique term such as CustomerID.

## Filter customers

Filter customers by the *Customer* table fields. The admin defines the filterable fields.

1. On the **Customers** page, select **Show filters**. The Filter pane displays.

1. Check the boxes next to the columns you want to use to filter customers.

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

**Customer profile tile** shows the different values from the unified *Customer* table. If a field has no value for the selected customer profile, it doesn't show except for the address field. The tile is structured into sections:

- The first section shows a predefined set of fields followed by all fields that are part of the search & filter index. All address-related fields are combined into a single line, which shows even if the profile contains no address information.
- **Additional fields** shows the remaining fields of the selected customer, except IDs.
- **IDs** lists all IDs under their corresponding table name. Fields are identified as IDs by their semantics.

**Activity timeline** shows data if you have configured [activities](activities.md). The timeline view contains chronologically sorted activities of the selected customer, starting with the most recent activity.

**Insights**:

- **Measures** show if you have configured [customer attribute measures](measures.md). They include calculated KPIs around your customers on the individual customer level.

- **Potential interests, potential brands** show if you configured a [brand or interest affinity enrichment](enrichment-microsoft.md). It represents potential interests and affinities for brands based on other customers whose profile is similar to the selected customer profile.

To return to the **Customers** page, select **Back to Customers**.

## Removing customer profiles

Profiles are generated dynamically based on source data. To modify generated profiles, you must modify the source to remove customer data, thus eliminating the resulting profile generation in Customer Insights - Data. [Learn more](dsr-rights-requests.md) 

## Next steps

[Add more data sources](data-sources.md), [enrich unified profiles](enrichment-manage.md), or [create segments](segments.md) to work with unified customer profiles in other applications.

[!INCLUDE [footer-include](includes/footer-banner.md)]
