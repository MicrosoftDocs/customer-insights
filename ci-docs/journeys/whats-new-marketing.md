---
title: New and upcoming features
description: Information about new features, improvements, and bug fixes in Dynamics 365 Customer Insights - Journeys releases.
ms.date: 10/17/2024
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
ms.collection: bap-ai-copilot
---

# What's new in Dynamics 365 Customer Insights - Journeys

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

[!INCLUDE [marketing-trial-cta](./includes/marketing-trial-cta.md)]

We're excited to announce our newest updates! This article summarizes early access features, preview features, general availability enhancements, monthly updates, and bug fixes. To see the long-term feature plans, take a look at the [Dynamics 365 and Power Platform release plans](/dynamics365/release-plans/).

Customer Insights - Journeys updates are [pushed to customers automatically](https://cloudblogs.microsoft.com/dynamics365/it/2020/04/27/automatic-update-policy-for-dynamics-365-marketing/). Solutions are available for early validations. To manually update your instances, follow the steps in [Keep Customer Insights - Journeys up to date](apply-updates.md).

To submit and vote on **feature requests** and **product suggestions**, go to the [Dynamics 365 Application Ideas portal](https://experience.dynamics.com/ideas/categories/?forum=dfa5b83d-9e4c-e811-a956-000d3a1bef07&forumName=Dynamics%20365%20Marketing).

## November 2024 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        |  1.1.50062.76  |

### General availability

- **Split audience into groups to deliver unique customer experiences** 
	- When you want customers to have different experiences in one journey, you need to divide them into groups. While this is possible today using attribute branches or segments, sometimes the number of customers in each branch is more important than what those customers have in common. For example, you may want to send a survey out to a random subset of your customers for feedback, something that would be time-consuming to configure today. The new journey split tile allows you to split your audience into branches to provide a subset of your audience with unique experiences, whether that be a survey, a new type of experience to test, or a first-come promotional offer. You can split your audience by percentages (for cases where you need randomness) or by numbers (for cases where you want to deliver specific experiences to a set number of people). 
	- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/provide-varied-experiences-one-journey-using-journey-split-tiles) 
	- [Docs](real-time-marketing-split-audience.md)

    :::image type="content" source="media/split-number-nov.png" alt-text="Split journey audience by number." lightbox="media/split-number-nov.png":::
    
    :::image type="content" source="media/split-percentage-nov.png" alt-text="Split journey audience by percentage." lightbox="media/split-percentage-nov.png":::

- **Improve engagement and compliance with double opt-in** 
	- By implementing double opt-in, you can cultivate a more effective email marketing strategy, leading to improved compliance, increased open and click-through rates, and a better overall brand experience for subscribers. Privacy and data protection laws in many regions require double opt-in functionality to help verify customer information. Double opt-in requires users to confirm subscription preferences through a follow-up email after the initial subscription. By confirming subscription preferences a second time, you comply with legal requirements and improve engagement by ensuring that users who’ve subscribed are intent on receiving future communications. When customers are certain they want to receive email communications, spam complaints and bounce rates are reduced, and your sender reputation is improved. 
	- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/improve-engagement-compliance-double-opt-in) 
	- [Docs](real-time-marketing-double-opt-in.md)

    :::image type="content" source="media/double-opt-in-nov.png" alt-text="An overview of double opt-in within Customer Insights - Journeys." lightbox="media/double-opt-in-nov.png":::

### Public preview

