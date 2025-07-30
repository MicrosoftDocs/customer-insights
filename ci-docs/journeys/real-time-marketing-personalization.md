---
title: Personalize content
description: Learn how to personalize content in Dynamics 365 Customer Insights - Journeys.
ms.date: 07/31/2024
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: sfi-image-nochange
---

# Personalize content

> [!NOTE]
> Personalization tokens created within a given business unit are limited *only* to that business unit. If you want to use the same tokens in other business units, you must recreate the tokens in the other respective business units. Learn more: [Business unit support in real-time journeys](real-time-marketing-business-units.md)

Dynamics 365 Customer Insights - Journeys's features offer powerful personalization capabilities. In this article, you'll learn how to set default values for personalized data, preview personalized content, personalize text messages and push notifications, and use related tables.

## Default values

Use default values to ensure your message always has appropriate content, even if the data is missing or blank. For example, if you're personalizing your message with a customer’s first name, you can add “customer” as the default value. That way your message will always be complete.

To set a default value:

1. Add a personalized element.
1. Enter the default content in the **Default value** field.

> [!div class="mx-imgBorder"]
> ![Screenshot of Default value field.](media/real-time-marketing-personalization-default.png)

## Personalize text messages and push notifications

You can add personalized content to your messages by selecting the ![Text and push personalization button.](media/real-time-marketing-sms-personalize-button.png "Text and push personalization button") icon:

> [!div class="mx-imgBorder"]
> ![Screenshot showing use of the text and push personalization button.](media/real-time-marketing-sms-personalize-example.png)

## Related tables

Related tables are signified with the ![Related table icon.](media/real-time-marketing-personalization-related-table.png "Related table icon") icon next to the item in the data source selection screen. For example: ![Related table example.](media/real-time-marketing-personalization-related-example.png "Related table example")

Select this field to navigate to the related table:

> [!div class="mx-imgBorder"]
> ![Screenshot showing use an example related table.](media/real-time-marketing-personalization-related-traverse2.png)

You can also search for fields in the related table (only the currently selected table will return results).

> [!div class="mx-imgBorder"]
> ![Screenshot showing a related table search.](media/real-time-marketing-personalization-related-search.png)

To navigate between levels, select the breadcrumbs:

> [!div class="mx-imgBorder"]
> ![Screenshot showing personalization breadcrumbs.](media/real-time-marketing-personalization-breadcrumbs.png)

Once you’ve selected a field, the full path to that field is displayed in the data binding.

> [!div class="mx-imgBorder"]
> ![Screenshot showing the full path to the field.](media/real-time-marketing-personalization-related-path.png)

## Limitations

- Option sets aren't supported for use in dynamic text. Option sets are supported in conditions, so an inline condition can be used to output option values in messages.
- Personalization can only use triggers. However, messages that use personalization based on a trigger can only be used in journeys that are started by those triggers. If such a message is included in a journey where the trigger is received mid-journey, the journey designer will give an error message.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
