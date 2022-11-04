---
title: "Match conditions for data unification"
description: "Match entities to create unified customer profiles."
recommendations: false
ms.date: 10/07/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: v-wendysmith
ms.author: mukeshpo
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-match
  - ci-merge
  - ci-map
  - customerInsights
---

# Match conditions for data unification

This step in unification defines the match order and rules for cross-entity matching. This step requires at least two entities.

> [!NOTE]
> Once you create your match conditions and select **Next**, you cannot remove a selected entity or attribute. If needed, select **Back** to review the selected entities and attributes before continuing.

[!INCLUDE [m3-first-run-note](includes/m3-first-run-note.md)]

## Include enriched entities (preview)

If you enriched entities on the data source level to help improve your unification results, select them. For more information, see [Enrichment for data sources](data-sources-enrichment.md). If you selected enriched entities on the **Duplicate records** page, you do not need to select them again.

1. On the **Matching conditions** page, select **Use enriched entities** at the top of the page.

1. From the **Use enriched entities** pane, choose one or more enriched entities.

1. Select **Done**.

## Specify the match order

Each match unifies two or more entities into a single, consolidated entity. At the same time, it keeps the unique customer records. The match order indicates the order in which the system tries to match the records.

> [!IMPORTANT]
> The first entity is called the primary entity, which serves as the basis for your unified profiles. Additional entities that are selected will be added to this entity.
>
> Important considerations:
>
> - Choose the entity with the most complete and reliable profile data about your customers as the primary entity.
> - Choose the entity that has several attributes in common with other entities (for example, name, phone number, or email address) as the primary entity.

1. On the **Matching conditions** page, use the move up and down arrows to move the entities in the order you want, or drag and drop them. For example, select **eCommerceCustomers** as the primary entity and **loyCustomers** as the second entity.

1. To have every record in the entity as a unique customer regardless if a match is found, select **Include all records**. Any records in this entity that do not match to records in any other entity are included in the unified profile. Records that do not have a match are called singletons.
  
The primary entity *Contacts:eCommerce* is matched with the next entity *CustomerLoyalty:Loyalty*. The dataset that results from the first match step is matched with the following entity if you’ve more than two entities.

:::image type="content" source="media/m3_match.png" alt-text="Screenshot of the selected match order for the entities." lightbox="media/m3_match.png":::

## Define rules for match pairs

Match rules specify the logic by which a specific pair of entities will be matched. A rule consists of one or more conditions.

The warning next to an entity name means that no match rule is defined for a match pair.

1. Select **Add rule** for an entity pair to define match rules.

1. In the **Add rule** pane, configure the conditions for the rule.

   :::image type="content" source="media/m3_add_rule.png" alt-text="Screenshot of Add rule pane.":::

   - **Select Entity/Field (first row)**: Choose an entity and an attribute that is likely unique to a customer. For example, a phone number or email address. Avoid matching by activity-type attributes. For example, a purchase ID will likely find no match in other record types.

   - **Select Entity/Field (second row)**: Choose an attribute that relates to the attribute of the entity specified in the first row.

   - **Normalize**: Select from following normalization options for the selected attributes.
     - **Numerals**: Converts other numeral systems, such as Roman numerals, to Arabic numerals. *VIII* becomes *8*.
     - **Symbols**: Removes all symbols and special characters. *Head&Shoulder* becomes *HeadShoulder*.
     - **Text to lower case**: Converts all character to lower case. *ALL CAPS and Title Case* becomes *all caps and title case*.
     - **Type (Phone, Name, Address, Organization)**: Standardizes names, titles, phone numbers, addresses, and organizations.
     - **Unicode to ASCII**: Converts unicode notation to ASCII characters. */u00B2* becomes *2*.
     - **Whitespace**: Removes all spaces. *Hello   World* becomes *HelloWorld*.

   - **Precision**: Set the level of precision to apply for this condition.
     - **Basic**: Choose from *Low (30%)*, *Medium (60%)*, *High (80%)*, and *Exact (100%)*. Select **Exact** to only match records that match 100 percent.
     - **Custom**: Set a percentage that records need to match. The system will only match records passing this threshold.

   - **Name**: Name for the rule.