- **Wait on segment membership to trigger the next step in a journey** 
	- Gain even more control over your customers' experience by waiting for them to become a member of a segment before continuing to the next steps in a journey. This added capability lets you personalize each customer's experience by choosing the correct path and actions relevant to individual customers based on whether they're in a segment. This capability adds to existing if/then capabilities that let you wait for a customer to open an email, click a link, or wait for another trigger to be activated before moving on to the next step in the journey. For example, let's say you use your journey to send credit card activation emails and you want to wait for the customer to activate their card before sending a welcome email. If the customer doesn’t activate their credit card within a few days, you want to send another reminder email. If you have a segment that includes all customers who have activated credit cards, you can use that segment as the condition for the if/then branch to wait for each customer to activate their credit card and send them the right communications. (Note: Due to holiday deployment lockdowns, we expect this capability to be rolled out in all regions by the week of Dec 9, 2024).
	- [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/use-segments-decide-which-path-customer-should-take-journey) 
	- [Docs](real-time-marketing-tile-reference.md#branching-the-customer-journey)

    :::image type="content" source="media/wait-segment-membership-release-planner.png" alt-text="Create a journey that waits until a customer becomes part of a segment then continues to the next step in the journey." lightbox="media/wait-segment-membership-release-planner.png":::

## October 2024 update

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        |  1.1.49129.84   |

> [!IMPORTANT]
> Starting on October 10, 2024, changes to link functionality affect the following areas:
> - **Link tracking**: Links in messages that were sent more than six months prior no longer produce tracking results, but otherwise function correctly. Links in messages sent less than six months prior continue to generate tracking analytics.
> - **Text messages**: URLs sent in SMS messages expire six months after the message is sent and no longer work.
> - **Unsubscribe links**: Unsubscribe links expire six months after the link is created and no longer work.

### Public preview

- **Understand customer inflows and exits at every journey step**
    - It’s critical to understand exactly what happened to each customer who entered and exited your real-time journeys. With improved journey analytics, you’ll gain confidence in the processing of every step in your journey through improved metrics and an increased ability to export data. For example, if your journey uses exit or exclusion segments, you'll be able to see and understand why fewer customers started your journey than were in the entry segment. You'll also be able to see the list of customers who entered and exited each step in the journey and export lists of up to 50,000 people for further analysis.
    - [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/confidently-understand-customer-inflows-exits-at-every-step-journey)
    - [Docs](real-time-marketing-analytics.md#journey-operational-analytics)
    
    :::image type="content" source="media/operational-analytics-1.png" alt-text="An overview of customer inflow, processed, and exit analytics." lightbox="media/operational-analytics-1.png":::

- **Get insights on email engagement with heatmap analytics**
    - Understanding the effectiveness of email campaigns can often be complex, particularly when information and links are abundant. Gaining clarity on which areas or links captivate your audience and drive them to act is crucial for refining the user experience and boosting email performance. Real-time journeys email insights now offer a clear view of your audience's preferences by illustrating their interactions within your emails. This immediate visual feedback highlights the content that resonates the most, empowering you to adjust your messaging for heightened impact and better conversion rates.
    - [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/get-insights-email-engagement-heatmap-analytics)
    - [Docs](email-insights.md)

### Monthly enhancements

- **Easily engage multiple audiences in a single journey with multiple segments**
    - If you already have created specific segments for different purposes and need to reach some or all of them, you can now easily do so by specifying multiple segments for a journey. There's no need to create another segment from scratch, combine existing segments into a composite one, or make multiple copies of the same journeys. Specifying multiple segments is not only straightforward and efficient but also enables marketers without segment creation roles to engage multiple audiences without waiting for a new segment to be created. Additionally, it reduces the number of segments that need maintenance or cleanup and does not add to the overall segment limit. 
        > [!NOTE]
        > All segments should be of the same entity, either leads or contacts or profiles. You can already specify multiple segments as exit segments or exclusion segments. This enhancement extends the ability to specify multiple segments to start a journey. Outbound marketing segments can't be used when specifying multiple segments.
    - [Docs](real-time-marketing-segment-based-journey.md#set-the-journey-start)
    
    :::image type="content" source="media/select-segment-journey.png" alt-text="Engage multiple audiences in a single journey with multiple segments." lightbox="media/select-segment-journey.png":::

### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Customizable error messages for form field validation - FastTrack blog](https://community.dynamics.com/blogs/post/?postid=cdcd1dbf-2b7f-ef11-ac20-7c1e521a63a7)

## September 2024 update

### Version number

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        |   1.1.48225.52   |

> [!IMPORTANT]
> Starting on October 10, 2024, changes to link functionality will affect the following areas:
> - **Link tracking**: Links in messages that were sent more than six months prior will no longer produce tracking results, but will otherwise function correctly. Links in messages sent less than six months prior will continue to generate tracking analytics.
> - **Text messages**: URLs sent in SMS messages will expire six months after the message is sent and will no longer work.
> - **Unsubscribe links**: Unsubscribe links will expire six months after the link is created and will no longer work.

### Public preview

- **Refine email content in running journeys**
    - To maximize customer engagement, it's crucial for customer experience teams to regularly refine email content, ensuring that communication remains current, relevant, and impactful. You can now easily edit content, layout, links, buttons, or dynamic content in your email messages while a journey is running—without creating a new version or interrupting the customer experience. Changing email messages in live journey gives you more freedom and power over your email marketing campaigns and helps you to respond to changing business or customer needs.
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/improve-engagement-editing-emails-live-journeys)
    - [Docs](edit-email-in-live-journey.md)

- **Streamline form filling and event registration with form prefill**
    - The repetitive task of filling out forms can be a significant deterrent to event registration. Nobody likes to repeat information that they've already provided. Imagine loyal customers who attend multiple conferences each year having to input their contact information and preferences every time. Form prefill in Dynamics 365 Customer Insights eliminates the need to repeatedly request basic details from your customers, reducing redundancy and saving time. This not only expedites the registration process but also allows for more strategic collection of customer data over time.
    - [Release plan](/dynamics365/release-plan/2024wave2/customer-insights/dynamics365-customer-insights-journeys/form-prefill-simplifies-form-filling-event-sign-up)
    - [Docs](real-time-marketing-form-prefill.md)

- **Control how fast customers can enter a journey**
    - There are times when you want to reach a large audience, but sending a message to the entire audience at the same time would cause problems for your business. With journey rate limiting, you’ll be able to space out message sending over time by setting how quickly you want customers to enter your journey. This feature helps prevent overwhelming downstream operations with a large influx of requests from customers who receive messages from your journey. For example, let's say you have a journey that sends messages to your entire customer base with a call to action to contact your call center. You may want to avoid creating a poor customer experience due to long wait times from an overwhelmed help desk if you send messages at the same time to everyone. Instead, you can now slow down how fast customers enter the journey, avoiding thousands of phone calls at the same time.
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/improve-customer-experience-controlling-how-fast-customers-enter-journey)
    - [Docs](control-how-fast-enter-journey.md)

### Monthly enhancements

- **Queued messages are not sent when journey is stopped**
    - When a journey is stopped, you now see an immediate change in the journey state to “Stopping.” This assures that your request was received and is being processed. Furthermore, if your messages are still pending in the send queue (this can happen when there is high volume of messages), such messages will now be removed immediately and will not be sent. This avoids a situation where messages continue to be delivered even though the journey has been stopped.
    - [Docs](journeys-overview.md)

- **Maximize email engagement and optimize content with link insights**
    - Link insights in real-time journeys allow you to analyze the performance of individual links in your emails. You can now view key metrics such as click rate and unique clicks per link and easily compare the performance of each link within your email campaigns. Use this data to optimize your content, improve engagement, and make more informed decisions to drive better results.
    - [Docs](real-time-marketing-analytics.md)

<!---

- **Outbound marketing removal notification and ability to hide outbound**
    - In-product banners are now shown to all users to inform them that Outbound marketing will be removed as of June 30th, 2025 and that social posting and LinkedIn lead generation will be removed as of Dec 2nd, 2024. We also added a highly visible card in the Settings > Versions page that talks about moving to real-time and now provide a button that can be used to hide outbound from the site map once the transition is complete.
    - [Docs]()

-->

## August 2024 update

There is no Dynamics 365 Customer Insights - Journeys release for August. We will be back in September with new feature improvements, updates, and bug fixes.

## July 2024 update

### Version number

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        |  1.1.46046.74   |

### General availability

- **Build custom reports using Microsoft Fabric integration**
    - In today's data-driven world, marketers face the challenge of gaining a comprehensive view of their campaigns to make informed decisions. Each business has unique needs and requirements for aggregating data from various sources. While Dynamics 365 Customer Insights - Journeys already offers powerful out-of-the-box reports, the app also offers additional custom reporting capabilities to address your unique scenarios. Now in real-time journeys, you can effortlessly create custom Power BI reports tailored to your business needs by leveraging Microsoft Fabric capabilities. Harness seamless access to data to gain a complete understanding of your campaigns, lead management, market performance, and customer engagement, enabling you to identify new opportunities.
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/build-custom-reports-using-fabric-integration)
    - [Docs](fabric-integration.md)

