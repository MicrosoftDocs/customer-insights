---
title: "Remove duplicates before unifying data"
description: "The second step in the unification process is selecting which record to keep when duplicates are found."
ms.date: 07/12/2024
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Remove duplicates in each table for data unification

The Deduplication rules step of unification finds and removes duplicate records for a customer from a source table so that each customer is represented by a single row in each table. Each table is deduplicated separately using rules to identify the records for a given customer.

Rules are processed in order.  After all rules have been run on all the records in a table, match groups that share a common row are combined into a single match group.

## Define deduplication rules

A good rule identifies a unique customer. Consider your data. It might be enough to identify customers based on a field such as email. However, if you want to differentiate customers that share an email, you might choose to have a rule with two conditions, matching on Email + FirstName. For more information, see [Deduplication best practices](data-unification-best-practices.md#deduplication).

1. On the **Deduplication rules** page, select a table and select **Add rule** to define the deduplication rules.

   > [!TIP]
   > If you enriched tables on the data source level to help improve your unification results, select **Use enriched tables** at the top of the page. For more information, see [Enrichment for data sources](data-sources-enrichment.md).

   :::image type="content" source="media/m3_duplicates_showmore.png" alt-text="Screenshot of Deduplication rules page with table highlighted and Add rule displayed"  lightbox="media/m3_duplicates_showmore.png":::

   1. In the **Add rule** pane, enter the following information:
      - **Select field**: Choose from the list of available fields from the table that you want to check for duplicates. Choose fields that are likely unique for every single customer. For example, an email address, or the combination of name, city, and phone number.
      - **Normalize**: Select [normalization options](data-unification-best-practices.md#normalization) for the column. Normalization only impacts the matching step, and doesn't change the data.
        - [!INCLUDE[normalization](includes/normalization.md)]
      - **Precision**: Set the level of precision. [Precision is used for exact match and fuzzy matching](data-unification-best-practices.md), and determines how close two strings need to be in order to be considered a match.
        - **Basic**: Choose from *Low (30%)*, *Medium (60%)*, *High (80%)*, and *Exact (100%)*. Select **Exact** to only match records that match 100 percent.
        - **Custom**: Set a percentage that records need to match. The system only matches records passing this threshold.
      - **Name**: Name for the rule.

      :::image type="content" source="media/m3_duplicates_add.png" alt-text="Screenshot of Add rule pane for removing duplicates.":::

   1. Optionally, select **Add** > **Add condition** to add more conditions to the rule. Conditions are connected with a logical AND operator and thus only executed if all conditions are met.

   1. Optionally, **Add** > **Add exception** to [add exceptions to the rule](data-unification-match-tables.md#add-exceptions-to-a-rule). Exceptions are used to address rare cases of false positives and false negatives.

   1. Select **Done** to create the rule.

1. Optionally, [add more rules](#define-deduplication-rules).

1. Select a table and then **Edit merge preferences**.

1. In the **Merge preferences** pane:
   1. Choose one of three options to determine which record to keep if a duplicate is found:
      - **Most filled**: Identifies the record with most populated columns as the winner record. It's the default merge option.
      - **Most recent**: Identifies the winner record based on the most recency. Requires a date or a numeric field to define the recency.
      - **Least recent**: Identifies the winner record based on the least recency. Requires a date or a numeric field to define the recency.

      If there's a tie, the winner record is the one with the MAX(PK) or the larger primary key value.

   1. Optionally, to define merge preferences on individual columns of a table, select **Advanced** at the bottom of the pane. For example, you can choose to keep the most recent email AND the most complete address from different records. Expand the table to see all its columns and define which option to use for individual columns. If you choose a recency-based option, you also need to specify a date/time field that defines the recency.

      :::image type="content" source="media/m3_adv_merge.png" alt-text="Advanced merge preferences pane showing recent email and complete address":::

   1. Select **Done** to apply your merge preferences.

1. After defining the deduplication rules and merge preferences, select **Next**.
  
> [!div class="nextstepaction"]
> [Next step for a single table: View unified data](data-unification-merge-tables.md)

> [!div class="nextstepaction"]
> [Next step for multiple tables: Define matching rules](data-unification-match-tables.md)

[!INCLUDE[footer-include](includes/footer-banner.md)]
