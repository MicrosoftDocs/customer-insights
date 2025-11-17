---
title: Access and interpret analytics
description: How to access and interpret Customer Insights - Journeys analytics in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/31/2025
ms.topic: article
author: colinbirkett
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: sfi-image-nochange
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
- **Push notification insights**: Complete details of push notification interactions for the selected contact, including a list of all messages sent to them and more.
- **Text message insights**: Complete details of text message interactions for the selected contact, including a list of all messages sent to them, plus lists of all clicks, replies, and more.
- **Custom channels insights**: Complete details of custom channel interactions for the selected contact, including messages sent, clicked, and more.
- **Website and form insights**: Monitor web behavior and see which marketing forms the contact has visited and submitted. View the content of each submission.

    :::image type="content" source="media/real-time-marketing-custom-channel-contact-insights.png" alt-text="Screenshot of custom channel contact insights." lightbox="media/real-time-marketing-custom-channel-contact-insights.png":::

## Lead insights

Just like with contact insights, you can access a complete overview of your selected lead's interactions with your marketing initiatives. The insights categories displayed for a lead are the same as previously described in contact insights. To view lead insights, go to **Real-time journeys** > **Audience** > **Leads**, select a lead record, and then open its **Insights** tab.

## Journey operational analytics

Journey operational analytics allows you to monitor and understand journey execution. Operational analytics is different from reporting. With operational analytics, speed is prioritized to help with monitoring, which can sometimes lead to data getting processed out of sequence, resulting in numbers that may not add up. However, numbers totalize once journey execution is complete and all data has been processed.

Operational analytics provides these capabilities:

- Export lists of customers who exited a step in the journey (up to 50,000 records).
- Understand why the number of customers in your starting segment is different than the number of customers who reached the first step in your journey. 
- Understand why and where customers exited your journey before completing each step in the journey flow.
- Understand why customers triggered to start your journey didn’t reach the first step in your journey.

Operational analytics has two parts:

- **The Sankey view**: Numbers on journey paths indicate how many customers went through that path. The widths of the connecting lines are in relative proportions to help you understand user flow through the journey, highlighting which branches are working well. An example is shown below (notice different widths and numbers on journey paths):

    :::image type="content" source="media/sankey_view.png" alt-text="Snapshot of the Sankey view within Customer Insights - Journeys." lightbox="media/sankey_view.png":::
 
- **Step analytics**: When you select any step in the journey, the right pane shows a wealth of information. There are three areas or groups:

- **Inflow and outflow information**: For every step, the top shows the number of customers who entered the step (Inflow), the number currently being processed (Processing), the number who have moved to the next step (Processed), and the number who have exited the journey (Exit). The percentage is calculated from the inflow volume. When the journey is running and counts are small, we prioritize showing these numbers as soon as possible (within minutes), and this can lead to inconsistencies (for example, a processed data point may be counted and shown before its corresponding inflow data point is shown). This self-corrects once the journey execution is complete.

    - **Flow details**: The flow details section shows additional details such as rate limits (if applied), unique people who entered the journey (different than inflow, that counts each entry rather than unique people, flow details are only available for channel tiles), and exit reasons. You can select the list icon to display the individuals in the step and reason codes for their status. You can also select the export button to export the data to Excel (with a limit of 50,000 records).

        :::image type="content" source="media/operational-analytics-2.png" alt-text="An overview of customer inflow, processed, and exit analytics with email performance metrics." lightbox="media/operational-analytics-2.png":::

    - **Goal analytics**: If a goal has been defined as a target set, you can view how the journey is progressing toward its goal and if it has met the goal.

### Channel analytics

In addition to journey-level analytics, for every message within a journey (email, text message, push notification, or custom channel), you can view detailed delivery funnel insights and performance metrics to assess the content's effectiveness. You can access channel-specific analytics by selecting the individual message tile within the journey, or by navigating to the message details page for each channel.

In the **Overview** section of the right pane, you can monitor key performance indicators (KPIs) per channel message such as:

- **Delivery rate**: The percentage of email, text, or custom channel messages delivered divided by the number of email, text, or custom channel messages sent.
- **Open rate**: The percentage of unique email or push notification opens divided by the number of emails or push notifications delivered.
- **Click rate**: The percentage of unique email, text, or push notification/custom channel clicks divided by the number of email, text, or push notification/custom channel links delivered.
- **Response rate**: The percentage of unique text message responses divided by the number of text messages sent. This KPI applies to text messages only.

To view **delivery and interaction statistics**, select the **View details** link in the **Delivery funnel** or **Delivery issues** section on the channel analytics pane. Delivery and interaction details allow you to analyze delivery, engagement, and performance data for your email, text, push notification, or custom channel messages.

- You can view deliverability details on messages sent, delivered, blocked, or bounced along with the respective reasons, detailed data on customers who opened or clicked a message, and unsubscription interaction data.
- For emails, delivery and interactions statistics include data on user agents your customers are using to engage with your emails. Under total opens, you can see data about email clients, and under total clicks, you can find data on types of devices, operating systems, and browsers.

A message’s unique opens and clicks are calculated based on the customer's journey run, not against the journey itself. In the case of a repeating journey, if the same customer enters the journey multiple times as it repeats and opens or clicks the same message each time, the system records multiple unique opens or clicks for each journey run. For example, if a customer clicks the same message in the same journey in two different runs, two unique clicks are recorded. 

You can export up to 10,000 interaction data records and up to 100 conditional content variation records. You can search through the data using a profile's email address and access links to audience profiles that interacted with your email messages. Exports are limited to 10,000 records due to browser cache limitations. Exporting more than 10,000 records can create confusion because records can display on more than one page and be exported more than once, causing the export to be larger than the display counts. Timestamps are reported according to the organization's time zone.

:::image type="content" source="media/analytics-delivery-and-interaction-details.png" alt-text="Screenshot of delivery and interaction details." lightbox="media/analytics-delivery-and-interaction-details.png":::

### Conversational voice

Voice calls are dependent on Contact Center making the call and sending the outcomes back to Customer Insights - Journeys. Voice conversations show the following insights:
- **Sent** This shows you how many voice conversation requests have been sent from Customer Insight - Journeys to Contact Center.
- **Blocked** This shows you how many voice conversations were blocked by Customer Insights - Journey, with the reason.
- **Call attempted** This shows how many calls have been attempted by Contact Center and what the outcomes were. A call attempt doesn't necessarily mean that your customer answered the call. For example, if your customer declined answering the call, this is still a call attempted. The call attempted interaction shows you the outcome of the call.
- **Call not attempted** This shows you how many calls were not attempted by Contact Center, with the reason.

### AI optimization

View near real-time data to help you evaluate how applying AI optimization improved your engagement rate.

:::image type="content" source="media/real-time-marketing-ai-optimization.png" alt-text="AI optimization screenshot." lightbox="media/real-time-marketing-ai-optimization.png":::

## Email insights

Email insights provide a deep dive into how your audience interacts with your emails over time.

Learn more: [Email insights](email-insights.md)

:::image type="content" source="media/analytics-email-insights.png" alt-text="Screenshot of email insights dashboard." lightbox="media/analytics-email-insights.png":::

> [!NOTE]
> Contact insights, lead insights, journey and channel analytics (including goal analytics, AI optimization, email insights, and delivery and interaction details) will display interaction data for the last 12 months only. However, all historical interaction data is still retained in the data storage.

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

## Learn more

Here are some advanced resources for this topic:

- [Custom reporting with Microsoft Fabric](fabric-integration.md)

## Related information

[Understand and Improve Your Marketing Journeys (video)](https://youtu.be/HtIvnS8IS9I)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
