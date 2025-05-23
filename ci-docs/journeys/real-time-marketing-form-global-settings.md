---
title: Set the default configuration for forms
<<<<<<< Updated upstream
<<<<<<< Updated upstream
description: Set the default configuration for all newly created forms in Dynamics 365 Customer Insights - Journeys.
=======
description: Default form configuration in Customer Insights - Journeys helps you create forms faster. Discover how to set up and manage defaults for marketing and event forms.
>>>>>>> Stashed changes
=======
description: Default form configuration in Customer Insights - Journeys helps you create forms faster. Discover how to set up and manage defaults for marketing and event forms.
>>>>>>> Stashed changes
ms.date: 05/23/2025
ms.topic: how-to
author: petrjantac
ms.author: colinbirkett
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:05/23/2025
---

# Set the default configuration for forms

<<<<<<< Updated upstream
<<<<<<< Updated upstream
Creating a new form can be challenging for nontechnical users due to the complexity of the form configuration, which requires system knowledge. Each time you create a new form, going through the configuration process can be time-consuming and can cause errors.
=======
Creating a new form can be challenging for nontechnical users because form configuration is complex and requires system knowledge. Each time you create a new form, the configuration process takes time and can introduce errors.
>>>>>>> Stashed changes
=======
Creating a new form can be challenging for nontechnical users because form configuration is complex and requires system knowledge. Each time you create a new form, the configuration process takes time and can introduce errors.
>>>>>>> Stashed changes

The form configuration feature lets you preset all your new forms, so you don't need to set every detail each time you create a form. Set defaults for all new marketing or event registration forms on the **Form Settings** page in the Customer Engagement section of **Settings**.

:::image type="content" source="media/real-time-marketing-form-global-settings.png" alt-text="Screenshot of the global form settings page in Dynamics 365 Customer Insights - Journeys." lightbox="media/real-time-marketing-form-global-settings.png":::

You get two out-of-the-box configurations for default form values based on the form type:

1. Event registration form defaults
1. Marketing form defaults

> [!WARNING]
> Don't delete these out-of-the-box configurations. Deleting them can cause configuration issues. If you delete an out-of-the-box configuration, create a new configuration of the same type and set it as the default. You only need one default configuration for each form type.

Select a configuration to edit default values for its form type.

The form configuration has four tabs:

