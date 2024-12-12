| Normalization       | Examples               |
| ------------------- | ---------------------- |
| Numerals            | Converts many Unicode symbols that represent numbers to simple numbers.<br>Examples: ❽ and Ⅷ are both normalized to the number 8.<br>Note: The symbols must be encoded in Unicode Point Format.  |
| Symbols             | Removes symbols and special characters.<br>Examples: !?"#$%&'( )+,.-_/:;<=>@^_\~{}`[ ]     |
| Text to lower case  | Converts upper case characters to lower case. <br>Example: "THIS Is aN EXamplE" is converted to "this is an example"   |
| Type – Phone        | Converts phones in various formats to digits, and accounts for variations in how country codes and extensions are presented. Symbols and whitespace are ignored. Leading '0' digits in country codes are ignored, matching +1 and +01. Extensions signified by a lettered prefix are ignored (X 123). The normalized country code *is* significant, so a phone with a country code won’t match a phone without a country code. <br>Example: +01 425.555.1212 matches 1 (425) 555-1212 <br>+01 425.555.1212 won't match (425) 555-1212 |
| Type - Name         | Converts over 500 common name variations and titles. <br>Examples: "debby" -> "deborah" "prof" and "professor" -> "Prof." |
| Type - Address      | Converts common parts of addresses <br>Examples: "street" -> "st" and "northwest" -> "nw"  |
| Type - Organization | Removes around 50 company name "noise words" such as "co," "corp," "corporation," and "ltd."  |
| Unicode to ASCII    | Converts Unicode characters to their ASCII letter equivalent <br>Example: The characters 'à,' 'á,' 'â,' 'À,' 'Á,' 'Â,' 'Ã,' 'Ä,' 'Ⓐ,' and 'Ａ' are all converted to 'a.'  |
| Whitespace          | Removes all white space         |
| Alias mapping       | Allows you to upload a custom list of string pairs that can then be used to indicate strings that should always be considered an exact match. <br>Use alias mapping when you have specific data examples you think should match, and aren't matched using one of the other normalization patterns. <br>Example: Scott and Scooter, or MSFT and Microsoft. |
| Custom bypass       | Allows you to upload a custom list of strings that can then be used to indicate strings that should never be matched.<br>Custom bypass is useful when you have data with common values that should be ignored, such as a dummy phone number or a dummy email. <br>Example: Never match the phone 555-1212, or test@contoso.com   |
