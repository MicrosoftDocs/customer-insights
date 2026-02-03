---
title: Overview of Customer Insights - Journeys forms
description: Overview of the forms capabilities in Dynamics 365 Customer Insights - Journeys. 
ms.date: 02/09/2025
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
> * [Asset library](upload-images-files.md)
> * [Forms](real-time-marketing-form-overview.md)
>
> You can still execute marketing campaigns without using such features by hosting your assets and forms in a content management system of your choice.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=ed9b04ef-a9b2-48b4-ac72-5b8f58d95c5a]

> [!IMPORTANT]
> The current HIP captcha used in Customer Insights - Journeys forms will be deprecated in March 2026 and fully removed by June 30, 2026.
> Please follow these instructions to keep your forms protected against bot submissions.

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

## Security notice

Security is an important aspect of marketing and event registration forms. Customer Insights - Journeys takes the following precautions to avoid any security risks:

- The Customer Insights - Journeys app accepts form submissions only from [domains allowed for external form hosting](domain-authentication.md). This security precaution applies for both forms and form capture.
- Forms can be rendered only on domains allowed for external form hosting.
- The out-of-box domain for forms hosted as a standalone page is enabled for external form hosting by default. Learn more: [Publish your form](real-time-marketing-form-create.md#publish-your-form)
- To avoid form submissions by bots, you should protect forms with a captcha. The form editor includes an out-of-the-box captcha option, but you can use any other third-party captcha service to improve the user experience. Learn more: [Integrate a custom captcha service with Customer Insights - Journeys forms](real-time-marketing-form-custom-captcha.md)
- The Customer Insights - Journeys app infrastructure contains necessary precautions to minimize the consequences of a possible DDoS attack. To prevent DDoS attacks, there's a limit of 2,000 requests/minute per org. The request limit includes visits, lookups, CAPTCHA, and form submissions. The limit allows around 100 to 500 submissions/minute, depending on the form.

## Privacy notice

- Marketing and event registration forms don't use any cookies. Form visit and form submit interactions use a [journey link tracking mechanism](real-time-marketing-link-tracking-mechanics.md) to get details about known users.

## Next steps

- [Create Customer Insights - Journeys forms](real-time-marketing-form-create.md)
- [Manage Customer Insights - Journeys forms](real-time-marketing-manage-forms.md)
- [Troubleshooting Customer Insights - Journeys forms](real-time-marketing-troubleshooting-forms.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
