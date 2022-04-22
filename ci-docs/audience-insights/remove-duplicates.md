---
title: "Remove duplicates before unifying data"
description: "The 2nd step in the unification process is selecting which record to keep when duplicates are found"
recommendations: false
ms.date: 04/22/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: v-wendysmith
ms.author: mukeshpo
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-map
  - ci-match
  - customerInsights
---

# Remove duplicates before unifying data

This step in unification sets up rules for handling duplicate records within an entity. *Deduplication* identifies duplicate records and merges them into one record. Source records get linked to the merged record with alternate IDs. This step is optional. If rules are not configured, system-defined rules are applied.

## Include enriched entities (preview)

If you enriched entities on the data source level to help improve your unification results, select them. For more information, see [Enrichment for data sources](data-sources-enrichment.md).

1. On the **Duplicate records** page, select **Use enriched entities** at the top of the page.

1. From the **Use enriched entities** pane, choose one or more enriched entities.

1. Select **Done**.

## Define deduplication on a match entity

1. On the **Duplicate records** page, select an entity and select **Add rule** to define the deduplication rules.

   :::image type="content" source="media/m3_duplicates_showmore.png" alt-text="Screenshot of Duplicate records pages with Show more highlighted":::

   1. In the **Add rule** pane, enter the following information:
      - **Select field**: Choose from the list of available fields from the entity that you want to check for duplicates. Choose fields that are likely unique for every single customer. For example, an email address, or the combination of name, city, and phone number.
        - **Normalize**: Select from following normalization options for the selected attributes.
        - **Numerals**: Converts other numeral systems, such as Roman numerals, to Arabic numerals. *VIII* becomes *8*.
        - **Symbols**: Removes all symbols and special characters. *Head&Shoulder* becomes *HeadShoulder*.
        - **Text to lower case: Converts all character to lower case**. *ALL CAPS and Title Case* becomes *all caps and title case*.
        - **Type (Phone, Name, Address, Organization)**: Standardizes names, titles, phone numbers, addresses, etc.
        - **Unicode to ASCII**: Converts unicode notation to ASCII characters. */u00B2* becomes *2*.
        - **Whitespace**: Removes all spaces. *Hello   World* becomes *HelloWorld*.
      - **Precision**: Set the level of precision to apply for this condition.
        - **Basic**: Choose from *Low*, *Medium*, *High*, and *Exact*. Select **Exact** to only match records that match 100 percent. Select one of the other levels to match records that aren't 100 percent identical.
        - **Custom**: Set a percentage that records need to match. The system will only match records passing this threshold.
      - **Name**: Name for the rule.

      :::image type="content" source="media/m3_duplicates_add.png" alt-text="Screenshot of Add rule pane for removing duplicates.":::

   1. Optionally, select **Add** > **Add condition** to add more conditions to the rule.

   1. Optionally, **Add** > **Add exception** to add exceptions to the rule. Exceptions are used to address rare cases of false positives and false negatives. For more information, see [Add exceptions to a rule](match-entities.md#add-exceptions-to-a-rule).

   1. Select **Done** to create the rule.

1. Optionally, add more rules.

1. Select an entity and then **Edit merge preferences**.

1. In the **Merge preferences** pane:
   1. Choose one of three options to determine which record to keep if a duplicate is found:
      - **Most filled**: Identifies the record with most populated attribute fields as the winner record. It's the default merge option.
      - **Most recent**: Identifies the winner record based on the most recency. Requires a date or a numeric field to define the recency.
      - **Least recent**: Identifies the winner record based on the least recency. Requires a date or a numeric field to define the recency.

   1. Optionally, to define deduplication rules on individual attributes of an entity, select **Advanced** at the bottom of the pane. For example, you can choose to keep the most recent email AND the most complete address from different records. Expand the entity to see all its attributes and define which option to use for individual attributes. If you choose a recency-based option, you also need to specify a date/time field that defines the recency.

      :::image type="content" source="media/m3_adv_merge.png" alt-text="Advanced merge preferences pane showing recent email and complete address":::

   1. Select **Done** to apply your merge preferences.

1. Select **Done** to apply your deduplication selections. The deduplication stats will display after the unification process is complete and run.

1. After defining the deduplication rules, select **Next**.

> [!div class="nextstepaction"]
> [Next step: Matching conditions](match-entities.md)

## Deduplication output as an entity

The deduplication process creates a new entity for every entity from the match pairs to identify the deduplicated records. These entities can be found along with the **ConflationMatchPairs:CustomerInsights** in the **System** section in the **Entities** page, with the name **Deduplication_DataSource_Entity**.

A deduplication output entity contains the following information:

- IDs / Keys
  - Primary key and Alternate ID fields. Alternate ID field consists of all the alternate IDs identified for a record.
  - Deduplication_GroupId field shows the group or cluster identified within an entity that groups all the similar records based on the specified deduplication fields. It's used for system processing purposes. If there are no manual deduplication rules specified and system defined deduplication rules apply, you may not find this field in the deduplication output entity.
  - Deduplication_WinnerId: This field contains the winner ID from the identified groups or clusters. If the Deduplication_WinnerId is same as the Primary key value for a record, it means that the record is the winner record.
- Fields used to define the deduplication rules.
- Rule and Score fields to denote which of the deduplication rules got applied and the score returned by the matching algorithm.

[!INCLUDE[footer-include](../includes/footer-banner.md)]