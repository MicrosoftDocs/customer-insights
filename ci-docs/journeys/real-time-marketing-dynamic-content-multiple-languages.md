---
title: Create dynamic email content in multiple languages
description: Learn how to use conditional content blocks in Dynamics 365 Customer Insights - Journeys to create email content that adapts to the country/region and language of your customers.
ms.date: 08/22/2023
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-desc
  - ai-seo-date:09/20/2023
  - bap-template
---

# Create dynamic email content in multiple languages

When you have customers in multiple countries and regions, you often need to send them email with the same content but with small variations based on their location or language. Dynamics 365 Customer Insights - Journeys offers two ways to do that. Both methods use the [audience profile](./real-time-marketing-audience-data.md) to determine which content to deliver.

- Create a separate email for each country/region you want to send to and in each language your customers speak. This method is easy to set up, although time-consuming. But because each audience requires a different email, the number of emails is higher.
- Use a [conditional content block](./content-blocks.md) that adapts to your customers' preferences. This method takes more steps to set up, but reduces the number of emails to one.

In this article, you'll learn how to use conditional content blocks to create multilingual email content for different audiences. You'll also learn how to customize your data model and add inline conditions and dynamic text to your email content.

## Conditional content by free text country/region

Suppose you want to add a footer with terms and conditions that vary depending on the country/region of your customers. The simplest scenario is to use the `Country/Region` column in the `Contact` table, which is a free text field that identifies your customers' country/region of residence. You can use this column to create conditions that compare the country/region with the variations you want to show in your email content.

1. [Create a content block](./content-blocks.md#creating-a-content-block) called "All Country Footer" and add a section and column where you place the text of the terms and conditions.

1. Add a condition for each country/region where you do business; for example, the UK, Spain, and Mexico.

    :::image type="content" source="./media/real-time-marketing-content-block-country-footer.png" alt-text="Screenshot showing the All Country Footer content block with conditions highlighted.":::

    The following screenshot illustrates how to create a condition called "UK" that compares the value of the `Country/Region` field with the value "United Kingdom":

    :::image type="content" source="./media/real-time-marketing-define-condition.png" alt-text="Screenshot showing the All Country Footer content block with a condition defined.":::

1. In each variation, add the appropriate text.

1. Add a condition and text for the other countries or regions and languages you want to support.

1. When you're finished, select **Ready to send** and [use it in your emails](#create-the-email).

## Conditional content by lookup country/region

The previous scenario relies on your users typing the country/region in a free text field and matching the values exactly with the conditions in the content block. Manual data entry can be prone to errors and inconsistencies. To make the solution more robust, you can extend the data model and select the country/region from a lookup table instead of entering free text.

1. In the [Maker portal](https://make.powerapps.com/), [create a table](/power-apps/maker/data-platform/create-edit-entities-portal) that contains just the names of the countries or regions you support.

1. [Create a table relationship](/power-apps/maker/data-platform/data-platform-entity-lookup) between the country table and the `Contact` table.

    This action updates the form for the `Contact` table to allow users to select the country/region from a list instead of typing it manually.

1. Set the condition in the content block to use the lookup column instead of the free text column.

    :::image type="content" source="./media/real-time-marketing-define-condition-using-related-table.png" alt-text="Screenshot of a content block with a condition defined using the contact's custom country lookup column.":::

1. Add a condition and text for the other countries/regions and languages you want to support.

1. When you're finished, select **Ready to send** and [use it in your emails](#create-the-email).

## Multiple languages in the same country/region

Some countries/regions have multiple official languages or languages that are widely spoken. In these cases, you may want to send email in the specific language of your contacts, not based just on their country/region. To do this, add another layer of personalization based on your customers' language.

1. In the [Maker portal](https://make.powerapps.com/), [create a table](/power-apps/maker/data-platform/create-edit-entities-portal) that contains just the names of the languages you support.

1. [Create a table relationship](/power-apps/maker/data-platform/data-platform-entity-lookup) between the language table and the `Contact` table.

    This action updates the form for the `Contact` table to allow users to select the language from a list instead of typing it manually.

1. Set the condition in the content block to use the lookup column instead of the free text column.

1. Add a condition and text for the other languages you want to support.

1. When you're finished, select **Ready to send** and [use it in your emails](#create-the-email).

## Multiple conditions in content block variations

With this data model extension in place, you can update the content block to use both the country/region and language columns to create conditions.

1. Add a condition to your content block for each country-language pair you want to support.

1. In each one, add two more conditions: one that compares the country column with a record from the country table, and another that compares the language column with a record from the language table.

    For example, here's how you can create a variation that shows the text for the UK in English:

    :::image type="content" source="./media/real-time-marketing-define-multiple-conditions-using-content-blocks.png" alt-text="Screenshot of a content block with a condition defined using the contact's custom country/region and language lookup columns.":::

1. When you're finished, select **Ready to send** and [use it in your emails](#create-the-email).

## Make standard content easier to update

In the previous scenarios, you added the text of the terms and conditions directly in the content block. However, putting the content there can create a maintenance nightmare if you need to update the text often or in multiple content blocks and emails.

To make updating standard content easier, create another table that holds the text of the terms and conditions for all the country/region and language combinations you support. Then use [inline conditions](real-time-marketing-personalize-inline-conditions.md) and [dynamic text from other tables](real-time-marketing-predefined-dynamic-text.md#using-data-from-additional-tables-in-dynamic-text) to read the text from this table and insert it in your email content.

### Create and populate a table with formatted text

1. Create a table called `Legal Texts` and add a rich text column called `Formatted Text`.

1. Populate the table with formatted terms and conditions for each country/region and language you support.

### Add inline conditions and dynamic text to the content block

With the table in place, update the content block to use inline conditions and dynamic text to read the text from the table based on the country/region and language and insert it in your email content.

1. Add a condition to the content block. Make sure that **Make condition on attribute** is selected.

1. Select **Choose an attribute** > **Other tables (needs record selection)**.

1. Select **Legal Texts** > **Formatted Text**.

1. Select the **Look for Formatted Text** box, press Enter, and select a variation.

1. Select **Done**.

1. Repeat for each combination of country/region and language you support.

This process creates tokens that you can use to insert the text from the `Legal Texts` table in your email content.

To build the logic for each country/region and language variation, place each token in an inline condition that checks the contact's language.

For example, here's an example of the logic for the UK variation that shows the terms and conditions text for English and Welsh speakers:

:::image type="content" source="./media/real-time-marketing-logic-build-country-conditional-content.png" alt-text="Screenshot of tokens in a conditional content block.":::

Now, instead of updating the terms and conditions in dozens of places, you can update them in one place and the changes are automatically reflected everywhere they're used.

## Create the email

With the content block ready, you can use it in your email and know that the terms and conditions will be sent according to the contact's country/region and language.

[Learn how to create emails with Customer Journeys - Insights](real-time-marketing-email.md).

## Next steps

- [Quickly design and deliver a marketing email with send now](email-quick-send.md)
- [Send a targeted email blast in Customer Insights - Journeys](real-time-marketing-email-get-started.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]