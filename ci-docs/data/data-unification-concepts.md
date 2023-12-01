---
title: "Data unification concepts and scenarios"
description: "Understand the concepts behind data unification in Customer Insights - Data including scenarios."
ms.date: 12/01/2023
ms.reviewer: v-wendysmith
ms.topic: conceptual
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Data unification concepts and scenarios

This article helps to explain the data unification process providing tips and examples to guide you through the process.

## Fuzzy matching

Fuzzy matching allows you to deduplicate and match string data when the data doesn’t exactly match. String data with typos and other small differences are good candidates for fuzzy matching.  

### How is fuzzy matching enabled?

When creating or editing a rule, each condition has a setting called **Precision** where you select how close two strings should be to be considered a match. The default precision setting requires an exact match for the strings being compared to match. Selecting any other value for precision enables fuzzy matching for that condition.

Precision can be set to low (30% match), medium (60% match), and high (80% match). You can also click the dropdown, and change ‘Basic’ to ‘Custom’, allowing you to set the precision in 1% increments.

> [!NOTE]
> Only string data type columns can use fuzzy matching. For columns with other data types such as integer, double, or datetime, the precision field is set to exact match and is read only.

### How are fuzzy matches made?

Fuzzy matches are made by computing the edit distance score for two strings. If the score meets or exceeds the precision threshold, then the strings are considered a match.  

The edit distance is the number of edits required to turn one string into another string, by adding, deleting, or changing a character.

For example, the strings “Jacqueline” and “Jaclyne” have an edit distance of 5 when we remove the ‘q’, ‘u’, ‘e’, ‘i’, ‘e’ characters, and insert the ‘y’ character.

The basic calculation to determine the edit distance score is: (Base string length – Edit Distance) / Base string length

|Base string |Comparison string |Score |
|----|-----|------|
|Jacqueline |Jaclyne |(10-5)/10=.5 |
|fred@gmail.com |fred@gmal.cm |(14-2) / 14 = .857 |
|franklin |frank |(8-2) / 8 = .75 |

### Normalization and fuzzy matching

Customer Insights – Data provides powerful data normalization routines that can handle many data discrepancies more efficiently than fuzzy matching. You can select one or more data normalization patterns for a column. Normalization doesn't change your data in the final output. The normalized data is only used for comparison purposes to match customer records more effectively.

| Normalization       | Examples       |
| ------------------- | -------------- |
| Numerals            | Converts Unicode representations of numbers to the number.<br>Examples: □ and Ⅷ are both normalized to the number 8.<br>Note: The symbols must be encoded in Unicode Point Format.                  |
| Symbols             | Removes the following symbols: !"#$%&'()\*+,-./:;<=>?@[\\]^_\`{|}~         |
| Text to lower case  | Converts upper case characters to lower case. <br>Example: ‘THIS Is aN EXamplE’ is converted to ‘this is an example’   |
| Type – Phone        | Converts phones in various formats to digits, and accounts for variations in how country codes and extensions are presented. <br>Example: +01 425.555.1212 = 1 (425) 555-1212        |
| Type - Name         | Converts over 500 common name variations and titles. <br>Examples: "debby" -> "deborah", "prof"  and "professor" -> "Prof."         |
| Type - Address      | Converts common parts of addresses <br>Examples: "street" -> "st", and  "northwest" -> "nw"        |
| Type - Organization | Removes around 50 company name ‘noise words’ such as "co", "corp", "corporation", and “ltd”.         |
| Unicode to ASCII    | Converts Unicode characters to their ASCII letter equivalent <br>Example: The characters 'à', 'á', 'â', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Ⓐ','Ａ'  are all converted to 'a'               |
| Whitespace          | Removes all white space         |
| Alias mapping       | Allows you to upload a custom list of string pairs that can then be used to indicate strings that should always be considered an exact match. <br>Alias mapping is use when you have specific data examples you think should match, and are not matched using one of the other normalization patterns above. <br>Example: Scott and Scooter, or IBM and International Business Machines. |
| Custom bypass       | Allows you to upload a custom list of strings that can then be used to indicate strings that should never be matched.<br>Custom bypass is useful when you have data that has common values that should be ignored, such as a dummy phone number or dummy email. <br>Example: Never match the phone 555-1212, or test@example.com                                                         |

