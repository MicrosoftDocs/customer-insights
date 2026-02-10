---
title: Overview of Customer Insights - Journeys forms
description: Overview of the forms capabilities in Dynamics 365 Customer Insights - Journeys. 
ms.date: 02/04/2026
ms.topic: article
author: petrjantac
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Overview of Customer Insights - Journeys forms

> [!IMPORTANT]
> Dynamics 365 Customer Insights - Journeys may transfer customer data outside of the selected Azure geographic location when using the following features that use Azure CDN (content delivery network) to operate globally:
>
> - [Asset library](upload-images-files.md)
> - [Forms](real-time-marketing-form-overview.md)
>
> You can still execute marketing campaigns without using such features by hosting your assets and forms in a content management system of your choice.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=ed9b04ef-a9b2-48b4-ac72-5b8f58d95c5a]

> [!IMPORTANT]
> The current HIP captcha used in Customer Insights - Journeys forms will be deprecated in March 2026 and fully removed by June 30, 2026.
> Please follow these **[instructions](real-time-marketing-form-security-privacy.md#hip-captcha-deprecation-and-new-recaptcha-experience)** to keep your forms protected against bot submissions.

## Form types

There are multiple types of forms in Customer Insights - Journeys:

1. [Marketing form](real-time-marketing-form-overview.md#marketing-form): Capture new leads or contacts.
1. [Event registration form](event-registration-experience.md): Allow registration to events.
1. [Preference center](real-time-marketing-preference-centers.md): Manage consent preferences.

The **marketing** and **event registration** form types are similar. All features of marketing forms apply to event registration forms, except for audience configuration. Event registration forms can only target a contact audience. Event registration forms have some extra features like dynamic components to render list of sessions, speakers, or details about event. Event registration forms can also create *event registration* records. Event registration forms also have a different publishing user interface.

### Marketing form

A marketing form is an inbound communication channel that allows customers to register for newsletters, ask for quotations, etc. The form is defined by a set of input fields that are arranged into a form layout.

Each marketing form is made from a collection of fields, buttons, graphical elements, and a few configuration settings. Each field included in your form is linked to an attribute of an entity in Customer Insights - Journeys.

The form editor allows you to easily and quickly create and publish forms. You can choose a template or start from scratch. You can also design form content using drag-and-drop elements and preview options. Once your form is ready, you can publish the form in one quick step.

> [!IMPORTANT]
> There's a limit of 2,000 requests/minute per org. The request limit includes visits, lookup, CAPTCHA, and form submission. The limit allows around 100 to 500 submissions/minute, depending on the form.

> [!WARNING]
> Bulk edit for forms is not supported. Using bulk edit can result in loss of form data.

## Form templates

There are several default, out-of-the-box form templates that are provisioned with Customer Insights - Journeys. You can also create your own custom form templates.

### Out-of-the-box form templates

You can use the out-of-the-box templates to quickly create a new form.

> [!IMPORTANT]
> All changes to the out-of-the-box templates can be reverted with an update to a newer version of Customer Insights - Journeys. If you want to customize out-of-the-box template, create a copy using the *Save as* feature.

### Custom form templates

Custom form templates simplify creating marketing and event registration forms. Custom templates can reflect styling adjustments to align with your style guide. You can set the audience configuration for the template and adjust the consent to meet your requirements.

To create a new custom form, navigate to the **Templates** section in the left site navigation. Select the **New template** button in the top ribbon and choose **Form**. You can access the list of all your form templates from the **Templates** page by selecting the **Form** tile.

:::image type="content" source="media/real-time-marketing-custom-form.png" alt-text="Custom form template" lightbox="media/real-time-marketing-custom-form.png":::

> [!TIP]
> If you want to use an existing form as a new custom template, you can copy its HTML code and paste it into the newly created custom template.

## Next steps with Customer Insights - Journeys forms

- [Create form](real-time-marketing-form-create.md): create your first form with step-by-step guide
- [Understand how forms work](real-time-marketing-manage-forms.md): edit live forms, unpublish, form field properties, styling, audience configuration, customizations.
- [Troubleshooting forms](real-time-marketing-troubleshooting-forms.md): resolve common issues
- [Security & privacy](real-time-marketing-form-security-privacy.md): learn about forms security
- [Deploy pages with forms](real-time-marketing-deploy-pages.md): embed your form into your own domain or Power Pages website
- [Form prefill](real-time-marketing-form-prefill.md): populate form fields with known values for your existing customers
- [Unmapped fields](real-time-marketing-forms-custom-fields.md): gather additional information about your customers without creating a new lead or contact attributes
- [Default form configuration](real-time-marketing-form-global-settings.md): define default configuration for your newly created forms including reCAPTCHA
- [Use submitted values](real-time-marketing-form-submitted-values.md): branch journeys and personalize DOI emails using submitted values
- [Filter cities by country/region](real-time-marketing-filter-cities-by-country-region.md)

### Extend forms functionality

- [Extend forms using code](developer/realtime-marketing-form-client-side-extensibility.md): use Javascript API to customize form behavior
- [Form capture](real-time-marketing-form-capture.md): get submissions from existing forms that weren't created using the Customer Insights - Journeys form editor
- [Customize form submission validation](real-time-marketing-form-customize-submission-validation.md)
- [Customize form editor](developer/extend-ui.md): add additional attributes to your form settings

[!INCLUDE [footer-include](./includes/footer-banner.md)]
