---
title: "Match entities for data unification"
description: "Match entities to create unified customer profiles."
ms.date: 03/09/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: v-wendysmith
ms.author: v-wendysmith
ms.reviewer: v-wendysmith
manager: shellyha
searchScope: 
  - ci-match
  - ci-merge
  - ci-map
  - customerInsights
---

# Match conditions

This step in customer or account unification defines the match order and rules for cross-entity matching.

## Include enriched entities (preview)

If you enriched entities on the data source level to help improve your unification results, select them. For more information, see [Enrichment for data sources](data-sources-enrichment.md). If you selected enriched entities on the **Duplicate records** page, you do not need to select them again.

1. On the **Matching conditions** page, select **Use enriched entities** at the top of the page.

1. From the **Use enriched entities** pane, choose one or more enriched entities.

1. Select **Done**.

## Specify the match order

Each match unifies two or more entities into a single, consolidated entity. At the same time, it keeps the unique customer records. The match order indicates the order in which the system tries to match the records.

> [!IMPORTANT]
> The entity that you choose as your primary entity will serve as the basis for your unified profiles dataset. Additional entities that are selected will be added to this entity. This doesn't mean that the unified entity will include *all* of the data included in this entity.
>
> Important considerations:
>
> - Choose the entity with the most complete and reliable profile data about your customers as primary entity.
> - Choose the entity that has several attributes in common with other entities (for example, name, phone number, or email address) as primary entity.

1. On the **Matching conditions** page, drag and drop entities in the order you want, or use the move up and down arrows. For example, select **eCommerce:eCommerceContacts** as the primary entity and **LoyaltyScheme:loyCustomers** as the second entity.

1. To have every record in the entity as a unique customer and matched to every following entity, select **Include all records**.
  
The primary entity *eCommerce:eCommerceContacts* is matched with the next entity *LoyaltyScheme:loyCustomers*. The dataset that results from the first match step is matched with the following entity if you’ve more than two entities.

:::image type="content" source="media/m3_match.png" alt-text="Screenshot of the selected match order for the entities." lightbox="media/m3_match.png":::

## Define rules for match pairs

Match rules specify the logic by which a specific pair of entities will be matched. A rule consists of one or more conditions.

The warning next to an entity name means that no match rule is defined for a match pair.

1. Select **Add rule** for an entity to define match rules.

1. In the **Create rule** pane, configure the conditions for the rule.

   :::image type="content" source="media/m3_create_rule.png" alt-text="Screenshot of Create rule pane.":::

   - **Select Entity/Field (first row)**: Choose a related entity and an attribute to specify a record property that is likely unique to a customer. For example, a phone number or email address. Avoid matching by activity-type attributes. For example, a purchase ID will likely find no match in other record types.

   - **Select Entity/Field (second row)**: Choose an attribute that relates to the attribute of the entity specified in the first row.

   - **Normalize**: Select from following normalization options for the selected attributes.
     - **Numerals**: Converts other numeral systems, such as Roman numerals, to Arabic numerals. *VIII* becomes *8*.
     - **Symbols**: Removes all symbols and special characters. *Head&Shoulder* becomes *HeadShoulder*.
     - **Text to lower case**: Converts all character to lower case. *ALL CAPS and Title Case* becomes *all caps and title case*.
     - **Type (Phone, Name, Address, Organization)**: Standardizes names, titles, phone numbers, addresses, and organizations.
     - **Unicode to ASCII**: Converts unicode notation to ASCII characters. */u00B2* becomes *2*.
     - **Whitespace**: Removes all spaces. *Hello   World* becomes *HelloWorld*.

   - **Precision**: Set the level of precision to apply for this condition.
     - **Basic**: Choose from *Low*, *Medium*, *High*, and *Exact*. Select **Exact** to only match records that match 100 percent. Select one of the other levels to match records that aren't 100 percent identical.
     - **Custom**: Set a percentage that records need to match. The system will only match records passing this threshold.

   - **Name**: Name for the rule.

1. To match entities only if attributes meet multiple conditions, select **Add condition** to add more conditions to a match rule. Conditions are connected with a logical AND operator and thus only executed if all conditions are met.

