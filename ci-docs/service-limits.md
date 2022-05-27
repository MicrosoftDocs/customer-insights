---
title: "Service limits in Dynamics 365 Customer Insights"
description: "Understand limits and restrictions."
ms.date: 05/28/2022

ms.subservice: audience-insights 
ms.topic: conceptual
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: mhart
manager: shellyha
---

# Service limits in Customer Insights

This article describes the built-in limits to the Customer Insights service, which are designed to ensure the reliability and stability of the service. Any requests for changes can be made through the [Ideas forum](https://go.microsoft.com/fwlink/?linkid=2074172). 

## Customer Insights

| Area  | Limits  | Notes |
|-------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| Segments, measures, and predictions | 300  | The total number of [segments](segments.md), [measures](measures.md), and [predictions](predictions.md) combined can't exceed 300.  |
| Relationships | 20 levels of depth on relationships in entity paths. | When creating [segments](segments.md) or [measures](measures.md) using the builder interface, entity paths can have up to 20 relationship hops between the start entity and the target entity.  |

## Fair scheduling of jobs

Customer Insights is a SaaS service that uses shared Azure resources. Customers tend to have workloads of variable intensity and on different schedules. To ensure fair access to the underlying resources, we make sure system processes are executed in fair order. Examples of system processes are jobs related to data unification, segment updates, or measure calculation. The fair scheduling protects you from queuing for resources if there's a spike of requested jobs. At the same time Customer Insights does not guarantee all jobs you queue are processed in parallel.

[!INCLUDE [footer-include](includes/footer-banner.md)]
