---
title: New and upcoming features
description: Discover the latest features, improvements, and bug fixes in Dynamics 365 Customer Insights - Journeys. Stay updated with our monthly release notes.
ms.date: 12/22/2025
ms.update-cycle: 180-days
ms.topic: whats-new
author: alfergus
ms.author: alfergus
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# What's new in Dynamics 365 Customer Insights - Journeys

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](transition-overview.md).

[!INCLUDE [marketing-trial-cta](./includes/marketing-trial-cta.md)]

We're excited to announce our newest updates! This article summarizes early access features, preview features, general availability enhancements, monthly updates, and bug fixes. To see the long-term feature plans, take a look at the [Dynamics 365 and Power Platform release plans](/dynamics365/release-plans/).

Customer Insights - Journeys updates are [pushed to customers automatically](https://cloudblogs.microsoft.com/dynamics365/it/2020/04/27/automatic-update-policy-for-dynamics-365-marketing/). Solutions are available for early validations. To manually update your instances, follow the steps in [Keep Customer Insights - Journeys up to date](apply-updates.md).

To submit and vote on **feature requests** and **product suggestions**, go to the [Dynamics 365 Application Ideas portal](https://experience.dynamics.com/ideas/categories/?forum=dfa5b83d-9e4c-e811-a956-000d3a1bef07&forumName=Dynamics%20365%20Marketing).

### December 2025 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys | 1.1.61220.59 |

#### General availability

- **Export copies of sent emails for record keeping**
	- With the new email export API, you can now automatically export exact copies of every email you send to your customers, ensuring you have a reliable and verifiable record. This capability not only saves time but also enhances your ability to manage customer interactions and resolve disputes efficiently.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/export-copies-sent-emails-record-keeping)

- **Wait on segment membership to trigger next step in a journey**
	- Get more control over your customers' experience by waiting for them to become a member of a segment before continuing to the next steps in a journey. With this capability, you can personalize each customer's experience by choosing the correct path and actions relevant to individual customers based on whether they're in a segment. This capability adds to existing if/then capabilities that let you wait for a customer to open an email, click a link, or wait for another trigger to be activated before moving on to the next step in the journey.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/use-segments-decide-which-path-customer-should-take-journey)
	- [Docs](add-action.md#wait-for-segment-membership-preview)

#### Monthly enhancements

- **Quiet times can last up to 21 days**
	- You can now set up quiet times for a maximum of 21 consecutive days, up from the previous limit of 3.
	- [Docs](real-time-marketing-quiet-times.md#set-up-overnight-quiet-times)

- **Introducing Teams webinar v2**
	- As part of our ongoing modernization of Teams integration, we introduced Teams meeting v2 and Teams town hall in November. With this release, we’re introducing Teams webinar v2 and a new authentication flow.
	- [Docs](teams-web-version-2.md)

- **New attributes for event timing in UTC**
	- If your journey spans events across multiple time zones, it likely operates in UTC. To ensure that the “Wait until a time specified by a trigger” condition uses the correct event timing, select the newly introduced attributes `Event start date UTC` and `Event end date UTC`.
	- [Docs](real-time-marketing-event-registration-journey.md#ensure-accurate-event-timing-with-utc-attributes)

#### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Why localized dates and times matter in event registration](https://community.dynamics.com/blogs/post/?postid=8795951f-7baa-f011-bbd3-00224826f06d)
- [Use submitted form values to branch journeys and personalize emails](real-time-marketing-form-submitted-values.md)

### November 2025 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys | 1.1.60115.76 |

#### General availability

- **Host large-scale online events with Teams town hall**
	- Integrate Microsoft Teams town hall into Customer Insights - Journeys to schedule and manage events for up to 10,000 attendees as part of your broader campaign strategy. You can now automatically trigger personalized invitations based on customer data and behavior, increasing the likelihood of attendance and engagement. Track participation and engagement metrics within Customer Insights, making it easier to segment audiences and tailor follow-up actions after the event.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/host-large-scale-online-events-teams-town-hall)
	- [Docs](teams-town-hall.md)

#### Public preview

- **Create static segments with up to 200,000 members**
	- Marketers often receive customer lists from various systems and need to act quickly. These lists typically lack the attributes required for dynamic segments or aren't part of an existing Dataverse view. This feature enables marketers to build static segments with up to 200,000 members using data from any source. Marketers can upload CSV files, use the API to create segments as part of a workflow, or select contacts from a Dataverse view.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/create-static-segments-up-200000-members)
	- [Docs](real-time-marketing-build-segments.md#use-csv-files-to-define-static-segment-membership-lists-for-up-to-2000000-members)

- **Maximize event ROI with paid registration, seamless payment integration**
	- With the new paid event registration capability in real-time journeys, you can now offer a seamless and secure ticketing experience. This feature empowers you to offer flexible pricing tiers and discount codes and increase registration conversion with a frictionless checkout. By embedding ticketing and payments directly into your event flow, you not only improve attendee satisfaction but also unlock new revenue streams and reduce operational overhead.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/maximize-event-roi-paid-registration-seamless-payment-integration)
	- [Docs (event passes)](real-time-journeys-event-passes.md), [Docs (payment gateway)](./developer/payment-gateway-integration.md)

#### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Why localized dates and times matter in event registration](https://community.dynamics.com/blogs/post/?postid=8795951f-7baa-f011-bbd3-00224826f06d)
- [Use submitted form values to branch journeys and personalize emails](real-time-marketing-form-submitted-values.md)

### October 2025 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys | 1.1.59247.68 |

#### General availability

- **Transform your outreach with Copilot-powered voice conversations**
	- To meet the rising customer expectations, brands constantly look for new ways to connect so they can stand out among the sea of messages. By integrating Customer Insights - Journeys with Contact Center, you can go beyond traditional marketing tactics by leveraging Copilot Studio agents to deliver meaningful, hyper-personalized experiences that boost customer satisfaction and engagement.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/transform-outreach-copilot-powered-voice-conversations)
	- [Docs](conversational-journeys-overview.md)

- **Automate scalable journey creation with the journey API**
	- With the new journey API, you can now automate journey creation by using templates, existing segments, and messages. For example, a team managing global events can programmatically generate hundreds of localized journey variants, each tailored by language, time zone, and audience segment, without manually configuring each one.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/automate-scalable-journey-creation-journey-api)
	- [Docs](./developer/create-journey-template-api.md)

- **Streamline event planning with set registration periods**
	- Whether you're managing a product launch, a training session, or a customer summit, knowing your attendee count in advance brings structure and predictability to event planning. It helps you finalize logistics, allocate resources efficiently, avoid last-minute surprises, and reduce unnecessary costs from overbooking or under-preparing. By enforcing registration deadlines, teams can plan smarter and deliver more polished events with better decision-making and operational efficiency across event workflows. With minimized uncertainty and improved coordination, this functionality enhances the overall experience for both organizers and participants.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/streamline-event-planning-set-registration-periods)
	- [Docs](set-up-event.md#the-form-tab)

- **Create event portals with event and registration details using Power Pages**
	- The new event portal enables you to quickly create a comprehensive hub where customers can access event details, session specifics, and speaker schedules. Customers can conveniently register using the event registration form. You can deploy the portal through Power Pages and customize it to match your brand identity with Power Pages Studio.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/enable-customers-find-sign-up-events-easily)
	- [Docs](event-portal-template.md)

- **Create an event portal on your own website using the event API**
	- Events play a pivotal role in your business strategy by helping you acquire and engage customers. Your clients need a centralized location where they can discover and learn about the events you organize. The event API is a programmatic method to access data of events, sessions, session tracks, passes, speakers, and sponsorships, which enables you to quickly create a comprehensive hub where customers can access important event details and register.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/create-event-portal-own-website)
	- [Docs](./developer/using-rtm-events-api.md)

