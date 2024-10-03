---
title: Real-time journeys transition FAQs
description: Answers to frequently asked questions about transitioning to real-time journeys in Customer Insights - Journeys.
ms.date: 09/20/2024
ms.topic: article
author: alfergus
ms.author: alfergus
ms.collection: bap-ai-copilot
---

# Real-time journeys transition FAQs

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

## What changes to Dynamics 365 Customer Insights – Journeys did Microsoft recently announce?

Customer Insights – Journeys includes two modules: outbound marketing and real-time journeys. Released in August 2021, real-time journeys offers advanced enterprise capabilities. Real-time journeys has been the default offering to new customers since August 2023.

After announcing in August 2023 that we'll only be investing in real-time journeys, we're now officially announcing that we're removing outbound marketing as of June 30, 2025. To avoid any business continuity issues, all customers still using outbound marketing must transition to real-time journeys before this date. We'll also remove social posting and LinkedIn lead generation capabilities on December 2, 2024. We don’t plan to support social posting in real-time journeys because it has low demand and usage. However, we're considering adding LinkedIn lead generation to real-time journeys in a future release.

No new licensing or provisioning is required to use real-time journeys; every one of your existing environments already has it. In fact, the updated license removes limits on number of environments (see [Announcing unlimited application installs in Dynamics 365 Customer Insights](https://www.microsoft.com/dynamics-365/blog/it-professional/2024/06/18/announcing-unlimited-application-installs-in-dynamics-365-customer-insights/)), so you can easily try real-time journeys in a separate environment if needed.

We have a dedicated section in our documentation for transition guidance: [Transition overview](transition-overview.md). You should bookmark this section as we update it regularly based on product updates, questions, and feedback.

## I'm an existing Dynamics 365 Customer Insights - Journeys customer using outbound marketing. How do these changes impact me?

As an existing outbound marketing customer, you must make a note of removal dates and transition to real-time journeys before that to avoid interruption. If you're using social posting or LinkedIn lead generation capabilities, note that they'll be removed sooner and your ability to create new social posts or LinkedIn leads will be restricted ahead of the removal date. Your data will still be available for reporting.

As is the case currently, newly created, copied, migrated, or restored environments will only include real-time journeys. You may be able to add outbound using the **Enable** link on the **Settings** > **Version** page. This link is only available when another existing environment with outbound marketing is present. If you don't see the enable link, follow the guidance for [requesting outbound marketing to be added](transition-overview.md#if-the-enable-link-isnt-available-or-doesnt-work)

## I'm a new Dynamics 365 Customer Insights - Journeys customer. How do these changes impact me?

As a new customer, when you provision Customer Insights – Journeys, you'll only see real-time journeys. We're not offering outbound marketing to new customers anymore, so your plan should be to implement and go live with real-time journeys. We're unable to make any exceptions to this, so you shouldn't raise any support requests for adding outbound marketing.

## I can't transition by the outbound marketing removal date. Can I request an exception?

Unfortunately, no. In August 2023, we communicated that outbound marketing will no longer receive investments and migration to real-time journeys was an important next step. We're now giving customers nearly a year advanced notice of the removal date, so customers have adequate time to plan and complete the transition to real-time journeys. You should prioritize and complete transitioning to real-time journeys before the outbound marketing removal date. We're not able to offer any exceptions because outbound marketing won't be supported past this date.

## Why aren't you supporting social posting in real-time journeys? Do you have a recommendation on what to use instead?

We decided not to support social posting capabilities in real-time journeys because it has low demand and usage. It's also not core to our real-time orchestration strategy. While there are many point solutions for social posting, we're unable to provide any single recommendation. That said, we'll continue to collect customer feedback and evaluate market demand to update our plans as needed.

## How should I plan for the transition?

We've prepared extensive resources (guidance, tools, and discussion forums) to help with the transition. See [Transition overview](transition-overview.md)

## Why should I transition to real-time journeys?

Real-time journeys introduces new ways of marketing by integrating the latest generative AI capabilities, while covering and enhancing traditional outbound scenarios. It offers a wealth of benefits to deliver engaging B2C and B2B experiences.

By transitioning to real-time journeys now, you can enjoy the following benefits:

**Leverage generative AI to do more with less**

Real-time journeys already assists marketers with several built-in Copilot capabilities to:

- Target the right audience simply by describing your segments using everyday words.
- Generate engaging email content within seconds simply by writing key points or selecting a topic and a tone of voice matching your message.
- Receive images recommendations from the library that complement your emails.
- Easily rewrite your existing content to make your messages more compelling.
- Create new journeys just by describing them in simple words.
- Target the right audience simply by describing your segments using everyday words.
- Prevent messages from sending during unwanted times.
- Effortlessly style your emails and forms based on your website design.
- Get step by step guidance to authenticate your domain.

**Optimize every interaction**

- Experience seamless integration with Dynamics 365 Customer Insights – Data to capitalize on customer understanding and insights to enhance every interaction.
- Craft journeys for contact and lead entities in Dataverse, or profiles from Customer Insights.
- React to customers' actions instantly using out-of-the-box triggers, custom triggers, or triggers based on any data change in Dataverse all without writing any code. 
- Refine your audience targeting with advanced segmentation capabilities and an unlimited number of segments.
- Deliver your messages through out-of-the-box text messages, push notifications, custom channels, and benefit from AI-powered channel optimization to reach customers on the most effective channel.
- Embrace hyper-personalization features like dynamic text and no-code conditional content to support 1:1 targeted, responsive campaigns tailored to individual preferences.

**Unify sales and marketing**

- Easily create powerful registration forms, identify leads, organize events or create nurturing journeys.
- Define granular qualification criteria to better identify and prioritize leads with the upcoming enhanced lead scoring builder.
- Align your efforts with sellers by sharing a unified timeline of customer activities.
- Seamlessly transfer qualified leads to the sales team or engage sales representatives within your customer journey at exactly the right time by assigning a sales call or triggering a sales sequence to further increase the likelihood of closing deals.

**Scale your business**

- Leverage business units, brand profiles, and the new consent center to tailor real-time journeys to cater to your business’ unique requirements.
- Scale your business with 300 million monthly interactions and reach up to 100 million marketing contacts.

Overall, transitioning to real-time journeys is a powerful way for your businesses to improve marketing strategies, enhance customer engagement, and drive growth.

## What about my outbound marketing features that are currently unavailable in real-time journeys?

Since the announcement of the transition to real-time journeys in August 2023, we've made several feature advancements to bridge most top gaps. For example, double-opt in and multiple improvements to segmentation, forms, journeys, etc., have been released. Over the next several months, we'll continue to make improvements wherever possible to bring you a seamless experience. However, our roadmap may not bring full parity with what was offered in outbound marketing. For more information, review the individual pages for each feature area in the transition guidance section: [Functional areas overview](transition-walkthrough-functional.md)

## How do I start with real-time journeys?

New customers directly start in real-time journeys. As a new customer you can start by exploring the main functionalities, create a journey, or send a quick email.  

If you're a current customer using outbound, you are in “mixed-mode” where both outbound and real-time journeys capabilities are available and can be used simultaneously. Our recommended approach is to start progressively with real-time journeys and then ramp up after you have gained confidence. You can start using real-time journeys for running new journeys. This way you have time to train and troubleshoot any dependencies or issues that may arise. Having created and successfully run a few real-time journeys, continue by moving your outbound journeys. This would be a great time to revisit and redesign them. For instance, many of your outbound journeys could flow more naturally and be reused by using triggers in real-time journeys.  

> [!div class="mx-imgBorder"]
> ![Graphic showing a gradual transition from outbound to real-time journeys.](media/outbound-to-real-time.png "Graphic showing a gradual transition from outbound to real-time journeys")

To make sure your transition to real-time journeys is a success, we've designed a user-friendly interface that doesn't require extensive retraining - you'll experience interface enhancements that significantly improve usability and efficiency.

To easily kickstart delivering experiences using real-time journeys, we've designed an email transition tool, made outbound segments available directly in real-time journeys, and empowered you to generate more engaging content and revisit or create new journey within minutes thanks to our new AI-powered Copilot features.

## Where can I get help setting up real-time journeys?

Real-time journeys is already available. To get started, you can consult our learning center: [Customer Insights - Journeys overview](real-time-marketing-overview.md)

If you're transitioning from outbound marketing, review our resource page ([Real-time journeys transition resources](transition-resources.md)) to receive guidance and prepare your transition to real-time journeys.

Reach out to your account manager with further questions or if help is needed.

## Will transitioning to real-time journeys require significant user retraining due to a new user interface?

Transitioning to real-time journeys doesn't require extensive user retraining, particularly for the most common marketing activities listed below. In these areas, you'll either encounter no differences in the user interface (UI) between outbound and real-time journeys, or you'll experience UI enhancements that significantly improve usability and efficiency.

**Email creation**

- Users familiar with the outbound email designer will find the same interface in real-time journeys for basic design and editing capabilities. The interface offers easier and more efficient personalization without need for any coding/scripting.

**Event planning**

- The user experience for event planning and forms remains the same in both outbound and real-time journeys, eliminating the need for additional training.

**Forms**

- Forms benefit from a revamped user experience based on the email planner.

**Segment building**

- The segment builder in real-time journeys has a user-friendly and intuitive UI. It now supports natural language instructions, simplifying segment creation. Users can provide instructions in everyday language instead of complex queries.

**Journeys**

- The journey UI has been redesigned in real-time journeys. Customer feedback indicates that the new UI is more user-friendly, efficient, and natural. Any retraining required for the redesigned journey UI is considered a worthwhile investment, as it improves usability and effectiveness.

## What's the new scale of real-time journeys and how does it compare to the previous level?

Marketers can now reach up to reach up to 100,000,000 contacts or leads and send up to 300,000,000 messages per month in real-time journeys. This is over 3x the previous outbound marketing limit of 30,000,000 contacts and 100,000,000 monthly interactions.

This added capacity empowers marketers to deliver personalized experiences at scale and delight their customers in new ways. Additional interactions help marketers grow their business, whether by increasing their customer base in new markets, reaching additional geographies, promoting new products, or expanding their prospective customer pipeline to reach higher sales targets.

## When is the increased scale available and is it available only for real-time journeys?

The new scale of 100,000,000 contacts and 300,000,000 monthly interactions can only be unlocked with real-time journeys. This is available immediately for customers who need to operate at the new scale. To learn more, reach out to your Microsoft representative.

## Are there any additional costs associated with the increased scalability level? What is the implementation process?

There's a contact threshold of 10,000,000 contacts purchased that unlocks the new scale. Existing customers that need to upgrade or new customers must meet the contact threshold to unlock the new scale and receive the increased throughput.

To unlock the new scale, reach out to your Microsoft sales representatives with your requirements. The end-to-end process to upgrade to the new scale will be completed within two weeks.

> [!TIP]
> If you have questions or comments, visit the [Outbound to real-time transition community forum](https://community.dynamics.com/forums/thread/?partialUrl=Outbound-to-Real-Time-Transition)

[!INCLUDE [footer-include](./includes/footer-banner.md)]