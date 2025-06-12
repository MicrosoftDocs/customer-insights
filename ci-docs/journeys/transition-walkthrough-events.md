---
title: Transition events from outbound marketing to real-time journeys
description: Learn how to transition event management capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/12/2025
ms.topic: how-to
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition events from outbound marketing to real-time journeys

> [!IMPORTANT]
> The [outbound marketing](/dynamics365/customer-insights/journeys/user-guide) module will be removed from Customer Insights - Journeys on June 30, 2025. To avoid interruptions, transition to real-time journeys before this date. For more information, see [Transition overview](transition-overview.md).

## Key information

You can find outbound marketing and real-time journeys events in the **Event planning** work area in Dynamics 365 Customer Insights – Journeys.

Creating events in real-time journeys is mostly the same as in outbound marketing. However, with new features in real-time journeys, the experience is improved and enhanced.

To create a new real-time event, you can select **+ Real-time event** in the top navigation bar. You can now easily see whether the event is created using the outbound marketing or the real-time marketing module in the event record:

:::image type="content" source="media/real-time-event.png" alt-text="Navigation menu of an event." lightbox="media/real-time-event.png":::

> [!NOTE]
The system displays a warning if you create outbound marketing events with a start or end date that falls after the removal of outbound marketing.

## Comparison of outbound marketing and real-time journeys events

Event management comprises three areas:

1. **Event setup**: Setup includes the creation of events, setup sessions, tracks, speakers, room reservations, and more.
1. **Event registration**: Registration includes the registration form, custom unmapped fields, and publishing the event.
1. **Event communication**: Communications include invitations, event registration confirmation, reminders, and post-event follow-ups.

### Event setup

Creating and setting up events, tracks, sessions, speakers, and registrants are a similar experience in real-time journeys. However, we make adjustments and improvements with every new feature we implement. Real-time journeys includes the following capabilities:

- Multi-session registration in real-time journeys events lets you manage the capacity of events and sessions more efficiently. For more information, see [Set up session-level registration](real-time-journeys-event-session.md).
- Waitlist is now a status of a registration and works for both events and sessions at the same time. For more information, see [Preview: Set up and manage an event waitlist](set-up-and-manage-waitlist.md).
- Custom registration fields are now managed in the form editor and answers are part of the form submission response. For more information, see [Create unmapped fields for registration forms (preview)](create-unmapped-fields-registration-forms.md)

### Event registration and publishing

The registration experience in real-time journeys is powered by an [event registration form](event-registration-experience.md#event-registration-form), a type of [Customer Insights - Journeys form](real-time-marketing-form-overview.md). Real-time journeys event registration forms offer enhanced personalization options that let you reuse forms for different events. The forms can bring in dynamic content including event name, location, list of speakers, sessions, and more. You can [create an event registration experience](event-registration-experience.md) in the following ways:

- **Registration form hosted as a standalone page**: A single page containing the registration form with all details about the event. The page is hosted by the Customer Insights - Journeys infrastructure, and no extra license is needed. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).
- **Registration form embedded into your website**: You can embed the event registration form into your website. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).
- **Registration portal on Power Pages**: You can use the event registration template to [Build a website using Power Pages Studio](event-portal-template.md).
- **Custom solution using events API**: For more information, see [Using events API in real-time journeys](/dynamics365/customer-insights/journeys/developer/using-rtm-events-api).

The following features are being planned to enhance event registration and publishing:

- [Create event portals with event and registration details using Power Pages - GA](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/enable-customers-find-sign-up-events-easily).
- [Create event portals with event and registration details on your own website - GA](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/create-event-portal-own-website).

### Event communication

Event-related communication in real-time journeys provides out-of-box triggers such as **Marketing event registration created**, **Marketing event check-in created**, and **Marketing event registration canceled**. You can communicate with attendees more quickly, as shown in the following diagram.

:::image type="content" source="media/event-planning-rtjourneys.png" alt-text="Transition event planning diagram." lightbox="media/event-planning-rtjourneys.png":::

While the process of inviting and registering attendees is consistent with that in outbound marketing, you need to create new emails and journeys for communication about events. For more information, see [transition segments, emails, journeys, and assets](transition-walkthrough-segments.md).

## Transition guidance

The following sections cover transition guidance for real-time events.

### Timing of the transition

Real-time events are available for all customers. Start transitioning as soon as possible. All events that don't require features in the roadmap should be created as real-time events by default.

The event schedule should also be taken into consideration when crafting the transition schedule. The key decision point is registration start and end date. If the registration period ends before the planned outbound marketing removal date, the event can still be created as outbound marketing event, even if the event takes place in the future. 

### Migration path

To transition your events and related communication:

1. Migrate all event-related communication to real-time journeys regardless of whether you’re using outbound or real-time events. Journey orchestration, segmentation, and other assets also work with outbound event registrations.
1. Identify new events you're planning to run and check whether there's any critical functionality stopping you from using real-time journeys. If there are no gaps identified, then create all new events in real-time journeys only.
1. Create the event registration experience per the guidance in the next section.
1. If possible, minimize the number of events that have a registration period open after outbound marketing removal. 

