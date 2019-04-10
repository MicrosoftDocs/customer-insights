---
uid: developers/articles/property-fn
title: Property function reference
author: vroha
description: Property function reference
ms.author: hakrou
ms.date: 03/29/2019
ms.service: crm-online
ms.topic: conceptual
---
# Property function reference

## Numeric Functions

Function Name |	Description
--------------|--------------
`Bin` | Places a numeric value into a set of equally sized buckets. Function returns `< lowerBound` and `>= upperBound` when the value is out of the specified range
`BinRanges` | Places a numeric value into a list of user-defined buckets

## String Functions

Function Name |	Description
--------------|-------------
`Substring`	| Returns the substring starting at a specified index, and optionally with a given length
`Split` 	| Splits a string on a delimiter and returns the specified token
`SplitAndJoin` | Splits a string on a delimiter and joins substrings, applying delimiters consequentially (one after another)
`Map` | Replaces the input string according to a set of user specified find/label pairs. If the string doesn't match any pair, it is changed to a user specified default value.
`Trim`	| Trims leading and trailing whitespaces in an input string
`Replace`	| Transforms the input string according to a list of user specified find/replace pairs. All possible replacements will be applied in the order they appear in the list. If the input string doesn't contain any of the given substrings, it keeps the original value.
`Keep`	| Keeps the values that have a partial or whole match and replaces all other values with the default value

## Raw Functions

Function Name |	Description
--------------|--------------
`GetPropertyOrDefault` | Returns property value, or default if this value cannot be obtained

### `String.Trim()`

Trims leading and trailing whitespaces in an input string. If the property cannot be found or calculated, function returns `defaultReturn`.

### Syntax

`Trim(source, defaultReturn)`

Parameter	| Description
------------|-------------
`source` |	Name of the property to use as the source string
`defaultReturn` | The value to return if the source cannot be found or calculated

### Examples

Source	| Function	| Result
--------------------|-----------|----------
`"  Microsoft   "`	| `Trim(source,  "default")`	| `Microsoft`
`"Microsoft"`		| `Trim(source,  "default")`	 | `Microsoft`
Not available	| `Trim(source,  "default")`	| `default`

### `String.Keep()`

Keeps the values that have a partial or whole match and replaces all other values with the default value.

### Syntax

`Keep(source, patternList, partialMatch, defaultReturn)`

Parameter	| Description
------------|-------------
`source`| Name of the property to use as the source string
`patternList`| List of strings to partially/wholly match against the original input
`partialMatch`| Flag for partial or whole match
`defaultReturn`| The value to return if the source cannot be found or calculated

### Remarks

Number of strings is limited to 50.
Length of each string is limited to 100.

### Examples

Source	| Function	| Result
--------------------|-----------|----------
`" MSFT "`| `Keep (source, { "SFT", "UK" }, true, "default")`| ` MSFT `
`"MSFT"`| `Keep (source, { "UK" }, true, "default")`| `default`
Not available| `Keep (source, { "ddd" }, "default")`| `default`
`" MSFT "`| `Keep (source, { "MSFT", "SF" }, false, "default")`| `default`
`"MSFT"`| `Keep (source, { "MSFT", "UK" }, false, "default")`| `MSFT`

### `Replace()`

Transforms the input string according to a list of user-specified
find/replace pairs. All possible replacements will be applied in the
order they appear in the list. If the input string doesn't contain any
of the given substrings, it keeps the original value.

### Syntax

`Replace(source, replacePairs, defaultReturn)`

Parameter	| Description
------------|-------------
`source`| Name of the property to use as the source string
`replacePairs`| List of `<Find, Replace>` string pairs, where each of the `Find` incoming strings must be unique
`defaultReturn`| The value to return if the source cannot be found or calculated

### Remarks

Number of replace pairs is limited to 100.
Length of each string is limited to 500.

### Examples

Source	| Function	| Result
--------------------|-----------|----------
`"AAabcAA"`| `Replace(source, {"abc" => "", "DDD" => "ddd"}, "defaultValue")`| `AAAA`
`"abcSAft"`| `Replace(source, { "abc" => "Micro", "Saft" => "Soft"}, "defaultValue")`| `Microsoft`
Not available| `Replace (source, { "ddd", "bbb"}, "defaultValue")`| `defaultValue`

### `Map()`

Replaces the input string according to a set of user specified find/label pairs. If the string doesn't match any pair, it is changed to a user specified default value.

### Syntax

`Map(source, replacePairs, partialMatch, defaultReturn)`

Parameter	| Description
------------|-------------
`source`| Name of the property to use as the source string
`replacePairs`| List of `<Find, Label>` string pairs, where each of the `Find` incoming strings must be unique
`partialMatch`| Flag for partial or whole match
`defaultReturn`| The value to return if the property cannot be found or calculated

### Remarks

Number of replace pairs is limited to 100.
Length of each string is limited to 500.

### Examples

Source	| Function	| Result
--------------------|-----------|----------
`"abc"`| `Map(source, {"ab" => "cde", "ddd" => "bbb"}, true, "defaultValue")`|`cde`
`"abc"`| `Map(source, { "dd" => "bbb"}, true, "defaultValue")`| `defaultValue`
`"Microsoft"`| `Map(source, { "dd" => "bbb", "Microsoft" => "MS"}, false, "defaultValue")`| `MS`
`"Microsoft"`| `Map(source, { "dd" => "bbb", "Micro" => "MS"}, false, "defaultValue")`| `defaultValue`
Not available| `Map(source, { "ddd" => "bbb"}, true, "defaultValue")`| `defaultValue`

### `Split()`

Splits a string on a delimiter and returns the specified token.

### Syntax

`Split(source, delimiter, index, defaultReturn)`

