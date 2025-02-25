---
title: New and upcoming features
description: Discover the latest features, improvements, and bug fixes in Dynamics 365 Customer Insights - Journeys. Stay updated with our monthly release notes.
ms.date: 02/24/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# What's new in Dynamics 365 Customer Insights - Journeys

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

[!INCLUDE [marketing-trial-cta](./includes/marketing-trial-cta.md)]

We're excited to announce our newest updates! This article summarizes early access features, preview features, general availability enhancements, monthly updates, and bug fixes. To see the long-term feature plans, take a look at the [Dynamics 365 and Power Platform release plans](/dynamics365/release-plans/).

Customer Insights - Journeys updates are [pushed to customers automatically](https://cloudblogs.microsoft.com/dynamics365/it/2020/04/27/automatic-update-policy-for-dynamics-365-marketing/). Solutions are available for early validations. To manually update your instances, follow the steps in [Keep Customer Insights - Journeys up to date](apply-updates.md).

To submit and vote on **feature requests** and **product suggestions**, go to the [Dynamics 365 Application Ideas portal](https://experience.dynamics.com/ideas/categories/?forum=dfa5b83d-9e4c-e811-a956-000d3a1bef07&forumName=Dynamics%20365%20Marketing).

### February 2025 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        | 1.1.52649.82  |
<!---
#### General availability

- **Accelerate journey creation using journey templates**
	- Increase your productivity by using journey templates to kickstart building your customer journeys. Save time using a template from common customer journey scenarios, make final updates with your chosen content and any slight adjustments to the flows, and publish.
	- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/marketers-accelerate-journey-creation-using-journey-templates)
	- [Docs](real-time-marketing-journey-templates.md)-->

#### Public preview
	
- **Wait on segment membership to trigger the next step in a journey** 
	- Gain even more control over your customers' experience by waiting for them to become a member of a segment before continuing to the next steps in a journey. This added capability lets you personalize each customer's experience by choosing the correct path and actions relevant to individual customers based on whether they're in a segment. This capability adds to existing if/then capabilities that let you wait for a customer to open an email, click a link, or wait for another trigger to be activated before moving on to the next step in the journey. For example, let's say you use your journey to send credit card activation emails and you want to wait for the customer to activate their card before sending a welcome email. If the customer doesn’t activate their credit card within a few days, you want to send another reminder email. If you have a segment that includes all customers who have activated credit cards, you can use that segment as the condition for the if/then branch to wait for each customer to activate their credit card and send them the right communications.
	- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/use-segments-decide-which-path-customer-should-take-journey) 
	- [Docs](add-action.md#preview-wait-for-segment-membership)

    :::image type="content" source="media/wait-segment-membership-release-planner.png" alt-text="Wait on segment membership to trigger the next step in a journey." lightbox="media/wait-segment-membership-release-planner.png":::

- **Allow individuals to reenter a one-time, dynamic segment journey** 
	- Audience members who move between stages of the customer lifecycle may need to repeat a lifecycle-specific state of the journey. For example, if a customer repeats a buying journey for a different product, they may reenter the dynamic segment conditions as they reenter the purchase funnel. As such, they should be allowed to reenter a journey for that dynamic segment when they come back into it. 
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/allow-individuals-re-enter-one-time-dynamic-segment-journey) 
	- [Docs](real-time-marketing-segment-based-journey.md)

- **Create event portals with event and registration details using Power Pages** 
	- Events are a pivotal element of your business strategy, aiding in customer acquisition and engagement. A centralized location is essential for your clients to discover and learn about events that you're organizing. The new event portal allows for the swift creation of a comprehensive hub where customers can access event details, session specifics, and speaker schedules and conveniently register using the event registration form. The portal can be seamlessly deployed through Power Pages, where it can be tailored to align with your brand identity using Power Pages Studio. 
	- [Release plan](/dynamics365/release-plan/2025wave1/customer-insights/dynamics365-customer-insights-journeys/enable-customers-find-sign-up-events-easily) 
	- [Docs](event-portal-template.md)
    > [!NOTE]
    > Due to rollout delays, the event registration template functionality for Power Pages aren't available until late February 2025.

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
