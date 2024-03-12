---
title: New and upcoming features
description: Information about new features, improvements, and bug fixes in Dynamics 365 Customer Insights - Journeys releases.
ms.date: 03/12/2024
ms.topic: article
author: alfergus
ms.author: alfergus
ms.collection: bap-ai-copilot
---

# What's new in Dynamics 365 Customer Insights - Journeys

[!INCLUDE [marketing-trial-cta](./includes/marketing-trial-cta.md)]

We're excited to announce our newest updates! This article summarizes early access features, preview features, general availability enhancements, monthly updates, and bug fixes. To see the long-term feature plans, take a look at the [Dynamics 365 and Power Platform release plans](/dynamics365/release-plans/).

Customer Insights - Journeys updates are [pushed to customers automatically](https://cloudblogs.microsoft.com/dynamics365/it/2020/04/27/automatic-update-policy-for-dynamics-365-marketing/). Solutions are available for early validations. To manually update your instances, follow the steps in [Keep Customer Insights - Journeys up to date](apply-updates.md).

To submit and vote on **feature requests** and **product suggestions**, go to the [Dynamics 365 Application Ideas portal](https://experience.dynamics.com/ideas/categories/?forum=dfa5b83d-9e4c-e811-a956-000d3a1bef07&forumName=Dynamics%20365%20Marketing).

## March 2024 update

### Version number

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        |   1.1.37290.68    |

### Public preview

- **Receive in-app task assistance from Copilot**
    - Use Copilot to receive timely in-app guidance in everyday language. You can also ask questions, which Copilot answers with reference to the Dynamics 365 Customer Insights - Journeys documentation.
    - [Release plan](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/receive-in-app-task-assistance-copilot)
    - [Docs](faqs-copilot-general.md)

- **Easily manage customer consent from contact and lead forms**
    - Enhanced contact and lead forms enable you to quickly see and update a customer's consent, helping you effortlessly manage which types of messages are sent to your customers. This comprehensive view gives you a single place to manage consent across every channel and line of business for your organization. See if a customer has opted out of all commercial communication from your business. Explore which topics a contact has opted in or out of receiving across all channels: email, text, and custom channels. Get a complete understanding of each contact and lead's consent preferences in one easy-to-use screen.
    - [Release plan](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/easily-manage-customer-consent-contact-lead-forms)
    - [Docs](real-time-marketing-email-text-consent.md#view-consent-records)

- **Build custom reports using Microsoft Fabric integration**
    - In today's data-driven world, marketers face the challenge of gaining a comprehensive view of their campaigns to make informed decisions. Each business has unique needs and requirements for aggregating data from various sources. While Dynamics 365 Customer Insights - Journeys already offers powerful out-of-the-box reports, the app also offers additional custom reporting capabilities to address your unique scenarios. Now in real-time journeys, you can effortlessly create custom Power BI reports tailored to your business needs by leveraging Microsoft Fabric capabilities. Harness seamless access to data to gain a complete understanding of your campaigns, lead management, market performance, and customer engagement, enabling you to identify new opportunities.
    - [Release plan](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/effortlessly-build-custom-reports-tailored-business-needs-using-fabric-integration)
    - [Docs](fabric-integration.md)

### Monthly enhancements

- **Email editor**
    - Accurately preview your real-time journeys emails in a wide variety of target email clients and platforms with Litmus integration.

### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [What you need to know about the event portal in Customer Insights – Journeys (FastTrack blog)](https://community.dynamics.com/blogs/post/?postid=9eef0126-bbbb-ee11-92bd-6045bdb56f43)
- [Understanding email variation in Customer Insights - Journeys (FastTrack blog)](https://community.dynamics.com/blogs/post/?postid=adfbe765-9dca-ee11-92bd-000d3a01c528)

## February 2024 update

### Version number

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        |   1.1.37290.59    |

### General availability

- **Stay compliant with one-click unsubscribe for emails**
    - One-click unsubscribe keeps you compliant with new requirements from Google and Yahoo for bulk email senders. Making it easy to unsubscribe from your messages in a single click improves your reputation as a brand and as an email sender. When combined with real-time journey consent topics, one-click unsubscribe encourages your customers to stay subscribed to your other commercial emails while unsubscribing from a single topic. Letting customers opt out easily can improve open rates, click-through rates, and ensure that your messages are less likely to be marked as spam.
    - [Release plan](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/stay-compliant-one-click-unsubscribe-emails)
    - [Docs](one-click-unsubscribe.md)

### Public preview

- **Streamline email creation with real-time HTML edits**
    - Easily customize emails in Dynamics 365 Customer Insights - Journeys with the ability to toggle back and forth between the visual editor and HTML code. Get more control over how you display information by marking the code and seeing how it renders across devices and email clients.
    - [Release plan](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/streamline-email-creation-real-time-html-edits)
    - [Docs](email-creation-with-html-edits.md)

- **Boost participation and simplify planning with session-based event registrations**
    - Event attendees can register for specific sessions in a multi-session event to ensure their event experience is relevant to their interests. You’ll be able to identify which sessions have the highest demand and tailor post-event follow-ups based on session participation.
    - [Release plan](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/boost-participation-simplify-planning-session-based-event-registrations)
    - [Docs](real-time-journeys-event-session.md)

- **Ensure messages go to the right contact email address**
    - It's critical that your messages are delivered by the right channel at the right time. Often, you'll need to pick the correct email address among the several you may have for a contact. Now, you can choose which of the contact’s email addresses to target in your journeys. For example, some email messages may be more appropriate for a contact’s work email address, whereas others may best target a personal email address. Now, you have full control over which email address to send email messages to, enabling you to reach your customers where they’re most likely to see your messages and take action.
    - [Release plan](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/ensure-messages-go-right-contact-email-address)
    - [Docs](real-time-marketing-audience-data.md)

### Monthly enhancements

- **Analytics: Optimize marketing efforts with enhanced channel insights**
    - With the introduction of improved key performance indicators, you can get a deeper understanding of your text, push notification and custom channels effectiveness. You can also access detailed reports on delivery and interaction metrics, export up to 50,000 records of interaction data, and see the profiles of the people who engaged with your messages.
- **Personalization: Dynamic data source for event registration code**
    - Make your life easier and enhance efficiency by using a single event registration confirmation email for many events. Create triggered journeys and design your emails to use the trigger as a data source for dynamic data for event details including a QR code that shows a personalized registration code for the recipient, enabling faster check-ins. You can still use the specific event option, if needed. (Note: this enhancement is available only in real-time journeys. Outbound marketing is still limited to using specific event selected at the design time and hence requires a separate email for each event). Learn more: [Use QR codes for event registration, links to content, or URLs](email-QR-code.md)
- **Quiet times: Change or disable quiet times for a specific message**
    - Change or disable quiet times enforcement on a particular message within a journey to support scenarios when a particular message in a journey should not be subject to regular quiet times settings. You can either pick from alternative quiet times settings that have already been created or disable quiet times enforcement entirely for the message.

### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights - Journeys features in our latest blogs and scenario docs:

- [Shaping the future of retail with AI and Dynamics 365 - Microsoft Dynamics 365 blog](https://cloudblogs.microsoft.com/dynamics365/bdm/2024/01/11/shaping-the-future-of-retail-with-ai-and-dynamics-365/)
- [Enhanced data collection and journey personalization with unmapped form fields](https://community.dynamics.com/blogs/post/?postid=3a361b7e-80b0-ee11-92bd-002248527d3d)
- [Transition to real time journeys – the time is now - Microsoft Dynamics 365 blog](https://cloudblogs.microsoft.com/dynamics365/it/2024/01/09/transition-to-real-time-journeys-the-time-is-now/)

## January 2024 update

There is no Dynamics 365 Customer Insights - Journeys release for January. We will be back in February with new feature improvements, updates, and bug fixes.

### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights - Journeys features in our latest blogs and scenario docs:

- [Customer Insights quickstart guide](customer-insights-quickstart-guide.md)
- [Transition to real time journeys – the time is now - Microsoft Dynamics 365 Blog](https://cloudblogs.microsoft.com/dynamics365/it/2024/01/09/transition-to-real-time-journeys-the-time-is-now/)

> [!Tip]
> To read about updates from previous years, see the [What's new archive](whats-new-marketing-archive.md) article.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