Parameter	| Description
------------|-------------
`source`| Name of the property to use as the source string
`delimiter` | A delimiter string
`Index`| The index of the token to extract after splitting (starting at 0)
`defaultReturn`| The value to return if the property cannot be found or calculated

### Remarks

`Index` is limited to 1000. If `Index` value exceeds 1000, `TooManyTokens` is returned.

### Examples

Source	| Function	| Result
--------------------|-----------|----------
`"v1, v2, v3"`| `Split(source, ",", 0, "Other")`| `v1`
`"v1, v2, v3"`| `Split(source, ",", 5, "Other")`| `Other`
Not available| `Split(source, ",", 0, "Other")`| `Other`

### `SplitAndJoin()`

Splits a string on a delimiter and joins substrings, applying delimiters consequentially (one after another).

### Syntax

`SplitAndJoin(source, delimiters, tokensToKeep, joinOn, defaultReturn)`

Parameter|Description
---------|-----------
`source`|The name of the property to use as the source string 
`delimiters`|A list of delimiter strings
`tokensToKeep`|The indexes of the tokens to extract and join after splitting, starting at 0
`joinOn`|A string on which to join tokens
`defaultReturn`|The value to return if the property cannot be found or calculated

### Remarks

Indexes are limited to 1000. If an index value exceeds 1000, the function returns `TooManyTokens`. 

### Examples

Source|Function|Result
------|--------|------
`v1,v2\|v3`|`SplitAndJoin(source, [",", "\|"], [1,2], ".", "defaultReturn")`\|`v2.v3`
`v1\|v2\|\|v3`|`SplitAndJoin(source, ["\|", "\|\|"], [1,2,3], ".", "defaultReturn")`|`v2..v3` (since the function applies the `\|` delimiter first)
`v1\|v2\|v3`|`SplitAndJoin(source, ["\|"], [1,2,3,5], ".", "defaultReturn")`\|`defaultReturn` (since 5 is an incorrect index)

### `Substring()`

Returns the substring starting at a specified index, and optionally with a given length.

### Syntax

`Substring(source, start, [length], defaultReturn)`

Parameter	| Description
------------|-------------
`source`| Name of the property to use as the source string
`start`| Zero-based position of the first character in the requested substring
`length`| Maximum number of characters in the substring
`defaultReturn`| The value to return if the property cannot be found or calculated

### Remarks

The function reads starting from the character at the `start` index until it reaches the end of the source string or the maximum number of characters requested.

Length, if specified, must be greater than 0.

### Examples

Source	| Function	| Result
--------------------|-----------|----------
`"abcd"`| `Substring(source, 1, 2, "default")`| `bc`
`"abcd"`| `Substring(source, 2, 10, "default")`| `cd`
Not available| `Substring(source, 0, 2, "default")`| `default`

### `Bin()`

Places a numeric value into a set of equally sized buckets. Function returns `< lowerBound` and `>= upperBound` when the value is out of the specified range.

### Syntax

`Bin(source, lowerBound, bucketSize, bucketCount, defaultReturn)`

Parameter	| Description
------------|-------------
`source`| Name of the property to use as the source string
`lowerBound`| Lower bound of the range to divide into buckets 
`bucketSize`| Size of each bucket. Must be a positive value
`bucketCount`| Number of buckets
`defaultReturn`| The value to return if the property cannot be read, either because it is not present or because it cannot be parsed to a double

### Examples

Source	| Function	| Result
--------------------|-----------|----------
`"25"`| `Bin(source, 0, 10, 10, "Default")`| `20 <= x < 30`
`"1000"`| `Bin(source, 0, 10, 10, "Default")`| `>= upperBound`
`"-100"`| `Bin(source, 0, 10, 10, "Default")`| `< lowerBound`
`"abc"`| `Bin(source, -100, 100, 2, "Default")`| `Default`

### `BinRanges()`

Places a numeric value into a list of buckets. Each bucket has an exclusive `upperBound` value and its inclusive lower bound is equal to the upper bound of the previous bucket. If a bucket does not have an upper bound, its upper bound is considered to be `+infinity`. There should be exactly one such bucket in the list. For the first bucket in the list, its lower bound is `-infinity`.

### Remarks

There should be at least 2 buckets in the list.

### Syntax

`BinRanges(source, buckets, defaultReturn)`

Parameter	| Description
------------|-------------
`source`| Name of the property to use as the source string
`buckets`| List of buckets
`defaultReturn` | The value to return if the property cannot be read, either because it is not present or because it cannot be parsed to a double

### Examples

Source	| Function	| Result
--------------------|-----------|----------
`"25"`| `BinRanges(source, ({upperBound: 100, label: "< 100"}, {label: ">= 100"}), "Default")`| `< 100`
`"1000"`| `BinRanges(source, ({uppperBound: 100, label: "< 100"}, {label: ">= 100"}), "Default")`| `>= 100`
`"-100"`| `BinRanges(source, ({uppperBound: 100, label: "< 100"}, {label: ">= 100"}), "Default")`| `< 100`
`"abc"`| `BinRanges(source, ({uppperBound: 100, label: "< 100"}, {label: ">= 100"}), "Default")`| `Default`

### `GetPropertyOrDefault ()`

Returns property value or default, if this value cannot be obtained

### Syntax

`GetPropertyOrDefault(source, defaultReturn)`

Parameter	| Description
------------|-------------
`source`| Name of the property to use as the source string
`defaultReturn`| The value to return if the property cannot be read, either because it is not present or because it cannot be parsed to a double

### Examples

Source	| Function	| Result
--------------------|-----------|----------
`null`| `GetPropertyOrDefault (source, "Default")`| `Default`
`"1000"`| `GetPropertyOrDefault (source, "Default")`| `1000`
`"abc"`| `GetPropertyOrDefault (source, "Default")`| `abc`
