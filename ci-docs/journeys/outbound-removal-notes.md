---
title: Notes about outbound marketing removal
description: Outbound marketing removal from Dynamics 365 Customer Insights – Journeys is complete. Learn how to access your old tables, data, and assets after the transition.
ms.date: 06/11/2026
ms.update-cycle: 180-days
ms.topic: concept-article
author: vinayd-msft
ms.author: alfergus
ms.reviewer: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:11/22/2024
---

# Notes about outbound marketing removal

Dynamics 365 Customer Insights – Journeys previously included an additional module called outbound marketing. This module was removed in May 2026.

This page contains some information that may be useful for customers who previously used this module.

## Accessing outbound marketing tables and data

If you previously used outbound marketing, you may still be able to access most of your tables and data created in outbound marketing. When outbound marketing was removed, the sitemap entry and outbound marketing services were removed. We did't remove any publicly documented outbound marketing tables or data in those tables, with some exceptions (see below). You can access these tables through the [Power Apps Maker portal](https://make.powerapps.com). While the tables and data remain in the system, they aren't being updated or refreshed, and some of them may not be usable or accessible from the user interface:

- **Asset library**: Common component; all items are available in real-time journeys.
- **Outbound marketing analytics data**: Merged with real-time journeys data.
    - Existing Power BI custom reports for outbound marketing don't work with the consolidated data because the data format, its location, and access methods are different in real-time journeys.
    - Insights reports that are part of the outbound marketing user interface aren't available anymore. If you want to rebuild those reports, see [Build custom reports using Microsoft Fabric integration](fabric-integration.md).
    - While the data models are the same between outbound marketing and real-time journeys, you must reconfigure existing custom reports and pipelines to use the new data sources in Microsoft Fabric. Here's the data schema: [Overview of Customer Insights - Journeys interaction data schema](/common-data-model/schema/core/applicationcommon/foundationcommon/crmcommon/solutions/customerinsightsjourneys/overview). The `SourceSystem` attribute refers to the source system (outbound marketing or real-time journeys) that generated the interaction.
    - You can also export your data using Microsoft Fabric capabilities and its native connectors. Alternatively, if you wish to use a third-party system to store and process Customer Insights - Journey data you can access and export interaction data into your own storage by following these steps:  [Leveraging Customer Insights - Journeys interaction data without Fabric](https://community.dynamics.com/blogs/post/?postid=75a63967-f115-f011-998a-7c1e525b5e9d).
- **Events**: Shared capability between real-time journeys and outbound marketing; the same tables are used. These tables and the data aren't removed.
    - There are some critical differences in the event forms and pages between outbound marketing and real-time journeys. Therefore, events created in outbound marketing aren't usable in real-time and must be recreated in real-time using the [user interface](set-up-event.md) or [API](./developer/using-rtm-event-api.md).
- **Outbound marketing segments**: Aren't removed, but aren't usable.
    - The segment table doesn't contain the actual list of members; this information was stored in an internal table that was removed. Segment queries are stored in the `msdyncrm_segment` table and remain available.
    - Outbound marketing segments may still be visible in real-time journeys. However, these segments aren't updated and shouldn't be used.
- **Marketing lists**: Not removed. You can keep using them in real-time journeys (you can include them in real-time journeys dynamic segments).
- Other outbound marketing assets such as **emails**, **content blocks**, **forms**, **marketing pages**, **consent data**, **journeys**, **templates**, **lead scoring models**, **social posts**, and **subscription lists** weren't removed.
    - These assets *can't be used* in real-time.
    - Any custom user interface that updated or added records to these assets and relied on outbound marketing services may fail (for example, any custom user interface that had plugins that reacted on retrieve/retrieve multiple messages).
- While the outbound marketing user interface isn't available in the sitemap, you can still access outbound marketing tables using the advanced search (or, in some cases, using the standard user interface such as in the contact timeline, which has links to outbound marketing messages). These tables, while available, may not work correctly and aren't supported.

## Past communications about outbound marketing removal

| Date       | Communication    |
|------------|--------------------------------------------------------------------------------------------------------------------|
| December 2022   | [Transition playbook](https://community.dynamics.com/blogs/post/?postid=1b4394d5-7764-4484-aba9-c7f972292c10) published.                                                                                  |
| July 2023 | Announced that outbound marketing isn't available to new customers, will receive no new features, and is being removed in the future: [Transition to real-time marketing and transform your customer experience](https://www.microsoft.com/dynamics-365/blog/it-professional/2023/07/18/transition-to-real-time-marketing-and-transform-your-customer-experience/). |
| October 2023   | Added [transition resources](transition-resources.md) and area-specific [transition guidance](transition-walkthrough-functional.md).                                 |
| January 2024   | Transition blog: [Transition to real time journeys – the time is now](https://www.microsoft.com/dynamics-365/blog/it-professional/2024/01/09/transition-to-real-time-journeys-the-time-is-now/).                                   |
| August 2024   | Announced that outbound marketing is being [removed after June 30, 2025](real-time-marketing-overview.md). In-product banner announcing outbound marketing removal added. Admin email and message in the message center. |
| March 2025   | Email and message center notification (MC1025068) to admins about product changes to support outbound marketing removal.          |
| June 2025 | Users creating new outbound marketing journeys, segments, or forms get a message dialog asking them to create these assets in real-time journeys instead of outbound marketing. |
| July 2025 | Email and message center notification (MC1119263) to admins about start of the [phased removal process](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working-updated-november-21-2025). |
| November 2025 | Email and message center notification (MC1189547) to admins about the start of the outbound marketing removal [phased removal process](transition-faqs.md#what-will-happen-after-june-30-2025-will-outbound-marketing-stop-working-updated-november-21-2025). |
| January 2026 | Email and message center notification (MC1214404) to admins about next phase of outbound marketing removal where live journeys, forms, events, and more will be stopped. |

## Outbound marketing documentation

As outbound marketing has reached its end of life, documentation pages about it have been removed. If you need to refer to the outbound marketing documentation, it's available for [download here](https://download.microsoft.com/download/85f03905-daeb-4370-8abe-f5c75f27daf9/dynamics365-customer-insights-journeys-outbound-marketing.pdf). The password for the document is `Outbound(not-supported)`. This documentation is provided for archival purposes. No updates are being made to this content and it will be removed in the future without any further notice.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