1. To match entities only if attributes meet multiple conditions, select **Add** > **Add condition** to add more conditions to a match rule. Conditions are connected with a logical AND operator and thus only executed if all conditions are met.

1. Optionally, consider advanced options such as [exceptions](#add-exceptions-to-a-rule) or [custom match conditions](#specify-custom-match-conditions).

1. Select **Done** to finalize the rule.

1. Optionally, [add more rules](#add-rules-to-a-match-pair).

1. Click **Next**.

> [!div class="nextstepaction"]
> [Next step: Unify fields](merge-entities.md)

### Add rules to a match pair

Match rules represent sets of conditions. To match entities by conditions based on multiple attributes, add more rules.

1. Select **Add rule** on the entity you want to add rules to.

1. Follow the steps in [Define rules for match pairs](#define-rules-for-match-pairs).

> [!NOTE]
> The order of rules matters. The matching algorithm tries to match a given customer record on the basis of your first rule and continues to the second rule only if no matches were identified with the first rule.

## Advanced options

### Add exceptions to a rule

In most cases, the entity matching leads to unique customer profiles with consolidated data. To address rare cases of false positives and false negatives, define exceptions for a match rule. Exceptions are applied after processing the match rules and avoid matching of all records, which fulfill the exception criteria.

For example, if your match rule combines last name, city, and date of birth, the system would identify twins with the same last name who live in the same town as the same profile. You can specify an exception that doesn't match the profiles if the first name in the entities you combine aren’t the same.

1. In the **Edit rule** pane, select **Add** > **Add exception**.

1. Specify the exception criteria.

1. Select **Done** to save the rule.

### Specify custom match conditions

Specify conditions that override the default match logic. There are four options available:

|Option  |Description |Example  |
|---------|---------|---------|
|Always match     | Defines values for the primary keys that are always matched.         |  Always match the row with primary key *12345* to the row with primary key *54321*.       |
|Never match     | Defines values for the primary keys that never match.        | Never match the row with primary key *12345* to the row with primary key *54321*.        |
|Bypass            | Defines values that the system should always ignore in the match phase. |  Ignore the values *11111* and *Unknown* during match.        |
|Alias mapping    | Defining values that the system should consider as the same value.         | Consider *Joe* to be equal to *Joseph*.        |

1. Select **Custom**.

   :::image type="content" source="media/m3_match_custom.png" alt-text="Custom button":::

1. Choose the **Custom type** and select **Download template**. Rename the template without using spaces. Use a separate template for each match option.

1. Open the downloaded template file and fill in the details. The template contains fields to specify the entity and the entity primary key values to be used in the custom match. Entity names are case sensitive. For example, if you want primary key *12345* from *Sales* entity to always match with primary key *34567* from *Contact* entity, fill in the template:
   - Entity1: Sales
   - Entity1Key: 12345
   - Entity2: Contact
   - Entity2Key: 34567

   The same template file can specify custom match records from multiple entities.

   > [!NOTE]
   > If you want to specify custom matching for deduplication on an entity, provide the same entity as both Entity1 and Entity2 and set the different primary key values. You must define at least one deduplication rule to the entity to use custom matching.

1. After adding all the overrides, save the template file.

1. Go to **Data** > **Data sources** and ingest the template files as new entities.

1. After uploading the files, select the **Custom** option again. Select the required entities from the dropdown menu and select **Done**.

   :::image type="content" source="media/custom-match-overrides.png" alt-text="Screenshot of the dialog to choose overrides for a custom match scenario.":::

1. Applying the custom match depends on the match option you want to use.

   - For **Always match** or **Never match**, proceed to the next step.
   - For **Bypass** or **Alias mapping**, select **Edit** on an existing match rule or create a new rule. In the Normalizations dropdown, choose the **Custom bypass** or **Alias mapping** option and select **Done**.

1. Select **Done** on the **Custom** pane to apply the custom match configuration.

   Each template file ingested is its own data source. If records are discovered that need special matching treatment, update the appropriate data source. The update will be used during the next unification process. For example, you identify twins with nearly the same name living at the same address that had been merged as one person. Update the data source to identify the twins as separate, unique records.

> [!div class="nextstepaction"]
> [Next step: Unify fields](merge-entities.md)

[!INCLUDE [footer-include](includes/footer-banner.md)]
