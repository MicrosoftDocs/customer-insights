---
title: Service limits in Dynamics 365 Customer Insights - Data
description: Understand limits and restrictions in the Customer Insights - Data application.
ms.date: 04/30/2024
ms.topic: article
author: JimsonChalissery
ms.author: jimsonc
ms.reviewer: mhart
---

# Service limits in Dynamics 365 Customer Insights - Data

 Customer Insights has built-in limits designed to ensure the reliability and stability of the service. Any requests for changes can be made through the [Ideas forum](https://go.microsoft.com/fwlink/?linkid=2074172).

## Customer Insights - Data

| Area  | Limits  | Notes |
|-------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| Segments and measures | 1,000  | The total number of active [segments](segments.md) and active [measures](measures.md) combined can't exceed 1,000 without potential performance degradation. For more information, see [Manage the number of active segments](segments.md#manage-the-number-of-active-segments) or [active measures](measures.md#manage-the-number-of-active-measures).|
| Calculated measures | 10 million rows in a measure copied to Dataverse. | If you want to create a [calculated measure](dataverse-measures.md) that is stored in Dataverse, break up the measure into multiple parts if it contains more than 10 million rows. |
| Relationships | 20 levels of depth on relationships in table paths. | When creating [segments](segments.md) or [measures](measures.md) using the builder interface, table paths can have up to 20 relationship hops between the start table and the target table.  |
|Data ingestion| Concurrent evaluations for Power Query data sources are limited. | Customer Insights - Data has the same [refresh limits like Dataflows in PowerBI.com](/power-query/power-query-online-limits#refresh-limits). |

## Fair scheduling of jobs

Customer Insights - Data is a SaaS service that uses shared Azure resources. Customers tend to have workloads of variable intensity and on different schedules. To ensure fair access to the underlying resources, we make sure system processes are executed in fair order. Examples of system processes are jobs related to data unification, segment updates, or measure calculation. The fair scheduling protects you from queuing for resources if there's a spike of requested jobs. At the same time, Customer Insights - Data doesn't guarantee all jobs you queue are processed in parallel.

[!INCLUDE [footer-include](includes/footer-banner.md)]
