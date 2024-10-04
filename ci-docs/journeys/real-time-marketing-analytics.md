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

Journey operational analytics allows you to monitor and understand journey execution. Operational analytics is different from reporting. With operational analytics, we prioritize speed that can sometimes lead to data getting processed out of sequence, and this can result in numbers that may not add up. However, numbers total once journey execution is complete and all of the data has been processed. 

Operational analytics provides these capabilities:
- Export lists of customers who exited a step in the journey (up to 50,000 records).
- Understand why the number of customers in your starting segment is different than the number of customers who reached the first step in your journey. 
- Understand why and where customers exited your journey before completing each step in the journey flow.
- Understand why customers triggered to start your journey didn’t reach the first step in your journey.

Operational analytics has two parts:

- **The Sankey view**: Numbers on the journey paths indicate how many customers went through the path. The widths of the connecting lines are in relative proportions and helps you understand the user flow through the journey, highlighting which branches are working well. For example, see the image below: 
 
- **Step analytics**: When you select any step in the journey, the right pane shows much information. There are three areas/groups:

    - **Inflow and outflow information**: For every step, the top shows the number of customers who entered the step (Inflow), the number currently being processed (Processing), the number who have moved to the next step (Processed), and the number who have exited the journey (Exit). The percentage is calculated from the inflow volume. When the journey is running and counts are small, we prioritize showing these numbers as soon as possible (within minutes) and this can lead to inconsistencies (for example, a processed data point may be counted and shown before its corresponding inflow data point is shown). This will self-correct once journey execution is complete.

    - **Flow details**: The flow details section shows additional details such as rate limits (if applied), unique people who entered the journey (different than Inflow which counts each entry rather than unique person), and exit reasons. You can click on the export button to get a detailed view of the individual customers and export this data to Excel (with a limit of 50,000).

    - **Goal analytics**: If a goal has been defined as a target set, you can view how the journey is progressing toward its goal and if it has met the goal.

## Email insights

Email insights provide a deep dive into how your audience interacts with your emails over time.

Learn more: [Email insights](email-insights.md)

:::image type="content" source="media/analytics-email-insights.png" alt-text="Screenshot of email insights dashboard." lightbox="media/analytics-email-insights.png":::

> [!NOTE]
> Contact insights, lead insights, journey and channel analytics (including, goal analytics, AI optimization, email insights and delivery and interaction details) will display interaction data for the last 12 months only. However, all historical interaction data is still retained in the data storage.

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
