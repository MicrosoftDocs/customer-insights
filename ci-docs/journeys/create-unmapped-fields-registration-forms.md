---
title: Create unmapped fields for registration forms
description: Learn how create unmapped fields for registration forms in Dynamics 365 Customer Insights - Journeys. 
ms.date: 05/01/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Preview: Create unmapped fields for registration forms

> [!IMPORTANT]
> A preview feature is a feature that is not complete, but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.
> 
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won’t be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data or other data that are subject to legal or regulatory compliance requirements.

The custom unmapped fields feature (also known as custom registration fields) allows you to **create and manage personalized questions for event attendees**, without affecting the Lead or Contact entity. It allows you to collect relevant information for each event, such as dietary preferences, session interests, feedback, and more. You can then use the answers to customize the communication with your attendees and personalize the event attendee experience. 

> [!TIP] 
> This article describes custom unmapped fields for event registration forms. For information on custom unmapped fields in marketing forms, see [Create unmapped fields for marketing forms](real-time-marketing-forms-custom-fields.md). 

## Creating unmapped form fields for your event  

To create a custom unmapped form field for your event, you can navigate to the Event > Form (this was previously called Website & Form) tab. You can now see a preview of the form on the right-hand side by selecting the **Edit** button. Once selected, you'll be taken to the form editor.

:::image type="content" source="media/create-custom-unmapped-fields-registration-forms.png" alt-text="Create unmapped form fields for your event." lightbox="media/create-custom-unmapped-fields-registration-forms.png":::

If this form is used in multiple events, you'll be presented with a dialog. Choose from one of the two options:  

1. To edit the form for **all events that are using this form**, select on the provided link. This opens the reusable form in the Forms section.  
1. To edit the form for **this event only**, create a copy with one select.

:::image type="content" source="media/create-copy-unmapped-fields.png" alt-text="Create a form copy for a single event." lightbox="media/create-copy-unmapped-fields.png":::

In the form editor, you'll notice a new section called “Unmapped” where you can select previously Saved fields or click **New** to create a new field. 

## Creating a new unmapped form field 

In the form editor, you can drag and drop a field type from the Elements panel to create unmapped fields of the corresponding type. 

:::image type="content" source="media/custom-unmapped-fields.png" alt-text="An overview of possible custom unmapped fields." lightbox="media/custom-unmapped-fields.png":::

Each unmapped field has a Logical name. There can be multiple fields with the same logical name, but you can use only a single field of the same logical name in a single form. Once you add a field to the canvas, all fields with the same logical name are disabled in the right pane and can’t be added to the form. The logical name is used as the key for the submitted value and is also used in journey orchestration based on the submitted values of the unmapped field. You can define the field label, placeholder text, default value, and set if the unmapped field is required for submission. The unmapped field can also be set as hidden, and you can set up a custom validation of the submitted value. 

The following field types are available for creating unmapped fields: 

- **Short text**: Represented as a standard input. 
- **Long text**: Suitable for longer text inputs. 
- **Option set**: You can select if the field is displayed as a dropdown or radio button. You can create multiple options. The user submitting the form can select only a single value. 
- **Multi-select**: Rendered as a list of checkboxes. You can create multiple options. The user submitting the form can select multiple values. 
- **Radio button**: Limited to only two options. 
- **Number**: A special type of input field that accepts only numeric values. 
- **Checkbox**: A single checkbox. 
- **Date & time**: You can define if it's rendered as Date only or a Date & time field. 

## Save fields to reuse them in other forms 

Unmapped fields and modified mapped fields can be saved for reuse later in other forms. The saved fields are shared across your organization, allowing your colleagues to use fields you've created. 

:::image type="content" source="media/save-field.png" alt-text="Save custom field.." lightbox="media/save-field.png":::

The saved unmapped fields are in the Unmapped section of the Fields right side pane. 

Once you add a saved field to canvas and modify it, you can save the changes to the original saved field by selecting the Update field button. 

The display name of the saved field must be unique. If you enter a display name of an existing field, you are prompted if you want to overwrite the existing field. 

## Viewing submitted responses  

Answers to the custom unmapped fields are recorded in the form submission response. Navigate to Registration and attendance to view all the responses together with event registration information in one table. This joint data table is created as a new system view for the registration form.  

> [!NOTE]
> Please note that it can take up to 2 minutes for the new system view to be created after a first submission is received.  

You can also create a new System view that can be reused across all events. To construct advanced queries, the Advanced search should be enabled for your organization. For more information, see [Advanced find in model-driven apps](/power-apps/user/advanced-find).

:::image type="content" source="media/registration-and-attendance-overview.png" alt-text="An overview of customer registration and attendance in the form." lightbox="media/registration-and-attendance-overview.png":::