- **Improve reliability of insights with advanced bot protection**
    - Ensuring the integrity of your data and the efficiency of your operations is paramount. Advanced bot protection in Customer Insights - Journeys empowers your business to thrive by safeguarding your business processes. Improve your business decisions with the confidence of knowing that the data you collect is accurate and represents real human interactions. With bot protection, you not only enhance the quality of your insights but also elevate the customer experience by minimizing disruptions caused by malicious bots.
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/improve-reliability-insights-advanced-bot-protection)
    - [Docs](bot-protection.md)

- **Optimize email content based on customer behavior across devices**
    - In real-time journeys email insights, you can now delve into comprehensive device data, including operating systems, browsers, device types, and email clients. Leverage the power of detailed engagement analysis across different platforms to fine-tune your marketing strategy. Tailor your email's design and content to align with the devices most used by your audience, ensuring seamless readability for your messages and, ultimately, leading to heightened customer interaction and loyalty.
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/increase-email-engagement-optimizing-content-based-customers-behavior-across-devices)
    - [Docs](real-time-marketing-analytics.md#email-insights)

### Public preview

- **Improve engagement and compliance with double opt-in**
    - Privacy and data protection laws in many regions require double opt-in functionality to help verify customer information. Double opt-in requires users to confirm subscription preferences through a follow-up email after the initial subscription. By confirming subscription preferences a second time, you comply with legal requirements and improve engagement by ensuring that users who’ve subscribed are intent on receiving future communications. When customers are certain they want to receive email communications, spam complaints and bounce rates are reduced, and your sender reputation is improved.
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/improve-engagement-compliance-double-opt-in)
    - [Docs](real-time-marketing-double-opt-in.md)

