---
title: Real-time journeys transition FAQs
description: Discover how to transition from outbound marketing to real-time journeys in Customer Insights - Journeys. Get answers to frequently asked questions.
ms.date: 04/14/2025
ms.topic: faq
author: alfergus
ms.author: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Real-time journeys transition FAQs

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

## What changes to Dynamics 365 Customer Insights – Journeys did Microsoft recently announce?

Customer Insights – Journeys includes two modules: outbound marketing and real-time journeys. Released in August 2021, real-time journeys offer advanced enterprise capabilities. Real-time journeys has been the default offering to new customers since August 2023.

After announcing in August 2023 that we'll only invest in real-time journeys, we're now officially announcing that we're removing outbound marketing as of June 30, 2025. To avoid business continuity issues, all customers still using outbound marketing must transition to real-time journeys before this date. As of December 2024, social posting and LinkedIn lead generation capabilities are also removed. We don't plan to support social posting in real-time journeys because it has low demand and usage. However, we're considering adding LinkedIn lead generation to real-time journeys in a future release.

No new licensing or provisioning is required to use real-time journeys; every one of your existing environments already has it. The updated license removes limits on the number of environments (see [Announcing unlimited application installs in Dynamics 365 Customer Insights](https://www.microsoft.com/dynamics-365/blog/it-professional/2024/06/18/announcing-unlimited-application-installs-in-dynamics-365-customer-insights/)), so you can easily try real-time journeys in a separate environment if needed.

There's a dedicated section for transition guidance: [Transition overview](transition-overview.md). You should bookmark this section. We update it regularly based on product updates, questions, and feedback.

## I'm an existing Dynamics 365 Customer Insights - Journeys customer using outbound marketing. How do these changes impact me?

As an existing outbound marketing customer, note the removal dates and transition to real-time journeys to avoid interruption. If you're using social posting or LinkedIn lead generation capabilities, they're already removed and your ability to create new social posts or LinkedIn leads is restricted. Your data is still available for reporting.

Newly created, copied, migrated, or restored environments only include real-time journeys. You might be able to add outbound using the **Enable** link on the **Settings** > **Version** page. This link is only available when another existing environment with outbound marketing is present. If you don't see the **Enable** link and you need access to outbound marketing, follow the guidance for [requesting outbound marketing to be added](transition-overview.md#if-the-enable-link-isnt-available-or-doesnt-work).

## I'm a new Dynamics 365 Customer Insights - Journeys customer. How do these changes impact me?

As a new customer, when you provision Customer Insights – Journeys, you only see real-time journeys. We don't offer outbound marketing to new customers, so you should plan to implement and go live with real-time journeys. We can't make any exceptions to this, so you shouldn't raise support requests for adding outbound marketing.

## I can't transition by the outbound marketing removal date. Can I request an extension?

We first announced the removal of outbound marketing in August 2023 and later set June 30, 2025 as the removal date, which remains unchanged. As detailed in [the next question](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working), after June 30, 2025, we'll begin taking steps to reduce outbound marketing usage and eventually remove it. If you've begun your transition and need more time, you can request an extension as explained in this document: [Requesting an extension for outbound marketing removal](https://download.microsoft.com/download/ef2db164-d7ef-4fdd-be9a-308939d1b4e1/OBMtoRTM.pdf) (downloadable PDF). Extension requests aren't automatic; they're evaluated on a case-by-case basis. If approved, extensions are granted for a limited period only.

## What will happen after June 30, 2025? Will outbound marketing stop working?

We'll gradually phase out outbound marketing. Starting sometime in June 2025, users trying to create new outbound marketing emails, journeys, segments, forms, events, etc., will see a message dialog advising them to use real-time journeys instead and informing them of the upcoming removal of outbound marketing. Initially, users can dismiss the dialog and continue creating outbound marketing objects. However, sometime in the near future (date to be decided based on outbound usage data), this dialog becomes non-dismissible and will block users from creating new outbound marketing content. Existing journeys, segments, forms, and events will continue to work. Unused segments won't be evaluated, and in-use segments may be evaluated less frequently. Outbound marketing support may be limited to critical issues only. As outbound marketing usage declines and eventually stops, we'll hide it from the interface and then remove it completely. Banner messages will be displayed before these actions are taken.  Decision to hide (and later, remove) outbound will be taken automatically by the system and will occur at different times for each customer. Until outbound is hidden, you will be able to use it to access existing campaigns, events, forms, reports etc. Once it is hidden, the data will still be present, but you may not be able to access it from the user interface. See also [What will happen to outbound tables and data when outbound marketing is removed?](transition-faqs.md#what-will-happen-to-outbound-tables-and-data-when-outbound-marketing-is-removed).

## What will happen to outbound tables and data when outbound marketing is removed?

When outbound marketing is removed, the sitemap entry and outbound marketing services will be removed. We won't delete any publicly documented outbound marketing tables or data from those tables, with some exceptions (see below). While the tables and data remain in the system, they **won't** be updated or refreshed, and they may not be usable or accessible from the user interface once the outbound marketing sitemap entry has been removed. See additional details below (this information is subject to change and will be updated as we get closer to the outbound marketing removal date):
- The **asset library** is common to both outbound marketing and real-time journeys. As such, the library and the items in it continue to be available and useable.	
- Outbound marketing **analytics** data will be merged with real-time journeys data.
    - Existing Power BI custom reports for outbound marketing won't work with the consolidated data because the data format, its location, and access methods are different in real-time journeys.
    - Insights reports that are part of the outbound marketing user interface won't be available anymore.
- **Events** is a shared capability between real-time journeys and outbound marketing and the same tables are used. These tables and the data won't be removed.
    - However, there are some critical differences in the event forms and pages between outbound marketing and real-time journeys. Therefore, events created in outbound marketing will stop working once outbound marketing is removed. Outbound marketing events that go past the outbound marketing removal date must be recreated in real-time journeys.
- Outbound marketing **segments** won't be removed but won't be usable.
    - The segment table itself doesn't contain the actual list of members; this information is stored in an internal table that will be removed. If you want to retain segment member data, you must export the segment data before outbound marketing services are removed.
    - Outbound marketing segments are currently available for use in real-time journeys. This functionality won't be supported once outbound marketing is removed. Any journey that uses outbound marketing segments will stop working.
- While the outbound marketing user interface won't be available in the sitemap, outbound marketing tables can still be accessed using the advanced search (or in some cases using the standard user interface such as in the contact timeline, which has links to outbound marketing messages). These forms, while available, may not work correctly and won't be supported.
- The **import email tool** in real-time journeys will be kept for an additional few months after outbound marketing is removed.
- Outbound marketing **emails**, **content blocks**, **forms**, **segments**, **marketing pages**, **consent data**, **journeys**, **templates**, **lead scoring models**, **social posts**, and **subscription lists** won't be deleted.
    - As these assets can't be used in real-time journeys, they need to be migrated or recreated. For more information, review the individual pages for each feature area in the transition guidance section: [Functional areas overview](transition-walkthrough-functional.md).
    - While these tables will remain, any custom user interface that updated or added records to them and relied on outbound marketing services may fail (for example, any custom user interface that had plugins that reacted on retrieve/retrieve multiple messages).
- **Marketing lists** won't be deleted. You can continue using them in real-time journeys (you can include them in real-time journeys dynamic segments).
- **Interaction data** won’t be deleted. Outbound marketing interaction data is being moved into the same store where real-time journeys interactions are stored. This enables combined reporting and interaction-based segments irrespective of where the interactions occurred (in outbound marketing or in real-time journeys). The [contact and lead timeline](timeline.md) already shows last (one) year of interactions from both outbound marketing and real-time journeys. To show data prior to that, you must [build custom reporting or export the data](transition-walkthrough-insights.md#how-to-transition).

## Why aren't you supporting social posting in real-time journeys? Do you have a recommendation on what to use instead?

We decided not to support social posting capabilities in real-time journeys because it had low demand and usage. It's also not core to our real-time orchestration strategy. While there are many point solutions for social posting, we can't provide any single recommendation. We'll continue to collect customer feedback and evaluate market demand to update our plans as needed.

## How should I plan for the transition?

We've prepared extensive resources (guidance, tools, and discussion forums) to help with the transition. See [Transition overview](transition-overview.md).

## What about my outbound marketing features that are currently unavailable in real-time journeys?

Real-time journeys is based on newer technology and has a different approach so that it can offer capabilities that outbound marketing can't. Customers might need to change their approach from what they used in outbound marketing. For instance, many scenarios are better solved with triggered journeys instead of segment-based journeys. While this requires designing journeys differently using triggers instead of segments, it's important to focus on the long-term benefits such as scale, Copilot, and other innovations that outbound marketing can't offer. That said, since the announcement we've prioritized many specific features in real-time journeys based on customer feedback and usage. To see more details on specific differences and workarounds, review the [functional area-specific pages](transition-walkthrough-functional.md).

## Why should I transition to real-time journeys?

Real-time journeys introduces new ways of marketing by integrating the latest generative AI capabilities while covering and enhancing traditional outbound scenarios. It offers a wealth of benefits to deliver engaging B2C and B2B experiences.

By transitioning to real-time journeys now, you can enjoy the following benefits:

**Leverage generative AI to do more with less**

Real-time journeys already assists marketers with several built-in Copilot capabilities to:

- Target the right audience simply by describing your segments using everyday words.
- Generate engaging email content within seconds simply by writing key points or selecting a topic and a tone of voice matching your message.
- Receive image recommendations from the library that complement your emails.
- Easily rewrite your existing content to make your messages more compelling.
- Create new journeys just by describing them in simple words.
- Prevent messages from sending during unwanted times.
- Effortlessly style your emails and forms based on your website design.
- Get step-by-step guidance to authenticate your domain.

**Optimize every interaction**

- Experience seamless integration with Dynamics 365 Customer Insights – Data to capitalize on customer understanding and insights to enhance every interaction.
- Craft journeys for contact and lead entities in Dataverse or profiles from Customer Insights - Data.
- React to customers' actions instantly using out-of-the-box triggers, custom triggers, or triggers based on any data change in Dataverse all without writing any code.
- Refine your audience targeting with advanced segmentation capabilities and an unlimited number of segments.
- Deliver your messages through out-of-the-box text messages, push notifications, and custom channels, and benefit from AI-powered channel optimization to reach customers on the most effective channel.
- Embrace hyper-personalization features like dynamic text and no-code conditional content to support 1:1 targeted, responsive campaigns tailored to individual preferences.

**Unify sales and marketing**

- Easily create powerful registration forms, identify leads, organize events or create nurturing journeys.
- Define granular qualification criteria to better identify and prioritize leads with the upcoming enhanced lead scoring builder.
- Align your efforts with sellers by sharing a unified timeline of customer activities.
- Seamlessly transfer qualified leads to the sales team or engage sales representatives within your customer journey at exactly the right time by assigning a sales call or triggering a sales sequence to further increase the likelihood of closing deals.

**Scale your business**

- Use business units, brand profiles, and the new consent center to tailor real-time journeys to cater to your business’s unique requirements.
- Scale your business with 300 million monthly interactions and reach up to 100 million marketing contacts.

Overall, transitioning to real-time journeys is a powerful way for your business to improve marketing strategies, enhance customer engagement, and drive growth.

## How do I start with real-time journeys?

New customers start directly in real-time journeys. As a new customer, start by exploring the main functionalities, creating a journey, or sending a quick email.

If you're a current customer using outbound marketing, you're in “mixed-mode” where both outbound marketing and real-time journeys capabilities are available and can be used simultaneously. Start progressively with real-time journeys and ramp up after you gain confidence. Use real-time journeys for running new journeys. This way, you have time to train and troubleshoot dependencies or issues that might arise. After creating and successfully running a few real-time journeys, continue by moving your outbound marketing journeys. This is a great time to revisit and redesign old journeys. For instance, many of your outbound marketing journeys could flow more naturally and be reused by using triggers in real-time journeys.

> [!div class="mx-imgBorder"]
> ![Graphic showing a gradual transition from outbound to real-time journeys.](media/outbound-to-real-time.png "Graphic showing a gradual transition from outbound to real-time journeys")

To ensure your transition to real-time journeys is a success, we've designed a user-friendly interface that doesn't require extensive retraining. You'll experience interface enhancements that significantly improve usability and efficiency.

To kickstart delivering experiences using real-time journeys, we've designed an email transition tool, made outbound segments available directly in real-time journeys, and empowered you to generate more engaging content and revisit or create new journeys within minutes with our new AI-powered Copilot features.

## Where can I get help setting up real-time journeys?

Real-time journeys is already available. To get started, consult our learning center: [Customer Insights - Journeys overview](real-time-marketing-overview.md).

If you're transitioning from outbound marketing, review our resource page: ([Real-time journeys transition resources](transition-resources.md)).

Reach out to your account manager with further questions or if you need help.

## Will transitioning to real-time journeys require significant retraining due to a new user interface?

Transitioning to real-time journeys doesn't require extensive retraining, particularly for the most common marketing activities. In these areas (listed below), you either encounter no differences in the user interface between outbound marketing and real-time journeys, or you experience user interface enhancements that significantly improve usability and efficiency.

**Email creation**

- Users familiar with the outbound marketing email designer will find the same interface in real-time journeys for basic design and editing capabilities. The interface offers easier and more efficient personalization without need for coding or scripting.

**Event planning**

- The user experience for event planning and forms remains the same in both outbound marketing and real-time journeys, eliminating the need for additional training.

**Forms**

- Forms benefit from a revamped user experience based on the email designer.

**Segment building**

- The segment builder in real-time journeys has a user-friendly and intuitive interface. It now supports natural language instructions, simplifying segment creation. Users can provide instructions in everyday language instead of creating complex queries.

**Journeys**

- The journey user interface has been redesigned in real-time journeys. Any retraining required for the redesigned journey interface is considered a worthwhile investment, as it improves usability and effectiveness.

## What's the new scale of real-time journeys and how does it compare to the previous level?

Marketers can now reach up to 100 million contacts or leads and send up to 300 million interactions per month in real-time journeys. This is over three times the previous outbound marketing limit of 30 million contacts and 100 million monthly interactions.

This added capacity empowers marketers to deliver personalized experiences at scale and delight their customers in new ways. Additional interactions help marketers grow their business, whether by increasing their customer base in new markets, reaching additional geographies, promoting new products, or expanding their prospective customer pipeline to reach higher sales targets.

## When is the increased scale available and is it available only for real-time journeys?

The new scale of 100 million contacts or leads and 300 million monthly interactions can only be unlocked with real-time journeys. It's available immediately for customers who need to operate at the new scale. To learn more, contact your Microsoft representative.

## Are there any additional costs associated with the increased scalability level? What is the implementation process?

There's a contact threshold of 10 million contacts purchased that unlocks the new scale. To unlock the new scale and receive the increased throughput, existing customers and new customers must meet the 10 million contact threshold.

To unlock the new scale, reach out to your Microsoft sales representative with your requirements. The end-to-end process to upgrade to the new scale is completed within two weeks.

[!INCLUDE [transition-comments](./includes/transition-comments.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