#### Transition of event registration experience

There were multiple options on how to build an event registration experience in outbound marketing. Each of these options has a slightly different migration path:

- **Event portal hosted on Power Portals** – Build a new event registration website using the Power Pages template. For more information, see [Build an event registration website using Power Pages](event-portal-template.md).
- **Event portal not hosted on Power Portals** – The recommended migration path is to build a new event registration experience using the new code snippet listing once available.
- **Outbound marketing form for event registration** – Replace these forms with real-time journeys event registration forms. For more information, see [Open the event management work area](open-events.md).
- **Custom solution using outbound marketing event management API (not using Angular application)** – Use the new events API. For more information, see [Using the events API in real-time journeys](developer/using-rtm-events-api.md).

For more information, see [Transition event registration experience](migrate-event-registration.md)

## Other relevant features 
- Set registration end date - On our roadmap, expected to release in October 2025 (subject to change).
- Set up event passes and payment gateway - On our roadmap, expected to release in October 2025 (subject to change).
- Recurring events - We do not have a published roadmap for this capability. You can set up the first event in the series and then use it as a template by using the “save as” functionality to create copies of the event. Alternatively, for simpler events, use can use sessions to represent events in the series.
- Event templates - We do not have a published roadmap for this capability. Create an event that you use as a starting point. Then use the “save as” functionality to create copies of the event that you can then edit and customize for your needs.
- Integration with ON24 - Contact On24 support for next steps. They can provide guidance for the existing customers.

## Frequently asked questions

*How are outbound marketing and real-time journeys events different?*

As with other parts of the system, real-time journeys events are built on the most advanced technology that lets us scale our product and offer the most up-to-date secure first-driven experience. The biggest difference is the event registration experience. Another difference is that when introducing new capabilities to real-time events, we consider feedback received from years of experience with outbound events and introduce several improvements. For more information, see [Real-time transition](transition-faqs.md#why-should-i-transition-to-real-time-journeys).

*What will happen once outbound marketing is removed?*

Events are a shared capability between real-time journeys and outbound marketing—the same tables are used. The tables and data won't be removed. However, there are some critical differences in the event forms and pages between outbound marketing and real-time journeys. Therefore, events created from outbound marketing stop working once outbound marketing is removed.

*What will happen with registrations in outbound marketing events?*

The outbound marketing registration records continue to be visible in the contact record as it's a Dataverse entity.

*Will the event data tables change?*

The data structure for real-time journeys events is the same now, but as we introduce changes and enhancements to the system, we might implement certain features differently.

*For any features that haven't been introduced yet, can we assume that they work the same way?*

We're trying to avoid making any model changes to the basic event entities. We don't recommend building custom solutions on system entities for features that aren't yet available in real-time journeys as this might present a certain level of risk.

*Is there any tool that helps me transition my live events?*

No. Any events that are live and are accepting registrations have to have the registration closed before the outbound removal. After the outbound removal, we'll no longer process registrations submitted via outbound forms.

*What should I do if the features I need for event planning aren't available?*

The most used features have a planned release date before the outbound removal date. We understand there might be some features that are important for your business and might not be available yet. You can *phase your transition*. Any events that don't need those features can be created as real-time events. You can also transition all your communication to real-time as outbound events can be used with real-time journeys and emails. This reduces the number of assets you need to transition closer to the date. You can also request an extension. For more information, see [How to request an extension](transition-faqs.md#i-cant-transition-by-the-outbound-marketing-removal-date-can-i-request-an-extension)

## Blogs and workarounds
- Cascaded fields where options provided in a field depend on a value in an earlier field that isn't yet supported. For more information, see the blog [Implementing cascading dropdown fields in real-time journeys forms](https://community.dynamics.com/blogs/post/?postid=ff86d88f-d892-ef11-ac21-6045bdd7e1ae).
- Sending timed reminders before an event. For more information, see [Boost event engagement with journeys](real-time-marketing-event-registration-journey.md#step-2-send-email-reminders-seven-days-and-one-day-before-the-event).

## Developer guidance 

If you're not using the out-of-the-box event record creation form, the way to distinguish an outbound marketing versus a real-time journeys record is by setting the **Marketing Module** attribute on the Event table (**msevtmgt_sourcesystem**).
- **100000001** - Outbound marketing
- **100000002** - Real-time journeys

If the value is **null**, the record created will be an **outbound marketing** event. For noncustomized forms and the out-of-the-box flow, this is automatically defined.

Existing event forms that were customized for Outbound marketing events won't work for Real-time marketing events. Crucial tabs may be hidden on a customized form. For example, the "Website and Forms" tab is needed for Real-time events to operate as the registration form and session level settings are set on that tab.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