1. **[General](real-time-marketing-form-global-settings.md#general)**: Set configuration details and common form settings.
1. **[Audience](real-time-marketing-form-global-settings.md#audience)**: Select the target audience (entity record) created or updated by the form submission.
1. **[Lead-Contact Mapping](real-time-marketing-form-global-settings.md#lead-contact-mapping)**: Only for the marketing form type. Review how lead and contact attributes map.
1. **[reCAPTCHA](real-time-marketing-form-global-settings.md#recaptcha)**: Set up a third-party form captcha.

:::image type="content" source="media/real-time-marketing-form-global-settings-general.png" alt-text="Screenshot of the General section in the global form settings page." lightbox="media/real-time-marketing-form-global-settings-general.png":::

## General

The first part of the **General** section lets you set the details of the form configuration. Set the name, select the form type, and label the configuration as default. Only one default configuration of the same type is allowed.

Select whether [form prefill](real-time-marketing-form-prefill.md) is automatically enabled for new forms.

<<<<<<< Updated upstream
<<<<<<< Updated upstream
The second part of the **General** section allows you to choose which default action will be taken after the form is submitted. Once submitted, the form can show a *Thank you* notification or you can set the *Error* notification. You can customize the content of both notifications.
=======
The second part of the **General** section lets you choose the default action after the form is submitted. After submission, the form can show a *Thank you* notification or an *Error* notification. Customize the content of both notifications.
>>>>>>> Stashed changes
=======
The second part of the **General** section lets you choose the default action after the form is submitted. After submission, the form can show a *Thank you* notification or an *Error* notification. Customize the content of both notifications.
>>>>>>> Stashed changes

## Audience

> [!IMPORTANT]
> A preview feature is a feature that isn't complete but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and could have limited or restricted functionality.
>
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won’t be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal or other data that are subject to legal or regulatory compliance requirements.

<<<<<<< Updated upstream
<<<<<<< Updated upstream
The **Audience** section allows you to set the default target audience for your newly created forms. The **Audience settings** determine which audience (that is, entity record) is used in the submission processing, and the conditions under which a new record is created or an existing record is updated. All **Audience settings** are visible in the form editor, allowing users to select their preferred audience when creating a new form.
=======
The **Audience** section lets you set the default target audience for your new forms. *Audience settings* determine which audience (entity record) is used in submission processing, and the conditions for creating a new record or updating an existing record. All *Audience settings* appear in the form editor, so you can select your preferred audience when you create a new form.
>>>>>>> Stashed changes
=======
The **Audience** section lets you set the default target audience for your new forms. *Audience settings* determine which audience (entity record) is used in submission processing, and the conditions for creating a new record or updating an existing record. All *Audience settings* appear in the form editor, so you can select your preferred audience when you create a new form.
>>>>>>> Stashed changes

Change the details of the out-of-the-box *Audience settings* or create new settings.

:::image type="content" source="media/real-time-marketing-form-global-settings-audience.png" alt-text="Audience section of global form settings." lightbox="media/real-time-marketing-form-global-settings-audience.png":::

<<<<<<< Updated upstream
<<<<<<< Updated upstream
The **Marketing form** type comes with three out-of-the-box audience settings:

- **Contact**: Update an existing contact using the selected matching rule (email address, by default). Create a new contact if no existing contact was matched.
- **Lead**: Always create a new lead, even if the same lead already exists (no matching rules are applied).
- **Lead & Contact**: Update an existing contact using the selected matching rule (email address by default). Create a new contact if no existing was matched. Always create a new lead, even if the same lead already exists (no matching rules are applied).
=======
The **marketing form** type has three out-of-the-box audience settings:
=======
The **marketing form** type has three out-of-the-box audience settings:

- **Contact**: Update an existing contact using the selected matching rule (email address by default). Create a new contact if no existing contact matches.
- **Lead**: Always create a new lead, even if the same lead already exists (no matching rules apply).
- **Lead & Contact**: Update an existing contact using the selected matching rule (email address by default). Create a new contact if no existing contact matches. Always create a new lead, even if the same lead already exists (no matching rules apply).
>>>>>>> Stashed changes

- **Contact**: Update an existing contact using the selected matching rule (email address by default). Create a new contact if no existing contact matches.
- **Lead**: Always create a new lead, even if the same lead already exists (no matching rules apply).
- **Lead & Contact**: Update an existing contact using the selected matching rule (email address by default). Create a new contact if no existing contact matches. Always create a new lead, even if the same lead already exists (no matching rules apply).
>>>>>>> Stashed changes

The **Event registration form** type comes with a single out-of-the-box audience setting:

- **Contact**: Update an existing contact using the selected matching rule (email address by default). Create a new contact if no existing contact was matched.

### Audience settings details

Change audience settings to specify when to create a new record and how to update an existing record to fit your business process. The following example uses a *contact* audience.

:::image type="content" source="media/real-time-marketing-form-global-settings-audience-details.png" alt-text="Audience details in global form settings." lightbox="media/real-time-marketing-form-global-settings-audience-details.png":::

- **Name**: Enter a name for your audience settings. This name appears in the form editor. Use short, descriptive names.
- **Target entity**: Select the entity used by form submission processing. Marketing forms support lead and contact entities, but event registration forms only support contact.

#### Matching rules

<<<<<<< Updated upstream
<<<<<<< Updated upstream
Matching rules help to configure how an existing record can be updated or when to create a new one. Matching rules follow the selected **Target entity**. You can see **Contact matching rules** if *Contact* is selected or **Lead matching rules** if *Lead* is selected.
=======
Matching rules set how to update an existing record or when to create a new one. Matching rules follow the selected *Target entity*. You see *Contact matching rules* if Contact is selected or *Lead matching rules* if Lead is selected.
>>>>>>> Stashed changes

> [!NOTE]
> This example uses a *Contact* audience. You see the same details for a *Lead* audience. The *Lead & Contact* audience lets you set separate details for both contact and lead.

First, **Choose how to handle duplicate contacts**. There are two options:
=======
Matching rules set how to update an existing record or when to create a new one. Matching rules follow the selected *Target entity*. You see *Contact matching rules* if Contact is selected or *Lead matching rules* if Lead is selected.

> [!NOTE]
> This example uses a *Contact* audience. You see the same details for a *Lead* audience. The *Lead & Contact* audience lets you set separate details for both contact and lead.
>>>>>>> Stashed changes

  - **Always create a new contact**: A new contact is always created. No matching rules are applied.
  - **Use a rule to match existing record**: Use a *matching rule* to find an existing record and avoid duplicates. Selecting this value unlocks the following extra options:
    - **Select contact matching rule**: The matching rule defines how to find and prioritize existing records. You can use the out-of-the-box matching rule *Update contact using email* or you can create you own custom matching rules. Custom matching rules can be created in **Settings** > **Matching rules**.
    - **Update matched contact with submitted data**
      - *Yes*: The best matching record is updated with form submission data.
      - *No*: The matched record isn't updated with form submission data. The form's submission data is only linked to the matched record.
    - **Create a new contact if there was no match to an existing one?**
      - Yes: If the matching rule doesn't find any suitable record to update, a new record is created.
      - No: No new record is created. The form submission data can be accessed only through the form submission.

## Lead-Contact Mapping

The **Lead-Contact Mapping** section is available only for the *marketing form* type. To use a combined Lead & Contact audience, define how the attributes map to each other. For example, link the Contact First Name attribute to the Lead First Name attribute, so the form field First Name updates attributes for both entities.

The combined Lead & Contact audience relies on [entity columns mapping](/power-apps/maker/data-platform/map-entity-fields), which you define in Power Apps. The mapping uses the *Parent contact* relationship.

> [!IMPORTANT]
> If you use solutions as the mechanism for implementing application lifecycle management (ALM), define the mappings as a [solution in Power Apps](/power-apps/maker/data-platform/solutions-overview).

:::image type="content" source="media/real-time-marketing-form-global-settings-mapping.png" alt-text="Screenshot of mapping options in global form settings." lightbox="media/real-time-marketing-form-global-settings-mapping.png":::

If you don't use solutions as the mechanism for implementing application lifecycle management (ALM), select the **Generate mappings** button to automatically link lead attributes to contact, or select **Edit in Power Apps** to manually define the mappings.

## reCAPTCHA

Protect your forms against bot attacks and malicious actors to keep the quality of captured data high. Marketing and event registration forms have standard captcha capabilities, but you can also [implement a custom captcha](real-time-marketing-form-custom-captcha.md) to improve the user experience.

<<<<<<< Updated upstream
<<<<<<< Updated upstream
The **reCAPTCHA** section allows you to enter the private key for and activate the reCAPTCHA plugin.
=======
In the reCAPTCHA section, enter the private key and activate the reCAPTCHA plugin.
>>>>>>> Stashed changes
=======
In the reCAPTCHA section, enter the private key and activate the reCAPTCHA plugin.
>>>>>>> Stashed changes

:::image type="content" source="media/real-time-marketing-configure-form-recaptcha.png" alt-text="Screenshot of the reCAPTCHA configuration section where you enter the private key and activate the plugin." lightbox="media/real-time-marketing-configure-form-recaptcha.png":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]
