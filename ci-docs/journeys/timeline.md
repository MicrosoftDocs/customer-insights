---
title: Customer interactions timeline
description: View historical customer interactions in Dynamics 365 Customer Insights - Journeys. Learn how to configure the timeline for a unified view of activities.
ms.date: 04/23/2025
ms.topic: article
author: alfergus
ms.author: colinbirkett
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:02/20/2025
---

# Customer interactions timeline

The interactions timeline for a contact or lead provides a unified view of historical interactions based on customer activities in Dynamics 365 Customer Insights - Journeys, Sales, and Customer Service.

You can also view Customer Insights activities in the timeline. For more information, see [Integrate Customer Insights activities with Dynamics 365 timelines](/dynamics365/customer-insights/activities-in-d365-timeline).

> [!TIP]
> To learn how to configure the timeline and view interactions across Dynamics 365 Sales and Customer Service, see [Use timeline](/power-apps/user/add-activities) in Power Apps.

Having a single view of all the activities that a customer engages in lets you get a complete understanding of your customer. Business stakeholders such as marketers, sales agents, customer service agents, account managers, and more can use the unified view of customers' historical interactions with the business to create personalized experiences through both digital and non-digital channels. For instance, a sales agent could learn about the newsletters that a contact has subscribed to in previous marketing campaigns and the product pages and blogs recently explored by the contact. The sales agent can then personalize communication with them in the next sales call. Similarly, a service agent could investigate the latest email communications received by a customer as part of a customer journey to help with an escalation scenario.

## How to enable marketing interactions in your contact or lead timeline

If you use the out-of-the-box contact and lead forms provided with Customer Insights - Journeys, marketing interactions automatically show up in the timeline. The timeline only displays interactions associated with the respective profile type (either contact or lead). For example, the timeline for a contact includes interactions for that contact only.

However, if you use custom forms for contacts and leads, you need to add a custom connector to the timeline component in your custom contact or lead form to see the marketing interactions.

To add the custom connector to your timeline component through the [Power Apps maker experience](https://make.powerapps.com/), do the following steps: 

1. Within the Power Apps maker experience, select **Tables**. 
1. Open the table you want (for example, Contact), and then select the **Forms** area.
1. Open your custom contact or lead form and select the timeline component in the form.
1. To add a new custom connector, in the **Properties** pane for the timeline component, go to **Custom connectors** and select **Add connector**.
    
    > [!div class="mx-imgBorder"]
    > ![Add a connector.](media/real-time-marketing-add-custom-connector.png "Add a connector")

1. The **New custom connector** pane is displayed. Add the following details and select **Save**:
    - **Constructor**: `msdynmkt_DynamicsMktTimelineInteractionAnalytics.TimelineInteractionAnalyticsResource`
    - **Resource path**: `msdynmkt_DynamicsMktTimelineInteractionAnalytics`

    > [!div class="mx-imgBorder"]
    > ![Custom connector details.](media/real-time-marketing-connector-details.png "Custom connector details")

1. The custom connector is now added to the timeline component. Select **Save** and then **Publish** to publish your custom contact or lead form. The timeline in your custom contact or lead form now shows the marketing interactions.

For more information, see [Use custom connectors with the timeline control](/power-apps/maker/model-driven-apps/custom-connectors-timeline-control).

## Key capabilities of the timeline

> [!div class="mx-imgBorder"]
> ![Screenshot of new timeline view.](media/whats-new-timelineview.png "Screenshot of new timeline view")

- Along with activities from Dynamics 365 Sales and Customer Service, you can view interactions based on activities from both Customer Insights - Journeys and outbound marketing. This includes interactions across the following marketing activities:
    - Emails
    - Text messages
    - Push notifications
    - Web activity
    - Forms
    - Events
- Use filtering to focus on specific types of marketing interactions like all emails that were opened by a contact.
- Preview the communications (such as emails, text messages, and push notifications) that a contact received or interacted with as part of your marketing campaigns within the timeline.

> [!IMPORTANT]
> To see marketing interactions on the timeline, enable the following read permissions:
>
> -	msdyncrm_marketingemail
> -	msevtmgt_event
> -	msdyncrm_marketingform
> -	msdynmkt_marketingform
> -	msdyncrm_website
> -	msdynmkt_email
> -	msdynmkt_pushnotification
> -	msdynmkt_sms

> [!NOTE]
> - Real-time marketing activities from the past 12 months are shown in the timeline for the selected contact or lead.
> - The Timeline doesn't display interactions for customer profiles.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
