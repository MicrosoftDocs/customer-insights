---
title: "Remove duplicates before unifying data"
description: "The 2nd step in the unification process is selecting which record to keep when duplicates are found"
ms.date: 03/02/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: v-wendysmith
ms.author: adkuppa
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-map
  - ci-match
---

# Remove duplicates

This step in customer or account unification sets up rules for handling duplicate records. This step is optional. If rules are not configured, system-defined rules are applied. Customer Insights identifies duplicate records and merges them into one record. Source records get linked to the merged record with alternate IDs.

> [!NOTE]
> For individual consumers (B-C), the unification process involves customers. For business accounts, this part of the unification process involves accounts. Screen titles indicate whether it is customers or accounts.

## Include enriched entities (preview)

If you enriched entities on the data source level to help improve your unification results, select them. For more information, see [Enrichment for data sources](data-sources-enrichment.md).

1. Select **Use enriched entities** at the top of the page.

1. From the **Use enriched entities** pane, choose one or more enriched entities.

1. Select **Apply**.

## Define deduplication on a match entity

1. Select **Set entities**. In case deduplication rules are already created, select **Edit**.

1. In the **Merge preferences** pane, choose the entities you want to run deduplication on.

   1. Specify how to combine the duplicate records and choose one of three options:
      - **Most filled**: Identifies the record with most populated attribute fields as the winner record. It's the default merge option.
      - **Most recent**: Identifies the winner record based on the most recency. Requires a date or a numeric field to define the recency.
      - **Least recent**: Identifies the winner record based on the least recency. Requires a date or a numeric field to define the recency.

   1. Optionally, to define deduplication rules on individual attributes of an entity, select **Advanced**. For example, you can choose to keep the most recent email AND the most complete address from different records. Expand the entity to see all its attributes and define which option to use for individual attributes. If you choose a recency-based option, you also need to specify a date/time field that defines the recency.

   1. Select **Done**.

1. Once the entities are selected and their merge preference is set, select **Add rule** to define the deduplication rules at an entity level.
   - **Select field**: Choose from the list of available fields from the entity that you want to check for duplicates. Choose fields that are likely unique for every single customer. For example, an email address, or the combination of name, city, and phone number.
   - **Normalize**: Select from following normalization options for the selected attributes.
     - Numerals: Converts other numeral systems, such as Roman numerals, to Arabic numerals. *VIII* becomes *8*.
     - Symbols: Removes all symbols and special characters. *Head&Shoulder* becomes *HeadShoulder*.
     - Text to lower case: Converts all character to lower case. *ALL CAPS and Title Case* becomes *all caps and title case*.
     - Type (Phone, Name, Address, Organization): Standardizes names, titles, phone numbers, addresses, etc.
     - Unicode to ASCII: Converts unicode notation to ASCII characters. */u00B2* becomes *2*.
     - Whitespace: Removes all spaces. *Hello   World* becomes *HelloWorld*.
   - **Precision**: Set the level of precision to apply for this condition.
     - **Basic**: Choose from *Low*, *Medium*, *High*, and *Exact*. Select **Exact** to only match records that match 100 percent. Select one of the other levels to match records that aren't 100 percent identical.
     - **Custom**: Set a percentage that records need to match. The system will only match records passing this threshold.
   - **Name**: Name for the rule.

1. Optionally, add more conditions to the rule.

1. Optionally, [add exceptions to the rule](#add-exceptions-to-a-rule).

1. Select **Done** to finalize the rule. The deduplication stats will display after the unification process is complete and run.

1. After defining the deduplication rules, select **Next**.

## Deduplication output as an entity

The deduplication process creates a new entity for every entity from the match pairs to identify the deduplicated records. These entities can be found along with the **ConflationMatchPairs:CustomerInsights** in the **System** section in the **Entities** page, with the name **Deduplication_DataSource_Entity**.

A deduplication output entity contains the following information:

- IDs / Keys
  - Primary key field and its alternate IDs field. Alternate IDs field consists of all the alternate IDs identified for a record.
  - Deduplication_GroupId field shows the group or cluster identified within an entity that groups all the similar records based on the specified deduplication fields. It's used for system processing purposes. If there are no manual deduplication rules specified and system defined deduplication rules apply, you may not find this field in the deduplication output entity.
  - Deduplication_WinnerId: This field contains the winner ID from the identified groups or clusters. If the Deduplication_WinnerId is same as the Primary key value for a record, it means that the record is the winner record.
- Fields used to define the deduplication rules.
- Rule and Score fields to denote which of the deduplication rules got applied and the score returned by the matching algorithm.