- **Create an event portal on your own website using the web application**
	-The event portal web application provides a lightweight, multilingual, and mobile-responsive interface for showcasing live events from the Dynamics 365 events API, enabling users to search by name or description, view detailed event information, and register directly using embedded Customer Insights - Journeys forms. It's built with plain JavaScript, HTML, and CSS, and supports fast deployment and easy customization.
     - [Docs](./developer/event-portal-web-application.md)

#### Public preview

- **Maximize event ROI with paid registration, seamless payment integration**
	- With the new paid event registration capability in real-time journeys, you can now offer a seamless and secure ticketing experience. This feature empowers you to offer flexible pricing tiers and discount codes and increase registration conversion with a frictionless checkout. By embedding ticketing and payments directly into your event flow, you not only improve attendee satisfaction but also unlock new revenue streams and reduce operational overhead.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/maximize-event-roi-paid-registration-seamless-payment-integration)
	- [Docs](real-time-journeys-event-passes.md)

#### Monthly enhancements

- **Prevent unintended opt‑outs in forms**
	- You can now stop your forms from unsubscribing contacts when they leave topics or purposes unchecked. Use the new “Ignore opt‑outs” toggle in the form settings or the default form settings to make sure unchecked boxes don’t create opt‑out records. By default, all new marketing and event registration forms don’t generate opt‑outs, helping you keep your audience engaged. This update gives you full control over consent handling and reduces accidental loss of subscriptions.
	- [Docs](real-time-marketing-manage-forms.md#manage-consent-in-forms)

- **Manual registrations can now contain custom unmapped fields**
    - When adding a registration manually, you can now include information using custom unmapped fields that you would typically collect through a registration form. This allows you to collect and store important event attendee information, even for last-minute sign-ups or someone who didn’t submit a registration form.
    - [Docs](create-unmapped-fields-registration-forms.md)

### September 2025 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys | 1.1.58607.69 |

#### Real-time journeys transition

- **Outbound marketing will be hidden and then removed**
	- As explained in [What will happen after June 30, 2025? Will outbound marketing stop working?](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working-updated-november-21-2025), outbound marketing removal is following a phased approach. We're currently in phase two where we are gradually enabling non-dismissible message dialogs when users try to create outbound marketing assets such as journeys, emails, segments, and so on. We aim to have these blocking dialogs enabled in all outbound marketing environments by the end of September 2025. We'll soon start moving some environments into phase three where we hide outbound marketing and then remove it. Outbound marketing environments in tenants with an approved extension won't be affected. Environments with approved extensions may see some warning messages or banners, but we won't take any action while the extension is in place. For more information, see [Transition overview](transition-overview.md) and [Real-time journeys transition FAQs](transition-faqs.md).

#### General availability

- **Simplify forms by filtering choices based on previous answers**
	- Guiding your customers through a smooth form submission experience is crucial to avoid frustration and abandonment before completion. New form field filtering dynamically adjusts options for one field based on the selection you make in another field, so users see only relevant choices. This feature makes forms simpler to understand and quicker to complete.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/simplify-forms-filtering-choices-based-previous-answers)
	- [Docs](real-time-marketing-manage-forms.md#filter-a-lookup-field-values-based-on-an-answer-in-a-previous-lookup-field-cascading-lookup-fields)

- **Collect extra customer info without updating your data model**
	- You can easily gather extra information about your customers by creating any kind of question directly in the marketing form editor without needing to create new custom attributes for your lead or contact entity. For example, you can create fields to ask, “How did you hear about our products?” or create contest questions to increase your customer satisfaction and retention.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/collect-extra-customer-information-without-creating-custom-attributes) 
	- [Docs](real-time-marketing-forms-custom-fields.md)