- **Split your audience into groups to deliver unique customer experiences**
    - When you want customers to have different experiences in one journey, you need to divide them into groups. While this is possible today using attribute branches or segments, sometimes the number of customers in each branch is more important than what those customers have in common. For example, you may want to send a survey out to a random subset of your customers for feedback, something that would be time-consuming to configure today. The new journey split tile allows you to split your audience into branches to provide a subset of your audience with unique experiences, whether that be a survey, a new type of experience to test, or a first-come promotional offer. You can split your audience by percentages (for cases where you need randomness) or by numbers (for cases where you want to deliver specific experiences to a set number of people).
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/provide-varied-experiences-one-journey-using-journey-split-tiles)
    - [Docs](real-time-marketing-split-audience.md)

### Monthly enhancements

- **Optimize your email content with enhanced insights for conditional content variations**
    - You can now effortlessly compare the performance of different email variants using conditional content within real-time journeys. Gain valuable insights into key metrics such as open rates, click rates, and unique clicks for each conditional content variant, enabling you to identify what resonates best with your audience. Optimize your email campaigns by leveraging data-driven decisions to improve engagement and drive better results.
    - [Docs](real-time-marketing-analytics.md#email-insights)

## June 2024 update

### Version number

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        |   1.1.43992.110   |

> [!NOTE]
> On July 1, 2024, active journeys in the real-time journeys area that were created on or before May 5, 2022 will stop working. To avoid disruption, follow the steps outlined in the [Known issues for journeys](journey-known-issues.md#steps-to-avoid-journey-disruption) article before July 1, 2024.

> [!IMPORTANT]
> After July 30, 2024, custom workflows that *write* to the **msdynmkt_contactpointconsent2** or **msdynmkt_contactpointconsent3** consent tables will no longer automatically have data synced to the latest **msdynmkt_contactpointconsent4** table. To ensure continued functionality of custom workflows, update the workflows to write to the **msdynmkt_contactpointconsent4** table *before* July 30.

> [!NOTE]
> Double opt-in for real-time journeys is not included in the June release. It's projected to roll out in a future release, likely in late July.

### General availability

- **Easily manage customer consent from contact and lead forms**
    - Enhanced contact and lead forms allow you to quickly see and update customer consent, helping you effortlessly manage what types of messages are sent to your customers. This comprehensive view gives you one place to manage consent across every channel and line of business for your organization. Quickly see if a customer has opted out of all commercial communication from your business. Explore which topics a contact has opted into or out of receiving across all channels: email, text, and custom channels. Get a complete understanding of each contact and lead's consent preferences in one easy-to-use screen.
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/easily-manage-customer-consent-contact-lead-forms)
    - [Docs](real-time-marketing-email-text-consent.md#view-and-manage-consent-records)

### Monthly enhancements

- **Pre-set country code for your phone number form fields**
    - Simplify the experience of entering the phone number into form by pre-setting the right country code. Once the code is pre-set, form submissions will no longer fail if wrong phone number format was entered.
    - [Docs](real-time-marketing-manage-forms.md#pre-set-phone-number-country-code)

### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Announcing unlimited application installs in Dynamics 365 Customer Insights - Microsoft Dynamics 365 blog](https://www.microsoft.com/dynamics-365/blog/it-professional/2024/06/18/announcing-unlimited-application-installs-in-dynamics-365-customer-insights/)

## May 2024 update

### Version number

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        |   1.1.41881.62    |

> [!NOTE]
> On July 1, 2024, active journeys in the real-time journeys area that were created on or before May 5, 2022 will stop working. To avoid disruption, follow the steps outlined in the [Known issues for journeys](journey-known-issues.md#steps-to-avoid-journey-disruption) article before July 1, 2024.

### General availability

- **Ensure messages go to the right contact email address**
    - It's critical that your messages are delivered by the right channel at the right time. Often, you'll need to pick the correct email address among the several you may have for a contact. Now you can choose which of a contact’s email addresses to target in your journeys. For example, some email messages may be more appropriate for a contact’s work email address, whereas others may best target a personal email address. Now, you have full control over which email address to send email messages to, enabling you to reach your customers where they’re most likely to see your messages and take action.
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/ensure-messages-go-right-contact-email-address)
    - [Docs](real-time-marketing-audience-data.md#change-your-audience-configuration)

### Monthly enhancements

- **Real-time journey segment membership**
    - Fixed an issue that causes inflated segment membership for some segments that use three or more entities and have repeating data in the columns.
This fix makes the membership data for those segments accurate, thus showing a lower count than before.
- **Real-time journeys now respect daylight savings time**
    - Recurring journeys that are scheduled to run repeatedly at a future date and time now adjust their schedules so that they are run at the expected time. For example, if you have a daily journey that runs at 9:00 AM in the Pacific Time Zone, that journey will continue to run at 9:00 AM after the next daylight savings time change. Before this fix, the journey would have run at 8:00 AM (or 10:00 AM), depending on the direction of the daylight savings time change.

### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Revolutionizing marketing workflows with Copilot in Dynamics 365 Customer Insights - Microsoft Dynamics 365 blog](https://cloudblogs.microsoft.com/dynamics365/bdm/2024/04/02/revolutionizing-marketing-workflows-with-copilot-in-dynamics-365-customer-insights/)

## April 2024 update

### Version number

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        |   1.1.40197.68    |

> [!NOTE]
> On July 1, 2024, active journeys in the real-time journeys area that were created on or before May 5, 2022 will stop working. To avoid disruption, follow the steps outlined in the [Known issues for journeys](journey-known-issues.md#steps-to-avoid-journey-disruption) article before July 1, 2024.

### General availability

- **Easily reference copies of sent emails in the timeline**
    - Understanding your company's customer interactions is key to improving your customer experience. Now you can deepen customer understanding by viewing exact copies of sent emails, allowing you to build more personalized experiences. Reviewing sent emails improves your overall visibility, compliance, and auditing.
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/easily-reference-copies-sent-emails-timeline)
    - [Docs](view-previously-sent-emails.md)

- **Capture responses from external, third-party forms**
    - Maximize the potential of your external custom-built forms and generate more leads and contacts for your business without the need to recreate them in real-time journeys. Capture submissions from any third-party form on your website and automatically create new leads or contacts in real-time journeys. This empowers you to better understand your audience, target them more accurately, and follow up effectively.
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/capture-responses-external-third-party-forms)
    - [Docs](real-time-marketing-form-capture.md)

### Public preview

- **Take campaigns from concept to launch using Copilot**
    - Defining campaigns and creating high-performing assets to achieve campaign goals can be a time-consuming and difficult task. Now, Copilot transforms the way you create campaigns, enhancing your productivity. To create a campaign, describe the outcomes you're looking to drive or provide a creative brief. Copilot leverages the power of data and AI to generate audiences, content, images, journeys, and more, allowing you to curate, edit, and launch your project in record time. You'll save countless hours by using Copilot to create a connected solution that you can update to achieve the goals that you've defined. Rest assured that you'll always be in the loop to refine, approve, and complete the campaign before it goes out to your customers.
    > [!NOTE]
    > The public preview is rolling out in phases, starting with selected customers who signed up previously. Sign up [here](https://adoption.microsoft.com/dynamics-365/customer-insights/) to get access as the preview program is expanded.
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/take-campaigns-concept-launch-using-copilot)

- **Improve reliability of insights with advanced bot protection**
    - In today’s world, ensuring the integrity of your data and the efficiency of your operations is paramount. Advanced bot protection in Customer Insights - Journeys empowers your business to thrive by safeguarding your business processes. Improve your business decisions with the confidence of knowing that the data you collect is accurate and represents real human interactions. With bot protection, you not only enhance the quality of your insights but also elevate the customer experience by minimizing disruptions caused by malicious bots.
    - [Release plan](/dynamics365/release-plan/2024wave1/customer-insights/dynamics365-customer-insights-journeys/improve-reliability-insights-advanced-bot-protection)
    - [Docs](bot-protection.md)

### Monthly enhancements

- **Email editor**
    - Email spam score is now available in real-time journeys, even when outbound marketing isn’t present (real-time journeys-only environments). Previously, spam score in real-time journeys was only available in mixed configurations (outbound marketing + real-time journeys).

### New blogs and scenario docs

Learn how to make the most of the new Dynamics 365 Customer Insights features in our latest blogs and scenario docs:

- [Revolutionizing marketing workflows with Copilot in Dynamics 365 Customer Insights - Microsoft Dynamics 365 blog](https://cloudblogs.microsoft.com/dynamics365/bdm/2024/04/02/revolutionizing-marketing-workflows-with-copilot-in-dynamics-365-customer-insights/)
- [Journey and email approval process in Customer Insights - Journeys (FastTrack blog)](https://community.dynamics.com/blogs/post/?postid=e2f9169d-eef7-ee11-a73d-000d3ae2664e)

## March 2024 update

### Version number

| App              | GA release      |
|------------------|-----------------|
| Customer Insights - Journeys        |   1.1.38813.71    |

> [!IMPORTANT]
> Starting on April 15, 2024, changes to link functionality will affect the following areas:
>
> - **Link tracking**: Links in messages that were sent more than one year prior will no longer produce tracking results, but will otherwise function correctly. Links in messages sent less than one year prior will continue to generate tracking analytics.
> - **Text messages**: URLs sent in SMS messages will expire one year after the message is sent and will no longer work.
> - **Unsubscribe links**: Unsubscribe links will expire one year after the link is created and will no longer work.

> [!NOTE]
> On July 1, 2024, active journeys in the real-time journeys area that were created on or before May 5, 2022 will stop working. To avoid disruption, follow the steps outlined in the [Known issues for journeys](journey-known-issues.md#steps-to-avoid-journey-disruption) article before July 1, 2024.

### Public preview

- **Receive in-app task assistance from Copilot**
    - Use Copilot to receive timely in-app guidance in everyday language. You can also ask questions, which Copilot answers with reference to the Dynamics 365 Customer Insights - Journeys documentation.
    - [Release plan](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/receive-in-app-task-assistance-copilot)
    - [Docs](faqs-copilot-general.md)

- **Easily manage customer consent from contact and lead forms**
    - Enhanced contact and lead forms enable you to quickly see and update a customer's consent, helping you effortlessly manage which types of messages are sent to your customers. This comprehensive view gives you a single place to manage consent across every channel and line of business for your organization. See if a customer has opted out of all commercial communication from your business. Explore which topics a contact has opted in or out of receiving across all channels: email, text, and custom channels. Get a complete understanding of each contact and lead's consent preferences in one easy-to-use screen.
    - [Release plan](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/easily-manage-customer-consent-contact-lead-forms)
    - [Docs](real-time-marketing-email-text-consent.md#view-and-manage-consent-records)

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
