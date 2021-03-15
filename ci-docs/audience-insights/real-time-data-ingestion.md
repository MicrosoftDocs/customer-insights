---
title: "Real-time data ingestion and limitations"
description: "General information about real-time capabilities in audience insights."
ms.date: 10/27/2020
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: Nils-2m
ms.author: nikeller
manager: shellyha
---

# Real-time data ingestion (preview)

The near real-time functionality lets you see, within seconds, the latest interactions that your customers have made with your products or services.

[Scheduled refreshes](system.md#schedule-tab) include large numbers of records and several complex operations. First, data is pulled from the data source. Next, the data is unified, and then enriched with additional information. Every run of this process can take minutes to hours.

The real-time functionality provides data immediately for consumption, until the subsequent scheduled refresh pulls this data from the data source.

Real-time updates have an expiration time after which they no longer override the value from the data source:

- Profile updates will be kept for 4 hours
- Activities will be kept for 30 days

These values are API call parameters that you can change. They aim to ensure that your source data remains your source of truth. If you want real-time updates to be included for longer, you need to add them to a data source so they get pulled during the next scheduled refresh.

## Real-time update of the unified customer profile fields

Updated profiles will show in the customer card view, or any other visualization, within a few seconds.

Because real-time operations take place after the data unification has happened, they only apply to the unified customer profiles. Consequently, real-time profile changes will not update measures, segment membership, or enrichments.

### Limitations

- Customer profiles can be updated, but not created or deleted.
- Exporting real-time updates to external systems, like Power BI, is not possible at the moment.

## Real-time creation of activities

The real-time API lets you publish a new activity from your source system (an individual source record) to a unified customer profile. The new activity will be available as a unified activity in that unified customer profile's timeline within seconds. You can see the timeline in the customer card view or any other timeline integration you configured.

> [!NOTE]
>
> - Activities are immutable. They don't change once created.
> - Currently, segments and measures won't update based on the new activity.
> - Activities added only through the real-time API are not part of exports and won't show up in PowerBI.

There are two ways to connect to the real-time API:

- [indirectly](#connect-via-the-dynamics-365-customer-insights-connector), using the [Dynamics 365 Customer Insights connector](/connectors/customerinsights/)
- [directly](#connect-directly-to-the-real-time-api), with code

Both ways share the following prerequisites:

- A Customer Insights environment
- Unified customer profiles
- Activities configured and run
- Contributor or Administrator permissions to authenticate your account

## Connect via the Dynamics 365 Customer Insights connector

The real-time API can ingest data from a dedicated Power Platform connector, the [Dynamics 365 Customer Insights connector](/connectors/customerinsights/), without the need to write and deploy any code.    
The connector can do the same real-time actions as the API. You need a valid license for premium connectors. For more information, see [Power Apps and Power Automate licensing FAQs](/power-platform/admin/powerapps-flow-licensing-faq).

- Power Platform [Power Apps and/or Power Automate](/connectors/)
- Azure [Logic Apps](/azure/connectors/apis-list)

For details about creating flows, see the [Power Automate documentation](/power-automate/).

## Connect directly to the real-time API

You can use the real-time capabilities by building your own pipeline and connecting directly to the real-time API.    
You can post an activity in the format of your source system or in the UnifiedActivity format. Get the format by making an API call to /api/instances/{instanceId}/manage/entities/UnifiedActivity.

Details of this API, including parameters and responses, can be found in the **EntityData** section on the [Customer Insights APIs reference](https://developer.ci.ai.dynamics.com/api-details#api=CustomerInsights). For more information, see [Work with Customer Insights APIs](apis.md).

## Understand your real-time usage with telemetry

Get an overview of the volume of requests to the real-time API and information about issues the system may encounter. You can [access the real-time telemetry](system.md#api-usage-tab). 


[!INCLUDE[footer-include](../includes/footer-banner.md)]