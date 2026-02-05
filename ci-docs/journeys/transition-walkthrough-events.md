---
title: Transition events from outbound marketing to real-time journeys
description: Learn how to transition event management capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 02/05/2026
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition events from outbound marketing to real-time journeys

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](transition-overview.md).

You can find outbound marketing and real-time journeys events in the **Event planning** work area in Dynamics 365 Customer Insights – Journeys.

Creating events in real-time journeys works mostly the same as in outbound marketing. New features in real-time journeys enhance and improve the overall experience.

To create a new real-time event, select **+ Real-time event** in the top navigation bar. You now see whether the event is created using the outbound marketing or the real-time journeys module in the event record:

:::image type="content" source="media/real-time-event.png" alt-text="Screenshot of the navigation menu for an event in Dynamics 365 Customer Insights – Journeys. The menu shows options to distinguish between outbound marketing and real-time journeys events." lightbox="media/real-time-event.png":::

> [!NOTE]
> The system shows a warning if you create outbound marketing events scheduled to start or end after outbound marketing is removed.

## Comparison of outbound marketing and real-time journeys events

Event management comprises three areas:

1. **Event setup**: Event setup includes the creation of events, setup sessions, tracks, speakers, room reservations, and more.
1. **Event registration**: Event registration includes the registration form, custom unmapped fields, and publishing the event.
1. **Event communication**: Event communications include invitations, event registration confirmation, reminders, and post-event follow-ups.

### Event setup

Creating and setting up events, tracks, sessions, speakers, and registrants is a similar experience in real-time journeys. But there are adjustments and improvements with each new feature in real-time journeys. Real-time journeys includes these capabilities:

- Multi-session registration in real-time journeys events lets you manage event and session capacity more efficiently. For more information, see [Set up session-level registration](real-time-journeys-event-session.md).
- Waitlist is now a registration status and works for events and sessions at the same time. For more information, see [Set up and manage an event waitlist](set-up-and-manage-waitlist.md).
- Custom registration fields are now managed in the form editor and answers are part of the form submission response. For more information, see [Create unmapped fields for registration forms](create-unmapped-fields-registration-forms.md).
- Event passes can now be found on a dedicated tab called **Passes**. For more information, see [Set up event passes (preview)](real-time-journeys-event-passes.md).
  
### Event registration and publishing

The registration experience uses the [registration form](event-registration-experience.md#event-registration-form), a type of [Customer Insights - Journeys form](real-time-marketing-form-overview.md), or the events API [Using the events API in real-time journeys](developer/using-rtm-events-api.md).

There are various options to build an event registration experience depending on whether you want to build a single registration page or an event portal.

#### Single registration page

- **Registration form hosted as a standalone page**: A single page containing the registration form with all details about the event. The page is hosted on Customer Insights infrastructure and requires no extra license. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).
- **Registration form embedded into your website**: You can embed the event registration form into your own website. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).

#### Event registration portal

- **Registration portal on Power Pages**: You can use the event registration template to build a website using Power Pages studio. For more information, see [Build an event registration website using Power Pages](event-portal-template.md).
- **Registration portal on your own domain built with the web application**: Use the out-of-box web application to build a registration portal hosted on your own domain. For more information, see [Create an event portal on your website using the web application](developer/event-portal-web-application.md).
- **Custom solution using the events API**: For more information, see [Using the events API in real-time journeys](developer/using-rtm-events-api.md).

### Event communication

Event-related communication in real-time journeys provides out-of-box triggers such as **Marketing event registration created**, **Marketing event check-in created**, and **Marketing event registration canceled**. You can communicate with attendees more quickly, as shown in the following diagram.

:::image type="content" source="media/event-planning-rtjourneys.png" alt-text="Transition event planning diagram." lightbox="media/event-planning-rtjourneys.png":::

While the process of inviting and registering attendees is consistent with that in outbound marketing, you need to create new emails and journeys for communication about events. For more information, see [transition segments, emails, journeys, and assets](transition-walkthrough-segments.md).

## Transition guidance

The following sections cover transition guidance for real-time events.

### Timing of the transition

