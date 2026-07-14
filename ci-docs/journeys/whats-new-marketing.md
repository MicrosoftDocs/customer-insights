---
title: New and upcoming features
description: Dynamics 365 Customer Insights - Journeys release notes list monthly preview features, general availability updates, enhancements, and bug fixes.
ms.date: 07/09/2026
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

[!INCLUDE [marketing-trial-cta](./includes/marketing-trial-cta.md)]

This article lists monthly release notes for Dynamics 365 Customer Insights - Journeys, including early access features, preview features, general availability updates, enhancements, and bug fixes. For longer-term feature plans, see the [Dynamics 365 and Power Platform release plans](/dynamics365/release-plans/).

Customer Insights - Journeys updates are [pushed to customers automatically](https://cloudblogs.microsoft.com/dynamics365/it/2020/04/27/automatic-update-policy-for-dynamics-365-marketing/). Solutions are available for early validation. To update your instances manually, follow the steps in [Keep Customer Insights - Journeys up to date](apply-updates.md).

To submit and vote on **feature requests** and **product suggestions**, go to the [Dynamics 365 Application Ideas portal](https://experience.dynamics.com/ideas/categories/?forum=dfa5b83d-9e4c-e811-a956-000d3a1bef07&forumName=Dynamics%20365%20Marketing).

### July 2026 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys | 1.2.1258.89 |

#### Public preview

- **Improve engagement and message timing with Outreach Optimization Agent**
	- Outreach Optimization Agent helps you automatically optimize when and how often you reach each customer by intelligently orchestrating message timing and follow‑ups based on engagement history and real‑time signals.
	- [Release plan](/dynamics365/release-plan/2026wave1/customer-insights/dynamics365-customer-insights-journeys/improve-engagement-message-timing-outreach-optimization-agent)
	- [Docs](outreach-optimization-agent.md)

#### Monthly enhancements

- **Create record enhancements**
	- When creating records from a journey, you can now leverage the full power of a rich text editor and personalization for text fields.
	- [Docs](create-records-activities.md)

### June 2026 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys | 1.2.437.94 |

#### General availability

- **Set message expirations to keep communication relevant**
	- Customers may experience frustration when they receive outdated communications, such as expired coupons and irrelevant reminders. This creates confusion and diminishes their trust in your brand. You can now set expiration dates on your messages, ensuring that only current and relevant information reaches your audience. This keeps your customers engaged and satisfied with relevant communications in moments that matter.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/set-message-expirations-keep-communication-relevant)
	- [Docs](message-expiration.md)

#### Public preview

- **Create journeys in minutes with Journey Creation Agent**
	- With the new Journey Creation Agent in Dynamics 365 Customer Insights - Journeys, anyone can create journeys in minutes, even if they've never done it before. Instead of spending time getting the mechanics of the journey right, you can now ensure you deliver the most personalized experience for your customers. Move from idea to execution in minutes, freeing up time and reducing dependency on technical experts.
	- [Release plan](/dynamics365/release-plan/2026wave1/customer-insights/dynamics365-customer-insights-journeys/create-journeys-minutes-journey-creation-agent)
	- [Docs](journey-creation-agent.md)

> [!NOTE]
> Journey Creation Agent was made available to many regions in the May 2026 release. On June 5, 2026, Journey Creation Agent will also be available in the North America (NAM) and Oceania (OCE) regions.

#### Monthly enhancements

- **Create effective audiences with conversational journey interactions**
	- Create targeted segments based on behavioral signals from conversational journey interactions, including voice and text message conversations.

- **Flexible column views for segment members**
    - You can now select a custom contact or lead view from the new view picker to control which columns appear in the segment members table. The **Export Members** button uses those same columns when exporting.

- **Open links in a new tab in forms**
	- Configure buttons and links in Customer Insights - Journeys forms to open their target content in a new browser tab, keeping the form page intact for the visitor.

### May 2026 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys | 1.1.65002.146 |

#### General availability

- **Create effective audiences with marketing website interactions**
	- Create targeted segments based on behavioral signals from marketing website interactions, including page visits and clicks. You can further refine your segment using information such as the name, type, or URL of the page visited.
	- [Docs](real-time-marketing-redesigned-segment-builder.md#create-a-segment-using-interactions)

#### Public preview

> [!NOTE]
> The following features are available as part of the 1.1.65002.153 update. To use AI Hub and the Journey Creation Agent, navigate to **Settings** > **Versions** and upgrade to 1.1.65002.153.

- **Create journeys in minutes with Journey Creation Agent**
	- With the new Journey Creation Agent in Dynamics 365 Customer Insights - Journeys, anyone can create journeys in minutes, even if they've never done it before. Instead of spending time getting the mechanics of the journey right, you can now ensure you deliver the most personalized experience for your customers. Move from idea to execution in minutes, freeing up time and reducing dependency on technical experts.
	- [Docs](journey-creation-agent.md)
 	- [Release plan](/dynamics365/release-plan/2026wave1/customer-insights/dynamics365-customer-insights-journeys/create-journeys-minutes-journey-creation-agent)
 
- **Govern Customer Insights - Journeys agents and Copilot centrally with Dynamics 365 AI Hub**
	- Dynamics 365 AI Hub provides a single, in‑product location to manage all Customer Insights - Journeys agents and Copilot features for your environment. You can complete prerequisites, enable or disable agents, and configure guardrails such as follow‑up limits or processing caps, without navigating between tools. Because AI Hub is aligned with tenant‑level settings in Copilot Hub in Power Platform Admin Center, your environment automatically remains compliant with global governance policies.
	- [Docs](ai-hub.md)

#### Monthly enhancements

- **Notifications about quota consumption for Customer Insights - Journeys**
	- Dynamics 365 Customer Insights now notifies you as your organization approaches its paid consumption quotas. You can also view detailed consumption information in **Settings** > **Overview** > **Quota limits**, making it easier to monitor usage, understand trends, and plan as your usage grows.
	- [Docs](quota-management.md)

- **Create lead records from journey update**
    - When creating a lead record from the new [Create record action](create-records-activities.md) in journeys, standard fields are now pre-populated.
    - [Docs](create-records-activities.md#add-optional-fields)

- **Test send with multiple conditional content variations**
	- Test send now lets you select up to 10 conditional content variations and send a test email for each in a single action. This makes it easy to validate that every variation of your email renders correctly before launching your campaign, without repeating the test for each email.

- **Segment expiration window extended to 120 days**
    - Last month, we began changing the state of segments that had been unused for more than 30 days to a new "Expired" state. We've now extended that automatic expiration window to 120 days. Expired segments can be republished to put them back in a "Ready to use" state for use in journeys and other segments.

- **Improved formatting for segment query viewer**
    - The query viewer in the segment designer has been updated with improved formatting, making it easier to read and understand the query structure.

- **Drag and drop attributes and conditions for faster segment editing**
    - Build segments even faster with new drag-and-drop segment editing capabilities. You can drag in attributes, interactions, and segments from the right panel directly onto the design canvas to add them to existing groups or create new ones. You can also drag and drop groups and conditions within the canvas to quickly reorder elements.

- **Audit history tab is now available for segments**
    - When auditing is enabled for segments, an "Audit history" tab is now available to make it easier to view past changes to the segment definition.

### April 2026 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys | 1.1.64196.104 |

#### General availability

- **Edit and view segment definitions directly using query editor**
    - Viewing the exact details about how your segment works is now easier than ever with the new query viewer in the segment editing experience. The query viewer opens alongside your editing window so you can see how your changes update the SQL query backing the segment in real time. You can also make changes in the SQL query directly that are reflected back into the segment builder or copy the SQL query from one segment to another as an editing shortcut.
    - [Docs](real-time-marketing-build-segments.md#view-and-edit-your-segment-with-the-query-view)

#### Public preview

- **Automatically update emails with the latest content**
	- Dynamic content blocks eliminate such manual work and the risk of sending emails with outdated content. When a dynamic content block is updated, all emails using that block are automatically refreshed to ensure recipients always receive the most current content.
	- [Release plan](/dynamics365/release-plan/2026wave1/customer-insights/dynamics365-customer-insights-journeys/automatically-update-emails-latest-content)
	- [Docs](content-blocks.md#static-vs-dynamic-content-blocks)

- **Transform customer journeys into action with record creation**
	- You can now create any record or activity directly from a journey with full control over fields and dynamic values. Instead of rigid workflows or manual data entry, you can automate actions for any scenario, including handing off high-value leads and opportunities or creating tasks for prompt follow-up, without leaving the journey builder. This means faster processes, fewer errors, and more flexibility to adapt customer journeys to your unique business needs without custom development.
	- [Release plan](/dynamics365/release-plan/2026wave1/customer-insights/dynamics365-customer-insights-journeys/close-leads-faster-automating-seamless-handoffs-between-marketing-sales)
	- [Docs](create-records-activities.md)

#### Monthly enhancements

- **Using HTML in personalization data requires explicit user acknowledgment**
	- Dynamic text and lists allow you to personalize content in emails and text messages. The source content used for personalization is typically expected to be plain text, so brand and other formatting is applied consistently across the entire message. However, there may be situations where you need to insert additional HTML tags in this source content to achieve specific formatting. We've introduced a new advanced option that allows HTML insertion to be included in the source content. For safety, this option is disabled by default.
	- [Docs](real-time-marketing-predefined-dynamic-text.md#allow-html-content-in-source-content)

- **Fix email rendering issues**
	- Rendering emails exactly as designed is critical for protecting a company's brand. However, email clients vary widely in how they interpret standard HTML. While the email designer automatically generates special HTML code to handle a variety of email clients, there may still be specific situations where emails don't render as expected. We've added a new article documenting known email rendering issues and tips and workarounds for them.
	- [Docs](email-troubleshoot-rendering.md)

### March 2026 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys | 1.1.62960.63 |

#### General availability

- **Create static segments with up to 200,000 members**
    - Marketers often receive customer lists from various systems and need to act quickly. These lists typically lack the attributes required for dynamic segments or aren't part of an existing Dataverse view. This feature enables marketers to build static segments with up to 200,000 members using data from any source. Marketers can upload CSV files, use the API to create segments as part of a workflow, or select contacts from a Dataverse view.
    - [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/create-static-segments-up-200000-members)
    - [Docs](real-time-marketing-build-segments.md#statically-include-or-exclude-up-to-2000000-segment-members)

- **Drive confident engagement with enhanced consent‑based segmentation**
	- As a marketer, you want to grow relationships on a foundation of trust, sending messages only to customers who expect to hear from you. Enhanced consent‑based segmentation turns your consent policies into clear, ready‑to‑use audiences. You can instantly see who qualifies for each purpose and channel, and build segments that stay aligned with your compliance profiles by design. You move faster from consent data to active audiences, so every journey is both relevant and respectful of customer choices.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/drive-confident-engagement-enhanced-consentbased-segmentation)
	- [Docs](real-time-marketing-consent-segments.md)

#### Public preview

- **Set message expirations to keep communication relevant**
	- Customers may experience frustration when they receive outdated communications, such as expired coupons and irrelevant reminders. This creates confusion and diminishes their trust in your brand. You can now set expiration dates on your messages, ensuring that only current and relevant information reaches your audience. This keeps your customers engaged and satisfied with relevant communications in moments that matter.
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/set-message-expirations-keep-communication-relevant)
	- [Docs](message-expiration.md)

#### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Real-time web personalization with Dynamics 365 Customer Insights - Data](https://community.dynamics.com/blogs/post/?postid=4979be1e-2417-f111-8341-6045bddc3c65)

### February 2026 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys | 1.1.62310.76 |

#### General availability

- **Maximize event ROI with paid registration, seamless payment integration** 
	- Hosting impactful events demands significant time, resources, and budget, but often requires the use of disparate and fragmented tools to sell event tickets. This challenge makes it difficult to track payments, reduce registration drop-off, and ultimately provide a delightful attendee experience. With the new paid event registration capability in real-time journeys, you can now offer a seamless and secure ticketing experience. We're introducing support for session registrations with passes, ensuring that attendees can only register for sessions that the pass gives them access to.  
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/maximize-event-roi-paid-registration-seamless-payment-integration) 
	- [Docs (event passes)](real-time-journeys-event-passes.md), [Docs (payment gateway)](./developer/payment-gateway-integration.md)

- **Enhanced reCAPTCHA**
	- Marketers rely on clean, trustworthy data to run effective journeys, but automated bot submissions can overwhelm forms, skew insights, and reduce conversion rates. Before this update, protecting forms required outdated HIP captcha or custom technical work, creating friction and leaving gaps in security. With the new built‑in reCAPTCHA, you protect your forms from bots while keeping the experience fast and accessible for real customers. You can add strong bot protection in seconds. No coding, no developer support, and no risk of losing data quality. This update boosts confidence in your form submissions, reduces spam, and ensures that every interaction you collect reflects real customer intent. The legacy HIP captcha is being deprecated to move to a more modern, secure, and user‑friendly reCAPTCHA experience. The HIP captcha will be deprecated in March 2026 and fully removed from all Customer Insights ‑ Journeys forms by June 30, 2026. 
	- [Release plan](/dynamics365/release-plan/2025wave2/customer-insights/dynamics365-customer-insights-journeys/strengthen-form-bot-protection-recaptcha) 
	- [Docs](real-time-marketing-form-security-privacy.md#protect-forms-from-bots-with-recaptcha)

#### Monthly enhancements

- **Segmentation - Unused segments are not evaluated after 30 days**
	- Segments that are published but not used in any live journey for 30 days are moved to the Expired state. These expired segments are no longer evaluated and aren't counted towards your segment limits, helping to save resources and boost overall performance. You need to publish them again before they can be used in a journey.

- **Segmentation – Usability and functional enhancements**
	- Several enhancements have been introduced to segmentation. Key improvements include:
		* Updates to the user interface and insights charts to fix accessibility issues and make them mobile friendly.
		* Ability to refresh segments manually.
		* Added common commands *Assign* and *Deactivate* to the command bar and enable them for customization.
		* Support for circular relationships (Contact > related table(s) > Contact).
		* Changed how related tables are evaluated to align with more common usage (`RELATEOPTIONAL` is the default now, `RELATE` remains available through the advanced menu. `RELATEOPTIONAL` allows rows to be returned even when the related record doesn't exist, treating the relationship as optional).
		* Stopped segments can be edited and published again.
		* Fixed issues with timeline where items were showing up out of order and had other issues with the end of the year.
		* Improved messages and information throughout (for example, show logical name to disambiguate similarly named attributes).
		* Increased query field size to support longer queries.

- **Ability to set co-organizers for Teams Town Hall**
	- You can now automatically assign co-organizers to Microsoft Teams Town Hall events directly within Customer Insights – Journeys. This enhancement streamlines event management, improves collaboration, and ensures smoother execution by giving additional users the ability to help manage and run Town Hall sessions.
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
