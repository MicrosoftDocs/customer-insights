---
title: Real-time data ingestion (preview)
description: Ingest real-time data into Dynamics 365 Customer Insights - Data to surface the latest customer activities within seconds. Connect with the API or connector.
ms.date: 07/29/2026
ms.reviewer: v-wendysmith
ms.topic: article
author: Scott-Stabbert
ms.author: sstabbert
searchScope: 
  - ci-system-api-usage
  - customerInsights
---

# Real-time data ingestion (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

The near real-time functionality lets you see, within seconds, the latest interactions that your customers have made with your products or services.

[Scheduled refreshes](schedule-refresh.md) include large numbers of records and several complex operations. First, the process pulls data from the data source. Next, it unifies the data, and then enriches it with additional information. Every run of this process can take minutes to hours.

The real-time functionality provides data immediately for consumption, until the subsequent scheduled refresh pulls this data from the data source.

Real-time updates have an expiration time after which they no longer override the value from the data source:

- Profile updates expire after four hours
- Activities expire after 30 days

These values are API call parameters that you can change. They aim to ensure that your source data remains your source of truth. If you want real-time updates to last longer, add them to a data source so the next scheduled refresh pulls them.

 > [!TIP]
 > Any ingested or modified data by using these APIs reflects directly in the corresponding Dataverse tables. With this approach, you can leverage the rest of the Dataverse ecosystem and functionalities to achieve end-to-end business scenarios.

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Real-time update of the unified customer profile fields

Updated profiles show in the customer card view, or any other visualization, within a few seconds.

Because real-time operations take place after the data unification process, they only apply to the unified customer profiles. Consequently, real-time profile changes don't update measures, segment membership, or enrichments.

### Limitations

- You can update customer profiles but can't create or delete them.
- You can't export real-time updates to external systems, like Power BI.

## Real-time creation of activities

The real-time API enables you to publish a new activity from your source system (an individual source record) to a unified customer profile. The new activity appears as a unified activity in that unified customer profile's timeline within seconds. You can see the timeline in the customer card view or any other timeline integration you configured.

> [!NOTE]
>
> - Activities don't change once created.
> - Segments and measures don't update based on the new activity.
> - Activities added only through the real-time API aren't part of exports and don't show up in Power BI.

You can connect to the real-time API in two ways:

- [Indirectly](#dynamics-365-customer-insights---data-connection), by using the [Dynamics 365 Customer Insights connector](/connectors/customerinsights/)
- [Directly](#direct-connection-to-the-real-time-api), by using code

Both methods share the following prerequisites:

- A Customer Insights - Data environment
- Unified customer profiles
- Activities configured and run
- Contributor or Administrator permissions to authenticate your account

## Dynamics 365 Customer Insights - Data connection

The real-time API can ingest data from a dedicated Power Platform connector, the [Dynamics 365 Customer Insights connector](/connectors/customerinsights/), without the need to write and deploy any code.
The connector can perform the same real-time actions as the API. You need a valid license for premium connectors. For more information, see [Power Apps and Power Automate licensing FAQs](/power-platform/admin/powerapps-flow-licensing-faq).

- Power Platform [Power Apps and/or Power Automate](/connectors/)
- Azure [Logic Apps](/azure/connectors/apis-list)

For details about creating flows, see the [Power Automate documentation](/power-automate/).

## Direct connection to the real-time API

You can use the real-time capabilities by building your own pipeline and connecting directly to the real-time API.
You can post an activity in the format of your source system or in the UnifiedActivity format. Get the format by making an API call to `/api/instances/{instanceId}/manage/tables/UnifiedActivity`.

Details of this API, including parameters and responses, can be found in the **TableData** section on the [API reference](https://developer.ci.ai.dynamics.com/api-details#api=CustomerInsights). For more information, see [Work with APIs](apis.md).

[!INCLUDE [footer-include](includes/footer-banner.md)]
