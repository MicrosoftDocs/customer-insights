---
title: Set the default configuration for forms
description: Set the default configuration for all newly created forms in Dynamics 365 Customer Insights - Journeys.
ms.date: 05/23/2025
ms.topic: how-to
author: petrjantac
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Set the default configuration for forms

Creating a new form can be challenging for nontechnical users due to the complexity of the form configuration, which requires system knowledge. Each time you create a new form, going through the configuration process can be time-consuming and can cause errors.

The form configuration feature allows you to preset all your new forms, eliminating the need to think about all the details each time you create a form. You can configure defaults for all your newly created marketing or event registration forms on the **Form Settings** page, located in the Customer Engagement section of **Settings**.

:::image type="content" source="media/real-time-marketing-form-global-settings.png" alt-text="Global form settings." lightbox="media/real-time-marketing-form-global-settings.png":::

There are two out-of-the-box configurations for default form values that follow the form type:

1. Event registration form defaults
1. Marketing form defaults

> [!WARNING]
> Don't delete these out-of-the-box configurations. This could result in configuration malfunction. If you delete an out-of-the-box configuration, create a new configuration of the same type and set it as default one. Otherwise, there is no point creating additional configurations, as there can be only a single configuration set as default for a specific form type.

You can select the configuration to edit default values for its respective form type.

There are four tabs representing various areas of form configuration:

1. **[General](real-time-marketing-form-global-settings.md#general)**: Set details of configuration and configure common form settings.
1. **[Audience](real-time-marketing-form-global-settings.md#audience)**: Select what target audience (that is, which entity record) to be created or updated by the form submission.
1. **[Lead-Contact Mapping](real-time-marketing-form-global-settings.md#lead-contact-mapping)**: Available only for the marketing form type. Review the platform mapping between attributes of lead and contact entities.
1. **[reCAPTCHA](real-time-marketing-form-global-settings.md#recaptcha)**: Set up third-party form captcha.

:::image type="content" source="media/real-time-marketing-form-global-settings-general.png" alt-text="General section of global form settings." lightbox="media/real-time-marketing-form-global-settings-general.png":::

## General

The first part of **General** section allows you to set the details of the form configuration itself. You can set the name, select the form type, and label the configuration as default. There can be only one default configuration of the same type.

You can also select if the [form prefill](real-time-marketing-form-prefill.md) is automatically enabled for your newly created forms.

The second part of the **General** section allows you to choose which default action will be taken after the form is submitted. Once submitted, the form can show a *Thank you* notification or you can set the *Error* notification. You can customize the content of both notifications.

## Audience

> [!IMPORTANT]
> A preview feature is a feature that is not complete but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and could have limited or restricted functionality.
>
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won’t be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal or other data that are subject to legal or regulatory compliance requirements.

The **Audience** section allows you to set the default target audience for your newly created forms. The **Audience settings** determine which audience (that is, entity record) is used in the submission processing, and the conditions under which a new record is created or an existing record is updated. All **Audience settings** are visible in the form editor, allowing users to select their preferred audience when creating a new form.

You can either modify the details of the out-of-the-box *Audience settings* or you can create new settings.

:::image type="content" source="media/real-time-marketing-form-global-settings-audience.png" alt-text="Audience section of global form settings." lightbox="media/real-time-marketing-form-global-settings-audience.png":::

The **Marketing form** type comes with three out-of-the-box audience settings:

- **Contact**: Update an existing contact using the selected matching rule (email address, by default). Create a new contact if no existing contact was matched.
- **Lead**: Always create a new lead, even if the same lead already exists (no matching rules are applied).
- **Lead & Contact**: Update an existing contact using the selected matching rule (email address by default). Create a new contact if no existing was matched. Always create a new lead, even if the same lead already exists (no matching rules are applied).

The **Event registration form** type comes with a single out-of-the-box audience setting:

- **Contact**: Update an existing contact using the selected matching rule (email address by default). Create a new contact if no existing contact was matched.

### Audience settings details

You can modify audience settings to specify when a new record is created and how to update an existing record to meet your business process requirements. The following example is valid for a *contact* audience.

:::image type="content" source="media/real-time-marketing-form-global-settings-audience-details.png" alt-text="Audience details in global form settings." lightbox="media/real-time-marketing-form-global-settings-audience-details.png":::

- **Name**: Name your audience settings. This name is visible in the form editor. Use short but descriptive names.
- **Target entity**: Select the target entity targeted by form submission processing. Marketing forms support lead and contact entities, but event registration forms are limited to contact only.

#### Matching rules

Matching rules help to configure how an existing record can be updated or when to create a new one. Matching rules follow the selected **Target entity**. You can see **Contact matching rules** if *Contact* is selected or **Lead matching rules** if *Lead* is selected.

> [!NOTE]
> We use a *Contact* audience in this example. You can see the same details for a *Lead* audience. The *Lead & Contact* audience allows you to set separate details for both contact and lead.

First, **Choose how to handle duplicate contacts**. There are two options:

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

The **Lead-Contact Mapping** section is available only for the *marketing form* type. To use a combined Lead & Contact audience, it's important to define how the attributes are mapped to each other. For example, you need to link the Contact First Name attribute to the Lead First Name attribute, so the form field First Name can update attributes for both entities.

The combined Lead & Contact audience relies on [entity columns mapping](/power-apps/maker/data-platform/map-entity-fields), which can be defined in Power Apps. The mapping uses the *Parent contact* relationship.

> [!IMPORTANT]
> If you use solutions as the mechanism for implementing application lifecycle management (ALM), you should define the mappings as a [solution in Power Apps](/power-apps/maker/data-platform/solutions-overview).

:::image type="content" source="media/real-time-marketing-form-global-settings-mapping.png" alt-text="Mapping in global form settings." lightbox="media/real-time-marketing-form-global-settings-mapping.png":::

In you don't use solutions as the mechanism for implementing application lifecycle management (ALM), you can select **Generate mappings** button to automatically link lead attributes to contact or you can select **Edit in Power Apps** to manually define the mappings.

## reCAPTCHA

Protecting your forms against bot attacks and malicious actors is crucial to ensure the quality of captured data. Marketing and event registration forms come with standard captcha capabilities, but you can also [implement a custom captcha](real-time-marketing-form-custom-captcha.md) to improve the user experience.

The **reCAPTCHA** section allows you to enter the private key for and activate the reCAPTCHA plugin.

:::image type="content" source="media/real-time-marketing-configure-form-recaptcha.png" alt-text="Enter key for reCAPTCHA." lightbox="media/real-time-marketing-configure-form-recaptcha.png":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]
