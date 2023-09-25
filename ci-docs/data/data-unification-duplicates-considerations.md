---
title: "Deduplication considerations"
description: "Learn what to consider when setting up deduplication rules for customer unification."
ms.date: 09/21/2023
ms.topic: conceptual
author: Scott-Stabbert
ms.author: sstabbert
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Deduplication considerations

This article contains key considerations when setting up your deduplication rules.

In this simple example, records 1, 2 and 3 share either an email or phone, and represent the same person.

|ID  |Name |Phone |Email |
|----|-----|------|------|
|1 |Person1 |(425) 555-1111 |AAA@A.com |
|2 |Person1 |(425) 555-1111 |BBB@B.com |
|3 |Person1 |(425) 555-2222 |BBB@B.com |
|4 |Person2 |(206) 555-9999 |Person2@contoso.com|

- We don’t want to match on just name as that would match different people with the same name.
- We create Rule 1 using Name and Phone, which matches records 1 and 2.
- We create Rule 2 using Name and Email, which matches records 2 and 3.
- The combination of Rule 1 and Rule 2 creates a single match group because they share record 2.

You decide the number of rules, and the conditions that uniquely identify your customers. The exact rules depend on the data you have available to match on, the quality of your data, and how exhaustive you want the deduplication process to be.

## Deduplication rule options

You can select **Normalization** routines to standardize data to get better matching, such as when you want to ignore extra whitespace or variations in case sensitivity between two strings. Normalization only impacts matching. It doesn't change the data in the final unified customer profile output.

You can select a **Precision** setting less than "Exact" to use fuzzy matching. Fuzzy matching is effective at matching strings that are close, but not exact in order to account for typos and small variations. For example, when comparing bob@contoso.com and bob@contoso.cm.

You can add conditions to a rule, such as matching FirstName and Phone. Conditions within a given rule are "AND" conditions; every condition must match for the rows to match. But separate rules are "OR" conditions. If rows aren't matched by Rule 1, then they can be matched by Rule 2.

## Winner and alternate records

Once rules have been run and duplicate records have been identified, the deduplication process selects a "Winner row". The nonwinner rows are called "Alternate rows." Alternate rows are used in the Matching conditions unification step to match records from other tables to the winner row. Rows are matched against the data in the alternate rows in addition to the winner row.

Once you have added a rule to a table, you can configure which row to select as the winner row through **Merge preferences**. Merge preferences are set per table. No matter what merge policy is selected, if there's a tie for a winner row, then first row in the data order is used as the tie breaker. 
