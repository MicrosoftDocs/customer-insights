---
title: Build event registration portal with Power Pages Studio
description: Build event registration portal with Power Pages template designed for Customer Insights - Journeys Event Management
ms.date: 1/3/2025
ms.topic: article
author: petrjantac
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# PREVIEW: Build event registration website using Power Pages Studio

> [!IMPORTANT]
> A preview feature is a feature that is not complete but is made available before it’s officially in a release so customers can get early access and provide feedback. Preview features aren’t meant for production use and may have limited or restricted functionality.
>
> Microsoft doesn't provide support for this preview feature. Microsoft Dynamics 365 Technical Support won’t be able to help you with issues or questions. Preview features aren’t meant for production use, especially to process personal data or other data that are subject to legal or regulatory compliance requirements.

Microsoft [Power Pages](https://learn.microsoft.com/power-pages/introduction) is a secure, enterprise-grade, low-code software as a service (SaaS) platform for creating, hosting, and administering modern external-facing business websites.

You can create an event registration website simply by using the Event Registration template. The template contains multiple pages for the whole registration process:

- Home - list of all events, which are enabled for this website
- Events - detail of event including list of speakers and sessions. This page is dynamic and the content is loaded based on the event selected in the Home page.
- Register to Event - page with event registration form. The registration form is dynamic. Each event can have a different registration form.

> [!IMPORTANT]
> Using Power Pages requires extra license. You can test Power Pages using a free trial. [Learn more](https://learn.microsoft.com/power-pages/go-live/assign-licensing) about licensing.

Power Pages combined with event registration template unlock powerful scenarios such as:

- Style and customize your website in Power Pages Studio editor
- [Set custom domain name for event registration website](#set-custom-domain-name-for-event-registration-website)
- [Create multiple event registration websites](#create-multiple-event-registration-websites)
- Each event can have a different registration form without the need to change any code
- Explore more [Power Pages capabilities](https://learn.microsoft.com/power-pages/capabilities)

## Step-by-step guide to build event registration website

This guide shows all step to create event registration website using Power Pages Studio and the new event registration template for Customer Insights - Journeys. The guide has two parts:

- Create website in Power Pages
- Configure website in Customer Insights - Journeys

If you encounter any issues while creating or editing your website, please refer to [Power Pages documentation](https://learn.microsoft.com/power-pages/introduction).

### Create website in Power Pages

1. **Create a new website**. Enter [https://make.powerpages.microsoft.com/](https://make.powerpages.microsoft.com/) in your browser to open Power Pages Studio. Select the right environment in the top right corner. Select *Start with a template*.
    :::image type="content" source="media/event-pp-template-create.png" alt-text="Create a new website." lightbox="media/event-pp-template-create.png":::
1. **Find Event Portal** template in Dynamics 365 section and select *Choose this template*.
    :::image type="content" source="media/event-pp-template-select.png" alt-text="Select a template." lightbox="media/event-pp-template-select.png":::
1. **Name your site**, set language. You can change the web address later to [use your own domain name](#set-custom-domain-name-for-event-registration-website). Select *Done* in the bottom right corner. It takes a few minutes to get your site ready. You can check the status of your newly created website in the list of Active sites.
1. Once your site is ready, select the *Edit* button to customize your website. Your new website is created as Private, not accessible for external audience.
1. The **Home** page contains the list of events. You can [customize what information about event is displayed](#customize-displayed-information-about-event-in-card-gallery-control) in the list of events by selecting the *Card gallery* control on the canvas. You can also easily change the hero image, logo in the page header, page footer, etc.
1. **Preview your website** by selecting the Preview button in the top right corner. You may need to enable pop-up windows to display the preview.
1. **Publish your website** by following the [Go-live checklist](https://learn.microsoft.com/power-pages/go-live/checklist).

### Configure website in Customer Insights - Journeys

1. **Create a new Power Pages Website configuration** to link your Power Pages website with Customer Insights - Journeys and simplify the event publishing for your event planners. Navigate to *Power Pages Websites* section of Event Management in *Settings*. Select *+ New* to create a new configuration.
    :::image type="content" source="media/event-pp-template-website-config.png" alt-text="Create a new website configuration." lightbox="media/event-pp-template-website-config.png":::
    Set the *Name* of your website configuration, which is visible to event planners so they can select on which website the event is hosted. Fill in the *Homepage URL*, which is the URL of your Power Pages website. To get your website URL, navigate to Power Pages Studio, select *Set up* in the left pane, and find the URL in the Site details. Select *Save & Close*.
1. **Enable [external form hosting](domain-authentication.md)** and optionally prefill for your Power Pages domain. *External form hosting* and *Prefill* can be enabled in *Settings* -> *Domains*.
1. **Create a new event** or edit an existing one. Navigate to the *Website and form* tab. Select *Power Pages website* as the destination of *Where do you want attendees to register for this event*. You default *Registration website* is automatically set. You can also change the form, which is used for this event. Each event can use a different form although these events are hosted on the same website.
    :::image type="content" source="media/event-pp-template-new-event.png" alt-text="Create a new event." lightbox="media/event-pp-template-new-event.png":::
1. Save your event and **Go live**.
1. Check your event listed in the preview or live version of your Power Pages website.

## Event registration website customization

### Customize displayed information about event in card gallery control

The card gallery control renders the list of events. You can choose from variety of layouts.

You can change what information is displayed about the event in the *Data* section of card gallery design. The Data source defines which entity records are listed. Always keep *Event* as the Data source. You can limit which events are displayed on this website by selecting a custom view as the *View* for card gallery.
:::image type="content" source="media/event-pp-template-card-gallery.png" alt-text="Customize card gallery." lightbox="media/event-pp-template-card-gallery.png":::

### Set custom domain name for event registration website

The custom domain name can be set in Power Platform admin center. [Learn more](https://learn.microsoft.com/power-pages/admin/add-custom-domain).

> [!IMPORTANT]
> Once you assign a custom domain name to your Power Pages website, check the following:
>
> - Your custom domain name is enabled for [external form hosting](domain-authentication.md). Otherwise the registration form cannot be rendered on your website.
> - The Power Pages Website configuration in Customer Insights - Journeys points to the right Home page URL. [Learn more](#power-pages-website-configuration-in-customer-insights---journeys).

### Create multiple event registration websites

It's possible to create multiple event registration websites and set which event is displayed on which website. Some events can be public while other events can be private only for authenticated users.

1. Build at least two websites in Power Pages using the Event Registration template.
1. Create multiple [*Power Pages Website* configuration in Customer Insights - Journeys Settings](#power-pages-website-configuration-in-customer-insights---journeys) and link each configuration to the correct Power Pages website. This allows the event planner to select the correct website while setting up the event in Event Management. A savedQuery with the filtering of events for that specific website is automatically created. This automatically generated view can't be customized, but you can save it as a new view to customize it.
1. Open the card gallery control in Power Pages Studio, which lists the events on the Home page, and [set the corresponding view as the *View*](#customize-displayed-information-about-event-in-card-gallery-control).

### Custom components for event registration

The event registration template uses multiple custom components such as Event Registration Form, Event Speaker Section, Event Session Section, etc. To add one of these custom components, select the plus icon on the canvas and review the list of Custom components. You can build your own pages applying these custom components as the building blocks.

### Power Pages Website configuration in Customer Insights - Journeys

This configuration links your Power Pages website with Customer Insights - Journeys and simplifies the event publishing for your event planners. Navigate to *Power Pages Websites* section of Event Management in *Settings*. Select *+ New* to create a new configuration. Or select an existing configuration to edit it.

:::image type="content" source="media/event-pp-template-website-config.png" alt-text="Create a new website configuration." lightbox="media/event-pp-template-website-config.png":::

You can set the following parameter of your website:

- The *Name* of your website configuration is visible to event planners so they can select on which website the event is hosted.
- The *Homepage URL* is the URL of your Power Pages website. To get your website URL, navigate to Power Pages Studio, select *Set up* in the left pane and find the URL in the Site details.
- The *Registration page URL* is an optional parameter. If you want to use a custom registration page instead of the Events page provided in the template, enter the page URL here.
- *Default website* defines if this configuration is selected as default for your newly created events hosted on Power Pages website.

> [!IMPORTANT]
> Updating the Homepage URL and/or Registration page URL of the existing configuration, automatically updates the public URL of all the events using this website configuration.