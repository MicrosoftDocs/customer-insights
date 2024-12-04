---
title: Create Customer Insights - Journeys forms
description: Create forms in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/13/2023
ms.topic: article
author: petrjantac
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Form settings - set default configuration of all your new forms

Creating a new form can be quite challenging for non-technical users due to the complexity of the form configuration, which requires system knowledge. Each time you create a new form, going through the configuration process can be time-consuming and may introduce errors.

The new global form configuration feature allows you to preset all your new forms, eliminating the need to think about all the details each time you create a form. You can configure defaults for all your newly created marketing or event registration forms on the *Form Settings* page, located in the Customer Engagement section of *Settings*.

[!div class="mx-imgBorder"]
![Global form settings.](media/real-time-marketing-form-global-settings.png)

There are two out-of-the-box configurations for default form values following the form type:

1. Event registration form defaults
1. Marketing form defaults

    > [!IMPORTANT]
    > Do not delete these out-of-the-box configurations! This may result in configuration malfunction. If you delete the out-of-the-box configuration, create a new configuration of the same type and set it as default one.

You can select the configuration to edit default values for its respective form type.

There are 4 tabs representing various areas of form configuration:

1. **[General](real-time-marketing-form-global-settings.md#general)** - set details of configuration and configure common settings of the form.
1. **Audience** - select what target audience (which entity record) will be created or updated by the form submission.
1. **Lead-contact Mapping** - available only for marketing form type. Review the platform mapping between attributes of lead and contact entities.
1. **reCAPTCHA** - set up 3rd party form captcha.

[!div class="mx-imgBorder"]
![General section of global form settings.](media/real-time-marketing-form-global-settings-general.png)

## General

The first part of *General* section allows you to set details of the form configuration itself. You can set the name, select form type, and label the configuration as default. There can be only one default configuration of the same type.

You can also select if the [Form prefill](real-time-marketing-form-prefill.md) will be automatically enabled for your newly created forms.

The second part of *General* section allows you to choose the default action, which will be taken after the form is submitted. Once submitted, the form can show *Thank you* notification or you can set the *Error* notification. You can customize the content of both notifications.

## Audience

The *Audience* section allows you to set default target audience for your newly created forms. The *Audience settings* determines what audience (entity record) is used in the submission processing and conditions under which new record is created or existing record is updated. All *Audience settings* are visible in the form editor, allowing users to select their preferred audience when creating a new form.

You can either modify the details of the out-of-the-box *Audience settings* or you can create your new one.

[!div class="mx-imgBorder"]
![Audience section of global form settings.](media/real-time-marketing-form-global-settings-audience.png)

**Marketing form** type comes with 3 out-of-the-box Audience settings:

- Contact - Update existing contact using the selected matching rule (email address by default). Create a new contact if no existing was matched.
- Lead - Always create new lead, even if the same lead already exists (no matching rules are applied).
- Lead & Contact - Update existing contact using the selected matching rule (email address by default). Create a new contact if no existing was matched. Always create new lead, even if the same lead already exists (no matching rules are applied).

**Event registration form** type comes with a single out-of-the-box Audience setting:

- Contact - Update existing contact using the selected matching rule (email address by default). Create a new contact if no existing was matched.

### Audience settings details

You can modify all audience settings to specify when new records are created and how to update existing ones to meet your business process requirements.

[!div class="mx-imgBorder"]
![Audience details in global form settings.](media/real-time-marketing-form-global-settings-audience-details.png)

[!INCLUDE [footer-include](./includes/footer-banner.md)]