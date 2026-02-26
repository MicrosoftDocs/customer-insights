---
title: New and upcoming features
description: Discover the latest features, improvements, and bug fixes in Dynamics 365 Customer Insights - Journeys. Stay updated with our monthly release notes.
ms.date: 02/11/2026
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

### February 2026 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys | 1.1.62310.44 |

#### General availability

- **Maximize event ROI with paid registration, seamless payment integration** 
	- Hosting impactful events demands significant time, resources, and budget, but often requires the use of disparate and fragmented tools to sell event tickets. This challenge makes it difficult to track payments, reduce registration drop-off, and ultimately provide a delightful attendee experience. With the new paid event registration capability in real-time journeys, you can now offer a seamless and secure ticketing experience. We're introducing support for session registrations with passes, ensuring that attendees can only register for sessions that the pass gives them access to.  
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/maximize-event-roi-paid-registration-seamless-payment-integration) 
	- [Docs (event passes)](real-time-journeys-event-passes.md), [Docs (payment gateway)](./developer/payment-gateway-integration.md)

	:::image type="content" source="media/paid-events.png" alt-text="An event passes UI." lightbox="media/paid-events.png":::

- **Enhanced reCAPTCHA** 
	- Marketers rely on clean, trustworthy data to run effective journeys, but automated bot submissions can overwhelm forms, skew insights, and reduce conversion rates. Before this update, protecting forms required outdated HIP captcha or custom technical work, creating friction and leaving gaps in security. With the new built‑in reCAPTCHA, you protect your forms from bots while keeping the experience fast and accessible for real customers. You can add strong bot protection in seconds. No coding, no developer support, and no risk of losing data quality. This update boosts confidence in your form submissions, reduces spam, and ensures that every interaction you collect reflects real customer intent. The legacy HIP captcha is being deprecated to move to a more modern, secure, and user‑friendly reCAPTCHA experience. The HIP captcha will be deprecated in March 2026 and fully removed from all Customer Insights ‑ Journeys forms by June 30, 2026. 
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/strengthen-form-bot-protection-recaptcha) 
	- [Docs](real-time-marketing-form-security-privacy.md#protecting-forms-from-bots-with-recaptcha)

#### Monthly enhancements

- **Segmentation - Unused segments are not evaluated after 30 days** 
	- Segments that are published but not used in any live journey for 30 days are moved to the Expired state. These expired segments are no longer evaluated and are not counted towards your segment limits, helping to save resources and boost overall performance. You need to publish them again before they can be used in a journey.

- **Segmentation – Usability and functional enhancements** 
	- Several enhancements have been introduced to segmentation. Key improvements include: 
		* Updates to UI and insights charts to fix accessibility issues and make them mobile friendly 
		* Ability to refresh segments manually 
		* Added common commands Assign and Deactivate to the command bar and enable it for customization 
		* Support for circular relationship (Contact > related table(s) > Contact) 
		* Changed how related tables are evaluated to align with more common usage (RELATEOPTIONAL is the default now, RELATE remains available via advance menu. RELATEOPTIONAL allows rows to be returned even when the related record doesn’t exist, treating the relationship as optional)
		* Allow stopped segments to be edited and published again 
		* Fixed issues with timeline where items were showing up out of order and had other issues with end of the year 
		* Improved messages and information throughout (for example, show logical name to disambiguate similarly named attributes)
		* Increased query field size to support longer queries

- **Ability to set co-organizers for Teams Town Hall** 
	- You can now automatically assign coorganizers to Microsoft Teams Town Hall events directly within Customer Insights – Journeys. This enhancement streamlines event management, improves collaboration, and ensures smoother execution by giving additional users the ability to help manage and run Town Hall sessions. 
	- [Docs](teams-town-hall.md)

- **Teams Live Events, Teams Meeting and Teams Webinar are retiring** 
	- Microsoft is retiring Teams live events and the associated Microsoft Graph APIs used to create Teams live events effective June 30, 2026, though Microsoft will honor all live events that are already scheduled through Feb 28, 2027. We encourage customers to migrate to use Teams town halls, which offers an improved experience for large-scale digital and hybrid events. Furthermore, Teams Meeting and Teams Webinar are being replaced with Teams Meeting v2 and Teams Webinar v2 after Feb 28, 2027, as well.
	- [Docs](teams-meeting-types.md#teams-meeting-v2-teams-webinar-v2-teams-town-hall)

#### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- Learn how to access analytics data from Customer Insights – Journeys using a minimalistic footprint of Microsoft Fabric - [CI - J Insights with Minimal Fabric: The Lightweight Access Pattern](https://community.dynamics.com/blogs/post/?postid=6df49d04-bbf2-f011-8407-7c1e527eb82f).

### January 2026 update

There's no Dynamics 365 Customer Insights - Journeys release for January. We'll be back in February with new feature improvements, updates, and bug fixes.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
