---
title: "Service limits"
description: "Understand limits and restrictions for Dynamics 365 Customer Insights."
ms.date: 08/31/2021
ms.service: customer-insights
ms.subservice: audience-insights 
ms.topic: conceptual
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: mhart
manager: shellyha
---

# Service limits for Dynamics 365 Customer Insights

This article describes the built-in limits to the Customer Insights service, which are designed to ensure the reliability and stability of the service. Any requests for changes can be made through the [Ideas forum](https://go.microsoft.com/fwlink/?linkid=2074172). 

## Customer insights limits
 
| Area  | Limits  | Notes |
|-------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| Segments and measures | 100 segments or measures. | The total number of active [segments](segments.md) and [measures](measures.md) combined can't exceed 100.  |
| Relationships | 20 levels of depth on relationships in entity paths. | When creating [segments](segments.md) or [measures](measures.md) using the builder interface, entity paths can have up to 20 relationship hops between the start entity and the target entity.  |

## Engagement insights limits

Engagement insights is a highly scalable application that can support millions of events per second. There is currently a limit to the number of events and workspaces allowed for an organization. <!--  Note for reviewers: This limit is for public preview, so will it change for GA? -->
 
- Maximum event volume per workspace  = 100 events per second

- Maximum number of workspaces per organization = 100

When events exceed the threshold, it can lead to loss of data in reports based on those events. You can [contact support](https://go.microsoft.com/fwlink/?linkid=2145734) to request a  volume increase before you exceed limits. We'll work with you to determine your need for a volume increase and support your request.

[!INCLUDE[footer-include](../includes/footer-banner.md)]