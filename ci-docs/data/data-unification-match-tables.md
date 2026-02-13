---
title: "Matching rules for data unification"
description: "Match tables to create unified customer profiles."
ms.date: 12/11/2024
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Define matching rules for data unification

This step in unification defines the match order and rules for cross-table matching. This step requires at least two tables. When records are matched, they're concatenated into a single record with all the fields from each table. Alternate rows (nonwinner rows from the Deduplication step) are considered when matching. But, if a row matches an alternate row in a table, the record is matched to the winner row.

> [!NOTE]
> Once you create your match conditions and select **Next**, you cannot remove a selected table or column. If needed, select **Back** to review the selected tables and columns before continuing.

[!INCLUDE [m3-first-run-note](includes/m3-first-run-note.md)]

## Include enriched tables (preview)

If you enriched tables on the data source level to help improve your unification results, select them. For more information, see [Enrichment for data sources](data-sources-enrichment.md). If you selected enriched tables on the **Deduplication rules** page, you don't need to select them again.

1. On the **Matching rules** page, select **Use enriched tables** at the top of the page.

1. From the **Use enriched tables** pane, choose one or more enriched tables.

1. Select **Done**.

## Specify the match order

Each match unifies two or more tables into a single, consolidated table. At the same time, it keeps the unique customer records. The match order indicates the order in which the system tries to match the records.

> [!IMPORTANT]
> The first table is called the primary table, which serves as the basis for your unified profiles. Additional tables that are selected will be added to this table.
>
> Important considerations:
>
> - Choose the table with the most complete and reliable profile data about your customers as the primary table.
> - Choose the table that has several columns in common with other tables (for example, name, phone number, or email address) as the primary table.
> - Tables can only match against other tables that are higher in priority. So Table2 can only match against Table1, and Table3 can match against Table2 *or* Table1.  

1. On the **Matching rules** page, use the move up and down arrows to move the tables in the order you want, or drag and drop them. For example, select **eCommerceContacts** as the primary table and **loyCustomer** as the second table.

1. To have every record in the table as a unique customer regardless if a match is found, select **Include all records**. Any records in this table that don't match to records in any other table are included in the unified profile. Records that don't have a match are called singletons.
  
The primary table *eCommerceContacts* is matched with the next table *loyCustomer*. The dataset that results from the first match step is matched with the following table if you have more than two tables. If duplicates still exist in *eCommerceContacts*, when *loyCustomer* is matched against *eCommerceContacts*, *eCommerceContacts* duplicate rows aren't reduced to a single customer record. However, if duplicate rows in *loyCustomer* match a row in *eCommerceContacts*, they're reduced into a single customer record.

:::image type="content" source="media/m3_match.png" alt-text="Screenshot of the selected match order for the tables." lightbox="media/m3_match.png":::

## Define rules for match pairs

Match rules specify the logic by which a specific pair of tables will be matched. A rule consists of one or more conditions.

The warning next to a table name means that no match rule is defined for a match pair.

1. Select **Add rule** for a table pair to define match rules.

1. In the **Add rule** pane, configure the conditions for the rule.

   :::image type="content" source="media/m3_add_rule.png" alt-text="Screenshot of Add rule pane.":::

   - **Select Table/Field (first row)**: Choose a table and a column that is likely unique to a customer. For example, a phone number or email address. Avoid matching by activity-type columns. For example, a purchase ID will likely find no match in other record types.

   - **Select Table/Field (second row)**: Choose a column that relates to the column of the table specified in the first row.

   - **Normalize**: Select normalization options for the column.

      [!INCLUDE [normalization-include](includes/normalization.md)]

   - **Precision**: Set the level of precision to apply for this condition. [Precision is used for exact match and fuzzy matching](data-unification-best-practices.md), and determines how close two strings need to be in order to be considered a match.
     - **Basic**: Choose from *Low (30%)*, *Medium (60%)*, *High (80%)*, and *Exact (100%)*. Select **Exact** to only match records that match 100 percent.
     - **Custom**: Set a percentage that records need to match. The system will only match records passing this threshold.
   - **Name**: Name for the rule.

1. To match tables only if columns meet multiple conditions, select **Add** > **Add condition** to add more conditions to a match rule. Conditions are connected with a logical AND operator and thus only executed if all conditions are met.

