---
title: Create unmapped fields for marketing forms (preview)
description: Mapped and unmapped fields for forms in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/12/2025
ms.topic: how-to
author: petrjantac
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Create unmapped fields for marketing forms (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Custom unmapped fields let you gather additional information about your customers by creating any kind of question directly in the form editor, without needing to create new custom attributes for your lead or contact entity. For example, you can create fields to ask, “What is your meal preference?” or create contest questions to increase customer satisfaction and retention.

> [!TIP]
> The preview of unmapped form fields is only available for marketing forms. Custom unmapped fields for event registration forms will be available soon.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## Difference between mapped and unmapped fields

There are two general types of fields: mapped and unmapped. If you want to store the submitted value on a contact or lead, use mapped fields. If you don't want the submitted value to be stored on a contact or lead, use unmapped fields.

- **Mapped fields** are linked to an existing attribute of an entity. For example, the `First Name` field is linked to the `firstname` attribute of the contact entity. When the form is submitted, the mapped fields update the corresponding lead or contact attribute. All contact and lead attributes (except some protected system fields) are available as fields in the form editor. If you create a new custom attribute of a lead or contact, it's automatically available as a field in the form editor.
- **Unmapped fields** aren't mapped to any attribute of any entity. These fields are typically used for one-off questions. Unmapped fields values aren't stored in contact or lead entities. The submitted values are stored in the form submission entity.

## Creating unmapped form fields

In the form editor, you can drag and drop a field type from the **Elements** panel to create unmapped fields of the corresponding type.

:::image type="content" source="media/real-time-marketing-add-custom-form-field.png" alt-text="Add unmapped field" lightbox="media/real-time-marketing-add-custom-form-field.png":::

Each unmapped field has a **Logical name**. There can be multiple fields with the same logical name, but you can use only a single field of the same logical name in a single form. Once you add a field to the canvas, all fields with the same logical name are disabled in the right pane and can’t be added to the form. The logical name is used as the key for the submitted value and is also used in journey orchestration based on the submitted values of the unmapped field. You can define the field label, placeholder text, default value, and set if the unmapped field is required for submission. The unmapped field can also be set as hidden, and you can set up a custom validation of the submitted value.

The following field types are available for creating unmapped fields:

- **Short text**: Represented as a standard input.
- **Long text**: Suitable for longer text inputs.
- **Option set**: You can select if the field is displayed as a *dropdown* or *radio button*. You can create multiple options. The user submitting the form can select only a single value.
- **Multi-select**: Rendered as a list of checkboxes. You can create multiple options. The user submitting the form can select multiple values.
- **Radio button**: Limited to only two options.
- **Number**: A special type of input field that accepts only numeric values.
- **Checkbox**: A single checkbox.
- **Date & time**: You can define if it's rendered as *Date* only or a *Date & time* field.

> [!WARNING]
> The unmapped field code must always be present in the stored form HTML code. If you create an unmapped field by DOM manipulation of an already rendered form, the field's submitted value won't be processed once the backend validation of the form submission is introduced.

### Branch journey using an unmapped field value

All submitted values of unmapped fields are stored in the form submission. The *Form Submission Fields Snapshot* attribute of the form submission interaction is a string containing all submitted values in *key: value* format. The *key* is *Field Value Localized name* of the form submission. The *value* is represented by the *Value* in form submission.

To branch your journey using submitted values of unmapped fields for journeys started by the *Marketing form submitted* trigger, perform the following steps:

1. Insert an **Attribute branch** tile anywhere in the journey where you want to check the values and give it a meaningful name (for example, "Check unmapped field").
1. For the first branch ("Branch 1"), select the **Add conditions** link on the right side of the journey canvas to configure the branching statement.
1. Provide a name for the branch (for example "option 1"), select **make condition on an attribute**, and choose **Trigger** > **Marketing Form Submitted** > **Form Submission Field Snapshot**.
1. Change the value of operator from *Equals* to *Contains*.
1. Enter the condition in this format: *Field Value Localized Name*: *Value*. For example "unmapped_field_name: 1".

:::image type="content" source="media/real-time-marketing-branch-journey-using-unmapped-field.png" alt-text="Branch journey using unmapped field" lightbox="media/real-time-marketing-custom-form.png":::

## Save fields to reuse them in other forms

Unmapped fields and modified mapped fields can be saved for reuse later in other forms. The saved fields are shared across your organization, allowing your colleagues to use fields you've created.

:::image type="content" source="media/real-time-marketing-save-field.png" alt-text="Save field" lightbox="media/real-time-marketing-save-field.png":::

- The **saved unmapped fields** are located in the *Unmapped* section of the **Fields** right side pane.
- The **saved mapped fields** can be found in the respective *Contact*, *Lead*, or *Lead & Contact* sections of the **Fields** right side pane.

Once you add a saved field to canvas and modify it, you can save the changes to the original saved field by selecting the *Update field* button.

The display name of the saved field must be unique. If you enter a display name of an existing field, you'll be prompted if you want to overwrite the existing field.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
