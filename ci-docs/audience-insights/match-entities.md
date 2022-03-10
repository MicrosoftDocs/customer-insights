---
title: "Match entities for data unification"
description: "Match entities to create unified customer profiles."
ms.date: 03/09/2022

ms.subservice: audience-insights
ms.topic: tutorial
author: adkuppa
ms.author: adkuppa
ms.reviewer: mhart
manager: shellyha
searchScope: 
  - ci-match
  - ci-merge
  - ci-map
  - customerInsights
---

# Match entities

TThis step in customer or account unification defines the match order and rules for cross-entity matching.

## Include enriched entities (preview)

If you already included enriched entities during the deduplication step, you can skip this section.

If you enriched entities on the data source level to help improve your unification results, select them. For more information, see [Enrichment for data sources](data-sources-enrichment.md).

1. Select **Use enriched entities** at the top of the page.

1. From the **Use enriched entities** pane, choose one or more enriched entities.

1. Select **Apply**.

## Specify the match order

Each match unifies two or more entities into a single, consolidated entity. At the same time, it keeps the unique customer records. The match order indicates the order in which the system tries to match the records.

> [!IMPORTANT]
> The entity that you choose as your primary entity will serve as the basis for your unified profiles dataset. Additional entities that are selected during the match phase will be added to this entity. This doesn't mean that the unified entity will include *all* of the data included in this entity.
>
> There are two considerations that can help you choose the hierarchy of your entities:
>
> - Choose the entity with the most complete and reliable profile data about your customers as primary entity.
> - Choose the entity that has several attributes in common with other entities (for example, name, phone number, or email address) as primary entity.

1. Select **Entity order**. For example, select **eCommerce:eCommerceContacts** as the primary entity and **LoyaltyScheme:loyCustomers** as the second entity.

1. To have every record in the entity as a unique customer and matched to every following entity, select **Include all records**.

1. Select **Done**.

After specifying the match order, the defined match pairs display in the **Matched records details** section. The key metrics are empty until the match process completes.

:::image type="content" source="media/match-page.png" alt-text="Screenshot of the Match page in the Unify area of the data unification process.":::
  
The primary entity *eCommerce:eCommerceContacts* is matched with the next entity *LoyaltyScheme:loyCustomers*. The dataset that results from the first match step is matched with the following entity if you’ve more than two entities.

## Define rules for match pairs

Match rules specify the logic by which a specific pair of entities will be matched. A rule consists of one or more conditions.

The **Needs rules** warning next to an entity name suggests that no match rule is defined for a match pair.

:::image type="content" source="media/match-rule-add.png" alt-text="Screenshot of the Matched record details section with control to add rules highlighted.":::

1. Select **Add rule** under an entity in the **Matched records details** section to define match rules.

1. In the **Create rule** pane, configure the conditions for the rule.

   :::image type="content" source="media/match-rule-conditions.png" alt-text="Screenshot of an opened match rule with conditions added.":::

   - **Entity/Field (first row)**: Choose a related entity and an attribute to specify a record property that is likely unique to a customer. For example, a phone number or email address. Avoid matching by activity-type attributes. For example, a purchase ID will likely find no match in other record types.

   - **Entity/Field (second row)**: Choose an attribute that relates to the attribute of the entity specified in the first row.

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

1. Provide a **Name** for the rule.

1. To match entities only if attributes meet multiple conditions, select **Add condition** to add more conditions to a match rule. Conditions are connected with a logical AND operator and thus only executed if all conditions are met.

1. Select **Done** to finalize the rule.

1. Optionally, [add more rules](#add-rules-to-a-match-pair).

1. Select **Save** to apply your changes.

### Add rules to a match pair

Match rules represent sets of conditions. To match entities by conditions based on multiple attributes, add more rules.

1. Select **Add rule** on the entity you want to add rules to.

2. Follow the steps in [Define rules for match pairs](#define-rules-for-match-pairs).

> [!NOTE]
> The order of rules matters. The matching algorithm tries to match on the basis of your first rule and continues to the second rule only if no matches were identified with the first rule.

## Run the match process

With configured match rules, including cross-entity matching and deduplication rules, you can run the match process.

Select **Run** to start the process. The matching algorithm takes some time to complete and you can't change the configuration until it completes. To make changes, you can cancel the run. Select the status of the job and select **Cancel job** on the **Progress details** pane.

You'll find the result of a successful run, the unified customer profile entity, on the **Entities** page. Your unified customer entity is called **Customers** in the **Profiles** section. The first successful match run creates the unified *Customer* entity. All subsequent match runs expand that entity.

[!INCLUDE [progress-details-include](../includes/progress-details-pane.md)]

## Review and validate your matches

Evaluate the quality of your match pairs and refine them if necessary.

The tiles on top of the page show key metrics, summarizing the number of matched records and duplicates.

:::image type="content" source="media/match-KPIs.png" alt-text="Cropped screenshot of the key metrics on the Match page with numbers and details.":::

- **Unique source records** shows the number of individual source records that were processed in last match run.
- **Matched and non-matched records** highlights how many unique records remain after processing the match rules.
- **Matched records only** shows the number of matches across all of your match pairs.

You can assess the results of each match pair and its rules in the **Matched records details** table. Compare the number of records that came from a match pair against the percentage of successfully matched records.

Review the rules of a match pair to see the percentage of successfully matched records at the rule level. Select the ellipsis (...) and then select **Match preview** to view all these records on the rule level. We recommend that you take a look at some records to validate that they were matched correctly.

Try different precision thresholds on conditions to find the optimal value.

  1. Select the ellipsis (...) for the rule that you want to experiment with and select **Edit**.

  2. Change the precisions values in the conditions you want to revise.

  3. Select **Preview** so see the number of matched and unmatched records for the selected condition.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
