---
title: Transition insights and reports
description: Learn how to transition insights and reporting capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/03/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition insights and reports

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Marketing analytics reports are a critical component of success campaigns. Among other things, reports determine:
-	How many emails have bounced, delivered, or opened?
-	Which contacts went to which path in a journey?
-	How many leads have been generated?
-	How many journeys ran last month?

Outbound marketing and real-time journeys have equivalent in-app reporting capabilities. Both modules report on KPIs for email sending at a contact, email, or journey level. Additionally, real-time journeys provides an aggregate set of dashboards for journey and channel analytics, as well as individual SMS, push notification, custom channel, and form insights. Real-time journeys also includes a marketing effectiveness dashboard, which provides valuable information about different marketing assets and their campaign impact. Learn more: [Access and interpret analytics](real-time-marketing-analytics.md).

> [!NOTE]
> If you're migrating your outbound marketing emails to real-time journeys, you won't be able to view past outbound marketing email data after the migration date in the real-time journeys email insights. Outbound marketing emails are recreated as new ones in real-time journeys and retain their data history separately. However, all historical outbound marketing data remains in the Customer Insights - Journeys storage and is accessible through Microsoft Fabric.

:::image type="content" source="media/real-time-marketing-effectiveness-analytics-dashboard.png" alt-text="Customer Insights - Journeys effectiveness analytics dashboard." lightbox="media/real-time-marketing-effectiveness-analytics-dashboard.png":::

Sometimes users need to consume marketing interaction data outside of the in-app experiences. This could mean the creation of reports or integration with other systems. Outbound marketing provides a mechanism to export this data to an Azure Blob storage and sample Power BI reports. This allows customers to also build their own custom reports or integration pipelines.

For custom reporting in real-time journeys, you can now effortlessly create custom Power BI reports tailored to your business needs without data movement, or export your data using Microsoft Fabric capabilities. Learn more: [Build custom reports using Microsoft Fabric integration](fabric-integration.md). With this capability, you have even more options to consume data with more data sources in your reports. Real-time journeys storage contains real-time journeys as well as outbound marketing interaction data. While the data models are the same between outbound marketing and real-time journeys, existing custom reports and pipelines must be reconfigured to use the new data sources in Microsoft Fabric.

Additionally, advanced bot protection for real-time journeys empowers your business to thrive by safeguarding your business processes. Improve your business decisions with the confidence of knowing that the data you collect is accurate and represents real human interactions. Learn more: [Improve reliability of insights with advanced bot protection](/dynamics365/customer-insights/journeys/bot-protection).

[!INCLUDE [transition-comments](./includes/transition-comments.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