1. Optionally, consider advanced options such as [exceptions](#add-exceptions-to-a-rule) or [custom match conditions](#specify-custom-match-conditions).

1. Select **Done** to finalize the rule.

1. Optionally, [add more rules](#add-rules-to-a-match-pair).

1. Select **Next**.

> [!div class="nextstepaction"]
> [Next step: View unified data](data-unification-merge-tables.md)

### Add rules to a match pair

Match rules represent sets of conditions. To match tables by conditions based on multiple columns, add more rules.

1. Select **Add rule** on the table you want to add rules to.

1. Follow the steps in [Define rules for match pairs](#define-rules-for-match-pairs).

> [!NOTE]
> The order of rules matters. The matching algorithm tries to match a given customer record on the basis of your first rule and continues to the second rule only if no matches were identified with the first rule.

## Advanced options

### Add exceptions to a rule

In most cases, the table matching leads to unique customer profiles with consolidated data. To address rare cases of false positives and false negatives, define exceptions for a match rule. Exceptions are applied after processing the match rules and avoid matching of all records, which fulfill the exception criteria.

For example, if your match rule combines last name, city, and date of birth, the system would identify twins with the same last name who live in the same town as the same profile. You can specify an exception that doesn't match the profiles if the first name in the tables you combine aren’t the same.

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
|Alias mapping    | Defines values that the system should consider as the same value.         | Consider *Joe* to be equal to *Joseph*.        |

1. Select **Custom**.

   :::image type="content" source="media/m3_match_custom.png" alt-text="Custom button":::

1. Choose the **Custom type** and select **Download template**. Rename the template without using spaces. Use a separate template for each match option.

1. Open the downloaded template file and fill in the details. The template contains fields to specify the table and the table primary key values to be used in the custom match. Table names are case sensitive. For example, if you want primary key *12345* from *Sales* table to always match with primary key *34567* from *Contact* table, fill in the template:
    - Table1: Sales
    - Table1Key: 12345
    - Table2: Contact
    - Table2Key: 34567

   The same template file can specify custom match records from multiple tables.

   If you want to specify custom matching for deduplication on a table, provide the same table as both Table1 and Table2 and set the different primary key values. You must define at least one deduplication rule to the table to use custom matching.

1. After adding all the overrides, save the template file.

1. Go to **Data** > **Data sources** and ingest the template files as new tables.

1. After uploading the files, select the **Custom** option again. Select the required tables from the dropdown menu and select **Done**.

   :::image type="content" source="media/custom-match-overrides.png" alt-text="Screenshot of the dialog to choose overrides for a custom match scenario.":::

1. Applying the custom match depends on the match option you want to use.

   - For **Always match** or **Never match**, proceed to the next step.
   - For **Bypass** or **Alias mapping**, select **Edit** on an existing match rule or create a new rule. In the Normalizations dropdown, choose the **Custom bypass** or **Alias mapping** option and select **Done**.

1. Select **Done** on the **Custom** pane to apply the custom match configuration.

   Each template file ingested is its own data source. If records are discovered that need special matching treatment, update the appropriate data source. The update will be used during the next unification process. For example, you identify twins with nearly the same name living at the same address that had been merged as one person. Update the data source to identify the twins as separate, unique records.

> [!div class="nextstepaction"]
> [Next step: View unified data](data-unification-merge-tables.md)

## Troubleshoot unification failures

### "Merge job failed" or "Match job failed. Please try again"

| Symptom | Likely cause | Resolution |
|---------|-------------|------------|
| Error on saving unification changes | Dataverse dependencies on unified columns | Go to Power Apps > Tables > find the referenced column > remove flows, views, or forms that depend on it, then retry |
| Match canceled after running for hours | Dataset too large for allocated resources | Reduce match rule complexity or contact support for scaling |
| Backstamping job skipped | Previous backstamping still running | Wait for current backstamping to complete; check progress on Unify status page |
| Backstamping takes many hours | Expected for large datasets | ~1 hour per 5M records. No action needed unless it exceeds 3x the expected duration |
| "Cannot delete data source" or "Cannot remove table from unification" | Downstream dependencies exist | Remove segments, measures, or exports that reference the table first |

### Backstamping duration expectations

| Record count | Expected backstamping time |
|-------------|---------------------------|
| < 1 million | < 30 minutes |
| 1-10 million | 30 min - 2 hours |
| 10-50 million | 2 - 10 hours |
| 50+ million | 10+ hours |

### How to resolve Dataverse dependencies

1. In Power Apps, go to **Tables** and find the table referenced in the error.
2. Select **Dependencies** to see what objects reference this table.
3. Remove or modify each dependency (flows, views, forms, other tables).
4. Return to Customer Insights - Data and retry the unification operation.

[!INCLUDE [footer-include](includes/footer-banner.md)]
