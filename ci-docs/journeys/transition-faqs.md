---
title: Real-time journeys transition FAQs
description: Discover how to transition from outbound marketing to real-time journeys in Customer Insights - Journeys. Get answers to frequently asked questions.
ms.date: 06/04/2025
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

## What changes to Dynamics 365 Customer Insights – Journeys did Microsoft announce in August 2024?

Customer Insights – Journeys includes two modules: outbound marketing and real-time journeys. Released in August 2021, real-time journeys offer advanced enterprise capabilities. Real-time journeys has been the default offering to new customers since August 2023.

After announcing in August 2023 that we'll only invest in real-time journeys, in August 2024, we officially announced that we would start removing outbound marketing after June 30, 2025. To avoid business continuity issues, all customers still using outbound marketing must transition to real-time journeys. In December 2024, social posting and LinkedIn lead generation capabilities were also removed. We don't plan to support social posting in real-time journeys because it has low demand and usage. However,we may consider adding LinkedIn lead generation to real-time journeys in a future release.

No new licensing or provisioning is required to use real-time journeys; every one of your existing environments already has it. The updated license removes limits on the number of environments (see [Announcing unlimited application installs in Dynamics 365 Customer Insights](https://www.microsoft.com/dynamics-365/blog/it-professional/2024/06/18/announcing-unlimited-application-installs-in-dynamics-365-customer-insights/)), so you can easily try real-time journeys in a separate environment if needed.

There's a dedicated section for transition guidance: [Transition overview](transition-overview.md). You should bookmark this section. We update it regularly based on product updates, questions, and feedback.

## I'm an existing Dynamics 365 Customer Insights - Journeys customer using outbound marketing. How do these changes impact me?

As an existing outbound marketing customer, you must transition to real-time journeys to avoid interruption. If you're using social posting or LinkedIn lead generation capabilities, they're already removed and your ability to create new social posts or LinkedIn leads is restricted. Your data is still available for reporting.

Newly created, copied, migrated, or restored environments no longer include outbound marketing; they contain only real-time journeys. Learn more: [Guidance for existing customers](transition-overview.md#guidance-for-existing-customers-currently-using-outbound-marketing).

## I'm a new Dynamics 365 Customer Insights - Journeys customer. How do these changes impact me?

When you provision Customer Insights – Journeys, you'll see real-time journeys only. We don't offer outbound marketing to new customers, so you should plan to implement and go live with real-time journeys. Don't submit requests or contact support for adding outbound marketing, as new customers aren't eligible for outbound marketing, and no exceptions will be made.

## I need more time to complete the transition. Can I request an extension?

We first announced the removal of outbound marketing in August 2023 and later set June 30, 2025, as the removal date, which remains unchanged. As detailed in [the next section](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working), we have started taking steps to reduce outbound marketing usage and eventually remove it. If you've begun your transition and need more time, you can request an extension as explained in this document: [Requesting an extension for outbound marketing removal](https://download.microsoft.com/download/ef2db164-d7ef-4fdd-be9a-308939d1b4e1/OBMtoRTM.pdf) (downloadable PDF). Extension requests aren't automatic; they're evaluated on a case-by-case basis. Extensions are only approved for customers already in the implementation phase of their transition plans. If approved, extensions are granted for a limited period only. Customers with approved extensions may still see warning messages and dialogs, but will be able to continue using outbound marketing until their approval date.

## What will happen after June 30, 2025? Will outbound marketing stop working?

We are implementing a phased approach for removing outbound marketing to minimize disruption to customers’ businesses. When we detect there are no active outbound marketing campaigns or events in an environment (“org”), we initially hide outbound marketing and then remove it after a few weeks. With this approach, the outbound marketing removal date is different for each environment as it depends on when the outbound marketing campaigns or events complete. While we continue to support outbound marketing, only critical issues are prioritized.

To reduce and eventually end outbound  marketing usage, we're applying a phased approach:

- **Phase 1 - Existing campaigns and event work; new ones can be created**: Users get messages about outbound marketing removal whenever they attempt to create a new outbound marketing email, journey, segment, form, or marketing page. They can dismiss the dialog and continue creating outbound marketing campaigns and events.  
- **Phase 2 - Existing campaigns and events work; new ones *can't* be created**: Users are no longer able to dismiss the dialog and therefore can't create new outbound marketing campaigns or events. We have not yet set a date for this phase; we'll announce it soon.
- **Phase 3 - Existing campaigns and events end, outbound marketing is hidden**: When existing campaigns and events are complete, we'll automatically hide outbound marketing from the user interface. After a few weeks, we'll remove outbound marketing.

We'll continue to communicate through the admin center and in-product messaging to keep you updated. This phased approach may be revised in the future (for example, we may set a common date to remove outbound marketing from all environments, even if they have active outbound marketing campaigns or events).

## I have an approved extension for outbound marketing. What can I expect?

An extension approval implies only one thing: your environment won't be moved to the “blocking” phase (described in the previous section) until after your approved date. Some of the messages and banners about outbound marketing removal may still be shown. Periodic product releases that update and change current functionality will continue to be applied as usual. 

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

[!INCLUDE [footer-include](./includes/footer-banner.md)]
