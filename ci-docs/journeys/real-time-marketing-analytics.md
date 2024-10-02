---
title: Access and interpret analytics
description: How to access and interpret Customer Insights - Journeys analytics in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/01/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Access and interpret analytics

Customer Insights - Journeys's dashboards and cross-journey insights show metrics, views, and insights summarized across single or multiple journeys, providing a deep understanding of journey, channel, and content performance. The built-in dashboards focus on measuring delivery, engagement, and journey goal attainment so that you can fine-tune the effectiveness of your journeys, channels, and content.

## Customer Insights - Journeys analytics overview

With Customer Insights - Journeys analytics, you can:

- Evaluate the effectiveness of journeys against your objectives.
- Troubleshoot journeys by identifying areas of friction.
- Discover what is working so that you can amplify or recreate the same approach elsewhere.
- Understand the effectiveness of various messages and channels of communication through key delivery and engagement insights.
- Gain insights into your audience's behavior and interests and tailor your marketing efforts to their specific needs. 

## Contact insights

Contact insights is a comprehensive view of how a contact has engaged with your journeys, including all past email sends, opens, clicks, form submissions, and more. Better understand your audience's behavior and interests, make informed decisions based on past engagement, and tailor your marketing efforts to their needs and preferences. To view contact insights, go to **Real-time journeys** > **Audience** > **Contacts**, select a contact record, and then open its **Insights** tab.

The following insights categories are provided:

- **Overview**: A chart of the engagement interactions and a summary of the most important KPIs for each channel for the selected contact.
- **Email insights**: Complete details of email interactions for the selected contact, including a list of all messages sent to them, plus lists of all opens, clicks, bounces, and more. View the email clients used to open emails and the device types, operating systems, and browsers used to click on emails.
- **Form insights**: See which marketing forms the contact has visited and submitted. View the content of each submission.
- **Text message insights**: Complete details of text message interactions for the selected contact, including a list of all messages sent to them, plus lists of all clicks, replies, and more.
- **Push notification insights**: Complete details of push notification interactions for the selected contact, including a list of all messages sent to them and more.
- **Custom channels insights**: Complete details of custom channel interactions for the selected contact, including messages sent, clicked and more.

    :::image type="content" source="media/real-time-marketing-custom-channel-contact-insights.png" alt-text="Screenshot of custom channel contact insights." lightbox="media/real-time-marketing-custom-channel-contact-insights.png":::

## Lead insights

Just like with contact insights, you can access a complete overview of your selected lead's interactions with your marketing initiatives. The insights categories displayed for a lead are the same as previously described in contact insights. To view lead insights, go to **Real-time journeys** > **Audience** > **Leads**, select a lead record, and then open its **Insights** tab.

## Journey operational analytics

Evaluate journey performance in near real-time using built-in operational analytics. The Sankey view in the designer helps you understand the user flow through the journey, highlighting which branches are working well.

Select any journey component to view near real-time operational analytics in the right pane, including:

- **Goal analytics**: If a goal has been defined as a target set, you can view how the journey is progressing toward its goal and if it has met the goal.

    :::image type="content" source="media/real-time-marketing-goal-analytics.png" alt-text="Goal analytics screenshot." lightbox="media/real-time-marketing-goal-analytics.png":::

