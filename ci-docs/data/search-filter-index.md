---
title: Manage the search and filter index for customer profiles
description: Manage the search and filter index to help users find unified customer profiles fast. Discover how to define searchable attributes, add filters, and apply changes.
ms.date: 08/13/2026
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom:
 - ai-gen-docs-bap
 - ai-seo-date: 08/13/2026
ai-usage: ai-assisted
---

# Manage the search and filter index for customer profiles

When you unify your customer data, the system creates a *Customer* table that gives you a unified view of your entire customer base. To help users [find information on a specific customer or group of customers](customer-profiles.md), an admin must set up the **Search** and **Filter** options for the **Customers** page.

   :::image type="content" source="media/search-filter.png" alt-text="Screenshot of the search and filter options on the Customers page.":::

## Define searchable attributes and indexed fields

If you're an admin defining searchable attributes for the first time, start by defining indexed fields. Choose all the attributes that users might use to search and filter customers on the **Customers** page. You can only specify attributes that exist in the *Customer* table created during the data unification process. For a field to be searchable, it must use the Edm.String data type and be marked as **Included in search**.

1. Go to **Customers** and select **Search & filter index** in the command bar.

1. Select **+ Add**.

1. Select the attributes in the list that you want to add as indexed fields and select **Apply**.

1. To add more attributes, select **Add**. To remove a selected attribute, select the attribute and then **Delete**.

   :::image type="content" source="media/search-filter-index.png" alt-text="Screenshot of the Search & filter index page.":::

1. Select **Run** when you're ready to apply your search and filter settings. After the changes are processed, view them in the [customer cards on the Customer page](customer-profiles.md).

## Define filtering options for an attribute

Set up the fields that you can use to filter customers on the **Customers** page.

1. Go to **Customers** and select **Search & filter index**.

1. Select an attribute and **Add Filter**. Define the number of results and the order for the results. Depending on the attribute's data type, one of the following panes appears.

   - String-type attributes: Specify the number of results you want on the **String filter** pane and the order policy for the results.

   - Numerical-type attributes: Specify the intervals on the **Number filter** pane and the order policy for the results.

   - Date-type attributes:  Specify the intervals on the **Date filter** pane and the order policy for the results.

1. Select **OK**. Repeat for all attributes you want to filter by.

1. Select **Run** when you're ready to apply your search and filter settings. After the changes are processed, view them in the [customer cards on the Customer page](customer-profiles.md).

## View indexed customer fields

The **Search & filter index** page displays the following information:

- **Name**: Shows the attribute name as it appears in the *Customer* table.
- **Data type**: Shows whether the data type is a string, a number, or a date.
- **Included in search**: Shows whether you can use this attribute to search for customers on the **Customers** page by using the **Search** field.
- **Add Filter**: Control to define how you can use this attribute for filtering on the **Customers** page.

## Performance considerations

For fast and optimized searches, add only fields with the following characteristics to the index:

 - **Low cardinality**: A small number of distinct values that repeat throughout your database.
 - **Short descriptive values**: One or two words that render nicely in a navigation tree.
 - Use the values within a field, and not the field name itself. For example, instead of the field name *Color*, add the values *Blue* or *Green* to the index.

## Best practices
 - Check for missing values, misspellings, or case discrepancies. Ensure consistency in your data to avoid repetitions.
 - Handle singular and plural versions of the same word. Filters don't get spell-checked or analyzed, so you can include every value in a searchable field, even if they differ by just one character.
 - Normalize searchable fields to make sure variations in case and characters are consistent.

Learn more about [Dataverse search](/power-platform/admin/configure-relevance-search-organization#set-up-dataverse-search).

## Next steps

Review the [unified profiles page](customer-profiles.md) to search for profiles or use the indexed fields to see a subset of all unified profiles.

[!INCLUDE [footer-include](includes/footer-banner.md)]
