---
title: Transition insights and reports
description: Learn how to transition insights and reporting capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 04/23/2025
ms.topic: article
author: alfergus
ms.author: colinbirkett
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition insights and reports

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. For more information, see [Transition overview](transition-overview.md)

## Comparison of outbound marketing and real-time journeys insights and reports

Outbound marketing and real-time journeys both have in-app reporting capabilities, including KPIs for email sending at a contact, email, or journey level. Real-time journeys additionally provides an aggregate set of dashboards for journey and channel analytics, as well as individual SMS, push notification, custom channel, and form insights. You can find more information about Real-time journeys analytics capabilities in the [Analytics overview](analytics-overview.md) and in [Access and interpret analytics](real-time-marketing-analytics.md).

Additionally, advanced bot protection for real-time journeys safeguards your business processes, ensuring that the data you collect is accurate and represents real human interactions. For more information, see [Improve reliability of insights with advanced bot protection](bot-protection.md).

## How to transition

For out-of-the-box insights, we’re automatically migrating outbound marketing interactions to real-time journeys storage and updating the outbound insights to align with real-time journeys widgets. As a result, and to comply with the [real-time journeys retention policy](real-time-marketing-analytics.md#email-insights), you’ll only be able to display outbound marketing interactions for the last 12 months in the out-of-the-box insights. Past data is still available in data storage.

> [!NOTE]
> If you’re a customer in the EU, NAM, OCE, or GBR region, only interactions created after January 1, 2024, are migrated by default. You can request additional data to be transferred by filling in [this form](https://go.microsoft.com/fwlink/?linkid=2313103).

## Email insights

When you import outbound emails to real-time journeys, you can't view past outbound marketing email data in the real-time journeys email insights after the migration date. Outbound marketing emails are recreated in real-time journeys and retain their data history separately. However, historical outbound marketing data remains in Customer Insights - Journeys storage.

## Custom reporting

Sometimes users need to consume marketing interaction data outside of the in-app experiences. This could mean creating reports or integration with other systems. Outbound marketing provides a mechanism to export this data to an Azure Blob storage and sample Power BI reports. This allows users to also build their own custom reports or integration pipelines.

For custom reporting in real-time journeys, you can create custom Power BI reports tailored to your business needs without data movement. Or you can export your data using Microsoft Fabric capabilities. For more information, see [Build custom reports using Microsoft Fabric integration](fabric-integration.md).

With this capability, you have even more options to consume data with more data sources in your reports. Real-time journeys storage contains real-time journeys as well as outbound marketing interaction data. While the data models are the same between outbound marketing and real-time journeys, you must reconfigure existing custom reports and pipelines to use the new data sources in Microsoft Fabric. Here's the data schema: [Overview of Customer Insights - Journeys interaction data schema](/common-data-model/schema/core/applicationcommon/foundationcommon/crmcommon/solutions/customerinsightsjourneys/overview). The *SourceSystem* attribute refers to the source system (outbound marketing or real-time journeys) that generated the interaction.

[!INCLUDE [transition-comments](./includes/transition-comments.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
