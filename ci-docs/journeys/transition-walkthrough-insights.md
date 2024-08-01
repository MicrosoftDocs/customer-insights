---
title: Transition insights and reports
description: Learn how to transition insights and reporting capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 11/16/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition insights and reports

Marketing analytics reports are a critical component of success campaigns. Among other things, reports determine:
-	How many emails have bounced, delivered, or opened?
-	Which contacts went to which path in a journey?
-	How many leads have been generated?
-	How many journeys ran last month?

Outbound marketing and real-time journeys have equivalent in-app reporting capabilities. Both modules report on KPIs for email sending at a contact, email, or journey level. Additionally, real-time journeys provides an aggregate set of dashboards for journey and channel analytics. Real-time journeys also includes a marketing effectiveness dashboard, which provides valuable information about different marketing assets and their campaign impact.

:::image type="content" source="media/real-time-marketing-effectiveness-analytics-dashboard.png" alt-text="Customer Insights - Journeys effectiveness analytics dashboard." lightbox="media/real-time-marketing-effectiveness-analytics-dashboard.png":::

Sometimes it's required to consume marketing interaction data outside of the in-app experiences. This could mean the creation of reports or integration with other systems. Outbound marketing provides a mechanism to export this data to an Azure Blob storage and sample Power BI reports. This has allowed customers to also build their own custom reports or integration pipelines.

For custom reporting in real-time journeys, you can now effortlessly create custom Power BI reports tailored to your business needs or export your data using Microsoft Fabric capabilities. Learn more: [Build custom reports using Microsoft Fabric integration](/dynamics365/customer-insights/journeys/fabric-integration). With this capability, you have even more options to consume data with more data sources in your own reports. While the data models are the same between outbound marketing and real-time journeys, existing custom reports and pipelines need to be reconfigured to use the new data sources in Microsoft Fabric.

Last but not least, real-time journeys' advanced bot protection empowers your business to thrive by safeguarding your business processes. Improve your business decisions with the confidence of knowing that the data you collect is accurate and represents real human interactions. Learn more: [Improve reliability of insights with advanced bot protection](/dynamics365/customer-insights/journeys/bot-protection).

> [!TIP]
> If you have questions or comments, visit the [Outbound to real-time transition community forum](https://community.dynamics.com/forums/thread/?partialUrl=Outbound-to-Real-Time-Transition)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
