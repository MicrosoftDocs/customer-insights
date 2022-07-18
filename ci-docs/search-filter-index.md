---
title: "Manage the Search & filter index for customer profiles"
description: "Quickly find information about unified customer profiles and filter for specified attributes."
ms.date: 11/01/2021
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: NimrodMagen
ms.author: nimagen
manager: shellyha
searchScope: 
  - ci-search-filter
  - customerInsights
---

# Manage the Search & filter index for customer profiles

The result of unifying your customer data is a Customer Profile entity that provides a unified view into your total customer base. For users to quickly [find information on a specific customer or group of customers](customer-profiles.md), an admin must configure the **Search** and **Filter** capabilities for the **Customers** page.

   :::image type="content" source="media/search-filter.png" alt-text="Search filter":::

## Add fields and specify attributes

If it's the first time you define searchable attributes as an administrator, define indexed fields first. We suggest you choose all the attributes by which users can search and filter customers on the **Customers** page. Only attributes that exist in the Customer Profile entity created during the data unification process can be specified.

1. Go to **Customers** and select **Search & filter index**.

2. Select **+ Add** to specify the indexed fields.

3. Select the attributes in the list you want to add as indexed fields. To add more attributes, select **Add**. To remove a selected attribute, select the attribute and then **Delete**.

> [!NOTE]
> **String** is the only data type that is included in search. Use it in the **Search** field on the Customers page to search for customers.

## Explore Indexed customer fields

The **Search & filter index** page displays the following information:

- **Name**: Represents the attribute's name as it appears in the Customer Profile entity.
- **Data type**: Specifies whether the data type is a string, a number, or a date.
- **Included in search**: Specifies whether this attribute can be used for searching customers on the **Customers** page using the **Search** field.
- **Add Filter**: Control to define how this attribute can be used for filtering on the **Customers** page.

## Edit filtering options for a given attribute

The **Filter** menu on the **Customers** page can include a varying number of attribute levels (for example, different age groups to filter customers by). Perform the following steps to set up the fields that can be used for filtering.

1. Go to **Customers** and select **Search & filter index**.

1. Select an attribute and **Add Filter**. Define the number of results and the order in which they'll be organized. Depending on the attribute's data type, one of the following panes appear.

   - String-type attributes: Specify the number of desired results on the **String filter** pane and the order policy by which they'll be organized.

   - Numerical-type attributes: Specify the intervals included on the **Number filter** pane and the order policy by which they'll be organized.

   - Date-type attributes:  Specify the intervals included on the **Date filter** pane and the order policy by which they'll be organized.

1. Select **Save**.

1. Select **Run** once you're ready to apply your settings. After the changes are processed, view them in the [customer cards on the Customer page](customer-profiles.md).

## Next steps

Review the [unified profiles page](customer-profiles.md) to search for profiles or use the indexed fields to see a subset of all unified profiles.

[!INCLUDE [footer-include](includes/footer-banner.md)]
