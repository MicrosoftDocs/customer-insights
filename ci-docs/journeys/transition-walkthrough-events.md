---
title: Outbound marketing to real-time journeys transition guide for events
description: Learn how to transition event management capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 01/29/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Outbound marketing to real-time journeys transition guide for events

> [!IMPORTANT]
> The [Outbound marketing](/dynamics365/customer-insights/journeys/user-guide) module will be removed from Customer Insights - Journeys on June 30, 2025. To avoid interruptions, transition to real-time journeys before this date. For more information, see [Transition overview](transition-overview.md).

## Key information

Outbound marketing (OBM) and Real-time journeys events are jointly presented under the Event planning work area in Dynamics 365 Customer Insights – Journeys.

The experience of creating events in Real-time journeys remains mostly unchanged. However, with the introduction of new features, we're improving and enhancing your experience with Outbound marketing.

> [!NOTE]
> When creating Outbound marketing events with a start or end date post the Outbound-removal date, you'll see a warning that you have to acknowledge.

## Comparing Outbound and Real-time marketing events

Event management comprises three areas:

1. **Event set up**: Creation of events, set up sessions, tracks, speakers, room reservations, and more.
1. **Event registration**: Registration form, custom unmapped fields, publishing of the event.
1. **Event communication**: Invitations, event registration confirmation, reminders, and post-follow ups.

### Event set up

Creation and set up of events, tracks and sessions, speakers, and registrants work the same way in Real-time journeys with two differences:

- Multi-session registration in Real-time journeys events allows you to manage capacity of events and sessions more efficiently. For more information, see [Set up session-level registration](real-time-journeys-event-session.md).
- Improved registration and publishing experience. For more information, see [Create an event registration experience in Customer Insights - Journeys](event-registration-experience.md).

The following features are relevant as you transition from Outbound marketing to Real-time journeys. These features provide better functionality than those available in Outbound marketing:

- [Maximize event capacity with waitlist registration](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/maximize-event-capacity-waitlist-registrations).
- Registration end date (available March 2025).
- Event passes (available March 2025).

### Event registration and publishing

