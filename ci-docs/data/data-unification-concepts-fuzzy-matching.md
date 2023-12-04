---
title: "Data unification concepts about fuzzy matching"
description: "Understand the concepts behind fuzzy matching when unifying data in Customer Insights - Data."
ms.date: 12/01/2023
ms.reviewer: v-wendysmith
ms.topic: conceptual
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Fuzzy matching

Fuzzy matching allows you to deduplicate and match string data when the data doesn’t exactly match. String data with typos and other small differences are good candidates for fuzzy matching.  

## How is fuzzy matching enabled?

Each condition in a rule has a setting called **Precision** where you select how close two strings should be to be considered a match. The default precision setting requires an exact match for the strings being compared to match. Selecting any other value for precision enables fuzzy matching for that condition.

Precision can be set to low (30% match), medium (60% match), and high (80% match). You can also select the dropdown, and change **Basic** to **Custom**, allowing you to set the precision in 1% increments.

> [!NOTE]
> Only string data type columns can use fuzzy matching. For columns with other data types such as integer, double, or datetime, the precision field is set to exact match and is read only.

## How are fuzzy matches made?

Fuzzy matches are made by computing the edit distance score for two strings. If the score meets or exceeds the precision threshold, then the strings are considered a match.  

The edit distance is the number of edits required to turn one string into another string, by adding, deleting, or changing a character.

For example, the strings “Jacqueline” and “Jaclyne” have an edit distance of 5 when we remove the ‘q’, ‘u’, ‘e’, ‘i’, ‘e’ characters, and insert the ‘y’ character.

The basic calculation to determine the edit distance score is: (Base string length – Edit Distance) / Base string length

|Base string |Comparison string |Score |
|----|-----|------|
|Jacqueline |Jaclyne |(10-5)/10=.5 |
|fred@gmail.com |fred@gmal.cm |(14-2) / 14 = 0.857 |
|franklin |frank |(8-2) / 8 = 0.75 |

## Normalization and fuzzy matching

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
| Alias mapping       | Allows you to upload a custom list of string pairs that can then be used to indicate strings that should always be considered an exact match. <br>Use alias mapping when you have specific data examples you think should match, and aren't matched using one of the other normalization patterns. <br>Example: Scott and Scooter, or IBM and International Business Machines. |
| Custom bypass       | Allows you to upload a custom list of strings that can then be used to indicate strings that should never be matched.<br>Custom bypass is useful when you have data that has common values that should be ignored, such as a dummy phone number or dummy email. <br>Example: Never match the phone 555-1212, or test@example.com                                                         |
## Performance – use exact match conditions too

Fuzzy matching is powerful, but takes more time and resources than exact matching. It is best to use data normalization as your first approach for data irregularities, and use fuzzy matching strategically.  

> [!IMPORTANT]
> Use at least one exact match condition in every rule.

The exact match conditions are run first to obtain a smaller set of values that need to be fuzzy matched. To be effective, the exact matching conditions should have a reasonable degree of uniqueness. For example, if all your customers live in the same country, then having an exact match on country would likely not help narrow the scope.

Columns like full name, email, phone or address fields have good uniqueness and are great columns to use as an exact match.

## Fuzzy matching fields with multiple values

Some fields like addresses commonly contain multiple substrings separated by spaces where Microsoft is misspelled, and the state is missing from the left address.

:::image type="content" source="media/fuzzy-matching-multi-values.png" alt-text="Fuzzy matching diagram showing the distance score and Inverse Document Frequency (IDF)":::

When multiple substrings are matched, another weight multiplier is applied based on the Inverse Document Frequency (IDF). This means that strings that are less common in your data for the specific column are given a higher weight. In this example, ‘Redmond’ and ‘98052’ are unique for the data in that column and have a multiplier of 2, while ‘Microsoft’ is highly unique and has a multiplier of 5.

The final score is computed using the Jaccard similarity coefficient where each edit distance score is multiplied by the IDF weight multiplier, added together, and then divided by the total possible score. If the final score meets or exceeds the precision threshold, then the strings are considered a match.

:::image type="content" source="media/jaccard-formula.png" alt-text="Jaccard formula":::

## Next steps

- [Deduplication concepts and scenarios](data-unification-concepts-dedpulication.md)

[!INCLUDE[footer-include](includes/footer-banner.md)]
