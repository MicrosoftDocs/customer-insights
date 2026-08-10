---
title: Transform dynamic text with Power Fx formulas
description: Apply Power Fx formulas to dynamic text in Customer Insights - Journeys to capitalize names, format numbers for a locale, and localize dates before sending.
ms.date: 08/08/2026
ms.topic: article
author: alfergus
ms.author: alfergus
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transform dynamic text with Power Fx formulas

Power Fx is a low-code formula language used across Microsoft Power Platform to create logic and customize app behavior. Its Excel-like syntax makes it easier to work with data, automate calculations, and build dynamic experiences.

You can apply a Power Fx formula to a piece of dynamic text so its value is transformed before it's inserted into a message. For example, you can capitalize a name, format a number for a specific locale, or format a date without creating a calculated column in Dataverse. Power Fx is used across Power Apps, Power Automate, and Power Pages, so if you already write formulas in those apps, you can use the same syntax in Customer Insights - Journeys.

Formula mode is optional and off by default. When it's off, dynamic text behaves exactly as described in the [Personalize content using predefined dynamic text](real-time-marketing-predefined-dynamic-text.md) article.

> [!IMPORTANT]
> Formulas run on a single piece of dynamic text at a time. You can't combine two dynamic text values in the same formula.

## Enable a formula for a piece of dynamic text

1. In the email editor, select the dynamic text you want to transform, and then select **Personalization**.

1. Expand the **Advanced** section.

1. Select the **Power Fx formula** checkbox.

1. In the formula box, enter a formula, using the dynamic text's display name as the variable. For example, if the display name is `EventName`, enter `Upper(EventName)`. If the display name contains spaces, enclose it in single quotes, for example `Upper('Event Name')`.

1. Review the **Output** field to confirm the formula produces the result you expect. The output updates automatically as you type, using the dynamic text's default value as sample input.

1. Select **Save**.

The dynamic text now applies your formula whenever the message is sent, in addition to its existing default value behavior.

> [!TIP]
> Select **Supported functions** to open a reference pane with functions relevant to the data type of your dynamic text (text, number, or date/time). Each entry includes an example formula, a sample input, and the expected output. Select the copy icon next to any example to insert it directly into the formula box.

## Handle empty values

If the underlying field can be empty, wrap your formula in `Coalesce()` to provide a fallback value instead of relying on the dynamic text's own default value behavior. For example:

`Coalesce(Upper(EventName), "UNSPECIFIED")`

## Format numbers and dates for a locale

Use `Text()` with a format string and a locale code to display numbers and dates the way your audience expects. For example:

- **Number**: `Text(AgingBalance, "#,##0.00", "de-DE")` displays `13.657,00` for a German-locale audience.

- **Date**: `Text(Birthday, "dddd, mmmm d", "de-DE")` displays `Sonntag, Dezember 31`.

> [!NOTE]
> For date/time dynamic text, the existing **Display options** setting (date/time format, locale, and time zone) described in the [Personalize content using predefined dynamic text](real-time-marketing-predefined-dynamic-text.md) article is separate from and unaffected by Power Fx formulas. Both can be used on the same dynamic text.

## Supported functions

Formula mode supports any [Power Fx function](/power-platform/power-fx/formula-reference-overview) that works on a single text, number, or date/time value. Functions that operate on tables or records, such as `Filter()`, `Sort()`, or `GroupBy()`, aren't available because a single dynamic text value isn't a table or record. See the full [Power Fx formula reference](/power-platform/power-fx/formula-reference-overview) for syntax details on any function.

> [!NOTE]
> If a formula fails to run (for example, because of a syntax or type error), the message still sends using the dynamic text's original value or default value. The formula error doesn't block or delay sending.

## Known limitations for Power Fx formulas

- Formulas can reference only one piece of dynamic text at a time. You can't combine two dynamic text values in a single formula (for example, joining a first name and last name).
- Formulas run when you send the message, not earlier in the journey.
- Custom or imported functions aren't supported. Only built-in Power Fx functions that work on a single value are available.
- The formula box accepts up to 500 characters, with a maximum nesting depth of five levels.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