The registration experience in Real-time journeys is powered by a [event registration form](event-registration-experience.md#event-registration-form); a type of [Customer Insights - Journeys form](real-time-marketing-form-overview.md). Real-time journeys event registration forms offer enhanced personalization options, allowing you to re-use forms between events by bringing in dynamic content (such as event name, location, list of speakers, sessions, and more). There are various options how to [Create event registration experience](event-registration-experience.md):

- Registration form hosted as a standalone page: A single page containing the registration form with all details about the event. The page is hosted on Customer Insights - Journeys infrastructure and no extra license is needed. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).
- Registration form embedded into your website: You can embed the event registration form into your website. For more information, see [Publish your form](real-time-marketing-form-create.md#publish-your-form).
- Registration portal on Power Pages: You can use the event registration template to [build a website using Power Pages Studio](event-portal-template.md).
- Custom solution using events API. For more information, see [Using events API in real-time journeys](/dynamics365/customer-insights/journeys/developer/using-rtm-events-api).

**Relevant upcoming features for event registration and publishing:**

- [Custom unmapped fields](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/collect-extra-customer-information-without-creating-custom-attributes).
- [Create event portals with event and registration details using Power Pages](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/enable-customers-find-sign-up-events-easily).
- [Create event portals with event and registration details on your own website](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/create-event-portal-own-website).

### Event communication

Event-related communication in Real-time journeys is more efficient due to the availability of out of box triggers such as Marketing event registration created, Marketing event check in created, and Marketing event registration canceled.

Event-based communications in Real-time journeys allow for more timely communication with attendees. This is illustrated in the following diagram:

:::image type="content" source="media/event-planning-rtjourneys.png" alt-text="Transition event planning diagram." lightbox="media/event-planning-rtjourneys.png":::

While the process of inviting and registering attendees is consistent with what was available in Outbound marketing, communication about events requires new emails and journeys to be created. For more information, see [transition segments, emails, journeys, and assets](transition-walkthrough-segments.md).

## Transition guidance

The following sections cover transition guidance for Real-time events.

### Timing of the transition

Real-time events are available for all customers. It's recommended to start transitioning as soon as possible. All events that don't require features in the roadmap should be created as Real-time events by default.

The event schedule should also be taken into consideration when crafting the transition schedule.

### Migration path

1.  Migrate all event related communication to Real-time marketing (RTM) regardless of if you’re using Outbound or Real-time events. Journey orchestration, segmentation, and other assets also work with Outbound event registrations.
2.  Identify existing events that have a registration period open post-Outbound marketing removal and recreate them using Real-time marketing.
3.  Identify new events you're planning to run and check whether there's any critical functionality stopping you from using Real-time marketing. If there are no gaps identified, then all new events should be created in Real-time marketing only.
4.  Recreate the event registration experience per the guidance in the next section.

#### Transition of event registration experience

There were multiple options on how to build event registration experience in Outbound marketing. Each of these options has a slightly different migration path.

- **Event portal hosted on Power Portals** – Build a new event registration website using Power Pages template. For more information, see [Build an event registration website using Power Pages](event-portal-template.md).
- **Event portal NOT hosted on Power Portals** – The recommended migration path is to build new event registration experience using the new code snippet listing once available.
- **OBM Marketing form for event registration** – Replace these forms with RTM Event registration forms. For more information, see [Open the event management work area](open-events.md).
- **Custom solution using OBM Event Management API (not using Angular application)** – Use the new Events API. For more information, see [Using the events API in Real-time journeys](developer/using-rtm-events-api.md).

## Frequently asked questions

*How are Outbound and Real-time marketing events different?*

As with other parts of the system, Real-time marketing events have been built on the most advanced technology that allows us to scale our product and offer the most up-to-date secure first-driven experience. The biggest difference is the event registration experience. Another difference is that when introducing new capabilities to Real-time events, we're taking into consideration feedback received from years of experience with Outbound events and introducing several improvements. For more information, see [Real-time transition](transition-faqs.md#why-should-i-transition-to-real-time-journeys).

*What will happen once Outbound marketing is removed?*

Events are a shared capability between Real-time journeys and Outbound marketing—the same tables are used. The tables and data won't be removed. However, there are some critical differences in the event forms and pages between Outbound marketing and Real-time journeys. Therefore, events created from Outbound marketing stop working once Outbound marketing is removed.

*What will happen to the existing Outbound marketing event records?*

The event record will still be visible in the UI. However, it will be in read-only mode. This means that you'll be able to see the event, its settings, and registrations but you won't be able to edit the event any longer.

*What will happen with registrations in Outbound marketing events?*

The OBM registration records continue to be visible in the contact record as it is a Dataverse entity.

*Will the event data tables change?*

The data structure for Real-time marketing events is the same now, but as we're introducing changes and enhancements to the system. We may implement certain features differently.

*For any features that haven't been introduced yet, can we assume that they work the same way?*

We're trying to avoid making any model changes to the basic event entities. We do not recommend building custom solutions on system entities for features that aren't yet available in Real-time marketing as this may present a certain level of risk.

*Will my event portal continue to work post-Outbound removal?*

Once Outbound marketing is removed, it will no longer be possible to create Outbound marketing events or to register for Outbound marketing events. There were multiple options on how to build event registration experience and portals in Outbound marketing. Each of these will have a different migration path. <!--- For more information, see Real-time journeys' migration path for Outbound marketing event registration \<need to link it to the correct section once this one is published too https://microsofteur-my.sharepoint.com/:w:/g/personal/petrjantac_microsoft_com/EWk-2RlWMFdKgGpKyaVZnlQBv8-eCxD9iUK0yX628V4YHQ?e=X7OmIE -->

*What will happen to the portals that are still live post-Outbound removal?*

The services stop processing registrations and the site will no longer be available. There will be a user-friendly message informing them that the event registration page is no longer available. The recommendation is to unpublish all the existing portals before Outbound removal.

*Is there any tool that helps me transition my live events?*

No. Any events that are live and are accepting registrations have to have the registration closed before the Outbound removal. After the Outbound removal, we'll no longer process registrations submitted via Outbound forms.

*What should I do if the features I need for event planning aren't available?*

The most used features have a planned release date before the Outbound removal date. We understand there might be some features that are important for your business and might not be available yet. You can *phase your transition*. Any events that don't need those features can be created as Real-time events. You can also transition all your communication to Real-time as Outbound events can be used with Real-time journeys and emails. This reduces the number of assets you need to transition closer to the date.

## Blogs and workarounds

- Workaround for custom unmapped fields: Enhanced data collection and journey personalization with unmapped form fields. For more information, see [FastTrack blog](https://community.dynamics.com/blogs/post/?postid=3a361b7e-80b0-ee11-92bd-002248527d3d).
- Cascaded fields where options provided in a field depend on a value in an earlier field that isn't yet supported. For more information, see the blog [Implementing cascading dropdown fields in RTM forms](https://community.dynamics.com/blogs/post/?postid=ff86d88f-d892-ef11-ac21-6045bdd7e1ae).
- Sending timed reminders before event. For more information, see [Boost event engagement with journeys](real-time-marketing-event-registration-journey.md#step-2-send-email-reminders-seven-days-and-one-day-before-the-event).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