- **Channel analytics**: For any message in the journey (email, text, or push notification), view the delivery funnel and additional metrics to diagnose the content performance.

    :::image type="content" source="media/analytics-channel-side-pane.png" alt-text="Email channel analytics screenshot." lightbox="media/analytics-channel-side-pane.png":::

    In the Overview section, you can monitor key performance indicators per channel message such as:
    - **Delivery rate**: The percentage of email, text, or custom channel messages delivered divided by the number of email, text, or custom channel messages sent.
    - **Open rate**: The percentage of unique email or push notification opens divided by the number of emails or push notifications delivered.
    - **Click rate**: The percentage of unique email, text, or push notification/custom channel clicks divided by the number of email, text, or push notification/custom channel links delivered.
    - **Response rate**: The percentage of unique text message responses divided by the number of text messages sent.
  
    To view **delivery and interaction statistics**, select the **View details** link in the **Delivery funnel** or **Delivery issues** section on the channel analytics pane. Delivery and interaction details allow you to analyze delivery, engagement, and performance data for your email, text, push notification, or custom channel messages. Timestamps are reported according to the organization's time zone. In this area, you can:

    - View deliverability details on messages sent, delivered, blocked, or bounced along with the respective reasons, detailed data on customers who opened or clicked a message, as well as unsubscription interaction data. A message’s unique opens and clicks are calculated based on the customer's journey run. This means that if the same customer enters the same journey multiple times and opens or clicks the same message each time, the system records multiple unique opens or clicks. For example, if a customer clicks the same message in two different journey executions, two unique clicks are recorded. 
    - For emails, delivery and interactions statistics include data on user agents your customers are using to engage with your emails. Under total opens you can see data about email clients and under total clicks you can find data on types of devices, operating systems, and browsers.
    - Use the search option in the top right to search for interactions by email address.
    - Access links to audience profiles that interacted with your messages. 
    - Export up to 50,000 records by selecting the export icon under the search bar.

    :::image type="content" source="media/analytics-delivery-and-interaction-details.png" alt-text="Screenshot of delivery and interaction details." lightbox="media/analytics-delivery-and-interaction-details.png":::
  
- **AI optimization**: Near real-time data to help you evaluate how applying AI optimization has helped your engagement rate.

    :::image type="content" source="media/real-time-marketing-ai-optimization.png" alt-text="AI optimization screenshot." lightbox="media/real-time-marketing-ai-optimization.png":::

## Email insights

Email insights provide a deep dive into how your audience interacts with your emails over time.

Learn more: [Email insights](email-insights.md)

:::image type="content" source="media/analytics-email-insights.png" alt-text="Screenshot of email insights dashboard." lightbox="media/analytics-email-insights.png":::

## Aggregate cross-journey analytics

The built-in aggregate cross-journey analytics dashboard shows relevant metrics and insights for all your journey orchestrations in one place.

:::image type="content" source="media/real-time-marketing-aggregate-analytics.png" alt-text="Aggregate cross-journey analytics dashboard." lightbox="media/real-time-marketing-aggregate-analytics.png":::

Use the aggregate cross-journey analytics dashboard to review recent journey effectiveness and quickly share reports with stakeholders.

Learn more: [How to use aggregate cross-journey analytics](real-time-marketing-cross-journey-analytics.md).

## Aggregate channel analytics

The aggregate channel analytics dashboard shows metrics and insights related to delivery and engagement.

:::image type="content" source="media/real-time-marketing-aggregate-channel-analytics.png" alt-text="Aggregate channel analytics dashboard." lightbox="media/real-time-marketing-aggregate-channel-analytics.png":::

Use the aggregate channel analytics dashboard to measure campaign effectiveness and track the performance of your marketing assets.

Learn more: [How to use aggregate channel analytics](real-time-marketing-channel-analytics.md).

> [!NOTE]
> There is no data retention policy for Customer Insights - Journeys interactions in aggregate cross-journey analytics and aggregate channel analytics. Dataverse entities are limited to a two-year retention policy after their initial creation date. Keep in mind that the two-year Dataverse entity retention policy might impact analytics views associated with interaction data from Dataverse entities.
> The aggregate cross-journey analytics, channel analytics, and marketing effectiveness analytics dashboards are not supported on mobile devices.

## Marketing effectiveness analytics

The marketing effectiveness analytics dashboard enables you to set up key milestones in your buyer’s journey and analyze how your Customer Insights - Journeys activities are contributing to driving customers to those milestones. The dashboard uses AI-powered multi-touch and single-touch attribution models.

:::image type="content" source="media/real-time-marketing-effectiveness-analytics-dashboard.png" alt-text="Customer Insights - Journeys effectiveness analytics dashboard." lightbox="media/real-time-marketing-effectiveness-analytics-dashboard.png":::

Learn more: [Preview: Marketing effectiveness analytics](real-time-marketing-effectiveness.md)

## Learn more

Here are some advanced resources for this topic:

- [Custom reporting with Microsoft Fabric](fabric-integration.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