1. Optionally, [add exceptions](/match-entities.md#add-exceptions-to-a-rule) to the rule.

1. Select **Done** to finalize the rule.

1. Optionally, [add more rules](#add-rules-to-a-match-pair).

### Add rules to a match pair

Match rules represent sets of conditions. To match entities by conditions based on multiple attributes, add more rules.

1. Select **Add rule** on the entity you want to add rules to.

1. Follow the steps in [Define rules for match pairs](#define-rules-for-match-pairs).

> [!NOTE]
> The order of rules matters. The matching algorithm tries to match on the basis of your first rule and continues to the second rule only if no matches were identified with the first rule.

## Preview rule results

Review the rules of a match pair to see the percentage of successfully matched records at the rule level.

1. Select the vertical ellipsis (...) on a rule and then select **Match preview** to view all records on the rule level. We recommend that you take a look at some records to validate that they were matched correctly.

1. Try different precision thresholds on conditions to find the optimal value.

   1. Select the vertical ellipsis (...) for the rule that you want to experiment with and select **Edit**.

   1. Change the precisions values in the conditions you want to revise.

   1. Select **Preview** to see the number of matched and unmatched records for the selected condition.

1. Try [Advanced options](#advanced-options) to make additional changes.

1. When you are satisfied with the results for the rules, select **Next**.

> [!div class="nextstepaction"]
> [Next step: Unify fields](merge-entities.md)

## Advanced options

### Add exceptions to a rule

In most cases, the entity matching leads to unique user profiles with consolidated data. To dynamically address rare cases of false positives and false negatives, you can define exceptions for a match rule. Exceptions are applied after processing the match rules and avoid matching of all records, which fulfill the exception criteria.

For example, if your match rule combines last name, city, and date of birth, the system would identify twins with the same last name who live in the same town as the same profile. You can specify an exception that doesn't match the profiles if the first name in the entities you combine aren’t the same.

1. Select **Edit** on the rule you want to add conditions to.

1. In the **Edit rule** pane, select **Add exception**.

1. Specify the exception criteria.

1. Select **Done** so save the rule.

### Specify custom match conditions

You can specify conditions that override the default match logic. There are four options available:

|Option  |Description |Example  |
|---------|---------|---------|
|Always match     | Defines values that are always matched.         |  Always match *Mike* and *MikeR*.       |
|Never match     | Defines values that never match.        | Never match *John* and *Jonathan*.        |
|Custom bypass     | Defines values that the system should always ignore in the match phase. |  Ignore the values *11111* and *Unknown* during match.        |
|Alias mapping    | Defining values that the system should consider as the same value.         | Consider *Joe* to be equal to *Joseph*.        |

1. Select **Custom**.

1. Choose the custom match option from the **Custom type** dropdown and select **Download template**. You need a separate template for each match option.

1. Open the downloaded template file and fill in the details. The template contains fields to specify the entity and the entity primary key values to be used in the custom match. For example, if you want primary key *12345* from *Sales* entity to always match with primary key *34567* from *Contact* entity, fill in the template:
    - Entity1: Sales
    - Entity1Key: 12345
    - Entity2: Contact
    - Entity2Key: 34567

   The same template file can specify custom match records from multiple entities.

   If you want to specify custom matching for deduplication on an entity, provide the same entity as both Entity1 and Entity2 and set the different primary key values.

1. After adding all the overrides, save the template file.

1. Go to **Data** > **Data sources** and ingest the template files as new entities.

1. After uploading the files and entities are available, select the **Custom** option again. You'll see options to specify the entities you want to include. Select the required entities from the dropdown menu and select **Done**.

   :::image type="content" source="media/custom-match-overrides.png" alt-text="Screenshot of the dialog to choose overrides for a custom match scenario.":::

1. Applying the custom match depends on the match option you want to use.

   - For **Always match** or **Never match**, proceed to the next step.
   - For **Custom bypass** or **Alias mapping**, select **Edit** on an existing match rule or create a new rule. In the Normalizations dropdown, choose the **Custom bypass** or **Alias mapping** option and select **Done**.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
