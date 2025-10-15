---
title: How to Use Submitted Values from Customer Insights – Journeys Forms
description: Discover how to personalize emails and branch journeys using the submitted values of forms
ms.date: 10/15/2025
ms.update-cycle: 180-days
ms.topic: how-to
author: petrjantac
ms.author: alfergus
---

# How to Use Submitted Values from Customer Insights – Journeys Forms

When a customer fills out a form in Customer Insights – Journeys, the values they submit can help you create more personalized and relevant experiences. This applies to both marketing forms and event registration forms.
There are two common scenarios you can use these submitted values:

1. Branch a journey
1. Personalize email

> [!NOTE]
> You can also use the submitted values to personalize Double Opt-in emails.

These scenarios work for both mapped and [unmapped fields](real-time-marketing-forms-custom-fields.md), so you can branch journeys or personalize emails regardless of whether the form fields are linked to a Contact or Lead attribute.

## Key Form Field Properties for Journey Branching and Personalization

Before we dive into the scenarios, let’s review which form field properties are most useful.

| Property | Description | Example |
|--|--------|--|
| **Field Value** | - Submitted value for text fields and text areas.<br>- **Numerical index** for option set, multi-select, and two-options fields.<br>- **Record ID** for lookup fields.<br> **Note:** For two-option fields, `False` or `0` value is represented by an empty value. | `1` (for option set field)|
| **Field Localized Value**| - Submitted value for text fields and text areas.<br>- **Human-readable value** for option set, multi-select, two-options, and lookup fields. | `Blue` (for option set) |
|**Display Name**          | - **Mapped fields**: Display name of the lead or contact attribute.<br>- **Unmapped fields**: Saved field name.<br>If the unmapped field wasn’t saved, this property contains the field label. | `First Name` |
| **Field Localized Name**  | - **Mapped fields**: Display name of the lead or contact attribute.<br>- **Unmapped fields**: Saved field name.<br>If the unmapped field wasn’t saved, this property contains the field label. | `First Name` |
| **Logical Name**          | - **Mapped fields**: Logical name of the lead or contact attribute.<br>- **Unmapped fields**: Logical name defined in the form editor.                   | `firstname` |

## Branch a journey based on submitted values

You can adjust the path of a journey depending on the answers your customer provided in the form.

For example: *If a customer selects “Interested in Product A”, you can branch them into a journey that sends more details about Product A.*

### Step by step guide - Choose favorite color example

To make this easier to follow, **let’s assume your form includes an option set field called Favorite color** with the following properties:

- Display name: Favorite color
- Field Localized Name: Favorite color
- Logical name: favoritecolor

And these options:

- Option 1:
  - Field value: 1
  - Field Localized Value: Blue
- Option 2:
  - Field value: 2
  - Field Localized Value: Red

1. **Create a new Trigger-based journey** using the **Marketing Form Submitted**, which works for both marketing and event registration form types. Choose your form and select **Create** button.
  :::image type="content" source="media/real-time-marketing-form-submitted-trigger.png" alt-text="Create trigger-based journey." lightbox="media/real-time-marketing-form-submitted-trigger.png":::
  If you don’t select a specific form, the journey will trigger from any form submission across all your forms. If your form updates multiple audiences (for example, both leads and contacts), make sure you select the correct audience for your journey.
1. On the **journey canvas**, add an action tile and select **Attribute branch** to create different paths based on submitted form values.  
    1. Set condition Trigger -> Marketing Form Submitted -> Form Submission Entity Reference -> Field Submissions -> Field Value.
    1. Enter the expected value. For example, if you want to create a branch for customers who selected Blue as their favorite color, enter 1 (the Field value assigned to Blue in the option set).
    1. Select *Field Submission Sort by Created On: Descending* to filter the correct form field.
  :::image type="content" source="media/real-time-marketing-form-set-trigger-condition.png" alt-text="Set trigger condition." lightbox="media/real-time-marketing-form-set-trigger-condition.png":::
1. **Filter the correct form field**. Select **Choose an attribute**, Field Submission -> Logical name and enter the expected value. For example, use favoritecolor, which is the logical name of the Favorite color option set field. Select Done button.
  :::image type="content" source="media/real-time-marketing-form-set-trigger-filter.png" alt-text="Set trigger filter." lightbox="media/real-time-marketing-form-set-trigger-filter.png":::
1. Add a **new branch and define another condition** (following steps 2 and 3) to cover the remaining options, so each possible value has its own path.

## Personalize email using submitted values

You can use submitted values to make your emails more relevant. There are two main approaches:

1. Insert dynamic text
1. Show a personalized list

Building personalized emails using submitted values works especially well for Double Opt-in emails, where the reference to a Contact or Lead record might be missing. In such cases, using the submitted form values ensures you can still personalize the message without relying on mapped Contact or Lead attributes.

### Insert dynamic text

This pulls the values your customer submitted and inserts them into the email.

1. Create a new or open an existing email.
1. Add Text element and select the Personalization icon.
1. Select *+ New dynamic text*.
1. Select *Choose and attribute*.
1. Select Trigger -> Marketing Form Submitted -> Form Submission Entity Reference -> Field Submissions -> Field Localized Value.
  :::image type="content" source="media/real-time-marketing-form-personalization-trigger.png" alt-text="Create dynamic text." lightbox="media/real-time-marketing-form-personalization-trigger.png":::
1. Select *Field Submission Sort by Created On: Descending* to filter the correct form field.
1. Select *Choose and attribute*.
1. Select Field Submission -> Logical name and enter the expected value. For example, `firstname`.
  :::image type="content" source="media/real-time-marketing-form-personalization-set-filter.png" alt-text="Set filter for dynamic text." lightbox="media/real-time-marketing-form-personalization-set-filter.png":::
1. Select Done, then Save.

### Show a personalized list

Create a Personalized list of what the customer submitted and include it in the email.

You can build personalized list using **Trigger -> Marketing Form Submitted -> Form Submission Entity Reference -> Field Submissions**. Choose the **Field localized Name** and **Field Localized Value** as columns. You can add conditions to exclude specific fields from the list. It is also possible to encapsulate the personalization tokens into html table to enhance the visual experience.

:::image type="content" source="media/real-time-marketing-form-personalized-list.png" alt-text="Set filter for dynamic text." lightbox="media/real-time-marketing-form-personalized-list.png":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]