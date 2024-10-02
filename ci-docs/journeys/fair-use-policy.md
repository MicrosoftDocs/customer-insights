---
title: Service limits and fair use policy
description: Learn about usage limits and quotas in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/12/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Service limits and fair use policy

Dynamics 365 Customer Insights - Journeys relies on shared cloud resources for data and processing. This policy defines the limits for resource usage per org. These limits ensure that other tenants' performance isn't affected and resources are evenly distributed.

The following tables show the current usage limits for Customer Insights - Journeys features.

## Customer Insights - Journeys (real-time journeys)

| Feature              | Attribute                                                   | Maximum                                                    |
|----------------------|-------------------------------------------------------------|------------------------------------------------------------|
| Interaction sending  | Interactions sent (email, text, push).                      | 300,000,000 per month (10,000,000 daily max)†              |
| Interactions         | Number of interactions each month per interacted person owned.  | 10 interactions per interacted person owned (if you need more, increase the number of interacted people owned). |
| Data sync            | Number of rows in a single [synchronized table](./mkt-settings-sync.md) (for example, number of marketing contacts). | 500,000,000 rows |
| Interaction personalization | Number of distinct dynamic attributes used in a single message. | 100 |
| Interaction personalization | Number of [entity relationships connected](/dynamics365/customerengagement/on-premises/customize/create-edit-entity-relationships) in personalization. | Up to 6 levels of relationship traversal is supported (in the traversal path, there can be at most 1 relationship of type 1:N or N:M) |
| Segment limits | Total number of segments that can be created in real-time journeys. | 10,000 total segments (2,000 dynamic segments, 8,000 static segments) |
| Segment limits for journey start | Number of contacts, leads, and Customer Insights - Data profiles in a real-time journeys segment used to start a journey. | 10,000,000 members |
| Segment limits for journey branching | Number of contacts, leads, and Customer Insights - Data profiles in a real-time journeys segment used to branch in a journey. | 10,000,000 members |
| Throughput (for segment-based journeys) | Total number of interactions sent per unit of time. | Up to 500,000 interactions/hr‡ |
| Throughput (for trigger-based journeys) | Total number of triggers processed per unit of time. | Up to 2,500 triggers/min |
| Latency of trigger-based journeys | Time from when a trigger is activated to completing first step in the journey. | P90 < 3 minutes, P95 < 5 minutes with up to 2,500 triggers activated per minute.<br>Additional triggers activated for your environment are subject to slower processing and potential failures (dropped events). |
| Trigger inputs         | Number of input attributes in a single [custom trigger](./real-time-marketing-custom-triggers.md) | 29 |

*† Support for monthly interactions above 100 million is in preview. You can request to be part of the preview by reaching out to your Microsoft representative. See the [Throughput guidance](real-time-marketing-throughput-guidance.md) article for more details.*<br>
*‡ See the [Throughput guidance](real-time-marketing-throughput-guidance.md) article for more details.*

## Outbound marketing

| Feature               | Attribute                                              | Maximum                                                     |
|-----------------------|--------------------------------------------------------|-------------------------------------------------------------|
| Data sync  | Number of rows in a single [synchronized table](./mkt-settings-sync.md) (for example, number of marketing contacts). | 30,000,000 rows |
| Data sync  | Total rows across all [synchronized tables](./mkt-settings-sync.md).| 100,000,000 rows                                        |
| Email personalization | Number of dynamic attributes.                           | 1,000                                                       |
| Email personalization | Number of [entity relationships connected](/dynamics365/customerengagement/on-premises/customize/create-edit-entity-relationships) in personalization. | 1 entity relationship (for example, contact.account, contact.events)               |
| Email sending         | Interactions sent (email).                              | 10,000,000 per month (1,000,000 daily max)                  |
| Event registrations   | Number of event registrations processed simultaneously. | 60 event registrations per second 40 concurrent requests |
| Segmentation          | Number of live dynamic segments per org.                | 1,000 (both user defined and system created*)                |
| Segmentation          | Total number of segments.                               | 10,000                                                      |
| Segment-based journeys | Number of contacts and Customer Insights - Data profiles in a segment used in a customer journey. | 1,000,000 members |

> [!NOTE]
> System segments are created in three ways:
> 1. Whenever a unified segment is created (a behavior block plus a profile).
> 1. Whenever a journey uses multiple segments that will create a union of segments. For example, you can choose the source type and add multiple segments.
> 1. Whenever a behavior segment is used in journeys.

If you have questions or concerns about how to optimize your resources, contact [Microsoft support](/power-platform/admin/get-help-support).

[!INCLUDE [footer-include](./includes/footer-banner.md)]