- **Generate leads that link to an existing contact**
	- Your business has unique ways of organizing customer data and classifying potential leads. Now, with real-time journey forms, you can manage your contacts and leads more effectively according to your company's established processes. For example, you can recognize existing customers who fill out a lead form, so they're not mistaken for new leads.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/generate-leads-that-link-existing-contact) 
	- [Docs](real-time-marketing-manage-forms.md#parent-contact-for-lead)

- **Collect extra event attendee information without updating your data model**
	- You can easily gather extra information about your event attendees by creating any question directly in the form editor without creating new custom attributes for your contact entity. For example, you can create fields to ask, "What is your meal preference?" or "How did you learn about this event?" You can also create contest questions to increase customer engagement and gather valuable insights that help you personalize the attendee experience.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/collect-extra-event-attendee-information-without-updating-data-model)
	- [Docs](create-unmapped-fields-registration-forms.md)

- **View Customer Insights - Data profile interactions on the timeline**
	- The timeline lets you see detailed information for a contact or lead by tracking marketing, sales, and service interactions over time in a single stream. If you orchestrate journeys that target Customer Insights - Data customer profiles, you can now see marketing interactions like emails sent, forms submitted, and website visits on the connected contact timeline. With this update, teams across the organization get a complete overview of marketing interactions relevant to their work. Sales representatives can review marketing touchpoints—including eBook downloads and email clicks—to refine their outreach strategies, and service agents can reference recent interactions to manage escalations and support inquiries.
	- [Docs](timeline.md)

#### Public preview

- **Automate scalable journey creation with the journey API**
	- With the new journey API, you can now automate journey creation by using templates, existing segments, and messages. For example, a team managing global events can programmatically generate hundreds of localized journey variants, each tailored by language, time zone, and audience segment, without manually configuring each one.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/automate-scalable-journey-creation-journey-api) 
	- [Docs](./developer/create-journey-template-api.md)

#### Monthly enhancements

- **Using the events API in real-time journeys**
	- Events play a pivotal role in your business strategy by helping you acquire and engage customers. Your clients need a centralized location where they can discover and learn about the events you organize. The events API is a programmatic method to access data of events, sessions, session tracks, passes, speakers, and sponsorships, which enables you to quickly create a comprehensive hub where customers can access important event details and register.

        With this enhancement, we have extended the existing API with the following capabilities: 
    1. Check in endpoint
    1. Event QR code endpoint
    1. Registrations count and session registrations count endpoint 
    1. Ability to retrieve list of sessions
    1. Ability to retrieve list of speakers
    1. Ability to retrieve list of sponsors and their logos
    1. Ability to submit registration via API
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/create-event-portal-own-website)
	- [Docs](./developer/using-rtm-events-api.md)

#### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Filter cities by selected country/region in Customer Insights - Journeys forms](real-time-marketing-filter-cities-by-country-region.md)

### August 2025 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys       |  1.1.57638.58 |

> [!IMPORTANT]
> On **August 4, 2025**, the Dynamics 365 Customer Insights - Journeys services public IP addresses were updated in all regions.
>
> **How do the updated IP addresses affect Customer Insights - Journeys users?**
>
> - **Real-time journeys**: So long as you update your allowlists (as described below under **Required action for administrators**), the IP address changes don't affect real-time journeys services.
> - **Outbound marketing**: Outbound marketing users who meet all of the following criteria are affected: (1) you are an existing outbound marketing user, (2) you use custom analytics reporting as described in [Prepare for analytic reporting with Power BI](custom-analytics.md), and (3) you restrict access to your "bring your own" storage accounts by firewall rules using IP addresses. If your custom analytics meet these criteria and are impacted, outbound marketing analytics exports are stopped due to unauthorized access to your blob storage from outbound marketing services. To verify whether the IP changes affect your outbound marketing analytics configuration, review the entity **Analytics configuration** and verify the **Service status**.
>
> **Required action for administrators**
>
> An administrator with firewall or network rights should update your allowlists to account for the new IP addresses. A list of all public IP addresses, categorized by geo, is available here: [Dynamics 365 Customer Insights - Journeys public IP addresses](marketing-public-ips.md).
>
> If your organization uses VNets (subnets) for allowlisting, it's not affected by the IP address changes.

#### Monthly enhancements

- **Protect existing lead and contact data with the "Ignore empty values" toggle**
	- To prevent accidental data loss, forms now support an "Ignore empty values" option in the form editor. When enabled, this setting ensures that empty fields submitted by end users don’t overwrite existing lead or contact data. It applies to marketing and registration forms, and is enabled by default for new forms The toggle is disabled for existing forms to the preserve current behavior.
	- [Docs](real-time-marketing-manage-forms.md#ignore-empty-values)

### July 2025 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys       | 1.1.57027.56  |

#### General availability

- **Orchestrate journeys using any marketing interaction**
	- Transform the way you communicate with your customers. By using marketing interaction triggers to orchestrate or branch customer journeys, you can now engage your customers based on the interactions they have with your marketing messages. Instantly adapt your strategies based on your customers' real-time interactions, ensuring that every message you send hits the right note. By engaging customers based on their interactions, you can significantly ramp up your chances of conversion with greater personalization. For example, you can branch and orchestrate journeys based on customer interactions with emails such as "email link clicked" or "email blocked."
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/orchestrate-journeys-using-marketing-interaction) 
	- [Docs](real-time-marketing-trigger-based-journey.md)

- **Respect quiet times, engage based on location and time zones**
	- As regulations around customer privacy become more stringent, it's crucial to contact customers at times that are most convenient to them and ensure compliance with local legal requirements. Now in Customer Insights - Journeys, in addition to setting quiet times based on your journey's time zone, you can align quiet times with your customers' time zones and regions, ensuring that they only receive messages and calls during suitable hours. Aligning interactions with local time allows you to adhere to local regulations and respect cultural norms and preferences, fostering customer trust and enhancing the effectiveness of your outreach strategies.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/respect-quiet-times-engage-based-location-time-zones) 
	- [Docs](real-time-marketing-quiet-times.md#use-time-zone-for-quiet-times)

	:::image type="content" source="media/qt-settings-updated.png" alt-text="Set up quiet times for a journey based location and time zone." lightbox="media/qt-settings-updated.png":::

- **Pause and resume journeys to handle unplanned events**
	- Safeguarding your brand's reputation and customer trust is critical. In the face of unplanned or unforeseen events, such as natural disasters, you may need to pause certain campaigns that might be deemed inappropriate or insensitive. Additionally, you may run into business or operational reasons for stopping a campaign, such as identifying the need to update some content or experiencing an unexpected call center outage. In such scenarios, it's prudent to halt customer outreach until the problem is addressed. Instead of stopping a campaign and adjusting the audience to exclude previously reached customers, you can now pause and resume journeys, allowing you to manage unplanned situations easily and stress-free.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/pause-resume-journeys-handle-unplanned-events) 
	- [Docs](pause-resume-journey.md)

	:::image type="content" source="media/journey-pause.png" alt-text="Pause and resume journeys to handle unplanned events." lightbox="media/journey-pause.png":::