### Performance – use exact match conditions too

Fuzzy matching is powerful, but takes more time and resources than exact matching. It is best to data normalization as your first approach to data irregularities, and use fuzzy matching strategically.  

It is also important to use at least 1 exact match condition in every rule.  The exact match conditions are run first to obtain a smaller set of values that need to be fuzzy matched.  To be effective, the exact matching conditions should have a reasonable degree of uniqueness.  For example, if all your customers live in the same country, then having an exact match on country would likely not help narrow the scope.

Columns like full name, email, phone or address fields have good uniqueness and are great columns to use as an exact match.

### Fuzzy matching fields with multiple values

Some fields like addresses commonly contain multiple substrings separated by spaces such as the example shown below where Microsoft is mis-spelled, and the state is missing from the left address.

When multiple sub-strings are matched, an additional ‘weight’ multiplier is applied based on the Inverse Document Frequency (IDF). This means that strings that are less common in your data for the specific column are given a higher weight. In this example, ‘Redmond’ and ‘98052’ are somewhat unique for the data in that column and have a multiplier of 2, while ‘Microsoft’ is highly unique and has a multiplier of 5.

The final score is computed using the Jaccard similarity coefficient where each edit distance score is multiplied by the IDF weight multiplier, added together, and then divided by the total possible score. If the final score meets or exceeds the precision threshold, then the strings are considered a match.

## Deduplication example

In this simple example, records 1, 2 and 3 share either an email or phone, and represent the same person.

|ID  |Name |Phone |Email |
|----|-----|------|------|
|1 |Person 1 |(425) 555-1111 |AAA@A.com |
|2 |Person 1 |(425) 555-1111 |BBB@B.com |
|3 |Person 1 |(425) 555-2222 |BBB@B.com |
|4 |Person 2 |(206) 555-9999 |Person2@contoso.com|

- We don’t want to match on just name as that would match different people with the same name.
- We create Rule 1 using Name and Phone, which matches records 1 and 2.
- We create Rule 2 using Name and Email, which matches records 2 and 3.
- The combination of Rule 1 and Rule 2 creates a single match group because they share record 2.

You decide the number of rules, and the conditions that uniquely identify your customers. The exact rules depend on the data you have available to match on, the quality of your data, and how exhaustive you want the deduplication process to be.

## Deduplication rule options - Normalize and Precision

You can select **Normalization** routines to standardize data to get better matching, such as when you want to ignore extra whitespace or variations in case sensitivity between two strings. Normalization only impacts matching. It doesn't change the data in the final unified customer profile output.

You can select a **Precision** setting less than "Exact" to use fuzzy matching. Fuzzy matching is effective at matching strings that are close, but not exact in order to account for typos and small variations. For example, when comparing bob@contoso.com and bob@contoso.cm.

You can add conditions to a rule, such as matching FirstName and Phone. Conditions within a given rule are "AND" conditions; every condition must match for the rows to match. But separate rules are "OR" conditions. If rows aren't matched by Rule 1, then they can be matched by Rule 2.

## Winner and alternate records

Once rules have been run and duplicate records have been identified, the deduplication process selects a "Winner row." The nonwinner rows are called "Alternate rows." Alternate rows are used in the Matching rules unification step to match records from other tables to the winner row. Rows are matched against the data in the alternate rows in addition to the winner row.

Once you have added a rule to a table, you can configure which row to select as the winner row through **Merge preferences**. Merge preferences are set per table. No matter what merge policy is selected, if there's a tie for a winner row, then first row in the data order is used as the tie breaker.
