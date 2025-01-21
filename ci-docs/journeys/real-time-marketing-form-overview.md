---
title: Overview of Customer Insights - Journeys forms
description: Overview of the forms capabilities in Dynamics 365 Customer Insights - Journeys. 
ms.date: 12/12/2024
ms.topic: article
author: petrjantac
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Overview of Customer Insights - Journeys forms

> [!IMPORTANT]
> Dynamics 365 Customer Insights - Journeys may transfer customer data outside of the selected Azure geographic location when using the following features that use Azure CDN (content delivery network) to operate globally:
> - [Asset library](upload-images-files.md)
> -	[Forms](real-time-marketing-form-overview.md)
>
> You can still execute marketing campaigns without using such features by hosting your assets and forms in a content management system of your choice.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=ed9b04ef-a9b2-48b4-ac72-5b8f58d95c5a]

## Form types

There are multiple types of forms in Customer Insights - Journeys:

1. [Marketing form](real-time-marketing-form-overview.md#marketing-form): Capture new leads or contacts.
1. [Event registration form](set-up-event.md): Allow registration to events.
1. [Preference center](real-time-marketing-preference-centers.md): Manage consent preferences.

The **marketing** and **event registration** form types are similar. All features of marketing forms apply to event registration forms, except for audience configuration. Event registration forms can only target a contact audience. Event registration forms have some extra features like dynamic components to render list of sessions, speakers, or details about event. Event registration forms can also create *event registration* records. Event registration forms also have a different publishing user interface.

### Marketing form

A marketing form is an inbound communication channel that allows customers to register for newsletters, ask for quotations, etc. The form is defined by a set of input fields that are arranged into a form layout.

Each marketing form is made from a collection of fields, buttons, graphical elements, and a few configuration settings. Each field included in your form is linked to an attribute of an entity in Customer Insights - Journeys.

The form editor allows you to easily and quickly create and publish forms. You can choose a template or start from scratch. You can also design form content using drag-and-drop elements and preview options. Once your form is ready, you can publish the form in one quick step.

> [!IMPORTANT]
> There's a limit of 2,000 requests/minute per org. The request limit includes visits, lookup, CAPTCHA, and form submission. The limit allows around 100 to 500 submissions/minute, depending on the form.

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