- **Tailor follow-up strategies by reacting to multiple customer actions at once**
	- By allowing marketers to react to multiple customer actions simultaneously, this feature enables faster, more intelligent decision-making within journeys, reducing the time and effort required to manage complex branching logic. Marketers can now consolidate multiple interaction outcomes into a single decision point, saving operational overhead while increasing precision in how each customer is engaged. This leads to better-targeted messaging, higher engagement rates, and stronger conversion outcomes. Additionally, simplifying journey configuration reduces setup time and ongoing maintenance, allowing teams to launch faster and scale efficiently across channels.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/tailor-follow-up-strategies-reacting-multiple-customer-actions-at-once) 
	- [Docs](multi-interaction-branching.md)

	:::image type="content" source="media/tailor-follow-up-strategies.png" alt-text="Tailor follow-up strategies by reacting to multiple customer actions at once." lightbox="media/tailor-follow-up-strategies.png":::

- **Maximize event capacity with waitlist registrations**
	- Ensuring marketing events are filled to capacity is crucial for success and return on investment. To encourage a high turnout for marketing events, you can now enable waitlist registrations, which ensures spots are filled when registered attendees cancel. By setting the capacity for events and sessions, prospective attendees are placed on a waitlist when events and sessions are full. Should a slot open, the system either automatically registers the individual next on the waitlist or lets you manually select the replacement from the pool of waitlist registrations. You can save time and easily manage waitlist-related communication with a new set of out-of-the-box triggers, allowing you to send personalized messaging to waitlisted attendees.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/maximize-event-capacity-waitlist-registrations) 
	- [Docs](set-up-and-manage-waitlist.md#manual-management-of-waitlist-registrations)

	:::image type="content" source="media/w-registering.png" alt-text="Maximize event capacity with waitlist registrations." lightbox="media/w-registering.png":::

#### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Time Zone Identification for Quiet Time feature in Dynamics 365 Customer Insights](https://community.dynamics.com/blogs/post/?postid=c1ad9596-0338-f011-8c4e-0022481da8cf)

### June 2025 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys       | 1.1.56329.38  |

#### Real-time journeys transition

- **Message dialogs when creating outbound assets**
	- Users will notice new message dialogs in the product whenever they attempt to create a new outbound marketing email, journey, segment, form, page, and more. These message dialogs advise users that outbound marketing will be removed soon. For now, users can dismiss the dialog and continue working in outbound marketing, but this will change in the future. Users will also see warning banners when current journeys and events are scheduled to run past June 30, 2025. For more information, see [Real-time journeys transition FAQs](transition-faqs.md).

#### General availability

- **Get insights on email engagement with heatmap analytics** 
	- Understanding the effectiveness of email campaigns can be complex, particularly when information and links are abundant. Gaining clarity on which areas or links captivate your audience and drive them to act is crucial for refining the user experience and boosting email performance. Real-time journeys email insights now offer a clear view of your audience's preferences by illustrating their interactions within your emails. This immediate visual feedback highlights the content that resonates the most, empowering you to adjust your messaging for heightened impact and better conversion rates. Heatmap now supports email variations. By leveraging these insights, you can understand which email variation captivates your audience and use it to personalize and optimize your upcoming campaigns or focus your efforts on the variations that yield the best results, ultimately driving better results for your business.  
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/get-insights-email-engagement-heatmap-analytics) 
	- [Docs](email-insights.md#click-map)

	:::image type="content" source="media/get-insights-heat-map.png" alt-text="Get insights on email engagement with heatmap analytics." lightbox="media/get-insights-heat-map.png":::

#### Public preview

- **Transform your outreach with custom-built AI agent-powered voice conversations** 
	- Brands are constantly looking for ways to anticipate customer needs and connect with them on the channels that is the most appropriate for the message engagement. By integrating Customer Insights - Journeys with Contact Center, you can leverage custom-built AI agents to deliver meaningful, hyper-personalized conversational voice calls that boost customer satisfaction and engagement.  For example, you can alert a customer about a flight delay via a voice call where the custom-built AI agent engages them in a natural language conversation to inform them about the issue and offer solutions such as reschedule or refund. The results of the conversation then drive the next action in the journey, whether that’s rescheduling the flight, issuing the refund, or sending an email because there was no answer.
	- [Docs](conversational-journeys-overview.md) 
	- [Blog](https://aka.ms/AI-Powered-Convos)

	:::image type="content" source="media/journey-ai-voice-conversation.png" alt-text="Transform your outreach with custom-built AI Agent powered voice conversations." lightbox="media/journey-ai-voice-conversation.png":::

- **Pause and resume journeys to handle unplanned events** 
	- Safeguarding your brand's reputation and customer trust is critical. In the face of unplanned or unforeseen events, such as natural disasters, you may need to pause certain campaigns that might be deemed inappropriate or insensitive. Additionally, you may run into business or operational reasons for stopping a campaign, such as identifying the need to update some content or experiencing an unexpected call center outage. In such scenarios, it's prudent to halt customer outreach until the problem is addressed. Instead of stopping a campaign and adjusting the audience to exclude previously reached customers, you can now pause and resume journeys, allowing you to manage unplanned situations easily and stress-free. 
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/pause-resume-journeys-handle-unplanned-events) 
	- [Docs](pause-resume-journey.md)

#### Monthly enhancements

- **Out-of-box cancel registration flow**
	- Event organizers can now include a cancel registration link in confirmation emails, enabling attendees to cancel their registration easily. This automatically updates their status to "Canceled" in the system, giving organizers real-time visibility while simplifying attendee management and improving support for waitlists.
	- [Docs](cancel-registration.md)

 #### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Time Zone Identification for Quiet Time feature in Dynamics 365 Customer Insights](https://community.dynamics.com/blogs/post/?postid=c1ad9596-0338-f011-8c4e-0022481da8cf)

### May 2025 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys       | 1.1.55604.58 |

#### General availability

- **Understand customer inflows and exits at every journey step** 
	- It’s critical to understand exactly what happened to each customer who entered and exited your real-time journeys. With improved journey analytics, you’ll gain confidence in the processing of every step in your journey through improved metrics and an increased ability to export data. For example, if your journey uses exit or exclusion segments, you can see and understand why fewer customers started your journey than were in the entry segment. You can also see the list of customers who entered and exited each step in the journey and export lists of up to 50,000 people for further analysis. 
	- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/confidently-understand-customer-inflows-exits-at-every-step-journey) 
	- [Docs](real-time-marketing-analytics.md)

