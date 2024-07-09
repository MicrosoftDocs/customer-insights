---
title: "Data unification best practices"
description: "Learn about the concepts and best practices when unifying data in Customer Insights - Data."
ms.date: 07/09/2024
ms.reviewer: v-wendysmith
ms.topic: conceptual
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Data unification best practices

When you set up rules to unify your data into a customer profile, consider these best practices:

- [**Avoid creating too many rules**](#unification-performance). Too many rules provide diminishing returns but increase processing time.

- [**Add rules progressively and track the results**](#unification-performance). Remove rules that don’t improve the match result.

- [**Deduplicate](#deduplication) each table** so that every customer is represented in a single row.

- **Use [normalization](#normalization) to standardize variations** in how data was entered such as Street vs. St vs. St. vs. st.

- **Use [fuzzy matching](#fuzzy-matching) to correct typos and errors** in how data was entered such as bob@contoso.com and bob@contoso.cm.

- **Narrow the scope of matches with [exact match](#exact-match)**. Make sure every rule with fuzzy conditions has at least one exact match condition.

- **Don’t match columns that contain heavily repeated data**. Make sure fuzzy-matched columns don’t have values repeated frequently, such as a form’s default value of "Firstname."

## Unification performance

Each rule takes time to run. Patterns such as comparing every table to every other table using every rule pattern makes your unification plan take hours longer to run. It also returns few if any more matches over a plan that compares each table to a base table.  

The best approach is to start with a basic set of rules you know are needed, such as comparing each table to your primary table. Your primary table should be the table with the most complete and accurate data. This table should be ordered at the top in the Matching rules unification step.  

Progressively add several rules and see how long the changes take to run, and if your results improve. Go to **Settings** > **System** > **Status** and select Match to see how long Match took for each unification run.

View the rule statistics on the Deduplication and Match pages to see if the number of Unique records changes. If a new rule matches some records, and the unique record count doesn't change, then a previous rule identified those matches.

## Deduplication

Use deduplication rules to remove duplicate customer records within a table so that a single row in each table represents each customer. A good rule identifies a unique customer.

In this simple example, records 1, 2 and 3 share either an email or phone, and represent the same person.

|ID  |Name |Phone |Email |
|----|-----|------|------|
|1 |Person 1 |(425) 555-1111 |AAA@A.com |
|2 |Person 1 |(425) 555-1111 |BBB@B.com |
|3 |Person 1 |(425) 555-2222 |BBB@B.com |
|4 |Person 2 |(206) 555-9999 |Person2@contoso.com|

We don’t want to match on just name as that would match different people with the same name.

- Create Rule 1 using Name and Phone, which matches records 1 and 2.

- Create Rule 2 using Name and Email, which matches records 2 and 3.

The combination of Rule 1 and Rule 2 creates a single match group because they share record 2.

You decide the number of rules, and the conditions that uniquely identify your customers. The exact rules depend on the data you have available to match on, the quality of your data, and how exhaustive you want the deduplication process to be.

## Winner and alternate records

Once rules are run and duplicate records are identified, the deduplication process selects a "Winner row." The nonwinner rows are called "Alternate rows." Alternate rows are used in the Matching rules unification step to match records from other tables to the winner row. Rows are matched against the data in the alternate rows in addition to the winner row.

Once you add a rule to a table, you can configure which row to select as the winner row through **Merge preferences**. Merge preferences are set per table. No matter what merge policy is selected, if there's a tie for a winner row, then first row in the data order is used as the tie breaker.

## Normalization

Use normalization to standardize data for better matching. Normalization performs well on large sets of data. 

The normalized data is only used for comparison purposes to match customer records more effectively. It doesn't change the data in the final unified customer profile output.


| Normalization       | Examples               |
| ------------------- | ---------------------- |
| Numerals            | Converts Unicode representations of numbers to the number.<br>Examples: ❽ and Ⅷ are both normalized to the number 8.<br>Note: The symbols must be encoded in Unicode Point Format.  |
| Symbols             | Removes symbols and special characters.<br>Examples: !?"#$%&'( )+,.-_/:;<=>@^_\~{}`[ ]     |
| Text to lower case  | Converts upper case characters to lower case. <br>Example: "THIS Is aN EXamplE" is converted to "this is an example"   |
| Type – Phone        | Converts phones in various formats to digits, and accounts for variations in how country codes and extensions are presented. <br>Example: +01 425.555.1212 = 1 (425) 555-1212  |
| Type - Name         | Converts over 500 common name variations and titles. <br>Examples: "debby" -> "deborah" "prof" and "professor" -> "Prof." |
| Type - Address      | Converts common parts of addresses <br>Examples: "street" -> "st" and "northwest" -> "nw"  |
| Type - Organization | Removes around 50 company name "noise words" such as "co," "corp," "corporation," and "ltd."  |
| Unicode to ASCII    | Converts Unicode characters to their ASCII letter equivalent <br>Example: The characters 'à,' 'á,' 'â,' 'À,' 'Á,' 'Â,' 'Ã,' 'Ä,' 'Ⓐ,' and 'Ａ' are all converted to 'a.'  |
| Whitespace          | Removes all white space         |
| Alias mapping       | Allows you to upload a custom list of string pairs that can then be used to indicate strings that should always be considered an exact match. <br>Use alias mapping when you have specific data examples you think should match, and aren't matched using one of the other normalization patterns. <br>Example: Scott and Scooter, or IBM and International Business Machines. |
| Custom bypass       | Allows you to upload a custom list of strings that can then be used to indicate strings that should never be matched.<br>Custom bypass is useful when you have data that has common values that should be ignored, such as a dummy phone number or dummy email. <br>Example: Never match the phone 555-1212, or test@example.com   |

## Exact match

Use precision to determine how close two strings should be to be considered a match. The default precision setting requires an exact match. Any other value enables fuzzy matching for that condition.

Precision can be set to low (30% match), medium (60% match), and high (80% match). Or you can customize and set the precision in 1% increments.

### Exact match conditions

The exact match conditions are run first to obtain a smaller set of values to fuzzy match. To be effective, the exact matching conditions should have a reasonable degree of uniqueness. For example, if all your customers live in the same country, then having an exact match on country wouldn't help narrow the scope.

Columns like full name, email, phone, or address fields have good uniqueness and are great columns to use as an exact match. 

Ensure the column you use for an exact match condition don’t have any values that are repeated frequently, such as a default value of "Firstname" captured by a form. Customer insights can profile data columns to provide insight into top repeating values. You can enable data profiling on Azure Data Lake (using Common Data Model or Delta format) connections and Synapse. Data profile is run when the data source is next refreshed. For more information, go to Data profiling.

## Fuzzy matching

Use fuzzy matching to match strings that are close but aren’t exact because of typos or other small variations. Use fuzzy matching strategically as it slows down processing and can result in timeouts. Make sure at least one exact match condition in any rule that has fuzzy conditions.  

Fuzzy matching isn't intended to capture name variations like Suzzie and Suzanne. These variations are better captured with the Normalization pattern **Type: Name** or the custom **Alias matching** where customers can enter their own list of name variations they want to consider as matches.

You can add conditions to a rule, such as matching FirstName and Phone. Conditions within a given rule are "AND" conditions; every condition must match for the rows to match. But separate rules are "OR" conditions. If Rule 1 doesn't match rows, then the rows are compared to Rule 2.

> [!NOTE]
> Only string data type columns can use fuzzy matching. For columns with other data types such as integer, double, or datetime, the precision field is set to exact match and is read only.

### Fuzzy matching calculations

Fuzzy matches are made by computing the edit distance score for two strings. If the score meets or exceeds the precision threshold, then the strings are considered a match.

The edit distance is the number of edits required to turn one string into another string, by adding, deleting, or changing a character.

For example, the strings "Jacqueline" and "Jaclyne" have an edit distance of five when we remove the q, u, e, i, and e characters, and insert the y character.

The basic calculation to determine the edit distance score is: (Base string length – Edit Distance) / Base string length.

|Base string |Comparison string |Score |
|----|-----|------|
|Jacqueline |Jaclyne |(10-4)/10=.6 |
|fred@gmail.com |fred@gmal.cm |(14-2) / 14 = 0.857 |
|franklin |frank |(8-3) / 8 = 0.625 |


[!INCLUDE[footer-include](includes/footer-banner.md)]