At this point, all new events will be by default created as Real-time events. As described in the [transtion FAQ document](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/transition-faqs#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working), we are in the Phase 4 of Outbound marketing removal so unless you have been granted an extension, you need to transition all your events immediately. 

### Migration path

To transition your events and related communication:

1. Migrate all event-related communication to real-time journeys regardless of whether you’re using outbound or real-time events. Journey orchestration, segmentation, and other assets also work with outbound event registrations. 
1. Transition the event registration experience per the guidance in [Transition of event registration experience](#transition-of-event-registration-experience).
1. Perform an analysis of Outbund events. Draft events or Live events without any registration should be created in Real-time marketing instead.
1. If possible, minimize the number of events that have a registration period open after outbound marketing removal, but for those events that are live, already have registrations, and their end date is after the outbound removal, consider using the [Event registration migration tool](event-migration.md) to migrate the existing registrations from Outboudn to Real-time event.

#### Transition of event registration experience

There were multiple options on how to build an event registration experience in outbound marketing. Each of these options has a slightly different migration path:

- **Event portal hosted on Power Portals**: Build a new event registration website using the Power Pages template. For more information, see [Build an event registration website using Power Pages](event-portal-template.md).
- **Event portal not hosted on Power Portals**: The recommended migration path is to build a new event registration experience using the new web application. For more information, see [Create an event portal on your website using the web application](developer/event-portal-web-application.md).
- **Outbound marketing form for event registration**: Replace these forms with real-time journeys event registration forms. For more information, see [Open the event management work area](open-events.md).
- **Custom solution using outbound marketing event management API (not using Angular application)**: Use the new events API. For more information, see [Using the events API in real-time journeys](developer/using-rtm-events-api.md).

For more information, see [Transition event registration experience](migrate-event-registration.md).

## Other relevant features

Here are other relevant and upcoming features to consider when transitioning events from outbound marketing to real-time journeys:

- **Recurring events**: We don't have a published roadmap for this capability. You can set up the first event in the series and then use it as a template by using the **Save as** functionality to create copies of the event. Alternatively, for simpler events, use can use sessions to represent events in the series.
- **Event templates**: We don't have a published roadmap for this capability. Create an event that you use as a starting point. Then use the **Save as** functionality to create copies of the event that you can then edit and customize for your needs.
- **Integration with ON24**: Contact On24 support for next steps. They can provide guidance for existing customers. We don't plan to introduce this integration in real-time journeys.

## Frequently asked questions

*How are outbound marketing and real-time journeys events different?*

As with other parts of the system, real-time journeys events are built on advanced technology that lets us scale our product and offer the most up-to-date, secure experience. The biggest difference is the event registration experience. Another difference is that when introducing new capabilities to real-time journeys events, we consider feedback received from years of experience with outbound marketing events. For more information, see [Real-time transition](transition-faqs.md#why-should-i-transition-to-real-time-journeys).

*What will happen once outbound marketing is removed?*

Events are a shared capability between real-time journeys and outbound marketing; the same tables are used. The tables and data won't be removed but there are some critical differences in the event forms and pages between outbound marketing and real-time journeys. Therefore, events created from outbound marketing stop working once outbound marketing is removed.

*What will happen with registrations in outbound marketing events?*

Outbound marketing registration records stay visible in the contact record because they're Dataverse entities. If you have Outbound event with registrations which is ending after the outbound marketing is removed, consider using the [Event registration migration tool](event-migration.md) to migrate the existing registrations from Outbound to Real-time event.

*Do I have to migrate my event portal?*
 
 Yes, please visit [Transition of event registration experience](#transition-of-event-registration-experience) to understand your options.

 *Is the angular app used for events portal in Outbound marketing being deprecated?*

 As part of outbound removal, we do not remove your Angular app based portal. While you can continue to use the portal, we strongly recommend that you move to new portals built using power pages or other technologies of your choice as we will no longer maintain the app and Microsoft will no longer provide any new security updates. Please visit [Transition of event registration experience](#transition-of-event-registration-experience) to understand your options.

*Will the event data tables change?*

The data structure for real-time journeys events is the same as outbound marketing for now, but as we introduce changes and enhancements to the system, we might implement some features differently.

*For any features that haven't been introduced yet, can we assume that they work the same way?*

We're trying to avoid making any model changes to the basic event entities. We don't recommend building custom solutions on system entities for features that aren't yet available in real-time journeys as this might present a certain level of risk.

*Is there any tool that helps me transition my live events?*

No. Any live events that accept registrations need to have registration closed before outbound marketing removal. After outbound marketing removal, we'll no longer process registrations submitted using outbound marketing forms.

*What should I do if the features I need for event planning aren't available?*

There are no planned features that are considered transition blockers for the event management area.

## Blogs and workarounds

Here are some relevant blogs and workarounds:

- Cascaded fields where options in a field depend on a value in a previous field that isn't supported yet. For more information, see the blog [Implementing cascading dropdown fields in real-time journeys forms](https://community.dynamics.com/blogs/post/?postid=ff86d88f-d892-ef11-ac21-6045bdd7e1ae).
- Sending timed reminders before an event. For more information, see [Boost event engagement with journeys](real-time-marketing-event-registration-journey.md#step-2-send-email-reminders-seven-days-and-one-day-before-the-event).
- Localization of date and time format for sessions. For more information, see [Why localized dates and times matter in event registration](https://community.dynamics.com/blogs/post/?postid=8795951f-7baa-f011-bbd3-00224826f06d)

## Developer guidance

If you aren't using the out-of-the-box event record creation form, distinguish an outbound marketing record from a real-time journeys record by setting the **Marketing module** attribute on the Event table (**msevtmgt_sourcesystem**).

- **100000001** - Outbound marketing
- **100000002** - Real-time journeys

If the value is **null**, the record is an **outbound marketing** event. For noncustomized forms and the out-of-the-box flow, this value is set automatically.

Existing event forms that were customized for outbound marketing events won't work for real-time journeys events. Crucial tabs might be hidden on a customized form. For example, the **Forms** tab is needed for real-time journeys events to operate as the registration form and session-level settings are set on that tab.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