#### Public preview

- **Respect quiet times, engage based on location and time zones** 
	- As regulations around customer privacy become more stringent, it's crucial to contact customers at times that are most convenient to them and ensure compliance with local legal requirements. Now in Customer Insights - Journeys, in addition to setting quiet times based on your journey's time zone, you can align quiet times with your customers' time zones and regions, ensuring that they only receive messages and calls during suitable hours. Aligning interactions with local time allows you to adhere to local regulations and respect cultural norms and preferences, fostering customer trust and enhancing the effectiveness of your outreach strategies.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/respect-quiet-times-engage-based-location-time-zones) 
	- [Docs](real-time-marketing-quiet-times.md#use-time-zone-for-quiet-times)
	- [Blog](https://community.dynamics.com/blogs/post/?postid=c1ad9596-0338-f011-8c4e-0022481da8cf)
   
	:::image type="content" source="media/quiet-time-settings.png" alt-text="Set up quiet times in Customer Insights - Journeys." lightbox="media/quiet-time-settings.png":::

- **Collect extra event attendee information without updating your data model** 
	- Easily gather additional information about your event attendees by creating any question directly in the form editor without creating new custom attributes for your contact entity. For example, you can create fields to ask, “What is your meal preference?”, "How did you learn about this event?", or you can create contest questions to increase your customer engagement and to gather valuable insights that help you personalize the attendee experience. 
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/collect-extra-event-attendee-information-without-updating-data-model) 
	- [Docs](create-unmapped-fields-registration-forms.md)

- **Tailor follow-up strategies by reacting to multiple customer actions at once** 
	- Marketers can now create more personalized customer experiences by branching on multiple interactions within a single journey step. Using the "Wait for trigger" tile after a marketing message, journey designers can select "Previous message gets an interaction" and configure multiple triggers, like Email Opened, Email Blocked, or Email Bounced, on the same branch. This streamlines journey design by consolidating logic and enabling smarter engagement paths based on how recipients interact.
	- [Docs](multi-interaction-branching.md)

	:::image type="content" source="media/multi-interaction-branching.png" alt-text="Configure journey branches based on multiple customer responses to marketing messages." lightbox="media/multi-interaction-branching.png":::

#### Monthly enhancements

- **Select the right form template for any audience while creating a new form** 
	- As part of a monthly enhancement, the template gallery now displays all form templates grouped for specific audiences. When creating a new form, you can see all available custom and out-of-the-box form templates. Once you choose a desired template, the newly created form adheres to the audience specified by that template.
	- [Docs](real-time-marketing-form-overview.md#custom-form-templates)

#### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Leveraging CI-J interaction data without Fabric](https://community.dynamics.com/blogs/post/?postid=75a63967-f115-f011-998a-7c1e525b5e9d)

### April 2025 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys       | 1.1.54652.140 |

#### General availability

- **Streamline form filling and event registration with form prefill**
	- The repetitive task of filling out forms can be a significant deterrent to event registration. Nobody likes to repeat information that they've already provided. Imagine loyal customers who attend multiple conferences each year having to input their contact information and preferences every time. Form prefill in Dynamics 365 Customer Insights eliminates the need to repeatedly request basic details from your customers, reducing redundancy and saving time. This not only expedites the registration process but also allows for more strategic collection of customer data over time.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/form-prefill-simplifies-form-filling-event-sign-up) 
	- [Docs](real-time-marketing-form-prefill.md)

	:::image type="content" source="media/form-prefill.png" alt-text="Streamline form filling and event registration with form prefill." lightbox="media/form-prefill.png":::

- **Personalize messages and make journey decisions based on web interactions** 
	- With Customer Insights - Journeys, you can now track and leverage your customers’ online behavior to deliver personalized experiences across your digital channels. For example, you can boost conversions and customer loyalty by sending tailored offers after customers visit your website and show interest in a product or service. By tracking additional data about customers' online journeys, you can get valuable insights into your customers' preferences and needs and easily measure your campaign’s effectiveness.
	- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/engage-customers-personalized-messages-based-website-interactions) 
	- [Docs](interaction-journey-decision.md)

#### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Updated transition FAQs](transition-faqs.md)
- [Real-time marketing event management - Multiple locations and languages events](https://community.dynamics.com/blogs/post/?postid=7b86ce12-2ae3-ef11-a730-6045bdf005c5)

### March 2025 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        | 1.1.53893.111  |

#### General availability

- **Refine email content in running journeys**
	- To maximize customer engagement, it's crucial for customer experience teams to regularly refine email content, ensuring that communication remains current, relevant, and impactful. You can now easily edit content, layout, links, buttons, or dynamic content in your email messages while a journey is running, without creating a new version or interrupting the customer experience. Changing email messages in live journeys gives you more freedom and power over your email marketing campaigns and helps you respond to changing business or customer needs.
	- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/improve-engagement-editing-emails-live-journeys)
	- [Docs](edit-email-in-live-journey.md)

	 :::image type="content" source="media/editable-emails.png" alt-text="Editable email links with alias." lightbox="media/editable-emails.png":::

- **Accelerate journey creation using journey templates**
	- Increase your productivity by using journey templates to kickstart building your customer journeys. Save time using a template from common customer journey scenarios, make final updates with your chosen content and any slight adjustments to the flows, and publish. 
	- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/marketers-accelerate-journey-creation-using-journey-templates)
	- [Docs](real-time-marketing-journey-templates.md)

	 :::image type="content" source="media/journey-templates.png" alt-text="Journey templates gallery." lightbox="media/journey-templates.png":::

