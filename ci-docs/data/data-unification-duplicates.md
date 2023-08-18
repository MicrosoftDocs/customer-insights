---
title: "Remove duplicates before unifying data"
description: "The second step in the unification process is selecting which record to keep when duplicates are found."
ms.date: 09/01/2023
ms.topic: tutorial
author: v-wendysmith
ms.author: sstabbert
ms.reviewer: v-wendysmith
---

# Remove duplicates before unifying data

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

This optional step in unification enables you to set up rules for eliminating duplicate records **within** a table. Deduplication identifies multiple records for a customer and selects the best record to keep (based on the selected merge policy) or merges the records into one (based on advanced merge preferences). Source records get linked to the merged record with alternate IDs. Nonwinner records are called alternate rows. Ideally, each individual table has a single row for each customer prior to matching records between tables.

Deduplication of customer records in each table is important to improve unification results and performance. Defining your own deduplication rules gives you flexibility and control. However, if you don't define any custom deduplication rules for a table, Dynamics 365 Customer Insights - Data runs default deduplication rules.

## Default deduplication rules

The system-defined rules apply if no deduplication rules are added.

1. Deduplicate on primary keys

   First, the system matches records that have the same primary key and keeps the first record in the table. For example, if four records are found with primary key “12345” the first of those four records found in the table are kept as the winner record.

1. Deduplicate on fields used in Matching conditions

   Next, the system deduplicates on all fields that are used in matching rules for the table. For example, in Matching conditions, if Table1 has rule 1 that matches on *Name+Email* and rule 2 that matches on *Name+Phone*, Customer Insights - Data deduplicates Table1 by doing an exact match on *Name+Email+Phone*. If several records are found with an exact match on *Name+Email+Phone*, then the first record in the table is kept as the winner. Use of normalization or precision in the match rules isn't used in default deduplication.

If you define your own deduplication rules, the system runs those rules first. Then, deduplicates the tables on the primary key. If duplicate primary keys are found, instead of picking the first record as the winner, it uses a winner record (if any) as defined by your custom deduplication rules.

For example, six records have primary key “20”. Three of these records are deduplicated by a custom rule and a winner selected. Customer Insights - Data then deduplicates on the primary key finding the winner record and the three remaining records. The system uses the previously defined winner record as the final winner. If there's no winner record in the set of records, or if there are multiple winner records defined by different deduplication rules, then the usual rule of using the first record as the winner applies.

## Include enriched tables (preview)

If you enriched tables on the data source level to help improve your unification results, select them. For more information, see [Enrichment for data sources](data-sources-enrichment.md).

1. On the **Duplicate records** page, select **Use enriched tables** at the top of the page.

1. From the **Use enriched tables** pane, choose one or more enriched tables.

1. Select **Done**.

## Define deduplication rules

A good rule identifies a unique customer. Consider your data. It may be enough to identify customers based on a field such as email. However, if you want to differentiate customers that share an email, you may choose to have a rule with two conditions, matching on Email + FirstName.

1. On the **Duplicate records** page, select a table and select **Add rule** to define the deduplication rules.

   :::image type="content" source="media/m3_duplicates_showmore.png" alt-text="Screenshot of Duplicate records page with table highlighted and Add rule displayed"  lightbox="media/m3_duplicates_showmore.png":::

   1. In the **Add rule** pane, enter the following information:
      - **Select field**: Choose from the list of available fields from the table that you want to check for duplicates. Choose fields that are likely unique for every single customer. For example, an email address, or the combination of name, city, and phone number.
      - **Normalize**: Select from following normalization options for the selected attributes. Normalization only impacts the matching step, and doesn't change the data.
        - **Numerals**: Converts other numeral systems, such as Roman numerals, to Arabic numerals. *VIII* becomes *8*.
        - **Symbols**: Removes all symbols and special characters. *Head&Shoulder* becomes *HeadShoulder*.
        - **Text to lower case: Converts all character to lower case**. *ALL CAPS and Title Case* becomes *all caps and title case*.
        - **Type (Phone, Name, Address, Organization)**: Standardizes names, titles, phone numbers, addresses, etc.
        - **Unicode to ASCII**: Converts unicode notation to ASCII characters. */u00B2* becomes *2*.
        - **Whitespace**: Removes all spaces. *Hello   World* becomes *HelloWorld*.
      - **Precision**: Set the level of precision to apply for this condition. Precision is used with fuzzy matching, and determines how close two strings need to be in order to be considered a match.
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
      - **Most filled**: Identifies the record with most populated attribute fields as the winner record. It's the default merge option.
      - **Most recent**: Identifies the winner record based on the most recency. Requires a date or a numeric field to define the recency.
      - **Least recent**: Identifies the winner record based on the least recency. Requires a date or a numeric field to define the recency.

      If there's a tie, the winner record is the one with the MAX(PK) or the larger primary key value.

   1. Optionally, to define merge preferences on individual attributes of a table, select **Advanced** at the bottom of the pane. For example, you can choose to keep the most recent email AND the most complete address from different records. Expand the table to see all its attributes and define which option to use for individual attributes. If you choose a recency-based option, you also need to specify a date/time field that defines the recency.

      :::image type="content" source="media/m3_adv_merge.png" alt-text="Advanced merge preferences pane showing recent email and complete address":::

   1. Select **Done** to apply your merge preferences.

1. After defining the deduplication rules and merge preferences, select **Next**.
  
> [!div class="nextstepaction"]
> [Next step for a single table: Unify fields](data-unification-merge-tables.md)

> [!div class="nextstepaction"]
> [Next step for multiple tables: Matching conditions](data-unification-match-tables.md)

[!INCLUDE[footer-include](includes/footer-banner.md)]
