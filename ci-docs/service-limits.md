---
title: Service limits in Customer Insights
description: Understand limits and restrictions in the Customer Insights SaaS service.
ms.date: 11/23/2022
ms.topic: conceptual
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: mhart
---

# Service limits in Customer Insights

 Customer Insights has built-in limits designed to ensure the reliability and stability of the service. Any requests for changes can be made through the [Ideas forum](https://go.microsoft.com/fwlink/?linkid=2074172).

## Customer Insights

| Area  | Limits  | Notes |
|-------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| Segments and measures | 500  | The total number of active [segments](segments.md) and active [measures](measures.md) combined can't exceed 500 without potential performance degradation. For more information, see [Manage the number of active segments](segments.md#manage-the-number-of-active-segments) or [active measures](measures.md#manage-the-number-of-active-measures).|
| Relationships | 20 levels of depth on relationships in table paths. | When creating [segments](segments.md) or [measures](measures.md) using the builder interface, table paths can have up to 20 relationship hops between the start table and the target table.  |
|Data ingestion| Concurrent evaluations for Power Query data sources are limited. | Customer Insights has the same [refresh limits like Dataflows in PowerBI.com](/power-query/power-query-online-limits#refresh-limits). |

## Fair scheduling of jobs

Customer Insights is a SaaS service that uses shared Azure resources. Customers tend to have workloads of variable intensity and on different schedules. To ensure fair access to the underlying resources, we make sure system processes are executed in fair order. Examples of system processes are jobs related to data unification, segment updates, or measure calculation. The fair scheduling protects you from queuing for resources if there's a spike of requested jobs. At the same time, Customer Insights doesn't guarantee all jobs you queue are processed in parallel.

[!INCLUDE [footer-include](includes/footer-banner.md)]
