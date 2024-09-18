---
title: "Manage the search & filter index for customer profiles"
description: "Quickly find information about unified customer profiles and filter for specified attributes."
ms.date: 09/27/2023
ms.reviewer: mhart
ms.topic: conceptual
author: NimrodMagen
ms.author: nimagen
ms.custom: bap-template
---

# Manage the search & filter index for customer profiles

The result of unifying your customer data is a *Customer* table that provides a unified view into your total customer base. For users to quickly [find information on a specific customer or group of customers](customer-profiles.md), an admin must configure the **Search** and **Filter** capabilities for the **Customers** page.

   :::image type="content" source="media/search-filter.png" alt-text="Search filter":::

## Define searchable attributes and indexed fields

If it's the first time you define searchable attributes as an administrator, define indexed fields first. We suggest you choose all the attributes by which users can search and filter customers on the **Customers** page. Only attributes that exist in the *Customer* table created during the data unification process can be specified. For a field to be searchable, the field must use the Edm.String data type and be marked as **Included in search**.

1. Go to **Customers** and select **Search & filter index**.

1. Select **+ Add**.

1. Select the attributes in the list you want to add as indexed fields and select **Apply**.

1. To add more attributes, select **Add**. To remove a selected attribute, select the attribute and then **Delete**.

   :::image type="content" source="media/search-filter-index.png" alt-text="Search & filter index page.":::

1. Select **Run** once you're ready to apply your search and filter settings. After the changes are processed, view them in the [customer cards on the Customer page](customer-profiles.md).

## Define filtering options for a given attribute

Set up the fields that can be used for filtering customers on the **Customers** page.

1. Go to **Customers** and select **Search & filter index**.

1. Select an attribute and **Add Filter**. Define the number of results and the order in which they'll be organized. Depending on the attribute's data type, one of the following panes appears.

   - String-type attributes: Specify the number of desired results on the **String filter** pane and the order policy by which they'll be organized.

   - Numerical-type attributes: Specify the intervals included on the **Number filter** pane and the order policy by which they'll be organized.

   - Date-type attributes:  Specify the intervals included on the **Date filter** pane and the order policy by which they'll be organized.

1. Select **OK**. Repeat for all attributes you want to filter by.

1. Select **Run** once you're ready to apply your search and filter settings. After the changes are processed, view them in the [customer cards on the Customer page](customer-profiles.md).

## View indexed customer fields

The **Search & filter index** page displays the following information:

- **Name**: Represents the attribute's name as it appears in the *Customer* table.
- **Data type**: Specifies whether the data type is a string, a number, or a date.
- **Included in search**: Specifies whether this attribute can be used for searching customers on the **Customers** page using the **Search** field.
- **Add Filter**: Control to define how this attribute can be used for filtering on the **Customers** page.

## Performance considerations
For optimized (fast) search index only fields that have these characteristics:
 - **Low cardinality**: A small number of distinct values that repeat throughout documents in your search corpus.
 - **Short descriptive values**: One or two words that render nicely in a navigation tree.
 - Use the values within a field, and not the field name itself, for example if there is a string field named "Color" the values could be "Blue" "Green" or any other value for that field.

Best practices:
 - Check for null values, misspellings, or case discrepancies: Ensure consistency in your data to avoid redundant facets.
 - Handle single and plural versions of the same word: By default, filters and facets don't undergo lexical analysis or spell check, which means that all values of a "facetable" field are potential facets, even if the words differ by one character.
 - Use normalizers: Optionally, you can assign a normalizer to a "filterable" and "facetable" field to smooth out variations in casing and characters.

Learn more about [dataverse search](https://go.microsoft.com/fwlink/?linkid=2167645).

## Next steps

Review the [unified profiles page](customer-profiles.md) to search for profiles or use the indexed fields to see a subset of all unified profiles.

[!INCLUDE [footer-include](includes/footer-banner.md)]
