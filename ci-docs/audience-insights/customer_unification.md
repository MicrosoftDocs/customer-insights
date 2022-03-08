---
title: "Map, match, and merge customer data for unification"
description: "Go through the data unification process with your customer data to create a single unified customer profile"
ms.date: 03/02/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: adkuppa
ms.author: adkuppa
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-map
  - ci-match
  - customerInsights
---

# Unify customer data

<!--- Add intro --->

## Select source fields

1. Go to **Data** > **Unify**.

1. For Source fields, select **Get started**.

1. Select the customer data **Entities** to combine into a customer profile.

1. For each entity, identify the columns you want to combine and reconcile. These columns are called *Attributes*. You can select the required attributes individually from an entity or include all attributes from an entity by selecting the **Include all fields** checkbox on the entity level. You can search on keywords across all attributes and entities to select the required attributes you want to map.

   <!--- Insert screenshot --->

   In this example, we're adding the **eCommerceContacts** and **loyCustomers** entities. By choosing these entities, you can derive insights on which of the online business customers are loyalty program members.

1. Select **Apply** to confirm your selections. The selected entities and attributes display.

### Select primary key and semantic type for attributes

<!--- Insert screenshot --->

1. Choose the **Primary key** for each entity. The primary key is an attribute unique to the entity. For an attribute to be a valid primary key, it shouldn't include duplicate values, missing values, or null values. String, integer, and GUID data type attributes are supported as primary keys.

1. For each attribute, choose a semantic type that best describes that attribute, such as name, city, or email address.

   > [!NOTE]
   > One field should map to the semantic type Person.FullName to populate the customer name in customer card. Otherwise, the customer cards will appear nameless.

   1. To use AI models for smart prediction of semantics, save time and improve accuracy, turn on **Intelligent mapping**. Intelligent mapping highlights AI-based semantics recommendation in the **Type** field. You can select any semantic type from the available list of options and override the suggested selection.
  
   1. To change an attribute type identified by the system, add a custom semantic type. Select the type field for an attribute, and type your custom semantic type name.

   1. To add an attribute thant contains a URL to profile images or logos, select the entity and field that contains the URL. In the **Type** input field, enter the following:
      - For a person: Person.ProfileImage
      - For an organization: Organization.LogoImage

   1. For an organization (preview) attribute, enter the attribute type "Organization.Name".

1. For attributes where a semantic type is automatically identified, review these attributes and types as they'll be used to combine your entities. These attributes are listed under **Review mapped fields**.

1. For attributes that aren't automatically mapped to a semantic type, select a semantic type field, or enter your custom attribute-type name. These attributes are listed under **Define the data in the unmapped fields**.

1. Click **Next**.

## Remove duplicates

Deduplication occurs when matching records. It identifies duplicate records and merges them into one record. Source records get linked to the merged record with alternate IDs.

Specifying deduplication rules isn't mandatory. If no such rules are configured, the system-defined rules are applied. They combine all records into a single record before passing the entity data to cross-entity matching for enhanced performance.

### Include enriched entities (preview)

If you enriched entities on the data source level, select them before running the match process. The enriched entities can improve your unification results. For more information, see [Enrichment for data sources](data-sources-enrichment.md). 

1. Select **Use enriched entities** at the top of the page.

1. From the **Use enriched entities** pane, choose one or more enriched entities.

1. Select **Apply**.

### Define deduplication on a match entity

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

## Match conditions

Define the rules for the matching process.

### Specify the match order

Each match unifies two or more entities into a single, consolidated entity. At the same time, it keeps the unique customer records. The match order indicates the order in which the system tries to match the records.

> [!IMPORTANT]
> The entity that you choose as your primary entity will serve as the basis for your unified profiles dataset. Additional entities that are selected during the match phase will be added to this entity. This doesn't mean that the unified entity will include *all* of the data included in this entity.
>
> There are two considerations that can help you choose the hierarchy of your entities:
>
> - Choose the entity with the most complete and reliable profile data about your customers as primary entity.
> - Choose the entity that has several attributes in common with other entities (for example, name, phone number, or email address) as primary entity.

### Add exceptions to a rule

In most cases, the entity matching leads to unique user profiles with consolidated data. To dynamically address rare cases of false positives and false negatives, you can define exceptions for a match rule. Exceptions are applied after processing the match rules and avoid matching of all records, which fulfill the exception criteria.

For example, if your match rule combines last name, city, and date of birth, the system would identify twins with the same last name who live in the same town as the same profile. You can specify an exception that doesn't match the profiles if the first name in the entities you combine aren’t the same.

### Deduplication output as an entity

The deduplication process creates a new entity for every entity from the match pairs to identify the deduplicated records. These entities can be found along with the **ConflationMatchPairs:CustomerInsights** in the **System** section in the **Entities** page, with the name **Deduplication_DataSource_Entity**.

A deduplication output entity contains the following information:
- IDs / Keys
  - Primary key field and its alternate IDs field. Alternate IDs field consists of all the alternate IDs identified for a record.
  - Deduplication_GroupId field shows the group or cluster identified within an entity that groups all the similar records based on the specified deduplication fields. It's used for system processing purposes. If there are no manual deduplication rules specified and system defined deduplication rules apply, you may not find this field in the deduplication output entity.
  - Deduplication_WinnerId: This field contains the winner ID from the identified groups or clusters. If the Deduplication_WinnerId is same as the Primary key value for a record, it means that the record is the winner record.
- Fields used to define the deduplication rules.
- Rule and Score fields to denote which of the deduplication rules got applied and the score returned by the matching algorithm.
