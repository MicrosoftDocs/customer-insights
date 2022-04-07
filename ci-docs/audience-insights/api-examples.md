---
title: "OData examples for the Dynamics 365 Customer Insights APIs"
description: "Commonly used examples of for the Open Data Protocol (OData) to query the Customer Insights APIs to review data."
ms.date: 04/07/2022
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
ms.reviewer: mhart
manager: shellyha
---

# OData query examples

The Open Data Protocol (OData) is a data access protocol built on core protocols like HTTP and commonly accepted methodologies like REST for the web. There are various kinds of libraries and tools can be used to consume OData services.

This article lists some frequently requested example queries to help you with building your own implementations based on the Customer Insights APIs.

You have to modify the query samples to make them work on the target environments: 

{serviceRoot}: https://api.ci.ai.dynamics.com/v1/instances/{instanceId} where {instanceId} is the GUID of the Customer Insights environment you want to query.
{CID}: GUID of a unified customer record. Example: ce759201f786d590bf2134bff576c369.
{PrimaryKey}: Identifier of the primary key of a customer record in a data source. Example: CNTID_1002
{DSname}: String with the entity name of a data source that gets ingested to Customer Insights. Example: Website_contacts.
{SegmentName}: String with the output entity name of a segment in Customer Insights. Example: Male_under_40.

> [!IMPORTANT]
> Auth?
> serviceRoot?
> how to get customer GUIDs, entity names, etc? Through UI?

## Customer

The following table contains a set of sample queries for the *Customer* collection.


|Query type |Example  | Note  |
|---------|---------|---------|
|Single customer ID     | {serviceRoot}/Customer?$filter=CustomerId eq '{CID}'          |  |
|Alternate key    | {serviceRoot}/Customer?$filter={DSname} eq '{PrimaryKey}'          |  Alternate keys persist in the unified customer entity       |
|Alternate key via CID     |  {serviceRoot}/Customer?$filter={DSname} eq '{CID}'       |         |
|Row4     |         |         |
|Row5     |         |         |
|Row6     |         |         |
|Row7     |         |         |
|Row8     |         |         |


## Search

## Segment membership

## Unified activity
