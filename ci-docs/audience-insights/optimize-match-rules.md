---
title: "Optimize match rules"
description: "Match entities to create unified customer profiles."
ms.date: 02/07/2022

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

# Optimize match rules

## Change the entity order in match rules

You can reorder entities for match rules to change the order in which they’re processed. Rules that are conflicting because of a changed order will be removed. You have to recreate removed rules with an updated configuration.

1. Go to **Data** > **Unify** > **Match** and select **Edit**.

1. In the **Edit rule** pane, select the **Move up/down** control or drag and drop entities to change the order.

   :::image type="content" source="media/reorder-match-rules.png" alt-text="Options to change in which order entities are processed in the match phase.":::

1. Select **Done** to save the rule.

1. Running the match process now groups the records based on the conditions defined in the deduplication rules. After grouping the records, the merge policy is applied to identify the winner record.

1. This winner record is then passed on to the cross-entity matching, along with the non-winner records (for example, alternate IDs) to improve the matching quality.

1. Any custom match rules defined overwrite deduplication rules. If a deduplication rule identifies matching records, and a custom match rule is set to never match those records, then these two records won't be matched.

## Manage match rules

You can reconfigure and fine-tune most of the match parameters.

:::image type="content" source="media/match-rules-management.png" alt-text="Screenshot of the dropdown menu with match rule options.":::

- **Change the order of your rules** if you defined multiple rules. You can reorder the match rules by selecting the **Move Up** and **Move Down** options or by drag and drop.

- **Change rule conditions** by selecting **Edit** and choose different fields.

- **Deactivate a rule** to retain a match rule while excluding it from the matching process.

- **Duplicate your rules** if you've defined a match rule and would like to create a similar rule with modifications, select **Duplicate**.

- **Delete a rule** by selecting the **Delete** symbol.

## Advanced options

### Add exceptions to a rule

In most cases, the entity matching leads to unique user profiles with consolidated data. To dynamically address rare cases of false positives and false negatives, you can define exceptions for a match rule. Exceptions are applied after processing the match rules and avoid matching of all records, which fulfill the exception criteria.

For example, if your match rule combines last name, city, and date of birth, the system would identify twins with the same last name who live in the same town as the same profile. You can specify an exception that doesn't match the profiles if the first name in the entities you combine aren’t the same.

1. Go to **Data** > **Unify** > **Match** and select **Edit** on the rule you want to add conditions to.

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

1. Go to **Data** > **Unify** > **Match** and select **Custom match** in the **Matched records details** section.

   :::image type="content" source="media/custom-match-create.png" alt-text="Screenshot of the match rules section with Custom match control highlighted.":::

1. In the **Custom** pane, go to the **Records** tab.

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

1. After uploading the files and entities are available, select the **Custom match** option again. You'll see options to specify the entities you want to include. Select the required entities from the dropdown menu and select **Done**.

   :::image type="content" source="media/custom-match-overrides.png" alt-text="Screenshot of the dialog to choose overrides for a custom match scenario.":::

1. Applying the custom match depends on the match option you want to use. 

   - For **Always match** or **Never match**, proceed to the next step.
   - For **Custom bypass** or **Alias mapping**, select **Edit** on an existing match rule or create a new rule. In the Normalizations dropdown, choose the **Custom bypass** or **Alias mapping** option and select **Done**.

1. Select **Save** on the **Match** page to apply the custom match configuration.

1. Select **Run** on the **Match** page to start the matching process. Other specified match rules are overridden by the custom match configuration.

#### Known issues

- Self-conflation doesn't show the normalized data in deduplication entities. However, it applies the normalization internally during deduplication. It's by design for all normalizations. 
- If the semantic type setting is removed in the **Map** phase when a match rule uses Alias mapping or Custom bypass, the normalization won't be applied. It only happens if you clear the semantic type after configuring the normalization in the match rule because the semantic type will be unknown.