- **Allow individuals to reenter a one-time, dynamic segment journey** 
	- Audience members who move between stages of the customer lifecycle may need to repeat a lifecycle-specific state of the journey. For example, if a customer repeats a buying journey for a different product, they may reenter the dynamic segment conditions as they reenter the purchase funnel. As such, they should be allowed to reenter a journey for that dynamic segment when they come back into it. 
	- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/allow-individuals-re-enter-one-time-dynamic-segment-journey) 
	- [Docs](real-time-marketing-segment-based-journey.md)

#### Public preview

- **Maximize event capacity with waitlist registrations**
	- Ensuring marketing events are filled to capacity is crucial for success and return on investment. To encourage a high turnout for marketing events, you can now enable waitlist registrations, which ensures spots are filled when registered attendees cancel. By setting the capacity for events and sessions, prospective attendees are placed on a waitlist when events and sessions are full. Should a slot open, the system automatically registers the individual next on the waitlist. That individual then automatically receives registration confirmation and personalized event information, ensuring your event is filled to capacity.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/maximize-event-capacity-waitlist-registrations)
	- [Docs](set-up-and-manage-waitlist.md)

	 :::image type="content" source="media/waitlist-feature-screen.png" alt-text="Maximize event capacity with waitlist registrations in Customer Insights - Journeys." lightbox="media/waitlist-feature-screen.png":::

- **Collect extra customer info without updating your data model**
	- Easily gather additional information about your customers by creating any kind of question directly in the marketing form editor without the need to create new custom attributes for your lead or contact entity. For example, you can create fields to ask, “How did you hear about our products?” or create contest questions to increase your customer satisfaction and retention.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/collect-extra-customer-information-without-creating-custom-attributes)
	- [Docs](real-time-marketing-forms-custom-fields.md)

	 :::image type="content" source="media/custom-form-fields-resized.png" alt-text="Collect extra customer info without updating your data model." lightbox="media/custom-form-fields-resized.png":::

	> [!NOTE]
	> Custom unmapped fields for event registration forms will be introduced in a future release.

#### Monthly enhancements

