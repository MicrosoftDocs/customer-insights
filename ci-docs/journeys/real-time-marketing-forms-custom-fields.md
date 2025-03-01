---
title: "Preview: Create unmapped fields for marketing forms"
description: Mapped and unmapped fields for forms in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/03/2024
ms.topic: article
author: petrjantac
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Preview: Create unmapped fields for marketing form

> [!IMPORTANT]
> A preview feature is a feature that is not complete but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.
>
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won’t be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data or other data that are subject to legal or regulatory compliance requirements.

Custom unmapped fields allow you to easily gather additional information about your customers by creating any kind of question directly in the form editor without the need to create new custom attributes for your lead or contact entity. For example, you can create fields to ask, “What is your meal preference?” or create contest questions to increase your customer satisfaction and retention.

> [!TIP]
> The preview of unmapped form fields is currently available only for marketing form. Custom unmapped fields for event registration forms will be available soon.

## Difference between mapped and unmapped fields

There are two general types of fields: mapped and unmapped. If you want to store the submitted value on Contact or Lead, use the mapped fields. If you don't want the submitted value to be stored on Contact or Lead, use the unmapped fields.

- **Mapped fields** are linked to an existing attribute of an entity. For example, the First Name field is linked to the firstname attribute of the Contact entity. When the form is submitted, the mapped fields update the corresponding Lead or Contact attribute. All contact and lead attributes (except some protected system fields) are available as fields in the form editor. If you create a new custom attribute of Lead or Contact, it is automatically available as a field in the form editor.
- **Unmapped fields** are not mapped to any attribute of any entity. These fields are typically used for one-off questions. Unmapped fields values are not stored in Contact or Lead entities. The submitted values are stored in the Form submission entity.

## Creating unmapped form fields

You can drag and drop a Field type from the Elements to create unmapped fields of the corresponding type.

:::image type="content" source="media/real-time-marketing-add-custom-form-field.png" alt-text="Add unmapped field" lightbox="media/real-time-marketing-custom-form.png":::

Each unmapped field has **Logical name**. There can be multiple fields with the same logical name, but you can use only a single field of the same logical name in a single form. Once you add a filed to canvas, all fields with the same logical name are disabled in the right pane and they can not be added to the form. The logical name is used as the key for the submitted value and it is also used in journey orchestration based on submitted values of unmapped field. You can define field label, placeholder text, default value and set if the unmapped field is required for the submission. The unmapped field can be also set as hidden and you can set up a custom validation of the submitted value.

The following field types are available for creating unmapped fields:

- **Short text** - represented as a standard input
- **Long Text** - suitable for longer text inputs
- **Option set** - you can select if the field is displayed as *dropdown* or *radio button*. You can create multiple options. The user submitting the form can select only a single value.
- **Multi-select** - rendered as a list of checkboxes. You can create multiple options. The user submitting the form can select multiple values value.
- **Radio button** - is limited to only two options.
- **Number** - is a special type of input field that accepts only numeric values.
- **Checkbox** - a single checkbox.
- **Date & Time** - you can define if it is rendered as Date only or Date & Time field.

> [!WARNING]
> The unmapped field code has to be always present in the stored form HTML code. If you create an unmapped field by DOM manipulation of an already rendered form, such field's submitted value will not be processed once the back-end validation of form submission is introduced.

### Branch journey using unmapped field value

All submitted values of unmapped fields are stored in the form submission. The *Form Submission Fields Snapshot* attribute of form submission interaction is a string containing all submitted values in *key: value* format. The *key* is *Field Value Localized name* of the form submission. The *value* is represented by the *Value* in form submission.

You can follow these steps to branch your journey using submitted values of unmapped fields for journeys started by *Marketing form submitted* trigger:

1. Insert an “Attribute branch” tile anywhere in the journey where you want to check the values and give it a meaningful name (for example “Check unmapped field”).
1. For the first branch (“Branch 1”), select the “add conditions” link on the right side of the journey canvas to configure the branching statement.
1. Provide a name for the branch (for example “option 1”), choose “make condition on an attribute” and choose “Trigger -> Marketing Form Submitted -> Form Submission Field Snapshot”.
1. Change the value of operator from *Equals* to *Contains*.
1. Enter the condition in this format: *Field Value Localized Name*: *Value*. For example “unmapped_field_name: 1”.

:::image type="content" source="media/real-time-marketing-branch-journey-using-unmapped-field.png" alt-text="Branch journey using unmapped field" lightbox="media/real-time-marketing-custom-form.png":::

## Save fields to reuse them in other forms

Both unmapped fields and modified mapped fields can be saved for later reuse in other forms. The saved fields are shared across your whole organization allowing your colleagues tou use fields created by you.

:::image type="content" source="media/real-time-marketing-save-field.png" alt-text="Save field" lightbox="media/real-time-marketing-custom-form.png":::

- The **saved unmapped fields** are located in section *Unmapped* of the Fields right hand side pane.
- The **saved mapped fields** can be found in the respective *Contact*, *Lead* or *Lead & Contact* section of the Fields right hand side pane.

Once you add a saved field to canvas and modify it, you can save the changes to the original saved field by selecting *Update field* button.

The display name of the saved field must be unique. If you enter a display name of an existing field, you will be prompted if you want to overwrite the existing field.
