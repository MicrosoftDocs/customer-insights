---
title: Create unmapped fields for registration forms
description: Learn how create unmapped fields for registration forms in Dynamics 365 Customer Insights - Journeys. 
ms.date: 10/23/2025
ms.topic: article
author: colinbirkett
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Create unmapped fields for registration forms

Custom unmapped fields (also known as custom registration fields) allow you to **create and manage personalized questions for event attendees** without affecting the Lead or Contact entity. Custom unmapped fields let you collect relevant information for each event, such as dietary preferences, session interests, feedback, and more. Use the information you gather to customize the communication with your attendees and personalize the event attendee experience.

> [!TIP]
> This article describes custom unmapped fields for event registration forms. For information on custom unmapped fields in marketing forms, see [Create unmapped fields for marketing forms](real-time-marketing-forms-custom-fields.md).

## Create unmapped form fields for your event  

To create a custom unmapped form field for your event, go to **Event planning** > **Form**. Select **Edit** to see a preview of the form on the right side. When you select **Edit**, you go to the form editor. Select **Edit** to edit the form.

:::image type="content" source="media/create-custom-unmapped-fields-registration-forms.png" alt-text="Create unmapped form fields for your event." lightbox="media/create-custom-unmapped-fields-registration-forms.png":::

If you use this form in multiple events, a dialog appears. You have the following two options:  

- To edit the form for *all events that use this form*, select the provided link. This action opens the reusable form in the Forms section.  
- To edit the form for *this event only*, select **Create a copy**.

:::image type="content" source="media/create-copy-unmapped-fields.png" alt-text="Create a form copy for a single event." lightbox="media/create-copy-unmapped-fields.png":::

In the form editor, a new section called **Unmapped** appears. You can select previously saved fields or select **+ New** to create a new field. 

## Create a new unmapped form field

In the form editor, drag and drop a field type from the **Elements** panel to create unmapped fields of the corresponding type. 

:::image type="content" source="media/custom-unmapped-fields.png" alt-text="An overview of possible custom unmapped fields." lightbox="media/custom-unmapped-fields.png":::

Each unmapped field has a logical field name. You can have multiple fields with the same logical field name, but you can only use a field of the same name once in a form. When you add a field to the canvas, the form editor disables all fields with the same logical name in the right pane and you can't add them to the form. The logical field name acts as the key for the submitted value. Journey orchestration uses this key based on the submitted values of the unmapped field. You can define the field label, placeholder text, default value, and set if the unmapped field is required for submission. You can hide the unmapped field and set up custom validation for the submitted value.

The following field types are available for creating unmapped fields:

- **Short text**: A field for standard input.
- **Long text**: A field for longer text inputs.
- **Option set**: A field for multiple option selections. You can select if the field is displayed as a dropdown or radio button. The user submitting the form can only select a single value.
- **Multi-select**: A field rendered as a list of checkboxes. You can create multiple options. The user submitting the form can select multiple values. 
- **Radio button**: A field limited to only two options.
- **Number**: A field that only accepts numeric values inputs.
- **Checkbox**: A field containing a single checkbox.
- **Date & time**: A field for inputting a date. You can configure the field for date only or for both date & time.

## Save fields to reuse them in other forms

You can save unmapped fields and modified mapped fields for later reuse in other forms. Your organization shares the saved fields, so your colleagues can use the fields you create.

:::image type="content" source="media/save-field.png" alt-text="Save custom field." lightbox="media/save-field.png":::

The **Fields** right side pane lists the saved unmapped fields in the **Unmapped** section.

When you add a saved field to the canvas and modify it, select **Update field** to save the changes to the original saved field.

The display name of the saved field must be unique. If you enter the same display name as an existing field, you're asked if you want to overwrite the existing field.

## Viewing submitted responses  

The form submission response records responses to the custom unmapped fields. Navigate to **Registration and attendance** to view all responses and event registration information in one table. The information includes the contact's registration ID, name, email, registration status, and date of creation. This joint data table is created as a new system view for the event. You can also add new registrations with custom unmapped fields manually through a quick create form in the registration grid.

> [!NOTE]
> It can take up to two minutes for the new system view to be created after a first submission is received.  

:::image type="content" source="media/registration-and-attendance-overview.png" alt-text="An overview of customer registration and attendance in the form." lightbox="media/registration-and-attendance-overview.png":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]