- **Create enhanced matching rules for forms and journeys**
	- Maintaining a consistent customer database without duplicate records is crucial for business operations. The matching process was extended with the context of the tracking link and parent contact for lead relation. If there are multiple contacts or leads identified by the matching rule, the tracking link context or the parent contact relation are used to prioritize the right record for matching.
	- [Docs](real-time-marketing-matching-rules.md)  

#### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Updated transition FAQs](transition-faqs.md)
- [Real-time marketing event management - Multiple locations and languages events](https://community.dynamics.com/blogs/post/?postid=7b86ce12-2ae3-ef11-a730-6045bdf005c5)

### February 2025 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        | 1.1.52649.82  |

#### Public preview
	
- **Wait on segment membership to trigger the next step in a journey** 
	- Gain even more control over your customers' experience by waiting for them to become a member of a segment before continuing to the next steps in a journey. This added capability lets you personalize each customer's experience by choosing the correct path and actions relevant to individual customers based on whether they're in a segment. This capability adds to existing if/then capabilities that let you wait for a customer to open an email, click a link, or wait for another trigger to be activated before moving on to the next step in the journey. For example, let's say you use your journey to send credit card activation emails and you want to wait for the customer to activate their card before sending a welcome email. If the customer doesn’t activate their credit card within a few days, you want to send another reminder email. If you have a segment that includes all customers who have activated credit cards, you can use that segment as the condition for the if/then branch to wait for each customer to activate their credit card and send them the right communications.
	- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/use-segments-decide-which-path-customer-should-take-journey) 
	- [Docs](add-action.md#wait-for-segment-membership-preview)

    :::image type="content" source="media/wait-segment-membership-release-planner.png" alt-text="Wait on segment membership to trigger the next step in a journey." lightbox="media/wait-segment-membership-release-planner.png":::

- **Allow individuals to reenter a one-time, dynamic segment journey** 
	- Audience members who move between stages of the customer lifecycle may need to repeat a lifecycle-specific state of the journey. For example, if a customer repeats a buying journey for a different product, they may reenter the dynamic segment conditions as they reenter the purchase funnel. As such, they should be allowed to reenter a journey for that dynamic segment when they come back into it. 
	- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/allow-individuals-re-enter-one-time-dynamic-segment-journey) 
	- [Docs](real-time-marketing-segment-based-journey.md)

- **Create event portals with event and registration details using Power Pages** 
	- Events are a pivotal element of your business strategy, aiding in customer acquisition and engagement. A centralized location is essential for your clients to discover and learn about events that you're organizing. The new event portal allows for the swift creation of a comprehensive hub where customers can access event details, session specifics, and speaker schedules and conveniently register using the event registration form. The portal can be seamlessly deployed through Power Pages, where it can be tailored to align with your brand identity using Power Pages Studio. 
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/enable-customers-find-sign-up-events-easily) 
	- [Docs](event-portal-template.md)

- **Create an event portal on your own website** 
	- Events are a pivotal element of your business strategy, aiding in customer acquisition and engagement. A centralized location is essential for your clients to discover and learn about events you are organizing. The new events API offers a programmatic method to access data of events, sessions, session tracks, passes, speakers, and sponsorships. Additionally, it allows you to register for events and sessions.
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/create-event-portal-own-website) 
	- [Docs](../journeys/developer/using-rtm-events-api.md)

#### Monthly enhancements

- **Create custom form templates** 
	- Creating marketing and event registration forms is now easier, as you can leverage a custom template. The custom template can reflect styling adjustments to align with your style guide. You can also set the audience configuration and adjust the consent to meet your requirements.
	- [Docs](real-time-marketing-form-overview.md#form-templates)  

#### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Updated transition guidance for event management](transition-walkthrough-events.md)
- [Real-time marketing event management - Multiple locations and languages events](https://community.dynamics.com/blogs/post/?postid=7b86ce12-2ae3-ef11-a730-6045bdf005c5)

### January 2025 update

There's no Dynamics 365 Customer Insights - Journeys release for January. We'll be back in February with new feature improvements, updates, and bug fixes.

#### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Optimize your email marketing campaigns with advanced analytics features - Microsoft Dynamics 365 Blog](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2024/12/02/optimize-your-email-marketing-with-advanced-analytics-features/)
- [Import contacts from excel to create segments in real-time marketing – FastTrack blog](https://community.dynamics.com/blogs/post/?postid=cc6aa275-47a3-ef11-8a69-7c1e52481105))
- [LinkedIn Lead Sync Integration with Dynamics 365 Customer Insights – Journeys – FastTrack blog](https://community.dynamics.com/blogs/post/?postid=fb6ed89f-67a1-ef11-8a69-7c1e520b1f9b)
- [Transition Customer Voice responses](transition-walkthrough-customer-voice.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
