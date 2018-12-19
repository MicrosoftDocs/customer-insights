---
layout: page
title: Define new properties

---

## Creating derived properties

Let's say you just rolled out a new firmware that captures very useful telemetry. This was a very big project that took months, including extensive reviews and careful deploy plans. Once it is out and data starts flowing in, you realized there are data quality issues.

Perhaps you spelled something wrong. Maybe different teams implemented telemetry names differently. Maybe some use milliseconds when seconds should have been used. It will take too long to deploy a new telemetry update.

In such cases you can define new properties based on existing properties. You use data transformation functions to modify the original values.

Currently, we offer the following property functions:

### String Functions

Function Name |	Description
--------------|-------------
`String.Substring`	| Returns the substring starting at the specified index, and optionally with a given length
`String.Split` 	| Splits a string on a delimiter and returns the specified token
`String.Map` | Replaces the input string according to a set of user specified original/transformed pairs. If the string doesn't match any pair, it keeps the original value.
`String.ReplaceOrDefault`	| Replaces the input string according to a set of user specified original/transformed pairs. If the string doesn't match any pair, the input is replaced by a user specified default value.
`String.MapToDefault`	| Replaces the input string according to a list of user specified strings. If the input string matches any of the specified strings or cannot be read, it is replaced by a user specified default value. If there is no match, the function returns the original string.
`String.Trim`	| Trims leading and trailing whitespaces in an input string.
`String.Filter` | Replaces the input string according to a set of user specified substring/label pairs. If the input string doesn't contain any of the specified substrings, it is changed to a user specified default value.
`String.FilterAway` | Replaces the input string according to a list of user specified substrings.  If the input string contains any of the specified substrings or cannot be read, it is replaced by a user specified default value. If there is no match, the function returns the original input string.
`String.ReplaceOrDefault`	| Replaces the input string according to a set of user specified original/transformed pairs. If the string doesn't match any pair, the input is replaced by a user specified default value.
{: .table .table-striped}

### Numeric Functions

Function Name |	Description
--------------|--------------
`Numeric.Bucket` |	Places a numeric value into a set of equally sized buckets, distributed between a lower and upper bound, and maps the remaining value into a user specified bucket.
`Numeric.BucketRanges` | Places a numeric value into a set of user specified buckets, each having a lower and upper bound.
{: .table .table-striped}

[Complete list and details of property functions](property-functions).
